# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The main engine's tune (tools/tune_study.py, docs/THE_TUNE.md): a tune is admissible when nothing reads LOSS against native
(and, in the cloud, no rise in the bill), dominates the main tune when no service gauge reads LOSS against it and one reads
GAIN, and the main tune stands in the searched set when it is admissible and nothing admissible dominates it."""
import sys
import tempfile
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
import tools.tune_study as TS
from tools.model_gate import PACE_GAUGES

SEEDS = [101, 102, 103, 104]


def gauges(**over):
    """One seed's gauges of the model, each 10 unless set; a small seed-dependent wobble so an interval has width."""
    return {g: over.get(g, 10.0) for g in PACE_GAUGES}


def study(setting, tune_values):
    """A study of one setting: native, and each tune's gauges as given (a function of the seed)."""
    per = {"native": {str(s): gauges() for s in SEEDS}}
    for t in TS.tunes(setting):
        f = tune_values.get(TS.key(t), lambda s: {})
        per[TS.key(t)] = {str(s): gauges(**f(s)) for s in SEEDS}
    return {"tree": "x", "seeds": SEEDS, "days": 1.0, "grids": TS.GRIDS, "main": TS.MAIN, "per_seed": {setting: per}}


def wob(s):
    return 0.01 * (s % 3)


class Rule(unittest.TestCase):
    def test_the_main_tune_stands_when_nothing_dominates_it(self):
        v = TS.judge(study("kind", {}))["kind"]
        self.assertTrue(v["main_admissible"])
        self.assertEqual(v["dominating"], [])
        self.assertTrue(v["stands"])

    def test_a_tune_with_a_service_gain_and_no_loss_dominates(self):
        ahead = "beat120-compass-center0.3"
        v = TS.judge(study("kind", {ahead: lambda s: {"alert_minutes": 8.0 + wob(s), "machine_hours": 12.0 + wob(s)}}))["kind"]
        self.assertEqual(v["dominating"], [ahead])                 # power given beside it does not stop it: the max
        self.assertFalse(v["stands"])
        self.assertEqual(v["ranked"][0], ahead)

    def test_a_tune_with_any_loss_against_native_is_not_admissible(self):
        bad = "beat15-compass-center0.2"
        v = TS.judge(study("kind", {bad: lambda s: {"alert_minutes": 6.0 + wob(s), "pending_pod_minutes_per_hour": 14.0 + wob(s)}}))["kind"]
        self.assertFalse(v["rows"][bad]["admissible"])
        self.assertNotIn(bad, v["dominating"])
        self.assertNotIn(bad, v["ranked"])

    def test_in_the_cloud_a_bigger_bill_is_not_admissible(self):
        dear = "beat30-cover-floor0.8"
        v = TS.judge(study("cloud", {dear: lambda s: {"alert_minutes": 8.0 + wob(s), "machine_hours": 11.0 + wob(s)}}))["cloud"]
        self.assertFalse(v["rows"][dear]["admissible"])
        cheap = "beat90-cover-floor1"
        v = TS.judge(study("cloud", {cheap: lambda s: {"machine_hours": 9.0 + wob(s)}}))["cloud"]
        self.assertEqual(v["dominating"], [cheap])                 # the same work for a smaller bill dominates in the cloud

    def test_the_page_carries_the_notice_and_the_verdict(self):
        with tempfile.TemporaryDirectory() as d:
            s = study("kind", {})
            TS.render(s, TS.judge(s), Path(d) / "TUNE.md")
            md = (Path(d) / "TUNE.md").read_text()
            self.assertIn("All patents, copyrights and trademarks filed in the USA", md)
            self.assertIn("It stands in the searched set", md)
            self.assertIn("No outside party has reviewed or approved these results.", md)

    def test_every_tune_reaches_the_governor_as_its_own_arguments(self):
        self.assertEqual(TS.ctl({"beat": 90, "compass-center": 0.2}), "--compass-center 0.2")
        self.assertEqual(TS.key({"beat": 90, "compass-center": 0.2}), "beat90-compass-center0.2")
        self.assertIn(TS.MAIN["kind"], TS.tunes("kind"))
        self.assertIn(TS.MAIN["cloud"], TS.tunes("cloud"))
        self.assertIn(TS.MAIN["onsite"], TS.tunes("onsite"))
        # the second search (31 October): the cover's floor reaches the governor as its own knob, the beat as the period
        self.assertEqual(TS.ctl({"beat": 10, "cover-floor": 1.0}), "--cover-floor 1")
        self.assertEqual(TS.PLANT["onsite"], "static")              # on site: the fixed machines' plant, no cluster autoscaler

    def test_a_study_is_judged_by_its_own_grids(self):
        # the first search's record (22 October) is judged by the grids it ran, whatever the tool searches now
        s = study("kind", {})
        s["grids"] = {"kind": {"beat": [60, 90], "compass-center": [0.3]}}
        s["main"] = {"kind": {"beat": 60, "compass-center": 0.3}}
        s["per_seed"]["kind"] = {k: v for k, v in s["per_seed"]["kind"].items() if k in ("native", "beat60-compass-center0.3", "beat90-compass-center0.3")}
        v = TS.judge(s)["kind"]
        self.assertEqual(set(v["rows"]), {"beat60-compass-center0.3", "beat90-compass-center0.3"})


if __name__ == "__main__":
    unittest.main()

# © 2026 The Omni-Compass LLC. All rights reserved. Evaluation and Simulation use only; any commercialization or
# monetization requires a signed, paid Omni-Compass Enterprise License. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
