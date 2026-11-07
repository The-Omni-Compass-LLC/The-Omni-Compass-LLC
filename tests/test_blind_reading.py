# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""A reading with no machine in service is blind, never an overload (omni-v11). On 18 October, in the CruiseKube test (run
39120444653, repetition 8), every worker of the kind cluster left service for two minutes while the service answered every
probe. omni-v10's governor read the load against no capacity, then divided by it: two decisions and a floor check failed.
omni-v11 holds: it records why, decides nothing from the reading, writes nothing, and keeps the last reading with machines."""
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from omni_controller.controller import Controller, parser  # noqa: E402

CP = {"metadata": {"name": "cp", "labels": {"node-role.kubernetes.io/control-plane": ""}},
      "spec": {"taints": [{"key": "node-role.kubernetes.io/control-plane", "effect": "NoSchedule"}]},
      "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}


def node(name, out_of_service):
    taints = [{"key": "node.kubernetes.io/unreachable", "effect": "NoSchedule"}] if out_of_service else []
    return {"metadata": {"name": name, "labels": {}}, "spec": {"taints": taints},
            "status": {"allocatable": {"cpu": "4"}, "conditions": [{"type": "Ready", "status": "True"}]}}


class Cluster:
    """Two workers serving one pod each; `out` takes both out of service in the reading."""
    def __init__(self):
        self.out = False

    def get(self, *args):
        if args[:2] == ("get", "nodes"):
            return {"items": [CP, node("w1", self.out), node("w2", self.out)]}
        if args[:2] == ("get", "pods") and "--field-selector=status.phase=Pending" in args:
            return "pod/p3"                                  # a pod waits, so the floor check reads the cluster
        if args[:2] == ("get", "pods"):
            pod = lambda n, w: {"metadata": {"name": n}, "spec": {"nodeName": w, "containers": [
                {"resources": {"requests": {"cpu": "500m"}}}]}, "status": {"phase": "Running"}}
            return {"items": [pod("p1", "w1"), pod("p2", "w2")]}
        if args[:2] == ("top", "nodes"):
            return "w1 900m 22%\nw2 800m 20%\n"
        if args[:2] == ("get", "hpa"):
            return {"items": []}
        raise ValueError(args)


class BlindReading(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.audit = Path(self.tmp.name) / "audit.jsonl"
        self.cluster = Cluster()
        k = Mock(); k.get.side_effect = self.cluster.get
        a = parser().parse_args(["--mode", "nodepool", "--active-nodes-only", "--node-scale-cmd", "true {n}",
                                 "--audit", str(self.audit), "--kill-file", str(Path(self.tmp.name) / "kill")])
        self.k = k
        self.c = Controller(a, kube=k)

    def tearDown(self):
        self.tmp.cleanup()

    def records(self):
        return [json.loads(line) for line in self.audit.read_text().splitlines() if line.strip()]

    def test_a_reading_with_no_machine_in_service_is_held_never_divided_by(self):
        self.c.step()                                         # a reading with machines first
        snap = self.c._snap
        self.assertEqual(snap["nodes"], 2)
        self.cluster.out = True
        self.c.step()                                         # omni-v10: ZeroDivisionError
        held = [r for r in self.records() if str(r.get("decision", "")).startswith("held")]
        self.assertEqual(len(held), 1)
        self.assertIn("no machine in service", held[0]["decision"])
        self.assertIs(self.c._snap, snap)                     # the last reading with machines stays
        self.assertIsNone(self.c.floor_step())                # the floor check holds too
        self.k.write.assert_not_called()

    def test_the_governor_takes_up_again_when_the_machines_return(self):
        self.cluster.out = True
        self.c.step()
        self.cluster.out = False
        self.c.step()
        decided = [r for r in self.records() if isinstance(r.get("decision"), dict)]
        self.assertEqual(len(decided), 1)
        self.assertEqual(decided[0]["decision"]["nodes_observed"], 2)
        self.assertFalse(any("error" in r for r in self.records()))


if __name__ == "__main__":
    unittest.main()
