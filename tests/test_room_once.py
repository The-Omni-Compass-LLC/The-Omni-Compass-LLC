# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The room counted once (omni-v24). In one decision every push for more pods was weighed against the whole free room: in the
corrected cloud model (seed 101, 4.98 h) five services were pushed to a target of 42% together, each alone fitting the room
one machine had just left, together not; their pods waited the hundred seconds a new machine takes, and the immune system
handed every target back the same minute. Now each decision first counts the room native's own growth takes (every service's
pods at the operator's own target past those running), and each push of Omni-Compass's takes its place in what is left before
the next service's push is weighed: a push never takes the room another service's own growth needs."""
import copy
import json
import math
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omni_controller.controller import Controller, parser  # noqa: E402


def hpa(name, target=50, replicas=4, util=100):
    return {"metadata": {"name": name, "namespace": "default"},
            "spec": {"scaleTargetRef": {"kind": "Deployment", "name": name}, "minReplicas": 1, "maxReplicas": 40,
                     "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": target}}}]},
            "status": {"currentReplicas": replicas, "desiredReplicas": replicas,
                       "currentMetrics": [{"type": "Resource", "resource": {"name": "cpu", "current": {"averageUtilization": util}}}]}}


class RoomOnce(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.audit = Path(self.tmp.name) / "audit.jsonl"
        k = Mock()
        k.get.side_effect = lambda *a: {"spec": {"template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "500m"}}}]}}}}
        a = parser().parse_args(["--mode", "nodepool", "--law", "compass", "--dial", "max", "--audit", str(self.audit),
                                 "--kill-file", str(Path(self.tmp.name) / "kill")])
        self.c = Controller(a, kube=k)
        self.s = {"alloc_m": 8000, "req_m": 2000, "open": 2, "nodes": 2}       # 6,000m free: twelve more pods of 500m

    def tearDown(self):
        self.tmp.cleanup()

    def push(self, h):
        x = self.c._placeable_target(h, self.s, 20.0, 50.0, 1.0)
        self.c._claim_room((h["metadata"]["namespace"], h["metadata"]["name"]), x)
        return x

    def test_native_growth_first_then_each_push_in_the_room_left(self):
        web, api = hpa("web"), hpa("api")                # each: demand 4 pods, 4 running, the operator's target 50%
        self.c._count_native_room([web, api])
        self.assertEqual(self.c.room_native_m, 2 * 4 * 500)  # native asks 8 of each: four new pods each, 4,000m
        first = self.push(web)                           # 8 of native's + the 4 pods 2,000m holds: 100 x 4 / 12
        self.assertAlmostEqual(first, 100 * 4 / 12)
        self.assertEqual(self.c.room_claimed_m, 4 * 500)
        second = self.push(api)                          # nothing left past native's growth: the operator's own target
        self.assertEqual(second, 50.0)
        new_pods = sum(math.ceil(100 * 4 / x - 1e-9) - 4 for x in (first, second))
        self.assertLessEqual(new_pods * 500, self.s["alloc_m"] - self.s["req_m"])   # every pod asked has a place

    def test_on_omni_v23_both_pushes_took_the_whole_room(self):
        # the fault, as omni-v23 weighed it: each service alone against the whole free room, none of native's growth counted
        free = self.s["alloc_m"] - self.s["req_m"]
        alone = 100 * 4 / (4 + free // 500)
        self.assertEqual(alone, 25.0)
        self.assertGreater(2 * (math.ceil(100 * 4 / alone) - 4) * 500, free)       # 24 new pods asked for 12 places

    def test_each_decision_counts_the_room_afresh(self):
        self.c.room_claimed_m = 6000.0                   # what a decision before took
        self.c._count_native_room([])                    # the decision's loop starts the count again (controller, omni-v24)
        self.assertEqual((self.c.room_native_m, self.c.room_claimed_m), (0.0, 0.0))
        self.assertEqual(self.push(hpa("web")), 25.0)

    def test_an_unread_service_claims_nothing(self):
        h = copy.deepcopy(hpa("web")); h["status"].pop("currentMetrics")
        self.c._count_native_room([h])
        self.assertEqual(self.c.room_native_m, 0.0)
        self.assertEqual(self.push(h), 20.0)             # unread: the cover's floor, as before, and no room counted
        self.assertEqual(self.c.room_claimed_m, 0.0)

    def test_the_decision_loop_resets_the_count(self):
        text = (Path(__file__).resolve().parents[1] / "omni_controller" / "controller.py").read_text()
        self.assertIn('self._count_native_room(s["hpas"])           # each decision counts the room afresh', text)
        self.assertIn("self._claim_room((ns, name), x)", text)

    def test_the_audit_names_the_room_already_taken(self):
        self.c.room_claimed_m = 1000.0
        self.push(hpa("web"))
        rec = [json.loads(x) for x in self.audit.read_text().splitlines() if '"placeable"' in x][-1]["placeable"]
        self.assertEqual(rec["room_claimed_m"], 1000)


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
