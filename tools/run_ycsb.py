#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass on top of a database's operator-set cache size: YCSB on MongoDB (docs/YCSB_PREREGISTRATION.md).

MongoDB as its publisher ships it, with the one setting an operator sets once for its storage engine's cache: the WiredTiger
cache size. YCSB (Yahoo's Cloud Serving Benchmark, the published core workloads) asks for records drawn from a key space that
widens and narrows over the run, so the working set steps through the operator's cache and past it. The operator's fixed
cache is the native controller here.

  native  MongoDB at the operator's cache size (512 MB) for the whole run
  omni    the same MongoDB, with the compass law (omnicompass/compass_law.py) on one knob, the cache size, through the
          server's own console (setParameter wiredTigerEngineRuntimeConfig cache_size), inside the cover [256 MB, 2,048 MB]:
          the compass reads the server's own mean read latency over the last second (serverStatus opLatencies) on a band from
          0 to the response line and holds it at 40% of the line; slow reads with the cache full and missing push the cache up
          (slow reads with room to spare, or in a cache that holds its working set, are not the cache's to mend), calm gives
          memory back 64 MB a second while the cache's misses are under one percent of the pages requested from it (amendment
          1: it holds the working set; the first counted set read "nothing evicted", which a cold cache satisfies while it fills);
          at 95% of the line with the cache full a quarter of the cover is added at once (fail up); the cache size is handed
          back to the operator's at the end and read back; a size found at a value Omni did not write stops it writing

Gauges from YCSB's own per-operation records (every operation's latency, raw), the server's own serverStatus (the cache
configured, the bytes in it, pages read into it) and the host's /proc/stat (CPU seconds, the compass's own cost included).
Memory held is the resource; no energy is claimed beyond the host's CPU seconds. Every row is reported, losses included.

  python3 tools/run_ycsb.py --setup                        # fetch and check YCSB, point the server at the operator's cache
  python3 tools/run_ycsb.py --workloads tuning --reps 3 --out DIR
  python3 tools/run_ycsb.py --report-only DIR              # re-read finished <workload>.json files and write YCSB.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import pathlib as _p; sys.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass.compass_law import Band, CompassLaw  # noqa: E402
from tools.knob_verdict import KnobVerdict, sample_cost, OBJECTIVES, RESOURCE as DEFAULT_OBJECTIVE  # noqa: E402  (amendment 2: the brain's own verdict)
from tools.store_brain import MemoryMax, read_meminfo  # noqa: E402  (omni-v22: the max on the cache)
from tools.readings import word as gel_word, aim as gel_aim, EVEN_SAME, EVEN_NOISE, SHOWN  # noqa: E402  (the words every table uses)

URL = os.environ.get("MONGO_URL", "mongodb://127.0.0.1:27017")
DB = "ycsb"
MB = 1024 * 1024
LINE_MS = 1.0             # the response line: an operation answered within 1 ms (set on the tuning workload's fourth smoke run, from 2 ms:
                          # on this stack a hit reads 0.15 to 0.24 ms and a miss 0.28 to 0.46 ms, so the 2 ms line kept every reading under the center)
CENTER = 0.4              # the compass holds the server's own read latency at 40% of the line
DT = 1.0                  # one decision a second
TAU = 2.0                 # memory given or taken shows in the misses within a couple of seconds
SMOOTH = 0.5
NATIVE_MB = 512           # the operator's cache (None with --native shipped: the server's own default, half of RAM less 1 GB)
NATIVE = "operator"
COVER_MB = (256, 2048)    # never under 256 MB (the server's own floor), never over 2 GB
STEP_MB = 64              # one notch of the knob
FAILUP_MB = 448           # past the wall: a quarter of the cover at once, and again the next second if still past it
DWELL_S = 5.0             # after growing, no taking back within five seconds; giving back is a notch a second
DIAL = os.environ.get("OMNI_DIAL", "max")   # omni-v22: max, the factory tune (the Brain); save, the tune-down (omni-v21's loop)
FULL = 0.8                # the cache counts as full when the bytes in it are 80% of its size or more (WiredTiger's own eviction_target, which
                          # its eviction workers hold the cache at), or when it evicted a page in the last second (store fix of 25 October:
                          # at 0.9 the cache read full in only 2 to 61 of about 460 seconds of every omni-v16 arm, so the grow path never opened)
RATE = 3000               # operations a second offered by YCSB (-target), the same in both arms
THREADS = 32              # YCSB's client threads
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
RECORD_BYTES = 1000       # YCSB's default: 10 fields of 100 bytes
DISTRIBUTION = "uniform"  # over the notch's key space, so the working set is the key space (see run_arm)
YCSB_VERSION = "0.17.0"
YCSB_URL = f"https://github.com/brianfrankcooper/YCSB/releases/download/{YCSB_VERSION}/ycsb-mongodb-binding-{YCSB_VERSION}.tar.gz"
YCSB_SHA256 = "6a054a706812269c80bfc6ed1e83457990c1c60b01f5083c873aaed05577e30d"   # recorded from the release before any run
YCSB_HOME = Path(os.environ.get("YCSB_HOME", str(Path.home() / f"ycsb-mongodb-binding-{YCSB_VERSION}")))
from omnicompass.student_t import T95  # noqa: E402  (the two-sided 95% point of Student's t, any degrees of freedom)
SAME_REL = 1e-6

WORKLOADS = {
    # name: (YCSB core workload file, base record count (keys at notch 1), steps, tuning?)
    #   250,000 records of 1 KB are about 275 MB in the cache at notch 1; notch 6 is about 1.6 GB, past the operator's 512 MB
    "tuning": ("workloada", 250_000, STEPS, True),      # 50/50 read/update, zipfian: the rules were set here
    "b": ("workloadb", 250_000, STEPS, False),          # 95/5 read/update, zipfian
    "c": ("workloadc", 250_000, STEPS, False),          # 100% read, zipfian
    "f": ("workloadf", 250_000, STEPS, False),          # read-modify-write, zipfian
    "burst": ("workloadb", 250_000, BURST, False),      # 95/5, the burst schedule
}

GAUGES = [  # key, label, direction
    ("work_inside_line_ops", "work inside the response line (operations a second answered within the line)", "higher"),
    ("ops", "throughput (operations a second)", "higher"),
    ("p95_ms", "latency, 95th percentile (ms)", "lower"),
    ("p99_ms", "latency, 99th percentile (ms)", "lower"),
    ("mean_ms", "latency, mean (ms)", "lower"),
    ("failed", "failed operations", "never more"),
    ("cache_mb_mean", "cache size held, mean (MB; the knob, the resource)", "spent"),
    ("cache_used_mb_mean", "bytes in the cache, mean (MB)", "spent"),
    ("pages_read", "pages read into the cache (misses)", "shown"),
    ("cpu_busy_share", "host CPU busy (share of the run)", "spent"),
    ("cpu_seconds", "host CPU-seconds", "spent"),
    ("cpu_s_per_1k_inside", "host CPU-seconds per 1,000 operations inside the line", "spent"),
    ("writes", "cache size changes written (the knob's moves)", "shown"),
    # store fix of 25 October: the CPU apart, beside the host figure (old runs lack these rows; the readers prefer process_cpu_seconds)
    ("process_cpu_seconds", "the store's and the harness's own CPU-seconds (mongod plus the compass and its sampler; steal excluded)", "spent"),
    ("server_cpu_seconds", "the server's own CPU-seconds (mongod)", "shown"),
    ("harness_cpu_seconds", "the harness's own CPU-seconds (the compass's brain in the omni arm, the sampler in both)", "shown"),
    ("host_cpu_seconds_no_steal", "host CPU-seconds without steal (the load generator included)", "shown"),
    ("steal_seconds", "CPU-seconds the hypervisor took (steal), host-wide", "shown"),
]
OPTIONAL_GAUGES = ("process_cpu_seconds", "server_cpu_seconds", "harness_cpu_seconds", "host_cpu_seconds_no_steal", "steal_seconds")  # absent from runs before 25 October
# the serverStatus sections the brain and the sampler read (store fix of 25 October: every other section is asked away, so the
# one-a-second reading no longer has the server build, and Python decode, the whole document)
STATUS_SECTIONS = ("wiredTiger", "opLatencies")


def lean_status_command(full_doc, keep=STATUS_SECTIONS):
    """The serverStatus command that asks only for the sections kept: every other section the server reported in a full
    document (a sub-document at the top level) is asked away with 0, so only names the server itself gave are sent."""
    cmd = {"serverStatus": 1}
    for k, v in full_doc.items():
        if isinstance(v, dict) and k not in keep:
            cmd[k] = 0
    return cmd


class LeanStatus:
    """serverStatus once in full, then only the sections the brain reads (STATUS_SECTIONS)."""

    def __init__(self, client):
        self.c, self.cmd = client, None

    def __call__(self):
        if self.cmd is None:
            full = self.c.admin.command("serverStatus")
            self.cmd = lean_status_command(full)
            return full
        return self.c.admin.command(dict(self.cmd))


class CacheSize:
    """The plug on the server's cache size: read once before the first write, write through the server's own console, read
    back, yield to any other writer, restore."""

    def __init__(self, client):
        self.c, self.snapshot, self.last_written = client, None, None
        self.status = LeanStatus(client)

    def _status(self):
        return self.status()

    def configured_mb(self, st=None):
        st = st or self._status()
        return int(st["wiredTiger"]["cache"]["maximum bytes configured"]) // MB

    def attach(self):
        self.snapshot = self.configured_mb(); self.last_written = self.snapshot
        return self.snapshot

    def lever(self, st=None):
        cur = self.configured_mb(st)
        if self.last_written is not None and cur != self.last_written:
            raise RuntimeError(f"another writer set the cache to {cur} MB (we wrote {self.last_written}): Omni stops writing")
        return cur

    def write(self, mb):
        self.c.admin.command({"setParameter": 1, "wiredTigerEngineRuntimeConfig": f"cache_size={int(mb)}M"})
        back = self.configured_mb(); self.last_written = back
        return back

    def restore(self):
        try:
            self.c.admin.command({"setParameter": 1, "wiredTigerEngineRuntimeConfig": f"cache_size={int(self.snapshot)}M"})
            return self.configured_mb() == self.snapshot
        except Exception:
            return False


def cache_stats(st):
    """(configured MB, bytes in cache MB, pages read into cache, pages evicted, pages requested from the cache) from one serverStatus."""
    c = st["wiredTiger"]["cache"]
    evicted = sum(int(c.get(k, 0)) for k in ("unmodified pages evicted", "modified pages evicted", "pages evicted by application threads"))
    return (int(c["maximum bytes configured"]) // MB, int(c["bytes currently in the cache"]) / MB, int(c.get("pages read into cache", 0)), evicted,
            int(c.get("pages requested from the cache", 0)))


def miss_share(pages_read_last_s, requested_last_s):
    """The cache's misses as a share of the pages requested from it in the last second; no request reads as no miss."""
    return pages_read_last_s / requested_last_s if requested_last_s > 0 else 0.0


# omni-v22: the server's own account of what a cache miss costs: WiredTiger's time reading pages from disk for the application's
# threads (the reads that stood in a request's way; the server's own eviction and read-ahead threads are not counted), in
# microseconds, beside the server's own read latency (opLatencies, microseconds).
MISS_TIME_KEY = "application threads page read from disk to cache time (usecs)"
MISS_COUNT_KEY = "application threads page read from disk to cache count"
REQUIRED_CACHE_KEYS = ("maximum bytes configured", "bytes currently in the cache", "pages read into cache", "pages requested from the cache",
                       MISS_TIME_KEY, MISS_COUNT_KEY)


def miss_time(st):
    """(the application threads' page reads from disk, their time in microseconds) from one serverStatus; None where the server
    gives no account of them (the attach check stops a run on such a server before it starts)."""
    c = st["wiredTiger"]["cache"]
    if MISS_TIME_KEY not in c:
        return None, None
    return int(c.get(MISS_COUNT_KEY, 0)), int(c[MISS_TIME_KEY])


def read_latency(st):
    """(total read latency in microseconds, read operations) from one serverStatus (opLatencies)."""
    r = st["opLatencies"]["reads"]
    return int(r["latency"]), int(r["ops"])


GIVEBACK_MISS_SHARE = 0.01  # amendment 1: a notch is given back only while the cache's misses (pages read into it) are under 1% of the pages
                            # requested from it in the last second (the cache holds the working set). The first counted set read "no page
                            # evicted in the last second", which a cold cache satisfies while it fills: every give-back of every burst arm came
                            # in the first seconds, and the cache then sat at the floor of the cover, evicting, for the rest of the arm.
GROW_MISS_SHARE = GIVEBACK_MISS_SHARE  # and the cache grows only while missing (1% or more): a full cache that holds its working set cannot mend a slow read


def cache_full(used_mb, cur_mb, evicted_last_s=0):
    """The cache is full when the bytes in it reach WiredTiger's own eviction target (FULL of its size) or it evicted a page in
    the last second (store fix of 25 October)."""
    return used_mb >= FULL * cur_mb or (evicted_last_s or 0) > 0


def decide(p, force, miss_share_last_s, cur_mb, last_change_age, full, wall=0.95, reads=True, native_mb=None):
    """The knob's move this second, in MB: slow reads (the service slow) grow the cache by ceil(force / 0.1) notches, but only
    while the cache is full (a slow read with room to spare is not the cache's to mend) and missing (amendment 1: misses at one
    percent of its requests or more); calm with the cache's misses under one percent of its requests (it holds the working set)
    gives back one notch after the dwell, and only in a second that requested pages (a second with none says nothing about the
    working set); past the wall, with the cache full, a quarter of the cover at once.
    Store fix of 25 October, the queue line of the database wire (docs/POSTGRES_PREREGISTRATION.md, amendment 2) for the cache:
    below the operator's own size (native_mb), a second that requested pages with misses at one percent of its requests or more
    adds one notch back, up to the operator's size, with no slow or full condition (a size below native's that misses no longer
    holds the working set; the omni-v16 runs held the cache at 448 MB to the end of two arms with misses at 9 to 13%)."""
    target, why = _decide(p, force, miss_share_last_s, cur_mb, last_change_age, full, wall, reads)
    if native_mb is not None and cur_mb < native_mb and reads and miss_share_last_s >= GROW_MISS_SHARE:
        back = min(native_mb, cur_mb + STEP_MB)
        if back > target:
            return back, f"missing below the operator's size ({100 * miss_share_last_s:.1f}% of requests): a notch added back, up to the operator's own size"
    return target, why


def _decide(p, force, miss_share_last_s, cur_mb, last_change_age, full, wall=0.95, reads=True):
    """The rule before the store fix (the slow, calm and wall moves); decide() adds the hand-back below native."""
    lo, hi = COVER_MB
    if p is not None and p >= wall and full:
        return min(hi, cur_mb + FAILUP_MB), "fail up: the line is at hand and the cache is full, a quarter of the cover at once"
    if force > 0.05:
        if not full:
            return cur_mb, "slow with room to spare: not the cache's to mend"
        if miss_share_last_s < GROW_MISS_SHARE:
            return cur_mb, "slow with the cache full but holding its working set (misses under 1% of requests): not the cache's to mend"
        return min(hi, cur_mb + STEP_MB * max(1, math.ceil(force / 0.1))), "slow with the cache full and missing: grow"
    if force < -0.05 and not reads:
        return cur_mb, "calm, but no page requested in the last second: nothing known, nothing taken"
    if force < -0.05 and miss_share_last_s < GIVEBACK_MISS_SHARE and cur_mb > lo and last_change_age >= DWELL_S:
        return max(lo, cur_mb - STEP_MB), "calm, the cache holding the working set (misses under 1% of requests): a notch given back"
    return cur_mb, "hold"


# omni-v22: the max on the WiredTiger cache (docs/YCSB_PREREGISTRATION.md, amendment 5; docs/STORE_ROOT_CAUSES_2026-10-30.md): the
# wire's own rule (decide) with the spend never clamped by an allowance where the server's own account says the misses cost the
# reads (WiredTiger's time reading pages from disk for the application's threads against the server's own read latency:
# tools/store_brain.py), held where they cost nothing (on a runner whose page cache holds the data files a cache miss is a read from
# memory: 12% to 16% of pages missing with the read latency unmoved), held while the host has no notch to spare, and no give-back
# below the working set's floor nor below the operator's cache. `--dial save` keeps omni-v21's loop, the verdict under the resource
# objective, where giving memory back is the aim.
METER = "WiredTiger's time reading pages from disk for the application's threads against the server's own read latency"


class Brain:
    """The knob's decision, one a second: obs holds reading_s (the mean read latency), reads (operations this second), miss_share,
    cache_mb, used_mb, full, requested (any page requested this second), cpu_share, miss_time_s (the application threads' time
    reading pages from disk this second), service_time_s (the reads' own latency summed this second), host_avail_mb and
    host_total_mb (the host's memory, None unread)."""

    def __init__(self, native, objective=DEFAULT_OBJECTIVE, line_ms=LINE_MS):
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
        reading, cur = obs["reading_s"], obs["cache_mb"]
        f = self.law.force(reading)
        want, why = decide(self.law.p, f, obs["miss_share"], cur, t - self.last_change, obs["full"], wall=self.law.band.wall_high,
                           reads=obs.get("requested", True), native_mb=self.native)
        target, why, info = self.max.step(t, want, why, cur, obs["used_mb"], obs.get("miss_time_s"), obs.get("service_time_s"),
                                          obs.get("host_avail_mb"), obs.get("host_total_mb"), fail_up=why.startswith("fail up"))
        info.update({"p": round(self.law.p, 4), "force": round(f, 4)})
        return target, why, info


class Omni(threading.Thread):
    """The brain, one decision a second, reading the server's own read latency, writing the audit; the knob is handed back at
    the end and read back. Amendment 2 (the brain's own verdict, 2026-10-09): the cache starts in watch and is written only
    inside the allowance a paired trial on the server itself has earned under the declared objective (tools/knob_verdict.py
    around the engine's own Verdict), one notch a trial; a trial holds the cache; a fail-up never spends beyond the allowance."""

    def __init__(self, plug: CacheSize, audit_path: Path, line_ms=LINE_MS, objective=DEFAULT_OBJECTIVE, dial=DIAL):
        super().__init__(daemon=True)
        self.plug, self.audit, self.objective = plug, audit_path, objective
        self.law = CompassLaw(Band(0.0, line_ms / 1000.0, center=CENTER), dt=DT, tau=TAU, smooth=SMOOTH)
        self.stop_flag = threading.Event(); self.last_change = -1e9; self.writes = 0; self.failups = 0
        self.foreign = False; self.handed_back = False; self.error = None; self.verdict = None; self.brain = None; self.dial = dial; self.line_ms = line_ms

    def govern_record(self):
        """The record of what governed the knob: the max's counts (omni-v22) or the verdict's allowance (the tune-down)."""
        if self.brain is not None:
            return self.brain.record()
        return self.verdict.record() if self.verdict else None

    def run(self):
        try:
            native = self.plug.attach(); st = self.plug._status(); lat0, ops0 = read_latency(st); _, _, rd0, ev0, rq0 = cache_stats(st)
            mr0, mt0 = miss_time(st)
            if native > COVER_MB[1]:
                # MongoDB as shipped (its default, half of RAM less 1 GB) holds more cache than the most Omni may set: the knob
                # is at its limit on native, and any size Omni wrote would sit below native (the max never goes below native)
                self.audit.write_text(json.dumps({"t": 0.0, "cache_mb": native, "why": "native's cache is above the cover: at its "
                                                  "limit on native, nothing written"}) + "\n")
                self.stop_flag.wait()
                self.handed_back = self.plug.restore()
                return
        except Exception as e:                                      # the brain never ran: say so in the audit and the record, never silently
            self.error = repr(e)
            self.audit.write_text(json.dumps({"t": 0.0, "error": self.error, "note": "the brain could not attach; no decision was made"}) + "\n")
            return
        t0 = time.monotonic(); cpu_prev = cpu_times()
        self.verdict = KnobVerdict(native, STEP_MB, COVER_MB, objective=self.objective, settle_s=TAU)
        if self.dial == "max":
            self.brain = Brain(native, self.objective, self.line_ms); self.verdict = None
        with open(self.audit, "w") as fh:
            while not self.stop_flag.is_set():
                tick = time.monotonic()
                try:
                    st = self.plug._status()
                    lat, ops = read_latency(st); dl, do = lat - lat0, ops - ops0; lat0, ops0 = lat, ops
                    mr, mt = miss_time(st)
                    mr_last, mt_last = (None, None) if mt is None else (mr - mr0, mt - mt0); mr0, mt0 = mr, mt
                    reading = (dl / do / 1e6) if do > 0 else 0.0           # the mean read latency of the last second, in seconds; no reads reads calm
                    f = self.law.force(reading)
                    cur, used, rd, ev, rq = cache_stats(st); ev_last = ev - ev0; ev0 = ev
                    rd_last = rd - rd0; rd0 = rd; rq_last = rq - rq0; rq0 = rq
                    share = miss_share(rd_last, rq_last)
                    cur = self.plug.lever(st); full = cache_full(used, cur, ev_last)
                    cpu_now = cpu_times(); d_total = cpu_now[0] - cpu_prev[0]; d_idle = cpu_now[1] - cpu_prev[1]; cpu_prev = cpu_now
                    cpu_share = (1.0 - d_idle / d_total) if d_total > 0 else None
                    cost = sample_cost(self.objective, do, reading if do > 0 else None, cur, cpu_share)
                    if self.brain is not None:                                           # the max (omni-v22)
                        h_avail, h_total = read_meminfo()
                        obs = {"reading_s": reading, "reads": do, "miss_share": share, "cache_mb": cur, "used_mb": used, "full": full,
                               "requested": rq_last > 0, "cpu_share": cpu_share,
                               "miss_time_s": None if mt_last is None else mt_last / 1e6, "service_time_s": dl / 1e6,
                               "host_avail_mb": h_avail, "host_total_mb": h_total}
                        self.brain.last_change = self.last_change - t0
                        target, why, vinfo = self.brain.step(tick - t0, obs)
                        vinfo["disk_reads_last_s"] = mr_last
                        self.failups = self.brain.failups
                    else:                                                                # the tune-down: omni-v21's loop
                        self.verdict.observe(cost, tick - t0)                               # measured under the cache of the last second
                        target, why = decide(self.law.p, f, share, cur, tick - self.last_change, full, wall=self.law.band.wall_high, reads=rq_last > 0,
                                             native_mb=native)
                        missing_below = cur < native and rq_last > 0 and share >= GROW_MISS_SHARE     # the size below native no longer holds the working set
                        target, why, vinfo = self.verdict.decide(
                            target, spend_ok=(f > 0.05 and full and share >= GROW_MISS_SHARE),
                            give_ok=(f < -0.05 and rq_last > 0 and share < GIVEBACK_MISS_SHARE),
                            t=tick - t0, why=why, stress=(f > 0.05 or missing_below), calm=f < -0.05, fail_up=why.startswith("fail up"))
                    wrote = None
                    if target != cur:
                        wrote = self.plug.write(target); self.writes += 1
                        if target > cur:
                            self.last_change = tick
                        if why.startswith("fail up") and self.brain is None:
                            self.failups += 1
                    fh.write(json.dumps({"t": round(tick - t0, 2), "reading_ms": round(reading * 1000, 3), "reads": do, "p": round(self.law.p, 4), "force": round(f, 4),
                                         "evicted_last_s": ev_last, "pages_read_last_s": rd_last, "pages_requested_last_s": rq_last, "miss_share": round(share, 4),
                                         "cache_mb": cur, "used_mb": round(used, 1), "full": full, "target_mb": target, "wrote_mb": wrote,
                                         "cpu_share": None if cpu_share is None else round(cpu_share, 4), "cost": None if cost is None else round(cost, 9),
                                         **vinfo, "why": why}) + "\n")
                except Exception as e:
                    fh.write(json.dumps({"t": round(tick - t0, 2), "error": repr(e)}) + "\n")
                    self.foreign = True
                    break
                time.sleep(max(0.0, DT - (time.monotonic() - tick)))
        self.handed_back = self.plug.restore()


class Sampler(threading.Thread):
    """The cache configured, the bytes in it and the pages read into it, once a second, in both arms."""

    def __init__(self, client):
        super().__init__(daemon=True)
        self.c, self.stop_flag, self.rows = client, threading.Event(), []
        self.status = LeanStatus(client)

    def run(self):
        while not self.stop_flag.is_set():
            try:
                self.rows.append(cache_stats(self.status()))
            except Exception:
                pass
            time.sleep(DT)


def cpu_times():
    with open("/proc/stat") as fh:
        f = fh.readline().split()
    vals = list(map(int, f[1:]))
    return sum(vals), vals[3] + vals[4]


# --- the CPU apart (store fix of 25 October) -------------------------------------------------------------------------
# The host figure above (kept, so every older table reads the same) counts every field but idle and iowait as busy: steal (the
# hypervisor's), and guest twice. Beside it: the host's busy time without steal, the steal itself, the server's own CPU from
# its /proc/<pid>/stat and the harness's own from getrusage, so the store's work and the compass's cost are read apart from
# the load generator, the runner's own processes and the machine's neighbours.
def host_cpu_split(line=None):
    """(busy jiffies without steal or guest, steal jiffies) from /proc/stat's cpu line (or the line given)."""
    if line is None:
        with open("/proc/stat") as fh:
            line = fh.readline()
    v = [int(x) for x in line.split()[1:]] + [0] * 10
    user, nice, system, idle, iowait, irq, softirq, steal = v[:8]
    return user + nice + system + irq + softirq, steal        # guest and guest_nice are already inside user and nice


def pid_of(name):
    """The oldest process whose command name is `name` (its /proc/<pid>/comm), or None."""
    best = None
    for d in Path("/proc").iterdir():
        if d.name.isdigit():
            try:
                if (d / "comm").read_text().strip() == name:
                    pid = int(d.name)
                    best = pid if best is None or pid < best else best
            except OSError:
                continue
    return best


def proc_cpu_jiffies(pid, stat_text=None):
    """utime + stime (jiffies) of one process from /proc/<pid>/stat (or the text given); None when it is gone."""
    try:
        txt = stat_text if stat_text is not None else Path(f"/proc/{pid}/stat").read_text()
    except (OSError, TypeError):
        return None
    rest = txt[txt.rindex(")") + 2:].split()                    # after the command name, which may hold spaces
    return int(rest[11]) + int(rest[12])                        # fields 14 and 15 of the stat line


class CpuApart:
    """The CPU of one arm apart: start() before the load, stop() after; figures in seconds."""

    def __init__(self, server_name):
        self.server_name = server_name

    def _read(self):
        import resource
        pid = pid_of(self.server_name)
        own = resource.getrusage(resource.RUSAGE_SELF)
        busy, steal = host_cpu_split()
        return {"pid": pid, "server": proc_cpu_jiffies(pid) if pid else None, "harness": own.ru_utime + own.ru_stime, "busy": busy, "steal": steal}

    def start(self):
        self.a = self._read()
        return self

    def stop(self):
        b, a, tck = self._read(), self.a, os.sysconf("SC_CLK_TCK")
        server = (b["server"] - a["server"]) / tck if (a["server"] is not None and b["server"] is not None and a["pid"] == b["pid"]) else None
        harness = b["harness"] - a["harness"]
        return {"server_cpu_seconds": server, "harness_cpu_seconds": harness,
                "process_cpu_seconds": (server + harness) if server is not None else None,
                "host_cpu_seconds_no_steal": (b["busy"] - a["busy"]) / tck, "steal_seconds": (b["steal"] - a["steal"]) / tck}


def parse_raw(path: Path):
    """YCSB's raw measurements: one line per operation, 'op, timestamp(ms), latency(us)'; returns [(t_s, latency_ms)]."""
    out = []
    if not path.exists():
        return out
    for line in path.read_text().splitlines():
        parts = [x.strip() for x in line.split(",")]
        if len(parts) < 3 or not parts[2].lstrip("-").isdigit():
            continue
        try:
            out.append((float(parts[1]) / 1000.0, float(parts[2]) / 1000.0))
        except ValueError:
            continue
    return out


def parse_failed(summary_text):
    """Failed operations from YCSB's summary: every '[<OP>-FAILED], Operations, n' line."""
    n = 0
    for line in summary_text.splitlines():
        p = [x.strip() for x in line.split(",")]
        if len(p) >= 3 and p[0].endswith("-FAILED]") and p[1] == "Operations":
            try:
                n += int(p[2])
            except ValueError:
                pass
    return n


def ycsb(cmd, workload_file, props, out_file: Path):
    """One YCSB invocation (load or run) with raw per-operation measurements written to out_file; returns its summary text."""
    out_file = Path(out_file).resolve(); out_file.parent.mkdir(parents=True, exist_ok=True)   # YCSB runs from its own home: absolute paths
    args = ["bash", str(YCSB_HOME / "bin" / "ycsb.sh"), cmd, "mongodb", "-s", "-P", str(YCSB_HOME / "workloads" / workload_file),
            "-p", f"mongodb.url={URL}/{DB}?w=1", "-p", "measurementtype=raw", "-p", f"measurement.raw.output_file={out_file}"]
    for k, v in props.items():
        args += ["-p", f"{k}={v}"]
    r = subprocess.run(args, capture_output=True, text=True, cwd=str(YCSB_HOME))
    return r.stdout + "\n" + r.stderr


def load_dataset(workload_file, records, log: Path):
    """The dataset for a workload, loaded once per workload (both arms read the same records); the collection is dropped first."""
    import pymongo
    c = pymongo.MongoClient(URL); c.drop_database(DB); c.close()
    txt = ycsb("load", workload_file, {"recordcount": records, "threads": THREADS, "insertorder": "ordered"}, log.with_suffix(".raw"))
    log.write_text(txt)
    if "[OVERALL]" not in txt:
        raise RuntimeError(f"YCSB load failed: {txt[-2000:]}")


def server_journal(unit):
    """The server's own journal and status, for the record when a restart does not come back (20 October: the omni-v12
    MongoDB runs B and C died at this wait with an empty mongod.log and nothing else recorded)."""
    out = []
    for cmd in (["sudo", "systemctl", "status", unit, "--no-pager", "-l"], ["sudo", "journalctl", "-u", unit, "--no-pager", "-n", "80"]):
        r = subprocess.run(cmd, capture_output=True, text=True)
        out.append(" ".join(cmd) + "\n" + (r.stdout + r.stderr)[-6000:])
    return "\n".join(out)


def fresh_server(cache_mb):
    """The cache emptied and the operator's size restored before an arm, both arms alike: the server restarted at the
    operator's configured size, the OS page cache dropped. A server that has not answered five minutes after its restart is
    restarted once more, with its journal printed; one that has not answered after that stops the run with the journal in the
    error, so the cause is in the record (never a bare "did not come back")."""
    import pymongo
    for attempt in (1, 2):
        subprocess.run(["sudo", "systemctl", "restart", "mongod"], check=True)
        subprocess.run(["sudo", "sh", "-c", "sync; echo 3 > /proc/sys/vm/drop_caches"], check=False)
        for _ in range(100):                                           # about five minutes: 2 s to select a server, 1 s between tries
            try:
                c = pymongo.MongoClient(URL, serverSelectionTimeoutMS=2000); st = c.admin.command("serverStatus")
                got = int(st["wiredTiger"]["cache"]["maximum bytes configured"]) // MB
                if cache_mb is not None and got != cache_mb:                 # None: MongoDB's own default, as shipped
                    c.admin.command({"setParameter": 1, "wiredTigerEngineRuntimeConfig": f"cache_size={cache_mb}M"})
                return c
            except Exception:
                time.sleep(1)
        journal = server_journal("mongod")
        print(f"mongod did not answer five minutes after its restart (attempt {attempt} of 2); its status and journal:\n{journal}", flush=True)
    raise RuntimeError("mongod did not come back after two restarts; its status and journal are printed above")


def run_arm(arm, wl_dir: Path, rep, workload_file, base, steps, step_s, line_ms, seed, objective=DEFAULT_OBJECTIVE):
    import pymongo
    d = wl_dir / f"rep-{rep}" / arm; d.mkdir(parents=True, exist_ok=True)
    c = fresh_server(NATIVE_MB)
    native_now = int(c.admin.command("serverStatus")["wiredTiger"]["cache"]["maximum bytes configured"]) // MB   # native's size, read
    sampler = Sampler(pymongo.MongoClient(URL)); sampler.start()
    omni = None
    if arm == "omni":
        omni = Omni(CacheSize(pymongo.MongoClient(URL)), d / "audit.jsonl", line_ms, objective); omni.start()
    records, failed, summaries = [], 0, []
    apart = CpuApart("mongod").start()
    cpu0 = cpu_times(); t0 = time.time()
    for i, notch in enumerate(int(s) for s in steps.split()):
        raw = d / f"notch-{i + 1}.raw"
        # the notch's key space: the first base x notch records of the loaded dataset, drawn uniformly, so the working set IS the
        # key space (YCSB's shipped zipfian keeps the hot set in a few megabytes whatever the key space: the smoke run showed the
        # cache never filling); the workload's read/update mix stays as shipped
        txt = ycsb("run", workload_file, {"recordcount": base * notch, "operationcount": 10 ** 9, "maxexecutiontime": int(step_s), "target": RATE,
                                          "threads": THREADS, "insertstart": 0, "insertorder": "ordered", "requestdistribution": DISTRIBUTION,
                                          "seed": seed * 100 + i}, raw)      # ordered keys, as loaded: a hashed key space would read records that are not there
        got = parse_raw(raw); summaries.append(txt); failed += parse_failed(txt); records += got
        lat = sorted(l for _, l in got); row = sampler.rows[-1] if sampler.rows else (native_now, 0.0, 0, 0, 0)
        print(f"   {arm} rep {rep} notch {notch}: {len(lat)} ops, mean {sum(lat) / max(1, len(lat)):.3f} ms, p95 {(lat[int(0.95 * len(lat))] if lat else float('nan')):.3f} ms, "
              f"inside the line {100 * sum(1 for l in lat if l <= line_ms) / max(1, len(lat)):.1f}%, cache {row[0]:.0f} MB, in cache {row[1]:.0f} MB", flush=True)
    t1 = time.time(); cpu1 = cpu_times(); cpu_apart = apart.stop()
    if omni:
        omni.stop_flag.set(); omni.join(timeout=30)
    sampler.stop_flag.set(); sampler.join(timeout=5)
    (d / "ycsb.log").write_text("\n\n".join(summaries))
    seconds = t1 - t0
    lat_sorted = sorted(l for _, l in records); n = len(lat_sorted)
    def q(p):
        return lat_sorted[min(n - 1, int(p * n))] if n else float("nan")
    inside = sum(1 for l in lat_sorted if l <= line_ms)
    rows = sampler.rows or [(native_now, 0.0, 0, 0)]
    total = cpu1[0] - cpu0[0]; idle = cpu1[1] - cpu0[1]; cpu_s = (total - idle) / os.sysconf("SC_CLK_TCK")
    g = {"arm": arm, "rep": rep, "seconds": round(seconds, 1), "operations": n,
         "work_inside_line_ops": inside / seconds, "ops": n / seconds, "p95_ms": q(0.95), "p99_ms": q(0.99),
         "mean_ms": (sum(lat_sorted) / n) if n else float("nan"), "failed": failed,
         "cache_mb_mean": sum(x[0] for x in rows) / len(rows), "cache_used_mb_mean": sum(x[1] for x in rows) / len(rows),
         "pages_read": rows[-1][2] - rows[0][2], "cpu_busy_share": (total - idle) / max(1, total), "cpu_seconds": cpu_s,
         "cpu_s_per_1k_inside": 1000.0 * cpu_s / max(1, inside), "writes": (omni.writes if omni else 0),
         "handed_back": (omni.handed_back if omni else True), "foreign_writer": (omni.foreign if omni else False), "failups": (omni.failups if omni else 0),
         "controller_error": (omni.error if omni else None),
         **cpu_apart,
         "verdict": (omni.govern_record() if omni else None)}
    (d / "arm.json").write_text(json.dumps(g, indent=1))
    print(f"   {arm} rep {rep}: {n} operations, inside the line {g['work_inside_line_ops']:.0f}/s, p95 {g['p95_ms']:.2f} ms, cache {g['cache_mb_mean']:.0f} MB, "
          f"in cache {g['cache_used_mb_mean']:.0f} MB, pages read {g['pages_read']:,}, CPU {cpu_s:.1f} s, handed back {g['handed_back']}"
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


def server_version():
    try:
        import pymongo
        return pymongo.MongoClient(URL).server_info().get("version", "?")
    except Exception:
        return "?"


def run_workload(name, out: Path, reps, step_s, line_ms, objective=DEFAULT_OBJECTIVE):
    workload_file, base, steps, tuning = WORKLOADS[name]
    wl_dir = out / f"ycsb-{name}"; wl_dir.mkdir(parents=True, exist_ok=True)
    ver = server_version()
    top = max(int(s) for s in steps.split())
    print(f"== {name}: YCSB {workload_file}, {base:,} records x notch (loaded to notch {top}: {base * top:,}), steps {steps}, {step_s} s a notch, MongoDB {ver}, "
          f"the verdict's objective {objective}", flush=True)
    c0 = fresh_server(NATIVE_MB)
    have = c0.admin.command("serverStatus")["wiredTiger"]["cache"]
    for key in REQUIRED_CACHE_KEYS:
        if key not in have:                                        # the brain reads these; a server that lacks one must stop the run, not run native in Omni's name
            raise SystemExit(f"serverStatus().wiredTiger.cache has no '{key}' on this server: the brain's account of a miss cannot be read")
    load_dataset(workload_file, base * top, wl_dir / "load.log")
    rec = {"workload": name, "tuning": tuning, "ycsb_workload": workload_file, "base_records": base, "steps": steps, "step_s": step_s,
           "line_ms": line_ms, "rate_ops": RATE, "threads": THREADS, "record_bytes": RECORD_BYTES, "native": NATIVE,
           "native_mb": NATIVE_MB if NATIVE_MB is not None else int(have["maximum bytes configured"]) // MB, "cover_mb": list(COVER_MB),
           "mongodb_version": ver, "ycsb_version": YCSB_VERSION, "ycsb_sha256": YCSB_SHA256, "objective": objective, "dial": DIAL, "engine": engine(), "reps": []}
    for rep in range(1, reps + 1):
        order = ("native", "omni") if rep % 2 else ("omni", "native")
        r = {}
        for arm in order:
            r[arm] = run_arm(arm, wl_dir, rep, workload_file, base, steps, step_s, line_ms, seed=1000 + rep, objective=objective)
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
    native_mb = recs[0]["native_mb"] if recs else NATIVE_MB
    L = ["# YCSB on MongoDB: Omni-Compass on top of a database's " + ("cache as shipped" if shipped else "operator-set cache size"), "",
         (f"MongoDB exactly as shipped, its WiredTiger cache at the server's own default ({native_mb} MB on this machine), is native; "
          "a cache above the cover is at its limit on native, and omni then reads and writes nothing. Otherwise omni is the compass law on the cache size "
          if shipped else f"MongoDB as shipped with the operator's WiredTiger cache ({native_mb} MB) is native; omni is the compass law on the cache size ")
         + 
         f"through the server's own console inside [{COVER_MB[0]}, {COVER_MB[1]}] MB, holding the server's own read latency at {CENTER:.0%} of "
         f"the {LINE_MS:.0f} ms line. YCSB's published core workloads, the same operations in both arms, the key space stepping through the "
         "cache and past it. Memory held is the resource; the host's CPU seconds include the compass's own cost. Every row is reported, "
         "losses included.", ""]
    for rec in recs:
        L += [f"## {rec['workload']}: YCSB {rec['ycsb_workload']}, {rec['base_records']:,} records × notch, steps {rec['steps']} × {rec['step_s']} s"
              + (" (the tuning workload)" if rec.get("tuning") else ""), "",
              f"MongoDB {rec['mongodb_version']}, YCSB {rec['ycsb_version']}; {rec['rate_ops']:,} operations a second offered from {rec['threads']} threads; "
              f"{len(rec['reps'])} paired repetitions; engine {rec['engine']['version']} at `{rec['engine']['commit']}`.", "",
              "| Gauge | native | omni | change | 95% interval of the difference | reading |", "|---|---:|---:|---:|---:|---|"]
        for k, label, direction in GAUGES:
            p = rec.get("paired", {}).get(k)
            if not p:
                continue
            ch = "" if p["native"] == 0 else f"{100 * p['diff'] / abs(p['native']):+.1f}%"
            L.append(f"| {label} | {fmt(p['native'])} | {fmt(p['omni'])} | {ch} | {fmt(p['ci95'][0])} to {fmt(p['ci95'][1])} | {p['reading']} |")
        hb = all(r["omni"]["handed_back"] for r in rec["reps"]); fw = any(r["omni"]["foreign_writer"] for r in rec["reps"])
        L += ["", f"Every omni arm handed back to the operator's cache size: {'yes' if hb else 'NO'}; another writer seen: {'yes' if fw else 'no'}; "
              f"fail-ups: {sum(r['omni']['failups'] for r in rec['reps'])}.", ""]
    (out / "YCSB.md").write_text("\n".join(_legal_stamp(L)) + "\n")
    return out / "YCSB.md"


def setup():
    """YCSB fetched from the project's release and checked against the SHA-256 recorded before any run; the server pointed at
    the operator's cache (its configuration file) and restarted. MongoDB itself is installed by the workflow from its publisher's
    repository, signed by the publisher's key."""
    tgz = YCSB_HOME.parent / f"ycsb-mongodb-binding-{YCSB_VERSION}.tar.gz"
    if not tgz.exists():
        urllib.request.urlretrieve(YCSB_URL, tgz)
    got = hashlib.sha256(tgz.read_bytes()).hexdigest()
    if got != YCSB_SHA256:
        print(f"YCSB checksum mismatch: {got} (expected {YCSB_SHA256})", file=sys.stderr); return 1
    if not YCSB_HOME.exists():
        subprocess.run(["tar", "xzf", str(tgz), "-C", str(YCSB_HOME.parent)], check=True)
    conf = Path("/etc/mongod.conf")
    if conf.exists():
        txt = conf.read_text()
        if NATIVE_MB is not None and "cacheSizeGB" not in txt:            # --native shipped: the server's own default stands
            txt = txt.replace("storage:\n", f"storage:\n  wiredTiger:\n    engineConfig:\n      cacheSizeGB: {NATIVE_MB / 1024:.3f}\n", 1)
            subprocess.run(["sudo", "tee", str(conf)], input=txt, text=True, check=True, capture_output=True)
        subprocess.run(["sudo", "systemctl", "restart", "mongod"], check=True)
    ver = server_version()
    print(f"YCSB {YCSB_VERSION} at {YCSB_HOME} (sha256 {got[:16]}...); MongoDB {ver} at native's cache ({NATIVE}: "
          f"{NATIVE_MB if NATIVE_MB is not None else 'the server default'} MB)")
    if ver == "?":                       # the server did not answer after its restart: no workload runs on a server that is not up
        print(f"mongod did not answer after the restart at native's cache (kernel {os.uname().release}); its status and journal:\n"
              f"{server_journal('mongod')}", file=sys.stderr)
        return 1
    return 0


def main(argv=None):
    global NATIVE, NATIVE_MB
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--setup", action="store_true")
    ap.add_argument("--native", default="operator", choices=("operator", "shipped"),
                    help="native: the operator's 512 MB cache (preregistered) or MongoDB exactly as shipped, its own default cache "
                         "(the founder's order of 17 October); a native cache above the cover is at its limit on native")
    ap.add_argument("--workloads", default="tuning")
    ap.add_argument("--reps", type=int, default=3)
    ap.add_argument("--step-s", type=float, default=20.0)
    ap.add_argument("--line-ms", type=float, default=LINE_MS)
    ap.add_argument("--out", default="ycsb-out")
    ap.add_argument("--objective", default=DEFAULT_OBJECTIVE, choices=OBJECTIVES,
                    help="what the brain's verdict judges a step by: resource (the index's reading: work, speed, memory and CPU together) or service (work and speed alone)")
    ap.add_argument("--report-only", default="")
    a = ap.parse_args(argv)
    NATIVE, NATIVE_MB = a.native, (None if a.native == "shipped" else 512)
    if a.setup:
        return setup()
    out = Path(a.out)
    if a.report_only:
        recs = [json.loads(f.read_text()) for f in sorted(Path(a.report_only).rglob("ycsb-*/*.json"))]
        print(report(recs, Path(a.report_only))); return 0
    names = list(WORKLOADS) if a.workloads == "all" else a.workloads.split(",")
    recs = [run_workload(n, out, a.reps, a.step_s, a.line_ms, a.objective) for n in names]
    print(report(recs, out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
