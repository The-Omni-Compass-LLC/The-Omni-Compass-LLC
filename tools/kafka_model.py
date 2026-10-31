#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Kafka consumer group in our own model, closed loop (evidence class S): the store gate's model for a wire that changes
what the knob does, where the open-loop replay (tools/store_gate.py) can only say what each wire decides on seconds the
standing wire's knob produced.

Everything in the model is set from the omni-v21 runs' own files (runs 40256717947, 40279909158, 40400868003 on the branch
`raw`), never guessed:

  partitions   8, each message keyed str(seq % 8) by the harness's producer (tools/run_kafka.py producer_proc) and placed by
               Kafka's own partitioner, murmur2(key) & 0x7fffffff mod 8 (checked against Kafka's own test vectors): the eight
               keys land on six partitions, 6 and 7 two keys each, 2 and 5 none (KEY_SHARE)
  assignment   Kafka's range assignor (kafka-python's default): member i of c takes the next 8 // c partitions, one more for
               the first 8 % c members; with the keys above, 2 members carry 3/8 and 5/8 of the load, 3 members 2/8, 2/8, 4/8,
               4 members 4/8 at most, 5 to 8 members 2/8 at most
  service      each member serves 1 / service_ms messages a second, oldest first across its partitions: the two native
               consumers' backlogged throughput, 1.6 x 1 / service_ms with the 5/8 member saturated, is what the runs read
               (2 ms of work: 817 to 826 a second; 5 ms: 310 to 331; 1 ms: 1,372 to 1,521)
  a change     the group stops consuming while it rebalances: an added consumer cost the messages a median 1.24 s more
               (quartiles 0.33 and 2.49 s, at most 3.35 s; 41 changes made in calm), a removed one 2.58 s (1.60 to 2.86 s, at
               most 3.01 s; 52 changes): the client learns of a rebalance at its next heartbeat, every 3 s as shipped
  host CPU     the runs' own fit of the host's busy share on the messages consumed a second (cpu_share), per workload
  producer     evenly spaced at base x notch for each notch's seconds (the run's own base and notch length), after 8 s for the
               group to form, then up to 30 s of drain, as the harness runs an arm

The brains: native holds the operator's count; the standing wire is the omni-v21 loop (tools/run_kafka.py Omni.run, its
decide, its tools/knob_verdict.KnobVerdict and the compass law, read from git at the base commit), replayed second by second;
the candidate is the checkout's own Brain (tools/run_kafka.py), the very code the real run drives. Gauges and words as the
real table reads them (tools/readings.py by the one key), every seed paired across arms.

  python3 tools/kafka_model.py [--base COMMIT] [--seeds 8] [--out results/model_gate/KAFKA_MODEL.md]
  python3 tools/kafka_model.py --check-replica RAW_RUN_DIR   # the replica against an archived arm's own audit
"""
from __future__ import annotations

import argparse
import bisect
import importlib.util
import json
import math
import random
import statistics
import subprocess
import sys
import tempfile
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

PARTITIONS = 8
LINE_S = 0.5
SETTLE_S = 8.0           # the harness lets the group form before the producer starts (run_arm)
DRAIN_S = 30.0           # and gives the group up to 30 s to catch up after it stops
DT_PLANT = 0.05          # the plant's step (s); the brain decides once a second
STALL_ADD = (0.0, 0.334, 1.237, 2.487, 3.346)       # min, quartiles, max of the measured stalls (s), omni-v21 runs
STALL_REMOVE = (0.5, 1.598, 2.578, 2.858, 3.010)
CPU_FIT = {"burst": (0.021, 0.000682), "tuning": (0.021, 0.000682), "light": (0.02, 0.000617), "heavy": (0.015, 0.001588)}
# (service ms, steps, notch s, base rate a second, one member's rate a second) as the omni-v21 runs offered and served them: the
# base from their workload records (runs A and B: 30 s a notch; run C: 20 s); the member's rate is a backlogged consumer's own
# messages a second in its own record (the median over the 18 native consumers of each workload: 494 to 498 at 2 ms of work,
# 199 at 5 ms, 978 to 991 at 1 ms), so two members carry that rate plus the 3/8 member's arrivals (825 a second at the burst's
# peak, as the runs read)
STEPS = "1 2 3 2 3 4 5 6 5 4 3 2 1 2 1"
WORKLOADS = {"burst": (2.0, "1 6 1 8 1 6", 30.0, 110.0, 495.0), "tuning": (2.0, STEPS, 30.0, 146.5, 495.0),
             "light": (1.0, STEPS, 30.0, 290.5, 981.0), "heavy": (5.0, STEPS, 30.0, 58.7, 199.0)}


def murmur2(data: bytes) -> int:
    """Kafka's murmur2 (the clients' Utils.murmur2), unsigned 32 bits."""
    length = len(data); m = 0x5bd1e995
    h = (0x9747b28c ^ length) & 0xffffffff
    for i in range(length // 4):
        j = 4 * i
        k = data[j] | (data[j + 1] << 8) | (data[j + 2] << 16) | (data[j + 3] << 24)
        k = (k * m) & 0xffffffff; k ^= k >> 24; k = (k * m) & 0xffffffff
        h = (h * m) & 0xffffffff; h ^= k
    extra, idx = length % 4, length & ~3
    if extra >= 3:
        h ^= data[idx + 2] << 16
    if extra >= 2:
        h ^= data[idx + 1] << 8
    if extra >= 1:
        h ^= data[idx]; h = (h * m) & 0xffffffff
    h ^= h >> 13; h = (h * m) & 0xffffffff; h ^= h >> 15
    return h


def key_share(partitions=PARTITIONS):
    """Each partition's share of the messages the harness's producer offers (keys str(seq % partitions))."""
    share = [0.0] * partitions
    for k in range(partitions):
        share[(murmur2(str(k).encode()) & 0x7fffffff) % partitions] += 1.0 / partitions
    return share


KEY_SHARE = key_share()


def range_assign(c, partitions=PARTITIONS):
    """Kafka's range assignor for one topic: member i takes the next partitions // c, one more for the first partitions % c."""
    c = max(1, min(c, partitions))
    n, extra = divmod(partitions, c)
    out, start = [], 0
    for i in range(c):
        size = n + (1 if i < extra else 0)
        out.append(list(range(start, start + size))); start += size
    return out


def heaviest_share(c, share=KEY_SHARE):
    return max(sum(share[p] for p in parts) for parts in range_assign(c, len(share)))


def draw(q, rng):
    """One draw from a distribution given by its min, quartiles and max (piecewise uniform between them)."""
    i = rng.randrange(4)
    return q[i] + (q[i + 1] - q[i]) * rng.random()


class Plant:
    """The consumer group as partition queues of fluid chunks [arrival time, messages]."""

    def __init__(self, mu, count, rng, cpu_fit):
        self.mu = mu
        self.count = count; self.assign = range_assign(count)
        self.q = [deque() for _ in range(PARTITIONS)]
        self.rng = rng; self.cpu_fit = cpu_fit
        self.stall_until = -1.0; self.changes = 0
        self.produced = 0.0; self.consumed = 0.0
        self.sec = []            # completions this second: (latency s, messages)
        self.arr = [0.0] * PARTITIONS   # each partition's arrivals this second (what the broker's log-end offsets read)
        self.last_served = [0.0] * count

    def set_count(self, c, now):
        c = max(1, min(PARTITIONS, int(c)))
        if c == self.count:
            return
        stall = draw(STALL_ADD if c > self.count else STALL_REMOVE, self.rng)
        self.stall_until = max(self.stall_until, now) + stall
        self.count = c; self.assign = range_assign(c); self.changes += 1
        self.last_served = [now] * c          # a member starts busy (the harness's store fix of 25 October)

    def step(self, now, dt, rate):
        if rate > 0:
            n = rate * dt
            for p in range(PARTITIONS):
                if KEY_SHARE[p] > 0:
                    self.q[p].append([now, n * KEY_SHARE[p]])
                    self.arr[p] += n * KEY_SHARE[p]
            self.produced += n
        if now < self.stall_until:
            return
        for i, parts in enumerate(self.assign):
            budget = self.mu * dt * (0.97 + 0.06 * self.rng.random())
            while budget > 1e-9:
                heads = [p for p in parts if self.q[p]]
                if not heads:
                    break
                p = min(heads, key=lambda x: self.q[x][0][0])
                chunk = self.q[p][0]
                take = min(budget, chunk[1])
                self.sec.append((now + dt - chunk[0] + 1.0 / self.mu, take))
                chunk[1] -= take; budget -= take; self.consumed += take
                self.last_served[i] = now
                if chunk[1] <= 1e-9:
                    self.q[p].popleft()

    def lag(self):
        return max(0, int(round(self.produced - self.consumed)))

    def second(self, now):
        """The brain's sample for the second just ended, as the wire reads it."""
        n = sum(m for _, m in self.sec)
        inside = sum(m for l, m in self.sec if l <= LINE_S)
        mean = sum(l * m for l, m in self.sec) / n if n > 0 else None
        a, b = self.cpu_fit
        cpu = min(1.0, max(0.02, a + b * n))
        idle = sum(1 for t in self.last_served if now - t >= 1.0)
        done, self.sec = self.sec, []
        arrivals, self.arr = self.arr, [0.0] * PARTITIONS
        return {"reading": mean, "n_msg": int(round(n)), "inside": int(round(inside)), "lag": self.lag(), "idle": idle,
                "cpu_share": cpu, "consumers": self.count, "completions": done, "arrivals": arrivals}


def load_module(path_or_source, name):
    spec = importlib.util.spec_from_file_location(name, path_or_source)
    mod = importlib.util.module_from_spec(spec); sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def standing_wire(base):
    """The omni-v21 wire and its verdict, read from git at base, in a scratch directory (never this checkout's files)."""
    tmp = Path(tempfile.mkdtemp())
    (tmp / "tools").mkdir()
    for rel in ("tools/run_kafka.py", "tools/knob_verdict.py"):
        src = subprocess.run(["git", "-C", str(ROOT), "show", f"{base}:{rel}"], check=True, capture_output=True, text=True).stdout
        (tmp / rel).write_text(src)
    kv = load_module(str(tmp / "tools" / "knob_verdict.py"), "kafka_model_standing_knob_verdict")
    saved = sys.modules.get("tools.knob_verdict")
    sys.modules["tools.knob_verdict"] = kv
    try:
        wire = load_module(str(tmp / "tools" / "run_kafka.py"), "kafka_model_standing_run_kafka")
    finally:
        if saved is not None:
            sys.modules["tools.knob_verdict"] = saved
    return wire


class StandingBrain:
    """The omni-v21 loop body (tools/run_kafka.py Omni.run at the base commit), one decision a second."""

    def __init__(self, wire, snapshot, objective):
        self.w = wire; self.snapshot = snapshot
        self.law = wire.CompassLaw(wire.Band(0.0, wire.LINE_MS / 1000.0, center=wire.CENTER), dt=wire.DT, tau=wire.TAU, smooth=wire.SMOOTH)
        self.verdict = wire.KnobVerdict(snapshot, 1, wire.COVER, objective=objective, settle_s=2 * wire.TAU)
        self.objective = objective; self.last_change = -1e9

    def step(self, t, obs):
        w = self.w
        reading = obs["reading"]
        if reading is None:
            reading = min(w.LINE_MS / 1000.0, 0.0 if obs["lag"] == 0 else w.LINE_MS / 1000.0)
        f = self.law.force(reading)
        cur, idle, lag, n_msg = obs["consumers"], obs["idle"], obs["lag"], obs["n_msg"]
        cost = w.sample_cost(self.objective, obs["inside"], reading if n_msg else None, cur, obs["cpu_share"])
        self.verdict.observe(cost, t)
        target, _, why = w.decide(self.law.p, f, lag, idle, cur, t - self.last_change, wall=self.law.band.wall_high,
                                  snapshot=self.snapshot, consumed=n_msg)
        fail_up = why.startswith("fail up")
        target, why, _ = self.verdict.decide(target, spend_ok=(f > 0.05 and lag > 0),
                                             give_ok=(f < -0.05 and idle > 0 and lag == 0 and cur <= self.snapshot and n_msg > 0),
                                             t=t, why=why, stress=f > 0.05, calm=f < -0.05, fail_up=fail_up)
        if target != cur:
            self.last_change = t
        return target, why


class NativeBrain:
    def step(self, t, obs):
        return obs["consumers"], "native: the operator's count"


def percentile(pairs, q):
    """The q quantile of latencies weighted by messages."""
    pairs = sorted(pairs)
    total = sum(m for _, m in pairs)
    if total <= 0:
        return float("nan")
    acc, want = 0.0, q * total
    for l, m in pairs:
        acc += m
        if acc >= want:
            return l
    return pairs[-1][0]


def run_arm(workload, brain_factory, seed, snapshot=2, base_rate=None, notch_s=None):
    service_ms, steps, notch_default, base_default, mu = WORKLOADS[workload]
    notch_s = notch_s or notch_default
    base = base_rate or base_default
    rng = random.Random(seed)
    plant = Plant(mu, snapshot, rng, CPU_FIT[workload])
    brain = brain_factory(snapshot)
    rates = [base * int(s) for s in steps.split()]
    t_prod = SETTLE_S; t_end_prod = t_prod + notch_s * len(rates)
    t, next_decision = 0.0, 0.0
    seconds, lat, lags, counts = [], [], [], []
    produced_target = 0.0
    while True:
        if t >= t_end_prod and (plant.lag() == 0 or t >= t_end_prod + DRAIN_S):
            break
        k = int((t - t_prod) // notch_s) if t >= t_prod else -1
        rate = rates[k] if 0 <= k < len(rates) else 0.0
        plant.step(t, DT_PLANT, rate)
        t += DT_PLANT
        if t + 1e-9 >= next_decision + 1.0:
            next_decision += 1.0
            obs = plant.second(t)
            lat.extend(obs["completions"])
            lags.append(obs["lag"]); counts.append(plant.count)
            if t >= t_prod:
                out = brain.step(t - t_prod, obs)
                target, why = out[0], out[1]
                plant.set_count(target, t)
                seconds.append({"t": round(t - t_prod, 1), "reading_ms": None if obs["reading"] is None else round(obs["reading"] * 1000, 1),
                                "lag": obs["lag"], "consumers": obs["consumers"], "target": target, "why": why})
    wall_s = t - t_prod
    n = sum(m for _, m in lat)
    inside = sum(m for l, m in lat if l <= LINE_S)
    a, b = CPU_FIT[workload]
    return {"p95_ms": 1000 * percentile(lat, 0.95), "p99_ms": 1000 * percentile(lat, 0.99), "p50_ms": 1000 * percentile(lat, 0.5),
            "mean_ms": 1000 * sum(l * m for l, m in lat) / n if n else float("nan"),
            "work_inside_line_mps": inside / max(wall_s, 1e-9), "lag_max": max(lags) if lags else 0,
            "lag_mean": statistics.mean(lags) if lags else 0, "consumers_mean": statistics.mean(counts) if counts else snapshot,
            "consumers_max": max(counts) if counts else snapshot, "changes": plant.changes,
            "over_line_s": sum(1 for s in seconds if s["reading_ms"] is not None and s["reading_ms"] > 1000 * LINE_S),
            "seconds": seconds}


GAUGES = [("work_inside_line_mps", "work inside the response line (messages a second handled within the line)", "higher"),
          ("p95_ms", "end-to-end latency, 95th percentile (ms)", "lower"),
          ("p99_ms", "end-to-end latency, 99th percentile (ms)", "lower"),
          ("p50_ms", "end-to-end latency, median (ms)", "lower"),
          ("mean_ms", "end-to-end latency, mean (ms)", "lower"),
          ("lag_max", "consumer lag, most messages waiting at once", "lower"),
          ("lag_mean", "consumer lag, mean messages waiting", "lower"),
          ("consumers_mean", "consumers running, mean (the resources held)", "spent"),
          ("changes", "consumer changes written (each a rebalance of the whole group)", "spent")]


def paired_reading(xs, ys, aim):
    """Seeds paired: the mean change of y against x in percent of x, and its word by the one key (a change under 0.5% STEADY)."""
    from tools.readings import word as gel_word, SIZE_FLOOR
    rel = [(y - x) / abs(x) for x, y in zip(xs, ys) if x and x == x and y == y]
    if not rel:
        same = all(abs(y - x) < 1e-9 for x, y in zip(xs, ys))
        return 0.0, "STEADY, the same" if same else "no value"
    mean = sum(rel) / len(rel)
    if abs(mean) < SIZE_FLOOR:
        return mean, f"STEADY, under the floor ({100 * abs(mean):.2f}%)"
    sd = statistics.stdev(rel) if len(rel) > 1 else 0.0
    half = 2.0 * sd / math.sqrt(len(rel)) if len(rel) > 1 else 0.0
    clear = (mean - half > 0) or (mean + half < 0)
    return mean, f"{gel_word(mean < 0, aim)}{'' if clear else ' (inside the seeds spread)'}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--base", default="29370eec0b", help="the commit whose tools/run_kafka.py is the standing wire")
    ap.add_argument("--seeds", type=int, default=8)
    ap.add_argument("--first-seed", type=int, default=101)
    ap.add_argument("--objective", default="resource")
    ap.add_argument("--workloads", default="burst,light,heavy,tuning")
    ap.add_argument("--notch-s", type=float, default=None, help="every workload's notch length (s): 30 as runs A and B, 20 as run C")
    ap.add_argument("--out", default=str(ROOT / "results" / "model_gate" / "KAFKA_MODEL.md"))
    ap.add_argument("--no-candidate", action="store_true", help="native against the standing wire only (the model's own check)")
    a = ap.parse_args(argv)
    standing = standing_wire(a.base)
    arms = {"native": lambda snap: NativeBrain(),
            "standing": lambda snap: StandingBrain(standing, snap, a.objective)}
    if not a.no_candidate:
        import tools.run_kafka as cand
        if hasattr(cand, "Brain"):
            arms["candidate"] = lambda snap: cand.Brain(snap, a.objective)
    seeds = list(range(a.first_seed, a.first_seed + a.seeds))
    record = {"base": a.base, "objective": a.objective, "seeds": seeds, "workloads": {}}
    lines = ["# The Kafka consumer group in our own model, closed loop", "",
             f"Evidence class S (our own model, never a benchmark result). The standing wire is `tools/run_kafka.py` at `{a.base}`; "
             f"the objective {a.objective}; seeds {seeds[0]} to {seeds[-1]}, every arm on the same seeds; notches of {a.notch_s or 30:g} s. Built by `tools/kafka_model.py` "
             "from the omni-v21 runs' own files (see its header).", ""]
    for wl in a.workloads.split(","):
        res = {arm: [run_arm(wl, f, s, notch_s=a.notch_s) for s in seeds] for arm, f in arms.items()}
        record["workloads"][wl] = {arm: [{k: v for k, v in r.items() if k != "seconds"} for r in rs] for arm, rs in res.items()}
        lines += [f"## {wl}", "", "| Gauge | " + " | ".join(arms) + " | " +
                  " | ".join(f"{x} against {y}" for x, y in pairs_of(arms)) + " |",
                  "|---|" + "---:|" * len(arms) + "---|" * len(pairs_of(arms))]
        for key, name, aim in GAUGES:
            means = [statistics.mean(r[key] for r in res[arm]) for arm in arms]
            cells = []
            for x, y in pairs_of(arms):
                m, w = paired_reading([r[key] for r in res[x]], [r[key] for r in res[y]], aim)
                cells.append(f"{w}, {100 * m:+.1f}%")
            lines.append(f"| {name} | " + " | ".join(f"{v:,.1f}" for v in means) + " | " + " | ".join(cells) + " |")
        lines.append(f"| seconds over the line, mean | " + " | ".join(f"{statistics.mean(r['over_line_s'] for r in res[arm]):.1f}" for arm in arms) + " | |" * 0)
        lines.append("")
    out = Path(a.out); out.parent.mkdir(parents=True, exist_ok=True)
    from tools.legal import stamp
    out.write_text("\n".join(stamp(lines)) + "\n")
    out.with_suffix(".json").write_text(json.dumps(record, indent=1) + "\n")
    print(f"{out}: {', '.join(a.workloads.split(','))}; arms {', '.join(arms)}")


def pairs_of(arms):
    names = list(arms)
    out = [(names[0], n) for n in names[1:]]
    if "candidate" in names and "standing" in names:
        out.append(("standing", "candidate"))
    return out


if __name__ == "__main__":
    main()
