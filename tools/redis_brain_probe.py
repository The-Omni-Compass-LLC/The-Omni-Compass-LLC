#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""docs/TAIL_LATENCY.md, section 4. Does the brain's presence inside the load generator's process lengthen the timed requests, with nothing else changed?

tools/run_redis.py runs the brain (Omni) as a thread inside the application's own Python process. Here the application is
the harness's own App, at the GitHub rate (1,500 requests a second, 32 request threads), and the brain is the harness's own
Omni loop, unchanged. Only the two outside parts are stand-ins, the same in both arms:
  - the store answers every request in a fixed 100 microseconds, sleeping as a socket wait does (Python's lock released), a
    hit with probability HIT and otherwise a miss with the declared 5 ms store trip, as the App writes it;
  - the plug writes nowhere: the brain reads the ceiling, decides, runs its trials and writes to a variable.
So the only difference between the arms is the brain thread computing once a second in the same process.

Usage: python3 tools/redis_brain_probe.py OUT_DIR [pairs=12] [seconds an arm=20]   (needs the redis package the harness imports)
Arms: alone (the App alone) and brain (the App with the brain), paired, the order alternating.
"""
import json, random, statistics as st, sys, threading, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from tools import run_redis as rr  # noqa: E402

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else "redis-brain-probe"); OUT.mkdir(parents=True, exist_ok=True)
REPS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
SECONDS = int(sys.argv[3]) if len(sys.argv) > 3 else 20
HIT = 0.6
MB = rr.MB


class Store:
    def __init__(self, seed):
        self.rng = random.Random(seed); self.lock = threading.Lock()

    def get(self, key):
        time.sleep(0.0001)
        with self.lock:
            hit = self.rng.random() < HIT
        return b"v" if hit else None

    def set(self, key, value):
        time.sleep(0.0001)


class Plug:
    """the plug's interface, writing nowhere; the cache always reads full, so the brain is never idle"""
    def __init__(self):
        self.cur = 64 * MB

    def attach(self):
        return self.cur

    def lever(self):
        return self.cur

    def write(self, mb):
        self.cur = int(mb) * MB
        return int(mb)

    def restore(self):
        self.cur = 64 * MB
        return True

    def evicted(self):
        return 0

    def used_mb(self):
        return self.cur / MB


brain_cpu = []
real_run = rr.Omni.run


def timed_run(self):
    c0 = time.thread_time(); real_run(self); brain_cpu.append(time.thread_time() - c0)


rr.Omni.run = timed_run


def arm(name, rep):
    steps = " ".join(["1"] * (SECONDS // 5))
    app = rr.App(Store(9000 + rep), 2048, 10_000, steps, 5.0, 9000 + rep, OUT / f"{name}-{rep}.log")
    omni = None
    if name == "brain":
        omni = rr.Omni(Plug(), app, OUT / f"audit-{rep}.jsonl", rr.LINE_MS, "resource"); omni.start()
    t0 = time.perf_counter(); app.start(); app.join(); wall = time.perf_counter() - t0
    if omni:
        omni.stop_flag.set(); omni.join()
    lat = sorted(l for _, l, _ in app.records)
    q = lambda p: lat[min(len(lat) - 1, int(p * len(lat)))]
    g = {"n": len(lat), "p99_ms": q(0.99), "p95_ms": q(0.95), "p50_ms": q(0.50), "mean_ms": st.mean(lat), "wall_s": wall,
         "hits": app.hits, "misses": app.misses}
    if omni:
        g["brain_cpu_s"] = brain_cpu.pop() if brain_cpu else None; g["brain_writes"] = omni.writes
    return g


rows = []
for rep in range(1, REPS + 1):
    order = ["alone", "brain"] if rep % 2 else ["brain", "alone"]
    res = {n: arm(n, rep) for n in order}
    rows.append({"rep": rep, "order": order, **res})
    (OUT / "gil.json").write_text(json.dumps(rows, indent=1))
    d = {k: (res["brain"][k] - res["alone"][k]) * 1000 for k in ("p99_ms", "p95_ms", "mean_ms")}
    print(rep, order, {k: round(v, 1) for k, v in d.items()}, "brain cpu", res["brain"].get("brain_cpu_s"), flush=True)

summary = {}
for k in ("p99_ms", "p95_ms", "p50_ms", "mean_ms"):
    d = [(r["brain"][k] - r["alone"][k]) * 1000 for r in rows]
    m = st.mean(d); s = st.stdev(d)
    summary[k + " (brain - alone, us)"] = {"mean": m, "sd": s, "se": s / len(d) ** 0.5, "n": len(d), "each": [round(x, 1) for x in d]}
summary["brain CPU, seconds a second"] = st.mean(r["brain"]["brain_cpu_s"] / r["brain"]["wall_s"] for r in rows if r["brain"].get("brain_cpu_s"))
(OUT / "summary.json").write_text(json.dumps(summary, indent=1))
print(json.dumps(summary, indent=1))
