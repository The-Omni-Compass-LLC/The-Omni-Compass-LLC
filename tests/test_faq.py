# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The buyer's questions (tools/faq.py): written from the records, every number read, never typed."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools import faq  # noqa: E402


class Faq(unittest.TestCase):
    def test_in_line_with_the_records(self):
        self.assertEqual(faq.main(["--check"]), 0, "python3 tools/faq.py")

    def test_says_no_outside_review_and_names_the_engine(self):
        md = (ROOT / "docs" / "FAQ.md").read_text(encoding="utf-8")
        self.assertIn("No outside party has reviewed or approved these results.", md)
        self.assertRegex(md, r"The engine that stands is omni-v\d+;")


if __name__ == "__main__":
    unittest.main()
