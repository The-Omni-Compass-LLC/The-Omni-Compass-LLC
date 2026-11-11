#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""What the governor wrote and what it cost, on every batch-stream rig, engine against engine, read from its own audit.

For each rig with Omni-Compass on top (the batch stream alone and through each scheduler and orchestrator), and for each engine
named, it reads the governor's audit (audit.jsonl) of every repetition of the three runs its table was written from (the recipe
in results/live/RECIPES.json; the files from the branch raw, through git, nothing checked out) and counts, an arm a repetition:

  web target writes   writes of the web service's autoscaler target (the flips of docs/LOSS_CAUSES_2026-11-06.md)
  limit raises        writes of a web pod's processor limit above the operator's (the conveyance)
  limit hand-backs    writes of a web pod's processor limit back to the operator's
  pool writes         writes of the node pool's size (parks and wakes)
  own processor       the governor's own processor over the window, in cores (its audit's overhead record)

  python3 tools/governor_writes.py [--engines 25,26] [--ref refs/remotes/origin/raw] [--json OUT] [--md OUT]

It reads; it judges nothing. Each count is the mean over the repetitions of the three runs (30 a rig), with its range.
"""
from __future__ import annotations

import argparse
import json
import statistics
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
RECIPES = ROOT / "results" / "live" / "RECIPES.json"
# the rigs and the table whose recipe names their three runs; the arms Omni-Compass decides in
RIGS = [("the batch stream alone", "BATCH", ("compass",)),
        ("the default scheduler", "VANILLA", ("compass",)), ("the bin-packing profile", "BINPACK", ("compass",)),
        ("KAI", "KAI", ("compass",)), ("Kueue", "KUEUE", ("compass",)), ("Volcano", "VOLCANO", ("compass",)),
        ("Koordinator", "KOORDINATOR", ("compass",)), ("Koordinator, cgroup root", "KOORDINATOR_CGROUP", ("compass",)),
        ("KAI, four ways", "KAI_4W_TOP", ("compass", "compassbare")),
        ("Kueue, four ways", "KUEUE_4W_TOP", ("compass", "compassbare")),
        ("Volcano, four ways", "VOLCANO_4W_TOP", ("compass", "compassbare")),
        ("bin-packing, four ways", "BINPACK_4W_TOP", ("compass", "compassbare")),
        ("KubeRay, four ways", "KUBERAY_4W_TOP", ("compass", "compassbare")),
        ("Crane, four ways", "CRANE_4W_TOP", ("compass", "compassbare")),
        ("Gödel, four ways", "GODEL_4W_TOP", ("compass", "compassbare")),
        ("Open Cluster Management, four ways", "OCM_4W_TOP", ("compass", "compassbare"))]
GAUGES = ("web target writes", "limit raises", "limit hand-backs", "pool writes", "own processor (cores)")


def show(ref, path):
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"{ref}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def read_audit(text):
    """(target, raises, backs, pool, cores) from one arm's audit."""
    target = raises = backs = pool = 0
    cores = None
    for line in text.splitlines():
        try:
            d = json.loads(line)
        except ValueError:
            continue
        if "overhead" in d and isinstance(d["overhead"], dict):
            cores = d["overhead"].get("cores_mean")
        w = d.get("write")
        if not w:
            continue
        s = " ".join(map(str, w)) if isinstance(w, list) else str(w)
        if "kind_nodepool" in s or "nodepool" in s:
            pool += 1
        elif "hpa" in s and "patch" in s:
            target += 1
        elif "patch" in s and "-p" in s and ("pod" in s or "deployment" in s):
            try:
                parts = w if isinstance(w, list) else s.split()
                v = json.loads(parts[parts.index("-p") + 1])[0]["value"]
            except (ValueError, KeyError, IndexError, TypeError):
                continue
            if v == "500m":
                backs += 1
            else:
                raises += 1
    return target, raises, backs, pool, cores


def rig(ref, runs, arms):
    """Every repetition's counts, an arm a repetition: {gauge: [values]}."""
    out = {g: [] for g in GAUGES}
    for run in runs:
        for rep in range(1, 11):
            for arm in arms:
                text = show(ref, f"{run}/paired-{rep}/bench-{arm}-{rep}/audit.jsonl")
                if text is None:
                    continue
                vals = read_audit(text)
                for g, v in zip(GAUGES, vals):
                    if v is not None:
                        out[g].append(v)
    return out


def summary(vals):
    if not vals:
        return None
    return {"mean": statistics.fmean(vals), "min": min(vals), "max": max(vals), "n": len(vals)}


def build(engines, ref):
    recipes = json.loads(RECIPES.read_text())
    data = []
    for label, table, arms in RIGS:
        row = {"rig": label, "table": table, "engines": {}}
        for e in engines:
            r = recipes.get(f"V{e}_{table}")
            if not r:
                continue
            counts = rig(ref, r["runs"], arms)
            row["engines"][str(e)] = {"runs": r["runs"], **{g: summary(v) for g, v in counts.items()}}
        data.append(row)
    return data


def fmt(s, cores=False):
    if not s:
        return "not run"
    if cores:
        return f"{s['mean']:.3f} ({s['min']:.3f} to {s['max']:.3f})"
    return f"{s['mean']:.1f} ({s['min']:g} to {s['max']:g})"


def render(data, engines):
    from tools.legal import stamp
    from tools.company_attribution import normalize
    a, b = engines[0], engines[-1]
    L = [f"# What the governor wrote and what it cost on every batch-stream rig: omni-v{a} against omni-v{b}", "",
         "Read from the governor's own audit (`audit.jsonl`) in every repetition of the three runs each rig's table was written "
         "from (`results/live/RECIPES.json`), on the branch `raw`, by `tools/governor_writes.py`. Each cell is the mean an arm a "
         "repetition (Omni-Compass's arms only: on top of the scheduler, and on the organism alone in the four ways), with its "
         "range. It reads what the governor did; it judges nothing: the readings stand in each rig's own three-run table.", ""]
    for g in GAUGES:
        cores = g.startswith("own processor")
        L += [f"## {g[0].upper() + g[1:]}", "", f"| Rig | omni-v{a} | omni-v{b} |", "|---|---:|---:|"]
        for row in data:
            ea, eb = row["engines"].get(str(a), {}), row["engines"].get(str(b), {})
            L.append(f"| {row['rig']} | {fmt(ea.get(g), cores)} | {fmt(eb.get(g), cores)} |")
        L.append("")
    L += ["The runs each rig was read from are its tables' own (`results/live/V<n>_<TABLE>.md`). Run and scored by Dubra "
          "Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved these results."]
    return normalize("\n".join(stamp(L)) + "\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--engines", default="25,26")
    ap.add_argument("--ref", default="refs/remotes/origin/raw")
    ap.add_argument("--json", default=str(ROOT / "results" / "GOVERNOR_WRITES.json"))
    ap.add_argument("--md", default=str(ROOT / "results" / "GOVERNOR_WRITES.md"))
    a = ap.parse_args(argv)
    engines = [int(x) for x in a.engines.split(",")]
    data = build(engines, a.ref)
    Path(a.json).write_text(json.dumps({"engines": engines, "rigs": data}, indent=1) + "\n")
    Path(a.md).write_text(render(data, engines))
    print(f"{a.md} written ({len(data)} rigs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
