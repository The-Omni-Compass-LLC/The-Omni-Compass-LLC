# New passages for the Live Benchmark Engine Manual (draft, not bound into any book)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Self-contained passages written from the live benchmark engine page as it stood at commit 77130d306e (the seven-part order of 24 October)
and its source (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`: `MECH0`, `MECH_SPEC`, `MUS_SPEC`, `DIRECT_FOLLOW`, `viewNote`,
`swSet`, `LAMP`). They name sections by anchor, not number, because the page's order is changing again; monitor numbers are given
by canvas id with the number they carried at 77130d306e. Colours are named only where the page's tokens fix them (`--direct`,
violet); native's colour and the signal words are being changed, so re-read the page before binding. Each passage is written to
drop into the manual where the page's final order puts it.

---

## The Omni-Compass side: on native, or direct

**The switch.** Every monitor that draws two sides (55 of them) carries, on its knob strip, a switch named **Omni-Compass side**
with two positions: **on native** and **direct · native off**. *On native* is Omni-Compass as it ships: on top of every native
controller, which keeps running underneath. *Direct* is Omni-Compass alone on the organism: every native controller under it
switched off (autoscaler, scheduler, manager: nothing else thinks it is in charge), each muscle's setting standing where the
snapshot taken once at the start found it until Omni-Compass's own law moves it. One press on any strip sets every strip; the
monitor numbers on the page take a violet outline while direct is in view, and Omni-Compass's line on a live chart is drawn in
violet (`--direct`), never a reading's colour. The factory button puts the switch back on native, as Omni-Compass ships.

**Two governed arms, one switch.** Both governed arms run every decision beside native, each with its own brain (`W.omniOn` with
`W.brainOn`, `W.dirA` with `W.brainD`), so the switch changes which one is in view, at once and with its whole history; it never
restarts a run. The kill switch hands both back to native. Native's side never moves with the switch.

**The switchboard's Arm row.** In the control panel (`#s-health`) the switchboard's **Arm** row has four positions:
*native* engages the kill switch, so every Omni-Compass side follows native; *Omni-Compass and native* releases it and puts every
strip on native; *Omni-Compass by itself* releases it and puts every strip on direct (the harness's arm by itself; on the
stress-test model every native controller off; the same arm runs on omni-v18 in the kind rig, `ARM=solo`,
results/model_gate/SOLO_V18.md (removed)); *Omni-Compass direct* does the same and opens Omni-Compass direct (`#s-direct`) on its newest
showing. The line under the row names the monitors that moved.

**How to read a monitor under each position.** The note on each strip says what that monitor's Omni-Compass side shows:

| Monitor | On native | Direct · native off |
|---|---|---|
| The 21 monitors drawn from the live organism or the harness record (canvas ids `ringN`, `ringO`, `immCv`, `swarm`, `feed0` to `feed3`, `deskCv`, `masterCv`, `band`, `phaseN`, `phaseO`, `strip`, `cvU`, `cvS`, `cvB`, `cvNat6c`, `tCube`, `tDelta`, `tModes`; monitors 1 to 9, 11 to 19 and 53 to 55 at 77130d306e) | Omni-Compass on top of native's own controllers, as it ships | on the stress-test model: every native controller under the sixty muscles off, each setting at the snapshot until Omni-Compass's law moves it (class S); on the harness: the record's arm by itself (`realms/harness.py` `SOLO`): every machine pool's own autoscaler off, in the plant and in its twin, Omni-Compass's max alone moving those pools (class S) |
| Omni-Compass direct's playback (`dirCv`, monitor 52) | the showing's Omni-Compass and native arm beside native | the showing's Omni-Compass direct arm beside native (class L, each a single showing) |
| An orchestrator, four ways (`orchCv`, monitor 36) | the four ways as the tables wrote them | unchanged: the four ways already carry Omni-Compass on the organism alone (compassbare against nativebare) |
| Every other record monitor (the runs, the tables, the clouds, the chips) | as recorded | unchanged, and it says so: no direct run of it exists yet, so its Omni-Compass side stays as recorded, never invented |

A harness record built before the arm existed carries no direct arm; the strip then says the Omni-Compass side shows the arm on
native until the record is rebuilt.

**What direct reads today (class S, our own model; the harness record the page carries, `readings_solo`, written by
`docs/engine/export_harness_trace.py` on seeds 3000, 3001 and 3002 as runs A, B and C).** On the harness organism, Omni-Compass by
itself against native: the work done fell 4.3%, 4.1% and 5.1% (less work: LOSS in all three runs); the muscle-decisions over the
line rose 178%, 181% and 200% (more over the line: LOSS in all three runs); the power drawn fell by less than 0.01% in each run
(the record reads it GAIN; a change that small is under the key's 0.5% floor). Each muscle alone, by itself against native: the
muscle-decisions over the line fell 29.2%, 20.9% and 26.1% (GAIN in all three runs), the share of its run each muscle took to
clear its line fell 26.6%, 24.4% and 24.1% (GAIN), the work and the power STEADY. Why: the max is built to ride on top of native's
controller; alone, the floor it holds is the snapshot, not native's controller, so in one body the pools that native would have
grown stand at their snapshot while the climb passes them. That is why Omni-Compass sits on top of native; the organism's reading
by itself is a LOSS at the factory tune and is on the next version's list with its cause (Honesty: the row stands). A LOSS seen on
a monitor while the strip reads direct is this reading, not a fault of the page.

---

## The mechanism panel: the engine's own knobs

**Where it is and what it turns.** Inside the control console (`#s-desk`, the panel `#mechPanel`) stands a second set of knobs.
The console's other knobs change the plant's conditions (demand, noise, sense delay, faults, the load profile); these change the
engine's own equations while it runs. Each knob is a constant of the brain (`omnicompass/core.py`), the governor's law
(`omnicompass/adapter.py`, `omnicompass/nervous_system.py`), the compass law (`omnicompass/compass_law.py`), Omni-Compass's hand on
each muscle, the model's native controller, or one muscle's body. Turned, the next decision of the live stress-test model is
computed with it, on both governed arms (on native and direct); native's controller knobs move every native controller, the one
under Omni-Compass on native included.

**How to turn one, and how to read it.** Each knob is a slider with its value, its equation and its factory value under it, and ↺
beside it puts that one knob back. A knob turned from the factory turns violet; each group has a button that puts the group back;
**The mechanism back to the factory** puts every knob back, and the console's factory button puts back every knob of the page,
these included. The count beside it reads either "every knob at the factory: the engine as it ships" or how many knobs are turned,
"a variation of the mechanism (class S); its readings are its own". Every turn is written to the console's event log with its
decision. Each group prints a live reading of the quantities its knobs act on, every decision, and the line at the top of the
panel prints the live model's decision with the muscles past the line, the work served, the work failed and the work waiting this
day, native beside the Omni-Compass side in view. The harness replays recorded positions, so turning any knob moves the live benchmark engine
to the stress-test model (the log says so); the knobs act on that model only. The proof engine, the core's Monte Carlo and
`docs/engine/check_live_engine.py` read the factory numbers, so every digest stays the Python's.

**Where each group acts.** The compass law, Omni-Compass's hand, native's controller and every muscle's body move the muscles at
once. The brain's four pieces move the brain's own state (E, U, I[U], S, B on the brain's monitors) and its grants: at the max
every organ may add capacity unless a security hold stands, so the brain's calm acts through the give-backs; set the dial to the
tune-down to watch the four pieces move the muscles too.

**Piece 1, the state: E, U, I[U] and the basin** (`omnicompass/core.py`, `cpp/src/core.cpp`). Live reading: E, U, I[U], the push,
and whether U is in its basin.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the pull toward the basin, K[P] | 0 to 30 | 12 | u = −U̇ + K[P]·(1 − U), bounded by U[auth]; push = u/U[auth]; a push above κ's knee holds every give-back |
| the command's authority, U[auth] | 5 to 50 | 25 | the largest command; the larger it is, the smaller the same command reads as push |
| assimilation, a | 0 to 1 | 0.339 | x ← (1 − a)·x + a·x[obs]: 0 hears nothing, 1 forgets everything |
| the double well's depth, μ | 0 to 8 | 3.782 | U̇ = μ·U·(1 − U²) − Ė/E[max] − λ[U]·U + u: two basins at U = ±1, a ridge at 0 |
| energy's relaxation, α[E] | 0.5 to 8 | 3.487 | Ė = −α[E]·E + β[int] + β[ext] + v |
| energy's scale, E[max] | 0.5 to 4 | 2.0 | unity loses Ė/E[max]: the smaller, the harder energy shakes it |
| energy's drag on the integral, σ₁ | 0 to 1.5 | 0.38 | İ[U] = (1 − U) − σ₁·E − δ·S − λ[I]·I[U] |
| the integral's leak, λ[I] | 0 to 2 | 0.719 | how fast the remembered shortfall fades |
| unity's own leak, λ[U] | 0 to 1 | 0 | a drag on U itself |

What an operator sees: a lower K[P] or a lower a leaves U slower to return to its basin after a surge, and the push on the brain's
monitors smaller; a shallower μ flattens the double well, so the ball on U's landscape wanders nearer the ridge; a smaller E[max]
lets the same stress tilt the well harder.

**Piece 2, the basin's potential and flow: S and Φ(S)** (`omnicompass/core.py`). Live reading: S, S[eq] beside its factory value,
and σ = S/S[eq], with a note when σ passes 1.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the inflow, δ | 0.05 to 2 | 0.705 | Ṡ = δ − α[s]·S − ¾·β[s]·S², so Φ(S) = −δ·S + ½α[s]·S² + ¼β[s]·S³ and Ṡ = −Φ′(S) |
| the linear drain, α[s] | 0 to 0.6 | 0.12 | the flow rests at S[eq], the root of Ṡ = 0: S[eq] = (−α[s] + √(α[s]² + 3β[s]·δ))/(1.5·β[s]), about 2.37 at the factory |
| the quadratic drain, β[s] | 0.01 to 0.6 | 0.10 | σ = S/S[eq] above 1 holds every give-back |

What an operator sees: a larger δ or smaller drains raise S[eq] and the stance's resting place on its landscape; while σ stands
above 1 the panel says every give-back is held, and on the tune-down the give-backs stop.

**Piece 3, the bath: B and Ḃ** (`omnicompass/core.py`). Live reading: B, Ḃ, the bath's natural period 2π/ω[B] (about 6.28 at the
factory) and its damping ω[B]/Q[B] (0.4 at the factory).

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the bath's frequency, ω[B] | 0.2 to 3 | 1.0 | B̈ = γ[c]·δ·S − (ω[B]/Q[B])·Ḃ − ω[B]²·B; the drive on energy beats at ½ω[B] |
| the bath's quality, Q[B] | 0.5 to 10 | 2.5 | the higher, the less the bath is damped and the longer it rings |
| the flow's coupling into the bath, γ[c] | 0 to 3 | 1.0 | how much of the flow S drives the bath |
| the bath's drive on energy, c | 0 to 3 | 1.0 | v = cos(½ω[B]·t)·c·tanh(z) enters Ė |
| the drive's offset, λ₀ | −2 to 2 | −0.40 | z = λ₀ + λ₁·(U − ½) + λ₂·S |
| unity's weight in the drive, λ₁ | 0 to 3 | 1.55 | as above |
| the flow's weight in the drive, λ₂ | 0 to 3 | 1.15 | as above |

What an operator sees: a higher Q[B] lets B ring longer after a disturbance on the bath's landscape; a larger c feeds that swing
back into E, so the stress on Piece 1's reading oscillates.

**Piece 4, the governor: one law coupling every muscle** (`omnicompass/adapter.py`, `omnicompass/nervous_system.py`,
`cpp/src/governor.cpp`). Live reading: ρ*, κ, h, calm, and the organs that may give back now.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the utilisation target, ρ₀ | 0.5 to 1 | 0.914 | ρ* = clamp(ρ₀ − k[I]·I[U] − k[E]·E, ρ[min], ρ₀): how full a muscle may run after a give-back |
| the target's floor, ρ[min] | 0.3 to 0.95 | 0.627 | as above |
| the shortfall's pull on the target, k[I] | 0 to 1 | 0.252 | as above |
| energy's pull on the target, k[E] | 0 to 1 | 0.297 | as above |
| the push that still lets go, κ's knee | 0 to 0.05 | 0.005 | κ = 1 while push ≤ the knee, else knee/push |
| the unity gate, U[gate] | 0 to 0.95 | 0.481 | h = (U − U[gate])/(1 − U[gate]); calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)) |
| the grants θ[nodes], θ[pods], θ[cpufreq], θ[power], θ[routing], θ[gpu] | 0 to 1 each | 0.7, 0.5, 0.3, 0.3, 0.5, 0.3 | an organ may give back only while calm ≥ its θ, the line clean, the senses seeing |

What an operator sees: raising an organ's θ above the live calm removes that organ from the list that may give back now; on the
tune-down its muscles stop handing capacity back. At the max this piece acts only through the give-backs.

**The compass law: one band, two antagonist forces, smooth** (`omnicompass/compass_law.py`, `cpp/src/compass_law.cpp`). Live
reading, for the muscle chosen in the last group: native's p, Omni-Compass's p, v and force F, k[d] for its τ, and the muscles
past the line now on each side.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the band's low edge (load ratio), lo | 0 to 0.6 | 0.2 | p = (r − lo)/(hi − lo): where each muscle stands in its band |
| the line (load ratio; 1 = full), hi | 0.6 to 1.5 | 1.0 | past it a muscle is over the line |
| the centre, where the two forces balance | 0.2 to 0.8 | 0.5 | below it the force pulls capacity back, above it pushes capacity in |
| the cushion before the line | 0 to 0.25 | 0.05 | from 1 − cushion the force is the whole authority A: a muscle is never let past the line |
| the spring, k[p] | 0.1 to 4 | 1 | F = A·tanh((k[p]·(p − centre) + k[d]·v)/A) |
| the authority, A | 0.1 to 2 | 1 | the force's ceiling: smooth (tanh), never hammering |
| the velocity's smoothing, s | 0 to 0.95 | 0.5 | v ← s·v + (1 − s)·Δp/dt |
| the damping, × each muscle's critical k[d] | 0 to 3 | ×1 | k[d] = max(0, 2√(k[p]·τ/dt) − 1)·dt for each muscle's own τ |

What an operator sees: the phase plane's shading (the force field) moves with the centre, the spring and the authority; a smaller
cushion lets the right-hand dots run closer to the right edge before the force fails up; less damping lets the Omni-Compass side
overshoot and the strip's muscles past the line rise.

**Omni-Compass's hand on each muscle: the max and the tune-down** (the page's capacity law on `omnicompass/adapter.py`). Live
reading: the settings Omni-Compass wrote this decision, the muscles it holds away from native's setting (in direct, from the
snapshot), and the dial.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| the push: capacity added per unit of force | 0 to 1 | 0.30 | the max: L ← L·(1 + gain·F) while F > 0 and the organ may expand; never below native |
| the lift-off's base | 0 to 1 | 0.15 | F < 0: L moves toward native's setting by min(1, base + slope·|F|) |
| the lift-off's slope | 0 to 2 | 0.5 | as above |
| the tune-down's floor, × native | 0.5 to 1 | 0.85 | the dial at the tune-down: never under this share of native's setting |
| the tune-down's step per unit of force | 0 to 0.5 | 0.10 | one step back: L = max(floor·L[nat], min(L, L[nat])·(1 + step·F)) |
| the dwell before a give-back, decisions | 0 to 10 | 3 | calm decisions in a row before one step back |
| the give-back's ceiling in the band | 0 to 1 | 0.40 | a step back only while p is under it |

What an operator sees: a larger push gain makes the Omni-Compass side add capacity faster under a surge (capacity held rises:
power given), a smaller lift-off holds it longer after the surge; the four tune-down knobs act only with the dial on the
tune-down.

**Native's own controller under every muscle** (the model's native rule: Kubernetes' published autoscaling rule, written by us).
Live reading: the settings native's controllers moved this decision, and the chosen muscle's setting and last wish.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| native's target load | 0.3 to 0.95 | 0.70 | desired = current·observed/target |
| native's tolerance | 0 to 0.5 | 0.10 | inside ±tolerance of the target native does nothing |
| native's largest step up, × current | 1 to 5 | ×2 | the most one step may add |
| native's stabilisation window, decisions | 1 to 20 | 5 | a step down only to the highest wish in the window |

What an operator sees: both sides change, because native's controller runs under Omni-Compass on native too; only direct, where
native's controllers are off, is untouched. The phase plane marks native's target on native's side while the stress-test model
runs.

**Every muscle: scale out, scale in, scale up, its response, its switch** (the model's sixty muscles, twelve to a body part).
Pick the muscle, then the scope: **this muscle**, **its body part** or **every muscle**. Live reading: the muscle's units on
native and on the Omni-Compass side, its ceiling, floor, size, τ and sensing delay, and whether it is governed.

| Knob | Range | Factory | Equation it enters |
|---|---|---|---|
| scale out: the most units it may hold, × its factory ceiling | ×0.25 to ×4 | ×1 | the ceiling c[max]; Omni-Compass's max rides up to it, never past |
| scale in: the fewest units, × its factory floor | ×0.25 to ×4 | ×1 | the floor c[min]; no controller takes it below |
| scale up: each unit's size | ×0.25 to ×4 | ×1 | capacity in service = units × size, on every arm alike |
| its response time τ | ×0.25 to ×4 | ×1 | c ← c + (L − c)·(1 − e^(−1/τ)); the law's damping follows τ |
| its sensing delay | +0 to +6 decisions | +0 | decisions between what the muscle does and what its controllers read |

The group's switch reads **Omni-Compass governs it** and, pressed, hands the muscles in scope back to native's own controller
while every other muscle stays governed; pressed again, Omni-Compass governs them again. The kill switch hands every muscle back
at once.

**A changed tune is not a result.** Every knob of this panel shows a variation of the mechanism (class S, our own model). The
benchmarks prove the factory tune only; a tune other than the factory's is its tuner's, and so are its readings. This is the one
place on the page where a person may turn the engine away from its factory tune, change its mechanism of action by hand and watch every
monitor move with it; the factory
button puts it back.

---

## The lights: STEADY only inside ±0.5%

A light that compares Omni-Compass against native at this moment reads by the key: GAIN where the Omni-Compass side helps the
muscle and the organism, LOSS where it hurts, STEADY where the two cannot be told apart. From 24 October STEADY is held to a change
inside ±0.5% of native's value (`LAMP.near` = 0.005; the founder's order: "Any gauge that gives anything over a 0.5 percent change
either way is a change"). On a cluster replay, a 95th percentile 0.5% or more faster than native's at the same moment lights GAIN,
0.5% or more slower lights LOSS, and only a difference inside ±0.5% lights STEADY; the light's own words say "within 0.5% of
native's". Where a light counts (the muscles over their line, the pods waiting), any difference of one is a change. The 0.5% rule
is the light's; the three-run tables keep their own rule (every interval clear of zero in all three runs, and under the key's
0.5% floor a change reads STEADY, under the floor), so a light that turns for a moment is a moment, and the judged reading stays in
the table. The heading light is unchanged: a gauge within 3% of its line, or whose own slope crosses it within three readings,
lights the middle lamp.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
