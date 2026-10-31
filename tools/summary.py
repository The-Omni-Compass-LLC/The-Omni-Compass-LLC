#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The whole summary, right out of the gate (the founder's order of 13 October 2026): what Omni-Compass is, the key to its
words (GAIN, STEADY, LOSS), and every headline result with its word and its evidence class, read from the result files in
this repository. Nothing here is typed in by hand: every number comes from the file named beside it. Standard library only,
so it runs on any Python 3.8 or later straight after a pull.

  python3 tools/summary.py              the summary, as plain text for a terminal
  python3 tools/summary.py --markdown   the same, as Markdown
  python3 tools/summary.py --fix        write the standing block into docs/STATE_OF_PLAY.md
  python3 tools/summary.py --check      fail if that block no longer matches the result files (run by verify.py)
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import NOTICE                                       # noqa: E402  (the notice, written once)
from tools.readings import (OWN_RUNS, GAIN, STEADY, LOSS, GIVEN, key_lines, key_text, gel_of_label, labelled, by_word)  # noqa: E402

WHAT = ("Omni-Compass is a supervisory governor. It always sits on top of a system's own native controller (the Kubernetes "
        "autoscaler, a database's pool, a GPU's firmware, a building's battery controller, a robot's servo) and is never "
        "standalone. It reads every gauge of the system and moves the native controller's own settings, one pedal: push for "
        "more, lift off for less, and lifting hands every setting back toward native. Its first rule is do no harm: the "
        "organism it governs is never left turning out less than native, nor less healthy, and every muscle works only as far "
        "as its own limit (DISCLOSURES.md, section 3); on the engine that stands no gauge may be moved past native away from "
        "its aim, and a setting it cannot improve stays native. Its default brain is "
        "the max: every muscle rides its own limit, never past it and never below native; the energy that takes is shown as "
        "power given, beside the work and the speed it bought. Every benchmark has exactly two arms, native and omni (Omni on "
        "top of native), and every result runs three times (A, B and C).")

CLASSES = ("Evidence classes: P is a physical meter; L is live software, the real thing (a real Kubernetes cluster, a real "
           "database); S is our own models. S is never presented as proof.")

INTERPRETATION_RULE = ("Interpret each muscle against its declared objective: report the actual native/Omni quantities and "
                       "classify each gauge by its own aim. The same work for less energy or fewer billed node-hours is a "
                       "resource GAIN even when throughput is STEADY. Any extra work calculated from that saving at a fixed "
                       "budget is a conditional capacity estimate, not work observed; see docs/OMNI_COMPASS_MANUAL.md and "
                       "tools/benefit_interpretation.py.")

READ_MORE = [("README.md", "the front page, newest result first"),
             ("docs/HOW_TO_READ_THE_RESULTS.md", "how to read every table, the key at its top"),
             ("tools/benefit_interpretation.py", "objective-specific GAIN/STEADY/LOSS and conditional capacity arithmetic"),
             ("docs/OMNI_COMPASS_MANUAL.pdf", "the manual, the key in its front matter"),
             ("results/OMNI_INDEX.md", "the one combined number, test by test"),
             ("docs/BENEFIT_SHEET.md", "one number and one word per benchmark"),
             ("docs/WIRING_VERDICTS.md", "write, watch or the operator's choice, knob by knob"),
             ("results/realms_v5/REALMS_V5.md", "every muscle alone and the seven organisms (modelled)"),
             ("results/grid_v5/GRID.md", "the seven organisms at 1, 10 and 100 copies and runs")]


def load(path):
    p = ROOT / path
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def pct(x, nd=1):
    return "no number" if x is None else f"{x:+.{nd}f}%"


def word_of_pct(x, loss=False):
    if x is None:
        return ""
    if abs(x) < 0.05:
        return STEADY
    return GAIN if x > 0 else (LOSS if loss else GIVEN)


def moved(what, x, unit, nd=3):
    """A measured change in its verb, never a bare sign beside a word: 'misses down 0.145 pp', 'misses up 0.020 pp'."""
    return f"{what} the same" if abs(x) < 0.5 * 10 ** -nd else f"{what} {'down' if x < 0 else 'up'} {abs(x):.{nd}f}{unit}"


def energy_moved(e, nd=3):
    """The energy beside its word: a rise is power given and wears its '+', a fall is a cut."""
    x = 100 * e
    if abs(x) < 0.5 * 10 ** -nd:
        return "energy the same"
    return f"power given +{x:.{nd}f}%" if x > 0 else f"energy cut {abs(x):.{nd}f}%"


def num(x, loss=False, nd=1):
    """The one number wearing its own word's sign (the founder's sign rule, tools/readings.py): GAIN '+', LOSS '−', STEADY '=',
    power given '+'; the raw value stays in the result files."""
    return "no number" if x is None else by_word(x, word_of_pct(x, loss), digits=nd)


def num_word(x, loss=False, nd=1):
    """The number and its word: '+4.3% GAIN', '+0.1% power given', '−2.0% LOSS'."""
    return "no number" if x is None else f"{num(x, loss, nd)} {word_of_pct(x, loss)}"


def evidence(bench: str) -> str:
    """The evidence class of a benefit-sheet row, by what the benchmark is."""
    b = bench.lower()
    if "organisms with the real cluster" in b:
        return "L, the cluster; S, the organism around it"
    if any(w in b for w in ("modelled", "robot arms", "power grids", "buildings and batteries", "drone swarms")):
        return "S"
    return "L"


def engine_line() -> str:
    try:
        from tools import omni_version as ov
        files = ov.engine_files()
        return f"{ov.version_of(files) or 'unversioned'}, fingerprint {ov.digest(files)[:16]} ({len(files)} files)"
    except Exception as e:                                       # the summary never fails for want of the version tool
        return f"unknown ({type(e).__name__})"


def index_part():
    d = load("results/OMNI_INDEX.json")
    if not d:
        return ["The Omni index: not built in this checkout (python3 tools/omni_index.py)."]
    h, s = d.get("headline_pct"), d.get("service_headline_pct")
    sheet = load("results/BENEFIT_SHEET.json") or {}
    eng = next((r.get("engine") for r in sheet.get("rows", []) if r.get("file") == "results/OMNI_INDEX.md"), None) or "the engines named in its tables"
    out = [f"The Omni index (evidence class L, real software on real computers: the software end, not bare metal and not the chip; every measure judged across our three runs; the three-run "
           f"tables of {eng}, each named in its table): {num_word(h, s is not None and s < -0.05)} on the "
           f"resource reading (work, speed, machines, energy), {num_word(s, True)} on the service reading (work and "
           "speed alone). Source: results/OMNI_INDEX.md."]
    for c, v in sorted((d.get("categories") or {}).items(), key=lambda kv: -(kv[1] or 0)):
        sv = (d.get("service_categories") or {}).get(c)
        out.append(f"  {c}: {num_word(v, sv is not None and sv < -0.05)}")
    return out


def benefit_part():
    d = load("results/BENEFIT_SHEET.json")
    if not d:
        return ["The benefit sheet: not built in this checkout (python3 tools/benefit_sheet.py)."]
    out = ["Every benchmark, one number and its word (source: docs/BENEFIT_SHEET.md; class in brackets):"]
    for r in by_engine(d.get("rows", [])):
        n = r.get("pct")
        out.append(f"  {r.get('benefit', '?'):<18} {num(n, bool(r.get('loss'))):>9}  {r['benchmark']} [{evidence(r['benchmark'])}; {r.get('engine', 'engine not named')}]")
    return out


def newest_engine():
    """The engine on this checkout as a name, omni-vN (None where the version tool cannot say)."""
    m = re.match(r"(omni-v\d+)", engine_line())
    return m.group(1) if m else None


def by_engine(rows):
    """The benefit sheet's rows, those on the engine that stands first (their own order kept within each group)."""
    new = newest_engine()
    return [r for r in rows if new and r.get("engine") == new] + [r for r in rows if not (new and r.get("engine") == new)]


def wiring_part():
    p = ROOT / "results" / "WIRING_VERDICTS.csv"
    try:
        rows = list(csv.DictReader(p.open(encoding="utf-8")))
    except OSError:
        return ["The wiring verdicts: not built in this checkout (python3 tools/wiring_verdicts.py)."]
    out = ["Wire in, or watch, knob by knob (source: docs/WIRING_VERDICTS.md; write: Omni holds the knob; watch: the knob stays "
           "native and Omni only reads it; the operator's choice: a trade):"]
    for kind in ("real knob", "modelled simulator", "modelled muscle", "organism with the cluster inside"):
        c = Counter(r["verdict"] for r in rows if r["kind"] == kind and r["counted"] == "yes")
        if c:
            w, ch, wa = c.get("write", 0), c.get("operator's choice", 0), c.get("watch", 0)
            out.append(f"  {kind}: write {w}, the operator's choice {ch}, watch {wa}")
    return out


NAMES = {"spine": "the spine", "compute_ai_cloud": "Compute / AI / Cloud", "physics_robotics_autonomous": "Physics / Robotics / Autonomous",
         "energy_facility_industrial": "Energy / Facility / Industrial", "distribution_specialized": "Distribution / Specialized",
         "stack": "the four stacked", "tower": "the whole tower"}


def realms_part():
    d = load("results/realms_v5/REALMS_V5.json")
    if not d:
        return []
    run = d.get("run", {})
    head = (f"The muscles and the seven organisms on engine {run.get('engine', '?')} at the {run.get('dial', '?')} (evidence class S, "
            f"our own models; run {run.get('started', '?')}, commit {str(run.get('commit', '?'))[:12]}, {run.get('muscles', '?')} "
            "muscles; source: results/realms_v5/REALMS_V5.md):")
    out = [head]
    kinds = Counter(gel_of_label(m.get("label")) or m.get("label") for m in d.get("muscles", []))
    out.append("  every muscle alone, over its loads: " + ", ".join(f"{k} {v}" for k, v in kinds.most_common()))
    for load_, orgs in (d.get("organisms") or {}).items():
        parts = []
        for name, o in orgs.items():
            sm = o.get("summary", {})
            v = sm.get("viol_pp", [None])[0]; e = sm.get("energy", [None])[0]
            nm = NAMES.get(name, name)
            parts.append(f"{nm}: {labelled(o.get('label'))}, {moved('misses', v, ' pp')}, {energy_moved(e)}"
                         if v is not None and e is not None else f"{nm}: {labelled(o.get('label'))}")
        out.append(f"  the organisms under the {load_} load: " + "; ".join(parts))
    return out


def grid_part():
    p = ROOT / "results" / "grid_v5" / "GRID.md"
    try:
        text = p.read_text(encoding="utf-8")
    except OSError:
        return []
    m = re.search(r"^\*\*(Across the grid: .*?)\*\*$", text, re.M)
    return [f"The grid (source: results/grid_v5/GRID.md): {m.group(1)}"] if m else []


def build(markdown=False):
    plain = lambda s: re.sub(r"\*\*|`", "", s) if not markdown else s
    L = [NOTICE if markdown else plain(NOTICE), ""]
    L += ["# Omni-Compass: the whole summary" if markdown else "OMNI-COMPASS: THE WHOLE SUMMARY", ""]
    L += [WHAT, "", CLASSES, "", INTERPRETATION_RULE, "", f"Engine on this checkout: {engine_line()}.", ""]
    L += key_lines() if markdown else key_text().splitlines()
    L += ["", "## The results, each with its word" if markdown else "THE RESULTS, EACH WITH ITS WORD", ""]
    for part in (index_part(), benefit_part(), wiring_part(), realms_part(), grid_part()):
        if part:
            L += part + [""]
    L += ["## Where to read more" if markdown else "WHERE TO READ MORE", ""]
    L += [f"- `{p}`: {w}" if markdown else f"  {p}: {w}" for p, w in READ_MORE]
    L += ["", OWN_RUNS, "", NOTICE if markdown else plain(NOTICE)]
    return "\n".join(L) + "\n"


# ---- the standing block: where things stand, written into the state of play from the result files, so that page never
# quotes a number the result files no longer hold (the founder's orders of 14 October: every push realigns; the manual is
# the wiring and operating manual and carries no results, so the block lives with the results' own front page)
BLOCK_START = "<!-- where things stand (tools/summary.py --fix) -->"
BLOCK_END = "<!-- end of where things stand -->"
BLOCK_PAGES = ("docs/STATE_OF_PLAY.md", "docs/OMNI_COMPASS_OWNERS_MANUAL.md")


def standing_block():
    """The block's Markdown: the engine, the modelled muscles and organisms, the grid, the index and every benchmark's
    one number with its word and class, each read from its own file."""
    L = [BLOCK_START, "",
         "**Where things stand, read from the result files.** Written by `python3 tools/summary.py --fix` from the files it "
         "names; `verify.py` fails a push in which this block no longer matches them. Nothing in it is typed by hand. The live "
         "results run on the engines named in their own tables, and every one of them runs again on the newest engine.", "",
         f"- **The engine on this checkout:** {engine_line()}."]
    rp = realms_part()
    if rp:
        L.append("- " + rp[0])
        L += ["  - " + x.strip() for x in rp[1:]]
    gp = grid_part()
    if gp:
        L.append("- " + gp[0])
    ip = index_part()
    L.append("- " + ip[0])
    L += ["  - " + x.strip() for x in ip[1:]]
    d = load("results/BENEFIT_SHEET.json") or {}
    if d.get("rows"):
        new = newest_engine()
        on_new = [r for r in d["rows"] if new and r.get("engine") == new]
        L += ["", f"**On the engine that stands ({new or 'unknown'}): {len(on_new)} of {len(d['rows'])} benchmarks so far.** "
              "Every other row is that engine's own result, named in its Engine column, and runs again on the engine that stands "
              "(`scripts/reruns.txt`); results are never read across engines.",
              "", "| Benchmark | Engine | Its one number | Its word | Class |", "|---|---|---:|---|---|"]
        for r in by_engine(d["rows"]):
            L.append(f"| {r['benchmark']} | {r.get('engine', 'not named')} | {num(r.get('pct'), bool(r.get('loss')))} | {r.get('benefit', '')} | {evidence(r['benchmark'])} |")
    L += ["", OWN_RUNS, "", BLOCK_END]
    return "\n".join(L)


def fix_pages(check=False):
    """Writes the standing block into every page that carries its markers (check: says which pages are stale)."""
    block, bad = standing_block(), []
    for rel in BLOCK_PAGES:
        p = ROOT / rel
        text = p.read_text(encoding="utf-8")
        a, b = text.find(BLOCK_START), text.find(BLOCK_END)
        if a < 0 or b < 0:
            bad.append(f"{rel}: no standing block (its markers are missing)")
            continue
        new = text[:a] + block + text[b + len(BLOCK_END):]
        if new != text:
            if check:
                bad.append(f"{rel}: the standing block no longer matches the result files (python3 tools/summary.py --fix)")
            else:
                p.write_text(new, encoding="utf-8")
    return bad


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--markdown", action="store_true", help="print Markdown instead of plain text")
    ap.add_argument("--fix", action="store_true", help="write the standing block into docs/STATE_OF_PLAY.md")
    ap.add_argument("--check", action="store_true", help="fail if the standing block in docs/STATE_OF_PLAY.md no longer matches the files")
    a = ap.parse_args(argv)
    if a.fix or a.check:
        bad = fix_pages(check=a.check)
        for b in bad:
            print(b, file=sys.stderr)
        if not bad:
            print("the standing block matches the result files" if a.check else "the standing block written")
        return 1 if bad else 0
    sys.stdout.write(build(markdown=a.markdown))
    return 0


if __name__ == "__main__":
    sys.exit(main())
