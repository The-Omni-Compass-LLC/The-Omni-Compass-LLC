# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The capacity test's A/B/C three-run table (docs/CAPACITY_PREREGISTRATION.md): the same test run three times as separate
GitHub runs on the same engine, each run's own table built by tools/capacity_report.py (CAPACITY.json in each archived run,
results/live/raw/capacity-run-<id>/). Each cap level gets two judged rows, completed work and capacity, each with the three
readings every three-run table uses (tools/confirm_abc.py's rule: GAIN or LOSS in all three of our runs, STEADY with no
difference beyond the noise, or the runs disagree; both rows are work done, so a rise is GAIN). Every row is shown, LOSS
included.

  python3 tools/capacity_abc.py A_DIR B_DIR C_DIR --out results/live/V5_CAPACITY.md
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.confirm_abc import CAPACITY, cell, engine            # noqa: E402
from tools.legal import stamp                                   # noqa: E402
from tools.readings import HIGHER, OWN_RUNS, STACK_RULE, receipt_key, run_word, three_run_reading  # noqa: E402

WORK = "completed work (requests answered within the line over the window)"


def load(d):
    """One run: its GitHub run id (from the folder's name), its label and its rows by cap level."""
    d = Path(d)
    run = d.name.rsplit("-", 1)[-1]
    rows = {r["cap_m"]: r for r in json.loads((d / "CAPACITY.json").read_text())["rows"]}
    meta = dict(line.split("=", 1) for line in (d / "RUN.txt").read_text().splitlines() if "=" in line) if (d / "RUN.txt").exists() else {}
    return run, meta, rows


def pair(r, key):
    """A cap row's paired difference in the shape confirm_abc reads (native, omni, diff, ci95)."""
    if key == "work":
        return {"native": r["work_native"], "omni": r["work_omni"], "diff": r["work_diff"], "ci95": [r["work_lo"], r["work_hi"]]}
    return {"native": r["capacity_native"], "omni": r["capacity_omni"], "diff": r["capacity_diff"],
            "ci95": [r["capacity_lo"], r["capacity_hi"]]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c")
    ap.add_argument("--out", required=True)
    a = ap.parse_args(argv)
    runs = [load(d) for d in (a.a, a.b, a.c)]
    L = ["# The capacity test, native and Omni-Compass on top at the same resource cap: the A/B/C three-run table", "",
         *receipt_key(), "",
         "Three separate GitHub runs of the same preregistered test on the same engine: A is the result, B and C are the "
         "replications. The cap is a quota on the served app's CPU, the same in both arms and enforced by the cluster; the "
         "load rises step by step past what the cap can serve. Each cell is omni against native at one cap, the paired change "
         "with its 95% interval: native's value → Omni-Compass's, the raw change with its true sign, then the run's own word. "
         "Completed work and capacity are work done, so more is GAIN and less is LOSS. " + STACK_RULE + " Every row is shown, LOSS "
         "included. Evidence class **L** (the real thing: a real Kubernetes cluster, real requests, every answer counted).", "",
         OWN_RUNS, "", "| Run | GitHub run | Label | Commit | Engine | Pairs per cap |", "|---|---|---|---|---|---:|"]
    engines = []
    for tag, (run, meta, rows) in zip("ABC", runs):
        sha, ver = engine(run)
        engines.append(ver.split(" ")[0])
        pairs = sorted({r["pairs"] for r in rows.values()})
        L.append(f"| {tag} | {run} | {meta.get('label', '?')} | `{sha}` | {ver} | {', '.join(map(str, pairs))} |")
    if any(meta.get("label") != tag for tag, (_, meta, _) in zip("ABC", runs)):
        L += ["", "The label column is the run's own record of the label it was started with. The conductor started these "
              "runs in order and, before 19 October, passed no label, so a run it started reads the workflow's default, A; "
              "the Run column is the table's place for each run, in the order started."]
    if len(set(engines)) == 1:                       # the title names the engine the three runs were on
        L[0] += " (" + engines[0].replace("omni-v", "Omni v") + ")"
    if len(set(engines)) > 1 or len({r for r, _, _ in runs}) < 3:
        L[2:2] = ["**Not one engine's three separate runs: " + ", ".join(engines) + ".** The readings below compare runs on "
                  "different engines.", ""]
    caps = sorted(set.intersection(*(set(rows) for _, _, rows in runs)))
    L += ["", "| Cap (cores) | Measure | A | B | C | Reading |", "|---:|---|---|---|---|---|"]
    tally, data = {}, {}
    for cap in caps:
        for key, label in (("work", WORK), ("capacity", CAPACITY)):
            rs = [pair(rows[cap], key) for _, _, rows in runs]
            v = three_run_reading(rs, HIGHER)      # both rows are work done: the aim, higher
            tally[v] = tally.get(v, 0) + 1
            data[f"{cap}:{key}"] = {"reading": v.strip("*"), "aim": HIGHER, "runs": rs}
            cells = [cell(r, run_word(r, HIGHER)) for r in rs]
            L.append(f"| {cap / 1000:g} | {label} | {cells[0]} | {cells[1]} | {cells[2]} | {v} |")
    L += ["", "Readings: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())) + ".", "",
          "How to read it: where the cap holds native back, a higher count for Omni-Compass on top at the same cap is more work "
          "from the same capacity, a GAIN; a lower count is a LOSS; a mean change under 0.5% reads STEADY, under the floor. Each run's own table, with its audit lines and what each step up in the cap gives each "
          "arm: `CAPACITY.md` in its archived folder."]
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(stamp(L)) + "\n", encoding="utf-8")
    out.with_suffix(".json").write_text(json.dumps({"runs": [r for r, _, _ in runs], "engines": engines, "rows": data},
                                                   indent=1) + "\n")
    print(f"{out}: " + ", ".join(f"{n} {v.strip('*')}" for v, n in sorted(tally.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
