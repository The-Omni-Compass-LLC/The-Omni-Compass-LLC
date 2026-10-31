# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The A/B/C table of the orchestrator's showing (.github/workflows/orchestrator.yml, tools/orchestrator_show.py): its arms run
side by side in each of three GitHub runs, A, B and C, from one commit, and each run's summary.json carries every pair's paired
change a step with its 95% interval. Each pair and gauge is read by the one key (tools/readings.py): a change of 0.5% or more is
a GAIN, a LOSS or power given by the gauge's aim, "in all three of our runs" when every run moved the same way clear of the noise,
"by the mean of our three runs" otherwise, with the count beyond the noise; STEADY under 0.5%. Every pair the runs carry is shown;
the README and the live engine page read the pair Omni on native against native from it (tools/headline.py). Until 27 October
2026 the omni-v18 record was written by hand from its runs; this tool rebuilds it from them, byte for byte.
Usage: python tools/three_arms_abc.py A_DIR B_DIR C_DIR --out results/orchestrator/V<n>_THREE_ARMS_ABC.md
  each DIR is an archived run (results/live/raw/run-<id>/) holding orchestrator-<run>-<room rule>-<id>/summary.json"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools.legal import stamp as _legal_stamp      # noqa: E402  (the legal notice every generated report carries)
from tools import readings as K                     # noqa: E402  (the one key)
from tools.repo import NAME as REPO_NAME            # noqa: E402  (the repository's name, written once)

GAUGES = {"requests": ("Work (requests a step)", K.HIGHER), "p95_ms": ("The 95th percentile (ms)", K.LOWER),
          "machines": ("Machines", K.SPENT), "units": ("Units", K.SPENT)}
ARMS = {"yardstick": "native", "omni_native": "Omni on native", "omni": "Omni direct",
        "batch": "the batch job beside the service", "drills": "the drills"}
TOTALS = ("answered", "failed", "wrong", "p95_ms", "machine_min", "unit_min")
FORMS = {(18, 25.0): "the full form: 18 steps of 25 s, clients 1 2 3 2 3 4 ...", (6, 15.0): "the quick form: six steps of 15 s"}


def showing(run_dir: Path):
    """(letter, room rule, run id, summary, the Omni arm's meta) of one archived run."""
    found = sorted(run_dir.glob("orchestrator-*-*-*/summary.json"))
    if len(found) != 1:
        raise SystemExit(f"{run_dir}: {len(found)} orchestrator-<run>-<room rule>-<id>/summary.json, not one")
    letter, room, rid = re.match(r"orchestrator-([^-]+)-([^-]+)-(\d+)$", found[0].parent.name).groups()
    meta_p = found[0].parent / "omni" / "meta.json"
    meta = json.loads(meta_p.read_text(encoding="utf-8")) if meta_p.exists() else {}
    return letter, room, rid, json.loads(found[0].read_text(encoding="utf-8")), meta


def commit_and_engine(run_id: str):
    """The run's commit (GitHub's own record of it) and the engine the version tool reads at that commit."""
    try:
        sha = subprocess.run(["gh", "api", f"repos/{REPO_NAME}/actions/runs/{run_id}", "--jq", ".head_sha"],
                             capture_output=True, text=True, timeout=60).stdout.strip()
        if not re.fullmatch(r"[0-9a-f]{40}", sha):
            return "unknown", "unknown"
        out = subprocess.run([sys.executable, str(ROOT / "tools" / "omni_version.py"), "--commit", sha], cwd=ROOT,
                             capture_output=True, text=True, timeout=300).stdout.strip().splitlines()
        return sha, (out[0] if out else "unknown")
    except (OSError, subprocess.SubprocessError):
        return "unknown", "unknown"


def said(word: str, rel: float) -> str:
    """One run's cell: its word, then its direction in words."""
    if rel == 0:
        return f"{word}, unchanged"
    return f"{word}, {'up' if rel > 0 else 'down'} {100 * abs(rel):.1f}%"


def build(dirs):
    runs = [showing(Path(d)) for d in dirs]
    letters = [r[0] for r in runs]
    rooms = {r[1] for r in runs}
    if len(rooms) != 1:
        raise SystemExit(f"the three runs ran different room rules: {sorted(rooms)}")
    shas = {letter: commit_and_engine(rid) for letter, _, rid, _, _ in runs}
    commits = {s for s, _ in shas.values()}
    if len(commits) != 1:
        raise SystemExit(f"the three runs are not from one commit: {sorted(commits)}")
    commit, engine = next(iter(shas.values()))
    metas = [m for *_, m in runs if m]
    form = FORMS.get((len(metas[0].get("steps", [])), float(metas[0].get("step_s", 0)))) if metas else None
    what = (f"Omni direct's three arms, three runs on GitHub's own machines (A, B and C from one commit), "
            f"{form or 'the steps of its summary'}, the {next(iter(rooms))} room rule")
    pairs = []
    for key in runs[0][3]["readings"]:
        pair, gauge = key.rsplit(": ", 1)
        if gauge in GAUGES and pair not in pairs:
            pairs.append(pair)
    rows = []
    for pair in pairs:
        for gauge, (label, aim_) in GAUGES.items():
            rs = [r[3]["readings"].get(f"{pair}: {gauge}") for r in runs]
            if any(x is None for x in rs):
                continue
            paired = [{"native": 1.0, "diff": float(x["rel"]), "ci95": [float(x["lo"]), float(x["hi"])]} for x in rs]
            rows.append({"pair": pair, "gauge": gauge, "label": label,
                         "reading": K.three_run_reading(paired, aim_).replace("**", ""),
                         "runs": {letter: {"word": K.run_word(p, aim_), "rel": round(float(x["rel"]), 4),
                                           "lo": round(float(x["lo"]), 3), "hi": round(float(x["hi"]), 3)}
                                  for letter, p, x in zip(letters, paired, rs)}})
    totals = {letter: {arm: {k: s[arm][k] for k in TOTALS if k in s[arm]} for arm in ARMS if arm in s}
              for letter, (_, _, _, sm, _) in zip(letters, runs) for s in [sm["summary"]]}
    return {"what": what, "class": "L", "commit": commit, "engine": engine,
            "runs": {letter: rid for letter, _, rid, _, _ in runs}, "rows": rows, "totals": totals}


def markdown(rec) -> list:
    L = ["# Omni direct's three arms: three runs on GitHub's machines", "",
         f"{rec['what']}. Commit `{rec['commit'][:12]}`, engine {rec['engine']}; runs "
         + ", ".join(f"{k} {v}" for k, v in rec["runs"].items()) + " (their files on the branch `raw`, `run-<id>/`). "
         "Native is Kubernetes' published autoscaling rule on the muscles, written by us; Omni on native is Omni-Compass on top "
         "of that rule; Omni direct is Omni-Compass alone on the muscles, no Kubernetes. Each run reads every pair by the one key, "
         "paired by step; the three runs are combined by the one rule (tools/readings.py, the founder's order of 24 October 2026): "
         "a change of 0.5% or more, the mean of the three runs, reads GAIN, LOSS or power given by the gauge's aim, in all three "
         "of our runs where every run moved the same way clear of zero, otherwise by the mean of our three runs with the count of "
         "runs beyond the noise; STEADY under 0.5%; the runs disagree when runs moved 0.5% or more in opposite directions. Each "
         "run's own word stands beside its number by the same floor.", "",
         "| Pair | Gauge | Three runs | " + " | ".join(rec["runs"]) + " |", "|---|---|---|" + "---|" * len(rec["runs"])]
    for r in rec["rows"]:
        L.append(f"| {r['pair']} | {r['label']} | **{r['reading']}** | "
                 + " | ".join(said(v["word"], v["rel"]) for v in r["runs"].values()) + " |")
    L += ["", "Each arm's totals in each run (requests answered, failed, wrong, the 95th percentile in ms, machine-minutes, unit-minutes):", "",
          "| Run | Arm | Answered | Failed | Wrong | 95th percentile (ms) | Machine-minutes | Unit-minutes |",
          "|---|---|---:|---:|---:|---:|---:|---:|"]
    for letter, arms in rec["totals"].items():
        for arm, t in arms.items():
            L.append(f"| {letter} | {ARMS[arm]} | {t['answered']:,} | {t['failed']:,} | {t['wrong']:,} | {t['p95_ms']:.1f} | "
                     f"{t['machine_min']:.1f} | {t['unit_min']:.1f} |")
    return L + ["", K.OWN_RUNS.split(" Preregistered")[0]]   # the showing was not preregistered: the line says whose runs these are


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("dirs", nargs=3, help="the archived runs A, B and C")
    ap.add_argument("--out", required=True, help="the table (.md); its record is written beside it (.json)")
    a = ap.parse_args(argv)
    rec = build(a.dirs)
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".json").write_text(json.dumps(rec, indent=1) + "\n", encoding="utf-8")
    out.write_text("\n".join(_legal_stamp(markdown(rec))) + "\n", encoding="utf-8")
    print(f"{out} and its record: {len(rec['rows'])} rows, engine {rec['engine']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
