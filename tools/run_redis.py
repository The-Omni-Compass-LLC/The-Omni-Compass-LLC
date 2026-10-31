#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on top of a Redis cache's operator-set memory ceiling (docs/REDIS_PREREGISTRATION.md).

Redis as shipped, with the two settings an operator sets once for a cache: a memory ceiling (maxmemory) and the eviction
rule (allkeys-lru). An application in front of it asks for keys drawn from a working set that widens and narrows over the
run; a hit is answered by Redis, a miss costs the application a trip to the store behind the cache (a declared fixed
delay) and the value is written back. The operator's fixed ceiling is the native controller here.

  native  Redis at the operator's ceiling (64 MB) for the whole run
  omni    the same Redis, with the compass law (omnicompass/compass_law.py) on one knob, the memory ceiling, through Redis's
          own console (CONFIG SET maxmemory), inside the cover [16 MB, 512 MB]: the compass reads the application's own
          request latency (hits fast, misses slow) on a band from 0 to the response line and holds it at 40% of the line;
          misses with the cache full push the ceiling up (a miss with room to spare is a cold miss, which no ceiling can
          mend), calm gives memory back 8 MB a second when nothing is being evicted; at 95% of the line with the cache full
          a quarter of the cover is added at once (fail up); the ceiling is handed back to the operator's at the end and
          read back; a ceiling found at a value Omni did not write stops it writing (one writer)

Gauges from the application's own records (every request's latency, hit or miss), Redis's own INFO (memory used, the
ceiling, evictions, hits and misses) and the host's /proc/stat (CPU seconds, the compass's own cost included). Memory held
is the resource; no energy is claimed beyond the host's CPU seconds. Every row is reported, losses included.

  python3 tools/run_redis.py --setup                      # start a Redis for the run (the workflow does this)
  python3 tools/run_redis.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_redis.py --report-only DIR            # re-read finished <workload>.json files and write REDIS.md
"""
from __future__ import annotations

import argparse
import json
import math
from collections import deque
import os
import random
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
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402  (amendment 2: the brain's own verdict)
from tools.store_brain import MemoryMax, read_meminfo, HOLD_WINDOW_S, MISS_WORTH  # noqa: E402  (omni-v22: the max on the ceiling)
from tools.readings import word as gel_word, aim as gel_aim, EVEN_SAME, EVEN_NOISE, SHOWN  # noqa: E402  (the words every table uses)
from tools.run_ycsb import host_cpu_split, pid_of, proc_cpu_jiffies  # noqa: E402  (the CPU apart, the same reading as the other stores)

HOST = os.environ.get("REDIS_HOST", "127.0.0.1")
PORT = int(os.environ.get("REDIS_PORT", "6390"))
MB = 1024 * 1024
LINE_MS = 2.0             # the response line: a request answered within 2 ms (a hit is well inside, a miss well outside)
CENTER = 0.4              # the compass holds the application's latency at 40% of the line
DT = 1.0                  # one decision a second
TAU = 2.0                 # memory given or taken shows in the misses within a couple of seconds
SMOOTH = 0.5
NATIVE_MB = 64            # the operator's ceiling
NATIVE = "operator"        # --native shipped: Redis exactly as shipped, no ceiling (maxmemory 0) and noeviction
POLICY = {"operator": "allkeys-lru", "shipped": "noeviction"}
COVER_MB = (16, 512)      # never under 16 MB, never over 512 MB
STEP_MB = 8               # one notch of the knob
FAILUP_MB = 128           # past the wall: a quarter of the cover at once, and again the next second if still past it
DWELL_S = 5.0             # after growing, no taking back within five seconds (no hunting); giving back is a notch a second
DIAL = os.environ.get("OMNI_DIAL", "max")   # omni-v22: max, the factory tune; save, the tune-down
MISS_PENALTY_MS = 5.0     # the declared trip to the store behind the cache, on a miss
WORKERS = 32              # the application's request threads
RATE = 1500.0             # requests a second offered, the same in both arms
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
ZIPF_S = 0.5              # the working set's key distribution (Zipf exponent): a hot core and a long tail, as application caches see
FULL = 0.9                # the cache counts as full when memory used is 90% of the ceiling or more
from omnicompass.student_t import T95  # noqa: E402  (the two-sided 95% point of Student's t, any degrees of freedom)
SAME_REL = 1e-6

WORKLOADS = {
    # name: (value bytes, base keyspace (keys at notch 1; about 20 MB of values at notch 1, 120 MB at notch 6), steps, tuning?)
    "tuning": (8192, 2_500, STEPS, True),
    "small": (2048, 10_000, STEPS, False),
    "large": (32768, 625, STEPS, False),
    "burst": (8192, 2_500, BURST, False),
}

GAUGES = [  # key, label, direction
    ("work_inside_line_rps", "work inside the response line (requests a second answered within the line)", "higher"),
    ("rps", "throughput (requests a second)", "higher"),
    ("hit_rate", "cache hit rate", "higher"),
    ("p95_ms", "latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "failed requests", "never more"),
    ("maxmemory_mb_mean", "memory ceiling held, mean (MB; the knob, the resource)", "spent"),
    ("used_mb_mean", "memory used, mean (MB)", "spent"),
    ("evictions", "keys evicted", "shown"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "spent"),
    ("cpu_seconds", "host CPU-seconds", "spent"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 requests inside the line", "spent"),
    ("writes", "ceiling changes written (the knob's moves)", "shown"),
    # store fix of 25 October: the CPU apart, beside the host figure (old runs lack these rows; the readers prefer process_cpu_seconds)
    ("process_cpu_seconds", "the stack's own CPU-seconds (redis-server, the application, the compass and its sampler; steal and the runner's other processes excluded)", "spent"),
    ("server_cpu_seconds", "the server's own CPU-seconds (redis-server)", "shown"),
    ("app_cpu_seconds", "the application's own CPU-seconds (its request threads)", "shown"),
    ("brain_cpu_seconds", "the compass's own CPU-seconds (the brain's thread; none in the native arm)", "shown"),
    ("sampler_cpu_seconds", "the sampler's own CPU-seconds (both arms)", "shown"),
    ("host_cpu_seconds_no_steal", "host CPU-seconds without steal", "shown"),
    ("steal_seconds", "CPU-seconds the hypervisor took (steal), host-wide", "shown"),
]
OPTIONAL_GAUGES = ("process_cpu_seconds", "server_cpu_seconds", "app_cpu_seconds", "brain_cpu_seconds", "sampler_cpu_seconds",
                   "host_cpu_seconds_no_steal", "steal_seconds")      # absent from runs before 25 October


def zipf_sampler(rng, n, s=ZIPF_S):
    """Keys 0..n-1 with probability proportional to 1/(k+1)^s (the hot set first); a table is built once per keyspace."""
    w = [1.0 / (k + 1) ** s for k in range(n)]
    tot = sum(w); acc = 0.0; cum = []
    for x in w:
        acc += x / tot; cum.append(acc)
    import bisect
    def draw():
        return bisect.bisect_left(cum, rng.random())
    return draw


class App(threading.Thread):
    """The application: requests at the offered rate, drawn from the working set of the moment; a hit is Redis's answer, a
    miss is the declared store trip and a write-back; every request's latency and hit/miss is recorded."""

    def __init__(self, r, value_bytes, base_keys, steps, step_s, seed, rec_path):
        super().__init__(daemon=True)
        self.r, self.value, self.steps, self.step_s = r, b"v" * value_bytes, [int(s) for s in steps.split()], step_s
        self.base_keys, self.rng, self.rec_path = base_keys, random.Random(seed), rec_path
        self.stop_flag = threading.Event(); self.lock = threading.Lock()
        self.records = []; self.failed = 0; self.hits = 0; self.misses = 0; self.recent = []
        self.sem = threading.Semaphore(WORKERS)

    def one(self, key):
        t0 = time.perf_counter()
        try:
            v = self.r.get(key)
            if v is None:
                time.sleep(MISS_PENALTY_MS / 1000.0)           # the store behind the cache
                self.r.set(key, self.value)
                hit = 0
            else:
                hit = 1
            lat = (time.perf_counter() - t0) * 1000.0
            with self.lock:
                self.records.append((time.time(), lat, hit)); self.recent.append((time.time(), lat))
                if hit:
                    self.hits += 1
                else:
                    self.misses += 1
        except Exception:
            with self.lock:
                self.failed += 1
        finally:
            self.sem.release()

    def run(self):
        interval = 1.0 / RATE
        for notch in self.steps:
            n = self.base_keys * notch
            draw = zipf_sampler(self.rng, n)
            prefix = f"k{n}:"
            t_end = time.perf_counter() + self.step_s; nxt = time.perf_counter()
            while time.perf_counter() < t_end and not self.stop_flag.is_set():
                now = time.perf_counter()
                if now >= nxt:
                    self.sem.acquire()
                    threading.Thread(target=self.one, args=(prefix + str(draw()),), daemon=True).start()
                    nxt += interval
                else:
                    time.sleep(min(0.0005, nxt - now))
            if self.stop_flag.is_set():
                break
        for _ in range(WORKERS):                                # wait for the last requests
            self.sem.acquire()

    def reading(self, since_s=1.0):
        """The application's own reading: mean latency (s) of the last second's requests; nothing asked reads calm."""
        now = time.time()
        with self.lock:
            self.recent = [(t, l) for t, l in self.recent if t >= now - since_s]
            lat = [l for _, l in self.recent]
        return (sum(lat) / len(lat) / 1000.0) if lat else 0.0

    def split(self, since_s=1.0):
        """The last second's hits and misses apart: (a hit's mean latency ms, a miss's, the miss share), or Nones."""
        cut = time.time() - since_s
        with self.lock:
            recent = [(lat, hit) for t, lat, hit in self.records[-20000:] if t >= cut]
        hits = [l for l, h in recent if h]; misses = [l for l, h in recent if not h]
        if not recent:
            return None, None, None
        return (sum(hits) / len(hits) if hits else None, sum(misses) / len(misses) if misses else None, len(misses) / len(recent))

    def last_second(self, line_ms, since_s=1.0):
        """The brain's sample: (requests answered, of them inside the line, mean latency in s) over the last second."""
        now = time.time()
        with self.lock:
            self.recent = [(t, l) for t, l in self.recent if t >= now - since_s]
            lat = [l for _, l in self.recent]
        if not lat:
            return 0, 0, None
        return len(lat), sum(1 for l in lat if l <= line_ms), sum(lat) / len(lat) / 1000.0


class Ceiling:
    """The plug on Redis's memory ceiling: read once before the first write, write through the console, read back,
    yield to any other writer, restore."""

    def __init__(self, r):
        self.r, self.snapshot, self.last_written = r, None, None

    def attach(self):
        self.snapshot = int(self.r.config_get("maxmemory")["maxmemory"]); self.last_written = self.snapshot
        return self.snapshot

    def lever(self):
        cur = int(self.r.config_get("maxmemory")["maxmemory"])
        if self.last_written is not None and cur != self.last_written:
            raise RuntimeError(f"another writer set maxmemory to {cur} (we wrote {self.last_written}): Omni stops writing")
        return cur

    def write(self, mb):
        self.r.config_set("maxmemory", str(int(mb) * MB))
        back = int(self.r.config_get("maxmemory")["maxmemory"])
        self.last_written = back
        return back // MB

    def restore(self):
        try:
            self.r.config_set("maxmemory", str(self.snapshot))
            return int(self.r.config_get("maxmemory")["maxmemory"]) == self.snapshot
        except Exception:
            return False

    def evicted(self):
        return int(self.r.info("stats").get("evicted_keys", 0))

    def used_mb(self):
        return int(self.r.info("memory")["used_memory"]) / MB


def decide(p, force, evicted_last_s, cur_mb, last_change_age, full, wall=0.95):
    """The knob's move this second, in MB: misses (the service slow) grow the ceiling by ceil(force / 0.1) notches, but
    only while the cache is full (a miss in a cache with room is a cold miss, which no ceiling can mend); calm with nothing
    evicted gives back one notch after the dwell; past the wall, with the cache full, the top of the cover at once."""
    lo, hi = COVER_MB
    if p is not None and p >= wall and full:
        return min(hi, cur_mb + FAILUP_MB), "fail up: the line is at hand and the cache is full, a quarter of the cover at once"
    if force > 0.05:
        if not full:
            return cur_mb, "misses with room to spare: cold misses, nothing for the ceiling to do"
        return min(hi, cur_mb + STEP_MB * max(1, math.ceil(force / 0.1))), "misses with the cache full: grow"
    if force < -0.05 and evicted_last_s == 0 and cur_mb > lo and last_change_age >= DWELL_S:
        return max(lo, cur_mb - STEP_MB), "calm, nothing evicted: a notch given back"
    return cur_mb, "hold"


# omni-v22: the max on the cache's ceiling (docs/REDIS_PREREGISTRATION.md, amendment 5; docs/STORE_ROOT_CAUSES_2026-10-30.md).
# On omni-v21 the verdict's allowance clamped every move, the wall's fail-up included, and the wall abandoned every spend trial,
# so in 4,426 of the 4,581 seconds the service stood over its line the brain asked for memory and was refused; the cache stayed at
# 64 to 80 MB while the working set needed more. Under the max (the factory tune, the founder's order of 12 October) memory the
# cache takes inside the operator's cover is power given, shown beside the hits it bought; the verdict's allowance judges the
# give-back below the operator's ceiling (the tune-down's ground), never a spend the service asks for.
METER = "the application's own split of each request into hits and misses"


def miss_time(obs):
    """(the misses' time, the service's time) over the last second, in seconds, from the application's own split: the misses'
    count times what a miss cost beyond a hit, and the requests times their mean. (None, None) where the second carries no hit and
    miss latencies (the wire's older records): nothing known, and the max then takes nothing."""
    hit, miss, share, mean, n = obs.get("hit_ms"), obs.get("miss_ms"), obs.get("miss_share"), obs.get("reading_s"), obs.get("n")
    if hit is None or miss is None or share is None or not mean or not n:
        return None, None
    return n * share * max(0.0, miss - hit) / 1000.0, n * mean


class Brain:
    """The knob's decision, one a second: the code the real run (Omni) and the closed-loop model (tools/redis_model.py) drive.
    obs: reading_s (the application's mean latency over the last second), n, inside, evicted_last_s, ceiling_mb, used_mb,
    cpu_share (or None), hit_ms, miss_ms and miss_share (the application's split), host_avail_mb and host_total_mb (None unread).

      the spend     misses with the cache full (the compass asking, by its own law: ceil(force / 0.1) notches a second; at the
                    wall a quarter of the cover at once) go through unclamped, up to the cover's top, where the application's own
                    split says the misses are MISS_WORTH of its time or more and the host has the notch to spare; the memory is
                    power given (tools/store_brain.py, MemoryMax)
      the hold      calm with nothing evicted for the dwell gives one notch back a second, never below the working set's floor
                    (the most the working set occupied in HOLD_WINDOW_S) nor below the operator's ceiling
      the audit     every decision with the max's reading beside it (the misses' share of the service's time, the floor, the host)"""

    def __init__(self, native_mb, objective=DEFAULT_OBJECTIVE, line_ms=LINE_MS):
        self.native_mb, self.objective = native_mb, objective
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.max = MemoryMax(native_mb, STEP_MB, COVER_MB, FULL, METER)
        self.last_change = -1e9

    @property
    def failups(self):
        return self.max.failups

    def record(self):
        return self.max.record(self.objective)

    def floor_mb(self, t):
        return self.max.floor.value(t)

    def step(self, t, obs):
        reading = obs["reading_s"]; cur = obs["ceiling_mb"]; ev_last = obs["evicted_last_s"]
        full = obs["used_mb"] >= FULL * cur
        f = self.law.force(reading)
        want, why = decide(self.law.p, f, ev_last, cur, t - self.last_change, full, wall=self.law.band.wall_high)
        miss_s, service_s = miss_time(obs)
        target, why, info = self.max.step(t, want, why, cur, obs["used_mb"], miss_s, service_s, obs.get("host_avail_mb"),
                                          obs.get("host_total_mb"), fail_up=why.startswith("fail up"))
        if target > cur:
            self.last_change = t                                       # the dwell runs from the last growth
        info.update({"p": round(self.law.p, 4), "force": round(f, 4)})
        return target, why, info


class Omni(threading.Thread):
    """The brain, one decision a second, writing the audit; the knob is handed back at the end and read back. Amendment 2 (the
    brain's own verdict, 2026-10-09): the ceiling starts in watch and is written only inside the allowance a paired trial on
    the cache itself has earned under the declared objective (tools/knob_verdict.py around the engine's own Verdict); a trial
    holds the ceiling; a fail-up never spends beyond the allowance."""

    def __init__(self, plug: Ceiling, app: App, audit_path: Path, line_ms=LINE_MS, objective=DEFAULT_OBJECTIVE, dial=DIAL):
        super().__init__(daemon=True)
        self.plug, self.app, self.audit, self.line_ms, self.objective, self.dial = plug, app, audit_path, line_ms, objective, dial
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event(); self.last_change = -1e9; self.writes = 0; self.failups = 0
        self.foreign = False; self.handed_back = False; self.verdict = None; self.brain = None
        self.cpu_s = 0.0                                             # the brain thread's own CPU-seconds so far (store fix of 25 October)

    def govern_record(self):
        """The record of what governed the knob: the max's counts (omni-v22) or the verdict's allowance (the tune-down)."""
        if self.brain is not None:
            return self.brain.record()
        return self.verdict.record() if self.verdict else None

    def run(self):
        c0 = time.thread_time()
        native_mb = self.plug.attach() // MB; ev0 = self.plug.evicted(); t0 = time.monotonic(); cpu_prev = cpu_times()
        if native_mb == 0:
            # Redis as shipped holds every key it is given (no ceiling): the knob is at its limit on native, and any ceiling
            # Omni wrote would sit below native (the max never goes below native). It reads and writes nothing, and says so.
            with open(self.audit, "w") as fh:
                fh.write(json.dumps({"t": 0.0, "maxmemory_mb": 0, "why": "native has no ceiling: at its limit on native, nothing written"}) + "\n")
            self.stop_flag.wait()
            self.handed_back = self.plug.restore()
            return
        self.verdict = KnobVerdict(native_mb, STEP_MB, COVER_MB, objective=self.objective, settle_s=TAU)
        if self.dial == "max":
            self.brain = Brain(native_mb, self.objective, self.line_ms); self.verdict = None
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    reading = self.app.reading(1.0)
                    n_req, inside, mean_s = self.app.last_second(self.line_ms)
                    f = self.law.force(reading)
                    ev = self.plug.evicted(); ev_last = ev - ev0; ev0 = ev
                    cur = self.plug.lever() // MB
                    used = self.plug.used_mb(); full = used >= FULL * cur
                    cpu_now = cpu_times(); d_total = cpu_now[0] - cpu_prev[0]; d_idle = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
                    cpu_share = (1.0 - d_idle / d_total) if d_total > 0 else None
                    cost = sample_cost(self.objective, inside, mean_s, cur, cpu_share)
                    hit_ms, miss_ms, miss_share = self.app.split(1.0)
                    if self.brain is not None:                                           # the max (omni-v22)
                        h_avail, h_total = read_meminfo()
                        obs = {"reading_s": reading, "n": n_req, "inside": inside, "evicted_last_s": ev_last, "ceiling_mb": cur, "used_mb": used,
                               "cpu_share": cpu_share, "hit_ms": hit_ms, "miss_ms": miss_ms, "miss_share": miss_share,
                               "host_avail_mb": h_avail, "host_total_mb": h_total}
                        target, why, vinfo = self.brain.step(tick - t0, obs)       # the Brain's decision (above)
                        self.failups = self.brain.failups
                    else:                                                                # the tune-down: omni-v21's loop
                        self.verdict.observe(cost, tick - t0)                            # measured under the ceiling of the last second
                        target, why = decide(self.law.p, f, ev_last, cur, tick - self.last_change, full, wall=self.law.band.wall_high)
                        target, why, vinfo = self.verdict.decide(
                            target, spend_ok=(f > 0.05 and full), give_ok=(f < -0.05 and ev_last == 0),
                            t=tick - t0, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=why.startswith("fail up"))
                        if target > cur and why.startswith("fail up"):
                            self.failups += 1
                    vinfo.update({"hit_ms": None if hit_ms is None else round(hit_ms, 3), "miss_ms": None if miss_ms is None else round(miss_ms, 3),
                                  "miss_share": None if miss_share is None else round(miss_share, 4)})
                    wrote = None
                    if target != cur:
                        wrote = self.plug.write(target); self.writes += 1
                        if target > cur:
                            self.last_change = tick
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3),
                                         "evicted_last_s": ev_last, "maxmemory_mb": cur, "used_mb": round(used, 1), "full": full, "target_mb": target, "wrote_mb": wrote,
                                         "requests_last_s": n_req, "inside_last_s": inside, "cpu_share": None if cpu_share is None else round(cpu_share, 4),
                                         "cost": None if cost is None else round(cost, 9), **vinfo, "why": why}) + "\n")
                except Exception as e:                        # a foreign writer or a lost console: say so, stop writing
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                self.cpu_s = time.thread_time() - c0
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plug.restore()


class Sampler(threading.Thread):
    """The ceiling, the memory used and the evictions, once a second, in both arms."""

    def __init__(self, r):
        super().__init__(daemon=True)
        self.r, self.stop_flag, self.rows = r, threading.Event(), []
        self.cpu_s = 0.0                                             # the sampler thread's own CPU-seconds so far

    def run(self):
        c0 = time.thread_time()
        while not self.stop_flag.is_set():
            try:
                m = self.r.info("memory"); s = self.r.info("stats")
                self.rows.append((int(m["maxmemory"]) / MB, int(m["used_memory"]) / MB, int(s.get("evicted_keys", 0))))
            except Exception:
                pass
            self.cpu_s = time.thread_time() - c0
            time.sleep(DT)


def cpu_apart(server_s, process_s, brain_s, sampler_s, busy_s, steal_s):
    """The arm's CPU apart (store fix of 25 October), all in seconds over the arm: the server's from its /proc/<pid>/stat, the
    harness process's from getrusage, the brain's and the sampler's from their own threads' clocks; the application is the
    harness process less the two threads. process_cpu_seconds, the stack's own (server, application, compass, sampler), is
    what the readers prefer to the host figure, which also counts steal and every other process on the runner."""
    app = max(0.0, process_s - brain_s - sampler_s)
    return {"server_cpu_seconds": server_s, "app_cpu_seconds": app, "brain_cpu_seconds": brain_s, "sampler_cpu_seconds": sampler_s,
            "process_cpu_seconds": (server_s + process_s) if server_s is not None else None,
            "host_cpu_seconds_no_steal": busy_s, "steal_seconds": steal_s}


def cpu_times():
    with open("/proc/stat") as fh:
        f = fh.readline().split()
    vals = list(map(int, f[1:]))
    return sum(vals), vals[3] + vals[4]


def run_arm(arm, wl_dir: Path, rep, value_bytes, base_keys, steps, step_s, line_ms, seed, objective=DEFAULT_OBJECTIVE):
    import redis
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    r = redis.Redis(host=HOST, port=PORT, socket_timeout=5)
    r.flushall()                                               # a cold cache, both arms alike
    r.config_set("maxmemory", str(NATIVE_MB * MB)); r.config_set("maxmemory-policy", POLICY[NATIVE])   # NATIVE_MB 0: no ceiling
    pipe = r.pipeline(transaction=False)                       # the warm-up: the notch-1 working set loaded once, both arms alike
    for k in range(base_keys):
        pipe.set(f"k{base_keys}:{k}", b"v" * value_bytes)
        if k % 500 == 499:
            pipe.execute()
    pipe.execute()
    r.config_resetstat()
    app = App(redis.Redis(host=HOST, port=PORT, socket_timeout=5, max_connections=WORKERS + 4), value_bytes, base_keys, steps, step_s, seed, d / "requests.log")
    sampler = Sampler(redis.Redis(host=HOST, port=PORT, socket_timeout=5)); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(Ceiling(redis.Redis(host=HOST, port=PORT, socket_timeout=5)), app, d / "audit.jsonl", line_ms, objective); omni.start()
    import resource
    tck = os.sysconf("SC_CLK_TCK"); pid = pid_of("redis-server")
    srv0 = proc_cpu_jiffies(pid) if pid else None; own0 = resource.getrusage(resource.RUSAGE_SELF); busy0, steal0 = host_cpu_split()
    brain0 = omni.cpu_s if omni else 0.0; samp0 = sampler.cpu_s
    cpu0 = cpu_times(); t0 = time.time()
    app.start(); app.join()
    t1 = time.time(); cpu1 = cpu_times()
    srv1 = proc_cpu_jiffies(pid) if pid else None; own1 = resource.getrusage(resource.RUSAGE_SELF); busy1, steal1 = host_cpu_split()
    apart = cpu_apart(None if srv0 is None or srv1 is None else (srv1 - srv0) / tck,
                      (own1.ru_utime + own1.ru_stime) - (own0.ru_utime + own0.ru_stime),
                      (omni.cpu_s - brain0) if omni else 0.0, sampler.cpu_s - samp0, (busy1 - busy0) / tck, (steal1 - steal0) / tck)
    if omni:
        omni.stop_flag.set(); omni.join(timeout=30)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    seconds = t1 - t0
    with open(d / "requests.log", "w") as fh:
        for t, lat, hit in app.records:
            fh.write(f"{t:.3f} {lat:.3f} {hit}\n")
    lat_sorted = sorted(l for _, l, _ in app.records); n = len(lat_sorted)
    def q(p):
        return lat_sorted[min(n - 1, int(p * n))] if n else float("nan")
    inside = sum(1 for l in lat_sorted if l <= line_ms)
    rows = sampler.rows or [(NATIVE_MB, 0.0, 0)]
    total = cpu1[0] - cpu0[0]; idle = cpu1[1] - cpu0[1]; cpu_s = (total - idle) / os.sysconf("SC_CLK_TCK")
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "requests": n, "hits": app.hits, "misses": app.misses,
         "work_inside_line_rps": inside / seconds, "rps": n / seconds, "hit_rate": app.hits / max(1, app.hits + app.misses),
         "p95_ms": q(0.95), "p99_ms": q(0.99), "mean_ms": (sum(lat_sorted) / n) if n else float("nan"), "failed": app.failed,
         "maxmemory_mb_mean": sum(x[0] for x in rows) / len(rows), "used_mb_mean": sum(x[1] for x in rows) / len(rows),
         "evictions": rows[-1][2], "cpu_busy_share": (total - idle) / max(1, total), "cpu_seconds": cpu_s,
         "cpu_s_per_1k_inside": 1000.0 * cpu_s / max(1, inside), "writes": (omni.writes if omni else 0), **apart,
         "handed_back": (omni.handed_back if omni else True), "foreign_writer": (omni.foreign if omni else False), "failups": (omni.failups if omni else 0),
         "verdict": (omni.govern_record() if omni else None)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    print(f"   {arm} rep {rep}: {n} requests, hit rate {g['hit_rate']:.1%}, inside the line {g['work_inside_line_rps']:.0f}/s, p95 {g['p95_ms']:.2f} ms, "
          f"ceiling {g['maxmemory_mb_mean']:.0f} MB, used {g['used_mb_mean']:.0f} MB, CPU {cpu_s:.1f} s, handed back {g['handed_back']}"
          + (f", verdict {g['verdict']['state']}" if g.get("verdict") else ""), flush=True)
    return g


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
        reading = "**LOSS in a repetition**"
    elif same:
        reading = EVEN_SAME
    elif not clear:
        reading = EVEN_NOISE
    else:
        reading = gel_word(mean < 0, gel_aim(direction, key))      # the word by what the gauge is for, never by its sign
    return {"native": nat, "omni": om, "diff": mean, "ci95": [lo, hi], "n": n, "significant": clear, "reading": reading}


def _num(x):
    return isinstance(x, (int, float)) and not (isinstance(x, float) and math.isnan(x))


def engine():
    try:
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], cwd=ROOT, capture_output=True, text=True, timeout=120).stdout.strip()
        sha = subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        return {"version": out.splitlines()[0] if out else "unknown", "commit": sha[:12]}
    except (OSError, subprocess.SubprocessError):
        return {"version": "unknown", "commit": "?"}


def run_workload(name, out: Path, reps, step_s, line_ms, objective=DEFAULT_OBJECTIVE):
    import redis
    value_bytes, base_keys, steps, tuning = WORKLOADS[name]
    wl_dir = out / f"redis-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    ver = redis.Redis(host=HOST, port=PORT).info("server").get("redis_version", "?")
    print(f"== {name}: {value_bytes} B values, working set {base_keys:,} keys x notch, steps {steps}, {step_s} s a notch, Redis {ver}, the verdict's objective {objective}", flush=True)
    rec = {"workload": name, "tuning": tuning, "value_bytes": value_bytes, "base_keys": base_keys, "steps": steps, "step_s": step_s,
           "line_ms": line_ms, "rate_rps": RATE, "miss_penalty_ms": MISS_PENALTY_MS, "native_mb": NATIVE_MB, "cover_mb": list(COVER_MB),
           "objective": objective, "dial": DIAL, "native": NATIVE, "redis_version": ver, "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, value_bytes, base_keys, steps, step_s, line_ms, seed=1000 + rep, objective=objective)
        rec["reps"].append(r)
        (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    rec["paired"] = {k: paired(rec["reps"], k, dr) for k, _, dr in GAUGES}
    (wl_dir / f"{name}.json").write_text(json.dumps(rec, indent=1))
    return rec


def fmt(v):
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "n/a"
    return f"{v:,.0f}" if abs(v) >= 100 else f"{v:,.3g}"


def report(recs, out: Path):
    shipped = bool(recs) and all(r.get("native") == "shipped" for r in recs)
    L = ["# Redis: Omni-Compass on top of a cache's " + ("memory as shipped (no ceiling)" if shipped else "operator-set memory ceiling"), "",
         ("Redis exactly as shipped, with no memory ceiling and noeviction, is native; with no ceiling the knob is at its limit on "
          "native, so omni reads and writes nothing, and every gauge is native's. Otherwise omni is the compass law on the ceiling "
          if shipped else
          f"Redis as shipped with the operator's ceiling ({recs[0]['native_mb'] if recs else NATIVE_MB} MB, allkeys-lru) is native; omni is the compass law on the ceiling ")
         + 
         f"through Redis's own console inside [{COVER_MB[0]}, {COVER_MB[1]}] MB, holding the application's own request latency at "
         f"{CENTER:.0%} of the {LINE_MS:.0f} ms line (a hit is inside, a miss and its {MISS_PENALTY_MS:.0f} ms store trip outside). The same "
         "requests in both arms. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is "
         "reported, losses included.", ""]
    for rec in recs:
        L += [f"## {rec['workload']}: {rec['value_bytes']} B values, working set {rec['base_keys']:,} keys × notch, steps {rec['steps']} × {rec['step_s']} s"
              + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"Redis {rec['redis_version']}; {rec['rate_rps']:.0f} requests a second offered; {len(rec['reps'])} paired repetitions; engine "
              f"{rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"]); fw = any(r["omni"]["foreign_writer"] for r in rec["reps"])
        L += ["", f"Every omni arm handed back to native's ceiling ({rec['native_mb'] or 'none'} MB): {'yes' if hb else 'NO'}; another writer seen: {'yes' if fw else 'no'}; "
              f"fail-ups: {sum(r['omni']['failups'] for r in rec['reps'])}.", ""]
    (out / "REDIS.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "REDIS.md"


def setup():
    """The workflow's Redis: the shipped binary, the operator's two settings (or, --native shipped, none: no ceiling and
    noeviction, as Redis ships), nothing else."""
    log = Path("/tmp/omni-redis.log")
    subprocess.run(["redis-server", "--port", str(PORT), "--daemonize", "yes", "--save", "", "--appendonly", "no", "--maxmemory", f"{NATIVE_MB}mb",
                    "--maxmemory-policy", POLICY[NATIVE], "--logfile", str(log), "--dir", "/tmp"], check=True)
    for _ in range(30):
        r = subprocess.run(["redis-cli", "-p", str(PORT), "ping"], capture_output=True, text=True)
        if r.stdout.strip() == "PONG":
            print(subprocess.run(["redis-server", "--version"], capture_output=True, text=True).stdout.strip()); return 0
        time.sleep(1)
    print("redis did not start", file=sys.stderr); return 1


def main(argv=None):
    global NATIVE, NATIVE_MB
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--native", default="operator", choices=("operator", "shipped"),
                    help="native: the operator's 64 MB ceiling with allkeys-lru (preregistered) or Redis exactly as shipped, no ceiling "
                         "and noeviction (the founder's order of 17 October); with no ceiling the knob is at its limit on native")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=20.0)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--out", default="redis-out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a step by: resource (the index's reading: work, speed, memory and CPU together) or service (work and speed alone)")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    NATIVE, NATIVE_MB = a.native, (0 if a.native == "shipped" else 64)
    if a.setup:
        return setup()
    out = Path(a.out)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("redis-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.line_ms, a.objective) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
