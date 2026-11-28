# The engine's machine-checked proofs

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This page states what is proved about the engine that stands, how each proof is checked by a machine, and what is still
open. Every proof is about the algorithm the engine executes, over every input in its declared set, never over samples.
No engine file was changed to make them: the proofs read the engine's own constants. `python3 tools/prove_engine.py`
checks all of them in under a second and writes `results/ENGINE_PROOFS.json`. `tests/test_engine_proofs.py` runs it on
every push, and fails a push where any claim is not proved, where a claim's premises admit no case (a vacuous proof),
or where the stored record differs from the one the proofs produce. `tests/test_engine_properties.py` then runs the
engine's own code on several thousand generated cases and checks every proved property on each case, with the proved
constants. A failure there would mean the proof and the code disagree.

Evidence class of everything on this page: **T**, proved. Two machine methods carry the proofs:

- **SMT (the z3 solver).** A claim P is proved when the solver shows that "the premises and not P" has no solution
  (unsat). Before that, the solver confirms that the premises alone have a solution, so no proof is vacuous. tanh enters
  only through true facts about it:
  - −1 < tanh x < 1;
  - tanh x has the sign of x;
  - tanh is increasing;
  - tanh is 1-Lipschitz: |tanh x − tanh y| ≤ |x − y|;
  - for the compass loop (section 1b) also: tanh is odd, tanh(−x) = −tanh(x).

  So whatever is proved for every function with these facts holds for tanh.
- **Interval arithmetic with outward rounding** (mpmath's interval arithmetic at 40 digits). Every enclosure computed is a
  true bound of the quantity over the whole box, rounding included. The U axis is cut into 96 cells for a tight
  enclosure. tanh of an interval is the hull of tanh at its two ends, which is exact because tanh is increasing.

## 1. The compass law (`omnicompass/compass_law.py`, `CompassLaw.force`)

For every reading position p, velocity estimate v, gains kp > 0 and kd ≥ 0, authority A > 0 and walls
0 < w[low] < centre < w[high] < 1, write raw = kp (p − centre) + kd v. The force is:
- f = A when p ≥ w[high];
- otherwise f = A tanh(raw / A), set to 0 when that value is negative while v > 0 and p > centre.

| Claim | Statement | Result |
|---|---|---|
| C1 | −A ≤ f ≤ A | proved |
| C2 | p ≥ w[high] ⇒ f = A (fail up at once) | proved |
| C3 | f < 0 ⇒ not (v > 0 and p > centre): it never takes back while the reading climbs above the centre | proved |
| C4 | with v = 0: f < 0 below the centre, f > 0 between the centre and the wall, f = 0 at the centre | proved |
| C5 | for one v: p₁ ≤ p₂ ⇒ f(p₁) ≤ f(p₂) (no inversion anywhere, the wall and the take-back rule included) | proved |
| C6 | at one p: v₁ ≤ v₂ ⇒ f(v₁) ≤ f(v₂) | proved |
| C7 | inside the band, away from the wall and the take-back rule: abs(f(p₁) − f(p₂)) ≤ kp abs(p₁ − p₂) (smooth, never a hammer) | proved |
| C8 | the default damping kd = max(0, 2 √(kp τ / Δt) − 1) Δt is never negative | proved |
| C9 | for kp > 0 and kd ≥ 0, raw < 0 never holds while v > 0 and p > centre: the take-back line can never act, and C3 holds by the sign of the pull alone | proved |

C9 is a finding about the code, not a fault in it: the line that zeroes a negative force while the reading climbs above
the centre never changes a decision for any admissible gain. Taking it out would change no decision and would change the
engine's fingerprint, so it stays until the next engine version.

## 1b. The compass loop, one decision a beat (model M1)

C1 to C9 are about one force. L1 to L4 are about the loop that force closes, on a declared model, so each is conditional
on that model and its conditions, and on nothing else.

**Model M1.** The lever moves by its gain times the force, and the reading follows the lever within the beat. With
e = p − centre, the next position is

    p′ = p − b f(p) + d,   b = b[up] when f ≥ 0, b = b[down] when f < 0,   abs(d) ≤ D

where a force that adds capacity lowers the reading, b[up] and b[down] are each side's effect on the reading per unit of
force, and d is the beat's disturbance: the load's own move in the beat, and the lever's rounding to its step (half a
step at most). **Conditions:** kd = 0 (no damping); b kp ≤ 1 on each side (one beat's move is never longer than the
distance it closes); b[up] A ≤ w[high] − centre (the fail-up step is never longer than the wall's distance from the
centre); and the lever inside its cover (at its cover a muscle has nothing more to give, and nothing below holds). The
solver is given one more true fact of tanh here: it is odd, tanh(−x) = −tanh(x).

| Claim | Statement | Result |
|---|---|---|
| L1 | p ≥ centre ⇒ centre ≤ p − b f ≤ p, and p ≤ centre ⇒ p ≤ p − b f ≤ centre: the move goes toward the centre and never past it | proved |
| L2 | p ≠ centre ⇒ abs(p − b f − centre) < abs(p − centre): away from the centre every move shortens the distance | proved |
| L3 | if b A tanh(kp R / A) ≥ D on each side, then abs(e) ≤ R ⇒ abs(e′) ≤ R for every d with abs(d) ≤ D: the ball of radius R is never left | proved |
| L4 | if b A tanh(kp R / A) ≥ D + δ on each side, δ > 0, then abs(e) ≥ R ⇒ abs(e′) ≤ abs(e) − δ: outside it every beat closes at least δ | proved |

**What follows, by elementary argument from L3 and L4.** Write b[min] = min(b[up], b[down]).

1. *A bounded push: the reading is held near the centre, not at it (practical, input-to-state stability).* For
   D < b[min] A the smallest ball L3 keeps has radius R*(D) = (A / kp) artanh(D / (b[min] A)). For every R′ > R*, put
   δ = b[min] A tanh(kp R′ / A) − D > 0: from any start the reading is inside the ball of radius R′ within
   ⌈(abs(e₀) − R′) / δ⌉ beats (L4) and never leaves it after (L3). So limsup abs(eₖ) ≤ R*(D). R* is 0 at D = 0, rises
   with D, and has no finite value once D reaches b[min] A.
2. *No push: the reading settles at the centre (asymptotic stability).* With D = 0 every ball of radius R′ > 0 is
   entered and kept, so eₖ → 0, and by L2 the distance falls at every beat.
3. *A push as large as the muscle's whole pull* (D ≥ b[min] A): nothing is claimed. The disturbance outruns the muscle;
   it is at its limit.
4. *A lever that moves in whole steps* (a clock in MHz steps, whole replicas) enters through d: D = D[load] + β q / 2,
   with q the step and β the reading's move per unit of lever.

**Where the proof stops, and what was computed there instead.** No live wire runs the proof's exact case: every one
builds the law with its default damping (`omni_controller/gpu_compass.py`, `omni_orchestrator/brain.py`,
`realms/compass_arm.py` and the data stores' runners), and the Kubernetes governor uses the force as a gate for whole
machine steps rather than as a lever's move. A muscle that lags its lever (τ beyond the beat) is outside M1 as well. Both
were run instead on the engine's own `CompassLaw.force` (`tools/compass_loop.py`, `results/model_gate/COMPASS_LOOP.md`;
our own model, class S, never a proof), every row kept whichever way it fell:

- M1, the proof's own case: 8 of 8 rows at or under R*, the largest tail 1.000 R* (a push held outward settles exactly on
  R*: the bound is tight).
- M2, a muscle that lags its lever by τ = 0.25, 1, 2 and 4 beats: without damping 24 of 32 rows at or under R*, the
  largest 1.870 R* (a slow push, τ = 4 beats); with the default damping for that τ, 31 of 32, the largest 1.105 R*; with
  three times the default, 32 of 32.
- M1 with the damping set for a lag the muscle does not have: with the default, 31 of 32, the largest 1.147 R*; with three
  times the default, 17 of 32, the largest 2.629 R*.

So on a lagging muscle the damping keeps the reading inside the proved radius where the undamped loop overshoots it, and a
damping set from a response time the muscle does not have can cost more than it gives: each wire's declared τ is part of
its tune. A proof of the damped, lagging loop (three states: the reading, the lever and the velocity estimate) is open
(section 5).

## 2. The plug's clip (`Plug.write`)

| Claim | Statement | Result |
|---|---|---|
| P1 | lo ≤ hi ⇒ lo ≤ clamp(x) ≤ hi: every value sent lies inside the cover | proved |
| P2 | lo ≤ x ≤ hi ⇒ clamp(x) = x: nothing inside the cover is clipped | proved |
| P3 | clamp(clamp(x)) = clamp(x) | proved |

## 3. The verdict's rule (`omnicompass/verdict.py`, judge "interval")

A trial step is allowed when three things hold: it does not read LOSS (no 95% interval wholly above zero), its median
cost mk ≤ min(m₀, m[native]) (1 + tol), and the largest estimated change is at most τ = ln(1 + tol).

| Claim | Statement | Result |
|---|---|---|
| V1 | allowed ⇒ every interval's lower end ≤ 0: an allowed step never reads LOSS against either reference | proved |
| V2 | allowed ⇒ every estimated change ≤ τ and mk ≤ m₀ (1 + tol) | proved |
| V3 | allowed ⇒ mk ≤ m[native] (1 + tol): stepwise, steps cannot add up past the cost first measured at native | proved |

## 4. The core engine as executed (`omnicompass/core.py`)

The engine does not run the continuous law. Per micro step h = 0.01 it:
1. computes the command u[k] from x[k];
2. holds u[k] through the four stages of one RK4 step;
3. takes x[k+1] = Fₕ(x[k], u[k]).

Theorems E1 to B1 are about that map, over the declared box:
- every parameter in `PARAMETER_RANGES`;
- E₀ and I₀ in [0, 1];
- U₀, S₀, B₀ and B′₀ in [−1, 1], with S₀ above the unstable root S₋ (theorem S1's premise; the declared box has
  starts below S₋, from which S leaves every bound, and they are outside every claim);
- the target σ = ±1, nearest or aimed wrong.

| Claim | Statement | Method | Result |
|---|---|---|---|
| E1 | E[k] ∈ [min(0, (β − c)/α[E]), max(1, (β + c)/α[E])] ⇒ E[k+1] in the same interval, for every value v[eff] takes at the four stages (abs(v[eff]) ≤ c) | SMT, exact linear arithmetic | proved |
| E2 | every RK4 stage of E lies in that interval widened by 0.13 | SMT | proved |
| I1 | for any drive F[i] ∈ [F[lo], F[hi]] at the four stages, I[k] ∈ [min(I₀, F[lo]/λ[I]), max(I₀, F[hi]/λ[I])] ⇒ I[k+1] in it too | SMT, nonlinear | proved |
| S1 | S moves toward its stable root S₊ and never past it: with L = sup abs(dṠ/dS) on the S box, every RK4 stage stays on the same side of S₊ when h L < 1 | intervals: L ≤ 1.953, h L ≤ 0.0196 | proved |
| U1 | the drift is below the actuator's limit on the whole stage box: sup abs(f[U]) ≤ F[D] = 16.32 < 25 | intervals | proved |
| U2 | every unsaturated micro step: abs(e[k+1]) ≤ (ρ + b) abs(e[k]) + a, ρ = 1 − h K[P] = 0.88, a ≤ 0.006495, b ≤ 0.02399 | intervals and the mean value theorem | proved |
| U3 | the ball abs(e) ≤ r* = a / (1 − ρ − b) ≤ 0.0677 is entered and never left. It lies inside the basin (0.10) and inside the unsaturated region. Beyond abs(e) = 0.0076 the error never changes sign, so U never overshoots σ by more than r*. Every RK4 stage of U lies in the stage box [−1.2, 1.2] | intervals | proved |
| U4 | every saturated micro step moves U toward σ by at least h (25 − F[D]) ≥ 0.0868 and at most 0.4132. Saturation needs abs(e) > 0.7238, so the step never passes σ | intervals | proved |
| U5 | from any admissible start (abs(e₀) ≤ 2, the target aimed wrong included), abs(e) ≤ 0.10 within 119 micro steps (95 unsaturated, 24 saturated) of the run's 200 | intervals | proved |
| B1 | the bath (B, B′), a linear damped oscillator driven by S, x′ = A x + (0, γ[c] δ S) with A = [[0, 1], [−ω[B]², −ω[B]/Q[B]]]: for every (ω[B], Q[B]) in the box the spectral radius of its RK4 step R(hA) is at most 0.99995, so it shrinks by at least 5.0 × 10⁻⁵ every micro step, stays bounded under the bounded S, and forgets its start | intervals and the remainder of eˣ | proved |

**How U2 is proved.** Unsaturated, the command cancels the drift at x[k] exactly, so k₁ = −K[P] e[k] and
e[k+1] = ρ e[k] + (h/6)(2 D₂ + 2 D₃ + D₄), where D[i] is f[U] at stage i less f[U] at x[k]. By the mean value theorem on the
segment to each stage:

    abs(D[i]) ≤ g[U] abs(ΔU[i]) + g[E] abs(ΔE[i]) + g[S] abs(ΔS[i]) + g[t] abs(Δt[i])

with the partial-derivative bounds g taken over the stage box. The stage displacements are bounded by the step times the
stage slopes (K[E] for E, K[S] for S, K[P] abs(e) + abs(D) for U), which gives abs(D[i]) ≤ A[i] + B[i] abs(e) by
recursion over the four stages. The enclosures are:

- g[U] ≤ 35.42, g[E] = 4.2, g[S] ≤ 10.0, g[t] ≤ 12.5;
- K[E] ≤ 12.55, K[S] ≤ 4.99.

A floating-point allowance of 10⁻¹² is added to a for the binary64 arithmetic the engine runs in.

**How B1 is proved.** For Q[B] ≥ 1/2 the eigenvalues λ of A have real part −ω[B]/(2Q[B]) and modulus ω[B] (a complex pair, or the double root at Q[B] = 1/2). The RK4 step multiplies each eigen-direction by R(hλ), R(z) = 1 + z + z²/2 + z³/6 + z⁴/24, and the remainder of the series of eᶻ gives

    abs(R(z)) ≤ e^(Re z) + abs(z)⁵/120 · e^abs(z)

The bound rises with Q[B], so it is evaluated at the largest Q[B] over 400 cells of ω[B] with outward rounding; its largest value, 0.99995, is the spectral-radius bound. A spectral radius below 1 makes the forced linear map bounded for every bounded input, and S is proved bounded (S1).

**What this closes.** `docs/TRACKING_THEOREM.md` carried three open items:
- a proved ε[h] over the declared box;
- discrete invariance over the box;
- an interval-arithmetic proof of the admissible set.

The first two are now proved for E, U, S and I[U], and the bath is proved stable (B1). Theorem 3's ultimate bound is proved: 0.0677 against the 0.0315
the 500 fixtures reached, which lies inside it. Theorem 4's discrete half moves from V (checked on fixtures) to T for
those four states. U5 also proves that CONVEY-5 passes for every admissible fixture: at least 9 of the 20 macro steps
end inside the basin.

## 5. What is still open

- **CERT-10 for every fixture.** U5's bound guarantees 9 macro steps inside, not 10. Every one of the 500 frozen fixtures
  certifies (V), but a proof for the whole box needs a tighter entry bound: a, b and q are worst-case constants over the
  whole box.
- **The bath's amplitude as a number.** B1 proves the bath is stable and bounded for every parameter in the box; an
  explicit bound on abs(B) needs a Lyapunov function for each (ω[B], Q[B]), and is not computed here. The bath is never fed
  back into any other state (no equation of E, U, I[U] or S reads it).
- **Convergence of the forced six-state system as a whole.** Bounded is proved for E, U, S and I[U]; convergence of E,
  I[U] and the bath to a set is not.
- **Starts below S₋.** From there S leaves every bound (the basin's negative side, `docs/book/THEORY.md`). They are
  outside every claim on this page, and the quartic closure named in the theory is the engine change that would remove
  them.
- **The damped, lagging compass loop.** L1 to L4 prove the loop without damping on a muscle that follows its lever within
  the beat (section 1b). With the default damping, and on a muscle that lags, the loop is computed (class S), not proved;
  the proof needs a Lyapunov function, or an interval certificate, over the reading, the lever and the velocity estimate
  together.
- **The live governors** (`omni_controller/*`) are proved here only through the parts they share: the compass law, the
  plug's clip and the verdict. Their Kubernetes, GPU and cloud wiring is tested, not proved; none of them runs the compass
  loop's proved case (section 1b).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License, or, for a pilot, a signed, paid pilot agreement for the systems and dates it names, from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
