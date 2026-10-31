# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The benefit sheet (tools/benefit_sheet.py): one number per benchmark, a plus always a GAIN for the system's declared aims,
its word (GAIN, STEADY, LOSS, power given) judged by what each gauge is for, read from the tables."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import benefit_sheet as bs  # noqa: E402


class TheSheet(unittest.TestCase):
    def test_the_words_and_the_numbers(self):
        self.assertEqual(bs.benefit_word(3, 0), "GAIN")
        self.assertEqual(bs.benefit_word(0, 2), "LOSS")
        self.assertEqual(bs.benefit_word(0, 0), "STEADY")
        self.assertEqual(bs.benefit_word(2, 1), "GAIN AND LOSS")
        self.assertEqual(bs.benefit_word(2, 0, 1), "GAIN, power given", "a GAIN bought with a resource is never a LOSS")
        self.assertEqual(bs.benefit_word(0, 0, 1), "power given")
        self.assertEqual(bs.fmt_pct(0.02), "0%")
        self.assertEqual(bs.fmt_pct(-24.9), "-25%")
        self.assertEqual(bs.fmt_pct(4.04), "+4.0%")
        self.assertEqual(bs.fmt_pct(None), "no number")

    def test_a_cut_reads_gain_and_a_resource_given_never_loss(self):
        rows = [["Gauge", "native (A)", "omni (A)", "A", "B", "C", "Reading"],
                ["energy (J)", "100", "80", "-20.0%", "-20.0%", "-20.0%", "**GAIN in all three of our runs**"],
                ["work (units)", "100", "110", "+10.0%", "+10.0%", "+10.0%", "**GAIN in all three of our runs**"],
                ["taps", "4", "8", "+100.0%", "+100.0%", "+100.0%", "**power given in all three of our runs**"],
                ["wait (s)", "10", "11", "+10.0%", "+10.0%", "+10.0%", "**higher in all three of our runs**"],
                ["noise", "1", "1", "+1.0%", "-1.0%", "+0.5%", "STEADY, no difference beyond the noise (3 of 3 runs)"]]
        aims = {"energy (J)": "spent", "work (units)": "higher", "taps": "spent", "wait (s)": "lower", "noise": "lower"}
        r, g, l_, gv = bs.sim_case_ratio(rows, aims)
        self.assertEqual((g, l_, gv), (2, 1, 1), "energy cut and more work: GAIN; a longer wait: LOSS; more taps: power given")
        self.assertAlmostEqual(r, (1.25 * 1.10 * 0.5 * (1 / 1.1) * 1.0) ** 0.2, places=9,
                               msg="less energy is plus, more work is plus, more taps and a longer wait are minus, noise is one")
        self.assertEqual(bs.in_words([("p95", "GAIN", "-65% to -71%", "lower"), ("memory", "power given", "+215%", "spent"),
                                      ("work", "LOSS", "-5%", "higher")]),
                         "p95 cut 65% to 71% (GAIN); memory up 215% (power given); work down 5.0% (LOSS)")
        self.assertEqual(bs.fmt_pct_words(31.0), "31% GAIN")   # the size beside its word, no sign (tools/readings.py by_word)
        self.assertEqual(bs.fmt_pct_words(-25.0), "25% power given", "a fall with no LOSS is the resources put in, its size beside the word")
        self.assertEqual(bs.fmt_pct_words(-25.0, loss=1), "25% LOSS")
        self.assertEqual(bs.fmt_pct_words(0.01), "0%: STEADY")

    def test_the_published_sheet_is_what_the_tables_give(self):
        self.assertEqual(bs.main(check=True), 0)


if __name__ == "__main__":
    unittest.main()
