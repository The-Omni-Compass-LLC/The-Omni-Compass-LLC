# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The brain's own verdict on a live knob (tools/knob_verdict.py), around the frozen engine's Verdict: every knob starts in
watch; a spend that costs more than it buys is refused and the knob stays native; a give-back that costs nothing is allowed
one step a trial; a trial holds the knob whatever the compass asks; the compass is clamped to the allowance between trials;
native is always free."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from tools import knob_verdict as kv  # noqa: E402


def run_knob(verdict, seconds, wanted_of, spend_ok_of, give_ok_of, cost_of):
    """Drive a knob for a number of seconds: the compass's wish, the conditions and the cost all follow the knob's value."""
    cur = verdict.native
    trace = []
    for t in range(seconds):
        verdict.observe(cost_of(cur, t), float(t))
        target, why, info = verdict.decide(wanted_of(cur, t), spend_ok_of(cur, t), give_ok_of(cur, t), float(t), "compass")
        trace.append((t, cur, target, info["verdict_phase"], why))
        cur = target
    return trace


class TheCost(unittest.TestCase):
    def test_the_two_objectives(self):
        self.assertAlmostEqual(kv.sample_cost(kv.RESOURCE, work=100.0, latency=0.002, resource=64, cpu_share=0.5), 64 * 0.5 * 0.002 / 100)
        self.assertAlmostEqual(kv.sample_cost(kv.SERVICE, work=100.0, latency=0.002, resource=64, cpu_share=0.5), 0.002 / 100)
        self.assertIsNone(kv.sample_cost(kv.RESOURCE, work=0, latency=0.002, resource=64, cpu_share=0.5), "nothing worked: nothing measured")
        self.assertIsNone(kv.sample_cost(kv.RESOURCE, work=None, latency=0.002, resource=64, cpu_share=0.5))
        with self.assertRaises(ValueError):
            kv.KnobVerdict(64, 8, (16, 512), objective="speed")


class ASpendKnob(unittest.TestCase):
    """A cache's ceiling: each notch of memory buys one percent of latency. Under the resource objective that is a loss; under
    the service objective a gain."""

    @staticmethod
    def cost(objective):
        def f(cur, t):
            latency = 0.002 * (1.0 - 0.01 * (cur - 64) / 8)          # one percent faster a notch
            return kv.sample_cost(objective, work=1000.0, latency=latency, resource=cur, cpu_share=0.3)
        return f

    def test_a_spend_that_costs_more_than_it_buys_is_refused_and_the_knob_stays_native(self):
        v = kv.KnobVerdict(64, 8, (16, 512), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        trace = run_knob(v, 300, wanted_of=lambda cur, t: 512, spend_ok_of=lambda cur, t: True, give_ok_of=lambda cur, t: False, cost_of=self.cost(kv.RESOURCE))
        self.assertEqual(v.state, "left native")
        self.assertGreaterEqual(v.counts["refused"], 2, "the first notch was tried, refused, and tried again after the recheck")
        self.assertEqual(v.counts["allowed"], 0)
        values = {target for _, _, target, _, _ in trace}
        self.assertEqual(values, {64, 72}, "the knob never went past the one notch under trial; the compass's wish of 512 was never granted")
        self.assertGreater(v.counts["clamped"], 100)
        self.assertEqual(trace[-1][2], 64)

    def test_the_same_spend_pays_under_the_service_objective(self):
        v = kv.KnobVerdict(64, 8, (16, 512), objective=kv.SERVICE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        trace = run_knob(v, 300, wanted_of=lambda cur, t: 512, spend_ok_of=lambda cur, t: True, give_ok_of=lambda cur, t: False, cost_of=self.cost(kv.SERVICE))
        self.assertTrue(v.state.startswith("acting"))
        self.assertGreaterEqual(v.verdicts[kv.SPEND].allowed, 5, "one notch a trial, as far as the trials got")
        self.assertEqual(v.counts["refused"], 0)
        self.assertLessEqual(max(target for _, _, target, _, _ in trace), v.allowed_high, "never past the allowance, even with the compass asking for the top of the cover")

    def test_a_trial_holds_the_knob_whatever_the_compass_asks(self):
        v = kv.KnobVerdict(64, 8, (16, 512), objective=kv.SERVICE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        trace = run_knob(v, 12, wanted_of=lambda cur, t: 64 if t % 2 else 512, spend_ok_of=lambda cur, t: True, give_ok_of=lambda cur, t: False, cost_of=self.cost(kv.SERVICE))
        first_allowed = next(e["t"] for e in v.events if e["verdict"] == "step allowed")
        ref = [x for x in trace if x[3] == "ref" and x[0] < first_allowed]; trial = [x for x in trace if x[3] == "trial" and x[0] < first_allowed]
        self.assertTrue(ref and trial)
        self.assertTrue(all(x[2] == 64 for x in ref), "the first reference stands at native (the deepest step allowed so far)")
        self.assertTrue(all(x[2] == 72 for x in trial), "the trial stands one notch further")
        self.assertGreater(v.counts["held"], 0)
        self.assertEqual(v.verdicts[kv.SPEND].allowed, 1, "allowed; the next reference will stand at 72 (incremental)")

    def test_a_spend_trial_runs_on_when_its_own_gain_calms_the_compass(self):
        """The trial's success removes the reason for it (the queue drains, the force drops): the trial must still finish."""
        v = kv.KnobVerdict(2, 1, (1, 8), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        trace = run_knob(v, 60, wanted_of=lambda cur, t: 8,
                         spend_ok_of=lambda cur, t: cur == 2,          # the compass asks only while the knob is native
                         give_ok_of=lambda cur, t: False,
                         cost_of=lambda cur, t: kv.sample_cost(kv.RESOURCE, work=100.0 * cur, latency=1.0 / cur ** 2, resource=cur, cpu_share=0.3))
        self.assertEqual(v.counts["abandoned"], 0)
        self.assertGreaterEqual(v.counts["allowed"], 1, "the consumer that drains the queue pays, and the step is allowed")

    def test_a_spend_trial_is_not_ended_by_the_calm_it_causes(self):
        """Amendment 3 (10 October 2026): the harness tells the verdict the service is calm the moment the spend works (the
        force drops below the cushion). The spend trial must still run to its samples and be judged; only the wall ends it."""
        v = kv.KnobVerdict(2, 1, (1, 8), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        cur = 2
        for t in range(60):
            v.observe(kv.sample_cost(kv.RESOURCE, work=100.0 * cur, latency=1.0 / cur ** 2, resource=cur, cpu_share=0.3), float(t))
            calm = cur > 2                                   # the extra consumer drains the queue: the compass reads calm at once
            target, why, info = v.decide(8, spend_ok=(cur == 2), give_ok=False, t=float(t), why="compass", stress=not calm, calm=calm)
            cur = target
        self.assertEqual(v.counts["abandoned"], 0, "the calm the spend causes never ends its own trial")
        self.assertGreaterEqual(v.counts["allowed"], 1)
        # the wall still ends every trial
        v2 = kv.KnobVerdict(2, 1, (1, 8), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        cur = 2
        for t in range(8):
            v2.observe(kv.sample_cost(kv.RESOURCE, work=100.0, latency=0.5, resource=cur, cpu_share=0.3), float(t))
            target, why, info = v2.decide(8, spend_ok=(cur == 2), give_ok=False, t=float(t), why="compass", stress=True, calm=False, fail_up=(t == 6))
            cur = target
        self.assertEqual(v2.counts["abandoned"], 1, "a fail-up abandons the running trial")
        self.assertEqual(cur, 2, "and the fail-up is clamped to the allowance: with no step allowed yet, native")

    def test_a_give_back_trial_still_ends_when_the_service_leaves_calm(self):
        v = kv.KnobVerdict(20, 1, (2, 20), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        cur = 20
        for t in range(12):
            v.observe(kv.sample_cost(kv.RESOURCE, work=100.0, latency=0.01, resource=cur, cpu_share=0.3), float(t))
            stress = t >= 6                                  # the service leaves calm mid-trial
            target, why, info = v.decide(2, spend_ok=False, give_ok=not stress, t=float(t), why="compass", stress=stress, calm=not stress)
            cur = target
        self.assertEqual(v.counts["abandoned"], 1, "the engine's rule: never a give-back trial under stress")
        self.assertEqual(cur, 20, "the knob is back at native")


class AGiveBackKnob(unittest.TestCase):
    """A pool: connections given back cost nothing while the service holds."""

    @staticmethod
    def cost(cur, t):
        return kv.sample_cost(kv.RESOURCE, work=500.0, latency=0.004, resource=cur, cpu_share=0.4)

    def test_each_step_back_is_allowed_one_trial_at_a_time_and_the_compass_is_clamped_to_them(self):
        v = kv.KnobVerdict(20, 1, (2, 90), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        trace = run_knob(v, 400, wanted_of=lambda cur, t: 2, spend_ok_of=lambda cur, t: False, give_ok_of=lambda cur, t: True, cost_of=self.cost)
        self.assertGreaterEqual(v.verdicts[kv.GIVE].allowed, 8)
        self.assertEqual(v.counts["refused"], 0)
        self.assertTrue(all(target >= v.allowed_low for _, _, target, _, _ in trace), "never deeper than the allowance")
        self.assertEqual(trace[-1][2], v.allowed_low, "the compass, wanting the floor, gets the allowance")

    def test_native_is_always_free_and_a_spend_above_native_is_not(self):
        v = kv.KnobVerdict(20, 1, (2, 90), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        run_knob(v, 100, wanted_of=lambda cur, t: 2, spend_ok_of=lambda cur, t: False, give_ok_of=lambda cur, t: True, cost_of=self.cost)
        self.assertGreater(v.verdicts[kv.GIVE].allowed, 0)
        target, why, _ = v.decide(20, False, False, 101.0, "fail up: handed back to the pooler's own setting", fail_up=True)
        self.assertEqual(target, 20, "back to the operator's setting, always: a fail-up ends any trial")
        self.assertIsNone(v.phase_dir)
        target, why, _ = v.decide(36, True, False, 102.0, "slow, clients waiting for a server: 16 more")
        self.assertLessEqual(target, 21, "above native only one notch, and only as a trial; the add rule's sixteen are not granted")
        target, why, _ = v.decide(600, True, False, 103.0, "fail up: a quarter of the cover at once", fail_up=True)
        self.assertEqual(target, 20, "a fail-up never spends beyond the allowance")

    def test_a_give_back_that_hurts_the_service_is_refused(self):
        def cost(cur, t):
            latency = 0.004 * (1.0 + 0.5 * (20 - cur))                   # fifty percent slower a connection fewer
            return kv.sample_cost(kv.RESOURCE, work=500.0, latency=latency, resource=cur, cpu_share=0.4)
        v = kv.KnobVerdict(20, 1, (2, 90), objective=kv.RESOURCE, min_samples=5, probe_every=10, recheck=30, settle_s=1.0)
        run_knob(v, 200, wanted_of=lambda cur, t: 2, spend_ok_of=lambda cur, t: False, give_ok_of=lambda cur, t: True, cost_of=cost)
        self.assertEqual(v.state, "left native")
        self.assertGreater(v.counts["refused"], 0)


class TheRecord(unittest.TestCase):
    def test_the_record_and_the_summary(self):
        v = kv.KnobVerdict(64, 8, (16, 512), min_samples=3, probe_every=5, recheck=10, settle_s=0.0)
        run_knob(v, 30, wanted_of=lambda cur, t: 64, spend_ok_of=lambda cur, t: False, give_ok_of=lambda cur, t: False, cost_of=lambda cur, t: 1.0)
        r = v.record()
        self.assertEqual(r["state"], "left native")
        self.assertEqual(r["counts"]["trials"], 0, "no condition, no trial: watch")
        self.assertIn("left native (0 trials, 0 allowed, 0 refused)", kv.summarize([r]))
        self.assertEqual(kv.summarize([]), "no verdict record")


if __name__ == "__main__":
    unittest.main()
