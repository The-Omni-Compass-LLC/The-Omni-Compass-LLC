#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every word a reader meets reads by the one key: run by verify.py on every release, so a push that leaves a published
word out of line fails (the founder's order of 6 November: "go through the top to bottom and confirm every ... file and
document, word, sentence, paragraph ... every claim and everything benchmarkable, defensible receipts").

What it reads: every published Markdown page (the front door, docs/, docs/engine/, docs/book/, docs/specs/, the
summaries at the top of results/), the live engine's word-for-word appendix (docs/engine/PAGE_WORD_FOR_WORD.md), and every
spoken line of the guided tour (the page's "tour" record: what the voice says aloud). What it leaves: the history and the
dated reports and every older engine's own page (docs/OMNI_V<n>.md), which keep the words of their day (docs/history/, any file dated _2026-MM-DD, docs/engine/audit_*/,
CHANGELOG.md); the pre-registrations, whose bytes are locked; the per-run tables under results/<folder>/, which
tools/reread.py reads again from their own data; the founder's rule books, which quote the retired words to retire them
(CLAUDE.md, AGENTS.md, GEMINI.md); and docs/WEBSITE_CLAIMS.md's remove list, which quotes what must come off.

Checks (each finding: file:line, the check, the words):
  even       the retired word EVEN as a reading (the founder's order of 25 October: STEADY)
  sign       a reading word with a bare signed number as its size ("GAIN +4.8%", "-2.3% LOSS"): the word first, then the
             direction in words, never a sign (a raw change is written "raw" beside it)
  direction  a direction word that contradicts its number ("+3.2% fewer", "-5% more", "down +4%", "up -4%")
  fewer      "on fewer machines" said of a result: the composition reads machines 77.7% more, power given; the founder's
             aim may be quoted only as the aim
  repeat     a root of "govern" twice within six words (the founder's order of 6 November: "supervisory" for what
             Omni-Compass does, "governor" for the products it sits on, never the same word twice in one breath)
  stale      a retired figure presented as the headline: the Omni index at 5.0% or 12.9% (omni-v21's readings)

  python3 tools/claims_check.py            (exit 0: every word in line; exit 1: one line per finding)
  python3 tools/claims_check.py --summary  (the count by check and by file)
"""
from __future__ import annotations

import collections
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "docs" / "engine" / "OMNI_COMPASS_LIVE_ENGINE.html"

KEEP_WORDS_OF_THEIR_DAY = (re.compile(r"^docs/history/"), re.compile(r"_20\d\d-\d\d-\d\d"), re.compile(r"^docs/engine/audit_"),
                           re.compile(r"(^|/)CHANGELOG\.md$"), re.compile(r"PREREGISTRATION"), re.compile(r"^results/[^/]+/"),
                           re.compile(r"^(CLAUDE|AGENTS|GEMINI)\.md$"), re.compile(r"^docs/WEBSITE_CLAIMS\.md$"),
                           re.compile(r"^\.github/"), re.compile(r"^docs/omni_v5/"), re.compile(r"^docs/handoff/"),
                           re.compile(r"CONSENSUS_AUDIT"), re.compile(r"^docs/DEVIATIONS\.md$"))

WORD = r"(?:GAIN|LOSS|STEADY|power given)"
NUM = r"[+\-−]\d+(?:\.\d+)?\s?%"
CHECKS = {
    "even": re.compile(r"\bEVEN\b"),
    "sign": re.compile(rf"(?<!raw )(?<!raw: )(?<!raw\s)\b{WORD}\b,?\s{{1,2}}{NUM}|(?<!raw )(?<!raw: ){NUM},?\s{{1,2}}{WORD}\b"),
    "direction": re.compile(r"\+\d+(?:\.\d+)?\s?%\s+(?:fewer|less|shorter|lower)\b|[\-−]\d+(?:\.\d+)?\s?%\s+(?:more|longer|higher)\b"
                            r"|\bdown\s\+\d|\bup\s[\-−]\d"),
    "fewer": re.compile(r"\bon fewer machines\b", re.I),
    "repeat": re.compile(r"\b[Gg]overn\w*\b(?:\W+\w+){0,5}?\W+[Gg]overn\w*\b"),
    "stale": re.compile(r"Omni index[^.\n]{0,80}?\b(?:5\.0|12\.9)\s?%|\b(?:5\.0|12\.9)\s?%[^.\n]{0,40}?Omni index"),
}
# proper names in which the word stands twice by its own right (a section's or a product's own title)
REPEAT_NAMES = re.compile(r"Governor Heartbeat|Self-Governed|governors_page|Orchestrators and Governors")
# the founder's aim may be quoted as the aim: "the aim: more work, faster, on fewer machines"
AIM = re.compile(r"\baim\b|founder's (?:words|aim|line)|\bgoal\b", re.I)


def standing() -> str:
    """The engine that stands (tools/omni_version.py), whose own page is read; every older engine's page keeps the words of its day."""
    sys.path.insert(0, str(ROOT / "tools"))
    import omni_version   # noqa: E402
    return "omni-" + next(iter(omni_version.VERSIONS))   # VERSIONS lists the newest first


def published() -> list[str]:
    files = subprocess.run(["git", "-C", str(ROOT), "ls-files", "*.md"], capture_output=True, text=True, check=True).stdout.split()
    n = re.sub(r"\D", "", standing().split("-v")[-1]) or "25"
    older = re.compile(rf"^docs/OMNI_V(?!{n}\.md$)\d+(_[A-Z0-9_]+)?\.md$")
    return [f for f in files if (not any(p.search(f) for p in KEEP_WORDS_OF_THEIR_DAY) and not older.search(f))
            or f == "docs/engine/PAGE_WORD_FOR_WORD.md"]


def tour_lines() -> list[tuple[str, str]]:
    """Every line the guided tour's voice says aloud, as the page carries it (its "tour" record)."""
    if not PAGE.exists():
        return []
    with PAGE.open(encoding="utf-8") as fh:
        page = fh.read()
    m = re.search(r'<script type="application/json" id="tour">(.*?)</script>', page, re.S)
    if not m:
        return []
    rec = json.loads(m.group(1))
    out = [(f"tour:{s.get('id')}", s.get("say") or "") for s in rec.get("steps", [])]
    if rec.get("nav"):
        out.append(("tour:nav", rec["nav"].get("say") or ""))
    return out


def scan(name: str, text: str, findings: list):
    for n, line in enumerate(text.splitlines(), 1):
        for key, rx in CHECKS.items():
            for m in rx.finditer(line):
                hit = m.group(0)
                if key == "repeat" and REPEAT_NAMES.search(line[max(0, m.start() - 30):m.end() + 30]):
                    continue
                if key == "fewer" and AIM.search(line[max(0, m.start() - 80):m.start()]):
                    continue
                findings.append((name, n, key, line[max(0, m.start() - 60):m.end() + 40].strip()))


def main(argv: list[str]) -> int:
    findings: list = []
    for f in published():
        p = ROOT / f
        if p.exists():
            scan(f, p.read_text(encoding="utf-8", errors="replace"), findings)
    for name, say in tour_lines():
        scan(name, say, findings)
    if "--summary" in argv:
        by_key = collections.Counter(k for _, _, k, _ in findings)
        by_file = collections.Counter(f for f, _, _, _ in findings)
        print("claims: " + (", ".join(f"{k} {v}" for k, v in by_key.most_common()) or "every word in line"))
        for f, v in by_file.most_common(40):
            print(f"  {v:5d}  {f}")
        return 1 if findings else 0
    for f, n, k, s in findings:
        print(f"{f}:{n}: {k}: {s}")
    print(f"claims: {len(findings)} out of line" if findings else "claims: every published word reads by the one key")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
