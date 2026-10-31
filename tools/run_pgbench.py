# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on top of a database's own connection pooler (docs/POSTGRES_PREREGISTRATION.md).

PostgreSQL (the PostgreSQL Global Development Group) runs as the distribution ships it; PgBouncer (its own project) sits
in front of it in transaction pooling with the pool size it ships with, 20 server connections; pgbench (PostgreSQL's own
benchmark) offers the load. That is native: the pooler's fixed pool is the DBA's one setting, made once.

omni is the same database, the same pooler and the same load, with the compass law (omnicompass/compass_law.py) on
one knob: the pooler's pool size, written through its own admin console (SET default_pool_size), inside the cover
[2, 90]. The reading is the service time the pooler itself reports every second (transaction time plus the time clients
waited for a server, per transaction), or the share of its clients queued for a server scaled to the line, whichever is
larger (amendment 1), on a band from 0 to the response line. Past the wall the knob is handed back to
the pooler's own setting at once (fail up). At the end it is handed back and read back.

Load: pgbench at a fixed client count, rate-limited, the rate stepping one notch at a time (1 2 3 2 3 4 5 6 5 4 3 2 1 2
1) with the base rate set before the counted runs by one native-only run with no rate limit (the peak notch offers
native's own unlimited capacity). Both arms run the same steps, paired, the order alternating between repetitions.

Gauges (from pgbench's per-transaction log, PgBouncer's SHOW POOLS and the host's /proc/stat): work inside the
response line (transactions a second whose latency, lag included, was within the line), throughput, p50/p95/p99
latency, failed transactions, server connections alive (the "machines"), the host's CPU busy share and CPU-seconds.
There is no watt-meter on a GitHub runner: nothing here is an energy claim.

Amendment 2 (docs/POSTGRES_PREREGISTRATION.md, declared before the second counted set): the console is read over one
connection held for the whole arm (class Console, the server's own wire protocol) instead of a psql process launched for
every reading, which was about five launches a second in the omni arm at about 50 ms of CPU each and was the CPU the
first counted set charged to Omni; the queue line: a server is taken back (the calm give-back and the slow-inside-the-server
shrink alike) only while the pooler's clients waited for a server under one percent of its time in the last second and a
transaction was served, and while they waited one percent or more one server a second is added back, up to the pooler's own
setting; the harness's own CPU is recorded beside the host's.

Usage:
  python tools/run_pgbench.py --setup                      # create the bench role and database (needs the postgres user)
  python tools/run_pgbench.py --workloads tpcb --reps 3 --out out
  python tools/run_pgbench.py --report-only all --out all  # re-read finished <workload>.json files and write PGBENCH.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import resource
import shutil
import socket
import struct
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw, Plug, clamp  # noqa: E402
from tools.legal import stamp as _legal_stamp  # noqa: E402
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402  (amendment 3: the brain's own verdict)
from tools.readings import word as gel_word, aim as gel_aim, EVEN_SAME, EVEN_NOISE, SHOWN  # noqa: E402  (the words every table uses)

# --- the frozen rule -----------------------------------------------------------------------------------------------
LINE_MS = 50.0            # the response line: a transaction answered within 50 ms, lag included
CENTER = 0.4              # the compass pulls the service to 40% of the line (the service profile of the Kubernetes adapter)
DT = 1.0                  # one decision a second
TAU = 2.0                 # the pool's response time: a slot added or removed shows in the reading within a couple of seconds
SMOOTH = 0.5
DEAD = 0.05               # a force inside the cushion moves nothing
UP = 0.10                 # adding: ceil(force / UP) slots a second (full force adds ten); taking back: one idle server a second
PEAK = 0.9                # the peak notch offers nine tenths of native's unlimited capacity: native at its knee, not past it
DWELL_S = 30.0            # after adding, no taking back within thirty seconds (no hunting); adding is never held (amendment 1). Store fix of 25
                          # October: five seconds before; near saturation the brain gave a server back on a calm second and added it back 1 to
                          # 10 seconds later, 21 to 39 writes an arm in the omni-v16 tpcb_hot runs, each closing a server and opening a new one
FLOOR, CEILING = 2, 90    # the cover: never under two server connections; never within ten of PostgreSQL's 100 connections
NATIVE_POOL = 20          # PgBouncer's shipped default_pool_size: native's setting and Omni's snapshot
WAIT_SHARE = 0.5          # where the time goes decides the direction: waiting for a server (add one) or inside it (take one)
GIVEBACK_WAIT_SHARE = 0.01  # amendment 2: a server is taken back only while clients waited for one under 1% of the pooler's time in the
                            # last second (the pool holds the demand), the one line the three database tests share (misses under 1%)


def service_reading(latency_s, waiting_share, line_s=LINE_MS / 1000.0):
    """The reading the compass sees (amendment 1, docs/POSTGRES_PREREGISTRATION.md): the pooler's service time per
    transaction, or the share of its clients queued for a server scaled to the line, whichever is larger. A pool too small
    for the offered rate shows at the pooler as clients waiting, not as a long transaction: its own clock cannot see the
    backlog that piles up in the clients' schedules, and the first untouched run proved it."""
    return max(latency_s, waiting_share * line_s)

STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
WORKLOADS = {             # name: (pgbench script flag, scale factor)
    "tpcb": ("", 20),             # the tuning workload: pgbench's TPC-B-like default script, 20 branches
    "select": ("-S", 20),         # untouched: select-only, read-heavy
    "simple_update": ("-N", 20),  # untouched: the default script without the branch and teller updates
    "tpcb_hot": ("", 2),          # untouched: two branches, every transaction fights for the same rows
}
GAUGES = [  # key, label, direction
    ("work_inside_line_tps", "work inside the response line (transactions a second answered within the line)", "higher"),
    ("tps", "throughput (transactions a second)", "higher"),
    ("p95_ms", "latency, 95th percentile (ms, lag included)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("p50_ms", "latency, median (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "failed transactions", "never more"),
    ("servers_alive_mean", "server connections alive, mean (the machines)", "spent"),
    ("servers_alive_max", "server connections alive, most at once", "spent"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "spent"),
    ("cpu_seconds", "host CPU-seconds", "spent"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 transactions inside the line", "spent"),
    ("harness_cpu_seconds", "the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both; inside the host's)", "shown"),
    ("pool_mean", "pool size, mean (the knob)", "shown"),
]
from omnicompass.student_t import T95  # noqa: E402  (the two-sided 95% point of Student's t, any degrees of freedom)
SAME_REL = 1e-6


# --- pure pieces (tested without a database) -----------------------------------------------------------------------
def decide(p, force, wait_share, idle, cur, snapshot, last_dir, since_change_s, wall=0.95, queue_share=0.0, served=True):
    """The pool size the brain wants this second, by the frozen rule. Returns (target, direction, reason).

    Amendment 2, the queue line: `queue_share` is the share of the pooler's time its clients spent waiting for a server in
    the last second and `served` says whether it counted a transaction. A server is taken back (the calm give-back and the
    slow-inside-the-server shrink alike) only while a transaction was served and that share is under GIVEBACK_WAIT_SHARE;
    while it is at the line or above, servers are added back, one per percent of waiting, up to the pooler's own setting
    (the snapshot), so a take-back that put clients in the queue is undone the next second and a rising load gets its
    servers back at once. Above the pooler's own setting only slowness adds, by the force, as before; adding is never held."""
    if p >= wall:
        return snapshot, 0, "fail up: handed back to the pooler's own setting"
    if force > DEAD and wait_share >= WAIT_SHARE:
        d, why = math.ceil(force / UP), f"slow, clients waiting for a server: {math.ceil(force / UP)} more"
    elif not served:
        return cur, 0, "nothing served in the last second: nothing known, nothing moved"
    elif queue_share >= GIVEBACK_WAIT_SHARE:
        if cur < snapshot:
            d = min(snapshot - cur, max(1, math.ceil(queue_share / GIVEBACK_WAIT_SHARE)))   # one server per percent of waiting
            why = f"clients waited for a server {100 * queue_share:.1f}% of the time: {d} added back, up to the pooler's own setting"
        else:
            return cur, 0, "clients waited for a server (1% or more of the time) at the pooler's own setting or above: the pool is in demand, nothing taken"
    elif force > DEAD:
        d, why = -1, "slow inside the server: one fewer"
    elif force < -DEAD:
        if idle < 1:
            return cur, 0, "calm, but no idle server to give back"
        d, why = -1, "calm, an idle server given back"
    else:
        return cur, 0, "inside the cushion"
    sign = 1 if d > 0 else -1
    if sign < 0 and last_dir > 0 and since_change_s < DWELL_S:
        return cur, 0, f"dwell: no taking back within {DWELL_S:.0f} seconds of adding"   # gas is never held; only the brake dwells (amendment 1)
    target = int(clamp(cur + d, FLOOR, CEILING))
    if target == cur:
        return cur, 0, "at the cover"
    return target, sign, why


def parse_latencies(files):
    """Latencies (microseconds) from pgbench's per-transaction log files (-l): client transaction time script epoch us lag."""
    out = []
    for f in files:
        with open(f) as fh:
            for line in fh:
                parts = line.split()
                if len(parts) >= 3:
                    try:
                        out.append(int(parts[2]))
                    except ValueError:
                        continue
    return out


def parse_log_rows(files):
    """(epoch seconds, latency us, schedule lag us) of every transaction in pgbench's per-transaction log files (-l, with -R):
    client transaction time script epoch us [lag]."""
    out = []
    for f in files:
        with open(f) as fh:
            for line in fh:
                parts = line.split()
                if len(parts) >= 6:
                    try:
                        out.append((int(parts[4]) + int(parts[5]) / 1e6, int(parts[2]), int(parts[6]) if len(parts) >= 7 else 0))
                    except ValueError:
                        continue
    return out


def aggregate_per_second(rows, interval=1):
    """pgbench's own --aggregate-interval columns, one line a second, from the per-transaction rows (store fix of 25 October):
    interval_start num_transactions sum_latency sum_latency_2 min_latency max_latency sum_lag sum_lag_2 min_lag max_lag. pgbench
    writes either this or the per-transaction log, never both, and the gauges are read from the per-transaction log; so the runner
    writes the same aggregate from it before the raw log is removed, and every second of a stall stays in the run's files."""
    agg = {}
    for t, lat, lag in rows:
        k = int(t // interval) * interval
        a = agg.get(k)
        if a is None:
            agg[k] = [1, lat, lat * lat, lat, lat, lag, lag * lag, lag, lag]
        else:
            a[0] += 1; a[1] += lat; a[2] += lat * lat; a[3] = min(a[3], lat); a[4] = max(a[4], lat)
            a[5] += lag; a[6] += lag * lag; a[7] = min(a[7], lag); a[8] = max(a[8], lag)
    return [f"{k} " + " ".join(str(x) for x in agg[k]) for k in sorted(agg)]


def latency_gauges(lat_us, seconds, line_ms=LINE_MS):
    """The gauges one arm's transactions give over `seconds` of offered load."""
    n = len(lat_us)
    if n == 0:
        return {"transactions": 0, "tps": 0.0, "work_inside_line_tps": 0.0, "inside_line_share": 0.0,
                "p50_ms": float("nan"), "p95_ms": float("nan"), "p99_ms": float("nan"), "mean_ms": float("nan")}
    s = sorted(lat_us)
    q = lambda f: s[min(n - 1, int(math.ceil(f * n)) - 1)] / 1000.0  # noqa: E731
    inside = sum(1 for x in lat_us if x <= line_ms * 1000)
    return {"transactions": n, "tps": n / seconds, "work_inside_line_tps": inside / seconds,
            "inside_line_share": inside / n, "p50_ms": q(0.5), "p95_ms": q(0.95), "p99_ms": q(0.99),
            "mean_ms": sum(lat_us) / n / 1000.0}


def paired(reps, key, direction):
    """omni against native on one gauge over the repetitions: means, the mean paired difference, its 95% interval."""
    d = [r["omni"][key] - r["native"][key] for r in reps if _num(r["omni"].get(key)) and _num(r["native"].get(key))]
    if not d:
        return None
    n = len(d)
    nat = sum(r["native"][key] for r in reps) / n
    om = sum(r["omni"][key] for r in reps) / n
    mean = sum(d) / n
    if n > 1:
        sd = math.sqrt(sum((x - mean) ** 2 for x in d) / (n - 1))
        half = T95.get(n - 1, 1.96) * sd / math.sqrt(n)
    else:
        half = float("nan")
    lo, hi = mean - half, mean + half
    same = abs(mean) <= SAME_REL * max(abs(nat), 1e-12)
    clear = n > 1 and (lo > 0 or hi < 0) and not same
    if direction == "shown":
        reading = SHOWN
    elif direction == "never more" and any(x > 0 for x in d):
        reading = "**LOSS in a repetition**"                                     # any increase, in any repetition, whatever the noise
    elif same:
        reading = EVEN_SAME
    elif not clear:
        reading = EVEN_NOISE
    else:
        reading = gel_word(mean < 0, gel_aim(direction, key))      # the word by what the gauge is for, never by its sign
    return {"native": nat, "omni": om, "diff": mean, "ci95": [lo, hi], "n": n, "significant": clear, "reading": reading}


def _num(x):
    return isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))


# --- the wires -----------------------------------------------------------------------------------------------------
class Console:
    """One connection to PgBouncer's admin console, held for the whole arm, speaking the server's own wire protocol (the
    simple query of PostgreSQL's protocol, version 3). No process is started for a reading (amendment 2): the first counted
    set launched a psql process for every reading, about five a second in the omni arm, at about 50 ms of CPU each.
    `query` returns the rows as dicts of strings (none for a command such as SET) and reconnects once on a lost connection;
    the protocol parsing is in `parse_messages`, tested without a server."""

    PROTOCOL_3 = 196608
    ROW_DESCRIPTION_TAIL = 18                                   # after a field's name: table oid, column, type oid, length, modifier, format

    def __init__(self, host, port, user, password="", database="pgbouncer", timeout=5.0):
        self.host, self.port, self.user, self.password, self.database, self.timeout = host, port, user, password, database, timeout
        self.sock = None
        self.logins = 0
        self.lock = threading.Lock()                                # the sampler and the brain share the one connection, one query at a time

    # the wire
    def _send(self, kind: bytes, payload: bytes):
        self.sock.sendall(kind + struct.pack("!I", len(payload) + 4) + payload)

    def _recv_exact(self, n):
        buf = b""
        while len(buf) < n:
            chunk = self.sock.recv(n - len(buf))
            if not chunk:
                raise ConnectionError("the console closed the connection")
            buf += chunk
        return buf

    def _message(self):
        head = self._recv_exact(5)
        return head[:1], self._recv_exact(struct.unpack("!I", head[1:])[0] - 4)

    def connect(self):
        self.close()
        self.sock = socket.create_connection((self.host, self.port), timeout=self.timeout)
        params = f"user\0{self.user}\0database\0{self.database}\0\0".encode()
        self._send(b"", struct.pack("!I", self.PROTOCOL_3) + params)
        while True:
            kind, body = self._message()
            if kind == b"R":                                    # authentication: ok, cleartext password, md5 password
                code = struct.unpack("!I", body[:4])[0]
                if code == 0:
                    continue
                if code == 3:
                    self._send(b"p", self.password.encode() + b"\0"); continue
                if code == 5:
                    # the digest PostgreSQL's md5 method itself defines (its wire protocol), not a hash chosen for security
                    inner = hashlib.md5(self.password.encode() + self.user.encode(), usedforsecurity=False).hexdigest()
                    self._send(b"p", ("md5" + hashlib.md5(inner.encode() + body[4:8], usedforsecurity=False).hexdigest()).encode()
                               + b"\0"); continue
                raise ConnectionError(f"the console asked for authentication method {code}, which this client does not speak")
            if kind == b"E":
                raise ConnectionError(self.error_text(body))
            if kind == b"Z":                                    # ready for query: logged in ('S' parameters, 'K' key, 'N' notices skipped)
                break
        self.logins += 1

    def close(self):
        if self.sock is not None:
            try:
                self.sock.close()
            except OSError:
                pass
            self.sock = None

    @staticmethod
    def error_text(body: bytes):
        fields = {}
        for part in body.split(b"\0"):
            if part:
                fields[chr(part[0])] = part[1:].decode(errors="replace")
        return f"{fields.get('S', 'ERROR')}: {fields.get('M', '')}".strip()

    @classmethod
    def parse_messages(cls, messages):
        """Rows from the messages of one simple query, as the server sends them: 'T' names the columns, each 'D' is a row,
        'E' is an error (raised once 'Z' arrives), 'Z' ends the result. Messages are (kind, body) pairs."""
        cols, rows, err = [], [], None
        for kind, body in messages:
            if kind == b"T":
                n = struct.unpack("!H", body[:2])[0]; pos = 2; cols = []
                for _ in range(n):
                    end = body.index(b"\0", pos); cols.append(body[pos:end].decode()); pos = end + 1 + cls.ROW_DESCRIPTION_TAIL
            elif kind == b"D":
                n = struct.unpack("!H", body[:2])[0]; pos = 2; vals = []
                for _ in range(n):
                    ln = struct.unpack("!i", body[pos:pos + 4])[0]; pos += 4
                    if ln < 0:
                        vals.append(None)
                    else:
                        vals.append(body[pos:pos + ln].decode()); pos += ln
                rows.append(dict(zip(cols, vals)))
            elif kind == b"E":
                err = cls.error_text(body)
            elif kind == b"Z":
                if err:
                    raise RuntimeError(err)
                return rows
        raise ConnectionError("the console closed the connection before the result ended")

    def _messages_until_ready(self):
        while True:
            kind, body = self._message()
            yield kind, body
            if kind == b"Z":
                return

    def query(self, sql, retry=True):
        """The rows of one console command; one reconnect on a lost connection, never on a command the console refused."""
        with self.lock:
            return self._query(sql, retry)

    def _query(self, sql, retry):
        try:
            if self.sock is None:
                self.connect()
            self._send(b"Q", sql.encode() + b"\0")
            return self.parse_messages(self._messages_until_ready())
        except (OSError, ConnectionError, ValueError, struct.error, UnicodeDecodeError):   # a lost or garbled connection: once more, fresh
            self.close()
            if not retry:
                raise
            self.connect()
            return self._query(sql, retry=False)


class Bouncer:
    """PgBouncer as a child process with its own ini, its admin console read over one held connection (Console)."""

    def __init__(self, workdir: Path, port: int, pg: str, dbname: str, user: str, password: str):
        self.dir, self.port, self.user = workdir, port, user
        self.dir.mkdir(parents=True, exist_ok=True)
        self.as_postgres = os.geteuid() == 0           # PgBouncer refuses to run as root
        if self.as_postgres:                            # its folder is postgres's to write (log, pid, socket); never world-writable
            shutil.chown(self.dir, user="postgres")
            os.chmod(self.dir, 0o755)
        (self.dir / "userlist.txt").write_text(f'"{user}" "{password}"\n')
        self.ini = self.dir / "pgbouncer.ini"
        self.ini.write_text("\n".join([
            "[databases]", f"{dbname} = {pg} dbname={dbname} user={user} password={password}", "", "[pgbouncer]",
            "listen_addr = 127.0.0.1", f"listen_port = {port}", f"unix_socket_dir = {self.dir}", "auth_type = trust",
            f"auth_file = {self.dir / 'userlist.txt'}", f"admin_users = {user}", "pool_mode = transaction",
            f"default_pool_size = {NATIVE_POOL}", "max_client_conn = 1000", f"logfile = {self.dir / 'pgbouncer.log'}",
            f"pidfile = {self.dir / 'pgbouncer.pid'}", ""]))
        self.proc = None
        self.console = Console("127.0.0.1", port, user, password)

    def start(self):
        cmd = ["pgbouncer", "-d", str(self.ini)]
        if self.as_postgres:
            cmd = ["runuser", "-u", "postgres", "--"] + cmd
        subprocess.run(cmd, check=True)
        for _ in range(50):
            time.sleep(0.1)
            try:
                self.console.connect()
                self.console.query("SHOW VERSION", retry=False)
                return
            except (OSError, ConnectionError, RuntimeError):
                continue
        raise RuntimeError("PgBouncer did not come up")

    def admin(self, sql, quiet=False):
        """One console command; the rows, or None if the console refused it (said on stderr unless quiet)."""
        try:
            return self.console.query(sql)
        except (OSError, ConnectionError, RuntimeError) as e:
            if not quiet:
                sys.stderr.write(f"{sql}: {e}\n")
            return None

    def rows(self, sql):
        return self.console.query(sql)

    def pool_size(self):
        for r in self.rows("SHOW CONFIG"):
            if r.get("key") == "default_pool_size":
                return int(r["value"])
        raise RuntimeError("SHOW CONFIG gave no default_pool_size")

    def set_pool_size(self, n):
        self.console.query(f"SET default_pool_size = {int(n)}")

    def pools(self, dbname):
        for r in self.rows("SHOW POOLS"):
            if r.get("database") == dbname:
                return {k: int(v) for k, v in r.items() if k.startswith(("cl_", "sv_", "maxwait")) and v is not None and v.lstrip("-").isdigit()}
        return {}

    def stats(self, dbname):
        for r in self.rows("SHOW STATS"):
            if r.get("database") == dbname:
                return {k: int(v) for k, v in r.items() if k.startswith("total_") and v is not None and v.lstrip("-").isdigit()}
        return {}

    def stop(self):
        try:
            self.console.query("SHUTDOWN", retry=False)
        except (OSError, ConnectionError, RuntimeError):
            pass                                                # the console closes as it shuts down
        self.console.close()
        pid = self.dir / "pgbouncer.pid"
        for _ in range(30):
            if not pid.exists():
                return
            time.sleep(0.1)


class PoolPlug(Plug):
    """One wire in (the pooler's own service time per transaction), one wire out (its pool size)."""

    def __init__(self, b: Bouncer, dbname: str, line_ms=LINE_MS):
        super().__init__(FLOOR, CEILING, tolerance=0.5)
        self.b, self.db, self.line_s = b, dbname, line_ms / 1000.0
        self.prev = None
        self.wait_share = 0.0
        self.waiting_share = 0.0
        self.last_latency_s = 0.0
        self.last_pools = {}       # the SHOW POOLS row of the last reading, so the brain reads it once a second (amendment 2)
        self.queue_share = 0.0     # the share of the pooler's time its clients spent waiting for a server, last second (amendment 2)
        self.served = False        # whether the pooler counted a transaction in the last second (amendment 2)
        self.last_xacts = 0        # the transactions the pooler counted in the last second: the brain's work sample (amendment 3)

    def _read_service(self):
        s = self.b.stats(self.db)
        p = self.b.pools(self.db)
        self.last_pools = p
        clients = p.get("cl_active", 0) + p.get("cl_waiting", 0)
        self.waiting_share = p.get("cl_waiting", 0) / clients if clients else 0.0   # clients queued for a server (amendment 1)
        if not s:
            self.served, self.last_xacts = False, 0
            return service_reading(self.last_latency_s, self.waiting_share, self.line_s)
        if self.prev is None:
            self.prev = s
            self.served, self.last_xacts = False, 0
            return service_reading(0.0, self.waiting_share, self.line_s)
        dx = s["total_xact_count"] - self.prev["total_xact_count"]
        dt = s["total_xact_time"] - self.prev["total_xact_time"]
        dw = s["total_wait_time"] - self.prev["total_wait_time"]
        self.prev = s
        if dx <= 0:
            self.wait_share, self.last_latency_s = self.waiting_share, 0.0       # nothing served: calm unless clients are queued
            self.served, self.queue_share, self.last_xacts = False, (1.0 if dw > 0 else 0.0), 0
            return service_reading(0.0, self.waiting_share, self.line_s)
        self.served, self.last_xacts = True, dx
        self.queue_share = dw / (dt + dw) if (dt + dw) > 0 else 0.0
        self.wait_share = max(self.queue_share, self.waiting_share)
        self.last_latency_s = (dt + dw) / dx / 1e6
        return service_reading(self.last_latency_s, self.waiting_share, self.line_s)

    def _read_lever(self):
        return float(self.b.pool_size())

    def _send(self, value):
        self.b.set_pool_size(int(round(value)))


# omni-v22: the max on the pooler's pool (docs/POSTGRES_PREREGISTRATION.md, amendment 4): the wire's own rule (decide) with a server
# added while clients wait never clamped by an allowance, up to the cover, and the pool never taken below the pooler's own setting
# (native); the hand-back by the queue line (amendment 2) above it. The servers it holds are power given, shown beside the waiting
# they cut. `--dial save` keeps omni-v21's loop, the verdict under the resource objective, where giving servers back is the aim.
DIAL = os.environ.get("OMNI_DIAL", "max")


class Brain:
    """The knob's decision, one a second: obs holds reading_s (the pooler's service time per transaction, wait included),
    wait_share, idle (idle servers), pool (the pool size now), queue_share and served (amendment 2's queue line)."""

    def __init__(self, snapshot, objective=DEFAULT_OBJECTIVE, line_ms=LINE_MS):
        self.snapshot, self.objective = int(snapshot), objective
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.last_dir, self.last_change = 0, -1e9
        self.counts = {"spend": 0, "failups": 0, "handed_back": 0, "held_native": 0, "hold": 0}

    def step(self, t, obs):
        cur = int(obs["pool"])
        f = self.law.force(obs["reading_s"])
        want, d, why = decide(self.law.p, f, obs["wait_share"], obs["idle"], cur, self.snapshot, self.last_dir, t - self.last_change,
                              wall=self.law.band.wall_high, queue_share=obs.get("queue_share", 0.0), served=obs.get("served", True))
        if want > cur:
            target = want; self.counts["spend"] += 1                  # clients waiting for a server: never clamped, up to the cover
            if why.startswith("fail up"):
                self.counts["failups"] += 1
            why += "; power given inside the cover"
        elif want < cur:
            if want >= self.snapshot:
                target = want; self.counts["handed_back"] += 1
            elif cur > self.snapshot:
                target = self.snapshot; self.counts["handed_back"] += 1
                why = "calm: handed back to the pooler's own setting, never below it"
            else:
                target = cur; self.counts["held_native"] += 1
                why = f"hold: {cur} is the pooler's own setting; the max never goes below native"
        else:
            target = cur; self.counts["hold"] += 1
        if target != cur:                                             # the dwell runs from the last change, as the loop's own clock did
            self.last_dir, self.last_change = (0, t) if why.startswith("fail up") else ((target > cur) - (target < cur), t)
        info = {"verdict_phase": None, "verdict_direction": None, "allowed_low": None, "allowed_high": None, "dial": "max",
                "p": round(self.law.p, 4), "force": round(f, 4)}
        return target, why, info

    def record(self):
        return {"dial": "max", "objective": self.objective, "native": self.snapshot, "notch": 1, "cover": [FLOOR, CEILING],
                "state": "the max: a server added while clients wait, never clamped; never below the pooler's own setting; no allowance",
                "allowed_low": None, "allowed_high": None, "counts": dict(self.counts)}


class Omni(threading.Thread):
    """The brain, one decision a second, writing the audit. Under the max (omni-v22, the factory tune) the Brain above decides;
    under the tune-down (`--dial save`) amendment 3's loop (the brain's own verdict, 2026-10-09): the pool starts in
    watch and is written only inside the allowance a paired trial on the pooler itself has earned under the declared objective
    (tools/knob_verdict.py around the engine's own Verdict): one server fewer while calm, one more while clients wait, each step
    judged on the pooler's own second-by-second readings; a trial holds the pool; the fail-up back to the operator's setting is
    always free, a spend beyond the allowance never."""

    def __init__(self, plug: PoolPlug, audit_path: Path, line_ms=LINE_MS, objective=DEFAULT_OBJECTIVE, dial=DIAL):
        super().__init__(daemon=True)
        self.plug, self.audit, self.objective, self.dial = plug, audit_path, objective, dial
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event()
        self.last_dir, self.last_change = 0, -1e9
        self.writes, self.failups = 0, 0
        self.foreign, self.handed_back = False, False
        self.error = None                                           # a fault before the first decision, written into the arm's record
        self.verdict = None; self.brain = None

    def govern_record(self):
        """The record of what governed the knob: the max's counts (omni-v22) or the verdict's allowance (the tune-down)."""
        if self.brain is not None:
            return self.brain.record()
        return self.verdict.record() if self.verdict else None

    def run(self):
        try:
            snapshot = self.plug.attach()
        except Exception as e:                                      # the brain never ran: say so in the audit and the record, never silently
            self.error = repr(e)
            self.audit.write_text(json.dumps({"t": 0.0, "error": self.error, "note": "the brain could not attach; no decision was made"}) + "\n")
            return
        t0 = time.monotonic(); cpu_prev = cpu_times()
        self.verdict = KnobVerdict(int(snapshot), 1, (FLOOR, CEILING), objective=self.objective, settle_s=TAU)
        if self.dial == "max":
            self.brain = Brain(int(snapshot), self.objective); self.verdict = None
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    reading = self.plug.read()
                    f = self.law.force(reading)
                    idle = self.plug.last_pools.get("sv_idle", 0)              # the reading's own SHOW POOLS row (amendment 2)
                    cur = int(self.plug.lever())
                    cpu_now = cpu_times(); d_busy = cpu_now[0] - cpu_prev[0]; d_total = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
                    cpu_share = (d_busy / d_total) if d_total > 0 else None
                    cost = sample_cost(self.objective, self.plug.last_xacts, self.plug.last_latency_s if self.plug.served else None, cur, cpu_share)
                    if self.brain is not None:                                           # the max (omni-v22): the Brain keeps its own dwell clock
                        target, why, vinfo = self.brain.step(tick - t0, {"reading_s": reading, "wait_share": self.plug.wait_share, "idle": idle, "pool": cur,
                                                                          "queue_share": self.plug.queue_share, "served": self.plug.served})
                        fail_up = why.startswith("fail up")
                    else:                                                                # the tune-down: omni-v21's loop
                        self.verdict.observe(cost, tick - t0)                       # measured under the pool of the last second
                        target, d, why = decide(self.law.p, f, self.plug.wait_share, idle, cur, int(snapshot), self.last_dir,
                                                tick - self.last_change, wall=self.law.band.wall_high,
                                                queue_share=self.plug.queue_share, served=self.plug.served)
                        fail_up = why.startswith("fail up")
                        target, why, vinfo = self.verdict.decide(
                            target, spend_ok=(f > DEAD and self.plug.wait_share >= WAIT_SHARE),
                            give_ok=(f < -DEAD and self.plug.served and self.plug.queue_share < GIVEBACK_WAIT_SHARE and idle >= 1),
                            t=tick - t0, why=why, stress=f > DEAD, calm=f < -DEAD, fail_up=fail_up)
                    d = (target > cur) - (target < cur)
                    wrote = None
                    if target != cur:
                        wrote = self.plug.write(target)
                        self.writes += 1
                        if fail_up:
                            self.failups += 1
                            self.last_dir, self.last_change = 0, tick
                        else:
                            self.last_dir, self.last_change = d, tick
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3), "latency_ms": round(self.plug.last_latency_s * 1000, 3),
                                         "waiting_share": round(self.plug.waiting_share, 3), "p": round(self.law.p, 4),
                                         "force": round(f, 4), "wait_share": round(self.plug.wait_share, 3),
                                         "queue_share": round(self.plug.queue_share, 4), "served": self.plug.served, "idle": idle,
                                         "xacts_last_s": self.plug.last_xacts, "cpu_share": None if cpu_share is None else round(cpu_share, 4),
                                         "cost": None if cost is None else round(cost, 9), **vinfo,
                                         "pool": cur, "target": target, "wrote": wrote, "why": why}) + "\n")
                except Exception as e:  # a foreign writer or a lost console: say so, stop writing
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plug.restore()


class Sampler(threading.Thread):
    """Server connections alive, once a second, in both arms."""

    def __init__(self, b: Bouncer, dbname: str):
        super().__init__(daemon=True)
        self.b, self.db, self.stop_flag, self.alive, self.pool = b, dbname, threading.Event(), [], []

    def run(self):
        while not self.stop_flag.is_set():
            p = self.b.pools(self.db)
            if p:
                self.alive.append(sum(p.get(k, 0) for k in ("sv_active", "sv_idle", "sv_used", "sv_tested", "sv_login")))
            try:
                self.pool.append(self.b.pool_size())
            except Exception:
                pass
            time.sleep(DT)


def cpu_times():
    """(busy, total) jiffies of the whole host from /proc/stat."""
    with open("/proc/stat") as fh:
        parts = fh.readline().split()
    v = [int(x) for x in parts[1:]]
    idle = v[3] + (v[4] if len(v) > 4 else 0)
    return sum(v) - idle, sum(v)


def pgbench(args, env, log=None):
    r = subprocess.run(["pgbench"] + args, capture_output=True, text=True, env=env)
    if log is not None:
        log.write_text(r.stdout + r.stderr)
    return r


def parse_summary(text):
    out = {"tps": None, "failed": 0}
    for line in text.splitlines():
        if line.startswith("tps = "):
            out["tps"] = float(line.split("=")[1].split("(")[0])
        if line.startswith("number of failed transactions:"):
            out["failed"] = int(line.split(":")[1].split("(")[0])
    return out


# --- one workload --------------------------------------------------------------------------------------------------
def run_arm(arm, b, wl_dir, rep, dbname, user, port, script, steps, step_s, base, clients, jobs, line_ms, objective=DEFAULT_OBJECTIVE, prepare=None):
    d = wl_dir / f"rep-{rep}" / arm
    d.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PGPASSWORD": "x"}
    conn = ["-h", "127.0.0.1", "-p", str(port), "-U", user]
    assert b.pool_size() == NATIVE_POOL, "every arm starts from the pooler's own setting"
    prep = prepare(d) if prepare is not None else None             # store fix of 25 October: the tables re-initialised and a CHECKPOINT, both arms alike
    # an uncounted warm-up at the base rate, both arms alike
    pgbench(conn + ["-c", str(clients), "-j", str(jobs), "-T", "5", "-R", f"{base:.1f}", "-n"] + script + [dbname], env)
    sampler = Sampler(b, dbname); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(PoolPlug(b, dbname, line_ms), d / "audit.jsonl", line_ms, objective); omni.start()
    cpu0, t0 = cpu_times(), time.monotonic()
    own0 = resource.getrusage(resource.RUSAGE_SELF)
    lat, failed, per_step = [], 0, []
    for k, notch in enumerate(steps):
        rate = base * notch
        prefix = d / f"step-{k:02d}"
        r = pgbench(conn + ["-c", str(clients), "-j", str(jobs), "-T", str(step_s), "-R", f"{rate:.1f}", "-n", "-l",
                           f"--log-prefix={prefix}"] + script + [dbname], env, d / f"step-{k:02d}.txt")
        s = parse_summary(r.stdout)
        files = sorted(d.glob(f"step-{k:02d}.*[0-9]"))
        l = parse_latencies(files)
        (d / f"step-{k:02d}.agg").write_text("\n".join(aggregate_per_second(parse_log_rows(files))) + "\n")   # every second of the step kept
        g = latency_gauges(l, step_s, line_ms)
        per_step.append({"step": k, "notch": notch, "offered_tps": rate, **g, "failed": s["failed"], "exit": r.returncode})
        lat += l; failed += s["failed"]
        for f in files:
            f.unlink()                                             # the per-step gauges are kept; the raw log is large
    seconds = time.monotonic() - t0
    cpu1 = cpu_times()
    own1 = resource.getrusage(resource.RUSAGE_SELF)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    g = latency_gauges(lat, step_s * len(steps), line_ms)
    g.update({"failed": failed, "seconds": seconds, "prepared": prep,
              "harness_cpu_seconds": (own1.ru_utime + own1.ru_stime) - (own0.ru_utime + own0.ru_stime),
              "console_logins": b.console.logins,
              "servers_alive_mean": sum(sampler.alive) / len(sampler.alive) if sampler.alive else float("nan"),
              "servers_alive_max": max(sampler.alive) if sampler.alive else float("nan"),
              "cpu_busy_share": (cpu1[0] - cpu0[0]) / max(1, cpu1[1] - cpu0[1]),
              "cpu_seconds": (cpu1[0] - cpu0[0]) / os.sysconf("SC_CLK_TCK"),
              "pool_mean": sum(sampler.pool) / len(sampler.pool) if sampler.pool else float("nan"),
              "pool_min": min(sampler.pool) if sampler.pool else None, "pool_max": max(sampler.pool) if sampler.pool else None,
              "steps": per_step})
    inside = g["work_inside_line_tps"] * step_s * len(steps)
    g["cpu_s_per_1k_inside"] = g["cpu_seconds"] / inside * 1000 if inside else float("nan")
    if omni is not None:
        omni.stop_flag.set(); omni.join(timeout=10)
        g.update({"writes": omni.writes, "fail_ups": omni.failups, "handed_back": bool(omni.handed_back),
                  "foreign_writer": omni.foreign, "controller_error": omni.error, "pool_read_back": b.pool_size(),
                  "verdict": omni.govern_record()})
    else:
        g.update({"writes": 0, "handed_back": True, "pool_read_back": b.pool_size()})
    if b.pool_size() != NATIVE_POOL:                             # belt and braces: the next arm starts native
        b.set_pool_size(NATIVE_POOL)
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    return g


def run_workload(name, out, pg, dbname, user, password, port, reps, steps, step_s, clients, jobs, calib_s, line_ms, objective=DEFAULT_OBJECTIVE):
    script_flag, scale = WORKLOADS[name]
    script = [script_flag] if script_flag else []
    wl_dir = out / f"pgbench-{name}"
    wl_dir.mkdir(parents=True, exist_ok=True)
    env = {**os.environ, "PGPASSWORD": password}
    direct = ["-h", pg_host(pg), "-p", pg_port(pg), "-U", user]
    r = pgbench(direct + ["-i", "-s", str(scale), "-q", dbname], env, wl_dir / "init.txt")
    if r.returncode != 0:
        raise SystemExit(f"pgbench -i failed: {r.stderr[-400:]}")
    b = Bouncer(wl_dir / "pgb", port, pg, dbname, user, password)
    b.start()
    try:
        snapshot = b.pool_size()
        assert snapshot == NATIVE_POOL
        # the base rate: native's own unlimited capacity, found once before the counted runs, over the peak notch
        cal = pgbench(["-h", "127.0.0.1", "-p", str(port), "-U", user, "-c", str(clients), "-j", str(jobs), "-T", str(calib_s), "-n"]
                      + script + [dbname], {**os.environ, "PGPASSWORD": "x"}, wl_dir / "calibration.txt")
        cap = parse_summary(cal.stdout)["tps"]
        if not cap:
            raise SystemExit(f"calibration gave no tps: {cal.stderr[-300:]}")
        base = PEAK * cap / max(steps)
        print(f"== {name}: native capacity {cap:.0f} tps unlimited; base rate {base:.0f} tps (peak notch {100 * PEAK:.0f}% of it); steps {steps}", flush=True)
        rec = {"workload": name, "script": script_flag or "tpcb (default)", "scale": scale, "line_ms": line_ms, "steps": steps,
               "step_s": step_s, "clients": clients, "jobs": jobs, "native_capacity_tps": cap, "base_tps": base,
               "snapshot_pool": snapshot, "cover": [FLOOR, CEILING], "center": CENTER, "objective": objective, "dial": DIAL, "engine": engine(), "reps": []}
        prepare = lambda d: reset_tables(pg, dbname, user, password, scale, d)   # noqa: E731  (the same state before every arm)
        for rep in range(1, reps + 1):
            order = ["native", "omni"] if rep % 2 else ["omni", "native"]
            one = {"rep": rep, "order": order}
            for arm in order:
                one[arm] = run_arm(arm, b, wl_dir, rep, dbname, user, port, script, steps, step_s, base, clients, jobs, line_ms, objective, prepare=prepare)
                print(f"== {name} rep {rep} {arm}: inside the line {one[arm]['work_inside_line_tps']:.0f} tps, p95 {one[arm]['p95_ms']:.1f} ms, "
                      f"servers {one[arm]['servers_alive_mean']:.1f}, pool {one[arm]['pool_mean']:.1f}, CPU {100 * one[arm]['cpu_busy_share']:.0f}%", flush=True)
            rec["reps"].append(one)
            (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
        rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
        return rec
    finally:
        b.stop()


def checkpoint_command(dbname):
    """CHECKPOINT as the postgres superuser (the bench role holds no right to it), the way --setup reaches the server."""
    pre = ["runuser", "-u", "postgres", "--"] if os.geteuid() == 0 else ["sudo", "-n", "-u", "postgres"]
    return pre + ["psql", "-qX", "-d", dbname, "-c", "CHECKPOINT"]


def reset_tables(pg, dbname, user, password, scale, d, run=subprocess.run):
    """Before every arm, both arms alike (store fix of 25 October): pgbench's tables re-initialised at the workload's scale and
    a CHECKPOINT, so each arm starts from the same tables and the same point in the checkpoint cycle (the omni-v16 runs
    initialised once a workload and ran six arms, about 45 minutes, on the growing tables, the checkpoints falling wherever
    they fell). Returns what was done, for the arm's record."""
    env = {**os.environ, "PGPASSWORD": password}
    direct = ["-h", pg_host(pg), "-p", pg_port(pg), "-U", user]
    t0 = time.monotonic()
    r = run(["pgbench"] + direct + ["-i", "-s", str(scale), "-q", dbname], capture_output=True, text=True, env=env)
    c = run(checkpoint_command(dbname), capture_output=True, text=True)
    (Path(d) / "prepare.txt").write_text((r.stdout or "") + (r.stderr or "") + "\n" + (c.stdout or "") + (c.stderr or ""))
    return {"reinit_exit": r.returncode, "checkpoint_exit": c.returncode, "seconds": round(time.monotonic() - t0, 2)}


def pg_host(pg):
    return dict(kv.split("=", 1) for kv in pg.split()).get("host", "127.0.0.1")


def pg_port(pg):
    return dict(kv.split("=", 1) for kv in pg.split()).get("port", "5432")


def engine():
    try:
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    except Exception:
        sha = ""
    try:
        v = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], cwd=ROOT, capture_output=True, text=True)
        ver = v.stdout.strip().splitlines()[0] if v.stdout.strip() else "unknown"
    except Exception:
        ver = "unknown"
    return {"commit": sha, "version": ver}


# --- the report ----------------------------------------------------------------------------------------------------
def pct(r, key):
    if r is None:
        return "no value"
    nat, diff, lo, hi = r["native"], r["diff"], r["ci95"][0], r["ci95"][1]
    if key in ("failed",) or not nat:
        return f"{diff:+.3g} ({lo:+.3g} to {hi:+.3g})"
    return f"{100 * diff / abs(nat):+.1f}% ({100 * lo / abs(nat):+.1f} to {100 * hi / abs(nat):+.1f})"


def fmt(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return f"{v:.3g}" if abs(v) < 10 else f"{v:,.1f}" if abs(v) < 1000 else f"{v:,.0f}"


def report(recs, out: Path):
    L = ["# PostgreSQL behind PgBouncer: native and omni (Omni-Compass on top of the pooler's own pool size)", "",
         "Native is PostgreSQL as shipped behind PgBouncer's shipped pool of 20 server connections; omni is the same with the compass law "
         f"writing the pool size through PgBouncer's own console inside [{FLOOR}, {CEILING}], handed back at the end. The load is pgbench, "
         "rate-limited, stepping one notch at a time, the peak notch offering native's own unlimited capacity. Every row is shown, losses "
         "included; a 95% interval of the paired difference (omni minus native) over the repetitions decides whether a change is beyond the "
         "noise. There is no watt-meter on the machine: the host's CPU-seconds are measured, no energy is claimed "
         "(`docs/POSTGRES_PREREGISTRATION.md`).", ""]
    for rec in recs:
        e = rec.get("engine", {})
        L += [f"## {rec['workload']} ({rec['script']}, scale {rec['scale']}): line {rec['line_ms']:.0f} ms, {len(rec['reps'])} paired repetitions", "",
              f"Native capacity, unlimited: {rec['native_capacity_tps']:,.0f} tps; base rate {rec['base_tps']:,.0f} tps; steps {rec['steps']} × {rec['step_s']} s; "
              f"{rec['clients']} clients. Engine {e.get('version', 'unknown')} at `{e.get('commit', '')[:12]}`.", "",
              "| Gauge | native | omni | change (95% interval) | reading |", "|---|---:|---:|---|---|"]
        for k, label, dr in GAUGES:
            r = (rec.get("paired") or {}).get(k)
            if r is None:
                continue
            L.append(f"| {label} | {fmt(r['native'])} | {fmt(r['omni'])} | {pct(r, k)} | {r['reading']} |")
        hb = all(x["omni"].get("handed_back") for x in rec["reps"])
        fw = any(x["omni"].get("foreign_writer") for x in rec["reps"])
        L += ["", f"The knob handed back and read back at the end of every omni arm: {'yes' if hb else '**NO**'}; "
              f"a foreign writer seen: {'**yes**' if fw else 'no'}; Omni's writes per arm: "
              + ", ".join(str(x["omni"].get("writes", 0)) for x in rec["reps"])
              + "; fail-ups per arm: " + ", ".join(str(x["omni"].get("fail_ups", 0)) for x in rec["reps"]) + ".", "",
              "Per repetition (inside the line tps / p95 ms / servers alive / pool mean):", ""]
        for x in rec["reps"]:
            n, o = x["native"], x["omni"]
            L.append(f"- rep {x['rep']} ({' then '.join(x['order'])}): native {n['work_inside_line_tps']:.0f} / {n['p95_ms']:.1f} / "
                     f"{n['servers_alive_mean']:.1f} / {n['pool_mean']:.1f}; omni {o['work_inside_line_tps']:.0f} / {o['p95_ms']:.1f} / "
                     f"{o['servers_alive_mean']:.1f} / {o['pool_mean']:.1f}")
        L.append("")
    (out / "PGBENCH.md").write_text("\n".join(_legal_stamp(L)) + "\n")


def setup(pg, dbname, user, password):
    """The bench role and database, through the postgres superuser."""
    pre = ["runuser", "-u", "postgres", "--"] if os.geteuid() == 0 else ["sudo", "-u", "postgres"]
    sql = (f"DO $$ BEGIN IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname='{user}') THEN CREATE ROLE {user} LOGIN PASSWORD '{password}'; "
           f"END IF; END $$;")
    subprocess.run(pre + ["psql", "-qc", sql], check=True)
    have = subprocess.run(pre + ["psql", "-tAc", f"SELECT 1 FROM pg_database WHERE datname='{dbname}'"], capture_output=True, text=True).stdout.strip()
    if have != "1":
        subprocess.run(pre + ["createdb", "-O", user, dbname], check=True)
    print(f"role {user} and database {dbname} ready")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--workloads", default="tpcb")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--steps", default=STEPS)
    ap.add_argument("--step-s", type=int, default=20)
    ap.add_argument("--clients", type=int, default=64)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--calib-s", type=int, default=20)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--pg", default="host=127.0.0.1 port=5432")
    ap.add_argument("--dbname", default="bench")
    ap.add_argument("--user", default="bench")
    ap.add_argument("--password", default="bench")
    ap.add_argument("--port", type=int, default=6543, help="the port our PgBouncer listens on")
    ap.add_argument("--out", default="out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a step by: resource (the index's reading: work, speed, connections and CPU together) or service (work and speed alone)")
    ap.add_argument("--report-only", default="")
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--smoke", action="store_true", help="a one-minute pass: short steps, one repetition")
    a = ap.parse_args(argv)
    if a.setup:
        setup(a.pg, a.dbname, a.user, a.password)
        return 0
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).glob("pgbench-*/*.json"))]
        recs = [r for r in recs if "reps" in r]
        for r in recs:
            r["paired"] = {k: paired(r["reps"], k, dr) for k, _, dr in GAUGES}
        report(recs, out)
        return 0
    for tool in ("pgbench", "psql", "pgbouncer"):
        if shutil.which(tool) is None:
            raise SystemExit(f"{tool} not found")
    steps = [int(x) for x in a.steps.split()]
    if a.smoke:
        a.reps, a.step_s, a.calib_s, steps = 1, 4, 4, [1, 2, 3, 2, 1]
    recs = []
    for name in a.workloads.split(","):
        if name not in WORKLOADS:
            raise SystemExit(f"unknown workload {name}; one of {sorted(WORKLOADS)}")
        recs.append(run_workload(name, out, a.pg, a.dbname, a.user, a.password, a.port, a.reps, steps, a.step_s, a.clients, a.jobs,
                                 a.calib_s, a.line_ms, a.objective))
    report(recs, out)
    print(f"report: {out / 'PGBENCH.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
