# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The 95% point of Student's t, computed: the printed tables to the last digit, and no fall to 1.96 past them."""
import math
import unittest

from omnicompass.student_t import T95, coverage, ibeta, t95

# the standard two-sided 95% points (any statistics table), to three decimals
TABLE = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228,
         11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131, 16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086,
         25: 2.060, 29: 2.045, 30: 2.042, 40: 2.021, 60: 2.000, 120: 1.980, 1000: 1.962}


class StudentT(unittest.TestCase):
    def test_the_standard_table(self):
        for df, t in TABLE.items():
            with self.subTest(df=df):
                self.assertEqual(t95(df), t)

    def test_the_limit_is_the_normal_point(self):
        self.assertEqual(t95(10 ** 6), 1.960)

    def test_falls_with_the_degrees_of_freedom(self):
        vals = [t95(df) for df in range(1, 300)]
        self.assertTrue(all(a >= b for a, b in zip(vals, vals[1:])))

    def test_coverage_at_the_point_is_95_percent(self):
        for df in (1, 3, 9, 30, 200):
            self.assertAlmostEqual(coverage(t95(df), df), 0.95, delta=2e-3)

    def test_incomplete_beta_known_values(self):
        self.assertAlmostEqual(ibeta(1.0, 1.0, 0.3), 0.3, places=12)          # the uniform distribution
        self.assertAlmostEqual(ibeta(2.0, 3.0, 0.4), 0.5248, places=12)       # 1 − (1 − x)³(1 + 3x) at x = 0.4
        self.assertEqual(ibeta(2.0, 2.0, 0.0), 0.0)
        self.assertEqual(ibeta(2.0, 2.0, 1.0), 1.0)

    def test_read_as_the_tables_were(self):
        self.assertEqual(T95.get(9, 1.96), 2.262)
        self.assertEqual(T95.get(10, 1.96), 2.228)                           # the old tables fell to 1.96 here
        self.assertEqual(T95[20], 2.086)
        self.assertTrue(math.isnan(T95.get(0)))
        self.assertEqual(T95.get(0, 1.96), 1.96)


if __name__ == "__main__":
    unittest.main()
