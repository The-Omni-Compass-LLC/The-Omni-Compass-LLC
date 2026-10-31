#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The card's three-run table: one GPU benchmark (scripts/gpu_paired.sh, tools/gpu_reps.py) run three times on rented
cards, A, B and C, each a separate run of the same engine and dial, read by the one key (tools/readings.py
three_run_reading): the change is the mean of the three runs' paired changes (Omni-Compass on top of native against
native) in percent of native; from 0.5% up it reads GAIN, LOSS or power given by what the gauge is for, "in all three of our
runs" where every run moved the same way clear of zero, otherwise "by the mean of our three runs" with the count of runs
beyond the noise. Each run's own word sits beside its number. Every gauge the runs share is a row; nothing is left out.
Usage: python tools/gpu_abc.py "TITLE" A_DIR B_DIR C_DIR --out results/gpu/V21_<NAME>.md
  each DIR holds GPU_REPS.json (the counted run's folder, results/gpu/run-<stamp>/), and its run id and engine are given
  with --ids and read from the engine file beside it (results/gpu/engine-<stamp>.txt)."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.gpu_reps import KEYS, LOWER as GPU_LOWER, SPENT as GPU_SPENT, PRIMARY, WALL  # noqa: E402
from tools.legal import stamp  # noqa: E402
from tools.readings import (HIGHER, LOWER, OWN_RUNS, SPENT, WORK_PER, by_word, run_word,  # noqa: E402
                            three_run_reading)


def gauge_aim(key):
    """The gauge's aim as tools/gpu_reps.py declares it."""
    return SPENT if key in GPU_SPENT else LOWER if key in GPU_LOWER else WORK_PER if key in (PRIMARY, WALL) else HIGHER


def engine_of(run_dir):
    """The engine and dial the run wrote beside its folder (scripts/gpu_rented_run.sh), or what is missing."""
    stamp_ = run_dir.name.split("run-", 1)[-1][:16]   # 20261027T102001Z, before a mode's suffix (-cap, -cap-full)
    f = run_dir.parent / f"engine-{stamp_}.txt"
    return f.read_text().strip().splitlines() if f.exists() else ["no engine file beside the run"]


def table(title, dirs, ids):
    runs = [json.loads((Path(d) / "GPU_REPS.json").read_text()) for d in dirs]
    engines = [engine_of(Path(d)) for d in dirs]
    if len({e[0] for e in engines}) != 1:
        raise SystemExit(f"the three runs ran different engines: {[e[0] for e in engines]}")
    lines = [f"# {title}", "",
             f"Three runs on rented cards (A, B and C), {runs[0]['receipt'].get('gpu_name', 'card')}, "
             f"{runs[0]['receipt'].get('reps', '?')} paired repetitions each; engine {engines[0][0]}; "
             f"{engines[0][1] if len(engines[0]) > 1 else ''}. Runs: " +
             ", ".join(f"{L} {i}" for L, i in zip("ABC", ids)) +
             " (their files on the branch `raw`, `run-<id>/`). Each run's own verdict (tools/gpu_reps.py): " +
             "; ".join(f"{L} {r['headline'].get('verdict', '?')}" for L, r in zip("ABC", runs)) + ".", "",
             "| Gauge | Three runs | A | B | C |", "|---|---|---|---|---|"]
    rows = {}
    for key in KEYS:
        rs = [r.get("paired", {}).get("omni", {}).get(key) for r in runs]
        if any(x is None or x.get("native") is None or x.get("native") != x.get("native") for x in rs):
            continue
        aim_ = gauge_aim(key)
        reading = three_run_reading(rs, aim_)
        cells = []
        for x in rs:
            w = run_word(x, aim_)
            change = 100 * x["diff"] / abs(x["native"]) if x["native"] else None
            cells.append(f"{w}, {by_word(change, w, digits=2)}" if change is not None else "—")
        rows[key] = {"reading": reading.replace("**", ""), "runs": rs}
        lines.append(f"| {key} | {reading} | " + " | ".join(cells) + " |")
    lines += ["", "Each arm's means in each run (native, then Omni-Compass on top of native):", "",
              "| Run | Gauge | Native | Omni-Compass on top of native |", "|---|---|---:|---:|"]
    for L, r in zip("ABC", runs):
        for key in (PRIMARY, "requests served", "requests not served", "energy, GPU (J)",
                    "response time, 95th percentile (ms)", "power-limit writes"):
            n, o = r.get("means", {}).get("native", {}).get(key), r.get("means", {}).get("omni", {}).get(key)
            if n is not None and o is not None:
                lines.append(f"| {L} | {key} | {n:,.2f} | {o:,.2f} |")
    lines += ["", OWN_RUNS, ""]
    return "\n".join(lines), {"title": title, "runs": list(ids), "engine": engines[0], "rows": rows}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title"); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c")
    ap.add_argument("--ids", required=True, help="the three runs' ids, A,B,C")
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    text, record = table(args.title, [args.a, args.b, args.c], args.ids.split(","))
    out = Path(args.out)
    out.write_text("\n".join(stamp(text.split("\n"))) + "\n")
    out.with_suffix(".json").write_text(json.dumps(record, indent=1, default=str) + "\n")
    print(f"{out} and its record: {len(record['rows'])} rows, engine {record['engine'][0]}")


if __name__ == "__main__":
    main()
