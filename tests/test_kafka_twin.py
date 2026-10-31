# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v22 on the Kafka consumer group (docs/KAFKA_PREREGISTRATION.md, amendment 4): the group's twin and the immune reflex.
On omni-v21 the verdict's allowance clamped the wall's fail-up and the wall abandoned every spend trial, so the brain asked for
consumers in 1,413 of the 1,428 seconds the service stood over its line and was refused; each test below fails on that wire."""
import unittest

from tools import run_kafka as K
from tools import kafka_model as M


def obs(arrival_rate, lag, consumers, reading=0.02, n_msg=None, idle=0):
    arrivals = [arrival_rate * s for s in M.KEY_SHARE]
    return {"reading": reading, "n_msg": int(n_msg if n_msg is not None else arrival_rate), "inside": int(arrival_rate),
            "lag": lag, "idle": idle, "consumers": consumers, "cpu_share": 0.3, "arrivals": arrivals}


class Twin(unittest.TestCase):
    def test_the_keys_land_on_six_partitions_and_the_range_assignor_splits_them(self):
        self.assertEqual([round(8 * s) for s in M.KEY_SHARE], [1, 1, 0, 1, 1, 0, 2, 2])
        self.assertAlmostEqual(M.heaviest_share(2), 5 / 8)
        self.assertAlmostEqual(M.heaviest_share(3), 4 / 8)
        self.assertAlmostEqual(M.heaviest_share(4), 4 / 8, msg="a fourth consumer adds no relief")
        self.assertAlmostEqual(M.heaviest_share(5), 2 / 8)

    def test_the_twin_learns_a_members_rate_from_a_second_the_queue_grew(self):
        tw = K.RateTwin()
        arrivals = [880 * s for s in M.KEY_SHARE]
        mu = tw.learn(2, arrivals, consumed=330 + 495)      # the 3/8 member serves its 330, the 5/8 member its 495
        self.assertAlmostEqual(mu, 495, delta=1)
        self.assertIsNone(tw.learn(2, arrivals, consumed=880), "a group that keeps up says nothing of its rate")

    def test_needed_skips_a_count_that_adds_no_relief(self):
        tw = K.RateTwin(); tw.mu_est.append(495.0)
        arrivals = [880 * s for s in M.KEY_SHARE]
        self.assertEqual(tw.needed(arrivals, 2, 8, K.RHO_SPEND), 3)
        self.assertEqual(tw.needed(arrivals, 2, 8, K.RHO_SPEND, backlog=2700), 5, "a backlog to drain needs more than the arrivals")

    def test_before_any_stall_is_seen_the_twin_takes_the_heartbeat_bound(self):
        self.assertEqual(K.RateTwin().stall_s, K.HEARTBEAT_MS / 1000.0)


class Reflex(unittest.TestCase):
    def brain(self):
        b = K.Brain(2, "resource")
        for t in range(1, 40):                                # calm: 110 a second, nothing waiting
            b.step(float(t), obs(110, 0, 2))
        return b

    def test_the_queue_growing_past_the_members_rate_goes_at_once_to_the_count_that_carries_it(self):
        b = self.brain()
        target, why, info = b.step(40.0, obs(880, 0, 2, reading=0.01, n_msg=880))
        target, why, info = b.step(41.0, obs(880, 55, 2, reading=0.06, n_msg=825))
        self.assertEqual(target, 5, why)
        self.assertIn("the twin", why)
        self.assertGreater(target, b.verdict.allowed_high, "the reflex is never clamped by the verdict's allowance")

    def test_held_through_a_calm_notch_and_handed_back_in_one_move(self):
        b = self.brain()
        b.step(40.0, obs(880, 0, 2, n_msg=880)); b.step(41.0, obs(880, 55, 2, reading=0.06, n_msg=825))
        for t in range(42, 72):
            target, why, _ = b.step(float(t), obs(880, 0, 5))
            self.assertEqual(target, 5)
        for t in range(72, 100):                              # a calm notch inside the window: the peak still in it, held
            target, why, _ = b.step(float(t), obs(110, 0, 5, reading=0.005))
            self.assertEqual(target, 5, why)
        target = 5
        for t in range(100, 160):
            target, why, _ = b.step(float(t), obs(110, 0, target, reading=0.005))
            if target != 5:
                break
        self.assertEqual(target, 2, "one move back to the operator's count once the window's peak has passed")

    def test_never_below_the_operators_count(self):
        b = self.brain()
        for t in range(40, 200):
            target, why, _ = b.step(float(t), obs(10, 0, 2, reading=0.001, idle=1))
            self.assertGreaterEqual(target, 2, why)


if __name__ == "__main__":
    unittest.main()
