#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Redis cache in our own model, closed loop (evidence class S): the store gate's model for the cache's ceiling.

The harness's application (tools/run_redis.py App) asks 1,500 requests a second for keys drawn Zipf(0.5) from the working set of
the moment; each notch of a workload is a keyspace of its own (the prefix k<n>:, n = base keys x notch), so a notch starts cold
and the last notch's keys stay in memory until evicted. A hit is Redis's answer; a miss is the store trip (5 ms) and a write
back. The model runs that exactly: the same sampler, an LRU cache measured in bytes, and the latency of a hit and of a miss
drawn from the omni-v21 native arms' own records. The brains: native holds the operator's 64 MB; a fixed ceiling (any MB) shows
what a cache of that size could do at all; the standing wire is omni-v21's loop (tools/run_redis.py decide, its
tools/knob_verdict.KnobVerdict and the compass law) read from git; the candidate is the checkout's own Brain, if it has one.

  python3 tools/redis_model.py --fixed 64,128,256,512 [--workloads tuning,small,large,burst] [--seeds 3]
"""
from __future__ import annotations

import argparse
import bisect
import json
import random
import statistics
import sys
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

MB = 1024 * 1024
RATE = 1500.0
MODEL_HOST_AVAIL_MB, MODEL_HOST_TOTAL_MB = 4096.0, 7168.0   # the model's host (class S): a GitHub runner's 7 GB with 4 GB available, room for every notch
LINE_MS = 2.0
MISS_PENALTY_MS = 5.0
ZIPF_S = 0.5
KEY_OVERHEAD = 96           # Redis's own bytes a key beside its value (dict entry, robj, SDS headers), the order of the shipped allocator's
BASELINE_MB = 1.0           # the server's memory with no keys
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
BURST = "1 6 1 8 1 6"
WORKLOADS = {"tuning": (8192, 2_500, STEPS), "small": (2048, 10_000, STEPS), "large": (32768, 625, STEPS), "burst": (8192, 2_500, BURST)}
HIT_MS = (0.099, 0.114, 0.122, 0.136, 0.286)      # a hit's latency (ms): the 1st, 25th, 50th, 75th and 99th percentiles of
                                                  # 654,827 hits in the omni-v21 native arms (runs 40254205224, 40276907808)
MISS_EXTRA_MS = (0.254, 0.368, 0.48, 0.569, 0.77)  # a miss beyond the 5 ms store trip, the same percentiles of 155,179 misses


def zipf_cum(n, s=ZIPF_S):
    w = [1.0 / (k + 1) ** s for k in range(n)]
    tot = sum(w); acc = 0.0; cum = []
    for x in w:
        acc += x / tot; cum.append(acc)
    return cum


def draw_q(q, rng):
    i = rng.randrange(4)
    return q[i] + (q[i + 1] - q[i]) * rng.random()


class Cache:
    """An LRU cache in bytes (Redis's allkeys-lru approximates it with sampled candidates)."""

    def __init__(self, ceiling_mb, value_bytes):
        self.keys = OrderedDict(); self.size = value_bytes + KEY_OVERHEAD
        self.ceiling = ceiling_mb * MB; self.evicted = 0

    def used(self):
        return BASELINE_MB * MB + len(self.keys) * self.size

    def set_ceiling(self, mb):
        self.ceiling = mb * MB
        self._evict()

    def _evict(self):
        while self.keys and self.used() > self.ceiling:
            self.keys.popitem(last=False); self.evicted += 1

    def get(self, k):
        if k in self.keys:
            self.keys.move_to_end(k)
            return True
        return False

    def put(self, k):
        self.keys[k] = True; self.keys.move_to_end(k)
        self._evict()


def run_arm(workload, ceiling_of, seed, step_s=30.0, start_mb=64.0):
    """ceiling_of(t, second's observation) -> the ceiling (MB) for the next second; None keeps it."""
    value, base, steps = WORKLOADS[workload]
    rng = random.Random(seed); lat_rng = random.Random(seed + 7)
    cache = Cache(start_mb, value)
    lats = []; per_second = []; ceilings = []; used = []
    t = 0.0
    for notch in [int(x) for x in steps.split()]:
        n = base * notch; cum = zipf_cum(n); prefix = n
        for _ in range(int(step_s)):
            sec = []; ev0 = cache.evicted; hits = []; misses = []
            for _ in range(int(RATE)):
                k = (prefix, bisect.bisect_left(cum, rng.random()))
                if cache.get(k):
                    l = draw_q(HIT_MS, lat_rng); hits.append(l)
                else:
                    l = MISS_PENALTY_MS + draw_q(MISS_EXTRA_MS, lat_rng); cache.put(k); misses.append(l)
                sec.append(l)
            t += 1.0
            lats.extend(sec)
            obs = {"reading_s": sum(sec) / len(sec) / 1000.0, "n": len(sec), "inside": sum(1 for x in sec if x <= LINE_MS),
                   "evicted_last_s": cache.evicted - ev0, "ceiling_mb": cache.ceiling / MB, "used_mb": cache.used() / MB,
                   "hit_ms": sum(hits) / len(hits) if hits else None, "miss_ms": sum(misses) / len(misses) if misses else None,
                   "miss_share": len(misses) / len(sec), "host_avail_mb": MODEL_HOST_AVAIL_MB, "host_total_mb": MODEL_HOST_TOTAL_MB}
            per_second.append(obs); ceilings.append(cache.ceiling / MB); used.append(cache.used() / MB)
            new = ceiling_of(t, obs)
            if new is not None and abs(new - cache.ceiling / MB) > 1e-9:
                cache.set_ceiling(new)
    lats.sort()
    q = lambda p: lats[min(len(lats) - 1, int(p * len(lats)))]
    return {"work_inside_line_rps": sum(o["inside"] for o in per_second) / len(per_second), "p95_ms": q(0.95), "p99_ms": q(0.99),
            "mean_ms": sum(lats) / len(lats), "ceiling_mean_mb": statistics.mean(ceilings), "used_mean_mb": statistics.mean(used),
            "hit_share": sum(1 for x in lats if x < MISS_PENALTY_MS) / len(lats)}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fixed", default="64,128,256,512")
    ap.add_argument("--workloads", default="tuning,small,large,burst")
    ap.add_argument("--seeds", type=int, default=2)
    ap.add_argument("--step-s", type=float, default=30.0)
    ap.add_argument("--compare", action="store_true", help="native, omni-v21's loop (from git at --base) and the candidate, seed for seed")
    ap.add_argument("--base", default="29370eec0b")
    a = ap.parse_args(argv)
    if a.compare:
        import tools.run_redis as cand
        def maker():
            b = cand.Brain(64, "resource")
            def step(t, obs):
                o = dict(obs); o["cpu_share"] = CPU_SHARE
                target, why, info = b.step(t, o)
                return target
            return step
        maker = maker if hasattr(cand, "Brain") else None
        print_compare(compare(a.workloads.split(","), list(range(101, 101 + a.seeds)), a.base, a.step_s, maker))
        return
    for wl in a.workloads.split(","):
        print(f"== {wl}")
        for mb in [float(x) for x in a.fixed.split(",")]:
            rs = [run_arm(wl, lambda t, o: None, s, a.step_s, start_mb=mb) for s in range(101, 101 + a.seeds)]
            m = {k: statistics.mean(r[k] for r in rs) for k in rs[0]}
            print(f"   fixed {mb:>5.0f} MB: work inside the line {m['work_inside_line_rps']:7.1f} a second, hits {100 * m['hit_share']:5.1f}%, "
                  f"mean {m['mean_ms']:5.2f} ms, p95 {m['p95_ms']:5.2f}, p99 {m['p99_ms']:5.2f}, used {m['used_mean_mb']:6.1f} MB")


# ------------------------------------------------------------------------------------------- the brains on the model
def load_module(path, name):
    import importlib.util
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def standing_wire(base):
    """omni-v21's Redis wire and its verdict, read from git at base into a scratch directory (never this checkout's files)."""
    import subprocess, tempfile
    tmp = Path(tempfile.mkdtemp()); (tmp / "tools").mkdir()
    for rel in ("tools/run_redis.py", "tools/knob_verdict.py"):
        src = subprocess.run(["git", "-C", str(ROOT), "show", f"{base}:{rel}"], check=True, capture_output=True, text=True).stdout
        (tmp / rel).write_text(src)
    kv = load_module(str(tmp / "tools" / "knob_verdict.py"), "redis_model_standing_knob_verdict")
    saved = sys.modules.get("tools.knob_verdict"); sys.modules["tools.knob_verdict"] = kv
    try:
        wire = load_module(str(tmp / "tools" / "run_redis.py"), "redis_model_standing_run_redis")
    finally:
        if saved is not None:
            sys.modules["tools.knob_verdict"] = saved
    return wire


CPU_SHARE = 0.3          # the host's busy share in the omni-v21 runs (0.26 to 0.32): a constant in the model, the same in every arm


class StandingBrain:
    """omni-v21's loop body (tools/run_redis.py Omni.run at the base commit), one decision a second, on the model's seconds."""

    def __init__(self, wire, native_mb, objective="resource"):
        self.w = wire
        self.law = wire.CompassLaw(wire.Band(0.0, wire.LINE_MS / 1000.0, center=wire.CENTER), dt=wire.DT, tau=wire.TAU, smooth=wire.SMOOTH)
        self.verdict = wire.KnobVerdict(native_mb, wire.STEP_MB, wire.COVER_MB, objective=objective, settle_s=wire.TAU)
        self.objective = objective; self.last_change = -1e9

    def __call__(self, t, obs):
        w = self.w
        f = self.law.force(obs["reading_s"])
        cur = obs["ceiling_mb"]; full = obs["used_mb"] >= w.FULL * cur
        cost = w.sample_cost(self.objective, obs["inside"], obs["reading_s"], cur, CPU_SHARE)
        self.verdict.observe(cost, t)
        target, why = w.decide(self.law.p, f, obs["evicted_last_s"], cur, t - self.last_change, full, wall=self.law.band.wall_high)
        target, why, _ = self.verdict.decide(target, spend_ok=(f > 0.05 and full), give_ok=(f < -0.05 and obs["evicted_last_s"] == 0),
                                             t=t, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=why.startswith("fail up"))
        if target != cur and target > cur:
            self.last_change = t
        return target if target != cur else None


def compare(workloads, seeds, base, step_s, candidate=None):
    """Native (the operator's 64 MB), omni-v21's loop and, where the checkout has one, the candidate, seed for seed."""
    wire = standing_wire(base)
    arms = {"native": lambda: (lambda t, o: None), "standing": lambda: StandingBrain(wire, 64)}
    if candidate is not None:
        arms["candidate"] = candidate
    out = {}
    for wl in workloads:
        out[wl] = {arm: [run_arm(wl, make(), s, step_s) for s in seeds] for arm, make in arms.items()}
    return out


def print_compare(res):
    keys = [("work_inside_line_rps", "work inside the line (requests a second)"), ("mean_ms", "latency, mean (ms)"), ("p95_ms", "latency, 95th percentile (ms)"),
            ("p99_ms", "latency, 99th percentile (ms)"), ("hit_share", "hit share"), ("ceiling_mean_mb", "ceiling held, mean (MB)"), ("used_mean_mb", "memory used, mean (MB)")]
    for wl, arms in res.items():
        print(f"== {wl}")
        names = list(arms)
        print("   gauge".ljust(44) + "".join(n.rjust(12) for n in names) + "   standing vs native, candidate vs standing (%)")
        for k, label in keys:
            means = {n: statistics.mean(r[k] for r in arms[n]) for n in names}
            rel = []
            if "standing" in means and means["native"]:
                rel.append(f"{100 * (means['standing'] - means['native']) / means['native']:+.1f}")
            if "candidate" in means and means.get("standing"):
                rel.append(f"{100 * (means['candidate'] - means['standing']) / means['standing']:+.1f}")
            print(f"   {label.ljust(41)}" + "".join(f"{means[n]:12.2f}" for n in names) + "   " + "  ".join(rel))


if __name__ == "__main__":
    main()
