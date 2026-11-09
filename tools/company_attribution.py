# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; commercial use requires a signed, paid Enterprise License.
# See LICENSE, NOTICE and DISCLOSURES.md.
"""Check publisher attribution in active, editable repository publications.

Canonical: Dubra Software Inc. / The Omni-Compass LLC.

    python3 tools/company_attribution.py --check
    python3 tools/company_attribution.py --fix
    python3 tools/company_attribution.py --inventory

--check and --fix cover editable top-level publications and manuals, not immutable
experiment records, engine-fingerprinted sources, archived version notes or binaries.
--inventory searches all tracked UTF-8 text but never writes it, and reports remaining
standalone names for human review; historical data must retain its original bytes.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CANONICAL = "Dubra Software Inc. / The Omni-Compass LLC"
# The negative lookbehind makes normalization idempotent.
STANDALONE = re.compile(
    r"(?<!Dubra Software Inc\. / )The Omni-Compass LLC"
    r"|(?<!Dubra Software Inc\. / )(?:The )?Omni Compass LLC"
)
VERSIONED = re.compile(r"OMNI_V\d+\.md$")
ROOT_PUBLICATIONS = (
    "LICENSE", "NOTICE", "CITATION.cff", "codemeta.json", "pyproject.toml",
)


def active_paths(root: Path = ROOT):
    result = set()
    for item in root.glob("*.md"):
        result.add(item)
    for item in (root / "docs").glob("*.md"):
        if not VERSIONED.fullmatch(item.name):
            result.add(item)
    for item in (root / ".github").glob("*.md"):
        result.add(item)
    for name in ROOT_PUBLICATIONS:
        item = root / name
        if item.exists():
            result.add(item)
    return sorted(p for p in result if p.is_file())


def normalize(text: str) -> str:
    return STANDALONE.sub(lambda match: CANONICAL, text)


def find_violations(root: Path = ROOT):
    results = []
    for path in active_paths(root):
        text = path.read_text(encoding="utf-8")
        for match in STANDALONE.finditer(text):
            line = text.count("\n", 0, match.start()) + 1
            results.append(f"{path.relative_to(root)}:{line}: standalone company attribution")
    # Explicitly test machine-readable names, not just the copyright banner.
    metadata = root / "codemeta.json"
    if metadata.is_file():
        record = json.loads(metadata.read_text(encoding="utf-8"))
        for key in ("author", "copyrightHolder"):
            for entry in record.get(key, []):
                if entry.get("name") != CANONICAL:
                    results.append(f"codemeta.json: {key} must use canonical publisher name")
    citation = root / "CITATION.cff"
    if citation.is_file():
        text = citation.read_text(encoding="utf-8")
        if f'  - name: "{CANONICAL}"' not in text:
            results.append("CITATION.cff: canonical organizational citation missing")
    package = root / "pyproject.toml"
    if package.is_file() and f'authors = [{{ name = "{CANONICAL}" }}]' not in package.read_text(encoding="utf-8"):
        results.append("pyproject.toml: canonical package author missing")
    return results


def inventory(root: Path = ROOT):
    try:
        output = subprocess.check_output(
            ["git", "ls-files", "-z"], cwd=root)
    except (OSError, subprocess.CalledProcessError):
        return ["inventory unavailable: Git metadata missing"]
    active = set(active_paths(root))
    rows = []
    for raw in output.split(b"\0"):
        if not raw:
            continue
        try:
            name = raw.decode("utf-8")
        except UnicodeDecodeError:
            continue
        path = root / name
        if path in active or not path.is_file():
            continue
        try:
            data = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        matches = list(STANDALONE.finditer(data))
        if matches:
            rows.append(f"{name}: {len(matches)} historical or nonpublication occurrences for review")
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    command = parser.add_mutually_exclusive_group(required=True)
    command.add_argument("--check", action="store_true")
    command.add_argument("--fix", action="store_true")
    command.add_argument("--inventory", action="store_true")
    args = parser.parse_args(argv)
    if args.inventory:
        print("\n".join(inventory()) or "No remaining standalone names in other tracked text.")
        return 0
    if args.fix:
        changed = []
        for path in active_paths():
            old = path.read_text(encoding="utf-8")
            new = normalize(old)
            if new != old:
                path.write_text(new, encoding="utf-8")
                changed.append(str(path.relative_to(ROOT)))
        print("\n".join(changed) if changed else "Active publisher names already canonical.")
        # Metadata is checked separately, not silently restructured.
    errors = find_violations()
    if errors:
        print("\n".join(errors))
        return 1
    print(f"PASS: {len(active_paths())} active publications use {CANONICAL}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
