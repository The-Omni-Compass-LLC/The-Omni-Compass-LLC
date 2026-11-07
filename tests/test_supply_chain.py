# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The supply chain is pinned (docs/THREAT_MODEL.md, T8): every GitHub action a workflow uses is named by its commit, never
by a tag that can be moved, with the tag beside it for Dependabot and the reader; and every package in the lock carries the
hashes pip checks each download against."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class SupplyChain(unittest.TestCase):
    def test_every_action_is_named_by_its_commit(self):
        loose = []
        for p in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            for i, ln in enumerate(p.read_text().split("\n"), 1):
                m = re.match(r"^\s*-?\s*uses:\s*(\S+)", ln)
                if m and not m.group(1).startswith("./") and not re.fullmatch(r"[\w.\-]+/[\w.\-/]+@[0-9a-f]{40}", m.group(1)):
                    loose.append(f"{p.name}:{i}: {m.group(1)}")
                elif m and not m.group(1).startswith("./") and not re.search(r"@[0-9a-f]{40} # v\d", ln):
                    loose.append(f"{p.name}:{i}: the tag is not written beside the commit")
        self.assertEqual(loose, [])

    def test_every_locked_package_carries_its_hashes(self):
        text = (ROOT / "requirements-lock.txt").read_text()
        blocks = re.split(r"\n(?=[A-Za-z0-9_.\-]+==)", text)
        pins = [b for b in blocks if re.match(r"[A-Za-z0-9_.\-]+==", b)]
        self.assertGreater(len(pins), 20)
        bare = [b.split()[0] for b in pins if not re.search(r"--hash=sha256:[0-9a-f]{64}", b)]
        self.assertEqual(bare, [])


if __name__ == "__main__":
    unittest.main()
