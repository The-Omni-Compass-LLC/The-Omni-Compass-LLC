# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The words for the places, written once (the founder's words of 31 October, night: "you need the terminology ... wherever it's
supposed to be, however it's supposed to be"): tools/places.py's block stands word for word on every page it names; it holds
no number, so no reading can go stale inside it; and a cloud set or a chip run is read for whether Omni-Compass holds."""
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import places as P  # noqa: E402
from tools import live_glossary as G  # noqa: E402


class Places(unittest.TestCase):
    def test_every_page_carries_the_block_word_for_word(self):
        self.assertEqual(P.check(), [])

    def test_a_page_that_differs_is_caught(self):
        text = (ROOT / "README.md").read_text(encoding="utf-8")
        changed = text.replace("A place holds when its runs read no LOSS.", "A place holds.", 1)
        self.assertNotEqual(P.with_block(changed), changed)

    def test_the_block_names_every_place_and_holds_no_number(self):
        b = P.block()
        for term in ("The software end", "Bare metal", "Through the cloud", "The chip", "The four arms", "Hold", "Where the benefit lives"):
            self.assertIn(f"**{term}.**", b)
        body = b.replace(P.BEGIN, "").replace(P.END, "")
        self.assertIsNone(re.search(r"\d+(\.\d+)?\s*%", body))      # no reading inside the words

    def test_runners_are_never_bare_metal_or_the_chip(self):
        self.assertIn("never called bare metal and never called the chip", P.block())

    def test_the_cloud_and_the_chip_must_show_they_hold(self):   # the two places of the founder's order of 1 November
        rows = {r[0]: r[2] for r in P.ROWS}
        self.assertTrue(rows["Through the cloud"].startswith("that it holds"))
        self.assertTrue(rows["Bare metal, the chip"].startswith("that it holds"))
        self.assertIn("the benefit", rows["The software end"])

    def test_the_glossary_carries_every_place(self):
        names = {t["term"] for t in G.TERMS}
        for term in ("the software end", "bare metal", "through the cloud", "the chip", "the four arms", "hold",
                     "where the benefit lives", "the cloud as the wire"):
            self.assertIn(term, names)
        self.assertEqual(G.check_sources([t for t in G.TERMS if t["term"] in names]), [])


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
