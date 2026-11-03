# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The oversight line (tools/oversight.py): the pages a person would answer, from the records and nowhere else; the 7% an
example, never a result; no 20% written."""
import pathlib
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "tools"))
from tools import oversight as ov  # noqa: E402


class Oversight(unittest.TestCase):
    def test_in_line_with_the_records(self):
        self.assertEqual(ov.main(["--check"]), 0, "python3 tools/oversight.py")

    def test_pooled_is_the_sum_of_the_tables(self):
        d = ov.build()
        self.assertTrue(d["rows"], "no Kubernetes table carries the alert minutes")
        self.assertAlmostEqual(d["pooled"]["native"], sum(r["native"] for r in d["rows"]))
        self.assertAlmostEqual(d["pooled"]["omni"], sum(r["omni"] for r in d["rows"]))
        self.assertAlmostEqual(d["example"]["bill_change"], 0.07 * d["pooled"]["change"])

    def test_the_example_is_labelled_and_no_twenty(self):
        md = (ROOT / "results" / "OVERSIGHT.md").read_text(encoding="utf-8")
        self.assertIn("The example, not a result.", md)
        self.assertIn("Not a 20% (13% + 7%).", md)
        self.assertNotIn("eliminat", md.lower())


if __name__ == "__main__":
    unittest.main()
