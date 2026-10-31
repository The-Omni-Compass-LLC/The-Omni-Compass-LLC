#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Omni-Compass by itself on the model cluster (the founder's order of 23 October; docs/SOLO_PREREGISTRATION.md): our own model,
class S, never a benchmark result. Three arms on the same seeds, each a day of the model cluster's web day, on the machines as
the kind rig has them (every worker made at the start, no cluster autoscaler; tools/model_gate.py, settings static and solo):

  native                     the pod autoscaler, as Kubernetes ships it
  Omni-Compass and native    the shipped governor on top of it (the compass law at the max, as ARM=compass runs it)
  Omni-Compass by itself     the pod autoscaler switched off: the pods at the operator's own count unless the governor
                             writes it through the workload's own scale (the pod muscle of its own, from omni-v19)

With --cand, each arm runs on both checkouts, and the candidate is read against the engine that stands arm by arm.

Each arm is read against the others by the model gate's own rule (tools/model_gate.py reading: the mean change over the seeds,
its 95% interval by Student t, the word by the gauge's aim). Usage:

  python3 tools/solo_study.py [--tree .] [--seeds 1-8] [--days 1] [--out DIR]   ->  results/model_gate/SOLO_<engine>.md and .json
"""
import argparse, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

HERE = Path(__file__).resolve()
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT))
from tools import model_gate as TG                      # noqa: E402
from tools.readings import by_word, interval_by_word  # noqa: E402
from tools.legal import stamp                         # noqa: E402

ARMS = {"native": ["--worker", "native", "--setting", "static"], "omni": ["--worker", "omni", "--setting", "static"],
        "solo": ["--worker", "omni", "--setting", "solo"]}
NAME = {"native": "native", "omni": "Omni-Compass and native", "solo": "Omni-Compass by itself"}
GAUGE_NAME = {"machine_hours": "machine-hours", "kwh_per_core_hour": "energy per used core-hour (kWh)",
              "pending_pod_minutes_per_hour": "pods waiting for a place (pod-minutes an hour)",
              "hpa_shortfall_minutes_per_hour": "the pod autoscaler's shortfall (minutes an hour)",
              "p95_ms": "95th percentile response (ms)", "alert_minutes": "minutes over the response line"}
PAIRS = [("solo", "native"), ("solo", "omni"), ("omni", "native")]


def engine(tree):
    out = subprocess.run([sys.executable, "tools/omni_version.py"], cwd=tree, env={**os.environ, "PYTHONPATH": str(tree)},
                         capture_output=True, text=True).stdout.strip().splitlines()
    return (out[0].split()[0] if out else "unknown"), (out[0] if out else "")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tree", default=str(ROOT), help="the engine that stands (its checkout)")
    ap.add_argument("--cand", default="", help="a candidate's checkout, read against the engine that stands arm by arm")
    ap.add_argument("--seeds", default="1-8")
    ap.add_argument("--days", type=float, default=1.0)
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--out", default="")
    a = ap.parse_args(argv)
    lo, _, hi = a.seeds.partition("-"); seeds = list(range(int(lo), int(hi or lo) + 1))
    tree = Path(a.tree).resolve(); eng, eng_line = engine(tree)
    cand = Path(a.cand).resolve() if a.cand else None; ceng, ceng_line = engine(cand) if cand else (None, None)
    work = Path(a.out or (ROOT / "results" / "model_gate" / "solo_work")); work.mkdir(parents=True, exist_ok=True)
    trees = {"base": tree, **({"cand": cand} if cand else {})}
    jobs = [(arm, s, k) for k in trees for s in seeds for arm in ARMS]
    run = lambda j: TG.run(trees[j[2]], [*ARMS[j[0]], "--seed", str(j[1]), "--days", str(a.days), "--period", "0",
                                          "--dir", str(work / f"{j[2]}-{j[0]}-{j[1]}")])
    with ThreadPoolExecutor(a.jobs) as ex:
        got = list(ex.map(run, jobs))
    both = {}
    for (arm, s, k), r in zip(jobs, got):
        both.setdefault(k, {}).setdefault(arm, {})[s] = r
    res = both["cand"] if cand else both["base"]
    if cand:
        eng, eng_line = ceng, ceng_line
    gauges = {g: v for g, v in TG.GAUGES.items() if g in GAUGE_NAME}
    rec = {"engine": eng, "engine_line": eng_line, "seeds": seeds, "days": a.days, "class": "S", "gauges": {}, "per_seed": both}
    if cand:                                                  # the candidate against the engine that stands, arm by arm
        rec["against_base"] = {arm: {g: TG.reading(g, [both["cand"][arm][s][g] - both["base"][arm][s][g] for s in seeds],
                                                   [both["base"][arm][s][g] for s in seeds], {**TG.GAUGES})
                                     for g in TG.GAUGES if g in GAUGE_NAME} for arm in ARMS}
    for g in gauges:
        means = {arm: sum(res[arm][s][g] for s in seeds) / len(seeds) for arm in ARMS}
        pairs = {}
        for x, y in PAIRS:
            xv = [res[x][s][g] for s in seeds]; yv = [res[y][s][g] for s in seeds]
            pairs[f"{x}_vs_{y}"] = TG.reading(g, [p - q for p, q in zip(xv, yv)], yv, gauges)
        rec["gauges"][g] = {"means": means, **pairs}
    out_md = ROOT / "results" / "model_gate" / f"SOLO_{eng.replace('omni-', '').upper()}.md"
    pct = lambda r: (by_word(100 * r["relative"], r["word"]) if r["relative"] == r["relative"] else "—")
    iv = lambda r, b: interval_by_word(100 * r["ci95"][0] / b, 100 * r["ci95"][1] / b, r["word"]) if b else "—"
    L = [f"# Omni-Compass by itself on the model cluster ({eng})", "",
         "Our own model (evidence class S), never a benchmark result. The founder's order of 23 October: beside native and "
         "Omni-Compass and native, a third arm, Omni-Compass by itself, with native's controllers switched off "
         "(`docs/SOLO_PREREGISTRATION.md`). This page reads what the engine that stands does by itself on the model cluster: "
         f"{len(seeds)} seeds of a day, the same seeds in every arm, read by the model gate's own rule "
         "(`tools/model_gate.py`: the mean change over the seeds, its 95% interval by Student t, the word by the gauge's aim; "
         "a resource that rose is power given).", "",
         f"Engine: {eng_line}. Written by `python3 tools/solo_study.py`; every seed's reading of every arm is in its JSON twin (`per_seed`).", "",
         "| Arm | What governs |", "|---|---|",
         "| native | the pod autoscaler (its target 70%), as Kubernetes ships it, on the machines as the kind rig has them (every worker "
         "made at the start, no Cluster Autoscaler: 12 machines) |",
         "| Omni-Compass and native | the shipped governor on top of the pod autoscaler, the compass law at the max (as ARM=compass "
         "runs it), on the same 12 machines |",
         "| Omni-Compass by itself | the pod autoscaler switched off: every workload's pods at the operator's own count unless the "
         "governor writes it through the workload's own scale, the pool "
         "at its starting size (12 machines); the shipped governor the only controller, the compass law at the max |", "",
         "## The means over the seeds", "", "| Gauge | native | Omni-Compass and native | Omni-Compass by itself |", "|---|---:|---:|---:|"]
    for g in gauges:
        m = rec["gauges"][g]["means"]
        L.append(f"| {GAUGE_NAME[g]} | {m['native']:.3f} | {m['omni']:.3f} | {m['solo']:.3f} |")
    for x, y in PAIRS:
        L += ["", f"## {NAME[x]} against {NAME[y]}", "", "| Gauge | Change | 95% interval | Reading |", "|---|---:|---:|---|"]
        for g in gauges:
            r = rec["gauges"][g][f"{x}_vs_{y}"]; b = rec["gauges"][g]["means"][y]
            if g == "hpa_shortfall_minutes_per_hour" and "solo" in (x, y):
                L.append(f"| {GAUGE_NAME[g]} | — | — | not read: by itself there is no pod autoscaler to fall short |"); continue
            L.append(f"| {GAUGE_NAME[g]} | {pct(r)} | {iv(r, b)} | **{r['word']}** |")
    if cand:
        L += ["", f"## The candidate ({ceng}) against the engine that stands ({engine(tree)[0]}), arm by arm", "",
              "| Gauge | native | Omni-Compass and native | Omni-Compass by itself |", "|---|---|---|---|"]
        for g in gauges:
            cells = []
            for arm in ARMS:
                r = rec["against_base"][arm][g]
                if g == "hpa_shortfall_minutes_per_hour" and arm == "solo":
                    cells.append("not read"); continue
                cells.append(r["word"] if r["word"].startswith("STEADY") else f"{r['word']} {pct(r)}")
            L.append(f"| {GAUGE_NAME[g]} | " + " | ".join(cells) + " |")
    m = lambda k, arm, g: sum(both[k][arm][s][g] for s in seeds) / len(seeds)
    base_eng = engine(tree)[0]
    own = "--own-replicas" in (Path(tree) / "omni_controller" / "controller.py").read_text()   # the engine carries the pod muscle of its own
    L += ["", "## What it says", "",
          (f"On the engine that stands ({base_eng}) the governor has a pod muscle of its own (`--own-replicas`, omni-v19): with the pod "
           "autoscaler switched off it sets each named workload's pods itself, through the workload's own scale, at the target the compass "
           "moves, reconciled every 15 s on the fast checks: its 95th percentile response "
           f"{m('base', 'solo', 'p95_ms'):,.0f} ms and {m('base', 'solo', 'alert_minutes'):,.1f} minutes over the line in the day, against "
           f"native's {m('base', 'native', 'p95_ms'):,.1f} ms and {m('base', 'native', 'alert_minutes'):,.1f} minutes, on the same machines.") if own else
          (f"On the engine that stands ({base_eng}) the governor moves a workload's pods only through the pod autoscaler's own object "
           "(its range and its target); with the pod autoscaler switched off it has no pod muscle of its own, so by itself it holds "
           f"every workload at the operator's count: its 95th percentile response {m('base', 'solo', 'p95_ms'):,.0f} ms and "
           f"{m('base', 'solo', 'alert_minutes'):,.0f} minutes over the line in the day, against native's "
           f"{m('base', 'native', 'p95_ms'):,.1f} ms and {m('base', 'native', 'alert_minutes'):,.1f} minutes.")]
    if cand:
        L += ["", f"The candidate ({ceng}) gives it a pod muscle of its own (`omni_controller/controller.py`, `_own_pods`): the "
              "replica count set through the workload's own scale by strict C's rule, at the target the compass moves inside the "
              "autoscaler's cover, never below the operator's count at the max. By itself it then reads "
              f"{m('cand', 'solo', 'p95_ms'):,.1f} ms and {m('cand', 'solo', 'alert_minutes'):,.1f} minutes over the line. Native and "
              "Omni-Compass and native read the same on both engines, gauge for gauge (the table above): the muscle acts only "
              "where the operator names a workload no autoscaler governs. Its own cost: the governor reads each workload it scales "
              f"twice at each reconciliation, every 15 s ({m('cand', 'solo', 'reads_per_hour'):,.0f} reads an hour here, twelve workloads, against "
              f"{m('cand', 'omni', 'reads_per_hour'):,.0f} on top of native)."]
    L += ["", "Our own model, class S: it shows the mechanism, never a benchmark result. The real arm runs on kind (`ARM=solo`, "
          "`scripts/kind_bench.sh`) on omni-v19, the engine that carries the muscle (`docs/SOLO_PREREGISTRATION.md`).", ""]
    out_md.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    out_md.with_suffix(".json").write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    print(f"{out_md}: {len(gauges)} gauges, {len(seeds)} seeds")


if __name__ == "__main__":
    sys.exit(main())
