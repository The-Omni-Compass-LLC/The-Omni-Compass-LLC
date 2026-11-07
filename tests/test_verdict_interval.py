# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The verdict in words (Omni v7, omnicompass/verdict.py, judge="interval"): on noisy work, a step that truly costs more
than the allowance is almost never allowed (far less often than the medians alone allowed it), a step that truly costs
nothing is still allowed, a clear rise reads LOSS, and an open interval measures on before it decides."""
import random
import unittest

from omnicompass.verdict import Verdict, change_interval


def trial_outcome(true_rise, judge, seed, tol=0.02, sigma=0.25, n=60):
    """One give-back trial on log-normal costs: reference at native, trial at step 1 costing true_rise more."""
    rng = random.Random(seed)
    v = Verdict(tolerance=tol, min_samples=n, probe_every=1, recheck=10 ** 6, max_trial=40, judge=judge)
    step = 0
    for _ in range(60):
        base = 10.0 * (1.0 + true_rise * step)
        v.observe([base * rng.lognormvariate(0.0, sigma) for _ in range(20)])
        step, _, ev = v.tick(True)
        if ev and ev["verdict"].startswith("step"):
            return ev
    return {"verdict": "no decision"}


class VerdictInWords(unittest.TestCase):
    def allowed(self, rise, judge, runs=300, **kw):
        return sum(trial_outcome(rise, judge, s, **kw)["verdict"] == "step allowed" for s in range(runs))

    def test_costly_steps_allowed_less_often(self):
        """On noisy work (log-normal, σ = 0.25), a step costing 3% or 5% more than native against a 2% allowance: the
        reading in words allows it a quarter to a half less often than the medians alone did."""
        for rise, most in ((0.03, 0.8), (0.05, 0.65)):
            med, ivl = self.allowed(rise, "median"), self.allowed(rise, "interval")
            self.assertLessEqual(ivl, most * med, (rise, med, ivl))

    def test_free_steps_still_allowed(self):
        """A step that costs nothing is kept almost as often as before (the allowance is not made unreachable), and
        nearly always where the work is quiet."""
        med, ivl = self.allowed(0.0, "median"), self.allowed(0.0, "interval")
        self.assertGreaterEqual(ivl, 0.85 * med, (med, ivl))
        self.assertGreaterEqual(self.allowed(0.0, "interval", runs=50, sigma=0.03), 45)

    def test_clear_rise_reads_loss(self):
        ev = trial_outcome(0.20, "interval", 7)
        self.assertEqual(ev["verdict"], "step refused: the muscle is slower there")
        self.assertEqual(ev["reading"], "LOSS")

    def test_wide_evidence_measures_on(self):
        """Very noisy work: the interval is wider than the allowance at min_samples, so the trial measures on (up to
        three times min_samples) before it decides."""
        v = Verdict(tolerance=0.02, min_samples=30, probe_every=1, recheck=10 ** 6, max_trial=40)
        rng, step, decided_at = random.Random(5), 0, None
        for t in range(40):
            v.observe([10.0 * rng.lognormvariate(0.0, 1.5) for _ in range(30)])
            step, _, ev = v.tick(True)
            if ev and ev["verdict"].startswith("step"):
                decided_at = t
                break
        self.assertIsNotNone(decided_at)
        self.assertGreaterEqual(decided_at, 4)       # reference (1 decision), then at least three decisions of trial

    def test_interval_arithmetic(self):
        lo, hi = change_interval([10.0] * 5, [11.0] * 5)
        self.assertAlmostEqual(lo, hi)
        self.assertGreater(lo, 0.0)
        self.assertIsNone(change_interval([], [1.0]))


if __name__ == "__main__":
    unittest.main()
