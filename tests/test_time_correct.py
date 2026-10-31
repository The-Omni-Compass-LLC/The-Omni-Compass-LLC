# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Every rule of the governor counts in seconds (Omni v7, omni_controller/controller.py): at a decision every 60, 15 or
5 seconds each rule keeps its time, the compass moves the HPA target by the same amount a minute, the pool gives back at
most one machine a minute, and at 60 s every count is the one v6 used. (The cloud's rule in one word, --give-back-only, left
the governor with omni-v24: the founder's order of 31 October struck the machines alone; tests/test_cloud_at_the_max.py.)"""
import unittest
from unittest.mock import Mock

from omni_controller.controller import Controller, parser, RELEASE_PERIOD_S


def controller(*extra):
    return Controller(parser().parse_args(["--audit", "", *extra]), kube=Mock())


class TimeCorrect(unittest.TestCase):
    RULES = ("n_slo_clear", "n_cruise_after", "n_strict_window", "n_verdict_every", "n_verdict_recheck", "n_verdict_trial")

    def test_at_60_s_the_counts_are_v6s(self):
        c = controller("--interval", "60", "--law", "compass")
        self.assertEqual([getattr(c, r) for r in self.RULES], [3, 2, 5, 10, 120, 20])
        self.assertEqual(c.verdict.probe_every, 10)
        self.assertEqual(c.verdict.recheck, 120)
        self.assertEqual(c.verdict.max_trial, 20)
        self.assertEqual(c.step_scale, 1.0)

    def test_each_rule_keeps_its_time_at_any_period(self):
        base = controller("--interval", "60")
        for period in (15, 5):
            c = controller("--interval", str(period))
            for r in self.RULES:
                self.assertEqual(getattr(c, r) * period, getattr(base, r) * 60, (period, r))

    def test_the_compass_moves_the_same_amount_a_minute(self):
        for period in (60, 15, 5):
            c = controller("--interval", str(period))
            self.assertAlmostEqual(c.step_scale * (60 / period), 1.0)

    def test_an_explicit_count_still_wins(self):
        c = controller("--interval", "15", "--slo-clear", "7", "--cruise-after", "0")
        self.assertEqual(c.n_slo_clear, 7)
        self.assertEqual(c.n_cruise_after, 0)

    def test_release_is_a_rate_in_time(self):
        self.assertEqual(RELEASE_PERIOD_S, 60.0)


if __name__ == "__main__":
    unittest.main()
