#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The stacked box's three-run table: the seven organisms with a card inside (tools/run_hil.py), run three times on rented
cards, A, B and C, read by the one key (tools/readings.py three_run_reading). A run that reached its deadline part-finished
is read as far as it got: every size whose repetitions are complete in all three runs is judged; a size with fewer
repetitions than planned in any run is shown with its count and judged only where every run has two or more; a size with
one repetition in a run is shown, never judged.

Each run's own contrasts come from the runner itself (run_hil.contrast on each repetition's omni and native arm.json): the
stacks' modelled plants (class S), the card's own meter (class P) and both together. For each run the three-run key takes
the mean change over its repetitions in percent of native and the 95% interval of that mean (Student's t on the run's own
repetitions); the words are the key's.

  python3 tools/hil_abc.py "TITLE" RUN_A RUN_B RUN_C --ids A,B,C --commits SHA_A,SHA_B,SHA_C --out results/gpu/V21_<NAME>.md
  each RUN is the run's own folder (results/hil/run-<stamp>/), holding size-<n>/rep-<k>/<organism>/{omni,native}/arm.json"""
from __future__ import annotations

import argparse
import json
import math
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import run_hil  # noqa: E402
from tools.legal import stamp  # noqa: E402
from tools.readings import HIGHER, LOWER, OWN_RUNS, SPENT, WORK_PER, by_word, run_word, three_run_reading  # noqa: E402
from omnicompass.student_t import T95  # noqa: E402

PARTS = (("sim", "the stacks (our own models, class S)"), ("card", "the card (its own meter, class P)"), ("all", "both together"))
MEASURES = (("primary", "work per energy", WORK_PER), ("work", "work", HIGHER), ("energy", "energy", SPENT),
            ("viol_pp", "time over the line (percentage points)", LOWER), ("p95", "the card's 95th percentile", LOWER))


def contrasts(run_dir):
    """{(size, organism): [per-repetition contrast dicts]} from the run's own arm.json files, as run_hil.rescore reads them."""
    root = Path(run_dir)
    res = {}
    for f in sorted(root.rglob("arm.json")):
        r = json.loads(f.read_text())
        size = next((int(p.name[5:]) for p in f.parents if p.name.startswith("size-")), 1)
        rep = next((p.name for p in f.parents if p.name.startswith("rep-")), "rep-1")
        res.setdefault((size, r["organism"]), {}).setdefault(rep, {})[r["arm"]] = r
    out = {}
    for key, reps in res.items():
        per = [run_hil.contrast(a["omni"], a["native"]) for _, a in sorted(reps.items()) if "omni" in a and "native" in a]
        if per:
            out[key] = per
    return out


def run_pair(xs, measure):
    """One run's paired result for the key: the mean change (a fraction of native) and its 95% interval over the repetitions."""
    vals = [x[measure] / (100.0 if measure == "viol_pp" else 1.0) for x in xs]
    n = len(vals); m = sum(vals) / n
    if n < 2:
        return {"native": 1.0, "diff": m, "ci95": None, "n": n}
    sd = math.sqrt(sum((v - m) ** 2 for v in vals) / (n - 1)); h = T95.get(n - 1, 2.0) * sd / math.sqrt(n)
    return {"native": 1.0, "diff": m, "ci95": [m - h, m + h], "n": n}


def engine_of(commit):
    r = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", commit], capture_output=True, text=True)
    return (r.stdout.strip().splitlines() or ["unknown"])[0]


def table(title, dirs, ids, commits):
    runs = [contrasts(d) for d in dirs]
    engines = [engine_of(c) for c in commits]
    if len({e.split(" (")[0] for e in engines}) != 1:
        raise SystemExit(f"the three runs ran different engines: {engines}")
    keys = sorted(set().union(*[set(r) for r in runs]))
    lines = [f"# {title}", "",
             f"Three runs on rented cards (A, B and C), engine {engines[0]}; runs " + ", ".join(f"{L} {i} (`{c[:12]}`)" for L, i, c in zip("ABC", ids, commits)) +
             " (their files on the branch `raw`, `run-<id>/`). Each run planned 10 paired repetitions at 1 copy, 10 at 10 and 10 at 100, and "
             "reached its rented hours' deadline part-finished: the repetitions each run finished are counted beside each row. A size "
             "is judged by the one key where every run finished two or more repetitions of it; with one repetition a run it is shown, not judged.",
             "", "| Copies | Organism | Part | Repetitions (A, B, C) | Measure | Three runs | A | B | C |",
             "|---:|---|---|---|---|---|---|---|---|"]
    record = {"title": title, "runs": list(ids), "commits": list(commits), "engine": engines[0], "rows": []}
    for size, name in keys:
        reps = [r.get((size, name), []) for r in runs]
        counts = [len(x) for x in reps]
        for part, part_name in PARTS:
            for measure, m_name, aim in MEASURES:
                if measure == "p95" and part != "card":
                    continue                                   # the card's own response time: one row, under the card
                rs = [run_pair([x[part] for x in xs], measure) if xs else None for xs in reps]
                if any(r is None for r in rs):
                    reading = "no value"
                elif any(r["ci95"] is None for r in rs):
                    reading = "one repetition in a run: shown, not judged"
                else:
                    reading = three_run_reading(rs, aim)
                cells = []
                for r in rs:
                    if r is None:
                        cells.append("—"); continue
                    w = run_word(r, aim) if r["ci95"] is not None else None
                    if measure == "viol_pp":
                        cells.append(f"{(w + ', ') if w else ''}{100 * r['diff']:+.2f} pp")
                    else:
                        cells.append(f"{(w + ', ') if w else ''}{by_word(100 * r['diff'], w, digits=2)}")
                organism = run_hil.NAMES.get(name, name)
                lines.append(f"| {size} | {organism} | {part_name} | {', '.join(map(str, counts))} | {m_name} | {reading} | " + " | ".join(cells) + " |")
                record["rows"].append({"copies": size, "organism": name, "part": part, "measure": measure, "repetitions": counts,
                                       "reading": reading.replace("**", ""), "runs": rs})
    lines += ["", OWN_RUNS, ""]
    return "\n".join(lines), record


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("title"); ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("c")
    ap.add_argument("--ids", required=True); ap.add_argument("--commits", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    text, record = table(args.title, [args.a, args.b, args.c], args.ids.split(","), args.commits.split(","))
    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(stamp(text.split("\n"))) + "\n")
    out.with_suffix(".json").write_text(json.dumps(record, indent=1) + "\n")
    print(f"{out} and its record: {len(record['rows'])} rows, engine {record['engine']}")


if __name__ == "__main__":
    main()
