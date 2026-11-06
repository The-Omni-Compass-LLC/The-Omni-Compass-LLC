# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""docs/REALM_MUSCLES.md from realms/catalog_v5.csv: every organism written out, muscle by muscle.

The seven organisms (the founder's order of 16 October): the spine first, the muscles every real stack runs on and an
organism of its own; then each realm's organism (its own families with the spine under them); then the two whole-catalog
organisms, the four stacked (every realm's organism on one clock, every duplicate of the spine kept) and the tower (every
muscle once). Every list is heaviest hitter first (tools/heavy_hitters.py, the founder's order of 1 November): the 1,107 in
the four realms they live in, each muscle under its home realm, then the spine's and each realm's own. Each muscle is followed
by the one knob Omni-Compass may hold on it; what the engine does with that knob, how it is wired and its own card are in
docs/MUSCLE_CATALOG.md (tools/muscle_catalog.py). What the spine is and why it is an organism is docs/THE_SPINE.md.

    python3 tools/realm_muscles.py
"""
from __future__ import annotations

import csv
from collections import OrderedDict
from pathlib import Path

try:                                                       # the legal notice every generated report carries
    from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
except ImportError:
    import sys as _s, pathlib as _p; _s.path.insert(0, str(_p.Path(__file__).resolve().parents[1])); from tools.legal import stamp as _legal_stamp, TOP as _LEGAL_TOP
ROOT = Path(__file__).resolve().parents[1]
import sys as _sys  # noqa: E402
_sys.path.insert(0, str(ROOT))
from tools import heavy_hitters as HH  # noqa: E402  (heaviest hitters first, the founder's order of 1 November)
CATALOG = ROOT / "realms" / "catalog_v5.csv"
OUT = ROOT / "docs" / "REALM_MUSCLES.md"
REALMS = OrderedDict([("compute_ai_cloud", "Compute / AI / Cloud"), ("physics_robotics_autonomous", "Physics / Robotics / Autonomous"),
                      ("energy_facility_industrial", "Energy / Facility / Industrial"), ("distribution_specialized", "Distribution / Specialized")])
BANNER = f"> {_LEGAL_TOP}"                 # the one notice (tools/legal.py); stamp() keeps one copy of it


def is_spine(r):
    """A spine muscle sits in all four realms (tools/run_realms_v5.py, spine_rows: the same rule the runners use)."""
    return set(REALMS) <= set(r["realms"].split(";"))


def families(rows):
    """The rows grouped by family, in the catalog's family order (family_id)."""
    out = OrderedDict()
    def key(r):                               # family order, then the muscle's id (numbers first, then the audited "AUDIT-nnnn" ids)
        mid = r["muscle_id"]
        return (int(r["family_id"]), (0, int(mid)) if mid.isdigit() else (1, mid))
    for r in sorted(rows, key=key):
        out.setdefault(r["family"], []).append(r)
    return out


def ranked(rows, h, mark_spine=True):
    """A condensed list, heaviest hitter first (tools/heavy_hitters.py): each muscle with its rank, its knob in brackets and,
    for a muscle of the spine listed under its home realm, the mark (spine)."""
    return "; ".join(f"{n} {r['muscle']} [{r['knob']}]" + (" (spine)" if mark_spine and is_spine(r) else "")
                     for n, r in enumerate(HH.order(rows, h), 1)) + "."


def section(fams):
    L = []
    for f, rs in fams.items():
        L += [f"### {f} ({len(rs)}; plant: {rs[0]['template']}, {rs[0]['preset']})",
              ", ".join(f"{r['muscle']} [{r['knob']}]" for r in rs), ""]
    return L


def build(rows):
    spine = [r for r in rows if is_spine(r)]
    in_realm = {k: [r for r in rows if k in r["realms"].split(";")] for k in REALMS}
    own = {k: [r for r in rows if r["realm"] == k and not is_spine(r)] for k in REALMS}
    stack = sum(len(v) for v in in_realm.values())
    L = [f"# The {len(rows):,} muscles, organism by organism", "", BANNER, "",
         f"Generated from `realms/catalog_v5.csv` (the catalog the engine that stands carries: {len(rows):,} distinct muscles in "
         f"{len({r['family'] for r in rows})} families) by `tools/realm_muscles.py`. A **muscle** is one setting on one machine that already has "
         "its own control; the one knob Omni-Compass may hold on it stands in brackets after its name. The catalog builds **seven "
         "organisms**, each run native and with Omni-Compass on top of native: the **spine**, the muscles every real stack runs on, "
         "an organism of its own and the base of the other six (as an operating system is the base of every program; "
         "`docs/THE_SPINE.md`); the four realms, each its own families with the spine under them, so the realm counts add to more "
         "than the tower; the four stacked; and the whole tower. What the engine does with each knob, which native controller owns "
         "it, where the reading is tapped and the setting written, how it is restored and its own card are written family by family "
         "in `docs/MUSCLE_CATALOG.md` (the manuals' muscle appendix); the organisms' results are in `results/realms_v5/REALMS_V5.md` "
         "and the grid in `results/grid_v5/GRID.md`, each named for the engine it ran on.", "",
         "## The seven organisms", "",
         "In the runners the spine is `spine` (organism 7 in `tools/run_scale.py` and the grid conductor, after the six that were "
         "numbered before it); every table lists it first, because the other six stand on it.", "",
         "| Organism | Runner name | Muscles | What it is |", "|---|---|---:|---|",
         f"| The spine | `spine` (7) | {len(spine)} | the muscles every real stack runs on, every one in all four realms: the base of the other six |"]
    for i, (k, name) in enumerate(REALMS.items(), 1):
        L.append(f"| {name} | `{k}` ({i}) | {len(in_realm[k]):,} | its {len(own[k])} own muscles on the spine of {len(spine)} |")
    L += [f"| The four stacked | `stack` (5) | {stack:,} | the four realms' organisms on one clock, every duplicate of the spine kept |",
          f"| The whole tower | `tower` (6) | {len(rows):,} | every muscle of the catalog once |", "",
          f"## The {len(rows):,} muscles in the four realms they live in, heaviest hitter first", "",
          HH.rule_words(), "",
          "Each realm below lists its home muscles, every muscle once, heaviest hitter first and down to its last; a muscle of the "
          "spine (it sits in all four realms) is listed under its home realm and marked (spine). Each name is followed by its rank "
          "in its realm and the one knob Omni-Compass may hold on it, in brackets.", ""]
    h = HH.hits()
    home = HH.by_realm(rows, h)
    for k, name in REALMS.items():
        L += [f"### {name}: {len(home[k])} muscles, heaviest hitter first", "", ranked(home[k], h), ""]
    L += [f"## The spine: {len(spine)} muscles, in all four realms, an organism of its own, heaviest hitter first", "",
          "The thirteen families of the spine are the computers every realm's work runs on and the power and cooling they need: "
          "Kubernetes workloads, containers, placement, node fleets, cloud capacity, hosts, GPUs, network, storage, observability, "
          "reliability and security, electrical distribution and cooling. Run alone, the spine is a data center with nothing of any "
          "one trade in it; under a realm, it is what that realm's own muscles stand on. Its muscles, heaviest hitter first:", "",
          ranked(spine, h, mark_spine=False), ""]
    for i, (k, name) in enumerate(REALMS.items(), 1):
        L += [f"## Organism {i}: {name}: {len(own[k])} own muscles on the spine of {len(spine)} = {len(in_realm[k]):,} in its organism", "",
              f"The spine above, and its {len(own[k])} own muscles (every muscle whose realms include it and that is not the spine's), "
              "heaviest hitter first:", "", ranked(own[k], h, mark_spine=False), ""]
    L += [f"## Organism 5: the four stacked, every duplicate kept, {stack:,} muscles", "",
          "The four realms' organisms above, run on one clock as one body (`stack`; the older name `stack_1226` is read as an alias): "
          f"every muscle listed under organisms 1 to 4, the spine counted once in each, {stack:,} in all.", "",
          f"## Organism 6: the whole tower, all {len(rows):,} muscles once", "",
          "Every muscle of the catalog once (`tower`; the older name `organism_656` is read as an alias): the spine and every realm's own "
          f"families, {len(rows):,} in all.", "",
          f"## Organism 7: the spine, {len(spine)} muscles", "",
          "The spine listed first above, run on its own (`spine`): the same muscles, the same native controllers, nothing of any one "
          "realm on top of them.", ""]
    return L, len(spine)


def main():
    rows = list(csv.DictReader(open(CATALOG, encoding="utf-8")))
    L, spine = build(rows)
    OUT.write_text("\n".join(_legal_stamp(L)) + "\n", encoding="utf-8")
    print(f"{OUT} {len(rows)} muscles, spine {spine}")


if __name__ == "__main__":
    main()
