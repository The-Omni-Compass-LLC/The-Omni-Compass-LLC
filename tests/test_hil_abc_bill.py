# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The organisms with a card inside read by the founder's two bills (1 November): the card's bill is the rental for each
arm's own window and its work per dollar the requests served for that bill (tools/hil_abc.py card_bill, arm_means), so the
chip's two arms, A native and B Omni-Compass on native, are read by what they cost and what they did inside it."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import hil_abc  # noqa: E402


def arm(organism, name, wall, served, energy):
    return {"organism": organism, "arm": name, "seed": 1, "wall_s": wall,
            "plants": [{"work": 10.0, "energy_j": 5.0, "viol": 0, "steps": 100}],
            "card": {"served": served, "energy_j": energy, "p95_ms": 500.0, "over_line_pct": 0.0}}


class CardBill(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        root = Path(self.tmp.name)
        for rep, (o_served, o_wall) in (("rep-1", (1100, 300.0)), ("rep-2", (1050, 303.0))):
            for name, wall, served in (("native", 300.0, 1000), ("omni", o_wall, o_served)):
                d = root / "size-10" / rep / "spine" / name
                d.mkdir(parents=True)
                (d / "arm.json").write_text(json.dumps(arm("spine", name, wall, served, 9000.0)))
        self.root = root

    def tearDown(self):
        self.tmp.cleanup()

    def test_the_bill_follows_the_window_and_work_per_dollar_the_requests_inside_it(self):
        per = hil_abc.contrasts(self.root)[(10, "spine")]
        self.assertEqual(len(per), 2)
        self.assertAlmostEqual(per[0]["card"]["bill"], 0.0)                    # the same window: the same rental
        self.assertAlmostEqual(per[0]["card"]["per_dollar"], 0.10)             # 10% more requests for it
        self.assertAlmostEqual(per[1]["card"]["bill"], 0.01)                   # a window 1% longer costs 1% more
        self.assertAlmostEqual(per[1]["card"]["per_dollar"], 1050 / 303 / (1000 / 300) - 1)

    def test_each_arm_keeps_its_receipts(self):
        m = hil_abc.arm_means(self.root)[(10, "spine")]
        self.assertEqual(m["native"]["n"], 2)
        self.assertAlmostEqual(m["native"]["served"], 1000)
        self.assertAlmostEqual(m["omni"]["served"], 1075)
        self.assertAlmostEqual(m["omni"]["wall_s"], 301.5)

    def test_the_bill_rows_sit_under_the_card_alone(self):
        names = [m for m, _, _ in hil_abc.MEASURES]
        self.assertIn("bill", names)
        self.assertIn("per_dollar", names)
        self.assertTrue({"bill", "per_dollar", "p95"} <= set(hil_abc.CARD_ONLY))


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
