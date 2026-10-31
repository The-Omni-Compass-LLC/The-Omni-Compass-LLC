#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The three-run reading of Omni direct's three arms, from the summaries of runs A, B and C (tools/orchestrator_show.py).

  python3 tools/orchestrator_abc.py A=<summary.json> B=<summary.json> C=<summary.json> --runs A=<id> B=<id> C=<id> \\
      --commit <sha> --out results/orchestrator/<NAME>

Each run's own reading of a pair and a gauge (the mean of the step-by-step differences and its 95% interval on Student's t,
as the showing wrote it) is combined by the repository's one rule (tools/readings.py, the founder's order of 24 October
2026): a change of 0.5% or more, the mean of the three runs, reads GAIN, LOSS or power given by the gauge's aim (in all three when every run's interval is clear of zero on the same side, otherwise by the mean of the three with the count beyond the noise); under 0.5% it reads STEADY, under the floor; runs that moved 0.5% or more in opposite ways disagree. Writes <NAME>.md and <NAME>.json.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

GAUGES = (("requests", "Work (requests a step)", "work"), ("p95_ms", "The 95th percentile (ms)", "wait"),
          ("machines", "Machines", "resource"), ("units", "Units", "resource"))
PAIRS = ("Omni on native against native", "Omni direct against native", "Omni direct against Omni on native")
from tools.legal import NOTICE, TOP  # noqa: E402  the notice is written once, in tools/legal.py


AIMS = {"work": "higher", "wait": "lower", "resource": "spent"}    # the key's aims (tools/readings.py)


def combine(runs: list[dict], aim: str) -> str:
    """The three runs read by the rule that stands (tools/readings.py three_run_reading, the founder's order of 24 October 2026:
    a change of 0.5% or more, the mean of the three runs, is a GAIN, a LOSS or power given by the gauge's aim; STEADY under it)."""
    from tools.readings import three_run_reading
    rs = [{"native": 1.0, "diff": r["rel"], "ci95": [r["lo"], r["hi"]]} for r in runs]
    return three_run_reading(rs, AIMS[aim]).replace("**", "")


def run_word_of(rel: float, aim: str) -> str:
    """One run's own word: its change of 0.5% or more read by the gauge's aim, STEADY under it."""
    from tools.readings import run_word
    return run_word({"native": 1.0, "diff": rel}, AIMS[aim])


def reread(path: Path) -> int:
    """The table read again from its own JSON by the rule that stands; returns how many readings changed."""
    rec = json.loads(path.read_text())
    aims, n = {g: a for g, _, a in GAUGES}, 0
    for r in rec["rows"]:
        new = combine(list(r["runs"].values()), aims[r["gauge"]])
        n += new != r["reading"]
        r["reading"] = new
        for v in r["runs"].values():
            v["word"] = run_word_of(v["rel"], aims[r["gauge"]])
    path.write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    path.with_suffix(".md").write_text(page(rec))
    return n


def words(rel: float) -> str:
    return "unchanged" if not rel else f"{'up' if rel > 0 else 'down'} {abs(100 * rel):.1f}%"


def build(summaries: dict, run_ids: dict, commit: str) -> dict:
    rows = []
    for pair in PAIRS:
        for g, label, aim in GAUGES:
            per = {L: summaries[L]["readings"].get(f"{pair}: {g}") for L in "ABC"}
            if any(v is None for v in per.values()):
                continue
            rows.append({"pair": pair, "gauge": g, "label": label, "reading": combine(list(per.values()), aim),
                         "runs": {L: {"word": v["word"], "rel": round(v["rel"], 4), "lo": round(v["lo"], 3), "hi": round(v["hi"], 3)}
                                  for L, v in per.items()}})
    totals = {L: {a: {k: s["summary"][a][k] for k in ("answered", "failed", "wrong", "p95_ms", "machine_min", "unit_min")}
                  for a in ("yardstick", "omni_native", "omni", "batch", "drills") if a in s["summary"]}
              for L, s in summaries.items()}
    import subprocess
    engine = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", commit], cwd=ROOT,
                            capture_output=True, text=True).stdout.strip()
    return {"what": "Omni direct's three arms, three runs on GitHub's own machines (A, B and C from one commit), the full form: "
                    "18 steps of 25 s, clients 1 2 3 2 3 4 ..., the busy room rule", "class": "L", "commit": commit,
            "engine": engine, "runs": run_ids, "rows": rows, "totals": totals}


def page(rec: dict) -> str:
    out = [f"# Omni direct's three arms: three runs on GitHub's machines\n", f"> {TOP}\n",
           f"{rec['what']}. Commit `{rec['commit'][:12]}`, engine {rec['engine']}; runs A {rec['runs']['A']}, B {rec['runs']['B']}, "
           f"C {rec['runs']['C']} (their files on the branch `raw`, `run-<id>/`). Native is Kubernetes' published autoscaling rule on "
           "the muscles, written by us; Omni on native is Omni-Compass on top of that rule; Omni direct is Omni-Compass alone on the "
           "muscles, no Kubernetes. Each run reads every pair by the one key, paired by step; the three runs are combined by the one "
           "rule (tools/readings.py, the founder's order of 24 October 2026): a change of 0.5% or more, the mean of the three runs, "
           "reads GAIN, LOSS or power given by the gauge's aim, in all three of our runs where every run moved the same way clear of "
           "zero, otherwise by the mean of our three runs with the count of runs beyond the noise; STEADY under 0.5%; the runs disagree "
           "when runs moved 0.5% or more in opposite directions. Each run's own word stands beside its number by the same floor.\n",
           "| Pair | Gauge | Three runs | A | B | C |", "|---|---|---|---|---|---|"]
    for r in rec["rows"]:
        cells = [f"{v['word']}, {words(v['rel'])}" for v in r["runs"].values()]
        out.append(f"| {r['pair']} | {r['label']} | **{r['reading']}** | " + " | ".join(cells) + " |")
    out += ["", "Each arm's totals in each run (requests answered, failed, wrong, the 95th percentile in ms, machine-minutes, "
            "unit-minutes):", "", "| Run | Arm | Answered | Failed | Wrong | 95th percentile (ms) | Machine-minutes | Unit-minutes |",
            "|---|---|---:|---:|---:|---:|---:|---:|"]
    names = {"yardstick": "native", "omni_native": "Omni on native", "omni": "Omni direct", "batch": "the batch job beside the service",
             "drills": "the drills"}
    for L, arms in rec["totals"].items():
        for a, t in arms.items():
            out.append(f"| {L} | {names[a]} | {t['answered']:,} | {t['failed']} | {t['wrong']} | {t['p95_ms']:.1f} | "
                       f"{t['machine_min']:.1f} | {t['unit_min']:.1f} |")
    out += ["", "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
            "---", "", f"*{NOTICE}*", ""]
    return "\n".join(out)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("summaries", nargs=3, help="A=<summary.json> B=<summary.json> C=<summary.json>")
    ap.add_argument("--runs", nargs=3, required=True, help="A=<run id> B=<run id> C=<run id>")
    ap.add_argument("--commit", required=True)
    ap.add_argument("--out", required=True, help="the path without its suffix")
    a = ap.parse_args(argv)
    summaries = {k: json.loads(Path(v).read_text()) for k, v in (s.split("=", 1) for s in a.summaries)}
    run_ids = dict(s.split("=", 1) for s in a.runs)
    rec = build(summaries, run_ids, a.commit)
    Path(a.out + ".json").write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    Path(a.out + ".md").write_text(page(rec))
    for r in rec["rows"]:
        print(f"{r['pair']:36s} {r['label']:26s} {r['reading']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
