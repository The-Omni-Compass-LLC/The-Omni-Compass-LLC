# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The Owner's Manual's chapter 16, "Results to Date", written from the newest table of each test, never typed (the founder's
order of 2 November 2026: no number on any page that was not calculated from its record).

Every block stands in docs/OMNI_COMPASS_OWNERS_MANUAL.md between its markers and is written from its record:

  kubernetes, addons, stores, robust, simulators, organisms   the benefit sheet's record (results/BENEFIT_SHEET.json): each test's
                                                               newest three-run table, its engine, its reading and every judged
                                                               gauge in the key's words, the span of the three runs' changes
  sheet                                                        the same record as one table, test by test
  cloud                                                        Azure's record (results/live/AKS_STEADY_100_OMNI_V18.md), its own
                                                               reading by the one key quoted
  realms, grid, scenarios                                      the front page's own parts (tools/organism_words.py), so the two
                                                               pages never read differently

  python3 tools/results_chapter.py          write every block
  python3 tools/results_chapter.py --check  exit 1 if any block differs from what its record gives (run by verify.py)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
from tools import organism_words as OW  # noqa: E402

MANUAL = ROOT / "docs" / "OMNI_COMPASS_OWNERS_MANUAL.md"
SHEET = ROOT / "results" / "BENEFIT_SHEET.json"
CLOUD = ROOT / "results" / "live" / "AKS_STEADY_100_OMNI_V18.md"

ADDONS = ("Goldilocks", "CruiseKube", "add-ons")
STORES = ("PostgreSQL", "MySQL", "MongoDB", "Kafka", "Redis")
SIMS = ("Power grids", "Robot arms", "Drone swarms", "Buildings and batteries")
GROUPS = {
    "kubernetes": lambda b: b.startswith("Real Kubernetes, ") and not any(x in b for x in ADDONS),
    "addons": lambda b: b.startswith("Real Kubernetes, ") and any(x in b for x in ADDONS),
    "stores": lambda b: b.split(",")[0] in STORES,
    "robust": lambda b: b.startswith("Robustness"),
    "simulators": lambda b: b.startswith(SIMS),
    "organisms": lambda b: "real cluster inside" in b,
}
LEAD = ("Written from the newest three-run table of each test by `python3 tools/results_chapter.py`, from the benefit sheet's "
        "record (`results/BENEFIT_SHEET.json`); `verify.py` fails a push where it differs. Each line names the test, its table and "
        "the engine its runs were on, its reading, and then every judged gauge with the span of the three runs' changes (the span "
        "of the three point estimates, not an interval), in the key's words. Run and scored by The Omni-Compass LLC's own code. No "
        "outside party has reviewed or approved these results.")


def begin(name: str) -> str:
    return f"<!-- results: {name} (tools/results_chapter.py) -->"


def end(name: str) -> str:
    return f"<!-- end of results: {name} -->"


def rows() -> list:
    return json.loads(SHEET.read_text(encoding="utf-8"))["rows"]


def how_much(pct: float) -> str:
    return f"{abs(pct):.1f}% {'GAIN' if pct > 0 else ('LOSS' if pct < 0 else 'STEADY')}"


def line(r: dict) -> list:
    name = re.sub(r"^Real Kubernetes, ", "", r["benchmark"])
    name = name[0].upper() + name[1:]
    words = r["words"].strip().rstrip(".")
    text = (f"- **{name}** (`{r['file']}`, {r['engine']}): **{r['benefit']}**, by the index's rule {how_much(r['pct'])}. "
            f"{words[0].upper() + words[1:]}.")
    return OW.wrap(text)


def group_block(name: str) -> list:
    picked = [r for r in rows() if GROUPS[name](r["benchmark"])]
    L = OW.wrap(LEAD) + [""]
    for r in picked:
        w = line(r)
        L += [w[0]] + ["  " + x for x in w[1:]]
    return L


def sheet_block() -> list:
    L = OW.wrap("Every test's newest table in one place, written from the same record (`results/BENEFIT_SHEET.json`) by "
                "`python3 tools/results_chapter.py`; the words beside each number are in each test's own line above and in "
                "`docs/BENEFIT_SHEET.md`.") + ["",
         "| Test | Engine | Reading | By the index's rule | Table |", "|---|---|---|---:|---|"]
    for r in rows():
        L.append(f"| {r['benchmark']} | {r['engine']} | **{r['benefit']}** | {how_much(r['pct'])} | `{r['file']}` |")
    return L


def cloud_block() -> list:
    t = CLOUD.read_text(encoding="utf-8")
    title = t.splitlines()[0].lstrip("# ").strip()
    m = re.search(r"\*\*Read by the one key\*\*.*?\): (.+?)(?:\n\n|$)", t, re.S)
    said = " ".join(m.group(1).split()) if m else "not found in the record"
    pairs = re.search(r"vs native, (\d+) paired repetitions", t)
    run = re.search(r"Run (\d+)", t)
    eng = re.search(r"engine \*\*(omni-v\d+)\*\*", t)
    text = (f"**{title}** (`{CLOUD.relative_to(ROOT)}`; run {run.group(1) if run else 'not named'}, engine "
            f"{eng.group(1) if eng else 'not named'}, {pairs.group(1) if pairs else 'not counted'} paired repetitions read). The "
            f"record's own reading, quoted from it by `python3 tools/results_chapter.py`: \"{said}\"")
    return OW.wrap(text)


def verdicts_block() -> list:
    """Section 16.6b: the wiring verdicts page's own summary, quoted from it."""
    t = (ROOT / "docs" / "WIRING_VERDICTS.md").read_text(encoding="utf-8")
    m = re.search(r"^In words: (.+)$", t, re.M)
    said = m.group(1).strip() if m else "not found on the page"
    return OW.wrap("What the page says today, quoted from it by `python3 tools/results_chapter.py` (`docs/WIRING_VERDICTS.md`, written "
                   f"by `tools/wiring_verdicts.py` from the tables that stand): \"{said}\"")


def worked_block() -> list:
    """Section 3.4's worked examples of S = G / (1 + G), from the newest tables: the all-four test's work and the pooler's connections."""
    rs = {r["benchmark"]: r for r in rows()}
    a4, pg = rs["Real Kubernetes, all four at once"], rs["PostgreSQL, the pooler's pool size"]
    m = re.search(r"work inside the line up ([\d.]+)% to ([\d.]+)%", a4["words"])
    c = re.search(r"connections held open cut ([\d.]+)% to ([\d.]+)%", pg["words"])
    lo, hi = float(m.group(1)), float(m.group(2))
    clo, chi = float(c.group(1)), float(c.group(2))
    glo, ghi = lo / 100.0, hi / 100.0
    rlo, rhi = 1.0 - chi / 100.0, 1.0 - clo / 100.0
    text = (f"**Two worked examples, from the newest tables** (written from the benefit sheet's record by "
            f"`python3 tools/results_chapter.py`). In the all-four Kubernetes test (`{a4['file']}`, {a4['engine']}) the same machines "
            f"answered {m.group(1)}% to {m.group(2)}% more requests inside the response line: *G* is {glo:.2f} to {ghi:.2f}, so the same "
            f"work would need 1/{1 + glo:.2f} to 1/{1 + ghi:.2f} of the machines, a saving *S* = *G* / (1 + *G*) of "
            f"{100 * glo / (1 + glo):.1f}% to {100 * ghi / (1 + ghi):.1f}%, had the fleet been free to shrink; on kind it was not, which "
            f"is why the table reports the work and not a bill. In the database test (`{pg['file']}`, {pg['engine']}) the pooler held "
            f"{c.group(1)}% to {c.group(2)}% fewer connections open for the same work: the resource there is connections, "
            f"*C[omni] / C[native]* is {rlo:.3f} to {rhi:.3f}, and read as more work for the same connections the gain would be "
            f"*G* = {100 * (1 / rhi - 1):.1f}% to {100 * (1 / rlo - 1):.1f}%. Which of the two a stack takes is decided by the stack, "
            f"and each table reports what happened.")
    return OW.wrap(text)


BLOCKS = {**{k: (lambda k=k: group_block(k)) for k in GROUPS},
          "sheet": sheet_block, "cloud": cloud_block, "worked": worked_block, "verdicts": verdicts_block,
          "realms": lambda: OW.realms_lines("../"), "grid": lambda: OW.grid_lines("../"),
          "scenarios": lambda: OW.scenarios_lines("../")}


def put(text: str) -> str:
    for name, make in BLOCKS.items():
        a, z = text.find(begin(name)), text.find(end(name))
        if a < 0 and z < 0:
            continue
        if a < 0 or z < 0 or z < a:
            raise SystemExit(f"the Owner's Manual carries a broken marker pair for results: {name}")
        text = text[:a] + "\n".join([begin(name)] + make() + [end(name)]) + text[z + len(end(name)):]
    return text


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args(argv)
    t = MANUAL.read_text(encoding="utf-8")
    missing = [n for n in BLOCKS if begin(n) not in t]
    new = put(t)
    if a.check:
        if missing:
            print("the Owner's Manual lacks the results blocks: " + ", ".join(missing))
            return 1
        if new != t:
            print("the Owner's Manual's chapter 16 differs from its records (python3 tools/results_chapter.py)")
            return 1
        print("the Owner's Manual's chapter 16: in line with its records")
        return 0
    MANUAL.write_text(new, encoding="utf-8")
    print("docs/OMNI_COMPASS_OWNERS_MANUAL.md: chapter 16 written from its records" + (f" (no markers yet: {', '.join(missing)})" if missing else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
