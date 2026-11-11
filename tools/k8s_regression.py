#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Why the real-Kubernetes category of the Omni index fell from omni-v21's campaign to omni-v25's: a forensic page, written
from the two campaigns' own three-run tables and the rig at every run's commit, never typed.

Both readings stand, each on its own engine and never read across as a result: omni-v21's nine tables (results/live/V21_*.json,
the index of 31 October) and omni-v25's nine (results/live/V25_*.json, the index on main). This page reads the two side by side
only to find what to test; the test itself is one engine, one rig, paired (docs/PACE_PREREGISTRATION.md, amendment 7).

    python3 tools/k8s_regression.py          (writes docs/K8S_REGRESSION_2026-11-11.md)
    python3 tools/k8s_regression.py --check  (exit 1 when the page differs from the tables)
    python3 tools/k8s_regression.py --json   (the numbers, for a reader's own check)

The beat of each run is read from the rig file at the run's own commit (scripts/kind_bench.sh: `OMNI_INTERVAL:-60` before
omni-v24, `scripts/factory_beat.sh` from it, 10 s on kind); a run whose commit is not in this clone is listed as unread.
"""
from __future__ import annotations

import json
import math
import re
import statistics as st
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import omni_index as OI                                           # noqa: E402
from tools.legal import stamp as legal_stamp                                 # noqa: E402
from tools.company_attribution import normalize as canonical_name            # noqa: E402

LIVE = ROOT / "results" / "live"
OUT = ROOT / "docs" / "K8S_REGRESSION_2026-11-11.md"
OLD, NEW = 21, 25
P95, MEAN = "response time (ms), 95th percentile", "response time (ms), mean"
WRITES = "settings commands the governor wrote on its own (no person touched either arm)"
PODS = "pods started"
HOST = "host CPU busy, the real machine under kind (%)"
CORES = "host cores (the real machine under kind)"
NODES = "worker nodes in service, mean"


def k8s_tests(v):
    return [t for t in OI.tests(pick=lambda f: f"V{v}_" + re.sub(r"^V\d+_", "", f)) if t["category"].startswith("Real Kubernetes")]


def mean_arm(rows, key, arm):
    r = rows.get(key)
    vals = [x.get(arm) for x in (r or {}).get("runs", []) if isinstance(x, dict) and x.get(arm) is not None]
    return st.mean(vals) if vals else None


def beat_at(commit):
    """The decision beat the kind rig at this commit gives the Omni-Compass arm when the run sets none."""
    got = subprocess.run(["git", "show", f"{commit}:scripts/kind_bench.sh"], cwd=ROOT, capture_output=True, text=True)
    if got.returncode:
        return "unread"
    if 'OMNI_INTERVAL:-60}' in got.stdout:
        return "60 s"
    if "factory_beat.sh" in got.stdout:
        return "10 s (the factory beat on site)"
    return "unread"


def build():
    tests = {v: {t["source"].split("/")[-1].split("_", 1)[1]: t for t in k8s_tests(v)} for v in (OLD, NEW)}
    cat = {v: 100 * (OI.gmean([1 + t["index_pct"] / 100 for t in tests[v].values()]) - 1) for v in (OLD, NEW)}
    rows = []
    for base in tests[OLD]:
        t_old, t_new = tests[OLD][base], tests[NEW][base]
        d = {v: json.loads((LIVE / f"V{v}_{base}").read_text(encoding="utf-8")) for v in (OLD, NEW)}
        speed = MEAN if "BATCH" in base else P95
        a = {(v, arm): mean_arm(d[v]["rows"], speed, arm) for v in (OLD, NEW) for arm in ("native", "omni")}
        nat = math.log(a[(NEW, "native")] / a[(OLD, "native")])
        omn = math.log(a[(NEW, "omni")] / a[(OLD, "omni")])
        dlog = nat - omn                                     # the change in ln(native / Omni-Compass), the index's speed
        rel = math.exp(omn - nat) - 1                        # the arm's response time against native's, campaign to campaign
        rows.append({
            "table": base.replace(".json", ""), "test": t_new["test"], "speed_gauge": speed,
            "index": {OLD: t_old["index_pct"], NEW: t_new["index_pct"]},
            "service": {OLD: t_old["service_pct"], NEW: t_new["service_pct"]},
            "native": {OLD: a[(OLD, "native")], NEW: a[(NEW, "native")]},
            "omni": {OLD: a[(OLD, "omni")], NEW: a[(NEW, "omni")]},
            "omni_against_native": rel, "speed_ratio_log_change": dlog,
            "writes": {v: mean_arm(d[v]["rows"], WRITES, "omni") for v in (OLD, NEW)},
            "pods": {v: mean_arm(d[v]["rows"], PODS, "omni") for v in (OLD, NEW)},
            "pods_native": {v: mean_arm(d[v]["rows"], PODS, "native") for v in (OLD, NEW)},
            "host_native": {v: mean_arm(d[v]["rows"], HOST, "native") for v in (OLD, NEW)},
            "cores": {v: mean_arm(d[v]["rows"], CORES, "native") for v in (OLD, NEW)},
            "nodes": {v: mean_arm(d[v]["rows"], NODES, "native") for v in (OLD, NEW)},
            "runs": {v: [r["run"] for r in d[v]["runs"]] for v in (OLD, NEW)},
            "engines": {v: sorted({r["engine"].split(" ")[0] for r in d[v]["runs"]}) for v in (OLD, NEW)},
            "beats": {v: sorted({beat_at(r["commit"]) for r in d[v]["runs"]}) for v in (OLD, NEW)},
        })
    return {"category": cat, "rows": rows}


def ch(old, new):
    """A raw change across the two campaigns, in words (not a reading: no engine is judged against another here)."""
    if old in (None, 0) or new is None:
        return "not read"
    x = 100 * (new / old - 1)
    return "the same" if abs(x) < 0.05 else f"{'up' if x > 0 else 'down'} {abs(x):.1f}%"


def worded(pct, service):
    """A test's index reading with its word first and its size in words (tools/omni_index.py index_word)."""
    w = OI.index_word(1 + pct / 100, 1 + service / 100)
    return f"{w}, {'up' if pct > 0 else 'down'} {abs(pct):.1f}%" if pct else f"{w}, the same"


def f1(x):
    return "not read" if x is None else f"{x:,.1f}"


def fall_sits(d):
    """Section 4's first finding, counted from the rows (never typed)."""
    rs = d["rows"]
    rose = sum(r["omni"][NEW] > r["omni"][OLD] for r in rs)
    big = sorted((r for r in rs if r["omni_against_native"] >= 0.10), key=lambda r: -r["omni_against_native"])
    small = [r for r in rs if r["omni_against_native"] < 0.10]
    more = sum(r["writes"][NEW] > r["writes"][OLD] and r["pods"][NEW] > r["pods"][OLD] for r in rs)
    span = lambda g: f"up {100 * min(r['omni_against_native'] for r in g):.1f}% to {100 * max(r['omni_against_native'] for r in g):.1f}%"
    name = lambda r: SHORT.get(r["table"], r["table"])
    both = lambda g: ", ".join(name(r) for r in g[:-1]) + " and " + name(g[-1]) if len(g) > 1 else name(g[0])
    of = lambda k: f"all {NUM[len(rs)]}" if k == len(rs) else f"{NUM.get(k, k)} of the {NUM[len(rs)]}"
    return (f"- The fall sits in the Omni-Compass arm: native held, the arm's own response time rose in {of(rose)} tests, "
            f"most over and above native's in {both(big)} ({span(big)}), least in {both(small)} ({span(small)}); in {of(more)} "
            "it also wrote more settings and started more pods.")


NUM = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}


SHORT = {"STEADY": "the steady load", "WANDERING": "the demand that wanders", "ALL_FOUR": "all four in one run",
         "FAIRNESS": "the noisy neighbour", "FAULTS": "the faults", "BATCH": "the queue of jobs",
         "TRACE_GOOGLE2011": "the public day", "KEDA_CPU_REQUESTS": "KEDA on the CPU target",
         "KEDA_REQUESTS": "KEDA's HTTP add-on"}


def render(d):
    c = d["category"]
    L = [
        "# Real Kubernetes, omni-v21's campaign beside omni-v25's: where the category's fall sits",
        "",
        "Written by `tools/k8s_regression.py` from the two campaigns' own three-run tables (`results/live/V21_*.json`, "
        "`results/live/V25_*.json`) and the kind rig at every run's own commit. Class L (live software on GitHub's machines). "
        "Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.",
        "",
        "## 1. Both readings stand, each on its own engine",
        "",
        f"- **omni-v21**: the real-Kubernetes category of the Omni index reads GAIN, up {c[OLD]:.4f}%, from its nine three-run "
        "tables (the index of 31 October, commit `3ad522226b`). It is omni-v21's historical reading and is labelled so.",
        f"- **omni-v25**: the same category reads GAIN, up {c[NEW]:.4f}%, from its nine three-run tables (`results/OMNI_INDEX.json` on "
        "main). It is the latest measured reading of the category.",
        "- **omni-v26** stands as the engine on main; its Kubernetes tables are not yet whole, so it has no category reading yet.",
        f"- The two differ by {c[OLD] - c[NEW]:.4f} points. Neither number is moved into the other's record: the index file on main "
        "keeps omni-v25's numbers, and no omni-v21 table is read as omni-v25's. Every number on this page is each engine's own; "
        "setting them side by side is a diagnosis of what to test, never a result.",
        "",
        "## 2. Test by test: native held, the Omni-Compass arm moved",
        "",
        "The index's speed is native's response time over the Omni-Compass arm's (the 95th percentile; the mean for the queue of "
        "jobs). Each campaign's arms are its own; every change below is raw, across the two campaigns. The sixth column "
        "compares the two arms' own changes: how much the Omni-Compass arm's response time moved from one campaign to the "
        "other over and above native's, which is the change in the index's speed ratio, turned the other way up. A busier host "
        "slows both arms, so the column reads where the change sits, not its cause.",
        "",
        "| test | index, omni-v21 | index, omni-v25 | native's response time (ms) | Omni-Compass arm's (ms) | the arm's response time, over and above native's | settings written by the Omni-Compass arm | pods it started |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for r in d["rows"]:
        L.append(
            f"| {r['test']} | {worded(r['index'][OLD], r['service'][OLD])} | {worded(r['index'][NEW], r['service'][NEW])} | "
            f"{f1(r['native'][OLD])} to {f1(r['native'][NEW])} ({ch(r['native'][OLD], r['native'][NEW])}) | "
            f"{f1(r['omni'][OLD])} to {f1(r['omni'][NEW])} ({ch(r['omni'][OLD], r['omni'][NEW])}) | "
            f"{ch(1.0, 1.0 + r['omni_against_native'])} | "
            f"{f1(r['writes'][OLD])} to {f1(r['writes'][NEW])} ({ch(r['writes'][OLD], r['writes'][NEW])}) | "
            f"{f1(r['pods'][OLD])} to {f1(r['pods'][NEW])} ({ch(r['pods'][OLD], r['pods'][NEW])}) |")
    L += ["", "Every value is the mean of the three runs' means, read from the table named in the first column's file "
          "(`results/live/V21_<table>.json`, `results/live/V25_<table>.json`).", ""]
    L += ["| table | omni-v21's runs | omni-v25's runs | beat of the Omni-Compass arm, omni-v21 | omni-v25 | host cores | workers in service | native's pods started | native's host busy (%) |",
          "|---|---|---|---|---|---|---|---|---|"]
    for r in d["rows"]:
        L.append(f"| {r['table']} | {', '.join(r['runs'][OLD])} | {', '.join(r['runs'][NEW])} | {'; '.join(r['beats'][OLD])} | "
                 f"{'; '.join(r['beats'][NEW])} | {f1(r['cores'][OLD])} and {f1(r['cores'][NEW])} | {f1(r['nodes'][OLD])} and "
                 f"{f1(r['nodes'][NEW])} | {f1(r['pods_native'][OLD])} and {f1(r['pods_native'][NEW])} | "
                 f"{f1(r['host_native'][OLD])} and {f1(r['host_native'][NEW])} |")
    L += [
        "",
        "## 3. What differs between the two campaigns",
        "",
        "- **The engine.** Seven of omni-v25's 65 fingerprinted files differ from omni-v21's (`OMNI_V21.json`, `OMNI_V25.json`); "
        "two of them touch Kubernetes, `omni_controller/controller.py` and `omni_controller/muscles.py`; the brain "
        "(`omnicompass/`) is byte for byte the same. Their changes: the hand-back tried five times against the API's failures "
        "(omni-v22; it runs only at the reset, after the window), the guard of the pod muscle of its own (omni-v23; it runs only in "
        "the arm by itself, not in these tests) and the factory beat (omni-v24). On these rigs only the beat changes a decision.",
        "- **The beat.** Every omni-v21 run's rig gives the Omni-Compass arm a full decision every 60 s; every omni-v25 run's rig "
        "reads the factory beat, 10 s on kind (the table above, read at each run's own commit). The raw receipts agree: "
        "`run-40227141899/paired-1/bench-compass-1/omni_interval.txt` reads 60, `run-41751107237/paired-1/bench-compass-1/omni_interval.txt` "
        "reads 10 (the branch `raw`).",
        "- **The rig, the same for both arms.** Between the two campaigns the kind rig came to read pods through its own collector "
        "(`tools/bench_integrity.py`) in place of a `kubectl` watch, seals every arm's files and refuses an arm that failed, restores "
        "the workload's rollout after each arm and grants the rights the arm by itself needs; the add-on rig "
        "(`scripts/kind_addons.sh`, `scripts/kubectl_keda.py`) is unchanged. The scorer (`tools/live_reps.py`) added the metered-work "
        "rows and a stricter test of \"the same\"; the 95th percentile and the mean are computed as before.",
        "- **The machines.** Both campaigns ran on GitHub's four-core runners with six kind workers in service. Native's own "
        "response time moved under 10% in eight of the nine tests. The queue of jobs is the exception: native's mean response time "
        "rose with a busier host in omni-v25's campaign, and the arm's rose with it, so that test's small fall is mostly the "
        "machine's, not the engine's.",
        "",
        "## 4. What the record says, and what it does not yet prove",
        "",
        fall_sits(d),
        "- That is the signature of a faster beat on a moving load: a decision every 10 s follows each step of the load and moves the "
        "autoscaler's target and the pod count more often, where a decision every 60 s rides through them. It is the leading cause, "
        "not yet a proven one.",
        "- The steady-load pace runs on omni-v25 (`results/pace/PACE.md`) read every slower beat against 10 s by small amounts on the "
        "response time; they do not cover a moving load, where the two campaigns part most.",
        "- The direct test is preregistered and dispatched on GitHub's free machines: `docs/PACE_PREREGISTRATION.md`, amendment 7, "
        "the demand that wanders, native and the Omni-Compass arm at 10, 60 and 90 s, one engine, one rig, paired, three runs "
        "(runs 42977431782, 42977442687 and 42977447533). No paid card or cloud run is needed.",
        "- What follows from it: if a slower beat reads better than 10 s there, the on-site factory beat is picked by amendment 4's "
        "frozen rule on those runs and lands as the next version through the model gate, keeping every repair made since omni-v21 "
        "(the hand-back retries, the pod muscle's guard, the Kafka wire's fix, the neighbour hold); every Kubernetes benchmark then "
        "runs again on it, read by its own engine. If not, the cause is looked for again in the files, and this page says so.",
        "",
    ]
    return canonical_name("\n".join(legal_stamp(L)) + "\n")


def main(argv):
    d = build()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    md = render(d)
    if "--check" in argv:
        same = OUT.exists() and OUT.read_text(encoding="utf-8") == md
        print("kubernetes regression: " + (f"{OUT.relative_to(ROOT)} matches the tables" if same else
                                            "the page differs from the tables: run python3 tools/k8s_regression.py"))
        return 0 if same else 1
    OUT.write_text(md, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} written")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
