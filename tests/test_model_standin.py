# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The model's stand-in cluster (pilot/selfpilot.py), corrected on 31 October: every pod is its own object with the metadata a real
cluster gives it, and the autoscaler's range is taken as the API takes it (a merge patch). Before, the pods carried no metadata
and the list repeated one object per workload: the governor's count of the room beside a workload failed on its first pod (4 to
7 decisions a day lost in the pace models, on every engine read before), every running pod of a workload read as on one machine,
and the raise of the autoscaler's range never landed. And the on-site plant of the gate (tools/model_gate.py, StaticFineSim,
pace_onsite): the kind rig's own machines, made at the start, no cluster autoscaler."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from pilot.selfpilot import SimCluster, SimKube  # noqa: E402


class StandIn(unittest.TestCase):
    def setUp(self):
        self.sim = SimCluster(101, days=0.01)
        self.sim.tick()                                   # one step, so the cluster's own counts exist
        self.kube = SimKube(self.sim, lambda rec: None)

    def test_every_pod_is_its_own_object_with_its_metadata(self):
        items = self.kube.get("get", "pods")["items"]
        self.assertTrue(items)
        names = [p["metadata"]["name"] for p in items]
        self.assertEqual(len(names), len(set(names)))                       # one object per pod, never one repeated
        for p in items:
            self.assertEqual(p["metadata"]["namespace"], "default")
            self.assertIn("app", p["metadata"]["labels"])
            self.assertIn(p["status"]["phase"], ("Running", "Pending"))
        w = self.sim.c.workloads[0]
        self.assertEqual(sum(p["metadata"]["labels"]["app"] == w.name for p in items), int(w.replicas))

    def test_the_autoscalers_range_lands_as_the_api_takes_it(self):
        w = self.sim.c.workloads[0]
        body = json.dumps({"spec": {"maxReplicas": w.max_rep + 3, "minReplicas": 2}})
        before = w.max_rep
        self.kube.write(["patch", "hpa", w.name, "--type", "merge", "-p", body], "test")
        self.assertEqual((w.max_rep, w.min_rep), (before + 3, 2))

    def test_the_autoscalers_target_still_lands_as_a_json_patch(self):
        w = self.sim.c.workloads[0]
        self.kube.write(["patch", "hpa", w.name, "--type", "json", "-p", json.dumps([{"op": "replace", "path": "/x", "value": 55}])], "t")
        self.assertAlmostEqual(w.target, 0.55)


class OnSitePlant(unittest.TestCase):
    def test_the_gate_reads_the_on_site_plant(self):
        text = (ROOT / "tools" / "model_gate.py").read_text()
        self.assertIn("class StaticFineSim(FineSim)", text)
        self.assertIn('("pace_onsite", "static")', text)
        self.assertIn('if self.autoscaler == "ca":', text)                 # no cluster autoscaler on machines already paid for


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
