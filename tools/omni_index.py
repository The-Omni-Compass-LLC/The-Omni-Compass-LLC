#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Omni index: one number for more for the same, or the same for less (docs/K8S_COMPASS_PREREGISTRATION.md).

Every measure of every test is turned into a ratio oriented so that above 1 is a GAIN against the system's declared aim
(more work, faster, fewer machines, less energy; the words are tools/readings.py's):

  work      work with Omni / work native        (capacity, or requests served)
  speed     p95 native / p95 with Omni          (a lower response time is faster)
  machines  machines native / machines with Omni (in service, or billed machine-hours)
  energy    energy native / energy with Omni    (or the bill)

A test's index is the geometric mean of its ratios, minus one, in percent. A category is the geometric mean of its
tests; the headline is the geometric mean of the real categories, each weighted the same. The modelled muscles are
shown beside the headline, never inside it. Every number is read from the test's own result file (SOURCES below names
the file, the table and the row); nothing is typed in. A test that did not take a measure leaves it out. Below 1 is a
LOSS for work and speed, and power given for machines and energy (a resource Omni put in, shown and counted, never called
a loss).

  python3 tools/omni_index.py  ->  results/OMNI_INDEX.md, results/OMNI_INDEX.json
"""
from __future__ import annotations

import json

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
import math
import re
import sys
from pathlib import Path

from tools.readings import judged, landed, with_own_runs, classify, GAIN, STEADY, LOSS, GIVEN, word_sign  # noqa: E402  (a reading in all three of our runs, or an older "confirmed")

ROOT = Path(__file__).resolve().parents[1]
LIVE = ROOT / "results" / "live"

# The three-run tables (tools/confirm_abc.py, docs/OMNI_V1.md, docs/OMNI_V3.md): each test's three runs on the frozen engine, every row with
# its reading by rule. (category, test, file, {measure: row key}, work). work: "equal" (the same fixed-rate work was sent
# to both arms and none failed: ratio 1), "capacity" (the capacity row of that table), or None (not taken). A measure
# counts only as its reading allows: GAIN, LOSS or power given in all three of our runs gives the geometric mean of
# the three runs' ratios; STEADY (no difference beyond the noise, or the same) or the runs disagree gives exactly 1 (nothing
# is claimed either way). Azure's billed runs and the six organisms join the index when their v1 tables land.
P95 = "response time (ms), 95th percentile"
MEAN = "response time (ms), mean"
NODES = "worker nodes in service, mean"
ENERGY = "energy, parked workers still on at idle power (Wh)"
STANDBY = "energy (Wh)"
CAPACITY = "work inside the response line (requests a second; the capacity test's own gauge, higher is better)"   # the row's name as the tables written before 13 October recorded it, kept to read them
CAPACITY_NOW = "work inside the response line (requests a second; the capacity test's own gauge)"                  # the same row since
SOURCES = [
    ("Real Kubernetes (GitHub)", "Steady same work: the load in steps at a fixed rate, ten pairs, three runs", "V7_STEADY.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, "equal"),
    ("Real Kubernetes (GitHub)", "Demand that wanders: up and down one step at a time, ten pairs, three runs", "V7_WANDERING.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "All four in one run: load up and down one step at a time, ten pairs, three runs", "V7_ALL_FOUR.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, "capacity"),
    ("Real Kubernetes (GitHub)", "Fairness: a noisy neighbour, ten pairs, three runs", "V7_FAIRNESS.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "Faults: machine down, spike, runaway pod, blind probe, ten pairs, three runs", "V7_FAULTS.json",
     {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "A queue of jobs: cruise, then the emergency brake, ten pairs, three runs", "V7_BATCH.json",
     {"speed": MEAN, "machines": NODES, "energy": STANDBY}, None),
    ("Real Kubernetes (GitHub)", "A public day of demand: the Google cluster trace of 2011 replayed one step at a time, ten pairs, three runs",
     "V7_TRACE_GOOGLE2011.json", {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "With its add-ons: KEDA on the CPU target and the live requests in flight, Omni-Compass on top, ten pairs, three runs",
     "V7_KEDA_CPU_REQUESTS.json", {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
    ("Real Kubernetes (GitHub)", "With its add-ons: KEDA's HTTP add-on on the live requests in flight, Omni-Compass on top, ten pairs, three runs",
     "V7_KEDA_REQUESTS.json", {"speed": P95, "machines": NODES, "energy": ENERGY}, None),
]
REAL = ("Real Kubernetes (GitHub)", "Real database (PostgreSQL behind PgBouncer, GitHub)", "Real messaging (Apache Kafka, GitHub)",
        "Real cache (Redis, GitHub)", "Real database cache (MongoDB under YCSB, GitHub)",
        "Real database buffer pool (MySQL under sysbench, GitHub)", "Real cloud (Azure AKS, billed)",
        "Real card (NVIDIA, its own meter)")
# the workload tables (tools/pgbench_abc.py, kafka_abc.py, redis_abc.py): per untouched workload, work = the work inside the
# line, speed = p95, machines = the resource held (connections to the database; consumers running; the cache's memory ceiling),
# energy = the host's CPU seconds over the run (no meter on a GitHub runner; the CPU the compass itself burns is the declared
# price, and a rise in all three of our runs there is power given and counts below 1). A table's tuning workload is shown in its own file and never counted.
WORKLOAD_TABLES = [
    ("Real database (PostgreSQL behind PgBouncer, GitHub)", "V7_PGBENCH.json", "pgbench `{wl}`: the pooler's pool size, three paired repetitions, three runs",
     {"work": "work_inside_line_tps", "speed": "p95_ms", "machines": "servers_alive_mean", "energy": "cpu_seconds"}),
    ("Real messaging (Apache Kafka, GitHub)", "V7_KAFKA.json", "Kafka `{wl}`: the consumer group's size, three paired repetitions, three runs",
     {"work": "work_inside_line_mps", "speed": "p95_ms", "machines": "consumers_mean", "energy": "cpu_seconds"}),
    ("Real cache (Redis, GitHub)", "V7_REDIS.json", "Redis `{wl}`: the cache's memory ceiling, three paired repetitions, three runs",
     {"work": "work_inside_line_rps", "speed": "p95_ms", "machines": "maxmemory_mb_mean", "energy": ("process_cpu_seconds", "cpu_seconds")}),
    ("Real database cache (MongoDB under YCSB, GitHub)", "V7_YCSB.json", "YCSB `{wl}`: the storage engine's cache size, three paired repetitions, three runs",
     {"work": "work_inside_line_ops", "speed": "p95_ms", "machines": "cache_mb_mean", "energy": ("process_cpu_seconds", "cpu_seconds")}),
    ("Real database buffer pool (MySQL under sysbench, GitHub)", "V7_SYSBENCH.json", "sysbench `{wl}`: the buffer pool's size, three paired repetitions, three runs",
     {"work": "work_inside_line_tps", "speed": "p95_ms", "machines": "pool_mb_mean", "energy": "cpu_seconds"}),
]
DB_FILE = WORKLOAD_TABLES[0][1]
AIM_LOWER = {"speed", "machines", "energy"}   # the measures whose declared aim is lower (work aims higher)
PENDING = {"Real cloud (Azure AKS, billed)": "the omni-v23 Azure sets run one at a time at the tune-down with native's cap (the steady set, the bursts 1 4 1 6 1 9 and 1 6 1 8 1 6, the real day of Google 2011; A, B and C, `scripts/azure_queue.txt`); the category joins as their three-run tables land",
           "Real card (NVIDIA, its own meter)": "the rerun on the current card controller (the 2026-10-02 run used the replaced one)"}


def ratio(measure, native, omni):
    if native is None or omni is None or native <= 0 or omni <= 0:
        return None
    return native / omni if measure in AIM_LOWER else omni / native


def gmean(xs):
    xs = [x for x in xs if x]
    return math.exp(sum(math.log(x) for x in xs) / len(xs)) if xs else None


def measure(row, m):
    """One measure's ratio over the three runs, as its reading allows: judged across our three runs (a change of 0.5% or more) gives the geometric mean
    of the runs' ratios (a LOSS, or power given, in all three of our runs counts below 1); anything else is exactly 1, nothing claimed."""
    reading = row["reading"]
    rs = [ratio(m, r["native"], r["omni"]) for r in row["runs"]]
    g = gmean(rs) if judged(reading) and all(rs) else 1.0
    return {"native": row["runs"][0]["native"], "omni": row["runs"][0]["omni"], "ratio": g, "reading": reading}


def whole(path):
    """A table that carries a result: a gauge row, or a workload beside the tuning one. A table written from runs that
    failed (its workloads or rows empty) is not whole, and the test is read from the newest whole table until its runs land.
    The rule is written once, in tools/readings.py (landed), and read by every tool that picks a benchmark's newest table."""
    return landed(path)


def newest(fname):
    """The same test's table on the newest engine that has a whole one (V<n>_<TEST>.json with the highest n whose table
    carries a result); tables of two engines are never pooled, and a later engine's three runs take the test's place the
    moment their table lands whole. A newer table written from failed runs (20 October: the omni-v12 MongoDB table, its B and
    C with no workload) is passed over, so no test leaves the index or the benefit sheet for a run that failed."""
    base = re.sub(r"^V\d+_", "", fname)
    found = sorted((int(m.group(1)), x.name) for x in LIVE.glob("V*_" + base) if (m := re.fullmatch(r"V(\d+)_" + re.escape(base), x.name)))
    for _, name in reversed(found):
        if whole(LIVE / name):
            return name
    return found[-1][1] if found else fname


def workload_gauge(gauges, key):
    """One measure's gauge from a workload table: key, or a tuple of keys read in order, the first whose three runs all hold a
    value (store fix of 25 October: a table written from runs that record the CPU apart reads the stack's own CPU-seconds,
    process_cpu_seconds; an older table reads the host's, cpu_seconds, as before)."""
    for k in (key if isinstance(key, tuple) else (key,)):
        g = gauges.get(k)
        if g and g.get("runs") and not any(x is None for x in g["runs"]):
            return g
    return None


def tests():
    out = []
    for cat, name, f, measures, work in SOURCES:
        f = newest(f)
        path = LIVE / f
        if not path.exists():
            continue
        data = json.loads(path.read_text())
        rows_ = data["rows"]
        r = {m: measure(rows_[key], m) for m, key in measures.items() if key in rows_}
        if work == "equal":
            r["work"] = {"native": 1.0, "omni": 1.0, "ratio": 1.0, "reading": "the same fixed-rate work sent to both arms"}
        elif work == "capacity" and (CAPACITY in rows_ or CAPACITY_NOW in rows_):
            r["work"] = measure(rows_.get(CAPACITY) or rows_[CAPACITY_NOW], "work")
        out.append({"category": cat, "test": name, "source": f"results/live/{f}", "runs": [x["run"] for x in data["runs"]],
                    "v1": bool(data.get("v1")), "measures": r})
    for cat, fname, label, measures_ in WORKLOAD_TABLES:
      fname = newest(fname)
      db = LIVE / fname
      if not db.exists():
        continue
      if True:
        data = json.loads(db.read_text())
        for wl, gauges in sorted(data["workloads"].items()):
            if wl == "tuning":
                continue                                        # the tuning workload is shown in its table, never counted
            r = {}
            for m, key in measures_.items():
                g = workload_gauge(gauges, key)
                if not g or any(x is None for x in g["runs"]):
                    continue
                reading = g["reading"]
                if judged(reading):
                    ratios = [(x["omni"] / x["native"]) if m == "work" else (x["native"] / x["omni"]) for x in g["runs"] if x["native"] and x["omni"]]
                    ratio = gmean(ratios) if ratios else 1.0
                else:
                    ratio = 1.0
                r[m] = {"native": g["runs"][0]["native"], "omni": g["runs"][0]["omni"], "ratio": ratio, "reading": reading}
            out.append({"category": cat, "test": label.format(wl=wl),
                        "source": f"results/live/{fname}", "runs": [x["run"] for x in data["runs"]], "v1": False, "measures": r})
    for t in out:
        g = gmean([m["ratio"] for m in t["measures"].values()])
        t["index_pct"] = 100 * (g - 1) if g else None
        s = gmean([m["ratio"] for k, m in t["measures"].items() if k in SERVICE])
        t["service_pct"] = 100 * (s - 1) if s else None
    return out


# The second reading, declared 2026-10-09 at the founder's question about the cache (docs/K8S_COMPASS_PREREGISTRATION.md, the
# Omni index, the service reading): the same tests, the same three-run rule, scored on what the stack is bought for, its
# service (work and speed), with the resources it spends or saves (machines, energy) shown beside it and not scored. It is
# computed for every test alike, never for one stack, and printed beside the resource reading, which stays the headline the
# program preregistered. Where a governor buys service with a resource (Redis's memory, Kafka's consumers) the two readings
# part; where it gives a resource back for the same service (the databases) the service reading says nothing moved.
SERVICE = {"work", "speed"}


def pct(x):
    if x is None:
        return ""
    v = 100 * (x - 1)
    return f"{v:+.2f}%" if 0 < abs(v) < 0.05 else f"{v:+.1f}%"


def pw(x, word):
    """A ratio's change beside its word: its size alone, no sign, as tools/readings.py by_word prints it (the referee's work order
    of 25 October: a raw change is never turned to wear the verdict's sign). A column with no word of its own keeps pct's true
    sign, read by the column's name."""
    if x is None:
        return ""
    v = 100 * (x - 1)
    size = f"{abs(v):.2f}%" if 0 < abs(v) < 0.05 else f"{abs(v):.1f}%"
    sg = word_sign(word)
    return size if sg else pct(x)


def with_word(x, word):
    """'4.3% GAIN', '0.1% power given', '0.0% STEADY'."""
    return "" if x is None else f"{pw(x, word)} {word}".strip()


def word_of(measure_, ratio_):
    """The word for a measure's ratio: above 1 is a GAIN; below 1 a LOSS for work and speed, and power given for machines
    and energy (a resource put in); exactly 1 is STEADY."""
    if ratio_ is None:
        return ""
    if ratio_ == 1.0:
        return STEADY
    if ratio_ > 1.0:
        return GAIN
    return GIVEN if measure_ in ("machines", "energy") else LOSS


def index_word(x, service=None):
    """The word for a combined number (a test's, a category's, the headline): a plus is a GAIN; a minus is a LOSS where the
    service reading (work and speed) is below 1 too, and otherwise power given (the resources put in outweigh what they
    bought on this reading); exactly 1 is STEADY."""
    if x is None:
        return ""
    if x == 1.0:
        return STEADY
    if x > 1.0:
        return GAIN
    return LOSS if service is not None and service < 1.0 else GIVEN


def engines_sentence(ts):
    """Which engine each test's table ran on, counted from the tables themselves: a test is read from its newest table, so
    while a version's runs land some tests stand on it and the rest on the engine before; no test's table is pooled."""
    by = {}
    for t in ts:
        m = re.match(r"results/live/V(\d+)_", t["source"])
        by.setdefault(int(m.group(1)) if m else 0, set()).add(t["test"].split(" `")[0])
    parts = [f"{len(v)} on omni-v{k}" for k, v in sorted(by.items(), reverse=True)]
    return ("Each test is read from its own newest three-run table: " + ", ".join(parts) + " (omni-v8, omni-v9 and omni-v10 changed only the "
            "CityLearn runner and the interval table, omni-v11 the Kubernetes governor's hold on a reading with no machine in service); "
            "a test stands on an older engine's table only until its three runs on the engine that stands land, no table is pooled across engines, and every row "
            "below names its table.")


def main():
    ts = tests()
    cats = {}
    for t in ts:
        cats.setdefault(t["category"], []).append(t)
    cat_g = {c: gmean([1 + t["index_pct"] / 100 for t in v if t["index_pct"] is not None]) for c, v in cats.items()}
    real = [cat_g[c] for c in REAL if c in cat_g]
    head = gmean(real)
    cat_s = {c: gmean([1 + t["service_pct"] / 100 for t in v if t["service_pct"] is not None]) for c, v in cats.items()}
    head_s = gmean([cat_s[c] for c in REAL if c in cat_s and cat_s[c]])
    avg = lambda c, m: gmean([t["measures"][m]["ratio"] for t in cats[c] if m in t["measures"]])
    L = ["# The Omni index: more for the same, or the same for less", "",
         "Every measure of every test is a ratio oriented so that above 1 is a GAIN against the system's declared aim with Omni-Compass on "
         "top of native: work (more), speed (a lower response time), machines (fewer: a cut), energy (less: a cut). Below 1 is a LOSS "
         "for work and speed, and power given for machines and energy (the key: `docs/HOW_TO_READ_THE_RESULTS.md`). A test's index is the "
         "geometric mean of its ratios; a category is the geometric mean of its tests; the headline is the geometric "
         "mean of the real categories, each weighted the same. Modelled muscles are shown beside it, never inside it. "
         "Every number is read from the test's own newest three-run table (`results/live/V<n>_*.json`, the newest engine with all three runs, made by "
         "`tools/confirm_abc.py`, `tools/pgbench_abc.py`, `tools/kafka_abc.py`, `tools/redis_abc.py`, `tools/ycsb_abc.py` and `tools/sysbench_abc.py` from the three archived runs; `tools/omni_index.py`).", "",
         f"## Headline: Omni-Compass on top of native, real machines, judged across our three runs (a change of 0.5% or more): **{pw(head, index_word(head, head_s))}, "
         f"{index_word(head, head_s)}** (more for the same, or the same for less, across work, speed, machines and energy)", "",
         "A measure enters only as its three-run reading allows (`docs/OMNI_V1.md`): GAIN, LOSS or power given in all three of our "
         "runs counts, as the geometric mean of the runs' ratios; STEADY (no difference beyond the noise) counts as exactly 1, so "
         "nothing inside the noise is claimed either way. " + engines_sentence(ts) + " Real Kubernetes, the real database, real messaging, the real cache, the real database's storage-engine cache and the real "
         "database's buffer pool are the real categories in; the steady and wandering Kubernetes tests join when their omni-v23 runs land, Azure and the card as their three-run tables land. A category's "
         "tuning workload is shown in its own table and never counted. Where native sat at its knee by design (nine tenths of its measured capacity), "
         "a queue that Omni keeps short makes the speed ratio large: that is what the test measures, and the resource it takes stands beside it. Each table names the engine it ran on.", "",
         "| Category | Index (work, speed, machines, energy) | Service reading (work and speed only) | More work by | Faster by (native p95 / omni p95) | Fewer machines by | Less energy by | Tests |",
         "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for c in list(REAL) + ["Modelled muscles (evidence S)"]:
        if c in cats:
            L.append(f"| {c} | **{with_word(cat_g[c], index_word(cat_g[c], cat_s.get(c)))}** | {with_word(cat_s.get(c), index_word(cat_s.get(c), cat_s.get(c)))} | "
                     f"{pct(avg(c, 'work'))} | {pct(avg(c, 'speed'))} | {pct(avg(c, 'machines'))} | {pct(avg(c, 'energy'))} | {len(cats[c])} |")
        elif c in PENDING:
            L.append(f"| {c} | pending | | | | | | {PENDING[c]} |")
    L += ["", f"## The second reading, declared 2026-10-09: service alone, **{pw(head_s, index_word(head_s, head_s))}, {index_word(head_s, head_s)}** (work and speed scored; machines and energy shown, not scored)", "",
          "The founder asked what a cache is for. Redis is bought for speed and spends memory to deliver it; when this reading was "
          "declared, the index counted that memory at the same weight as the speed, so the Redis table of that day read −25% while "
          "its work and hit rate were a GAIN in all three of our runs (the table that stands now, after the cost fixes of 9 to 10 "
          "October, reads STEADY on every counted workload). The question is fair and the answer is a second reading, not a changed first one: the same tests, the "
          "same three-run rule, scored on the service the stack is bought for (work inside the line and the 95th percentile) with "
          "the resources it spent or saved shown beside it and not scored. It is computed for every test alike, never for one "
          "stack, and the preregistered reading above stays the headline. The two readings say different true things. Where the "
          "governor buys service with a resource (Redis's memory ceiling, Kafka's consumers) the service reading is higher and the "
          "resource reading says what it took; where it gives a resource back for the same service (the database pools and caches) "
          "the service reading is STEADY and the resource reading carries the cut, a GAIN. Kafka's speed ratio is a hundredfold (native's "
          "queue grew at nine tenths of its capacity by design), so the service reading leans on it; a reader who wants the number "
          "without that lean has the category table, where each category is one row. Neither reading hides a LOSS: less work or a "
          "slower response in all three of our runs counts below 1 in both.", ""]
    L += ["", "Read: every column points the same way: a plus is a GAIN against the system's declared aims; a minus is a LOSS in the work "
          "and speed columns, and power given in the machines and energy columns (more of the resource put in). \"Fewer machines by +4%\" means Omni did the "
          "same work on 4% fewer machine-hours; \"less energy by +3%\" means 3% less energy for the same work; \"faster by +95%\" means "
          "native's slowest-5% response is 1.95 times Omni's (Omni answers about twice as fast); \"more work by +45%\" means 45% more work "
          "inside the response line. The energy figure on GitHub's Kubernetes is a declared model, not a meter; the database's, the "
          "messaging and the cache's energy columns are the host's CPU seconds (the compass's own CPU included; a rise in all three of our runs is "
          "power given and counts below 1); their machines columns are the resource held: connections open to the database, consumers running, the cache's "
          "memory ceiling, the storage engine's cache size, the buffer pool's size; Azure's machines are its own billed count.",
          "", "## Every test", "",
          "| Category | Test | Index | Service reading | More work by | Faster by | Fewer machines by | Less energy by | Source |", "|---|---|---:|---:|---:|---:|---:|---:|---|"]
    for t in ts:
        m = t["measures"]
        def cell(k):
            if k not in m:
                return "not taken"
            rd = m[k].get("reading", "")
            if judged(rd):
                return with_word(m[k]['ratio'], word_of(k, m[k]['ratio']))
            if rd.startswith("the same fixed-rate work"):
                return "STEADY (equal by design)"
            c = classify(rd, "spent" if k in ("machines", "energy") else "higher" if k == "work" else "lower")
            return {"same": "STEADY, the same", "noise": "STEADY, inside the noise", "disagree": "the runs disagree (counted as 1)"}.get(c, rd)
        ix = "" if t["index_pct"] is None else with_word(1 + t['index_pct'] / 100, index_word(1 + t['index_pct'] / 100, None if t['service_pct'] is None else 1 + t['service_pct'] / 100))
        sx = "not taken" if t["service_pct"] is None else with_word(1 + t['service_pct'] / 100, index_word(1 + t['service_pct'] / 100, 1 + t['service_pct'] / 100))
        L.append(f"| {t['category']} | {t['test']} | **{ix}** | {sx} | {cell('work')} | {cell('speed')} | {cell('machines')} | "
                 f"{cell('energy')} | `{t['source']}` |")
    (ROOT / "results" / "OMNI_INDEX.md").write_text("\n".join(_legal_stamp(with_own_runs(L))) + "\n")
    (ROOT / "results" / "OMNI_INDEX.json").write_text(json.dumps(
        {"headline_pct": None if head is None else 100 * (head - 1),
         "service_headline_pct": None if head_s is None else 100 * (head_s - 1),
         "categories": {c: None if g is None else 100 * (g - 1) for c, g in cat_g.items()},
         "service_categories": {c: None if g is None else 100 * (g - 1) for c, g in cat_s.items()}, "tests": ts}, indent=1) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    sys.exit(main())
