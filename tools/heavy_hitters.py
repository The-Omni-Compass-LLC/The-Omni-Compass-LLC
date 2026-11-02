#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Heaviest hitters first: the one order every list of the catalog's muscles takes, written once.

The founder's order of 1 November, night: wherever the catalog of the 1,107 muscles is listed, in full or condensed, it is
"always the most heaviest hitters first", in descending order down to the last, "broken into the four categories they live".

**The four categories** are the four realms, each muscle under its own home realm (`realms/catalog_v5.csv`, column `realm`),
so the four lists hold every muscle once and add to 1,107. A muscle of the spine (it sits in all four realms) is listed under
its home realm and marked as the spine's.

**A muscle's hit** is what Omni-Compass did for it against native in the newest record of every muscle alone
(`results/realms_v5/REALMS_V5.json`, written by `tools/run_realms_v5.py`; our own models, evidence class S; the engine and the
day it ran on are in the record and on every page that uses this order). The heaviest hitter is the muscle with the most of its
own life taken back under its line, so the hit is read in this order:

1. **Decisions taken back under its line**: native's decisions over the muscle's line less Omni-Compass's, over the record's
   seeds and both of the muscle's loads, in percent of all of the muscle's decisions (the record's own change in the share of
   decisions over the line, read as a cut). A decision over the line is a muscle past its own limit, the first harm do no harm
   names, so every muscle that takes decisions back under its line comes first, the most first.
2. **The line cleared sooner**: for a muscle whose decisions over the line do not move, the time to clear the work waiting in
   line taken away, in percent of native's (the line load), the most first.
3. **Work added**: for a muscle that only adds work, the work added in percent of native (the mean of both loads), the most first.
4. **No hit**: the same as native (no change of 0.5% or more on any gauge, the one key's floor), then at its limit on native
   (native already runs the knob at the top of its range, so Omni-Compass writes nothing).

Equal hits are ordered by the catalog's own number, so the order is total and the same on every run of this file.

The order reads a record; it moves no engine rule and no catalog row (the catalog file keeps the order the runners read it
in, so no seed or result moves). When the record of every muscle alone runs again on a newer engine, every list follows it.

    python3 tools/heavy_hitters.py              the ten heaviest hitters of each realm, with their hits
    python3 tools/heavy_hitters.py --check      every catalog page lists its muscles in this order (verify.py runs the tests)
"""
from __future__ import annotations

import argparse
import ast
import csv
import json
import re
import sys
from collections import OrderedDict, namedtuple
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "realms" / "catalog_v5.csv"
RECORD = ROOT / "results" / "realms_v5" / "REALMS_V5.json"
REALMS = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                      ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized")])
NO_HIT = ("AT ITS LIMIT ON NATIVE", "SAME AS NATIVE")

Hit = namedtuple("Hit", "tier value gauge rescued label")   # tier 1 misses, 2 line, 3 work, 4 same, 5 at its limit; value in percent


def _lit(x):
    return ast.literal_eval(x) if isinstance(x, str) else x


def catalog_number(mid: str) -> tuple:
    """The catalog's own number: the numbered ids first, then the audited and the v5 ids, each in its own order."""
    return (0, int(mid), "") if mid.isdigit() else (1, int("".join(c for c in mid if c.isdigit()) or 0), mid)


def hit_of(m: dict) -> Hit:
    """One muscle's hit from its entry in the record of every muscle alone."""
    label = str(m.get("label", ""))
    loads = m.get("loads") or {}
    vn = sum(int(L.get("viol_native", 0) or 0) for L in loads.values())
    vm = sum(int(L.get("viol_max", 0) or 0) for L in loads.values())
    steps = sum(int(L.get("steps", 0) or 0) for L in loads.values())
    rescued = max(0, vn - vm)
    if label == "AT ITS LIMIT ON NATIVE":
        return Hit(5, 0.0, None, rescued, label)
    if label == "SAME AS NATIVE" or not loads:
        return Hit(4, 0.0, None, rescued, label)
    if rescued > 0 and steps > 0:
        return Hit(1, 100.0 * rescued / steps, "misses", rescued, label)
    line = _lit((loads.get("line") or {}).get("line"))
    sooner = (line[0] - line[1]) / line[0] if line and line[0] and line[0] > 0 and line[1] is not None else 0.0
    if sooner > 0:
        return Hit(2, 100.0 * sooner, "line", rescued, label)
    works = [(_lit(L.get("summary")) or {}).get("work", [0.0])[0] for L in loads.values()]
    work = sum(works) / len(works) if works else 0.0
    if work > 0:
        return Hit(3, 100.0 * work, "work", rescued, label)
    return Hit(4, 0.0, None, rescued, label)


@lru_cache(maxsize=4)
def _hits(record: str) -> tuple:
    rec = json.loads(Path(record).read_text())
    run = rec.get("run") or {}
    return ({m["row"]["muscle_id"]: hit_of(m) for m in rec.get("muscles") or []},
            {"engine": run.get("engine", ""), "started": run.get("started", ""), "seeds": len(run.get("seeds") or []),
             "commit": str(run.get("commit", ""))[:12]})


def hits(record: Path = RECORD) -> dict:
    """{muscle_id: Hit} from the record."""
    return _hits(str(record))[0]


def record_run(record: Path = RECORD) -> dict:
    """The engine, the day, the seeds and the commit of the record the order reads."""
    return _hits(str(record))[1]


NONE = Hit(4, 0.0, None, 0, "")


def key(row: dict, h: dict | None = None) -> tuple:
    """The sort key: the tier, then the hit within it, the more first, then the catalog's number."""
    x = (h if h is not None else hits()).get(row["muscle_id"], NONE)
    return (x.tier, -x.value, catalog_number(row["muscle_id"]))


def order(rows, h: dict | None = None) -> list:
    """The rows, heaviest hitter first."""
    h = h if h is not None else hits()
    return sorted(rows, key=lambda r: key(r, h))


def by_realm(rows, h: dict | None = None) -> "OrderedDict[str, list]":
    """The four realms in their standing order, each its home muscles heaviest hitter first."""
    h = h if h is not None else hits()
    out = OrderedDict((k, []) for k in REALMS)
    for r in rows:
        out.setdefault(r["realm"], []).append(r)
    return OrderedDict((k, order(v, h)) for k, v in out.items())


def words(x: Hit) -> str:
    """The hit in words, the word first (the order of 23 October), the number beside it carrying the word's sign."""
    if x.tier == 5:
        return "at its limit on native: native runs the knob at the top of its range and Omni-Compass writes nothing"
    if x.tier == 4:
        return "STEADY: the same as native, no change of 0.5% or more"
    return {"misses": f"GAIN +{x.value:.2f}%: of all its decisions, {x.value:.2f}% taken back under its line ({x.rescued:,} decisions)",
            "line": f"GAIN +{x.value:.1f}%: the work waiting in line cleared {x.value:.1f}% sooner",
            "work": f"GAIN +{x.value:.1f}%: work up {x.value:.1f}%"}[x.gauge]


def short(x: Hit) -> str:
    """The hit in a few words, for a table cell."""
    if x.tier == 5:
        return "at its limit on native"
    if x.tier == 4:
        return "STEADY"
    return {"misses": f"GAIN +{x.value:.2f}% of decisions back under the line",
            "line": f"GAIN +{x.value:.1f}%, the line cleared sooner",
            "work": f"GAIN +{x.value:.1f}%, work up"}[x.gauge]


def rule_words(record: Path = RECORD) -> str:
    """The order in one paragraph, for every page that lists the muscles."""
    run = record_run(record)
    return ("**Heaviest hitters first** (the founder's order of 1 November): every list of the muscles is ordered by what "
            "Omni-Compass did for each muscle against native in the record of every muscle alone (`results/realms_v5/REALMS_V5.json`; "
            f"our own models, evidence class S; {run['engine']}, run {run['started']}, {run['seeds']} seeds, both loads). First the "
            "muscles that take decisions back under their line, the largest share of all their decisions first (a decision over the "
            "line is a muscle past its own limit, the first harm do no harm names); then the muscles that clear the work waiting in "
            "line sooner, the most first; then the muscles that only add work; then the muscles the same as native; last the muscles "
            "at their limit on native, where Omni-Compass writes nothing; equal hits by the catalog's number. The four lists are the "
            "four realms, each muscle under its home realm, every muscle once (`tools/heavy_hitters.py`).")


# ------------------------------------------------------------------------------------------------------------- the check
ID_CELL = re.compile(r"^\|\s*\d+\s*\|\s*([0-9A-Za-z-]+)\s*\|")


def page_order(path: Path) -> "OrderedDict[str, list]":
    """The muscle ids of each ranked table on a page, by the table's heading (a heading that starts with '### ' and names a
    realm), as the page lists them."""
    out, cur = OrderedDict(), None
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            cur = next((k for k, n in REALMS.items() if line[4:].startswith(n)), None)
            if cur:
                out[cur] = []
            continue
        m = ID_CELL.match(line)
        if cur and m:
            out[cur].append(m.group(1))
    return out


def check(path: Path, rows=None) -> list:
    """Every realm's ranked table on the page in the heaviest-hitter order, every muscle once."""
    rows = rows if rows is not None else list(csv.DictReader(open(CATALOG, encoding="utf-8")))
    want = {k: [r["muscle_id"] for r in v] for k, v in by_realm(rows).items()}
    got = page_order(path)
    bad = []
    for k, ids in want.items():
        if got.get(k) != ids:
            n = next((i for i, (a, b) in enumerate(zip(got.get(k, []), ids)) if a != b), min(len(got.get(k, [])), len(ids)))
            bad.append(f"{path.relative_to(ROOT)}: {REALMS[k]} is not heaviest hitter first (first difference at rank {n + 1})")
    return bad


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args(argv)
    rows = list(csv.DictReader(open(CATALOG, encoding="utf-8")))
    if a.check:
        bad = check(ROOT / "docs" / "MUSCLE_CATALOG.md", rows)
        for b in bad:
            print("FAIL", b)
        print("heaviest hitters first: " + ("FAIL" if bad else "PASS"))
        return 1 if bad else 0
    h = hits()
    run = record_run()
    print(f"the record: {run['engine']}, {run['started']}, {run['seeds']} seeds (class S)")
    for k, rs in by_realm(rows, h).items():
        print(f"\n{REALMS[k]}: {len(rs)} muscles")
        for i, r in enumerate(rs[:a.top], 1):
            print(f"  {i:>3}. {r['muscle']:<38} {short(h.get(r['muscle_id'], NONE))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
