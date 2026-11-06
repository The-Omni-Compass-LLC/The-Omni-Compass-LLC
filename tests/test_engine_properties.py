# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""The engine's own code, run on thousands of generated cases, checked against what tools/prove_engine.py proves.

The proofs are about the algorithm; these tests run the engine files themselves (omnicompass/compass_law.py,
omnicompass/verdict.py, omnicompass/core.py) and check every proved property on each case, with the proved constants
read from results/ENGINE_PROOFS.json. A failure here means the proof and the code disagree. Generation is derandomized,
so every run checks the same cases."""
import copy
import json
import math
import sys
import unittest
from pathlib import Path

from hypothesis import given, settings, strategies as st, HealthCheck

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass import core as C  # noqa: E402
from omnicompass.compass_law import Band, CompassLaw, Plug, ForeignWriter, clamp  # noqa: E402
from omnicompass.verdict import Verdict, change_interval  # noqa: E402

PROOFS = json.loads((ROOT / "results" / "ENGINE_PROOFS.json").read_text())
U = PROOFS["intervals"]
SET = settings(max_examples=300, deadline=None, derandomize=True, suppress_health_check=[HealthCheck.too_slow])
finite = dict(allow_nan=False, allow_infinity=False)


def law(kp, tau, dt, authority, center=0.5):
    return CompassLaw(Band(lo=0.0, hi=1.0, center=center), dt=dt, tau=tau, kp=kp, authority=authority)


class CompassLawProperties(unittest.TestCase):
    @SET
    @given(kp=st.floats(0.01, 50), tau=st.floats(0, 600), dt=st.floats(0.1, 120), A=st.floats(0.01, 10),
           readings=st.lists(st.floats(-2, 3, **finite), min_size=1, max_size=30))
    def test_bounded_fail_up_and_no_take_back_climbing(self, kp, tau, dt, A, readings):
        g = law(kp, tau, dt, A)
        self.assertGreaterEqual(g.kd, 0.0)                                        # C8
        for r in readings:
            f = g.force(r)
            self.assertLessEqual(abs(f), A + 1e-12)                               # C1
            if g.p >= g.band.wall_high:
                self.assertEqual(f, A)                                            # C2
            if f < 0:
                self.assertFalse(g.v > 0 and g.p > g.band.center)                 # C3

    @SET
    @given(kp=st.floats(0.01, 50), tau=st.floats(0, 600), dt=st.floats(0.1, 120), A=st.floats(0.01, 10),
           p0=st.floats(-1, 2, **finite), v=st.floats(-5, 5, **finite), r1=st.floats(-1, 2, **finite), r2=st.floats(-1, 2, **finite))
    def test_monotone_in_reading_for_a_given_climb(self, kp, tau, dt, A, p0, v, r1, r2):
        # the same prior state (p, v) in both copies; smooth=0.5 mixes the new difference in, so compare equal climbs by
        # fixing the velocity estimate the force sees: set smooth to 1 (velocity held) for this check
        g = law(kp, tau, dt, A)
        g.smooth, g.p, g.v = 1.0, p0, v
        lo, hi = sorted((r1, r2))
        a, b = copy.deepcopy(g), copy.deepcopy(g)
        self.assertLessEqual(a.force(lo), b.force(hi) + 1e-12)                    # C5

    @SET
    @given(kp=st.floats(0.01, 50), tau=st.floats(0, 600), dt=st.floats(0.1, 120), A=st.floats(0.01, 10),
           p=st.floats(0.0, 0.94, **finite))
    def test_points_home_at_rest(self, kp, tau, dt, A, p):
        g = law(kp, tau, dt, A)
        g.smooth, g.p, g.v = 1.0, p, 0.0
        f = g.force(p)
        if p < 0.5:
            self.assertLess(f, 0.0)                                               # C4
        elif p > 0.5:
            self.assertGreater(f, 0.0)


class Lever(Plug):
    def __init__(self, lo, hi, start):
        super().__init__(lo, hi)
        self.v, self.sent = start, []

    def _read_service(self):
        return 0.5

    def _read_lever(self):
        return self.v

    def _send(self, value):
        self.sent.append(value)
        self.v = value


class PlugProperties(unittest.TestCase):
    @SET
    @given(lo=st.floats(-100, 100, **finite), width=st.floats(0.0, 100), start_frac=st.floats(0, 1),
           writes=st.lists(st.floats(-500, 500, **finite), max_size=40))
    def test_every_write_inside_the_cover_and_restore_returns(self, lo, width, start_frac, writes):
        hi = lo + width
        dev = Lever(lo, hi, lo + start_frac * width)
        snap = dev.attach()
        for w in writes:
            dev.write(w)
        for sent in dev.sent:
            self.assertTrue(lo <= sent <= hi)                                     # P1
        self.assertEqual(dev.snapshot, snap)                                      # the restore point never moves
        self.assertTrue(dev.restore())
        self.assertAlmostEqual(dev.v, snap)

    @SET
    @given(writes=st.lists(st.floats(0, 10, **finite), min_size=1, max_size=10), moved=st.floats(20, 30))
    def test_a_foreign_writer_takes_the_lever_and_nothing_more_is_sent(self, writes, moved):
        dev = Lever(0.0, 10.0, 5.0)
        dev.attach()
        dev.write(writes[0])
        dev.v = moved                                                             # someone else moved it
        with self.assertRaises(ForeignWriter):
            dev.write(1.0)
        n = len(dev.sent)
        self.assertIsNone(dev.write(2.0))
        self.assertTrue(dev.restore())
        self.assertEqual(len(dev.sent), n)                                        # never fights the new owner
        self.assertEqual(dev.v, moved)

    @SET
    @given(lo=st.floats(-10, 10, **finite), width=st.floats(0, 10), x=st.floats(-50, 50, **finite))
    def test_clamp(self, lo, width, x):
        hi = lo + width
        c = clamp(x, lo, hi)
        self.assertTrue(lo <= c <= hi)                                            # P1
        if lo <= x <= hi:
            self.assertEqual(c, x)                                                # P2
        self.assertEqual(clamp(c, lo, hi), c)                                     # P3


class VerdictProperties(unittest.TestCase):
    @settings(max_examples=120, deadline=None, derandomize=True, suppress_health_check=[HealthCheck.too_slow])
    @given(costs=st.lists(st.floats(0.8, 1.3), min_size=1, max_size=6), sigma=st.floats(0.01, 0.4),
           seed=st.integers(0, 10 ** 6), incremental=st.booleans())
    def test_an_allowed_step_never_reads_loss_and_never_passes_the_allowance(self, costs, sigma, seed, incremental):
        import random
        rnd = random.Random(seed)
        tol = 0.02
        vd = Verdict(tolerance=tol, min_samples=20, probe_every=1, recheck=50, max_trial=200, incremental=incremental)
        step = 0
        native = None
        for t in range(1200):
            step, trial, event = vd.tick(calm=True)
            mult = costs[min(step, len(costs) - 1)]
            vd.observe([mult * math.exp(rnd.gauss(0.0, sigma)) for _ in range(5)])
            if event and event.get("verdict") == "step allowed":
                ivs = event["interval_ln"]
                self.assertTrue(all(lo <= 0.0 + 1e-5 for lo, _ in ivs))           # V1
                self.assertLessEqual(event["cost_step"], event["cost_native"] * (1 + tol) + 1e-12)   # V2
                if incremental:
                    native = vd.native_cost if native is None else native
                    self.assertLessEqual(event["cost_step"], native * (1 + tol) + 1e-12)            # V3
        self.assertEqual(vd.state, "left native" if vd.allowed == 0 else "acting")

    def test_interval_arithmetic_is_welch(self):
        self.assertIsNone(change_interval([], [1.0]))
        lo, hi = change_interval([1.0, 1.1, 0.9], [1.0, 1.1, 0.9])
        self.assertAlmostEqual((lo + hi) / 2, 0.0)


def admissible():
    """A fixture from the declared box (core.sample_state and PARAMETER_RANGES) with S0 above S- (theorem S1's premise)."""
    names = list(C.PARAMETER_RANGES)
    par = st.tuples(*[st.floats(*C.PARAMETER_RANGES[n]) for n in names]).map(lambda vs: C.Params(**dict(zip(names, vs))))
    state = st.tuples(st.floats(0, 1), st.floats(-1, 1), st.floats(0, 1), st.floats(-1, 1), st.floats(-1, 1), st.floats(-1, 1))
    return st.tuples(par, state, st.booleans()).filter(lambda ps: ps[1][3] > C.s_roots(ps[0])[0] + 1e-6)


class TrackingProperties(unittest.TestCase):
    """The executed sampled-data controller (core.control_command + core.rk4_step), every micro step of a whole run."""

    @settings(max_examples=150, deadline=None, derandomize=True, suppress_health_check=[HealthCheck.too_slow, HealthCheck.filter_too_much])
    @given(fx=admissible())
    def test_every_proved_claim_holds_on_every_micro_step(self, fx):
        p, s, wrong = fx
        x = C.State(*s)
        sigma = C.nearest_basin_sign(x.U) * (-1 if wrong else 1)
        a, b = U["U2"]["a_upper"], U["U2"]["b_upper"]
        rho, rstar = U["U2"]["rho"], U["U3"]["r_star_upper"]
        step_min = U["U4"]["step_min"]
        beta = p.beta_int + p.beta_ext
        e_lo, e_hi = min(0.0, (beta - p.c) / p.alpha_E), max(1.0, (beta + p.c) / p.alpha_E)
        s_minus, s_plus = C.s_roots(p)
        e0 = abs(x.U - sigma)
        h = C.MICRO_DT
        inside_by = None
        k = 0
        for m in range(C.MACRO_STEPS):
            t = m * C.MACRO_DT
            for _ in range(C.MICRO_STEPS):
                u, raw = C.control_command(x, p, t, sigma)
                xn = C.rk4_step(x, p, t, h, u)
                e, en = x.U - sigma, xn.U - sigma
                self.assertTrue(e_lo - 1e-12 <= xn.E <= e_hi + 1e-12)                                     # E1
                if x.S < s_plus:
                    self.assertTrue(x.S - 1e-15 <= xn.S <= s_plus + 1e-12)                                # S1
                elif x.S > s_plus:
                    self.assertTrue(s_plus - 1e-12 <= xn.S <= x.S + 1e-15)
                if abs(raw) <= C.U_AUTHORITY:
                    self.assertLessEqual(abs(en), (rho + b) * abs(e) + a + 1e-12)                         # U2
                else:
                    self.assertGreaterEqual(abs(e) - abs(en), step_min - 1e-12)                           # U4
                    self.assertEqual(e > 0, en > 0)
                self.assertLessEqual(abs(en), max(e0, rstar) + 1e-12)                                     # U3
                k += 1
                if inside_by is None and abs(en) <= C.BASIN_TOL:
                    inside_by = k
                x = xn
                t += h
        self.assertIsNotNone(inside_by)
        self.assertLessEqual(inside_by, U["U5"]["micro_steps_max"])                                       # U5

    @settings(max_examples=60, deadline=None, derandomize=True, suppress_health_check=[HealthCheck.too_slow])
    @given(U0=st.floats(0.8, 1.0), E0=st.floats(0.8, 1.0), c=st.floats(4.0, 5.0), Emax=st.floats(1.0, 1.5),
           l0=st.floats(1.5, 2.0), up_side=st.booleans())
    def test_saturated_steps_where_the_drift_is_strongest(self, U0, E0, c, Emax, l0, up_side):
        """The corner the generated fixtures rarely reach: the target aimed wrong (|e| near 2), E high and v_eff at -c,
        so the drift opposes the command and the actuator saturates; U4 must hold on each such step."""
        sign = 1 if up_side else -1
        p = C.Params(beta_int=0.0, beta_ext=0.0, c=c, E_max=Emax, lambda_0=-sign * l0, lambda_1=0.1, lambda_2=0.0, mu=6.0,
                     lambda_U=0.5)
        # dE/dt = -alpha_E E + v: E high strengthens the upward case's drift, E low the downward case's
        x = C.State(E0 if up_side else 1.0 - E0, sign * U0, 0.5, 0.0, 0.0, 0.0)
        sigma = -C.nearest_basin_sign(x.U)
        step_min = U["U4"]["step_min"]
        saturated = 0
        t = 0.0
        for _ in range(C.MACRO_STEPS * C.MICRO_STEPS):
            u, raw = C.control_command(x, p, t, sigma)
            xn = C.rk4_step(x, p, t, C.MICRO_DT, u)
            e, en = x.U - sigma, xn.U - sigma
            if abs(raw) > C.U_AUTHORITY:
                saturated += 1
                self.assertGreaterEqual(abs(e) - abs(en), step_min - 1e-12)                               # U4
                self.assertEqual(e > 0, en > 0)                                                           # no overshoot
            x, t = xn, t + C.MICRO_DT
        self.assertLessEqual(abs(x.U - sigma), U["U3"]["r_star_upper"])
        if E0 > 0.9 and c > 4.5 and Emax < 1.2:
            self.assertGreater(saturated, 0)                                                              # the corner is reached


if __name__ == "__main__":
    unittest.main()
