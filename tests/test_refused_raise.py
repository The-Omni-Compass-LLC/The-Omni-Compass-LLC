# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A raise the cluster's admission refuses is not written again until the pod or the raise changes or the wait passes
(v12): the omni-v11 capacity test wrote every refused CPU-limit raise again at every fast check, about 9 a minute."""
import unittest
from types import SimpleNamespace
from unittest import mock

from omni_controller import muscles as M
from omni_controller.muscles import Muscles
from tests.test_quota_convey import Cluster, pod, quota


class RefusedRaise(unittest.TestCase):
    def setUp(self):
        self.now = 1000.0
        p = mock.patch.object(M.time, "time", lambda: self.now)
        p.start(); self.addCleanup(p.stop)
        self.c = Cluster([quota(used='1000m')], reject=True)
        self.events = []
        self.m = Muscles(self.c, SimpleNamespace(cap_deployments='default/web', cap_min_change_m=10), self.events.append)
        self.m._convey_engaged = lambda: True

    def patches(self):
        return sum(1 for w in self.c.writes if w[0] == 'patch')

    def test_a_refused_raise_is_held_and_asked_again_after_its_wait(self):
        self.assertEqual(self.m.convey(), {})
        self.assertEqual(self.patches(), 1)
        held = [e for e in self.events if "convey resize rejected" in str(e.get("error", ""))]
        self.assertEqual(held[-1]["held_s"], M.REFUSED_WAIT_S[0])
        for _ in range(20):                                       # every fast check inside the wait: nothing written
            self.now += 5.0
            self.m.convey()
        self.assertEqual(self.patches(), 1)
        self.now += M.REFUSED_WAIT_S[0]                           # the wait passed: asked once more, refused, the wait doubled
        self.m.convey()
        self.assertEqual(self.patches(), 2)
        held = [e for e in self.events if "convey resize rejected" in str(e.get("error", ""))]
        self.assertEqual(held[-1]["held_s"], 2 * M.REFUSED_WAIT_S[0])

    def test_the_wait_never_passes_its_last(self):
        for _ in range(12):
            self.now += M.REFUSED_WAIT_S[1] + 1.0
            self.m.convey()
        held = [e for e in self.events if "convey resize rejected" in str(e.get("error", ""))]
        self.assertEqual(held[-1]["held_s"], M.REFUSED_WAIT_S[1])

    def test_a_pod_whose_limit_changed_is_asked_at_once(self):
        self.m.convey()
        self.assertEqual(self.patches(), 1)
        self.c.pods[0]['spec']['containers'][0]['resources']['limits']['cpu'] = '400m'   # someone else moved it
        self.now += 5.0
        self.m.convey()
        self.assertEqual(self.patches(), 2)

    def test_an_accepted_raise_clears_the_hold(self):
        self.m.convey()
        self.c.reject = False
        self.now += M.REFUSED_WAIT_S[0] + 1.0
        self.assertEqual(self.m.convey(), {'default/web': 1000})
        self.assertEqual(self.m.refused, {})


if __name__ == "__main__":
    unittest.main()

# © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
