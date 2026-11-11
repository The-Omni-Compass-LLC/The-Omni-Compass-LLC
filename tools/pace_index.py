#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The heartbeat dial's index page (results/pace/PACE.md), written from the newest engine's pace tables, never typed.

The decision pace's real runs (docs/PACE_PREREGISTRATION.md, amendment 3) are tabled by tools/confirm_abc.py --pair, two
tables a beat: the beat against native (V<n>_PACE_<beat>) and against the factory beat (V<n>_PACE_<beat>_VS_FACTORY). This
page counts each table's readings by the one key's words, names the three runs and repeats the rows a reader looks at
first, each read from its table's JSON. Until 11 November the page was written by hand.

  python3 tools/pace_index.py            write results/pace/PACE.md from the newest engine's pace tables
  python3 tools/pace_index.py --check    exit 1 when the page differs from what its tables say (verify.py)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import stamp as legal_stamp                                 # noqa: E402
from tools.company_attribution import normalize as canonical_name            # noqa: E402
from tools.repo import URL as REPO_URL                                       # noqa: E402

PACE = ROOT / "results" / "pace"
OUT = PACE / "PACE.md"
TABLE = re.compile(r"^V(\d+)_PACE_(\d+)(_VS_FACTORY)?\.json$")
# the rows a reader looks at first: the machines, the answer and its line, the failures, the alert, the pods' start
FIRST = ("worker nodes in service, mean", "node-hours", "response time (ms), 95th percentile",
         "time over the response line (% of samples)", "failed requests (%)",
         "alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line)",
         "pod start wait, total (s)")
WORDS = (("GAIN", "GAIN"), ("LOSS", "LOSS"), ("power given", "power given"), ("STEADY", "STEADY"),
         ("the runs disagree", "runs disagree"))


def tables(engine: int | None = None):
    """{(beat, vs_factory): (path, json)} of the newest engine with pace tables (or the one named)."""
    found = {}
    for p in PACE.glob("V*_PACE_*.json"):
        m = TABLE.match(p.name)
        if m:
            found.setdefault(int(m.group(1)), {})[(int(m.group(2)), bool(m.group(3)))] = p
    if not found:
        return None, {}
    v = engine if engine is not None else max(found)
    return v, {k: (p, json.loads(p.read_text(encoding="utf-8"))) for k, p in sorted(found.get(v, {}).items())}


def counts(rows: dict) -> dict:
    out = {w: 0 for _, w in WORDS}
    for r in rows.values():
        reading = r.get("reading", "") if isinstance(r, dict) else ""
        for start, w in WORDS:
            if reading.startswith(start):
                out[w] += 1
                break
    return out


def factory_beat(md: Path):
    m = re.search(r"Omni-Compass at its default, deciding every (\d+(?:\.\d+)?) s", md.read_text(encoding="utf-8"))
    return m.group(1) if m else None


def build(engine: int | None = None) -> str:
    v, ts = tables(engine)
    if not ts:
        raise SystemExit("pace_index: no pace tables in results/pace/")
    fb = next((factory_beat(p.with_suffix(".md")) for (b, vs), (p, _) in ts.items() if vs), None)
    against = {False: "native", True: f"the factory beat ({fb} s)" if fb else "the factory beat"}
    beats = sorted({b for b, _ in ts})
    L = [f"# The heartbeat dial on real Kubernetes: every beat against native and against the factory beat (omni-v{v}, three runs)",
         "",
         "The decision pace's real runs (`docs/PACE_PREREGISTRATION.md`, amendment 3; `scripts/reruns.txt`, \"kubernetes decision "
         f"pace\"): the steady load, native and Omni-Compass on top of native at the factory beat ({fb} s on site since omni-v24) "
         f"and at {', '.join(str(b) for b in beats[:-1])} and {beats[-1]} s, every arm in every repetition, ten paired "
         "repetitions a run, three runs (A, B and C) on GitHub's machines, class L. A beat other than the factory's is a changed "
         "tune: its readings show the engine's range, never a benchmark result (the founder's order of 22 October), and every "
         "row of every table is shown, LOSS included. Each table was written by `tools/confirm_abc.py --pair` from the archived "
         "runs on the branch `raw`; each reading is the one key's (`tools/readings.py`); this page is written from the tables by "
         "`tools/pace_index.py`.",
         "",
         "| Beat | Against | GAIN | LOSS | power given | STEADY | runs disagree | Table |",
         "|---:|---|---:|---:|---:|---:|---:|---|"]
    for (b, vs), (p, d) in ts.items():
        c = counts(d.get("rows", {}))
        L.append(f"| {b} s | {against[vs]} | " + " | ".join(str(c[w]) for _, w in WORDS)
                 + f" | [{p.with_suffix('.md').name}]({p.with_suffix('.md').name}) |")
    runs = next(iter(ts.values()))[1].get("runs", [])
    L += ["", "The runs: " + ", ".join(f"{r['tag']} [{r['run']}]({REPO_URL}/actions/runs/{r['run']})" for r in runs)
          + (f"; every one on {runs[0]['engine']}." if runs and len({r.get('engine') for r in runs}) == 1 else "."),
          "", "## The rows a reader looks at first", ""]
    for (b, vs), (p, d) in ts.items():
        rows = d.get("rows", {})
        L += [f"### {b} s against {against[vs]}", "", "| Gauge | Reading |", "|---|---|"]
        L += [f"| {g} | {rows[g]['reading']} |" for g in FIRST if g in rows]
        L.append("")
    L += ["Run and scored by Dubra Software Inc. / The Omni-Compass LLC's own code. No outside party has reviewed or approved "
          "these results."]
    return canonical_name("\n".join(legal_stamp(L)) + "\n")


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    text = build()
    if "--check" in argv:
        ok = OUT.exists() and OUT.read_text(encoding="utf-8") == text
        print("pace_index: results/pace/PACE.md " + ("reads its tables" if ok else "differs from its tables: python3 tools/pace_index.py"))
        return 0 if ok else 1
    OUT.write_text(text, encoding="utf-8")
    print(f"{OUT.relative_to(ROOT)} written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
