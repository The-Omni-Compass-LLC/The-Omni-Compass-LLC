# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v27, the conveyance (omni_controller/muscles.py, convey): no CPU another workload is owed is conveyed.

1. Koordinator's best-effort pod asks for its CPU only in Koordinator's reclaimed processor (kubernetes.io/batch-cpu, in
   millicores: request 500, limit 1k on the batch rigs). omni-v26 read it as using nothing, so its CPU was conveyed to the
   serving pods: on Koordinator's rigs on omni-v25 its batch processor stood 11% smaller at the window's end and the queue waited
   longer for a place (docs/LOSS_CAUSES_2026-11-07.md). It is counted now by what it may use, and it has room of its own.
2. While another workload's pods wait for a place (Pending on no machine, of no workload an HPA scales, a DaemonSet's aside),
   nothing is raised and each limit given steps back by half its raise at each pass, as omni-v26 holds native's target for them.
"""
import unittest

from omni_controller.muscles import claim_m, has_room, qty
from tests.test_convey_shared_host import Cluster, muscles, node, pod


def best_effort(name, node_name, phase="Running"):
    """A Koordinator best-effort pod as the batch rigs run it: its CPU asked only of Koordinator's batch processor."""
    p = pod(name, node_name, app="omni-batch-stream", phase=phase)
    p["spec"]["containers"][0]["resources"] = {"limits": {"kubernetes.io/batch-cpu": "1k", "kubernetes.io/batch-memory": "64Mi"},
                                               "requests": {"kubernetes.io/batch-cpu": "500", "kubernetes.io/batch-memory": "64Mi"}}
    return p


def unplaced(p):
    p["spec"].pop("nodeName", None)
    p["status"]["phase"] = "Pending"
    return p


def machines():
    return [node("a", kind=False), node("b", kind=False)]


class Owed(unittest.TestCase):
    def test_koordinators_batch_processor_is_read_as_cpu(self):
        c = best_effort("be-1", "a")["spec"]["containers"][0]
        self.assertEqual((qty("1k"), qty("500"), qty("250m")), (1000.0, 500.0, 0.25))
        self.assertEqual(claim_m(c), 1000.0)
        self.assertTrue(has_room(best_effort("be-1", "a")))
        # a pod with only CPU keeps omni-v13's reading
        self.assertEqual(claim_m(pod("x", "a", req="200m", limit="500m")["spec"]["containers"][0]), 500.0)

    def test_best_effort_pods_are_counted_on_their_machine(self):
        # b carries two best-effort pods: 0.95 x 4000 - 2 x 1000 = 1800m for web-2 (omni-v26 conveyed 3800m)
        c = Cluster(machines(), [pod("web-1", "a"), pod("web-2", "b"), best_effort("be-1", "b"), best_effort("be-2", "b")])
        m, events = muscles(c)
        self.assertEqual(m.convey(), {"default/web-1": 3800, "default/web-2": 1800})

    def test_another_workloads_waiting_pods_hold_every_raise_and_take_half_back(self):
        c = Cluster(machines(), [pod("web-1", "a", limit="3700m"), pod("web-2", "b", limit="500m"),
                                 unplaced(pod("job-1", "b", app="omni-batch-stream", req="500m", limit="1"))])
        m, events = muscles(c)
        out = m.convey()
        # web-1 gives back half its raise (3700m -> 2100m); web-2 is not raised
        self.assertEqual(out, {"default/web-1": 2100})
        whys = [why for args, why in c.writes if args[0] == "patch"]
        self.assertTrue(whys and all("wait for a place" in w for w in whys))
        owed = [e for e in events if e.get("convey") == "owed"]
        self.assertTrue(owed and owed[0]["others_waiting"] == 1)
        # once the job has its place the room is conveyed again, the job counted on its machine
        job = c.pods[2]
        job["spec"]["nodeName"], job["status"]["phase"] = "b", "Running"
        self.assertEqual(m.convey(), {"default/web-1": 3800, "default/web-2": 2800})

    def test_a_governed_services_waiting_pod_keeps_the_raise(self):
        # another service an HPA scales keeps its own rule (omni-v19's hand-back, omni-v26's decision): its pod waiting for a
        # machine is not a queue's
        c = Cluster(machines(), [pod("web-1", "a"), pod("web-2", "b"), unplaced(pod("api-1", "b", app="api"))])
        m, events = muscles(c)
        m.served = lambda: [("default", {"app": "web"}), ("default", {"app": "api"})]
        self.assertEqual(m.convey(), {"default/web-1": 3800, "default/web-2": 3800})
        self.assertFalse(any(e.get("convey") == "owed" for e in events))

    def test_a_daemonsets_pod_and_the_services_own_pod_keep_the_raise(self):
        ds = unplaced(pod("proxy-new", "b", app="kube-proxy", ns="kube-system"))
        ds["metadata"]["ownerReferences"] = [{"kind": "DaemonSet", "name": "kube-proxy"}]
        c = Cluster(machines(), [pod("web-1", "a"), pod("web-2", "b"), ds, unplaced(pod("web-3", "b"))])
        m, events = muscles(c)
        self.assertEqual(m.convey(), {"default/web-1": 3800, "default/web-2": 3800})
        self.assertFalse(any(e.get("convey") == "owed" for e in events))


class Wired(unittest.TestCase):
    def test_the_governor_hands_the_conveyance_its_autoscaled_workloads(self):
        # the conveyance reads which workloads an HPA scales from the governor's last decision (its snapshot and the selector
        # each HPA's deployment carries), so another service's waiting pod is never read as a queue's
        import tempfile
        from tests.test_neighbour_hold import cluster, controller
        with tempfile.TemporaryDirectory() as tmp:
            cluster(tmp)
            c = controller(tmp)
            self.assertEqual(c.m.served(), [])            # before the first decision: nothing read yet
            c.step()
            self.assertEqual(c.m.served(), [("default", {"app": "web"})])


if __name__ == "__main__":
    unittest.main()
