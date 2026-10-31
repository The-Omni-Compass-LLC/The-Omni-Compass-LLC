# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
from tools.benefit_interpretation import interpret_pair
import unittest


class BenefitInterpretationTests(unittest.TestCase):
    def test_resource_cut_is_gain_and_capacity_is_explicitly_conditional(self):
        r = interpret_pair("resource", 100, 95)
        self.assertEqual(r["classification"], "GAIN")
        self.assertEqual(round(r["resource_saved_pct"], 2), 5.00)
        self.assertEqual(round(r["conditional_work_capacity_pct"], 2), 5.26)
        self.assertIn("not work observed", r["interpretation"])


    def test_resource_increase_is_power_given_not_automatically_loss(self):
        r = interpret_pair("resource", 100, 103)
        self.assertEqual(r["classification"], "POWER GIVEN")
        self.assertIn("what service gain it bought", r["interpretation"])


    def test_work_and_latency_use_different_objective_directions(self):
        self.assertEqual(interpret_pair("work", 100, 110)["classification"], "GAIN")
        self.assertEqual(interpret_pair("latency", 100, 90)["classification"], "GAIN")
        self.assertEqual(interpret_pair("safety", 100, 101)["classification"], "LOSS")


    def test_equal_values_are_even(self):
        self.assertEqual(interpret_pair("resource", 100, 100)["classification"], "STEADY")


if __name__ == "__main__":
    unittest.main()
