# The tracking theorem: what the U channel provably does, and what it does not

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page proves the internal tracking result of the canonical engine (`symmetric_verified`, mechanism id in
`results/MECHANISM_IDENTITY.json`) in four steps, from the continuous law to the code as executed. Each statement
carries one evidence class (see `docs/EVIDENCE_LEDGER.md`): **T** proved here, **V** checked by computation over a
finite, frozen set (`tools/tracking_bounds.py` → `results/TRACKING_BOUNDS.json`).

What this page establishes is **internal**: inside the declared model, the controller conveys U to its target
σ. It does not establish that σ is the right target for any outside plant, that the telemetry map is right,
that any actuator mapping (HPA, GPU, CPU) is right, any energy saving, production performance, or stability of the
whole forced six-state system. Target correctness and target conveyance are separate obligations; this page carries
only the second.

## Setting

U channel of equation (2): `dU/dt = f[U](x, t) + u`, with the uncontrolled drift

    f[U](x, t) = μ U (1 − U²) − (dE/dt) / E[max] − λ[U] U

and the bounded cancellation-plus-proportional controller (`omnicompass/core.py`, `control_command`)

    u = sat(−f[U](x, t) + K[P] (σ − U)),   sat(v) = max(−u[max], min(u[max], v)),   K[P] = 12, u[max] = U_AUTHORITY = 25.

Tracking error `e = U − σ`, σ ∈ {−1, +1}.

## Theorem 1 (T). Unsaturated tracking

On the unsaturated region `Ω[unsat] = { x : |−f[U](x, t) − K[P] e| ≤ u[max] }`, `de/dt = −K[P] e`. Along any interval
spent in `Ω[unsat]`, `e(t) = e(t₀) exp(−K[P] (t − t₀))`, and `V = e²/2` satisfies `dV/dt = −K[P] e² < 0` for `e ≠ 0`.

*Proof.* Inside `Ω[unsat]` the saturation is inactive, so `dU/dt = f[U] − f[U] + K[P] (σ − U) = −K[P] e`; since σ
is constant, `de/dt = dU/dt`. The solution and `dV/dt = e de/dt = −K[P] e²` follow. ∎

This is a statement about intervals inside `Ω[unsat]` only; it is not global convergence.

## Theorem 2 (T). The saturated case, under a declared drift bound

**Assumption D.** Along the trajectory, `|f[U](x(t), t)| ≤ F[D] < u[max]`.

Under D:
1. If saturation is active with `e < 0`, then `u = +u[max]` and `de/dt = f[U] + u[max] ≥ u[max] − F[D] > 0`; symmetrically
   for `e > 0`. So `dV/dt ≤ −(u[max] − F[D]) |e| < 0` wherever saturation is active.
2. With Theorem 1, `V` is strictly decreasing wherever `e ≠ 0`, saturated or not; `e` never changes sign (at `e = 0`
   the command is unsaturated because `F[D] < u[max]`, so `e = 0` is an equilibrium of the error dynamics).
3. Any saturated stretch ends within `(|e(t₀)| − e*) / (u[max] − F[D])` time units, `e* = (u[max] − F[D]) / K[P]`; the
   ball `|e| ≤ e*` lies inside `Ω[unsat]` and is forward invariant, and inside it the decay is exponential at rate K[P].

*Proof of 1.* Saturation with `u = +u[max]` means `−f[U] − K[P] e > u[max]`, so `−K[P] e > u[max] + f[U] ≥ u[max] − F[D] > 0`,
so `e < 0`, and `de/dt = f[U] + u[max] ≥ u[max] − F[D]`. The other side is symmetric. 2 and 3 follow from 1 and
Theorem 1, and `|−f[U] − K[P] e| ≤ F[D] + K[P] |e| ≤ u[max]` on the ball. ∎

**Where D holds (T).** On the declared box — parameters in `PARAMETER_RANGES`, `E₀` in [0, 1], `|U| ≤ 1.1` — equation
(1) keeps E in `[(β − c)/α[E], (β + c)/α[E]]` widened to hold E₀ (the right side of (1) points inward at
both ends, because `|v[eff]| ≤ c`), so `|E| ≤ 7/4.2`, `|dE/dt| ≤ 4.2·|E| + 2 + 5 ≤ 14`, and

    F[D] = 6 · 2/(3√3) + 14 / 1 + 0.5 · 1.1 = 16.86 < 25 = u[max].

Because e keeps its sign and `|e|` does not grow (continuous time), U stays between U₀ and σ, so `|U| ≤ 1` and the
box is self-consistent for the nearest-basin target. **Theorem 2 therefore holds globally over the declared box, in
continuous time.** The actuator can still saturate: `|raw| ≤ F[D] + K[P] |e₀|` can exceed 25 when `|e₀|` is near 1.

**Checked (V).** Over the 500 frozen fixtures: observed `max |f[U]|` = 6.84 (nearest target), 7.01 (wrong target), each
under that fixture's own bound (max 8.99) and under 16.86; saturated micro steps 0 of 100 000 (nearest target), 5 of
100 000 (wrong target).

## Theorem 3 (T with a computed constant). The executed sampled-data controller

The code does not run the continuous law. Per micro step `h = MICRO_DT = 0.01`, it computes `uₖ` from `xₖ`, holds it
through the four stages of one RK4 step (zero-order hold), and takes `xₖ₊₁ = F[h](xₖ, uₖ)`. There is no overwrite of U
after the step, no projection onto a basin, no state replacement.

Integrating the U equation over one held interval,

    eₖ₊₁ = eₖ + h (f[U](xₖ) + uₖ) + ∫[tₖ, tₖ+h] (f[U](x(t)) − f[U](xₖ)) dt + τₖ

with `τₖ` the RK4 truncation error. Unsaturated, `f[U](xₖ) + uₖ = −K[P] eₖ`, so

    eₖ₊₁ = ρ eₖ + dₖ,   ρ = 1 − h K[P] = 0.88,   |dₖ| ≤ (h²/2) sup|df[U]/dt| + |τₖ| =: ε[h].

Then by induction `|eₖ| ≤ ρᵏ |e₀| + (1 − ρᵏ)/(1 − ρ) · ε[h]`, and the error enters and stays in the
neighbourhood `|e| ≤ ε[h] / (1 − ρ)`.

The proof above is exact given ε[h]. **ε[h] itself is computed, not proved (V):** the largest `|dₖ|` over
every micro step of the 500 frozen fixtures is 0.00378 (nearest target), giving the ultimate bound 0.0315, inside
`BASIN_TOL` = 0.10 that CONVEY-5 and CERT-10 test. With the target aimed wrong, ε[h] = 0.0243 (dominated by the
long transient, which includes the 5 saturated steps) and the bound 0.20 is wider than the basin — a conservative
bound; the fixtures still certify 500 of 500.

**Proved since 19 October (T, computer-assisted; `docs/ENGINE_PROOFS.md`, claims U2 to U5).** Over the whole
declared box, not the fixtures: every unsaturated micro step satisfies `|eₖ₊₁| ≤ (ρ + b)|eₖ| + a` with `a ≤ 0.006495`
and `b ≤ 0.02399`. These are interval enclosures with outward rounding of the stage-to-stage drift differences, bounded
by the mean value theorem. So the ball `|e| ≤ a / (1 − ρ − b) ≤ 0.0677` is entered and never left, inside `BASIN_TOL`.
Every saturated step moves U toward σ by at least 0.0868 and never past it. From any admissible start the error is in
the basin within 119 of the run's 200 micro steps. The fixtures' 0.0315 lies inside the proved 0.0677.

What the discrete execution does **not** inherit: the continuous monotone decay. Within the band, `|e|` grew on 27 061
of 100 000 micro steps and e changed sign 747 times — the sampled controller dithers inside `ε[h] / (1 − ρ)`.

**CONVEY and CERT.** They are dwell checks against a declared neighbourhood (`|U − σ| ≤ 0.10` for 5 and 10
consecutive macro steps). Theorem 3 says why they pass when the bound sits inside the neighbourhood. They are not an
external certification.

## Theorem 4 (T continuous; V discrete). Admissibility

Admissible set for a fixture with parameters p and initial state x0:

    A = { x : E ∈ [E[lo], E[hi]],  |U − σ| <= |U₀ − σ|,  S between S₀ and S₊(p) }

`E_lo, E_hi` as in Theorem 2; `S₊` the stable root of equation (6).

- **Continuous (T).** A is forward invariant: E by the inward-pointing field at both ends; U by Theorem 2; S because
  equation (6) is the one-dimensional gradient flow of Φ, monotone toward `S₊` from any `S₀ > S₋`
  (`s_admissibility` in `results/core_evidence.json`: 500 of 500 fixtures start above `S_minus`).
- **Discrete (V).** For the executed map `F[h](x, C(x))`, every micro step of every fixture: `xₖ ∈ A` implied
  `xₖ₊₁ ∈ A` — 0 failures in 100 000 steps, target nearest or wrong. This is a finite verification on the frozen
  fixtures.
- **Discrete (T, since 19 October).** Over the whole box, for the executed RK4 step (`docs/ENGINE_PROOFS.md`):
  - E stays in its interval (E1, exact linear arithmetic in z3), and so does every stage (E2);
  - S moves toward S₊ and never past it (S1);
  - U stays within `max(|U₀ − σ|, 0.0677)` of σ (U3, U4);
  - I[U] stays in its interval for any bounded drive (I1).

## What remains open (O)

- Global stability of the forced six-state system. E, U, S and I[U] are proved bounded under the executed step
  (`docs/ENGINE_PROOFS.md`). Not proved: the bath B, which nothing reads back, and convergence of E, I[U] and B to a set.
- CERT-10 for every fixture in the box: the proved entry bound (119 micro steps) leaves 9 macro steps inside the basin,
  not 10. Every one of the 500 fixtures certifies (V).
- The inheritance / intertwining residual against an outside plant: instrumented (`tools/gpu_reps.py`,
  representation fidelity), not yet measured on a real card.
- The printed configuration (`printed_eight_line`) is not covered by this page: its U drift is logistic, not the
  double well, and needs its own bound (`docs/CANONICAL_ENGINE.md`).

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
