# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only. Any commercial use, commercialization,
# monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass
# Enterprise License from The Omni-Compass LLC. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Work for the bill (tools/work_per_bill.py): the one number the receipts prove, written from the receipts and nowhere else."""
import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import work_per_bill as wpb  # noqa: E402


class WorkForTheBill(unittest.TestCase):
    def test_the_identity_holds_on_every_run(self):
        # G read off the receipt's own work per dollar equals (1 + w) / (1 + b) − 1, and ln(1 + G) = ln(1 + w) − ln(1 + b)
        r = wpb.run_g({"work": 100.0, "bill": 2.0}, {"work": 110.0, "bill": 2.1})
        self.assertAlmostEqual(r["G"], (1.10 / 1.05) - 1, places=12)
        self.assertAlmostEqual(r["log_check"], 0.0, places=12)
        self.assertAlmostEqual(r["approx_w_minus_b"], 0.10 - 0.05, places=12)

    def test_a_bill_that_rises_less_than_the_work_is_more_work_for_the_bill(self):
        self.assertGreater(wpb.run_g({"work": 100.0, "bill": 1.0}, {"work": 112.0, "bill": 1.01})["G"], 0)
        self.assertLess(wpb.run_g({"work": 100.0, "bill": 1.0}, {"work": 101.0, "bill": 1.05})["G"], 0)

    def test_an_owners_bill_counts_each_line_by_its_share(self):
        # a line Omni-Compass does not move only pulls b toward 0: the compute line's −10% is −9.79% of a $3,310 bill
        r = wpb.owner_bill({"compute": 3240.0, "egress": 40.0, "storage": 30.0}, {"compute": -0.10})
        self.assertAlmostEqual(r["B_native"], 3310.0)
        self.assertAlmostEqual(r["b"], -0.10 * 3240.0 / 3310.0, places=12)
        self.assertAlmostEqual(sum(r["shares"].values()), 1.0, places=12)

    def test_the_combined_number_lies_between_the_places(self):
        g = wpb.total_for({"bare": 500.0, "cloud": 3310.0}, {"bare": (0.02, 0.0), "cloud": (0.05, 0.01)})
        self.assertGreater(g, 0.02)
        self.assertLess(g, (1.05 / 1.01) - 1)

    def test_the_page_is_what_the_receipts_give(self):
        self.assertEqual(wpb.main(["--check"]), 0, "python3 tools/work_per_bill.py")

    def test_every_chip_run_matches_its_receipt(self):
        tb = json.loads((ROOT / "results" / "TWO_BILLS.json").read_text(encoding="utf-8"))
        d = json.loads(wpb.OUT_JSON.read_text(encoding="utf-8"))
        for pr, r in zip(tb["chip"]["per_run"], d["places"]["bare_metal"]["runs"]):
            self.assertAlmostEqual(r["G"], pr["omni"]["per_dollar"] / pr["native"]["per_dollar"] - 1, places=9)

    def test_no_place_without_counted_work_carries_a_G(self):
        d = json.loads(wpb.OUT_JSON.read_text(encoding="utf-8"))
        cl = d["places"].get("cloud") or {}
        if cl.get("status") != "read":
            self.assertIsNone(cl.get("G"))
            self.assertIsNone(d["total"]["G"])


if __name__ == "__main__":
    unittest.main()
