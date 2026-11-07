# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The report card's counts, computed from the repository at the commit it is run on (docs/REPORT_CARD.md, section 1).

Every count in the report card's first section is computed here, never typed: the engine's fingerprint, the tests, the
checks, the tables by engine, the model gate's pages, the figures, the pages, the manuals' page counts, the legal notice, the
catalog, the benefit board and the LOSS ledger. A grading names its commit; the counts are true at that commit.

    python3 tools/report_card.py            print the counts as the report card's table
    python3 tools/report_card.py --write    write them between the report card's markers
"""
from __future__ import annotations

import argparse
import collections
import contextlib
import io
import json
import re
import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
CARD = ROOT / "docs" / "REPORT_CARD.md"
BEGIN = "<!-- the repository in numbers (tools/report_card.py) -->"
END = "<!-- end of the repository in numbers -->"
MANUALS = (("the Operator's", "docs/OMNI_COMPASS_MANUAL.pdf"), ("the Owner's", "docs/OMNI_COMPASS_OWNERS_MANUAL.pdf"),
           ("the Live Engine", "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.pdf"))


def standing() -> tuple[str, dict]:
    """The engine that stands (the newest fingerprint) and its file map."""
    fps = sorted(ROOT.glob("OMNI_V*.json"), key=lambda f: int(re.sub(r"\D", "", f.stem)))
    d = json.loads(fps[-1].read_text(encoding="utf-8"))
    files = d.get("files") or {}
    files = files if isinstance(files, dict) else {x["path"]: x.get("sha256") for x in files}
    return "omni-v" + re.sub(r"\D", "", fps[-1].stem), files


def unit_cases() -> int:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
        return unittest.defaultTestLoader.discover(str(ROOT / "tests"), top_level_dir=str(ROOT)).countTestCases()


def pdf_pages(path: Path) -> str:
    if not path.exists() or not shutil.which("pdfinfo"):
        return "not read"
    out = subprocess.run(["pdfinfo", str(path)], capture_output=True, text=True).stdout
    m = re.search(r"^Pages:\s+(\d+)", out, re.M)
    return f"{int(m.group(1)):,}" if m else "not read"


def counts() -> list[tuple[str, str]]:
    eng, files = standing()
    n = int(eng.split("-v")[1])
    prev = ROOT / f"OMNI_V{n - 1}.json"
    same = ""
    if prev.exists():
        p = json.loads(prev.read_text(encoding="utf-8")).get("files") or {}
        p = p if isinstance(p, dict) else {x["path"]: x.get("sha256") for x in p}
        same = f", {sum(1 for k, v in files.items() if p.get(k) == v)} of them omni-v{n - 1}'s bytes"
    receipt = (ROOT / "results" / "VERIFY_RECEIPT.txt").read_text(encoding="utf-8")
    at = re.search(r"at commit ([0-9a-f]{12})", receipt)
    passed, failed = len(re.findall(r"^PASS", receipt, re.M)), len(re.findall(r"^FAIL", receipt, re.M))
    tables = collections.Counter(re.match(r"V(\d+)_", f.name).group(1) for f in (ROOT / "results" / "live").glob("V*_*.md")
                                 if re.match(r"V\d+_", f.name))
    newest = sorted(tables, key=int)[-1]
    rows = json.loads((ROOT / "results" / "BENEFIT_SHEET.json").read_text(encoding="utf-8"))["rows"]
    by_eng = collections.Counter(r["engine"] for r in rows)
    led = (ROOT / "docs" / "LOSS_LEDGER.md").read_text(encoding="utf-8")
    sec = led.split("## Against my own native", 1)[1].split("\n## ", 1)[0]
    loss = collections.Counter(); nocause = collections.Counter()
    for ln in sec.splitlines():
        if ln.startswith("| omni-v"):
            c = [x.strip() for x in ln.strip().strip("|").split("|")]
            loss[c[0]] += 1
            if not c[4] or re.search(r"not yet|none written|no cause", c[4], re.I):
                nocause[c[0]] += 1
    from tools import organism_words as OW
    mus = OW.muscles()
    import csv
    cat = ROOT / "realms" / "catalog_v5.csv"
    fams = len({r.get("family") for r in csv.DictReader(cat.open(encoding="utf-8"))}) if cat.exists() else None
    legal = subprocess.run([sys.executable, str(ROOT / "tools" / "legal.py"), "--check"], cwd=ROOT, capture_output=True, text=True).stdout
    lm = re.search(r"(\d[\d,]*) files carry it", legal)
    func = subprocess.run([sys.executable, str(ROOT / "tools" / "function_tests.py"), "--list"], cwd=ROOT, capture_output=True,
                          text=True).stdout
    out = [
        (f"Engine files in the fingerprint ({eng})", f"{len(files)}{same}"),
        ("Unit test cases collected under `tests/`", f"{unit_cases():,}"),
        ("Function-test files (`tools/function_tests.py --list`)", str(len([x for x in func.splitlines() if "tests/" in x]))),
        ("C++ parity test files (the sealed twins)", str(len([f for f in (ROOT / "tests").glob("test_cpp_*.py") if "parity" in f.name]))),
        (f"Checks in `verify.py --quick` at the receipt's commit ({at.group(1) if at else 'not named'})", f"{passed} PASS, {failed} FAIL"),
        ("GitHub workflows (`.github/workflows/`)", str(len(list((ROOT / ".github" / "workflows").glob("*.y*ml"))))),
        ("Three-run tables in `results/live/`, all engines", f"{sum(tables.values()):,}"),
        ("Of them, by engine, newest first", "; ".join(f"omni-v{k}: {tables[k]}" for k in sorted(tables, key=int, reverse=True)[:5])),
        (f"Three-run tables on the engine that stands ({eng})", str(tables.get(str(n), 0)) +
         ("" if tables.get(str(n)) else f" (the newest are omni-v{newest}'s)")),
        ("Model gate pages (`results/model_gate/`)", str(len(list((ROOT / "results" / "model_gate").glob("*.md"))))),
        ("Pages in `docs/` (top level), preregistrations, engine pages, history pages",
         ", ".join(str(x) for x in (len(list((ROOT / "docs").glob("*.md"))), len(list((ROOT / "docs").glob("*PREREGISTRATION*.md"))),
                                     len(list((ROOT / "docs").glob("OMNI_V*.md"))), len(list((ROOT / "docs" / "history").glob("*.md")))))),
        ("Drawn figures (`docs/book/figures/`)", str(len(list((ROOT / "docs" / "book" / "figures").glob("*.svg"))))),
        ("The Operator's, Owner's and Live Engine Manuals (PDF pages)", ", ".join(pdf_pages(ROOT / p) for _, p in MANUALS)),
        ("Files carrying the legal notice (`tools/legal.py --check`)", f"{int(lm.group(1).replace(',', '')):,}" if lm else "not read"),
        ("Muscles in the catalog, in our own models: GAIN, STEADY, LOSS",
         f"{mus['total']:,}: {mus['gain']}, {mus['limit'] + mus['same']}, {mus['loss']}" + (f" ({fams} families)" if fams else "")),
        ("Benchmarks on the benefit board, by the engine of their newest table",
         f"{len(rows)}: " + ", ".join(f"{k} {v}" for k, v in sorted(by_eng.items(), key=lambda t: -int(t[0].split('-v')[1])))),
        ("LOSS rows against Omni-Compass's own native (the ledger), by engine; of them without a cause written",
         "; ".join(f"{k}: {v}, {nocause.get(k, 0)} without" for k, v in sorted(loss.items(), key=lambda t: -int(t[0].split('-v')[1])))),
    ]
    return out


def table() -> list[str]:
    return ["| Piece | Count |", "|---|---:|"] + [f"| {a} | {b} |" for a, b in counts()]


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--write", action="store_true")
    a = ap.parse_args(argv)
    t = table()
    if not a.write:
        print("\n".join(t))
        return 0
    s = CARD.read_text(encoding="utf-8")
    i, j = s.find(BEGIN), s.find(END)
    if i < 0 or j < i:
        print("the report card carries no markers for its counts")
        return 1
    CARD.write_text(s[:i] + "\n".join([BEGIN] + t + [END]) + s[j + len(END):], encoding="utf-8")
    print("the report card's counts written from the repository")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
