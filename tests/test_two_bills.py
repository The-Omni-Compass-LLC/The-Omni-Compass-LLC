# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The two bills (tools/two_bills.py, the founder's design of 1 November 2026): four arms, A the chip native, B the chip with
Omni-Compass on native, C the cloud native, D the cloud with Omni-Compass on native, each read by its bill and the work done
inside it; every number from a table the repository holds, each place on its own engine and named."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import two_bills as tb  # noqa: E402


class TwoBills(unittest.TestCase):
    def setUp(self):
        self.chip, self.cloud = tb.chip(), tb.cloud()
        self.text = tb.PAGE.read_text(encoding="utf-8")

    def test_the_page_is_what_the_tables_give(self):
        self.assertEqual(tb.main(["--check"]), 0)

    def test_four_arms_named_and_the_runs_never_lettered(self):
        for arm in ("A, native", "B, Omni-Compass on native", "C, native", "D, Omni-Compass on native"):
            self.assertIn(arm, self.text)
        self.assertIn("| Run 1 | Run 2 | Run 3 |", self.text)

    def test_the_chip_bill_is_the_rental_of_each_arms_own_window(self):
        for r in self.chip["per_run"]:
            for side in ("native", "omni"):
                a = r[side]
                self.assertAlmostEqual(a["bill"], tb.CHIP_PRICE * a["seconds"] / 3600.0)
                self.assertAlmostEqual(a["per_dollar"], a["work"] / a["bill"])

    def test_each_place_names_its_engine(self):
        self.assertIn("omni-v23", self.text)
        self.assertIn(f"Kubernetes on Azure's AKS, {tb.CLOUD_ENGINE}", self.text)

    def test_a_place_that_counted_no_work_reads_no_work_per_dollar(self):
        if self.cloud["work_key"] is None:
            self.assertIn("counted no work done", self.text)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
