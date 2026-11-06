# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every workflow names its token's rights (docs/THREAT_MODEL.md, T9): at the top, or on every job. None leaves its token
the repository's default rights, and a workflow whose token only reads cannot push, start a run or read another run's
files."""
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]


def test_every_workflow_names_its_tokens_rights():
    open_ = []
    for f in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        wf = yaml.safe_load(f.read_text())
        jobs = wf.get("jobs") or {}
        if "permissions" not in wf and not all("permissions" in (j or {}) for j in jobs.values()):
            open_.append(f.name)
    assert not open_, "workflows leaving their token the repository's default rights: " + ", ".join(open_)


def test_a_read_only_token_is_given_only_where_nothing_needs_more():
    for f in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
        text = f.read_text()
        wf = yaml.safe_load(text)
        if wf.get("permissions") != {"contents": "read"}:
            continue
        for needs in ("git push", "raw_archive.sh save", "/dispatches", "run-id:", "id-token"):
            assert needs not in text, f"{f.name} reads only, yet carries {needs!r}"
