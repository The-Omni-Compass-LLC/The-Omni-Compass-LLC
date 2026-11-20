#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine's ladder: every version recorded as a benchmark step (the founder's order of 14 November: "all these runs and all
these versions of engines are to be recorded as benchmarks, as versions, so people can see all of the tuning mechanism of how
improving and what makes it the defensible, benchmarkable engine").

  python3 tools/engine_ladder.py            write results/ENGINE_LADDER.md and .json
  python3 tools/engine_ladder.py --check    fail when the ladder differs from the records it is read from

For each version, read from the repository's own records and nothing else: its fingerprint (OMNI_VN.json: digest and files),
the change-control row that says what changed and why (docs/CHANGE_CONTROL.md), its model gate against the version before
(results/model_gate/VN_VS_VM.json, our own models, class S: the candidate's readings against the engine that stood, counted by
word), and its own three-run tables on real machines (results/live/VN_*.json and results/gpu/VN_*_ABC.json: every judged row
counted by its word). Each table is its own engine's record and is never read across engines; the ladder sets them side by side
so the tuning can be followed step by step, LOSS rows counted with the rest.
"""
from __future__ import annotations

import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.chips_board import TOP, END, word  # noqa: E402  (one notice, one word reader)
from tools.reread import gauges  # noqa: E402

OUT_MD, OUT_JSON = ROOT / "results" / "ENGINE_LADDER.md", ROOT / "results" / "ENGINE_LADDER.json"
WORDS = ("GAIN", "LOSS", "power given", "the runs disagree", "STEADY")


def versions():
    out = []
    for f in glob.glob(str(ROOT / "OMNI_V*.json")):
        m = re.match(r"OMNI_V(\d+)\.json$", Path(f).name)
        if m:
            d = json.loads(Path(f).read_text())
            out.append((int(m.group(1)), str(d.get("digest", ""))[:16], len(d.get("files") or {})))
    return sorted(out)


def change_rows():
    rows = {}
    cc = ROOT / "docs" / "CHANGE_CONTROL.md"
    for line in cc.read_text().splitlines():
        m = re.match(r"^\| omni-v(\d+) \| ([^|]*) \| `?([0-9a-f]*)`? \| ([^|]*) \| (.*) \|$", line)
        if m:
            rows[int(m.group(1))] = {"landed": m.group(2).strip(), "change": m.group(5).strip()}
    return rows


def gate(n):
    for f in sorted(glob.glob(str(ROOT / "results" / "model_gate" / f"V{n}_VS_V*.json"))):
        m = re.match(rf"V{n}_VS_V(\d+)\.json$", Path(f).name)
        if not m or int(m.group(1)) != n - 1 and not (n == 21 and int(m.group(1)) == 20):
            continue
        d = json.loads(Path(f).read_text())
        c = Counter()
        for mod in (d.get("models") or {}).values():
            for g in ((mod or {}).get("gauges") or {}).values():
                w = ((g or {}).get("cand_vs_base") or {}).get("word")
                if w:
                    c[word(w)] += 1
        return {"record": f"results/model_gate/{Path(f).stem}.md", "against": f"omni-v{m.group(1)}", "models": len(d.get("models") or {}),
                "readings": dict(c)}
    md = sorted(glob.glob(str(ROOT / "results" / "model_gate" / f"V{n}_VS_V{n - 1}.md")))
    return {"record": f"results/model_gate/{Path(md[0]).name}", "against": f"omni-v{n - 1}", "models": None, "readings": {}} if md else None


def tables(n):
    out = []
    for f in sorted(glob.glob(str(ROOT / "results" / "live" / f"V{n}_*.json")) + glob.glob(str(ROOT / "results" / "gpu" / f"V{n}_*_ABC.json"))):
        try:
            d = json.loads(Path(f).read_text())
        except (OSError, ValueError):
            continue
        c = Counter()
        if isinstance(d.get("rows"), list):
            for r in d["rows"]:
                w = word(r.get("reading", ""))
                if w in WORDS:
                    c[w] += 1
        else:
            for _, g in gauges(d):
                w = word(g.get("reading", ""))
                if w in WORDS:
                    c[w] += 1
        if c:
            out.append({"table": str(Path(f).relative_to(ROOT))[:-5] + ".md", "readings": dict(c)})
    return out


def build():
    cc = change_rows()
    steps = []
    for n, digest, files in versions():
        ts = tables(n)
        tot = Counter()
        for t in ts:
            tot.update(t["readings"])
        steps.append({"version": f"omni-v{n}", "digest": digest, "files": files, **cc.get(n, {"landed": "", "change": ""}),
                      "gate": gate(n), "tables": ts, "table_readings": dict(tot)})
    return {"steps": steps}


def cnt(c):
    return ", ".join(f"{w} {c[w]}" for w in WORDS if c.get(w)) or "none"


def render(b):
    L = ["# The engine's ladder: every version a benchmark step", "", f"> {TOP}", "",
         "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
         "Every version of the engine, in order, read from the repository's own records (`tools/engine_ladder.py`): its "
         "fingerprint, what changed and why (`docs/CHANGE_CONTROL.md`), its model gate against the version before (our own models, "
         "evidence class S, never proof: the candidate's readings against the engine that stood, by word), and its own three-run "
         "tables on real machines (evidence class L and, on the chips, P: every judged row by its word, LOSS rows counted with the "
         "rest). A version lands only when its gate reads no LOSS against the engine that stands (the rule since 15 October); every "
         "benchmark then runs again on it, and its tables are its own record, never read across engines. The ladder sets them side "
         "by side so the tuning can be followed step by step.", "",
         "| Version | Landed (UTC) | Digest | Files | Model gate against the version before (class S) | Its own three-run tables | Their judged rows |",
         "|---|---|---|---:|---|---:|---|"]
    for s in b["steps"]:
        g = s["gate"]
        n = int(s["version"].split("v")[-1])
        if g:
            gs = f"[{Path(g['record']).name}]({g['record'].replace('results/', '')}): " + (cnt(g["readings"]) if g["readings"] else "read in its page")
        else:
            gs = "none: before the gate (15 October)" if n <= 7 else "no gate record of its own"
        L.append(f"| {s['version']} | {s['landed'] or 'before the change-control record'} | `{s['digest']}` | {s['files']} | {gs} | "
                 f"{len(s['tables'])} | {cnt(s['table_readings'])} |")
    L += ["", "## What each version changed, and why", ""]
    for s in reversed(b["steps"]):
        if s["change"]:
            L += [f"- **{s['version']}** ({s['landed']}): {s['change']}"]
    L += ["", "## Each version's own tables", ""]
    for s in reversed(b["steps"]):
        if s["tables"]:
            L += [f"### {s['version']}", "", "| Table | Judged rows |", "|---|---|"]
            L += [f"| [{Path(t['table']).name}]({t['table'].replace('results/', '')}) | {cnt(t['readings'])} |" for t in s["tables"]]
            L.append("")
    L += ["---", "", f"*{END}*", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    b = build()
    md, js = render(b), json.dumps(b, indent=1, sort_keys=True) + "\n"
    if "--check" in argv:
        bad = [p.name for p, s in ((OUT_MD, md), (OUT_JSON, js)) if not p.exists() or p.read_text() != s]
        if bad:
            print("engine ladder out of date (python3 tools/engine_ladder.py): " + ", ".join(bad)); return 1
        print(f"engine ladder: {len(b['steps'])} versions, current"); return 0
    OUT_MD.write_text(md); OUT_JSON.write_text(js)
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}: {len(b['steps'])} versions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
