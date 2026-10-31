#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every three-run table read again by the rule that stands (tools/readings.py three_run_reading), from its own data.

The founder's order of 24 October 2026: a change of 0.5% or more either way is a change, and reads GAIN, LOSS or power given by
what the gauge is for; STEADY is kept for a change under 0.5%. Each table's JSON holds every run's paired values for every gauge
(native, Omni-Compass, the difference and its 95% interval), so every reading is read again from them, never typed in:

  JSON tables  (results/live and results/orchestrator, V<n>_*.json): every gauge that carries its aim and its three runs is read
               again; the Markdown twin's row for it is rewritten in place (its reading, and in the kind tables each run's number
               beside that run's own word), the tallies under the table are counted again, and a note under the title says the
               table was read again and by which rule. The numbers themselves never change.
  Markdown-only tables  (the deterministic simulators: CityLearn, pandapower, MuJoCo, the swarms): a row that reads GAIN, LOSS
               or power given in all three runs whose runs' mean change is under 0.5% reads STEADY, under the floor.

A gauge read from single pairs (one pair a run, no interval: the 24-hour robustness run) keeps its reading: no noise can be
judged there. A row whose reading is a receipt of its own kind (the robustness test's hand-back facts) is not a gauge and
keeps its words.

  python3 tools/reread.py            read every table again and write it
  python3 tools/reread.py --check    exit 1 when any table's readings differ from the rule that stands
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.readings import (EVEN_FLOOR, SIZE_FLOOR, Tally, reading_kind, run_word, three_run_reading)  # noqa: E402

DIRS = (ROOT / "results" / "live", ROOT / "results" / "orchestrator")
NOTE = ("> **Read again on 24 October 2026 by the rule that stands** (`tools/reread.py`, `tools/readings.py`): a change of 0.5% or "
        "more, the mean of the three runs, is a change and reads GAIN, LOSS or power given by what the gauge is for; STEADY is kept for "
        "a change under 0.5%. Where every run moved the same way, clear of zero, the word reads in all three of our runs; otherwise "
        "by the mean of our three runs, with the count of runs that stood beyond the noise. The numbers are the runs' own; only the "
        "words were read again, and this rule replaces the one the text below describes.")
NOTE_START = "> **Read again on "
STACKS = {"REDIS": "run_redis", "KAFKA": "run_kafka", "PGBENCH": "run_pgbench", "SYSBENCH": "run_sysbench", "YCSB": "run_ycsb",
          "CPU_POWER": "run_cpu_power"}
TALLY_RE = re.compile(r"^\*\*Across \d+ .* where the runs disagree\.\*\*$")
READINGS_RE = re.compile(r"^Readings: .*\.$")


def gauges(data):
    """(path, gauge) for every gauge the table holds, in the order its Markdown twin prints them."""
    out = []
    for k, g in (data.get("rows") or {}).items():
        if isinstance(g, dict) and "reading" in g:
            out.append((("rows", k), g))
    for wl, gs in (data.get("workloads") or {}).items():
        for k, g in (gs or {}).items():
            if isinstance(g, dict) and "reading" in g:
                out.append((("workloads", wl, k), g))
    return out


def readable(g):
    """True when the gauge carries what the rule reads: its aim and three runs each with native and its difference, and at least
    one run with an interval (single pairs keep their reading)."""
    rs = g.get("runs")
    if not g.get("aim") or not isinstance(rs, list) or len(rs) != 3 or any(not isinstance(r, dict) for r in rs):
        return False
    if any(r.get("native") is None or r.get("diff") is None for r in rs):
        return False
    ci = [r.get("ci95") or [] for r in rs]
    finite = [len(c) == 2 and all(isinstance(x, (int, float)) and x == x for x in c) for c in ci]
    return any(finite)          # a run with no interval (one pair) stands inside its noise (tools/readings.py significant)


def bare(s):
    return (s or "").strip().strip("*").strip()


def reread_json(path):
    """(changes, new data, the gauges read again in order as (old, new, gauge)) for one JSON table."""
    data = json.loads(path.read_text())
    seq, n = [], 0
    for _, g in gauges(data):
        old = g["reading"]
        if readable(g):
            new = bare(three_run_reading(g["runs"], g["aim"]))
            if bare(old) != new:
                n += 1
            g["reading"] = new
        seq.append((old, g["reading"], g))
    return n, data, seq


def cells(line):
    return line.strip().strip("|").split("|")


def kind_cell(r, w):
    from tools.confirm_abc import cell
    return cell(r, w)


def patch_md(md, seq, kind):
    """The Markdown twin with every gauge row's reading rewritten, matched in order by its old reading."""
    lines, i = md.split("\n"), 0
    for old, new, g in seq:
        while i < len(lines):
            ln = lines[i]
            i += 1
            if ln.startswith("|") and not ln.startswith("|---") and bare(cells(ln)[-1]) == bare(old):
                cs = cells(ln)
                cs[-1] = f" {new if new.startswith(('STEADY', 'shown', 'no value')) else '**' + new + '**'} "
                if kind and readable(g) and len(cs) == 5:
                    cs[1:4] = [f" {kind_cell(r, run_word(r, g['aim']))} " for r in g["runs"]]
                elif kind and readable(g) and len(cs) == 6:      # the capacity test's rows: the cap, then the measure
                    cs[2:5] = [f" {kind_cell(r, run_word(r, g['aim']))} " for r in g["runs"]]
                elif kind == "store" and len(cs) == 7 and isinstance(g.get("runs"), list) and len(g["runs"]) == 3 \
                        and all(isinstance(r, dict) and r.get("native") is not None and r.get("diff") is not None for r in g["runs"]):
                    cs[3:6] = [f" {kind_cell(r, run_word(r, g['aim']) if g.get('aim') else None)} " for r in g["runs"]]   # a data store's rows: native → Omni-Compass on every run
                lines[i - 1] = "|" + "|".join(cs) + "|"
                break
    return "\n".join(lines)


def with_note(md):
    """The table with the note under its title block, once: an earlier note and the blank line after it are taken out first."""
    lines, out, skip = md.split("\n"), [], False
    for ln in lines:
        if ln.startswith(NOTE_START):
            skip = True
            continue
        if skip and ln == "":
            skip = False
            continue
        skip = False
        out.append(ln)
    at = next((j for j, ln in enumerate(out) if ln.startswith("Run and scored by")), None)
    if at is None:
        at = next((j for j, ln in enumerate(out) if ln.startswith("# ")), 0)
    out[at + 1:at + 1] = ["", NOTE]
    return "\n".join(out)


def retally(md, data, stack):
    """The counts under the table, counted again from the readings now in the data."""
    lines = md.split("\n")
    if data.get("rows"):
        c = Counter(reading_kind(g["reading"]) for _, g in gauges(data))
        new = "Readings: " + ", ".join(f"{n} {v}" for v, n in sorted(c.items())) + "."
        lines = [new if READINGS_RE.match(ln) else ln for ln in lines]
    if stack:
        mod = __import__(f"tools.{stack}", fromlist=["GAUGES"])
        dirs = {k: dr for k, _, dr in mod.GAUGES}
        t, n_wl = Tally(), 0
        for wl, gs in (data.get("workloads") or {}).items():
            if wl == "tuning":
                continue
            n_wl += 1
            for k, g in gs.items():
                t.add(g["reading"], dirs.get(k, g.get("aim")), k)
        for j, ln in enumerate(lines):
            if TALLY_RE.match(ln):
                what = re.match(r"^\*\*Across \d+ (.*?): ", ln).group(1)
                lines[j] = t.sentence(n_wl, what)
    return "\n".join(lines)


def md_only(path):
    """A deterministic simulator's Markdown table: a row read GAIN, LOSS or power given in all three runs whose runs' mean change
    is under 0.5% reads STEADY, under the floor. Returns (changes, new text)."""
    text, n, out = path.read_text(), 0, []
    pct = re.compile(r"^\s*([+−-])(\d+(?:\.\d+)?)%")
    for ln in text.split("\n"):
        if ln.startswith("|") and not ln.startswith("|---"):
            cs = cells(ln)
            r = bare(cs[-1])
            if re.match(r"^(GAIN|LOSS|power given) in all three of our runs$", r):
                vals = [pct.match(c) for c in cs[1:-1]]
                vals = [(-1 if m.group(1) in "−-" else 1) * float(m.group(2)) for m in vals if m]
                if len(vals) >= 3:
                    mean = sum(vals[-3:]) / 3
                    if abs(mean) < 100 * SIZE_FLOOR:
                        cs[-1] = f" {EVEN_FLOOR} (the three runs' mean {abs(mean):.2f}%) "
                        ln = "|" + "|".join(cs) + "|"
                        n += 1
        out.append(ln)
    return n, "\n".join(out)


def reread_pair(p: Path, write: bool = True):
    """One table (its .json and .md) read again by the rule that stands, as main() reads every table: returns (readings
    changed, whether the page's text changed). tools/reproduce.py applies it to a table it rebuilds, so a rebuilt table is
    compared with the published one as both stand under the same rule."""
    n, data, seq = reread_json(p)
    md = p.with_suffix(".md")
    if not md.exists():
        return n, False
    text = md.read_text()
    kind = "| Measure | A | B | C | Reading |" in text or ("store" if "| native (A) | omni (A) | A | B | C | Reading |" in text else False)
    stack = next((m for s, m in STACKS.items() if re.search(rf"_{s}(_|\.json$)", p.name)), None)
    new_text = retally(with_note(patch_md(text, seq, kind)), data, stack) if seq else text
    if write and (n or new_text != text):
        p.write_text(json.dumps(data, indent=1) + "\n")
        md.write_text(new_text if new_text.endswith("\n") else new_text + "\n")
    return n, new_text != text


def main(argv):
    check, total, tables = "--check" in argv, 0, 0
    for d in DIRS:
        for p in sorted(d.glob("V*_*.json")):
            md = p.with_suffix(".md")
            if isinstance(json.loads(p.read_text()).get("rows"), list):   # the three arms' table: its own writer reads it again
                from tools import orchestrator_abc
                before = (p.read_text(), md.read_text() if md.exists() else "")
                n = orchestrator_abc.reread(p)
                changed = before != (p.read_text(), md.read_text() if md.exists() else "")
                if check and changed:
                    p.write_text(before[0]); md.write_text(before[1])
                tables += changed
                total += n
                continue
            n, changed = reread_pair(p, write=not check)
            if n or changed:
                tables += 1
                total += n
        for md in sorted(d.glob("V*_*.md")):
            if md.with_suffix(".json").exists():
                continue
            n, new_text = md_only(md)
            if n:
                tables += 1
                total += n
                if not check:
                    md.write_text(with_note(new_text))
    print(f"reread: {total} readings {'differ from' if check else 'read again by'} the rule that stands, in {tables} tables")
    return 1 if check and (total or tables) else 0      # a page whose text would change fails too, readings or not


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
