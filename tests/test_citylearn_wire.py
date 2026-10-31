# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The CityLearn battery wire of omni-v9, at omni-v10's glide (tools/run_citylearn.py): what it reads and how far it may move.

  - the reading is causal: the coming hour is read from the same hour of past days only, never from an hour not yet seen;
  - until a day has been seen it reads the last hour, as before;
  - the adjustment never changes by more than SLEW in an hour, and reaches its target when the target is within reach;
  - with the compass's force bounded by one (CompassLaw's authority), the adjustment never leaves [−GAIN, GAIN], so a
    battery command moves by at most GAIN of its range, inside the battery's own limits.
"""
import random
import unittest

from omnicompass.compass_law import Band, CompassLaw
from tools.run_citylearn import FORECAST_DAYS, GAIN, SLEW, coming_hour, glide, reading


class ComingHour(unittest.TestCase):
    def test_reads_only_the_same_hour_of_past_days(self):
        hist = list(range(24 * 10))                      # hour t-k carries the value len - k
        got = coming_hour(hist)
        same = [hist[-24 * d] for d in range(1, FORECAST_DAYS + 1)]
        self.assertAlmostEqual(got, sum(same) / len(same))

    def test_never_reads_an_hour_not_yet_seen(self):
        rng = random.Random(3)
        hist = [rng.uniform(-20, 40) for _ in range(200)]
        before = coming_hour(hist)
        hist_future = hist + [1e9]                       # an hour appended after the reading cannot change it
        self.assertEqual(coming_hour(hist), before)
        self.assertNotEqual(coming_hour(hist_future), 1e9)

    def test_fewer_than_a_day_reads_the_last_hour(self):
        self.assertEqual(coming_hour([5.0, 7.0, 9.0]), 9.0)

    def test_fewer_than_a_week_uses_the_days_it_has(self):
        hist = [0.0] * 50                                # 50 hours: the same hour one and two days back exist
        hist[-24], hist[-48] = 2.0, 4.0
        self.assertEqual(coming_hour(hist), 3.0)


class Glide(unittest.TestCase):
    def test_never_moves_more_than_slew(self):
        rng = random.Random(7)
        off = 0.0
        for _ in range(5000):
            new = glide(off, rng.uniform(-3, 3))
            self.assertLessEqual(abs(new - off), SLEW + 1e-12)
            off = new

    def test_reaches_a_target_within_reach(self):
        self.assertEqual(glide(0.2, 0.2 + SLEW / 2), 0.2 + SLEW / 2)

    def test_stays_inside_gain_under_any_bounded_force(self):
        rng = random.Random(11)
        law = CompassLaw(Band(0.0, 10.0), dt=1.0, tau=1.0)
        off = 0.0
        for _ in range(20000):
            f = law.force(rng.uniform(-30, 40))
            self.assertLessEqual(abs(f), 1.0 + 1e-12)
            off = glide(off, -GAIN * f)
            self.assertLessEqual(abs(off), GAIN + 1e-12)
            cmd = max(-1.0, min(1.0, rng.uniform(-1, 1) + off))
            self.assertTrue(-1.0 <= cmd <= 1.0)


class OneKey(unittest.TestCase):
    """The run's own receipt reads every score by the one key (tools/readings.py), never by the sign of its number."""
    def test_a_fall_is_a_gain(self):
        self.assertEqual(reading("cost_total", 1.10, 1.00), "GAIN")
        self.assertEqual(reading("discomfort_proportion", 0.80, 0.70), "GAIN")

    def test_a_rise_in_power_held_is_power_given(self):
        for score in ("cost_total", "daily_peak_average", "all_time_peak_average", "ramping_average",
                      "monthly_one_minus_load_factor_average", "zero_net_energy"):
            self.assertEqual(reading(score, 1.00, 1.06), "power given")

    def test_a_rise_in_a_miss_is_a_loss(self):
        self.assertEqual(reading("annual_normalized_unserved_energy_total", 0.0175, 0.0176), "LOSS")
        self.assertEqual(reading("discomfort_proportion", 0.70, 0.71), "LOSS")

    def test_identical_is_even_and_missing_is_not_scored(self):
        self.assertEqual(reading("cost_total", 1.0, 1.0), "STEADY")
        self.assertEqual(reading("cost_total", None, 1.0), "not scored")


if __name__ == "__main__":
    unittest.main()
