# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The source code of Omni-Compass as printed pages, for a copyright registration.

  python3 tools/code_book.py            # writes release/copyright/OMNI_COMPASS_SOURCE_FULL.pdf and ..._DEPOSIT.pdf

FULL: every current source file of the repository (Python, C++, shell, workflows; the archive left out), in reading
order (the engine first, then the controllers, the C++ twins, the realms, tools, scripts, tests, workflows), each file
under its own heading, every page headed with the work's title and version and numbered, a contents list at the front.
DEPOSIT: the title page, then the first 25 and the last 25 pages of source of FULL, the identifying portion the United
States Copyright Office asks for with a computer program (Circular 61). The version is the git commit printed on every
page, so either file can be matched to the repository exactly.
"""
from __future__ import annotations

import datetime, subprocess, sys
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "release" / "copyright"
EXT = (".py", ".cpp", ".hpp", ".h", ".sh", ".yml", ".yaml")
ORDER = ["omnicompass/", "omni_controller/", "cpp/", "fleet/", "realms/", "benchmarks/", "tools/", "scripts/",
         "deploy/", "tests/", ".github/"]
TITLE = "The Omni-Compass: source code"
OWNER = "The Omni-Compass LLC"
W, H = letter
M, FS, LH = 40, 7.0, 8.4                 # margin, font size, line height (points)
COLS = int((W - 2 * M) / (FS * 0.6))     # Courier is 0.6 em wide
ROWS = int((H - 2 * M - 30) / LH)


def files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.split()
    src = [f for f in out if f.endswith(EXT) and not f.startswith("archive/")]
    rank = lambda f: (next((i for i, p in enumerate(ORDER) if f.startswith(p)), len(ORDER)), f)
    return sorted(src, key=rank)


def pages(paths):
    """[(file, [lines of this page])] in print order; long lines wrapped at the column limit."""
    out = []
    for f in paths:
        text = (ROOT / f).read_text(errors="replace").expandtabs(4).splitlines()
        rows = [f"==== {f} ({len(text)} lines) ===="]
        for n, line in enumerate(text, 1):
            body = f"{n:5d}  {line}"
            while len(body) > COLS:
                rows.append(body[:COLS]); body = "       " + body[COLS:]
            rows.append(body)
        for i in range(0, len(rows), ROWS):
            out.append((f, rows[i:i + ROWS]))
    return out


def header(c, version, page, total):
    c.setFont("Helvetica", 7)
    c.drawString(M, H - M + 8, f"{TITLE}. Version {version}. Copyright (c) 2026 {OWNER}. All rights reserved.")
    c.drawRightString(W - M, H - M + 8, f"page {page} of {total}")
    c.drawString(M, M - 18, "Confidential. Evaluation and Simulation use only; any other use requires a signed, paid "
                 "Omni-Compass Enterprise License.")


def title_page(c, version, nfiles, nlines, npages, kind):
    c.setFont("Helvetica-Bold", 20); c.drawString(M, H - 120, TITLE)
    c.setFont("Helvetica", 11)
    lines = [f"Owner and author: {OWNER}", f"Version (git commit): {version}",
             f"Printed: {datetime.date.today().isoformat()}", "",
             f"{kind}", f"{nfiles} source files, {nlines:,} lines, {npages:,} pages of source in the full listing.", "",
             "Languages: Python, C++, shell, YAML (GitHub Actions workflows).",
             "Order: the engine (omnicompass/), the controllers (omni_controller/), the C++ twins (cpp/), the fleet",
             "and realms models, tools, scripts, deployment, tests, workflows.", "",
             f"Copyright (c) 2026 {OWNER}. All rights reserved. Not open source. Any commercial use,",
             "commercialization, monetization, production use, redistribution or hosted service requires a signed,",
             "paid Omni-Compass Enterprise License. Patent applications, copyright registrations and trademark",
             "applications have been filed in the United States by The Omni-Compass LLC / Dubra Software."]
    y = H - 160
    for s in lines:
        c.drawString(M, y, s); y -= 16


def draw(path, pgs, version, nfiles, nlines, kind, contents=None, numbers=None):
    c = canvas.Canvas(str(path), pagesize=letter)
    c.setTitle(TITLE); c.setAuthor(OWNER); c.setSubject(f"version {version}")
    total = len(pgs)
    title_page(c, version, nfiles, nlines, total if numbers is None else numbers[1], kind); c.showPage()
    if contents:
        rows = [f"{p:6d}  {f}" for f, p in contents]
        for i in range(0, len(rows), ROWS):
            c.setFont("Helvetica-Bold", 10); c.drawString(M, H - M - 10, "Contents (page of the source listing)")
            c.setFont("Courier", FS); y = H - M - 30
            for r in rows[i:i + ROWS - 2]:
                c.drawString(M, y, r); y -= LH
            c.showPage()
    for k, (f, rows) in enumerate(pgs):
        page = numbers[0][k] if numbers else k + 1
        header(c, version, page, numbers[1] if numbers else total)
        c.setFont("Courier", FS); y = H - M - 12
        for r in rows:
            c.drawString(M, y, r); y -= LH
        c.showPage()
    c.save()


def main():
    version = subprocess.run(["git", "rev-parse", "--short=12", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
    try:                                                   # the frozen engine it carries, if the bytes match (docs/OMNI_V1.md)
        sys.path.insert(0, str(ROOT / "tools")); import omni_version as ov
        files = ov.engine_files(); v = ov.version_of(files)
        if v:
            version += f", {v} (engine {ov.digest(files)[:16]})"
    except (OSError, ValueError, KeyError, ImportError, AttributeError, subprocess.SubprocessError):
        pass
    paths = files()
    nlines = sum(len((ROOT / f).read_text(errors="replace").splitlines()) for f in paths)
    pgs = pages(paths)
    contents, seen = [], set()
    for i, (f, _) in enumerate(pgs, 1):
        if f not in seen:
            seen.add(f); contents.append((f, i))
    OUT.mkdir(parents=True, exist_ok=True)
    full = OUT / "OMNI_COMPASS_SOURCE_FULL.pdf"
    draw(full, pgs, version, len(paths), nlines, "Complete source listing.", contents=contents)
    n = len(pgs); keep = list(range(min(25, n))) + list(range(max(25, n - 25), n))
    dep = OUT / "OMNI_COMPASS_SOURCE_DEPOSIT.pdf"
    draw(dep, [pgs[i] for i in keep], version, len(paths), nlines,
         "Identifying portion for deposit: the first 25 and the last 25 pages of the source listing.",
         numbers=([i + 1 for i in keep], n))
    print(f"{full.relative_to(ROOT)}: {n} pages of source, {len(paths)} files, {nlines:,} lines, version {version}")
    print(f"{dep.relative_to(ROOT)}: {len(keep)} pages of source (first 25, last 25)")


if __name__ == "__main__":
    sys.exit(main())
