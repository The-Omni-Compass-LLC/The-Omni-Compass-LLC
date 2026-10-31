#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The record of the orchestrators on the same organisms (tools/orchestrators_arm.py; docs/ORCHESTRATORS_PREREGISTRATION.md):
results/orchestrators/ORCHESTRATORS.json, every run's gauges and every reading, and ORCHESTRATORS.md, the page.

  python3 tools/orchestrators_report.py [--out results/orchestrators]   write the page again from the record

Every reading is paired by repetition (the same injection in both arms) and read by the one key (tools/readings.py): the word
first, then the size of the change with the word's sign; under 0.5% STEADY. Our own models, evidence class S."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp  # noqa: E402
from tools.readings import OWN_RUNS, by_word, interval_by_word  # noqa: E402

NAMES = {"p95_ms": "the 95th percentile response time", "alert_minutes": "minutes over the line (500 ms)",
         "requests_failed": "requests failed (unanswered in 10 s)", "requests_served": "requests served",
         "pending_pod_minutes": "pods waiting for a place (pod-minutes)", "batch_turnaround_s": "a job's turnaround",
         "batch_makespan_s": "the stream's makespan (first job in to last job done)", "batch_pods_done": "batch pods done",
         "machine_hours": "machine-hours", "energy_kwh": "energy"}
WORDS = ("GAIN", "LOSS", "power given", "STEADY")


def engine_name():
    try:
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py")], capture_output=True, text=True,
                             cwd=ROOT, timeout=120).stdout.strip().splitlines()
        return out[0].split()[0] if out else "unknown"
    except (OSError, subprocess.SubprocessError):
        return "unknown"


def cell(r):
    if r is None:
        return "—"
    return f"{r['word']} {by_word(r['pct'], r['word'])}"


def counts(readings):
    c = {w: 0 for w in WORDS}
    for r in readings:
        if r:
            c[r["word"]] += 1
    return " · ".join(f"{w} {c[w]}" for w in WORDS if c[w]) or "—"


def build(runs, reps, orgs, sets, orchs):
    """{setting: {organism: {...}}}: the means and the paired readings."""
    from tools.orchestrators_arm import GAUGES, read
    rec = {}
    for s in sets:
        for o in orgs:
            nat = [runs.get((o, s, "default", "native", k)) for k in range(reps)]
            arms = {"native": nat}
            for orch in orchs:
                arms[f"orch:{orch}"] = nat if orch == "default" else [runs.get((o, s, orch, "orch", k)) for k in range(reps)]
                arms[f"omni:{orch}"] = [runs.get((o, s, orch, "omni", k)) for k in range(reps)]
            failed = sorted({f"{name} repetition {k}: {g['_failed']}" for name, gs in arms.items()
                             for k, g in enumerate(gs) if g and "_failed" in g} |
                            {f"{name} repetition {k}: no run" for name, gs in arms.items() for k, g in enumerate(gs) if g is None})
            gauges = [g for g in GAUGES if all(x and g in x for x in nat)]

            def pair(a, b, g):
                ps = [(x[g], y[g]) for x, y in zip(arms[a], arms[b]) if x and y and g in x and g in y]
                return read(ps, *GAUGES[g]) if len(ps) >= 2 else None
            entry = {"benchmark": None, "gauges": gauges, "failed": failed, "means": {}, "vs_native": {}, "omni_vs_orch": {},
                     "omni_vs_native": {}, "omni_writes": {}}
            for name, gs in arms.items():
                ok = [x for x in gs if x and "_failed" not in x]
                entry["means"][name] = {g: sum(x[g] for x in ok) / len(ok) for g in gauges if ok and all(g in x for x in ok)}
            for orch in orchs:
                if orch != "default":
                    entry["vs_native"][orch] = {g: pair("native", f"orch:{orch}", g) for g in gauges}
                entry["omni_vs_orch"][orch] = {g: pair(f"orch:{orch}", f"omni:{orch}", g) for g in gauges}
                entry["omni_vs_native"][orch] = {g: pair("native", f"omni:{orch}", g) for g in gauges}
                ok = [x for x in arms[f"omni:{orch}"] if x and "_failed" not in x]
                entry["omni_writes"][orch] = sum(x.get("_writes", 0) for x in ok) / max(1, len(ok))
            rec.setdefault(s, {})[o] = entry
    return rec


def fmt(v, g):
    if v is None:
        return "—"
    if g in ("machine_hours", "energy_kwh"):
        return f"{v:.3f}"
    if g in ("requests_served", "requests_failed", "batch_pods_done"):
        return f"{v:,.0f}"
    return f"{v:,.1f}"


def render(rec, meta):
    from tools.orchestrators_arm import ORCHESTRATORS, ORGANISMS, SETTINGS
    orchs = meta["orchestrators"]
    L = ["# The orchestrators on the same organisms, with the same injection", "",
         f"Our own models (evidence class S), never a benchmark result. The record of `tools/orchestrators_arm.py`, preregistered in "
         f"`docs/ORCHESTRATORS_PREREGISTRATION.md` before its first run; {meta['reps']} repetitions on every organism, repetition k "
         f"seeded from the engine's jump generator (base {meta['base']}), the same injection in every arm of it. Omni-Compass is the "
         f"shipped Kubernetes governor of {meta['engine']} (`omni_controller/`) at its factory flags, the rig's own.", "",
         "The founder's order of 25 October: \"all the orchestrators to have the same injection ran through. Those orchestrators sit "
         "on the same organism. And there lies the third arm ... And of course then OmniCompass on top of that same stack.\"", "",
         "## The three arms", "",
         "| Arm | What runs on the organism |", "|---|---|",
         "| native | Kubernetes alone: its default scheduler places every pod, the service's autoscaler (HPA), and in the cloud the Cluster Autoscaler |",
         "| the orchestrator | the same organism and the same work, every pod sent to the orchestrator the way its project documents it, its shipped rule deciding what goes in and where |",
         "| Omni-Compass on top | the orchestrator's arm with Omni-Compass's governor on top; it writes only what it writes on a real cluster (the service's autoscaler, a machine's idle mark, the service pods' processor limit), never an orchestrator's own objects |",
         "", "## The orchestrators", "", "| Orchestrator | Its rule in the model, from its own release |", "|---|---|"]
    for k in orchs:
        L.append(f"| {ORCHESTRATORS[k]} | {meta['rules'][k]} |")
    L += ["", "## The organisms", "",
          "Each organism carries one injection, from the benchmark named; each runs in both settings.", "",
          "| Organism | Benchmark it carries | Window | Clients over the window |", "|---|---|---:|---|"]
    for o in meta["organisms"]:
        b, dur, steps, two, batch, faults = ORGANISMS[o]
        extra = (" (two services)" if two else "") + (" + the batch stream" if batch and any(steps) else "") + (" + the fault drill" if faults else "")
        L.append(f"| {o} | {b} | {dur} s | {' '.join(map(str, steps)) if any(steps) else 'none (the batch stream alone)'}{extra} |")
    L += ["", "| Setting | The machines |", "|---|---|",
          "| on-site | the kind rig: six workers that are containers on one runner, each reporting the runner's 4 cores; the pods share the 3 cores the governor's own leaves; no cluster autoscaler |",
          "| cloud | machines of 2 cores of their own (1.9 allocatable), the Cluster Autoscaler at its defaults, 2 to 9 machines, 90 s to boot |",
          "", "## How to read a cell", "",
          "Each cell is a paired reading by the one key: the word first, then the size of the change with the word's sign "
          "(GAIN +, LOSS −, power given +, STEADY =). Time waited, missed or failed that fell is a GAIN; work that rose is a GAIN; a "
          "resource spent that fell is a cut (GAIN) and one that rose is power given, never a loss. A change under 0.5% is STEADY. "
          "Beside each count, the detailed tables give the 95% interval over the repetitions.", ""]
    for s in meta["settings"]:
        sname = "on-site (the kind rig)" if s == "onsite" else "the cloud"
        L += [f"## {sname[0].upper() + sname[1:]}: each orchestrator against Kubernetes alone", "",
              "The words over every gauge of the organism (how many read GAIN, LOSS, power given, STEADY).", "",
              "| Organism | " + " | ".join(ORCHESTRATORS[k] for k in orchs if k != "default") + " |",
              "|---|" + "---|" * (len(orchs) - 1)]
        for o in meta["organisms"]:
            e = rec[s][o]
            L.append(f"| {o} | " + " | ".join(counts(e["vs_native"][k].values()) for k in orchs if k != "default") + " |")
        L += ["", f"## {sname[0].upper() + sname[1:]}: Omni-Compass on top of each orchestrator, against that orchestrator alone", "",
              "| Organism | " + " | ".join(ORCHESTRATORS[k] for k in orchs) + " |", "|---|" + "---|" * len(orchs)]
        for o in meta["organisms"]:
            e = rec[s][o]
            L.append(f"| {o} | " + " | ".join(counts(e["omni_vs_orch"][k].values()) for k in orchs) + " |")
        L.append("")
    L += ["## Every organism, gauge by gauge", ""]
    for s in meta["settings"]:
        for o in meta["organisms"]:
            e = rec[s][o]
            L += [f"### {o}, {'on-site' if s == 'onsite' else 'cloud'}", ""]
            if e["failed"]:
                L += ["Runs that failed (listed, never dropped): " + "; ".join(e["failed"]), ""]
            head = ["Gauge", "native (mean)"] + [f"{ORCHESTRATORS[k]}" for k in orchs if k != "default"]
            L += ["Each orchestrator against Kubernetes alone (its mean, then its reading):", "",
                  "| " + " | ".join(head) + " |", "|---|---:|" + "---|" * (len(head) - 2)]
            for g in e["gauges"]:
                row = [NAMES.get(g, g), fmt(e["means"]["native"].get(g), g)]
                for k in orchs:
                    if k != "default":
                        r = e["vs_native"][k][g]
                        row.append(f"{fmt(e['means'][f'orch:{k}'].get(g), g)}, {cell(r)}")
                L.append("| " + " | ".join(row) + " |")
            L += ["", "Omni-Compass on top of each, against that orchestrator alone (the reading, its 95% interval):", "",
                  "| Gauge | " + " | ".join(ORCHESTRATORS[k] for k in orchs) + " |", "|---|" + "---|" * len(orchs)]
            for g in e["gauges"]:
                row = [NAMES.get(g, g)]
                for k in orchs:
                    r = e["omni_vs_orch"][k][g]
                    row.append(f"{cell(r)} ({interval_by_word(r['lo'], r['hi'], r['word'])})" if r else "—")
                L.append("| " + " | ".join(row) + " |")
            L += ["", "Omni-Compass's writes a run (mean): " +
                  ", ".join(f"{ORCHESTRATORS[k]} {e['omni_writes'][k]:.1f}" for k in orchs), ""]
    L += ["## What the model leaves out", "",
          "The processor alone is modelled (memory, disks and the network are not); a request's cost, the clients' rate and the pod "
          "start times are the rig's own calibration (the model gate's); every orchestrator's rule is written from its release "
          "and documentation, never from its code, and each is listed above with the file it was read from. The Gödel scheduler, "
          "KubeRay, Crane and the multi-cluster orchestrators (Karmada, Open Cluster Management, Armada) run on GitHub's machines "
          "four ways (`results/live/GOVERNORS.md`); their rules join this model once each one's shipped default is read from its "
          "release, and nothing is written for them here before that.", "",
          OWN_RUNS, ""]
    return "\n".join(stamp(L)) + "\n"


def write_report(runs, a, out: Path):
    from tools.orchestrators_arm import ORCHESTRATORS, RULES
    out.mkdir(parents=True, exist_ok=True)
    orgs, sets, orchs = a.organisms.split(","), a.settings.split(","), a.orchs.split(",")
    flat = {(o, s, orch, arm, k): g for (o, s, orch, arm, k, _), g in runs.items()}
    rec = build(flat, a.reps, orgs, sets, orchs)
    meta = {"engine": engine_name(), "reps": a.reps, "base": a.base, "organisms": orgs, "settings": sets,
            "orchestrators": orchs, "rules": {k: RULES[k] for k in orchs}, "evidence": "S (our own models)"}
    data = {"meta": meta, "readings": rec,
            "runs": [{"organism": o, "setting": s, "orchestrator": orch, "arm": arm, "rep": k, "gauges": g}
                     for (o, s, orch, arm, k), g in sorted(flat.items())]}
    (out / "ORCHESTRATORS.json").write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")
    (out / "ORCHESTRATORS.md").write_text(render(rec, meta))
    print(f"wrote {out / 'ORCHESTRATORS.md'} and ORCHESTRATORS.json ({len(flat)} runs)")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "results" / "orchestrators"))
    ap.add_argument("--check", action="store_true", help="exit 1 when the page is not what the record gives")
    a = ap.parse_args(argv)
    out = Path(a.out)
    data = json.loads((out / "ORCHESTRATORS.json").read_text())
    page = render(data["readings"], data["meta"])
    if a.check:
        ok = (out / "ORCHESTRATORS.md").read_text() == page
        print("orchestrators page: current" if ok else "orchestrators page: out of date (python3 tools/orchestrators_report.py)")
        return 0 if ok else 1
    (out / "ORCHESTRATORS.md").write_text(page)
    print(f"wrote {out / 'ORCHESTRATORS.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
