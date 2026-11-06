# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v13, the conveyance (omni_controller/muscles.py, convey): another muscle's room is never conveyed.

1. Every other pod on a machine is counted by what it may use: its own limit where it has one, its request where it has
   none (omni-v12 and before counted requests alone, so a batch pod's room between its request and its limit read idle).
2. On a shared host (kind) at its top (busy at or over 75%) while another workload there has room of its own (a limit
   above its request), the limits given go back to the operator's; under the top but within the band's 5% cushion, no
   limit is raised again. A host with no such workload keeps the v7 rule (raises held at the top, limits given stay).

KubeRay's rig with the organism alone, 20 October (docs/OMNI_V13.md): the web pods' limits were raised to 3,700m in the
queue's first half minute and kept through the saturated queue; the batch pods hashed 7.6% slower, the queue finished
0.7% later (LOSS in all three runs) and the web served no faster while the queue ran."""
import unittest

from tests.test_convey_shared_host import Cluster, Stat, muscles, node, pod


def batch(name, node_name):
    """A batch pod as the KubeRay rig's stream runs it: 500m requested, a 1-core limit."""
    return pod(name, node_name, app="omni-batch-stream", req="500m", limit="1")


class Handback(unittest.TestCase):
    def kind(self, extra=(), limit="500m"):
        nodes = [node("w1"), node("w2"), node("w3")]
        pods = [pod("web-1", "w1", limit=limit), pod("web-2", "w2", limit=limit), pod("web-3", "w3", limit=limit),
                pod("dns", "w1", app="coredns", req="300m", limit="300m", ns="kube-system")] + list(extra)
        return Cluster(nodes, pods)

    def test_other_pods_are_counted_by_their_own_limit(self):
        """Under the cushion the arithmetic runs, every other pod counted by its limit: w2 carries a batch pod (500m
        requested, 1 core limit), so web-2 may have 0.95 x 4000 - 1000 = 2800m, not the 3300m omni-v12 conveyed."""
        c, stat = self.kind([batch("b-1", "w2")]), Stat(0.40)
        m, events = muscles(c, stat)
        self.assertEqual(m.convey(), {"default/web-1": 3500, "default/web-2": 2800, "default/web-3": 3800})

    def test_the_top_with_another_workloads_room_hands_every_limit_back(self):
        c, stat = self.kind([batch("b-1", "w2"), batch("b-2", "w3")], limit="3700m"), Stat(0.80)
        m, events = muscles(c, stat)
        out = m.convey()
        self.assertEqual(out, {"default/web-1": 500, "default/web-2": 500, "default/web-3": 500})
        whys = [why for args, why in c.writes if args[0] == "patch"]
        self.assertTrue(whys and all("at its top" in w for w in whys))
        self.assertTrue(any(e.get("convey") == "handed back" for e in events))

    def test_within_the_cushion_nothing_is_raised_and_nothing_handed_back(self):
        c, stat = self.kind([batch("b-1", "w2")]), Stat(0.72)
        for p in c.pods[:1]:
            p["spec"]["containers"][0]["resources"]["limits"]["cpu"] = "3500m"
        m, events = muscles(c, stat)
        out = m.convey()
        # web-1 already holds w1's 3500m: it stays; web-2 and web-3 at 500m are not raised inside the cushion
        self.assertEqual(out, {})
        self.assertFalse(any(a[0] == "patch" for a, _ in c.writes))
        held = [e for e in events if e.get("convey") == "held"]
        self.assertTrue(held and held[0]["machines"] == ["w2", "w3"])

    def test_under_the_cushion_the_room_is_conveyed_again(self):
        c, stat = self.kind([batch("b-1", "w2")]), Stat(0.65)
        m, events = muscles(c, stat)
        self.assertEqual(m.convey(), {"default/web-1": 3500, "default/web-2": 2800, "default/web-3": 3800})

    def test_a_host_with_no_room_but_its_own_keeps_the_v7_rule(self):
        """Only the serving pods and pods without room of their own (a limit equal to the request, or none): the host's
        top holds raises and keeps the limits given, as omni-v7 to omni-v12 did; nothing is handed back."""
        c, stat = self.kind(limit="3800m"), Stat(0.80)
        m, events = muscles(c, stat)
        out = m.convey()
        # web-1 shares w1 with coredns (300m, its limit its request): 3800 -> 3500 is a lowering, written at the top
        self.assertEqual(out, {"default/web-1": 3500})
        self.assertFalse(any(e.get("convey") == "handed back" for e in events))

    def test_an_unread_host_holds_and_hands_nothing_back(self):
        """A host whose busy share cannot be read is blind, never at its top (the omni-v11 rule): raises held, limits
        given kept."""
        c = self.kind([batch("b-1", "w2")], limit="3700m")
        m, events = muscles(c, None)
        out = m.convey()
        # the lowerings to each node's own arithmetic go on (w1 3500m, w2 2800m beside its batch pod); w3's raise is held
        self.assertEqual(out, {"default/web-1": 3500, "default/web-2": 2800})
        self.assertFalse(any(e.get("convey") == "handed back" for e in events))

    def test_separate_machines_count_limits_and_never_hand_back(self):
        nodes = [node("a", kind=False), node("b", kind=False)]
        c = Cluster(nodes, [pod("web-1", "a"), pod("web-2", "b"), batch("b-1", "b"), batch("b-2", "b")])
        m, events = muscles(c, None)
        # b: 0.95 x 4000 - 2 x 1000 = 1800m (omni-v12: 0.95 x 4000 - 2 x 500 = 2800m)
        self.assertEqual(m.convey(), {"default/web-1": 3800, "default/web-2": 1800})
        self.assertFalse(any(e.get("convey") in ("held", "handed back") for e in events))


if __name__ == "__main__":
    unittest.main()
