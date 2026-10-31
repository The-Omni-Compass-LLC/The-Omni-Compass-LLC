# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The paid cloud set's stopping rule (tools/stop_rule.py): it stops only when the bill is read, never on a LOSS, never
before a look is reached, and its 99% point is Student's."""
import random
import unittest

from tools import stop_rule as S

P95, FAIL = S.HARM


def arms(n, cut=0.0, sd=0.01, harm=0.0, seed=1):
    rng = random.Random(seed)
    nat, omni = {}, {}
    for r in range(1, n + 1):
        b = 1.0 + rng.gauss(0, 0.1)
        nat[str(r)] = {S.BILL: b, P95: 500.0, FAIL: 1.0}
        omni[str(r)] = {S.BILL: b * (1 - cut) + rng.gauss(0, sd), P95: 500.0 + harm + rng.gauss(0, 1), FAIL: 1.0 + rng.gauss(0, 0.01)}
        nat[str(r)][P95] += rng.gauss(0, 1)
    return nat, omni


class StopRule(unittest.TestCase):
    def test_t_point(self):
        self.assertAlmostEqual(S.t_point(9), 3.250, places=2)       # the two-sided 99% point at 9 degrees of freedom
        self.assertAlmostEqual(S.t_point(1000), 2.581, places=2)

    def test_clear_cut_stops_at_the_first_look(self):
        nat, omni = arms(30, cut=0.10)
        go, why = S.decide(nat, omni, 11)
        self.assertFalse(go)
        self.assertIn("GAIN", why)

    def test_nothing_decided_before_a_look(self):
        nat, omni = arms(9, cut=0.10)
        self.assertTrue(S.decide(nat, omni, 10)[0])

    def test_noise_runs_on(self):
        nat, omni = arms(30, cut=0.0, sd=0.2)
        self.assertTrue(S.decide(nat, omni, 21)[0])

    def test_precise_even_stops(self):
        nat, omni = arms(30, cut=0.0, sd=0.001)
        go, why = S.decide(nat, omni, 11)
        self.assertFalse(go)
        self.assertIn("STEADY", why)

    def test_a_loss_never_stops_the_set(self):
        nat, omni = arms(30, cut=0.10, harm=50.0)
        self.assertTrue(S.decide(nat, omni, 21)[0])

    def test_a_lost_repetition_leaves_the_look_unreached(self):
        nat, omni = arms(10, cut=0.10)
        del omni["3"]
        self.assertTrue(S.decide(nat, omni, 11)[0])


class Title(unittest.TestCase):
    def test_a_set_under_the_rule_is_counted_apart(self):
        from scripts import dispatch_grid as G
        kv = {"replica_ceiling": "0", "dial": "save"}
        old, new = G.azure_title(kv), G.azure_title({**kv, "stop_looks": "10,20,40,70"})
        self.assertNotEqual(old, new)
        self.assertEqual(new, "aks-metered steady replica room 0 to the cap, stopping rule dial save eastus Standard_D2s_v4")
        self.assertEqual(G.azure_group(new), G.azure_group(old))     # the same machine-family queue


if __name__ == "__main__":
    unittest.main()
