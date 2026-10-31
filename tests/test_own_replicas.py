# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v19: Omni-Compass by itself (the founder's order of 23 October; docs/SOLO_PREREGISTRATION.md). The pod muscle of its own
sets the replica count of a workload the operator names (--own-replicas) and no autoscaler governs, through the workload's own
scale, by strict C's rule at the compass's target; it holds where an autoscaler governs the workload, never goes below the
operator's count at the max, writes nothing when the replicas are left native, and the reset hands the operator's count back.
In the models, a pool switched to by itself holds its count unless the brain's floor or ceiling moves it."""
import json
import subprocess
import unittest

from omni_controller.controller import Controller, parser, OWN_REPL_ANN, OWN_TARGET_ANN, OWN_RANGE_ANN


class Kube:
    """The workload default/web: its deployment (replicas, CPU request, selector, annotations) and its pods' usage."""
    def __init__(self, replicas=2, busy=1.0, target="50", rng="1,10", hpa=False):
        self.replicas, self.busy, self.hpa, self.writes = replicas, busy, hpa, []
        self.ann = {OWN_TARGET_ANN: target, OWN_RANGE_ANN: rng}
        self.audit = lambda r: None

    def get(self, *args):
        if args[:2] == ("get", "deployment"):
            return {"metadata": {"name": "web", "namespace": "default", "annotations": dict(self.ann)},
                    "spec": {"replicas": self.replicas, "selector": {"matchLabels": {"app": "web"}},
                             "template": {"spec": {"containers": [{"resources": {"requests": {"cpu": "200m"}}}]}}}}
        if args[:2] == ("top", "pods"):
            return "\n".join(f"web-{i} {int(200 * self.busy)}m 10Mi" for i in range(self.replicas))
        if args[:2] == ("get", "hpa"):
            return {"items": self._hpas()}
        raise ValueError(args)

    def _hpas(self):
        return [{"metadata": {"name": "web", "namespace": "default"}, "spec": {"scaleTargetRef": {"name": "web"}}}] if self.hpa else []

    def write(self, args, why):
        self.writes.append(list(args))
        if args[0] == "scale":
            self.replicas = int(args[-1].split("=")[1])
        elif args[0] == "annotate":
            kv = args[-1]
            if kv.endswith("-"):
                self.ann.pop(kv[:-1], None)
            else:
                k, v = kv.split("=", 1); self.ann[k] = v


def governor(k, *extra):
    a = parser().parse_args(["--mode", "nodepool", "--law", "compass", "--own-replicas", "default/web", "--audit", "", *extra])
    return Controller(a, kube=k)


def decide(c, k, slo_clean=True):
    s = {"hpas": k._hpas(), "pending": 0}
    return c._own_pods(s, {"slo_clean": slo_clean, "security_block": 0.0}, 0.6)


class OwnPace(unittest.TestCase):
    """omni-v19: between decisions the pod muscle of its own keeps the pod autoscaler's pace (every 15 s on the fast checks),
    at the target the last decision set; the compass moves the target only in a decision."""

    def test_a_check_between_decisions_adds_pods_at_once(self):
        k = Kube(replicas=2, busy=0.4); c = governor(k, "--interval", "60", "--floor-interval", "5", "--node-scale-cmd", "true")
        self.assertEqual(decide(c, k), {})                             # 2 pods at 40% against the 50% target: nothing to do
        x = dict(c.own_x)
        k.busy = 1.0                                                   # the load rises between two decisions
        c.k.get = k.get
        for _ in range(c.n_own):                                       # 15 s of 5 s checks: one reconciliation
            c._own_check()
        self.assertEqual(k.replicas, 4)                                # up at once, at the decision's own target
        self.assertEqual(c.own_x, x)                                   # the target stayed where the decision set it

    def test_the_pace_is_fifteen_seconds_at_any_beat(self):
        for beat in ("15", "60", "120"):
            c = governor(Kube(), "--interval", beat, "--floor-interval", "5")
            self.assertEqual(c.n_own, 3)
            self.assertEqual(c.n_own_window * 15, 300)                 # the window of fewer pods: 300 s at any beat


class OwnPods(unittest.TestCase):
    def test_busy_pods_get_more_at_once(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        self.assertEqual(decide(c, k), {("default", "web"): 4})       # ceil(2 x 100% / 50%) = 4, up at once
        self.assertEqual(k.writes[0], ["annotate", "deployment", "web", "-n", "default", "--overwrite", f"{OWN_REPL_ANN}=2"])
        self.assertEqual(k.writes[-1], ["scale", "deployment", "web", "-n", "default", "--replicas=4"])

    def test_an_autoscaler_on_the_workload_holds_the_muscle(self):
        k = Kube(replicas=2, busy=1.0, hpa=True); c = governor(k)
        self.assertEqual(decide(c, k), {})
        self.assertEqual(k.writes, [])

    def test_never_below_the_operators_count_at_the_max(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        decide(c, k)                                                   # 2 -> 4, the count of 2 recorded
        k.busy = 0.05
        for _ in range(3 * c.n_own_window):
            decide(c, k)
        self.assertEqual(k.replicas, 2)                                # back to the operator's count, never under it

    def test_fewer_pods_only_after_the_window(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        decide(c, k); k.busy = 0.05
        decide(c, k)
        self.assertEqual(k.replicas, 4)                                # the window's highest recommendation holds

    def test_replicas_left_native_write_nothing(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k, "--native", "replicas")
        self.assertIsNone(decide(c, k))
        self.assertEqual(k.writes, [])

    def test_no_target_named_writes_nothing(self):
        k = Kube(replicas=2, busy=1.0); k.ann.pop(OWN_TARGET_ANN); c = governor(k)
        self.assertEqual(decide(c, k), {})
        self.assertEqual(k.writes, [])

    def test_the_reset_hands_the_count_back(self):
        k = Kube(replicas=2, busy=1.0); c = governor(k)
        decide(c, k)
        c.restore()
        self.assertEqual(k.replicas, 2)
        self.assertNotIn(OWN_REPL_ANN, k.ann)


class Refusing(Kube):
    """A cluster that refuses the muscle's scale writes (a permission, an admission, an API fault) `refuse` times, then allows them."""
    def __init__(self, refuse=10 ** 9, **kw):
        super().__init__(**kw)
        self.refuse, self.hpa_spec = refuse, None

    def write(self, args, why):
        if args[0] == "scale" and self.refuse > 0:
            self.refuse -= 1
            self.writes.append(list(args) + ["(refused)"])
            raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr='Error from server (Forbidden): deployments.apps "web" is forbidden: '
                                                                              'cannot patch resource "deployments/scale"')
        if args[0] == "autoscale":
            self.writes.append(list(args)); self.hpa = True; self.hpa_spec = list(args)
            return
        super().write(args, why)


class HandBack(unittest.TestCase):
    """omni-v23 (the founder's order of 31 October): Omni direct keeps every muscle Omni-Compass cannot be. A knob whose scale
    writes the cluster refuses three times in a row goes back to native's own pod autoscaler, made from the operator's own target
    and range; the muscle then leaves the workload to it; a write that lands ends the run of refusals."""

    def test_three_refusals_hand_the_knob_to_natives_autoscaler(self):
        k = Refusing(replicas=2, busy=1.0); c = governor(k)
        for n in (1, 2):
            self.assertEqual(decide(c, k), {})
            self.assertEqual(c.own_refused[("default", "web")], n)
            self.assertFalse(k.hpa)
        self.assertEqual(decide(c, k), {})
        self.assertTrue(k.hpa)
        self.assertEqual(k.hpa_spec, ["autoscale", "deployment", "web", "-n", "default", "--cpu-percent=50", "--min=1", "--max=10"])
        self.assertIn(("default", "web"), c.own_handed)
        self.assertEqual(k.replicas, 2)                                # the count the cluster kept: never a knob nobody moves
        scale_tries = len([w for w in k.writes if w[0] == "scale"])
        self.assertEqual(decide(c, k), {})                             # the autoscaler governs it now: nothing more written
        self.assertEqual(len([w for w in k.writes if w[0] == "scale"]), scale_tries)

    def test_a_write_that_lands_ends_the_run_of_refusals(self):
        k = Refusing(refuse=2, replicas=2, busy=1.0); c = governor(k)
        decide(c, k); decide(c, k)
        self.assertEqual(c.own_refused[("default", "web")], 2)
        self.assertEqual(decide(c, k), {("default", "web"): 4})       # the third write lands
        self.assertNotIn(("default", "web"), c.own_refused)
        self.assertFalse(k.hpa)

    def test_no_range_recorded_gives_ten_times_the_operators_count(self):
        k = Refusing(replicas=3, busy=1.0); k.ann.pop(OWN_RANGE_ANN); c = governor(k)
        for _ in range(3):
            decide(c, k)
        self.assertEqual(k.hpa_spec[-2:], ["--min=1", "--max=30"])


class ModelPools(unittest.TestCase):
    def test_a_pool_by_itself_holds_its_count(self):
        from realms import harness as H
        row = next(r for r in H.catalog() if r["template"] == "compute_pool" and r["knob"] == "capacity")
        p = H.make_plant(row, 7101); p.native_off = True
        n0 = p.n + len(p.pending)
        for _ in range(60):
            p.step()
        self.assertEqual(p.n + len(p.pending), n0)

    def test_by_itself_is_the_same_arm_where_native_is_a_setting(self):
        from realms.harness import native_off_pool
        self.assertTrue(native_off_pool("compute_pool", "capacity"))
        self.assertTrue(native_off_pool("compute_pool", "setpoint"))
        self.assertFalse(native_off_pool("compute_pool", "power"))
        self.assertFalse(native_off_pool("thermal_zone", "setpoint"))


if __name__ == "__main__":
    unittest.main()
