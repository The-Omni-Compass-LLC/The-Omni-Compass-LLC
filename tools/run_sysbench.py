#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on top of a database's operator-set buffer pool: sysbench on MySQL (docs/MYSQL_PREREGISTRATION.md).

MySQL 8.0 as Ubuntu ships it, with the one setting an operator sets once for InnoDB: the buffer pool size, which the server
resizes online in chunks of 128 MB. sysbench's published OLTP workloads ask for rows from a set of tables that widens and
narrows over the run (one notch = one more table of a million rows), so the working set steps through the operator's pool
and past it. The operator's fixed pool is the native controller here.

  native  MySQL at the operator's pool (512 MB) for the whole run
  omni    the same MySQL, with the compass law (omnicompass/compass_law.py) on one knob, the buffer pool size, through the
          server's own console (SET GLOBAL innodb_buffer_pool_size), inside the cover [128 MB, 2,048 MB]: the compass reads the
          workload's own mean statement latency over the last second (performance_schema, sysbench's account only, its prepared
          statements counted; store fix of 25 October) on a band from 0 to the statement
          line and holds it at 40% of the line; slow statements with the pool full push the pool up a chunk or more (slow
          statements with room to spare are not the pool's to mend), calm with the pool's misses under one percent of its read requests gives a chunk back
          (amendment 2: the pool grows only while it is missing, one percent or more, the same line the other way; a second
          with no read request moves nothing)
          after a dwell; at 95% of the line with the pool full four chunks are added at once (fail up); the pool is handed back
          to the operator's at the end and read back; a size found at a value Omni did not write stops it writing

Gauges from sysbench's own latency histogram and summary (every transaction counted into buckets about 2% wide), the server's
own status (the pool configured, the pages in it, the pages read from disk) and the host's /proc/stat (CPU seconds, the
compass's own cost included). Memory held is the resource; no energy is claimed beyond the host's CPU seconds. Every row is
reported, losses included.

  python3 tools/run_sysbench.py --setup                    # the benchmark user, the operator's pool in the server's own
                                                           # configuration file, the server restarted
  python3 tools/run_sysbench.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_sysbench.py --report-only DIR          # re-read finished <workload>.json files and write SYSBENCH.md
"""
from __future__ import annotations

import argparse
import json
import math
import os
import re
import subprocess
import sys
import threading
import time
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402
from tools.run_ycsb import cpu_times, engine, fmt, paired  # noqa: E402  (the same paired reading and host clock as the other stores)
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402  (amendment 3: the brain's own verdict)
from tools.store_brain import MemoryMax, read_meminfo  # noqa: E402  (omni-v22: the max on the pool)

HOST = os.environ.get("MYSQL_HOST", "127.0.0.1")
USER = os.environ.get("MYSQL_USER", "omni")
PASSWORD = os.environ.get("MYSQL_PWD", "omni-bench")       # a local benchmark user on a throwaway runner, created by --setup
LOAD_USER = os.environ.get("SYSBENCH_USER", "omni_load")   # the account sysbench connects as, apart from the harness's (store fix of 25 October):
                                                           # the brain reads the statements of this account only, never its own monitoring queries
# The statements the brain reads (store fix of 25 October): sysbench 1.0.20 runs its OLTP scripts as server-side prepared
# statements, which the performance schema counts as statement/com/Execute (the binary protocol's execute) or
# statement/sql/execute_sql (an SQL-level EXECUTE), not as statement/sql/select and the other three. The omni-v16 runs read
# only those four, so the brain counted 4.1 statements a second in every arm (its own and the sampler's monitoring SELECTs)
# while sysbench sent 994 to 4,839 queries a second: its force and the verdict's work sample never saw the workload.
WORKLOAD_EVENTS = ("statement/sql/select", "statement/sql/update", "statement/sql/insert", "statement/sql/delete",
                   "statement/com/Execute", "statement/sql/execute", "statement/sql/execute_sql")
DB = "sbtest"
MB = 1024 * 1024
PAGE = 16 * 1024          # InnoDB's page
LINE_STMT_MS = 0.6        # the statement line: one SQL statement answered within 0.6 ms on the server (written as 1 ms; set on the tuning
                          # workload's smoke runs: a hit reads 0.14 to 0.22 ms on GitHub's runners and a notch missing a third of its reads
                          # 0.05 to 0.06 ms more, so the center, 40% of the line, sits at 0.24 ms, above the hits and under the misses)
GIVEBACK_MISS_SHARE = 0.01  # a chunk is given back only while the pool's misses are under 1% of its read requests (the pool holds the working
                          # set); InnoDB keeps stale pages resident, so "pages free" and "no page read from disk" never say that
CENTER = 0.4              # the compass holds the server's own statement latency at 40% of the line
DT = 1.0                  # one decision a second
TAU = 2.0
SMOOTH = 0.5
NATIVE_MB = 512           # the operator's pool
OPERATOR_MB, SHIPPED_MB = 512, 128   # --native operator (preregistered) or shipped (MySQL 8.0's own default pool, 128 MB)
NATIVE = "operator"
CHUNK_MB = 128            # innodb_buffer_pool_chunk_size as shipped: the pool is resized in whole chunks
COVER_MB = (128, 2048)    # never under one chunk, never over 2 GB
STEP_MB = CHUNK_MB        # one notch of the knob is one chunk
FAILUP_MB = 512           # past the wall: four chunks at once (about a quarter of the cover), and again the next second if still past it
DWELL_S = 10.0            # after growing, no taking back within ten seconds (a shrink evicts pages and the resize itself takes seconds)
DIAL = os.environ.get("OMNI_DIAL", "max")   # omni-v22: max, the factory tune (the Brain); save, the tune-down (omni-v21's loop)
FULL = 0.9                # the pool counts as full when the pages holding data are 90% of its pages or more
THREADS = 32              # sysbench's client threads
TABLES = 6                # tables prepared; notch n uses the first n
TABLE_ROWS = 1_000_000    # rows a table: about 240 MB of data and index each, so notch 1 fits the operator's pool and notch 6 does not
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
RESIZE_WAIT_S = 90.0      # the server's online resize is asynchronous; the plug waits this long for it to complete
RAND_TYPE = "uniform"     # rows drawn uniformly over the tables in use, so the working set is the key space (sysbench's shipped 'special'
                          # draw sends three quarters of the requests to one percent of the rows: the first smoke run showed the pool
                          # filling only at the top notch and misses at 3.5% of reads, nothing for the knob to answer; see the preregistration)
SAME_REL = 1e-6
LUA = Path(os.environ.get("SYSBENCH_LUA", "/usr/share/sysbench"))

WORKLOADS = {
    # name: (sysbench script, statements a transaction as the script ships, transactions a second offered (--rate), steps, tuning?)
    #   the transaction line for the work-inside-the-line gauge is the statement line times the statements a transaction
    "tuning": ("oltp_point_select", 1, 3000, STEPS, True),       # one point select a transaction: the rules were set here
    "read_only": ("oltp_read_only", 14, 300, STEPS, False),      # 10 point selects and 4 range queries a transaction
    "read_write": ("oltp_read_write", 18, 200, STEPS, False),    # the read-only mix plus 2 updates, a delete and an insert
    "update_index": ("oltp_update_index", 1, 1000, STEPS, False),  # one indexed update a transaction
    "burst": ("oltp_read_only", 14, 300, BURST, False),          # read-only on the burst schedule
}

GAUGES = [  # key, label, direction
    ("work_inside_line_tps", "work inside the response line (transactions a second answered within the line)", "higher"),
    ("tps", "throughput (transactions a second)", "higher"),
    ("qps", "queries a second", "higher"),
    ("p95_ms", "latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "errors (sysbench's ignored errors: deadlocks and retries)", "never more"),
    ("pool_mb_mean", "buffer pool held, mean (MB; the knob, the resource)", "spent"),
    ("pool_used_mb_mean", "pages holding data, mean (MB)", "spent"),
    ("disk_reads", "pages read from disk into the pool (misses)", "shown"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "spent"),
    ("cpu_seconds", "host CPU-seconds", "spent"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 transactions inside the line", "spent"),
    ("writes", "buffer pool size changes written (the knob's moves)", "shown"),
]


def connect():
    import pymysql
    return pymysql.connect(host=HOST, user=USER, password=PASSWORD, autocommit=True, connect_timeout=5)


def query(conn, sql):
    with conn.cursor() as cur:
        cur.execute(sql)
        return cur.fetchall()


def status(conn):
    """The server's own figures, one read: {name: value} from SHOW GLOBAL STATUS for the pool and the statements' timer."""
    rows = query(conn, "SHOW GLOBAL STATUS WHERE Variable_name IN ('Innodb_buffer_pool_pages_total', 'Innodb_buffer_pool_pages_data', "
                       "'Innodb_buffer_pool_pages_free', 'Innodb_buffer_pool_reads', 'Innodb_buffer_pool_read_requests', 'Innodb_buffer_pool_resize_status')")
    st = {k: v for k, v in rows}
    st["pool_bytes"] = int(query(conn, "SELECT @@innodb_buffer_pool_size")[0][0])
    t = query(conn, workload_statements_sql())[0]
    st["stmt_timer_ps"], st["stmt_count"] = int(t[0]), int(t[1])
    f = query(conn, FILE_READS_SQL)[0]
    st["file_reads"], st["file_read_ps"] = int(f[0]), int(f[1])
    return st


# omni-v22: the server's own account of what a pool miss costs: the performance schema's timer on the data files' reads (every
# page the pool did not hold and had to read, read-ahead included), in picoseconds, beside the workload's own statement timer.
# The instrument wait/io/file/innodb/innodb_data_file is enabled and timed as MySQL 8.0 ships (checked on 8.0.46).
FILE_READS_SQL = ("SELECT COALESCE(SUM(COUNT_READ), 0), COALESCE(SUM(SUM_TIMER_READ), 0) FROM performance_schema.file_summary_by_event_name "
                  "WHERE EVENT_NAME = 'wait/io/file/innodb/innodb_data_file'")


def file_reads(st):
    """(data file reads, their time in picoseconds) from one status read."""
    return st["file_reads"], st["file_read_ps"]


def workload_statements_sql(user=None):
    """The workload's statement timer and count: sysbench's own account only (the harness's monitoring queries run as another
    account and are never read), its plain and prepared statements alike (WORKLOAD_EVENTS)."""
    user = LOAD_USER if user is None else user
    events = ", ".join(f"'{e}'" for e in WORKLOAD_EVENTS)
    return ("SELECT COALESCE(SUM(SUM_TIMER_WAIT), 0), COALESCE(SUM(COUNT_STAR), 0) FROM performance_schema.events_statements_summary_by_user_by_event_name "
            f"WHERE USER = '{user}' AND EVENT_NAME IN ({events})")


def pool_stats(st):
    """(configured MB, pages holding data MB, pages read from disk, resize status text) from one status read."""
    return st["pool_bytes"] // MB, int(st.get("Innodb_buffer_pool_pages_data", 0)) * PAGE / MB, int(st.get("Innodb_buffer_pool_reads", 0)), str(st.get("Innodb_buffer_pool_resize_status", ""))


def read_requests(st):
    """The pool's logical read requests (hits and misses together) from one status read."""
    return int(st.get("Innodb_buffer_pool_read_requests", 0))


def miss_share(disk_reads_delta, requests_delta):
    """The pool's misses as a share of its read requests over an interval; no requests reads as no misses."""
    return (disk_reads_delta / requests_delta) if requests_delta > 0 else 0.0


def pool_full(st):
    total = int(st.get("Innodb_buffer_pool_pages_total", 0)) or 1
    return int(st.get("Innodb_buffer_pool_pages_data", 0)) >= FULL * total


def stmt_latency(st):
    """(total statement time in picoseconds, statements) from one status read (performance_schema)."""
    return st["stmt_timer_ps"], st["stmt_count"]


def resizing(text):
    t = text.lower()
    return bool(t) and "completed" not in t and ("resiz" in t or "progress" in t or "withdraw" in t or "start" in t)


class BufferPool:
    """The plug on the server's buffer pool size: read once before the first write, write through the server's own console in
    whole chunks, wait for the server's online resize, read back, yield to any other writer, restore."""

    def __init__(self, conn):
        self.c, self.snapshot, self.last_written = conn, None, None
        self.restore_info = {}

    def _status(self):
        return status(self.c)

    def configured_mb(self, st=None):
        st = st or self._status()
        return st["pool_bytes"] // MB

    def attach(self):
        self.snapshot = self.configured_mb(); self.last_written = self.snapshot
        return self.snapshot

    def lever(self, st=None):
        st = st or self._status()
        cur = self.configured_mb(st)
        if resizing(pool_stats(st)[3]):
            return self.last_written if self.last_written is not None else cur     # mid-resize: the server is still carrying out our write
        if self.last_written is not None and cur != self.last_written:
            raise RuntimeError(f"another writer set the pool to {cur} MB (we wrote {self.last_written}): Omni stops writing")
        return cur

    def write(self, mb):
        mb = int(round(mb / CHUNK_MB)) * CHUNK_MB
        query(self.c, f"SET GLOBAL innodb_buffer_pool_size = {mb * MB}")
        self.last_written = mb
        t0 = time.monotonic()
        while time.monotonic() - t0 < RESIZE_WAIT_S:
            st = self._status()
            if self.configured_mb(st) == mb and not resizing(pool_stats(st)[3]):
                return mb
            time.sleep(0.5)
        return self.configured_mb()

    def _settle(self, budget_s):
        """Wait, up to budget_s, for a resize the server is still carrying out; the status seen first and the seconds waited."""
        t0 = time.monotonic(); st = self._status(); first = pool_stats(st)[3]
        while resizing(pool_stats(st)[3]) and time.monotonic() - t0 < budget_s:
            time.sleep(0.5); st = self._status()
        return first, round(time.monotonic() - t0, 1)

    def restore(self):
        """Hand the pool back to the snapshot and read it back. The server carries out a resize on its own time, and a shrink
        under load withdraws its last blocks only when the load eases; while one is in progress the server ignores a new size.
        So: wait for any resize in flight, write the snapshot, and if the server did not take it (still resizing), wait once
        more and write once more. The receipt (what was in flight, the seconds waited, the writes, the final read-back) is
        restore_info, written into the arm's record. The first counted runs restored without this wait and 15 of 45 omni arms
        read not handed back for exactly this reason (docs/MYSQL_PREREGISTRATION.md, the first set's result)."""
        info = {"ok": False, "resize_in_flight_at_end": "", "waited_s": 0.0, "writes": 0, "final_mb": None}
        try:
            first, waited = self._settle(RESIZE_WAIT_S)
            info["resize_in_flight_at_end"], info["waited_s"] = first, waited
            got = None
            for _ in range(2):
                got = self.write(self.snapshot); info["writes"] += 1
                if got == self.snapshot:
                    break
                _, w2 = self._settle(RESIZE_WAIT_S); info["waited_s"] = round(info["waited_s"] + w2, 1)
            info["final_mb"], info["ok"] = got, (got == self.snapshot)
        except Exception as e:
            info["error"] = repr(e)
        self.restore_info = info
        return info["ok"]


GROW_MISS_SHARE = GIVEBACK_MISS_SHARE  # amendment 2: the pool grows only while its misses are 1% or more of its read requests (it is not holding
                                       # the working set); a slow statement in a full pool that holds its working set is not the pool's to mend.
                                       # The same one-percent line gates the give-back; no new number.


def decide(p, force, misses_last_s, cur_mb, last_change_age, full, wall=0.95, reads=True):
    """The knob's move this second, in MB: slow statements (the service slow) grow the pool by ceil(force / 0.1) chunks, but only
    while the pool is full (a slow statement with room to spare is not the pool's to mend) and missing (amendment 2: misses at one
    percent of its read requests or more; a full pool that holds its working set cannot mend a slow statement); calm with the
    pool's misses under one percent of its read requests (the pool holds the working set) gives back one chunk after the dwell,
    and only in a second that saw read requests (amendment 2: a second with none says nothing about the working set); past the
    wall, with the pool full, four chunks at once. misses_last_s is the miss share of the last second."""
    lo, hi = COVER_MB
    if p is not None and p >= wall and full:
        return min(hi, cur_mb + FAILUP_MB), "fail up: the line is at hand and the pool is full, four chunks at once"
    if force > 0.05:
        if not full:
            return cur_mb, "slow with room to spare: not the pool's to mend"
        if misses_last_s < GROW_MISS_SHARE:
            return cur_mb, "slow with the pool full but holding its working set (misses under 1% of reads): not the pool's to mend"
        return min(hi, cur_mb + STEP_MB * max(1, math.ceil(force / 0.1))), "slow with the pool full and missing: grow"
    if force < -0.05 and not reads:
        return cur_mb, "calm, but no read request in the last second: nothing known, nothing taken"
    if force < -0.05 and misses_last_s < GIVEBACK_MISS_SHARE and cur_mb > lo and last_change_age >= DWELL_S:
        return max(lo, cur_mb - STEP_MB), "calm, the pool holding the working set (misses under 1% of reads): a chunk given back"
    return cur_mb, "hold"


# omni-v22: the max on the buffer pool (docs/MYSQL_PREREGISTRATION.md, amendment 6; docs/STORE_ROOT_CAUSES_2026-10-30.md): the
# wire's own rule (decide) with the spend never clamped by an allowance where the server's own account says the misses cost the
# statements (the performance schema's timer on the data files' reads against the workload's statement timer: tools/store_brain.py),
# held where they cost nothing (on a runner whose page cache holds the data files a pool miss is a read from memory: 9% to 12% of
# page reads missing with the latency unmoved), held while the host has no chunk to spare, and no give-back below the working set's
# floor nor below the operator's pool. `--dial save` keeps omni-v21's loop, the verdict under the resource objective, where giving
# memory back is the aim.
METER = "the performance schema's timer on the data files' reads against the workload's statement timer"


class Brain:
    """The knob's decision, one a second: obs holds reading_s (the mean statement latency), statements, miss_share, pool_mb,
    used_mb, full, reads (any read request this second), resizing, cpu_share, miss_time_s (the data files' read time this second),
    service_time_s (the statements' own time this second), host_avail_mb and host_total_mb (the host's memory, None unread)."""

    def __init__(self, native, objective=DEFAULT_OBJECTIVE, line_ms=LINE_STMT_MS):
        self.native, self.objective = native, objective
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.max = MemoryMax(native, STEP_MB, COVER_MB, FULL, METER)
        self.last_change = -1e9

    @property
    def failups(self):
        return self.max.failups

    def record(self):
        return self.max.record(self.objective)

    def step(self, t, obs):
        reading, cur = obs["reading_s"], obs["pool_mb"]
        f = self.law.force(reading)
        want, why = decide(self.law.p, f, obs["miss_share"], cur, t - self.last_change, obs["full"], wall=self.law.band.wall_high, reads=obs.get("reads", True))
        target, why, info = self.max.step(t, want, why, cur, obs["used_mb"], obs.get("miss_time_s"), obs.get("service_time_s"),
                                          obs.get("host_avail_mb"), obs.get("host_total_mb"), fail_up=why.startswith("fail up"))
        info.update({"p": round(self.law.p, 4), "force": round(f, 4)})
        return target, why, info


class Omni(threading.Thread):
    """The brain, one decision a second, reading the server's own statement latency, writing the audit; the knob is handed back
    at the end and read back. Amendment 3 (the brain's own verdict, 2026-10-09): the pool starts in watch and is written only
    inside the allowance a paired trial on the server itself has earned under the declared objective (tools/knob_verdict.py
    around the engine's own Verdict), one chunk a trial; a trial holds the pool, and no sample is taken while the server is
    still resizing; a fail-up never spends beyond the allowance."""

    def __init__(self, plug: BufferPool, audit_path: Path, line_ms=LINE_STMT_MS, objective=DEFAULT_OBJECTIVE, dial=DIAL):
        super().__init__(daemon=True)
        self.plug, self.audit, self.objective, self.dial, self.line_ms = plug, audit_path, objective, dial, line_ms
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event(); self.last_change = -1e9; self.writes = 0; self.failups = 0
        self.foreign = False; self.handed_back = False; self.error = None; self.verdict = None; self.brain = None

    def govern_record(self):
        """The record of what governed the knob: the max's counts (omni-v22) or the verdict's allowance (the tune-down)."""
        if self.brain is not None:
            return self.brain.record()
        return self.verdict.record() if self.verdict else None

    def run(self):
        try:
            native = self.plug.attach(); st = self.plug._status(); lat0, n0 = stmt_latency(st); _, _, rd0, _ = pool_stats(st); rq0 = read_requests(st)
            fr0, frt0 = file_reads(st)
        except Exception as e:                                      # the brain never ran: say so in the audit and the record, never silently
            self.error = repr(e)
            self.audit.write_text(json.dumps({"t": 0.0, "error": self.error, "note": "the brain could not attach; no decision was made"}) + "\n")
            return
        t0 = time.monotonic(); cpu_prev = cpu_times()
        self.verdict = KnobVerdict(native, STEP_MB, COVER_MB, objective=self.objective, settle_s=TAU, max_trial=120)   # a resize takes seconds
        if self.dial == "max":
            self.brain = Brain(native, self.objective, self.line_ms); self.verdict = None
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    st = self.plug._status()
                    lat, n = stmt_latency(st); dl, dn = lat - lat0, n - n0; lat0, n0 = lat, n
                    fr, frt = file_reads(st); fr_last, frt_last = fr - fr0, frt - frt0; fr0, frt0 = fr, frt
                    reading = (dl / dn / 1e12) if dn > 0 else 0.0        # the mean statement latency of the last second, in seconds; none reads calm
                    f = self.law.force(reading)
                    cur, used, rd, rs = pool_stats(st); rd_last = rd - rd0; rd0 = rd
                    rq = read_requests(st); rq_last = rq - rq0; rq0 = rq
                    share = miss_share(rd_last, rq_last)
                    cur = self.plug.lever(st); full = pool_full(st)
                    cpu_now = cpu_times(); d_total = cpu_now[0] - cpu_prev[0]; d_idle = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
                    cpu_share = (1.0 - d_idle / d_total) if d_total > 0 else None
                    cost = sample_cost(self.objective, dn, reading if dn > 0 else None, cur, cpu_share)
                    if self.brain is not None:                                           # the max (omni-v22)
                        h_avail, h_total = read_meminfo()
                        obs = {"reading_s": reading, "statements": dn, "miss_share": share, "pool_mb": cur, "used_mb": used, "full": full,
                               "reads": rq_last > 0, "resizing": resizing(rs), "cpu_share": cpu_share,
                               "miss_time_s": frt_last / 1e12, "service_time_s": dl / 1e12, "host_avail_mb": h_avail, "host_total_mb": h_total}
                        self.brain.last_change = self.last_change - t0
                        target, why, vinfo = self.brain.step(tick - t0, obs)
                        vinfo["file_reads_last_s"] = fr_last
                        self.failups = self.brain.failups
                    else:                                                                # the tune-down: omni-v21's loop
                        self.verdict.observe(cost, tick - t0, settled=not resizing(rs))  # measured under the pool of the last second, once resized
                        target, why = decide(self.law.p, f, share, cur, tick - self.last_change, full, wall=self.law.band.wall_high, reads=rq_last > 0)
                        target, why, vinfo = self.verdict.decide(
                            target, spend_ok=(f > 0.05 and full and share >= GROW_MISS_SHARE),
                            give_ok=(f < -0.05 and rq_last > 0 and share < GIVEBACK_MISS_SHARE),
                            t=tick - t0, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=why.startswith("fail up"))
                    wrote = None
                    if target != cur and not resizing(rs):
                        wrote = self.plug.write(target); self.writes += 1
                        self.last_change = tick                            # a shrink and a grow both start the dwell: the resize takes seconds
                        if why.startswith("fail up") and self.brain is None:
                            self.failups += 1
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3), "statements": dn, "p": round(self.law.p, 4), "force": round(f, 4),
                                         "disk_reads_last_s": rd_last, "read_requests_last_s": rq_last, "miss_share": round(share, 4), "pool_mb": cur, "used_mb": round(used, 1),
                                         "full": full, "resize": rs, "target_mb": target, "cpu_share": None if cpu_share is None else round(cpu_share, 4),
                                         "cost": None if cost is None else round(cost, 9), **vinfo,
                                         "wrote_mb": wrote, "why": why}) + "\n")
                except Exception as e:
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plug.restore()


class Sampler(threading.Thread):
    """The pool configured, the pages holding data and the pages read from disk, once a second, in both arms."""

    def __init__(self, conn):
        super().__init__(daemon=True)
        self.c, self.stop_flag, self.rows = conn, threading.Event(), []

    def run(self):
        while not self.stop_flag.is_set():
            try:
                self.rows.append(pool_stats(status(self.c))[:3])
            except Exception:
                pass
            time.sleep(DT)


def parse_histogram(text):
    """sysbench's latency histogram (--histogram=on): one line a bucket, 'value |bars count', values in ms; returns [(ms, count)]."""
    out = []
    on = False
    for line in text.splitlines():
        if "Latency histogram" in line:
            on = True; continue
        if on:
            m = re.match(r"\s*([0-9.]+)\s*\|[* ]*\s*(\d+)\s*$", line)
            if m:
                out.append((float(m.group(1)), int(m.group(2))))
            elif out and line.strip() and not line.strip().startswith("value"):
                on = False
    return out


def parse_summary(text):
    """transactions, queries, ignored errors, seconds, and sysbench's own mean and 95th percentile (ms) from its summary."""
    def grab(pat, default=0.0):
        m = re.search(pat, text)
        return float(m.group(1)) if m else default
    return {"transactions": grab(r"transactions:\s+(\d+)"), "queries": grab(r"queries:\s+(\d+)"), "errors": grab(r"ignored errors:\s+(\d+)"),
            "seconds": grab(r"total time:\s+([0-9.]+)s"), "avg_ms": grab(r"avg:\s+([0-9.]+)"), "p95_ms_sysbench": grab(r"95th percentile:\s+([0-9.]+)")}


def quantile(hist, q):
    """A quantile from the histogram's buckets (the bucket's value stands for its latency; buckets are about 2% apart)."""
    total = sum(c for _, c in hist)
    if not total:
        return float("nan")
    acc = 0
    for v, c in hist:
        acc += c
        if acc >= q * total:
            return v
    return hist[-1][0]


def sysbench(script, cmd, tables, rate, seconds, out_file: Path | None, extra=()):
    args = ["sysbench", str(LUA / f"{script}.lua"), f"--mysql-host={HOST}", f"--mysql-user={LOAD_USER}", f"--mysql-password={PASSWORD}", f"--mysql-db={DB}",
            f"--tables={tables}", f"--table-size={TABLE_ROWS}", f"--threads={THREADS}", *extra]
    if cmd == "run":
        args += [f"--rate={rate}", f"--time={int(seconds)}", f"--rand-type={RAND_TYPE}", "--histogram=on", "--report-interval=0", "--percentile=95"]
    args.append(cmd)
    r = subprocess.run(args, capture_output=True, text=True)
    txt = r.stdout + "\n" + r.stderr
    if out_file is not None:
        out_file.write_text(txt)
    return txt


def prepare_dataset(log: Path):
    """The dataset, the same tables for every workload: dropped and prepared once per workload (both arms read the same rows)."""
    c = connect(); query(c, f"DROP DATABASE IF EXISTS {DB}"); query(c, f"CREATE DATABASE {DB}"); c.close()
    txt = sysbench("oltp_read_only", "prepare", TABLES, 0, 0, log)
    if "Creating table" not in txt and "Inserting" not in txt:
        raise RuntimeError(f"sysbench prepare failed: {txt[-2000:]}")


def server_journal(unit):
    """The server's own journal and status, for the record when a restart does not come back."""
    out = []
    for cmd in (["sudo", "systemctl", "status", unit, "--no-pager", "-l"], ["sudo", "journalctl", "-u", unit, "--no-pager", "-n", "80"]):
        r = subprocess.run(cmd, capture_output=True, text=True)
        out.append(" ".join(cmd) + "\n" + (r.stdout + r.stderr)[-6000:])
    return "\n".join(out)


def fresh_server(pool_mb):
    """The pool emptied and the operator's size restored before an arm, both arms alike: the server restarted at the operator's
    configured size, the OS page cache dropped. A server that has not answered after its restart is restarted once more, with
    its journal printed; one that has not answered after that stops the run with the journal in the error (20 October: the
    MongoDB rig had died at the same wait with nothing recorded)."""
    for attempt in (1, 2):
        subprocess.run(["sudo", "systemctl", "restart", "mysql"], check=True)
        subprocess.run(["sudo", "sh", "-c", "sync; echo 3 > /proc/sys/vm/drop_caches"], check=False)
        for _ in range(120):
            try:
                c = connect(); st = status(c)
                if st["pool_bytes"] // MB != pool_mb:
                    BufferPool(c).write(pool_mb)
                return c
            except Exception:
                time.sleep(1)
        journal = server_journal("mysql")
        print(f"mysql did not answer after its restart (attempt {attempt} of 2); its status and journal:\n{journal}", flush=True)
    raise RuntimeError("mysql did not come back after two restarts; its status and journal are printed above")


def run_arm(arm, wl_dir: Path, rep, script, stmts, rate, steps, step_s, line_stmt_ms, objective=DEFAULT_OBJECTIVE):
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    line_ms = line_stmt_ms * stmts                            # the transaction line: the statement line times the statements a transaction
    c = fresh_server(NATIVE_MB)
    sampler = Sampler(connect()); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(BufferPool(connect()), d / "audit.jsonl", line_stmt_ms, objective); omni.start()
    hist_all, failed, tx, qs, summaries = [], 0, 0, 0, []
    cpu0 = cpu_times(); t0 = time.time()
    for i, notch in enumerate(int(s) for s in steps.split()):
        txt = sysbench(script, "run", notch, rate, step_s, d / f"notch-{i + 1}.log")
        h = parse_histogram(txt); s = parse_summary(txt); summaries.append(txt)
        hist_all += h; failed += int(s["errors"]); tx += int(s["transactions"]); qs += int(s["queries"])
        inside = sum(cnt for v, cnt in h if v <= line_ms); n = sum(cnt for _, cnt in h)
        row = sampler.rows[-1] if sampler.rows else (NATIVE_MB, 0.0, 0)
        print(f"   {arm} rep {rep} notch {notch}: {int(s['transactions'])} transactions, mean {s['avg_ms']:.3f} ms, p95 {quantile(h, 0.95):.3f} ms, inside the line "
              f"{100 * inside / max(1, n):.1f}%, pool {row[0]:.0f} MB, data pages {row[1]:.0f} MB", flush=True)
    t1 = time.time(); cpu1 = cpu_times()
    if omni:
        omni.stop_flag.set(); omni.join(timeout=4 * RESIZE_WAIT_S + 30)      # the last decision's resize, the settle, two writes
    sampler.stop_flag.set(); sampler.join(timeout=5)
    (d / "sysbench.log").write_text("\n\n".join(summaries))
    seconds = t1 - t0
    hist = sorted(hist_all); n = sum(cnt for _, cnt in hist)
    inside = sum(cnt for v, cnt in hist if v <= line_ms)
    rows = sampler.rows or [(NATIVE_MB, 0.0, 0)]
    total = cpu1[0] - cpu0[0]; idle = cpu1[1] - cpu0[1]; cpu_s = (total - idle) / os.sysconf("SC_CLK_TCK")
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "transactions": tx, "queries": qs,
         "work_inside_line_tps": inside / seconds, "tps": tx / seconds, "qps": qs / seconds, "p95_ms": quantile(hist, 0.95), "p99_ms": quantile(hist, 0.99),
         "mean_ms": (sum(v * cnt for v, cnt in hist) / n) if n else float("nan"), "failed": failed,
         "pool_mb_mean": sum(x[0] for x in rows) / len(rows), "pool_used_mb_mean": sum(x[1] for x in rows) / len(rows),
         "disk_reads": rows[-1][2] - rows[0][2], "cpu_busy_share": (total - idle) / max(1, total), "cpu_seconds": cpu_s,
         "cpu_s_per_1k_inside": 1000.0 * cpu_s / max(1, inside), "writes": (omni.writes if omni else 0),
         "handed_back": (omni.handed_back if omni else True), "foreign_writer": (omni.foreign if omni else False), "failups": (omni.failups if omni else 0),
         "controller_error": (omni.error if omni else None),
         "restore": (omni.plug.restore_info if omni else {}),
         "verdict": (omni.govern_record() if omni else None)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    print(f"   {arm} rep {rep}: {tx} transactions, inside the line {g['work_inside_line_tps']:.0f}/s, p95 {g['p95_ms']:.2f} ms, pool {g['pool_mb_mean']:.0f} MB, "
          f"data pages {g['pool_used_mb_mean']:.0f} MB, disk reads {g['disk_reads']:,}, CPU {cpu_s:.1f} s, handed back {g['handed_back']}"
          + (f", verdict {g['verdict']['state']}" if g.get("verdict") else ""), flush=True)
    return g


def server_version():
    try:
        return str(query(connect(), "SELECT VERSION()")[0][0])
    except Exception:
        return "?"


def sysbench_version():
    try:
        return subprocess.run(["sysbench", "--version"], capture_output=True, text=True).stdout.strip()
    except OSError:
        return "?"


def run_workload(name, out: Path, reps, step_s, line_stmt_ms, objective=DEFAULT_OBJECTIVE):
    script, stmts, rate, steps, tuning = WORKLOADS[name]
    wl_dir = out / f"sysbench-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    ver = server_version()
    print(f"== {name}: sysbench {script} ({stmts} statements a transaction, {rate} a second offered), {TABLES} tables of {TABLE_ROWS:,} rows, steps {steps}, "
          f"{step_s} s a notch, MySQL {ver}, the verdict's objective {objective}", flush=True)
    fresh_server(NATIVE_MB)
    prepare_dataset(wl_dir / "prepare.log")
    rec = {"workload": name, "tuning": tuning, "script": script, "statements": stmts, "rate_tps": rate, "steps": steps, "step_s": step_s,
           "line_stmt_ms": line_stmt_ms, "line_ms": line_stmt_ms * stmts, "threads": THREADS, "tables": TABLES, "table_rows": TABLE_ROWS, "rand_type": RAND_TYPE,
           "native_mb": NATIVE_MB, "chunk_mb": CHUNK_MB, "cover_mb": list(COVER_MB), "mysql_version": ver, "sysbench_version": sysbench_version(),
           "objective": objective, "dial": DIAL, "native": NATIVE, "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, script, stmts, rate, steps, step_s, line_stmt_ms, objective)
        rec["reps"].append(r)
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
    (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    return rec


def report(recs, out: Path):
    shipped = bool(recs) and all(r.get("native") == "shipped" for r in recs)
    native_mb = recs[0]["native_mb"] if recs else NATIVE_MB
    L = ["# sysbench on MySQL: Omni-Compass on top of a database's " + ("buffer pool as shipped" if shipped else "operator-set buffer pool"), "",
         (f"MySQL exactly as Ubuntu ships it, its InnoDB buffer pool at MySQL's own default ({native_mb} MB), is native" if shipped else
          f"MySQL as Ubuntu ships it with the operator's InnoDB buffer pool ({native_mb} MB) is native")
         + "; omni is the compass law on the pool size "
         f"through the server's own console inside [{COVER_MB[0]}, {COVER_MB[1]}] MB in chunks of {CHUNK_MB} MB, holding the server's own statement "
         f"latency at {CENTER:.0%} of the {LINE_STMT_MS:g} ms statement line. sysbench's published OLTP workloads, the same transactions in both arms, "
         "the tables in use stepping through the pool and past it. Memory held is the resource; the host's CPU seconds include the compass's own "
         "cost. Every row is reported, losses included.", ""]
    for rec in recs:
        L += [f"## {rec['workload']}: sysbench {rec['script']}, {rec['statements']} statements a transaction, {rec['rate_tps']} a second offered, steps {rec['steps']} × {rec['step_s']} s"
              + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"MySQL {rec['mysql_version']}, {rec['sysbench_version']}; {rec['threads']} client threads; the transaction line {rec['line_ms']:g} ms; "
              f"{len(rec['reps'])} paired repetitions; engine {rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"]); fw = any(r["omni"]["foreign_writer"] for r in rec["reps"])
        L += ["", f"Every omni arm handed back to native's pool size ({rec['native_mb']} MB): {'yes' if hb else 'NO'}; another writer seen: {'yes' if fw else 'no'}; "
              f"fail-ups: {sum(r['omni']['failups'] for r in rec['reps'])}.", ""]
    (out / "SYSBENCH.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "SYSBENCH.md"


def setup():
    """The benchmark user on the local server, the operator's pool and chunk in the server's own configuration file, the
    performance schema on; the server restarted. MySQL and sysbench themselves are installed by the workflow from Ubuntu's own
    packages."""
    sql = (f"CREATE USER IF NOT EXISTS '{USER}'@'%' IDENTIFIED BY '{PASSWORD}'; GRANT ALL PRIVILEGES ON *.* TO '{USER}'@'%' WITH GRANT OPTION; "
           f"CREATE USER IF NOT EXISTS '{LOAD_USER}'@'%' IDENTIFIED BY '{PASSWORD}'; GRANT ALL PRIVILEGES ON {DB}.* TO '{LOAD_USER}'@'%'; FLUSH PRIVILEGES;")
    ok = False
    for cmd in (["sudo", "mysql", "-e", sql], ["mysql", "-uroot", "-proot", "-h", HOST, "-e", sql]):
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            ok = True; break
    if not ok:
        print(f"could not create the benchmark user: {r.stderr[-500:]}", file=sys.stderr); return 1
    conf = Path("/etc/mysql/mysql.conf.d/omni-bench.cnf")
    txt = (f"[mysqld]\ninnodb_buffer_pool_size = {NATIVE_MB}M\ninnodb_buffer_pool_chunk_size = {CHUNK_MB}M\ninnodb_buffer_pool_instances = 1\n"
           "performance_schema = ON\n")
    subprocess.run(["sudo", "tee", str(conf)], input=txt, text=True, check=True, capture_output=True)
    subprocess.run(["sudo", "systemctl", "restart", "mysql"], check=True)
    c = fresh_server(NATIVE_MB)
    print(f"MySQL {server_version()} at native's {NATIVE_MB} MB pool ({NATIVE}) (chunk {CHUNK_MB} MB); {sysbench_version()}; user {USER}, load user {LOAD_USER}; pool reads {status(c)['pool_bytes'] // MB} MB")
    return 0


def main(argv=None):
    global NATIVE, NATIVE_MB
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--native", default="operator", choices=("operator", "shipped"),
                    help="native's pool: the operator's 512 MB (preregistered) or MySQL as shipped, its own 128 MB (the founder's order of "
                         "17 October: native as it is shipped); omni starts from the same pool and goes beyond it if it can")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=20.0)
    ap.add_argument("--line-ms", type=float, default=LINE_STMT_MS, help="the statement line (ms)")
    ap.add_argument("--out", default="sysbench-out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a step by: resource (the index's reading: work, speed, memory and CPU together) or service (work and speed alone)")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    NATIVE, NATIVE_MB = a.native, (SHIPPED_MB if a.native == "shipped" else OPERATOR_MB)
    if a.setup:
        return setup()
    out = Path(a.out)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("sysbench-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.line_ms, a.objective) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
