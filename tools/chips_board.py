#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every chip, every run: the board of the GPU benchmark (the founder's order of 14 November: "results for all different chips ...
as a benchmark ... however it's combined to be the one scenario, but as well as all the scenarios").

  python3 tools/chips_board.py            write results/CHIPS_BOARD.md and .json from the chip tables
  python3 tools/chips_board.py --check    fail when the board differs from what the tables say (verify.py)

Each chip is its own benchmark: arm A, the card under its own firmware (native), against arm B, the same card with Omni-Compass on
top, three runs on rented machines (A, B and C), every row read by the one key (tools/readings.py) in the table the runs wrote
(results/gpu/*_ABC.json, tools/gpu_abc.py). Nothing is computed here but counts: each table's rows by their word, the card's own
meter (class P) apart from the stacks' models (class S), and every row that is not STEADY listed with its word, LOSS rows
included. The combined board adds the chips together on each engine and never across engines (a table is its engine's record).
A chip wired but not yet run is listed as such, with the workflow that runs it, never with a number.
"""
from __future__ import annotations

import glob
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT_MD, OUT_JSON = ROOT / "results" / "CHIPS_BOARD.md", ROOT / "results" / "CHIPS_BOARD.json"

NOTICE = ("© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any "
          "commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of "
          "Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. "
          "Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`.")
TOP = NOTICE + " `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com"
END = NOTICE + " All patents, copyrights and trademarks filed in the USA. www.omni-compass.com"

# every chip the harness can rent, run or not: (chip, where, machine, workflow, the table-name key that marks its tables)
CHIPS = [
    ("NVIDIA A10, 24 GB", "Lambda", "gpu_1x_a10 (one card)", "lambda-gpu.yml (test 1card)", "A10_"),
    ("NVIDIA A100, 40 GB SXM4", "Lambda", "gpu_1x_a100_sxm4 (one card)", "lambda-gpu.yml (test 1card, instance_type)", "A100_CAP|A100_SAVE|A100_FAST"),
    ("NVIDIA A100, 80 GB SXM4, eight cards", "Lambda", "gpu_8x_a100_80gb_sxm4", "lambda-gpu.yml (test 8card); not now, the founder's word of 14 November, for its cost an hour", "A100_8CARD"),
    ("NVIDIA A10G, 24 GB", "Amazon", "g5.xlarge, g5.2xlarge (one card)", "aws-gpu.yml (14 November)", "A10G_"),
    ("NVIDIA L4, 24 GB", "Amazon", "g6.xlarge (one card)", "aws-gpu.yml (instance_type g6.xlarge)", "L4_"),
    ("NVIDIA T4, 16 GB", "Amazon", "g4dn.xlarge (one card)", "aws-gpu.yml (instance_type g4dn.xlarge)", "T4_"),
    ("NVIDIA H100, 80 GB PCIe", "Lambda", "gpu_1x_h100_pcie (one card)", "lambda-gpu.yml (test 1card, instance_type)", "H100_"),
]
ORDER = ("GAIN", "LOSS", "power given", "the runs disagree", "STEADY", "shown, not judged", "no value")


def word(reading: str) -> str:
    r = (reading or "").strip()
    for w in ("GAIN", "LOSS", "power given", "the runs disagree", "STEADY", "EVEN"):
        if r.startswith(w):
            return "STEADY" if w == "EVEN" else w
    if r.startswith("one repetition") or "shown, not judged" in r:
        return "shown, not judged"
    return "no value"


def engine_of(d) -> str:
    e = d.get("engine")
    e = e[0] if isinstance(e, list) else e
    m = re.match(r"(omni-v\d+)", str(e or ""))
    return m.group(1) if m else "unknown"


def chip_of(name: str) -> str:
    for chip, _, _, _, key in CHIPS:
        if re.search(key, name):
            return chip
    return "unknown"


def tables():
    out = []
    for f in sorted(glob.glob(str(ROOT / "results" / "gpu" / "*_ABC.json"))):
        name = Path(f).name
        d = json.loads(Path(f).read_text())
        rows = d["rows"]
        counts = {"P": Counter(), "S": Counter(), "P+S": Counter()}
        listed = []
        if isinstance(rows, dict):          # the card alone: every gauge is the card's own meter (class P)
            for g, r in rows.items():
                w = word(r.get("reading", ""))
                counts["P"][w] += 1
                if w not in ("STEADY", "shown, not judged", "no value"):
                    listed.append({"class": "P", "where": "the card", "gauge": g, "reading": r["reading"]})
        else:                               # the stacks with the card inside: the card's meter, the models, both together
            cls = {"card": "P", "sim": "S", "all": "P+S"}
            for r in rows:
                w = word(r.get("reading", ""))
                c = cls.get(r.get("part"), "S")
                counts[c][w] += 1
                if w not in ("STEADY", "shown, not judged", "no value"):
                    listed.append({"class": c, "where": f"{r.get('copies')}x {r.get('organism')}", "gauge": r.get("measure"),
                                   "reading": r["reading"]})
        out.append({"table": f"results/gpu/{name[:-5]}.md", "chip": chip_of(name), "engine": engine_of(d), "title": d["title"],
                    "runs": d.get("runs", []), "counts": {k: dict(v) for k, v in counts.items() if v}, "listed": listed})
    return out


def build():
    ts = tables()
    register = []
    for chip, where, machine, wf, _ in CHIPS:
        mine = [t for t in ts if t["chip"] == chip]
        register.append({"chip": chip, "where": where, "machine": machine, "workflow": wf,
                         "tables": [t["table"] for t in mine],
                         "engines": sorted({t["engine"] for t in mine}, key=lambda e: int(e.split("v")[-1])),
                         "status": "run" if mine else "wired, not yet run"})
    combined = {}
    for t in ts:
        e = combined.setdefault(t["engine"], {"chips": set(), "tables": 0, "P": Counter(), "S": Counter(), "P+S": Counter()})
        e["chips"].add(t["chip"]); e["tables"] += 1
        for k, v in t["counts"].items():
            e[k].update(v)
    combined = {k: {"chips": sorted(v["chips"]), "tables": v["tables"], **{c: dict(v[c]) for c in ("P", "S", "P+S") if v[c]}}
                for k, v in sorted(combined.items(), key=lambda kv: int(kv[0].split("v")[-1]))}
    return {"register": register, "tables": ts, "combined": combined}


def cnt(c: dict) -> str:
    return ", ".join(f"{w} {c[w]}" for w in ORDER if c.get(w)) or "none"


def render(b) -> str:
    L = [f"# Every chip, every run: the GPU benchmark board", "", f"> {TOP}", "",
         "Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.", "",
         "Each chip is its own benchmark: **arm A**, the card under its own firmware (native), against **arm B**, the same card "
         "with Omni-Compass on top, three runs on rented machines (A, B and C), every row read by the one key "
         "(`tools/readings.py`) in the table its runs wrote. The cloud's two arms (C, native on a cloud cluster; D, Omni-Compass "
         "on top of it) are the cloud's own tables (`results/TWO_BILLS.md`). Nothing here is computed but counts; every row that "
         "is not STEADY is listed with its word, LOSS rows included. The card's own meter is evidence class P; the stacks' "
         "models around the card are class S (our own models, never proof). A table is its engine's record: the combined board "
         "adds chips together on one engine, never across engines. Written by `tools/chips_board.py` from `results/gpu/*_ABC.json`.", "",
         "## 1. Every chip", "", "| Chip | Where | Machine | Workflow | Status | Tables | Engines |", "|---|---|---|---|---|---:|---|"]
    for r in b["register"]:
        L.append(f"| {r['chip']} | {r['where']} | {r['machine']} | `{r['workflow'].split(' ')[0]}`{r['workflow'][len(r['workflow'].split(' ')[0]):]} | "
                 f"{r['status']} | {len(r['tables'])} | {', '.join(r['engines']) or 'none'} |")
    L += ["", "## 2. Every table, each chip its own scenario", ""]
    for chip in [r["chip"] for r in b["register"] if r["tables"]]:
        L += [f"### {chip}", "", "| Table | Engine | Runs (A, B, C) | The card's own meter (class P) | The stacks' models (class S) | Both together |",
              "|---|---|---|---|---|---|"]
        for t in [t for t in b["tables"] if t["chip"] == chip]:
            c = t["counts"]
            L.append(f"| [{Path(t['table']).name}]({Path(t['table']).name.join(['gpu/', ''])}) | {t['engine']} | {', '.join(t['runs'])} | "
                     f"{cnt(c.get('P', {}))} | {cnt(c.get('S', {}))} | {cnt(c.get('P+S', {}))} |")
        L.append("")
        rows = [(t, x) for t in b["tables"] if t["chip"] == chip for x in t["listed"]]
        if rows:
            L += ["Every row that is not STEADY:", "", "| Table | Class | Where | Gauge | Reading |", "|---|---|---|---|---|"]
            L += [f"| {Path(t['table']).stem} | {x['class']} | {x['where']} | {x['gauge']} | {x['reading']} |" for t, x in rows]
            L.append("")
    L += ["## 3. All chips combined, engine by engine", "",
          "| Engine | Chips | Tables | The card's own meter (class P) | The stacks' models (class S) | Both together |", "|---|---|---:|---|---|---|"]
    for e, v in b["combined"].items():
        L.append(f"| {e} | {', '.join(v['chips'])} | {v['tables']} | {cnt(v.get('P', {}))} | {cnt(v.get('S', {}))} | {cnt(v.get('P+S', {}))} |")
    waiting = [r["chip"] for r in b["register"] if not r["tables"]]
    L += ["", "## 4. Not yet run", "",
          ("Wired and not yet run, so no number stands for them: " + "; ".join(waiting) + ". The engine that stands runs on each "
           "the moment its workflow is started; the eight-card machine waits on the founder's word for its cost an hour.") if waiting
          else "Every chip in the register has run.", "", "---", "", f"*{END}*", ""]
    return "\n".join(L)


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    b = build()
    md, js = render(b), json.dumps(b, indent=1, sort_keys=True) + "\n"
    if "--check" in argv:
        bad = [p.name for p, s in ((OUT_MD, md), (OUT_JSON, js)) if not p.exists() or p.read_text() != s]
        if bad:
            print("chips board out of date (python3 tools/chips_board.py): " + ", ".join(bad)); return 1
        print(f"chips board: {len(b['tables'])} tables on {sum(1 for r in b['register'] if r['tables'])} chips, current"); return 0
    OUT_MD.write_text(md); OUT_JSON.write_text(js)
    print(f"wrote {OUT_MD.relative_to(ROOT)} and {OUT_JSON.relative_to(ROOT)}: {len(b['tables'])} tables")
    return 0


if __name__ == "__main__":
    sys.exit(main())
