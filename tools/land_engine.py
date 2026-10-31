#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Land the next engine version in every place that names the engine that stands, in one command, and check that none is left behind.

  python3 tools/land_engine.py v12 --since 2026-10-19T09:00:00Z   once the engine files are final, tested and through the model gate
  python3 tools/land_engine.py --check                            every place names the newest engine (verify.py runs it)

The founder's order of 18 October: the engine keeps being tuned, version after version (v11, v20, v30 ...), each one a step that
leaves everything intact and moves only what moved, until the final organism. A landing is two kinds of work.

The bookkeeping is the same every time and is done here: the fingerprint (OMNI_VN.json) and the version list
(tools/omni_version.py); the conductor's campaign (scripts/dispatch_grid.py: the grid's manifest, the engine, the moment the
campaign starts for the grid, the reruns and the clouds); the new grid manifest (results/grid_vN/DISPATCHED.json) and the
three grid workflows' checkouts; the reruns queue's header; the package (0.N.0 in pyproject.toml and codemeta.json); the root
file list (tools/layout_check.py); a release group for the version (tools/release_manifest.py, which the person extends with
the files the version changed); and the catalog's and the index's lines that name the engine.

The words are written by a person, because they say what changed and why: docs/OMNI_VN.md, the README, the state of play,
CLAUDE.md, the CHANGELOG, both manuals, the receipts and the live benchmark engine's page. --check reads every one of them and names any
that still calls an older engine the one that stands. Nothing else moves: every earlier fingerprint, table and result stays
where it is, as that engine's record.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# (file, pattern): every capture group is the number of the engine that stands
BOOKKEEPING = [
    ("scripts/dispatch_grid.py", r'"results" / "grid_v(\d+)"'),
    ("scripts/dispatch_grid.py", r'ENGINE = "omni-v(\d+)"'),
    ("scripts/dispatch_grid.py", r'\bSINCE = "[^"]+"\s+# only this campaign, omni-v(\d+)'),
    ("scripts/dispatch_grid.py", r'RERUN_SINCE = "[^"]+"\s+# omni-v(\d+):'),
    ("scripts/dispatch_grid.py", r'AZURE_SINCE = "[^"]+"\s+# omni-v(\d+):'),
    ("scripts/dispatch_grid.py", r'counted in no v(\d+) table'),
    ("scripts/reruns.txt", r'The omni-v(\d+) campaign'),
    ("scripts/reruns.txt", r'the moment omni-v(\d+) landed'),
    (".github/workflows/grid.yml", r'results/grid_v(\d+)'),
    (".github/workflows/six.yml", r'results/grid_v(\d+)'),
    (".github/workflows/six-kube.yml", r'results/grid_v(\d+)'),
    ("pyproject.toml", r'(?m)^version = "0\.(\d+)\.0"'),
    ("codemeta.json", r'"version": "0\.(\d+)\.0"'),
    ("codemeta.json", r'"softwareVersion": "0\.(\d+)\.0 \(engine omni-v(\d+)\)"'),
    ("tools/muscle_catalog.py", r'the engine that stands, omni-v(\d+), carries'),
    ("tools/omni_index.py", r'the omni-v(\d+) Azure sets run'),
    ("tools/omni_index.py", r'join when their omni-v(\d+) runs land'),
    ("tools/omni_version.py", r'VERSIONS = \{"v(\d+)": ROOT / "OMNI_V(\d+)\.json"'),
    ("tools/omni_version.py", r'prints "omni-v(\d+)",'),
    ("tools/omni_version.py", r'Omni v(\d+), the engine that stands \(OMNI_V(\d+)\.json, docs/OMNI_V(\d+)\.md\)'),
]
# the words a person writes: each pattern names the engine that stands on a standing page
WORDS = [
    ("README.md", r'\*\*Engine on main:\*\* omni-v(\d+)'),
    ("README.md", r'The engine on main is \*\*omni-v(\d+)\*\*'),
    ("README.md", r'## The engine that stands: omni-v(\d+)'),
    ("CLAUDE.md", r'## The engine: Omni v(\d+) stands'),
    ("docs/OMNI_COMPASS_MANUAL.md", r'The engine that stands in this edition is \*\*omni-v(\d+)\*\*'),
    ("docs/OMNI_COMPASS_MANUAL.md", r'prints `omni-v(\d+) \(digest'),
    ("docs/engine/OMNI_COMPASS_LIVE_ENGINE.html", r'<html[^>]*data-engine="omni-v(\d+)"'),
    # 27 October 2026: each of these still held an older engine's number two and three versions on, unseen by this check
    ("README.md", r'The engine that stands\s+is omni-v(\d+) \(`OMNI_V(\d+)\.json`'),
    ("README.md", r"The released factory profile is omni-v(\d+)'s"),
    ("docs/FACTORY_PROFILE.md", r"The released factory profile is omni-v(\d+)'s \(`OMNI_V(\d+)\.json`"),
    ("docs/OMNI_COMPASS_OWNERS_MANUAL.md", r"The released factory profile is omni-v(\d+)'s \(`OMNI_V(\d+)\.json`"),
    ("docs/OMNI_COMPASS_OWNERS_MANUAL.md", r"The engine that stands is \*\*omni-v(\d+)\*\* \(`OMNI_V(\d+)\.json`"),
    ("docs/OMNI_COMPASS_OWNERS_MANUAL.md", r"for this edition, `omni-v(\d+) \(digest"),
    ("docs/STATE_OF_PLAY.md", r"## The engine that stands\s+\*\*omni-v(\d+)\*\* \(`OMNI_V(\d+)\.json`"),    ("docs/engine/OMNI_COMPASS_LIVE_ENGINE.html", r"The engine that stands is omni-v(\d+) \(<code>docs/OMNI_V(\d+)\.md</code>\)"),    ("docs/engine/APPRAISAL.md", r"\*\*Engine\.\*\* The engine that stands is \*\*omni-v(\d+)\*\* \(`OMNI_V(\d+)\.json`"),    ("docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md", r"\(omni-v(\d+), `OMNI_V(\d+)\.json`\)\. The page names its engine"),
    ("docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md", r"It covers the page as built on omni-v(\d+);"),
    ("docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md", r"### 3\.2 The sections, as built on omni-v(\d+)"),
    ("docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md", r"the page stands on \(omni-v(\d+)\)\."),
    ("docs/OMNI_COMPASS_MANUAL.md", r"quoted here ran on omni-v7, whose rules omni-v(\d+) carries"),
]
SINCE_RE = r'((?:\bSINCE|RERUN_SINCE|AZURE_SINCE) = ")[^"]+(")'


def newest(root: Path = ROOT) -> int:
    """The engine that stands: the first entry of tools/omni_version.py's version list."""
    m = re.search(r'VERSIONS = \{"v(\d+)"', (root / "tools" / "omni_version.py").read_text())
    return int(m.group(1))


def check(root: Path = ROOT) -> list[str]:
    """Every place that is not on the engine that stands, in words."""
    n = newest(root)
    bad = []
    for path, pat in BOOKKEEPING + WORDS:
        p = root / path
        if not p.exists():
            bad.append(f"{path}: missing"); continue
        hits = list(re.finditer(pat, p.read_text()))
        if not hits:
            bad.append(f"{path}: no line names the engine that stands ({pat})")
        for m in hits:
            if any(int(g) != n for g in m.groups()):
                bad.append(f"{path}: names omni-v{next(g for g in m.groups() if int(g) != n)} where the engine that stands is omni-v{n}")
    for path in (f"OMNI_V{n}.json", f"docs/OMNI_V{n}.md", f"results/grid_v{n}/DISPATCHED.json"):
        if not (root / path).exists():
            bad.append(f"{path}: missing")
    man = root / f"results/grid_v{n}/DISPATCHED.json"
    if man.exists() and json.loads(man.read_text()).get("engine") != f"omni-v{n}":
        bad.append(f"{man.relative_to(root)}: its engine is not omni-v{n}")
    if f'"OMNI_V{n}.json"' not in (root / "tools" / "layout_check.py").read_text():
        bad.append(f"tools/layout_check.py: OMNI_V{n}.json is not in the root file list")
    if f'"engine_v{n}' not in (root / "tools" / "release_manifest.py").read_text():
        bad.append(f"tools/release_manifest.py: no release group for omni-v{n}")
    return bad


def land(n: int, since: str, root: Path = ROOT, fingerprint: bool = True) -> None:
    old = newest(root)
    if n != old + 1:
        sys.exit(f"the engine that stands is omni-v{old}; the next is v{old + 1}, not v{n}")
    if not re.fullmatch(r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ", since):
        sys.exit("--since takes the moment the version lands on main, in UTC: 2026-10-19T09:00:00Z")
    ver = root / "tools" / "omni_version.py"
    s = ver.read_text()
    s = s.replace('VERSIONS = {', f'VERSIONS = {{"v{n}": ROOT / "OMNI_V{n}.json", ', 1)
    s = s.replace(f'prints "omni-v{old}",', f'prints "omni-v{n}", "omni-v{old}",', 1)
    s = re.sub(rf'Omni v{old}, the engine that stands \(OMNI_V{old}\.json, docs/OMNI_V{old}\.md\), ',
               f'Omni v{n}, the engine that stands (OMNI_V{n}.json, docs/OMNI_V{n}.md), Omni v{old} (OMNI_V{old}.json), ', s, count=1)
    ver.write_text(s)
    for path, pat in BOOKKEEPING:
        if path == "tools/omni_version.py":
            continue
        p = root / path
        text = p.read_text()

        def bump(m):
            out, last = [], m.start()
            for i in range(1, (m.lastindex or 0) + 1):
                out += [text[last:m.start(i)], str(n)]; last = m.end(i)
            return "".join(out) + text[last:m.end()]
        text = re.sub(pat, bump, text)
        if path == "scripts/dispatch_grid.py":
            text = re.sub(SINCE_RE, rf'\g<1>{since}\g<2>', text)
        p.write_text(text)
    lay = root / "tools" / "layout_check.py"
    lay.write_text(lay.read_text().replace(f'"OMNI_V{old}.json",', f'"OMNI_V{old}.json", "OMNI_V{n}.json",', 1))
    rel = root / "tools" / "release_manifest.py"
    s = rel.read_text()
    anchor = re.search(rf'\n(\s*)"engine_v{old}', s)
    s = s[:anchor.start()] + (f'\n{anchor.group(1)}"engine_v{n}": ["OMNI_V{n}.json", "tools/omni_version.py", "docs/OMNI_V{n}.md"],'
                              f'   # extend with the files omni-v{n} changed') + s[anchor.start():]
    rel.write_text(s)
    grid = root / "results" / f"grid_v{n}"; grid.mkdir(parents=True, exist_ok=True)
    (grid / "DISPATCHED.json").write_text(json.dumps({"engine": f"omni-v{n}", "dispatches": []}, indent=2) + "\n")
    if fingerprint:                          # the fingerprint of the engine files as they stand now
        subprocess.run([sys.executable, str(ver), "--write", f"v{n}"], cwd=root, check=True)
    print(f"omni-v{n} landed in the bookkeeping; the campaign starts at {since}. The words a person writes next:")
    for w in [f"docs/OMNI_V{n}.md (new)", "README.md", "docs/STATE_OF_PLAY.md", "CLAUDE.md", "CHANGELOG.md",
              "docs/OMNI_COMPASS_MANUAL.md, docs/OMNI_COMPASS_OWNERS_MANUAL.md and docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md (then docs/book/build_book.py, all three)",
              "docs/THE_RECEIPTS.md", "docs/engine/OMNI_COMPASS_LIVE_ENGINE.html and docs/engine/APPRAISAL.md",
              f"docs/OMNI_V{old}.md (it stood until today)", f"results/model_gate/V{n}_VS_V{old}.md (tools/model_gate.py)"]:
        print("  " + w)
    for b in check(root):
        print("  still to do: " + b)


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args[:1] == ["--check"]:
        bad = check()
        for b in bad:
            print(b)
        print(f"every place names omni-v{newest()}, the engine that stands" if not bad else f"{len(bad)} places are not on omni-v{newest()}")
        return 1 if bad else 0
    if len(args) == 3 and re.fullmatch(r"v\d+", args[0]) and args[1] == "--since":
        land(int(args[0][1:]), args[2]); return 0
    print(__doc__.split("\n\n")[1] if "\n\n" in __doc__ else __doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
