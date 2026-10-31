# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v19's immune system (docs/OMNI_V19.md; the founder's order of 24 October: where Omni-Compass cannot beat native, native
stays). The immune hand-back: a pod that waits while Omni-Compass holds a pod autoscaler's target below the operator's own gets
the operator's target back at once and held, the hold doubling for each hand-back in a row and halving after a quiet hold. The
immune memory for pods: extra pods are asked for only as far as the machines can place the largest rise seen times themselves.
Immune maturity: no give-back trial before one recheck period has passed."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omni_controller.controller import Controller, parser  # noqa: E402


def hpa(target, replicas=4, util=60):
    return {"metadata": {"name": "web", "namespace": "default"},
            "spec": {"scaleTargetRef": {"kind": "Deployment", "name": "web"}, "minReplicas": 1, "maxReplicas": 40,
                     "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": target}}}]},
            "status": {"currentReplicas": replicas, "desiredReplicas": replicas,
                       "currentMetrics": [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": util}}}]}}


class ImmuneSystem(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.audit = Path(self.tmp.name) / "audit.jsonl"
        self.k = Mock()
        self.k.get.side_effect = lambda *a: {"spec": {"template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "500m"}}}]}}}}
        a = parser().parse_args(["--mode", "nodepool", "--law", "compass", "--dial", "save", "--node-scale-cmd", "true {n}",
                                 "--audit", str(self.audit), "--kill-file", str(Path(self.tmp.name) / "kill")])
        self.c = Controller(a, kube=self.k)
        self.c._gain = lambda h: 1.0                          # nothing conveyed: native's target is the operator's

    def tearDown(self):
        self.tmp.cleanup()

    def records(self):
        return [json.loads(line) for line in self.audit.read_text().splitlines() if line.strip()]

    def test_a_pod_waiting_hands_the_target_back_to_native_at_once_and_holds_it(self):
        key = ("default", "web")
        self.c.changed[key], self.c.cmd_hpa[key] = 50, 30     # the operator's 50%, Omni-Compass holding 30% (more pods)
        self.c._pods_wait_handback({"hpas": [hpa(30)], "pending": 3})
        args = self.k.write.call_args[0][0]
        self.assertEqual(args[:3], ["patch", "hpa", "web"])
        self.assertEqual(json.loads(args[-1])[0]["value"], 50)  # native's target back, from the fast check
        self.assertEqual(self.c.cmd_hpa[key], 50)
        self.assertTrue(self.c._held_native(key))               # held: the decision keeps native's target
        immune = [r["immune"] for r in self.records() if "immune" in r]
        self.assertEqual((immune[0]["target_was"], immune[0]["target_back_to"], immune[0]["hold_s"]), (30, 50, 600))
        self.k.write.reset_mock()
        self.c._pods_wait_handback({"hpas": [hpa(30)], "pending": 3})
        self.k.write.assert_not_called()                        # already handed back and held: nothing written twice

    def test_a_target_at_native_is_never_touched(self):
        key = ("default", "web")
        self.c.changed[key], self.c.cmd_hpa[key] = 50, 50
        self.c._pods_wait_handback({"hpas": [hpa(50)], "pending": 3})
        self.k.write.assert_not_called()

    def test_the_hold_doubles_in_a_row_and_halves_after_a_quiet_hold(self):
        key = ("default", "web")
        self.c.changed[key], self.c.cmd_hpa[key] = 50, 30
        t = [1000.0]
        with patch("omni_controller.controller.time.time", side_effect=lambda: t[0]):
            self.c._pods_wait_handback({"hpas": [hpa(30)], "pending": 1})
            self.assertEqual(self.c.pod_hold[key][1], 600.0)
            t[0] += 601; self.c.cmd_hpa[key] = 30
            self.assertFalse(self.c._held_native(key))
            self.c._pods_wait_handback({"hpas": [hpa(30)], "pending": 1})
            self.assertEqual(self.c.pod_hold[key][1], 1200.0)     # a second hand-back in a row: twice as long
            t[0] += 1201 + 1201                                   # a quiet hold as long again
            self.assertFalse(self.c._held_native(key))
            self.assertEqual(self.c.hold_n[key], 1)               # the next hold is halved

    def test_extra_pods_leave_room_for_the_largest_rise_seen(self):
        s = {"alloc_m": 8000, "req_m": 2000, "open": 2, "nodes": 2}
        h = hpa(50, replicas=4, util=100)                         # demand: 4 pods' worth at 100% of their request
        alone = self.c._placeable_target(h, s, 20.0, 50.0, 1.0)  # room for 12 more pods of 500m: placeable 16
        held = self.c._placeable_target(h, s, 20.0, 50.0, 2.0)   # a rise of 2x seen: half the placeable pods
        self.assertEqual(alone, 25.0)                             # 100 x 4 / 16
        self.assertEqual(held, 50.0)                              # 100 x 4 / 8: no more pods than the rise leaves room for
        self.assertLess(alone, held)

    def test_no_give_back_trial_before_one_recheck_period(self):
        v = self.c.verdict
        self.assertEqual(v.last_probe, self.c.n_verdict_recheck - self.c.n_verdict_every)
        first = None
        for t in range(self.c.n_verdict_recheck + 2):
            _, trial, _ = v.tick(True)
            if trial and first is None:
                first = v.t
        self.assertGreaterEqual(first, self.c.n_verdict_recheck)   # the immune memory has watched the organism first

    def test_a_redline_omni_cannot_lift_goes_to_native_when_native_is_stronger(self):
        """omni-v21 (omnicompass/immune.py): the service over its line, Omni-Compass's pods fewer than native's own rule would ask
        and its push at its limit, native's twin (more pods, a shorter M/M/1 wait) reads lower: the target goes to native."""
        self.c.a.slo_ms = 500
        h = hpa(70, replicas=4, util=100)
        h["metadata"]["annotations"] = {"omnicompass.io/original-target-utilization": "50"}
        self.c._app_demand = lambda h_: 4.0                     # four pods' worth: native's 50% asks for eight
        answers = [self.c._immune_native(h, "default", "web", 30.0, 50.0, 30.0, 900.0) for _ in range(3)]
        self.assertEqual(answers, [False, False, True])
        self.assertTrue(any(r.get("immune", {}).get("immune") == "handed to native" for r in self.records()))

    def test_a_redline_native_cannot_beat_stays(self):
        """More pods than native would ask: native's twin waits longer, so Omni-Compass keeps the target and says so."""
        self.c.a.slo_ms = 500
        h = hpa(30, replicas=10, util=40)
        h["metadata"]["annotations"] = {"omnicompass.io/original-target-utilization": "50"}
        self.c._app_demand = lambda h_: 4.0                     # native's 50% asks for eight; Omni-Compass runs ten
        self.assertEqual([self.c._immune_native(h, "default", "web", 30.0, 50.0, 30.0, 900.0) for _ in range(4)], [False] * 4)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
