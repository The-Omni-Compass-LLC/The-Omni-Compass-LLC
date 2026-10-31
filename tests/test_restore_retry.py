# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""omni-v22: the hand-back lands. On 30 October (six-kube run 41044680505, repetition 346) one 500 from the cluster's API on the
autoscaler list, at the reset, ended the governor's whole hand-back on its first read: the conveyed CPU limits (1230m, 1850m) and the
replica range (1 to 13) stayed behind and the arm was marked invalid. Now every step of the hand-back is tried RESTORE_TRIES times
against a transient failure, each muscle on its own, and what did not land is raised, never silent."""
import json
import subprocess
import unittest
from unittest import mock

from omni_controller import controller as C
from omni_controller import muscles as M
from omni_controller.controller import ANNOTATION, RANGE_ANN, Controller, parser

HPA = {"metadata": {"name": "php-apache", "namespace": "default", "annotations": {RANGE_ANN: "1,10", ANNOTATION: "50"}},
       "spec": {"scaleTargetRef": {"name": "php-apache"}, "minReplicas": 1, "maxReplicas": 13,
                "metrics": [{"type": "Resource", "resource": {"name": "cpu", "target": {"type": "Utilization", "averageUtilization": 80}}}]}}


class Weather:
    """A cluster whose API answers 500 to the first `fail` reads and writes, as the overloaded kind runner's did."""

    def __init__(self, fail=0):
        self.fail, self.writes, self.reads = fail, [], 0

    def _storm(self, what):
        if self.fail > 0:
            self.fail -= 1
            raise subprocess.CalledProcessError(1, ["kubectl", *what], stderr="API 500 for apis/autoscaling/v2/horizontalpodautoscalers")

    def get(self, *args):
        self.reads += 1
        self._storm(args)
        if args[:2] == ("get", "hpa"):
            return {"items": [json.loads(json.dumps(HPA))]}
        if args[:2] == ("get", "deployment"):
            return {"metadata": {"name": "php-apache", "namespace": "default", "annotations": {}}, "spec": {"replicas": 2}}
        return {"items": []}

    def write(self, args, why):
        self._storm(args)
        self.writes.append((list(args), why))


def governor(k):
    a = parser().parse_args(["--mode", "nodepool", "--law", "compass", "--audit", ""])
    c = Controller(a, kube=k)
    c.records = []
    c.audit = lambda rec: (c.records.append(rec), rec)[1]
    return c


class HandBack(unittest.TestCase):
    def setUp(self):
        self.sleeps = []
        self.p1 = mock.patch.object(C.time, "sleep", lambda s: self.sleeps.append(s)); self.p1.start()
        self.p2 = mock.patch.object(M.time, "sleep", lambda s: self.sleeps.append(s)); self.p2.start()

    def tearDown(self):
        self.p1.stop(); self.p2.stop()

    def test_one_500_on_the_autoscaler_list_no_longer_ends_the_hand_back(self):
        k = Weather(fail=1); c = governor(k)
        c.restore()
        whys = [w for _, w in k.writes]
        self.assertIn("reset: restore the HPA's own replica range", whys)
        self.assertIn("reset: restore original HPA target", whys)
        self.assertIn("reset: remove range record", whys); self.assertIn("reset: remove record", whys)
        errs = [r for r in c.records if "error" in r and r["error"].startswith("restore:")]
        self.assertEqual(len(errs), 1, errs); self.assertEqual(errs[0]["attempt"], 1); self.assertEqual(errs[0]["of"], M.RESTORE_TRIES)
        self.assertEqual(self.sleeps, [1.0], "one second before the second try")

    def test_a_storm_through_every_try_is_raised_and_named_never_silent(self):
        k = Weather(fail=10 ** 6); c = governor(k)
        with self.assertRaises(RuntimeError) as cm:
            c.restore()
        self.assertIn("hand-back incomplete", str(cm.exception)); self.assertIn("autoscalers", str(cm.exception))
        self.assertEqual(k.reads, M.RESTORE_TRIES, "the list tried RESTORE_TRIES times, no more")
        self.assertEqual(len(self.sleeps), M.RESTORE_TRIES - 1); self.assertLessEqual(sum(self.sleeps), 15.0, "inside the rig's 60 s wait")

    def test_the_range_and_the_target_are_tried_on_their_own(self):
        k = Weather(fail=0); c = governor(k)
        failing = {"n": 2}
        real_write = k.write

        def write(args, why):
            if why == "reset: restore the HPA's own replica range" and failing["n"] > 0:
                failing["n"] -= 1
                raise subprocess.CalledProcessError(1, ["kubectl", *args], stderr="API 500")
            real_write(args, why)
        k.write = write
        c.restore()
        whys = [w for _, w in k.writes]
        self.assertEqual(whys.count("reset: restore the HPA's own replica range"), 1, "landed on the third try")
        self.assertIn("reset: restore original HPA target", whys, "the target's hand-back never waited on the range's")

    def test_the_muscles_name_the_lever_that_did_not_land(self):
        k = Weather(fail=0); c = governor(k)
        calls = {"n": 0}

        def stormy():
            calls["n"] += 1
            raise OSError("connection reset")
        c.m._restore_core = stormy
        with self.assertRaises(RuntimeError) as cm:
            c.restore()
        self.assertIn("kill hardware and power cap", str(cm.exception))
        self.assertEqual(calls["n"], M.RESTORE_TRIES)
        whys = [w for _, w in k.writes]
        self.assertIn("reset: restore original HPA target", whys, "the autoscaler's hand-back landed before the muscle failed")

    def test_a_fault_that_is_not_the_apis_weather_is_not_retried(self):
        k = Weather(fail=0); c = governor(k)
        calls = {"n": 0}

        def broken():
            calls["n"] += 1
            raise KeyError("cooling_restore_c")
        c.m._restore_cooling = broken
        with self.assertRaises(RuntimeError):
            c.restore()
        self.assertEqual(calls["n"], 1, "a programming fault is reported at once, not retried")
        self.assertEqual(self.sleeps, [])


if __name__ == "__main__":
    unittest.main()
