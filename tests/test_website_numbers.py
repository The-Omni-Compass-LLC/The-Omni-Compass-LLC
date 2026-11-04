# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The website's numbers (tools/website_numbers.py): written from the records; four arms, A, B, C and D; the model table that the
website printed as 47.2% and 49.9% is out of results/; every number never to be printed is named with where it came from."""
import json
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from tools import website_numbers as W  # noqa: E402


class WebsiteNumbers(unittest.TestCase):
    def test_in_line_with_the_records(self):
        self.assertEqual(W.main(["--check"]), 0, "python3 tools/website_numbers.py")

    def test_four_arms_never_three(self):
        n = json.loads((ROOT / "results" / "WEBSITE_NUMBERS.json").read_text(encoding="utf-8"))
        self.assertEqual([k for k in n["arms"] if len(k) == 1], ["A", "B", "C", "D"])
        self.assertTrue(n["arms"]["D"]["against_C"], "arm D is read from the cloud's own receipt")
        self.assertIn("three runs of one test", n["rule"])

    def test_the_model_table_is_no_result(self):
        self.assertFalse((ROOT / "results" / "ABC_TABLE.json").exists(), "a model table in results/ is read by the website as a result")
        self.assertTrue((ROOT / "docs" / "history" / "model_tables" / "ABC_TABLE_MODEL.json").exists())
        n = json.loads((ROOT / "results" / "WEBSITE_NUMBERS.json").read_text(encoding="utf-8"))
        banned = {x["number"] for x in n["not_allowed"]}
        for x in ("47.2%", "49.9%", "+5.3% GPU energy", "three arms"):
            self.assertIn(x, banned)
        allowed = json.dumps({k: v for k, v in n.items() if k != "not_allowed"})
        for x in ("47.2", "49.9"):
            self.assertNotIn(x, allowed, f"{x} is printed nowhere")

    def test_every_category_or_none(self):
        n = json.loads((ROOT / "results" / "WEBSITE_NUMBERS.json").read_text(encoding="utf-8"))
        idx = json.loads((ROOT / "results" / "OMNI_INDEX.json").read_text(encoding="utf-8"))
        self.assertEqual(len(n["index"]["categories"]), len(idx["categories"]))


if __name__ == "__main__":
    unittest.main()
