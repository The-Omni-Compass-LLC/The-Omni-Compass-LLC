# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every zip of Omni-Compass, built one way: from a commit, in parts under an upload limit, each part openable on its own,
and every part carrying the legal papers.

  python3 tools/export_zip.py                     # HEAD, parts of at most 25 MB, into out/export/
  python3 tools/export_zip.py --commit <sha> --limit-mb 20 --out DIR
  python3 tools/export_zip.py --include-raw       # also the archived run files (the branch raw), which are large

Each part holds, at its root, README.md, LICENSE, NOTICE, DISCLOSURES.md, PATENTS.md and TRADEMARKS.md as they stand at
that commit, and EXPORT_NOTICE.txt (the notice, the commit, the part's number and every part's name); the zip's own comment
is the notice, so it shows in any tool that opens the file. The commit is checked against origin/main and the export says
whether it was pushed (the founder's rule: zips are built from a pushed commit)."""
from __future__ import annotations

import argparse
import datetime as dt
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools.legal import BUNDLE, PLAIN  # noqa: E402


def git(*args, binary=False):
    r = subprocess.run(["git", "-c", "safe.directory=*", *args], cwd=ROOT, capture_output=True, check=True)
    return r.stdout if binary else r.stdout.decode()


def files_at(commit: str, include_raw: bool):
    """(path, blob sha, size) of every file at the commit; with include_raw, the raw receipts too: from the commit while main
    carried them, else from the branch raw (scripts/raw_archive.sh fetch), placed under results/live/raw/ as opened."""
    out = []
    for ln in git("ls-tree", "-r", "-l", commit).splitlines():
        meta, path = ln.split("\t", 1)
        mode, kind, sha, size = meta.split()
        if kind != "blob" or (not include_raw and path.startswith("results/live/raw/")):
            continue
        out.append((path, sha, int(size) if size.isdigit() else 0))
    if include_raw and not any(p.startswith("results/live/raw/") for p, _, _ in out):
        for ref in ("refs/remotes/origin/raw", "refs/heads/raw"):
            try:
                listing = git("ls-tree", "-r", "-l", ref)
            except subprocess.CalledProcessError:
                continue
            for ln in listing.splitlines():
                meta, path = ln.split("\t", 1)
                mode, kind, sha, size = meta.split()
                if kind == "blob":
                    out.append(("results/live/raw/" + path, sha, int(size) if size.isdigit() else 0))
            break
    return out


def blob(sha: str) -> bytes:
    return git("cat-file", "blob", sha, binary=True)


def plan_parts(files, limit: int, reserve: int):
    """Files packed into parts by their size (uncompressed, so every part stays under the limit once compressed)."""
    parts, cur, size = [], [], 0
    for f in sorted(files, key=lambda x: x[0]):
        if cur and size + f[2] > limit - reserve:
            parts.append(cur); cur, size = [], 0
        cur.append(f); size += f[2]
    if cur:
        parts.append(cur)
    return parts


def export(commit: str = "HEAD", limit_mb: float = 25.0, out: Path | None = None, include_raw: bool = False) -> list[Path]:
    sha = git("rev-parse", commit).strip()
    try:
        pushed = subprocess.run(["git", "-c", "safe.directory=*", "merge-base", "--is-ancestor", sha, "origin/main"], cwd=ROOT).returncode == 0
    except OSError:
        pushed = False
    files = files_at(sha, include_raw)
    legal = {p: (s, z) for p, s, z in files if p in BUNDLE}
    reserve = sum(z for _, z in legal.values()) + 64 * 1024
    body = [f for f in files if f[0] not in BUNDLE]
    parts = plan_parts(body, int(limit_mb * 1024 * 1024), reserve)
    out = out or ROOT / "out" / "export"
    out.mkdir(parents=True, exist_ok=True)
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    names = [f"omni-compass-{sha[:12]}-part{i + 1:02d}-of-{len(parts):02d}.zip" for i in range(len(parts))]
    written = []
    for i, part in enumerate(parts):
        z = out / names[i]
        notice = (f"{PLAIN}\n\nOmni-Compass export of commit {sha} ({'pushed to main' if pushed else 'NOT on origin/main'}), "
                  f"written {stamp}. Part {i + 1} of {len(parts)}; every part opens on its own and carries the legal papers "
                  f"({', '.join(BUNDLE)}).\nParts: {', '.join(names)}\n")
        with zipfile.ZipFile(z, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            zf.comment = PLAIN.encode("utf-8")[:65000]
            zf.writestr("EXPORT_NOTICE.txt", notice)
            for p, (s, _) in sorted(legal.items()):
                zf.writestr(p, blob(s))
            for p, s, _ in part:
                zf.writestr(p, blob(s))
        written.append(z)
    return written


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--commit", default="HEAD")
    ap.add_argument("--limit-mb", type=float, default=25.0)
    ap.add_argument("--out", type=Path)
    ap.add_argument("--include-raw", action="store_true")
    a = ap.parse_args(argv)
    for z in export(a.commit, a.limit_mb, a.out, a.include_raw):
        print(f"{z}  {z.stat().st_size / 1e6:.1f} MB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
