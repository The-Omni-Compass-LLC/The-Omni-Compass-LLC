# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Prevent active publisher-facing material from reverting to a single company."""
from pathlib import Path
import json
import unittest

from tools.company_attribution import (
    ROOT, CANONICAL, STANDALONE, active_paths, find_violations, normalize,
)


class CanonicalCompanyAttribution(unittest.TestCase):
    def test_normalization_is_idempotent_and_preserves_links(self):
        self.assertEqual(normalize(CANONICAL), CANONICAL)
        self.assertEqual(normalize(normalize("The Omni-Compass LLC")), CANONICAL)
        self.assertEqual(normalize("Omni Compass LLC"), CANONICAL)
        self.assertEqual(normalize("The Omni Compass LLC"), CANONICAL)
        repo = "https://github.com/The-Omni-Compass-LLC/The-Omni-Compass-LLC"
        self.assertEqual(normalize(repo), repo)
        self.assertEqual(normalize("Omni-Compass"), "Omni-Compass")

    def test_copyright_and_legal_identity_are_jointly_presented(self):
        for name in ("LICENSE", "NOTICE", "DISCLOSURES.md", "README.md"):
            with self.subTest(file=name):
                self.assertIn(CANONICAL, (ROOT / name).read_text(encoding="utf-8"))
        meta = json.loads((ROOT / "codemeta.json").read_text(encoding="utf-8"))
        self.assertTrue(meta["author"] and meta["copyrightHolder"])
        for group in ("author", "copyrightHolder"):
            self.assertTrue(all(x.get("name") == CANONICAL for x in meta[group]))
        self.assertIn(f'authors = [{{ name = "{CANONICAL}" }}]',
                      (ROOT / "pyproject.toml").read_text(encoding="utf-8"))
        self.assertIn(f'  - name: "{CANONICAL}"',
                      (ROOT / "CITATION.cff").read_text(encoding="utf-8"))

    def test_all_active_publisher_documents_and_manuals_are_consistent(self):
        entries = active_paths()
        self.assertGreaterEqual(len(entries), 100, "expected all active docs")
        self.assertFalse(find_violations(), "noncanonical active attribution remains")
        for name in ("docs/OMNI_COMPASS_MANUAL.md",
                     "docs/OMNI_COMPASS_OWNERS_MANUAL.md",
                     "docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md"):
            with self.subTest(manual=name):
                s = (ROOT / name).read_text(encoding="utf-8")
                self.assertIn(CANONICAL, s)
                self.assertIsNone(STANDALONE.search(s))


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
