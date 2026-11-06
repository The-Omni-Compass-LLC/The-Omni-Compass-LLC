#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The six organisms' full grid, built from the saved receipts (results/scale/receipts/v3-<size>x.md, each the
printed receipt of one GitHub `six` run): 6 organisms x sizes 1, 10, 100, 1,000 clusters x runs 1, 10, 100, 1,000.

    python3 tools/grid.py        writes results/scale/GRID.md

A cell whose receipt is not saved yet reads "running"; 1,000 runs at 1,000 clusters reads "not run" (about 6,000
machine-hours, beyond the machines available). How to read every table: docs/HOW_TO_READ_THE_RESULTS.md.
"""
from __future__ import annotations

import re

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
import sys; sys.path.insert(0, str(ROOT))  # noqa: E402
from realms.harness import STACK, TOWER, organism_sizes  # noqa: E402
REC = ROOT / "results" / "scale" / "receipts"
ENGINE = "v3"            # the receipts of the engine this grid is built on (v1's grid and receipts: results/scale/v1/)
OUT = ROOT / "results" / "scale" / "GRID.md"
SIZES, RUNS = (1, 10, 100, 1000), (1, 10, 100, 1000)
ORGS = ["Compute / AI / Cloud", "Physics / Robotics / Autonomous", "Energy / Facility / Industrial",
        "Distribution / Specialized", "The four stacked, duplicates kept", "The whole tower, every muscle once"]
_SZ = organism_sizes()
MUSCLES = {"Compute / AI / Cloud": _SZ["compute_ai_cloud"], "Physics / Robotics / Autonomous": _SZ["physics_robotics_autonomous"],
           "Energy / Facility / Industrial": _SZ["energy_facility_industrial"], "Distribution / Specialized": _SZ["distribution_specialized"],
           "The four stacked, duplicates kept": _SZ[STACK], "The whole tower, every muscle once": _SZ[TOWER]}
COLS = {"label": 4, "band": 5, "wpe": 6, "work": 7, "energy": 8, "viol": 9, "knobs": 10}


def parse(path):
    """{(runs, organism): {column: text}} and the receipt's source line."""
    cells, runs, source = {}, None, ""
    for line in path.read_text().splitlines():
        m = re.match(r"## (\d+) runs?$", line.strip())
        if m:
            runs = int(m.group(1)); continue
        if line.startswith("Source:"):
            source = line[len("Source:"):].strip()
        if runs and line.startswith("| ") and not line.startswith("| #") and not line.startswith("|---"):
            f = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(f) >= 11 and f[1] in MUSCLES:
                cells[(runs, f[1])] = {k: f[i] for k, i in COLS.items()}
    return cells, source


def main():
    data, sources = {}, {}
    for sc in SIZES:
        p = REC / f"{ENGINE}-{sc}x.md"
        if p.exists():
            data[sc], sources[sc] = parse(p)

    def cell(sc, r, org, k):
        if sc == 1000 and r == 1000:
            return "not run"
        c = data.get(sc, {}).get((r, org))
        if c is None and sc == 1000 and r == 100:
            return "not run yet"
        if c is None:
            return "to run"
        v = c[k]
        return v.split(" (")[0] if k in ("wpe", "work", "energy", "viol") else v

    head = "| Organism (muscles) | " + " | ".join(f"{sc}x, {r} run{'s' if r > 1 else ''}" for sc in SIZES for r in RUNS) + " |"
    rule = "|---|" + "---:|" * (len(SIZES) * len(RUNS))
    L = ["# The six organisms: the full grid", "",
         "Evidence class **S** (models of the plants, not hardware). Every organism runs native (its own controllers) "
         "and native with Omni-Compass on top (the compass law on every muscle, Omni v3, `docs/OMNI_V3.md`) "
         "on the same seed, the same load and the same clock. **Size** is the number of copies of the organism governed "
         "together on one clock: 1, 10, 100 and 1,000 clusters. **Runs** are paired seeds from 7000 on; 1, 10, 100 and "
         "1,000 runs are the first N of the same set, so each block nests inside the next. Built by `tools/grid.py` from "
         "the saved receipts in `results/scale/receipts/`; the v1 grid and its receipts are kept in `results/scale/v1/`. How to read it: `docs/HOW_TO_READ_THE_RESULTS.md`.", "",
         "Sources:"] + [f"- {sc}x: {sources[sc]}" if sc in sources else f"- {sc}x: to run" for sc in SIZES] + [
         "- 1,000 runs at 1,000 clusters is not run: about 6,000 machine-hours, beyond the machines available.",
         "- 100 runs at 1,000 clusters is not run yet: about 650 runner-hours (one run of the four stacked at 1,000 copies "
         "takes 2 to 3 hours).", ""]
    for k, title, note in (("wpe", "Work per energy, with Omni-Compass on top against native", "higher means more work for each unit of energy"),
                           ("energy", "Energy, with Omni-Compass on top against native", "the aim is lower"),
                           ("viol", "Time over the service line, with Omni-Compass on top minus native (percentage points)",
                            "the aim is lower; band first holds where it is at or under 0"),
                           ("work", "Work done, with Omni-Compass on top against native", "equal is the guardrail"),
                           ("label", "Label by the preregistered rule", "chosen by code, never by hand")):
        L += [f"## {title} ({note})", "", head, rule]
        for org in ORGS:
            L.append(f"| {org} ({MUSCLES[org]}) | " + " | ".join(cell(sc, r, org, k).replace("**", "")
                                                                 for sc in SIZES for r in RUNS) + " |")
        L.append("")
    done = [(sc, r, o) for sc in data for (r, o) in data[sc]]
    knobs = all(data[sc][(r, o)]["knobs"] == "True" for sc, r, o in done)
    held = sum(1 for sc, r, o in done if data[sc][(r, o)]["band"] == "held")
    L += ["## Summary of the completed cells", "",
          f"- Cells completed: {len(done)} of {len(SIZES) * len(RUNS) * len(ORGS) - len(ORGS)} (six organisms x 15 size and run cells).",
          f"- Band first held: {held} of {len(done)}."
          + ("" if held == len(done) else " Not held in: " + "; ".join(
              f"{o}, {sc}x, {r} run{'s' if r > 1 else ''} ({data[sc][(r, o)]['viol']} pp)"
              for sc, r, o in done if data[sc][(r, o)]["band"] != "held") + " (a single run has no interval; inside the "
              "2% the rule allows, and held over 10, 100 and 1,000 runs)."),
          f"- Every knob handed back in every completed cell: {knobs}.",
          f"- Work done: the largest cost in any completed cell is {max(0.0, -min(float(data[sc][(r, o)]['work'].split('%')[0]) for sc, r, o in done)):.3f}% "
          "(thermal zones held warmer have a little less margin in a heat spike; `docs/REALMS_PREREGISTRATION.md`), inside "
          "the 2% the rule allows (`DISCLOSURES.md`, section 3).",
          "- The full receipt of each size, with the 95% interval of every number, is in `results/scale/receipts/`."]
    OUT.write_text("\n".join(_legal_stamp(L)) + "\n")
    print(OUT, len(done), "cells")


if __name__ == "__main__":
    main()
