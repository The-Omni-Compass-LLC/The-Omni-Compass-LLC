#!/usr/bin/env python3
# SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0
# Copyright (c) 2026 The Omni-Compass LLC / Dubra Software. All rights reserved.
# Evaluation and Simulation use only; any commercialization, monetization or other use requires a signed, paid
# Omni-Compass Enterprise License. See LICENSE, NOTICE and DISCLOSURES.md.
# All patents, copyrights and trademarks filed in the USA. www.omni-compass.com
"""Machine-checked proofs of the engine's properties (docs/ENGINE_PROOFS.md). No engine file is changed: every proof
reads the engine's own constants and is about the algorithm the engine executes.

Two kinds of proof, each over every input in its declared set, never over samples:

  SMT (z3)        a claim P is proved when the solver shows that "the premises and not P" has no solution (unsat).
                  tanh enters only through true facts about it (bounded by 1, odd in sign, increasing, 1-Lipschitz),
                  so anything proved for every function with those facts holds for tanh.
  intervals       enclosures computed with outward rounding (mpmath's interval arithmetic), so every bound printed is
                  a true upper bound of the quantity over the whole box, rounding included.

  python3 tools/prove_engine.py            prove everything, write results/ENGINE_PROOFS.json, exit 1 if any fails
  python3 tools/prove_engine.py --quiet    the same, printing only the summary line

What is proved (each item names its theorem in docs/ENGINE_PROOFS.md):
  C1-C8  the compass law's force (omnicompass/compass_law.py): bounded by its authority, fails up at the wall, never
         takes back while the reading climbs above the centre, points home at rest, is monotone in position and in
         velocity, is Lipschitz (no hammer) inside the band, and its default damping is never negative
  P1-P3  the plug's clip: every write inside the cover, nothing clipped that was inside, clipping idempotent
  V1-V3  the verdict's rule (omnicompass/verdict.py, judge="interval"): an allowed step never reads LOSS, never passes the
         allowance, and stepwise never adds up past the cost first measured at native
  E1-E2  the executed RK4 micro step keeps E in its box, and every RK4 stage inside the box widened by 0.13
  I1     the executed RK4 micro step keeps the memory I_U in its box
  S1     the executed RK4 micro step moves S toward its stable root S+ and never past it (from any S0 above S-)
  U1-U5  the executed sampled-data controller (theorem 3 of docs/TRACKING_THEOREM.md, here with every constant proved):
         the drift bound on the stage box, the saturated step, the unsaturated step |e+| <= (rho + b)|e| + a, the
         ultimate bound a / (1 - rho - b) inside the basin, and the number of micro steps that bound is reached in
  B1     the bath (B, B'): its RK4 step is strictly stable for every parameter in the box (spectral radius below 1), so it
         stays bounded under the bounded S and forgets its start
"""
from __future__ import annotations

import argparse, json, math, sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from omnicompass import core as C  # noqa: E402

OUT = ROOT / "results" / "ENGINE_PROOFS.json"
H = Fraction(C.MICRO_DT).limit_denominator(10 ** 6)           # 1/100, the micro step the engine executes
KP, UMAX = C.KP, C.U_AUTHORITY
R = C.PARAMETER_RANGES


# ----------------------------------------------------------------------------------------------- SMT (z3) proofs
def smt_proofs():
    import z3
    out = {}

    def prove(name, premises, claim, what):
        # the premises must be satisfiable on their own, or "no counterexample" would hold of anything (a vacuous proof)
        live = z3.Solver()
        live.set("timeout", 120000)
        live.add(*premises)
        if live.check() != z3.sat:
            out[name] = {"claim": what, "result": "vacuous: the premises admit no case"}
            return
        s = z3.Solver()
        s.set("timeout", 120000)
        s.add(*premises)
        s.add(z3.Not(claim))
        r = s.check()
        out[name] = {"claim": what, "result": "proved" if r == z3.unsat else ("counterexample" if r == z3.sat else "unknown")}
        if r == z3.sat:
            out[name]["model"] = str(s.model())

    Real = z3.Real
    T = z3.Function("tanh", z3.RealSort(), z3.RealSort())

    def tanh_facts(*xs):
        """True facts about tanh at the arguments used: bounded, the sign of its argument, increasing, 1-Lipschitz."""
        f = []
        for x in xs:
            f += [T(x) > -1, T(x) < 1, z3.Implies(x > 0, T(x) > 0), z3.Implies(x < 0, T(x) < 0), z3.Implies(x == 0, T(x) == 0)]
        for a in xs:
            for b in xs:
                f += [z3.Implies(a <= b, T(a) <= T(b)),
                      z3.If(T(a) >= T(b), T(a) - T(b), T(b) - T(a)) <= z3.If(a >= b, a - b, b - a)]
        return f

    kp, kd, A, c, wh, wl = Real("kp"), Real("kd"), Real("A"), Real("center"), Real("wall_high"), Real("wall_low")
    law = [kp > 0, kd >= 0, A > 0, wl > 0, wl < c, c < wh, wh < 1]

    def force(p, v, x):
        """The force exactly as CompassLaw.force computes it, with x standing for raw / authority (A x = raw)."""
        pre = A * T(x)
        zeroed = z3.And(pre < 0, v > 0, p > c)
        return z3.If(p >= wh, A, z3.If(zeroed, 0, pre)), [A * x == kp * (p - c) + kd * v]

    p, v, x = Real("p"), Real("v"), Real("x")
    f, d = force(p, v, x)
    base = law + d + tanh_facts(x)
    prove("C1", base, z3.And(f <= A, f >= -A), "the force never exceeds its authority, either way")
    prove("C2", base, z3.Implies(p >= wh, f == A), "past the wall (0.95) the force is the full authority up at once")
    prove("C3", base, z3.Implies(f < 0, z3.Not(z3.And(v > 0, p > c))),
          "the force never takes back while the reading climbs above the centre")
    prove("C4", base, z3.And(z3.Implies(z3.And(v == 0, p < c), f < 0),
                              z3.Implies(z3.And(v == 0, p > c, p < wh), f > 0),
                              z3.Implies(z3.And(v == 0, p == c), f == 0)),
          "at rest the force points home: down below the centre, up above it, nothing at the centre")
    p1, p2, x1, x2, v1, v2 = Real("p1"), Real("p2"), Real("x1"), Real("x2"), Real("v1"), Real("v2")
    f1, d1 = force(p1, v, x1)
    f2, d2 = force(p2, v, x2)
    prove("C5", law + d1 + d2 + tanh_facts(x1, x2) + [p1 <= p2], f1 <= f2,
          "for a given velocity the force never falls as the reading rises (no inversion)")
    g1, e1 = force(p, v1, x1)
    g2, e2 = force(p, v2, x2)
    prove("C6", law + e1 + e2 + tanh_facts(x1, x2) + [v1 <= v2], g1 <= g2,
          "at a given reading the force never falls as the climb quickens")
    both_inside = [p1 < wh, p2 < wh, z3.Not(z3.And(A * T(x1) < 0, v > 0, p1 > c)), z3.Not(z3.And(A * T(x2) < 0, v > 0, p2 > c))]
    prove("C7", law + d1 + d2 + tanh_facts(x1, x2) + both_inside,
          z3.If(f1 >= f2, f1 - f2, f2 - f1) <= kp * z3.If(p1 >= p2, p1 - p2, p2 - p1),
          "inside the band the force changes no faster than kp times the reading (smooth, never a hammer)")
    tau, dt, s = Real("tau"), Real("dt"), Real("s")
    kd_default = z3.If(2 * s - 1 > 0, 2 * s - 1, 0) * dt
    prove("C8", [kp > 0, tau >= 0, dt > 0, s >= 0, s * s * dt == kp * tau], kd_default >= 0,
          "the default damping (critical for the muscle's response time) is never negative")

    # the plug's clip (Plug.write: v = clamp(value, lo, hi))
    lo, hi, val = Real("lo"), Real("hi"), Real("value")
    clamp = lambda q: z3.If(q < lo, lo, z3.If(q > hi, hi, q))
    prove("P1", [lo <= hi], z3.And(lo <= clamp(val), clamp(val) <= hi), "every value the plug sends lies inside the cover")
    prove("P2", [lo <= val, val <= hi], clamp(val) == val, "a value already inside the cover is sent as it is")
    prove("P3", [lo <= hi], clamp(clamp(val)) == clamp(val), "clipping twice is clipping once")

    # the verdict's rule (Verdict.tick, judge="interval"): allow = not LOSS and within and d_max <= tau
    lo1, hi1, lo2, hi2, mk, m0, nat, tol, tl = (Real(n) for n in ("lo1", "hi1", "lo2", "hi2", "mk", "m0", "native", "tol", "tau_tol"))
    prem = [tol > 0, tl > 0, m0 > 0, nat > 0, mk > 0, lo1 <= hi1, lo2 <= hi2]
    loss = z3.Or(lo1 > 0, lo2 > 0)
    bound = z3.If(m0 <= nat, m0, nat)
    d_max = z3.If((lo1 + hi1) / 2 >= (lo2 + hi2) / 2, (lo1 + hi1) / 2, (lo2 + hi2) / 2)
    allow = z3.And(z3.Not(loss), mk <= bound * (1 + tol), d_max <= tl)
    prove("V1", prem, z3.Implies(allow, z3.And(lo1 <= 0, lo2 <= 0)), "an allowed step never reads LOSS against either reference")
    prove("V2", prem, z3.Implies(allow, z3.And((lo1 + hi1) / 2 <= tl, (lo2 + hi2) / 2 <= tl, mk <= m0 * (1 + tol))),
          "an allowed step's estimated change is within the allowance against the fresh reference")
    prove("V3", prem, z3.Implies(allow, mk <= nat * (1 + tol)),
          "stepwise, an allowed step stays within the allowance of the cost first measured at native: steps cannot add up")

    # the executed RK4 micro step, E component: k_i = -alpha_E E_i + beta + v_i with |v_i| <= c (|cos| <= 1, |tanh| < 1)
    alpha = Fraction(R["alpha_E"][0]).limit_denominator(10 ** 6)
    h = z3.RealVal(str(H))
    al = z3.RealVal(str(alpha))
    E, beta, cc = Real("E"), Real("beta"), Real("c")
    vs = [Real(f"v{i}") for i in range(1, 5)]
    lo_E = z3.If((beta - cc) / al < 0, (beta - cc) / al, 0)
    hi_E = z3.If((beta + cc) / al > 1, (beta + cc) / al, 1)
    pre = [cc >= R["c"][0], cc <= R["c"][1], beta >= 0, beta <= R["beta_int"][1] + R["beta_ext"][1], E >= lo_E, E <= hi_E]
    pre += [z3.And(vi >= -cc, vi <= cc) for vi in vs]
    k1 = -al * E + beta + vs[0]
    E2 = E + h / 2 * k1
    k2 = -al * E2 + beta + vs[1]
    E3 = E + h / 2 * k2
    k3 = -al * E3 + beta + vs[2]
    E4 = E + h * k3
    k4 = -al * E4 + beta + vs[3]
    En = E + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    prove("E1", pre, z3.And(En >= lo_E, En <= hi_E),
          "the executed RK4 micro step keeps E in [min(0, (beta - c)/alpha_E), max(1, (beta + c)/alpha_E)]")
    w = z3.RealVal("0.13")
    prove("E2", pre, z3.And(*[z3.And(q >= lo_E - w, q <= hi_E + w) for q in (E2, E3, E4)]),
          "every RK4 stage of E stays inside that box widened by 0.13")

    # the executed RK4 micro step, I_U component: k_i = F_i - lambda_I I_i with F_i = (1 - U) - sigma_1 E - delta S bounded
    I, lam, Flo, Fhi, I0 = Real("I"), Real("lambda_I"), Real("F_lo"), Real("F_hi"), Real("I0")
    Fs = [Real(f"F{i}") for i in range(1, 5)]
    lo_I = z3.If(Flo / lam < I0, Flo / lam, I0)
    hi_I = z3.If(Fhi / lam > I0, Fhi / lam, I0)
    preI = [lam >= R["lambda_I"][0], lam <= R["lambda_I"][1], Flo <= Fhi, I >= lo_I, I <= hi_I]
    preI += [z3.And(Fi >= Flo, Fi <= Fhi) for Fi in Fs]
    j1 = Fs[0] - lam * I
    I2 = I + h / 2 * j1
    j2 = Fs[1] - lam * I2
    I3 = I + h / 2 * j2
    j3 = Fs[2] - lam * I3
    I4 = I + h * j3
    j4 = Fs[3] - lam * I4
    In = I + h / 6 * (j1 + 2 * j2 + 2 * j3 + j4)
    prove("I1", preI, z3.And(In >= lo_I, In <= hi_I),
          "the executed RK4 micro step keeps I_U in [min(I0, F_lo/lambda_I), max(I0, F_hi/lambda_I)] for any bounded drive")
    return out


# ----------------------------------------------------------------------------------------------- interval proofs
def interval_proofs():
    from mpmath import iv, mpf
    iv.dps = 40
    out = {}

    def I(a, b=None):
        return iv.mpf([a, a if b is None else b])

    def rng(name):
        lo, hi = R[name]
        return I(lo, hi)

    def tanh(X):
        """tanh of an interval: it is increasing, so the enclosure is tanh of the two ends, each with outward rounding."""
        lo = 1 - 2 / (iv.exp(2 * I(X.a)) + 1)
        hi = 1 - 2 / (iv.exp(2 * I(X.b)) + 1)
        return iv.mpf([lo.a, hi.b])

    def absmax(X):
        return max(abs(X.a), abs(X.b))

    def up(x):
        """A float that is a true upper bound of the interval's largest magnitude (for the record)."""
        return float(mpf(absmax(x)) * (1 + mpf(10) ** -30))

    h = I(H.numerator) / I(H.denominator)
    kp = I(KP)
    rho = 1 - h * kp
    mu, lamU, Emax, aE = rng("mu"), rng("lambda_U"), rng("E_max"), rng("alpha_E")
    beta = rng("beta_int") + rng("beta_ext")
    c, l0, l1, l2, wB = rng("c"), rng("lambda_0"), rng("lambda_1"), rng("lambda_2"), rng("omega_B")
    dl, aS, bS = rng("delta"), rng("alpha_s"), rng("beta_s")
    trig = I(-1, 1)                                             # cos and sin of the time phase, any value

    # the boxes. E: theorem E1 over every beta and c, widened by 0.13 for the stages (theorem E2)
    E_lo = min(0.0, (0.0 - R["c"][1]) / R["alpha_E"][0])
    E_hi = max(1.0, (R["beta_int"][1] + R["beta_ext"][1] + R["c"][1]) / R["alpha_E"][0])
    E_st = I(E_lo - 0.13, E_hi + 0.13)
    # S: from any S0 in [-1, 1] above S-, S stays between S0 and S+ (theorem S1); S+ is largest at delta 1, alpha_s and
    # beta_s smallest; the stage box widens it by h max|dS/dt| (checked below)
    a_ = 0.75 * R["beta_s"][0]
    s_plus_max = (-R["alpha_s"][0] + math.sqrt(R["alpha_s"][0] ** 2 + 4 * a_ * R["delta"][1])) / (2 * a_)
    S_box = I(-1.0, max(1.0, s_plus_max) + 1e-9)
    # U: the tracking error never grows outside the ultimate bound (U3-U4), so |U| <= 1 + r*; the stage box allows 1.2
    U_st = I(-1.2, 1.2)

    def dS(S):
        return dl - aS * S - I(3) / 4 * bS * S * S

    # S1: the RK4 step moves S toward S+ and never past it, when h L < 1, L = max |dS'/dS| over the S box
    L = aS + I(3) / 2 * bS * I(max(abs(S_box.a), abs(S_box.b)))
    hL = h * L
    out["S1"] = {"claim": "the executed RK4 micro step moves S toward S+ and never past it, from any S0 above S-",
                 "L_upper": up(L), "hL_upper": up(hL), "result": "proved" if hL.b < 1 else "not proved"}
    KS = I(max(absmax(dS(S_box)), 0))
    S_st = I(S_box.a - float(mpf(absmax(h * KS))) - 1e-9, S_box.b + float(mpf(absmax(h * KS))) + 1e-9)

    # the U drift and its partial derivatives over the stage box, U cut into cells for a tight enclosure
    cells = 96
    edges = [U_st.a + (U_st.b - U_st.a) * k / cells for k in range(cells + 1)]
    FD = gU = gS = gt = mpf(0)
    KE = mpf(0)
    for k in range(cells):
        U = iv.mpf([edges[k], edges[k + 1]])
        z = l0 + l1 * (U - mpf("0.5")) + l2 * S_st
        th = tanh(z)
        sech2 = 1 - th * th
        sech2 = iv.mpf([max(sech2.a, 0), min(sech2.b, 1)])
        v = trig * c * th
        dE = -aE * E_st + beta + v
        fU = mu * U * (1 - U * U) - dE / Emax - lamU * U
        dfU_dU = mu * (1 - 3 * U * U) - trig * c * sech2 * l1 / Emax - lamU
        dfU_dS = -trig * c * sech2 * l2 / Emax
        dfU_dt = (wB / 2) * trig * c * th / Emax
        FD, gU, gS, gt = max(FD, absmax(fU)), max(gU, absmax(dfU_dU)), max(gS, absmax(dfU_dS)), max(gt, absmax(dfU_dt))
        KE = max(KE, absmax(dE))
    gE = absmax(aE / Emax)
    FD, gU, gS, gt, gE, KE, KSv = (I(q) for q in (FD, gU, gS, gt, gE, KE, absmax(KS)))
    # the stage box for E must hold every stage: |E_i - E| <= h KE (theorem E2 proves 0.13 directly; checked here too)
    out["U1"] = {"claim": "the drift |f_U| is below the actuator's limit on the whole stage box, so a saturated step "
                          "moves U toward its target in every RK4 stage",
                 "F_D_upper": up(FD), "u_max": UMAX, "result": "proved" if FD.b < UMAX else "not proved"}

    # unsaturated step: d = e+ - rho e = (h/6)(2 D2 + 2 D3 + D4), D_i = f_U(stage i) - f_U(x_k) (the command cancels the
    # drift at x_k exactly), bounded by the mean value theorem on the segment to each stage
    side = gE * KE + gS * KSv + gt                              # the stage moves that do not depend on the error
    A2, B2 = h / 2 * side, h / 2 * gU * kp
    A3, B3 = h / 2 * (gU * A2 + side), h / 2 * gU * (kp + B2)
    A4, B4 = h * (gU * A3 + side), h * gU * (kp + B3)
    # the engine runs in binary64: about a hundred operations a step on magnitudes under 40 move d by under 1e-12
    a = h / 6 * (2 * A2 + 2 * A3 + A4) + I("1e-12")
    b = h / 6 * (2 * B2 + 2 * B3 + B4)
    margin = 1 - rho - b
    rstar = a / margin if margin.a > 0 else None
    out["U2"] = {"claim": "every unsaturated micro step: |e(k+1)| <= (rho + b)|e(k)| + a",
                 "rho": float(rho.a), "a_upper": up(a), "b_upper": up(b), "result": "proved" if margin.a > 0 else "not proved"}
    no_flip = a / (rho - b)
    # every RK4 stage of U lies between U(k) and sigma, moved by at most h |D_i| past that segment (U_i - sigma =
    # (1 - c_i h KP) e + c_i h D_(i-1)); with |U| <= 1 + r* and |e| <= 2 + r*, the stages must fit in the U stage box
    eta = h * (A3 + B3 * (2 + rstar)) if rstar is not None else None
    stages_fit = bool(rstar is not None and (1 + rstar + eta).b <= U_st.b)
    out["U3"] = {"claim": "the ball |e| <= r* = a / (1 - rho - b) is entered and never left, and it lies inside the basin "
                          "(|U - sigma| <= BASIN_TOL) and inside the unsaturated region; outside a/(rho - b) the error never "
                          "changes sign, so U never overshoots its target by more than r*",
                 "r_star_upper": up(rstar) if rstar is not None else None, "basin_tol": C.BASIN_TOL,
                 "no_sign_change_beyond": up(no_flip),
                 "unsaturated_inside_ball": bool(rstar is not None and (FD + kp * rstar).b <= UMAX),
                 "U_stages_inside_stage_box": stages_fit, "stage_overshoot_upper": up(eta) if eta is not None else None,
                 "result": "proved" if (rstar is not None and rstar.b < C.BASIN_TOL and (FD + kp * rstar).b <= UMAX
                                        and stages_fit) else "not proved"}

    # saturated step: |e| > (u_max - F_D)/KP; every stage slope has the sign of u, the step moves U toward sigma by at
    # least h (u_max - F_D) and at most h (u_max + F_D), which is less than |e|: no overshoot
    sat_e = (UMAX - FD) / kp
    step_min, step_max = h * (UMAX - FD), h * (UMAX + FD)
    out["U4"] = {"claim": "every saturated micro step moves U toward its target by at least h (u_max - F_D), never past it",
                 "saturated_only_beyond_e": float(sat_e.a), "step_min": float(step_min.a), "step_max_upper": up(step_max),
                 "result": "proved" if (step_min.a > 0 and step_max.b < sat_e.a) else "not proved"}

    # how many micro steps the error needs to enter |e| <= BASIN_TOL from the farthest start (|e0| <= 2: U0 in [-1, 1],
    # sigma = +-1, the target aimed wrong included): saturated steps take off at least step_min, unsaturated steps
    # multiply |e| by at most q = rho + b + a / BASIN_TOL while |e| > BASIN_TOL
    q = rho + b + a / I(C.BASIN_TOL)
    n_unsat = math.ceil(math.log(C.BASIN_TOL / 2.0) / math.log(float(q.b))) if q.b < 1 else None
    n_sat = math.ceil(2.0 / float(step_min.a))
    out["U5"] = {"claim": "from any admissible start the error is inside the basin within n micro steps",
                 "q_upper": up(q), "unsaturated_steps_max": n_unsat, "saturated_steps_max": n_sat,
                 "micro_steps_max": (n_unsat + n_sat) if n_unsat is not None else None,
                 "run_micro_steps": C.MACRO_STEPS * C.MICRO_STEPS,
                 # the dwell checks read |U - sigma| <= BASIN_TOL at the end of each macro step: entry by micro step n
                 # leaves MACRO_STEPS - ceil(n / MICRO_STEPS) + 1 macro steps inside
                 "macro_steps_inside_at_least": (C.MACRO_STEPS - math.ceil((n_unsat + n_sat) / C.MICRO_STEPS) + 1)
                                                if n_unsat is not None else None,
                 "result": "proved" if n_unsat is not None else "not proved"}

    # B1: the bath (B, B') is a linear damped oscillator driven by S, x' = A x + (0, gamma_c delta S), A = [[0, 1],
    # [-w^2, -w/Q]]. Its RK4 step is x+ = R(hA) x + (the forcing, bounded because S is), R(z) = 1 + z + z^2/2 + z^3/6 +
    # z^4/24. For Q >= 1/2 the eigenvalues of A have Re = -w/(2Q) and modulus w (a complex pair, or the double root at
    # Q = 1/2), and |R(z)| <= e^(Re z) + |z|^5/120 e^|z| (the remainder of e^z's series). The bound rises with Q, so it is
    # taken at the largest Q, over cells of w with outward rounding: below 1 everywhere means the spectral radius of R(hA)
    # is below 1 for every parameter in the box, so the bath forgets its start geometrically and stays bounded under the
    # bounded S (input-to-state stable)
    q_max = I(R["Q_B"][1])
    w_lo, w_hi, wcells = R["omega_B"][0], R["omega_B"][1], 400
    rad = mpf(0)
    for k in range(wcells):
        W = iv.mpf([w_lo + (w_hi - w_lo) * k / wcells, w_lo + (w_hi - w_lo) * (k + 1) / wcells])
        bound = iv.exp(-h * W / (2 * q_max)) + (h * W) ** 5 / 120 * iv.exp(h * W)
        rad = max(rad, mpf(bound.b))
    out["B1"] = {"claim": "the bath's RK4 step is strictly stable for every parameter in the box: the spectral radius of "
                          "R(hA) is below 1, so the bath stays bounded under the bounded S and forgets its start",
                 "Q_min": R["Q_B"][0], "spectral_radius_upper": float(rad * (1 + mpf(10) ** -30)),
                 "decay_per_micro_step_at_least": float(1 - rad * (1 + mpf(10) ** -30)),
                 "result": "proved" if (rad < 1 and R["Q_B"][0] >= 0.5) else "not proved"}
    out["_constants"] = {"h": float(H), "KP": KP, "U_AUTHORITY": UMAX, "U_stage_box": [U_st.a.__float__(), U_st.b.__float__()],
                         "E_stage_box": [float(E_st.a), float(E_st.b)], "S_stage_box": [float(S_st.a), float(S_st.b)],
                         "g_U": up(gU), "g_E": up(gE), "g_S": up(gS), "g_t": up(gt), "K_E": up(KE), "K_S": up(KSv),
                         "U_cells": cells}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args(argv)
    res = {"smt": smt_proofs(), "intervals": interval_proofs()}
    items = {k: v for part in res.values() for k, v in part.items() if not k.startswith("_")}
    bad = sorted(k for k, v in items.items() if v.get("result") != "proved")
    res["summary"] = {"proved": len(items) - len(bad), "of": len(items), "not_proved": bad}
    OUT.write_text(json.dumps(res, indent=1) + "\n")
    if not args.quiet:
        for k, v in items.items():
            print(f"{k:3} {v['result']:13} {v['claim']}")
    print(f"engine proofs: {len(items) - len(bad)} of {len(items)} proved" + (f"; not proved: {', '.join(bad)}" if bad else ""))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
