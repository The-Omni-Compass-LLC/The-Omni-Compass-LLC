# Omni-Compass: mechanism of action, from the equations to the muscles

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Every statement here is tied to code in this repository, and the measured numbers are reproduced by
`python tools/mechanism.py`, which writes `results/MECHANISM_OF_ACTION.json`. The engine files are frozen. Their SHA-256
hashes are checked by `verify.py`.

## 1. The state: six numbers that describe the whole system

| Symbol | Name | What it stands for in a data centre |
|---|---|---|
| E | energy / excitation | how hard the system is being driven: queues, overload, power, heat |
| U | order parameter | how healthy and settled the system is: +1 healthy basin, -1 failed basin |
| I[U] | integrated need | unmet need accumulated over time: memory of pressure that has not been relieved |
| S | stress | slow structural stress from heat, power, network, security, staleness |
| B, Ḃ | bath and its rate | a damped oscillator driven by stress: the slow "tide" of physical load |

## 2. The equations (omnicompass/core.py, lines 5-12)

```
(1) dE/dt     = −α[E] E + β[int] + β[ext] + v[eff]
(2) dU/dt     = μ U (1 − U²) − (dE/dt)/E[max] − λ[U] U + u,          |u| ≤ 25
(3) dI[U]/dt  = (1 − U) − σ₁ E − δ S − λ[I] I[U]
(4) v[eff]    = cos(ω[B] t / 2) · c · tanh(λ₀ + λ₁ (U − 0.5) + λ₂ S)
(5) Φ(S)      = αₛ S² / 2 + βₛ S³ / 4 − δ S
(6) dS/dt     = −dΦ/dS = δ − αₛ S − (3/4) βₛ S²
(7) dB/dt     = Ḃ ;   dḂ/dt = γ[c] δ S − (ω[B] / Q[B]) Ḃ − ω[B]² B
(8) R[B]      = finite-difference audit of (7) at every step, never fed back
```

Each term does one job:

- **(1) Energy.** Energy decays at rate α[E] = 3.487. It is driven by two forcings: internal pressure `β[int]` (queue and
  overload) and external pressure `β[ext]` (power, heat, network, staleness, security). The drive term `v[eff]` (4) is
  bounded by `c` through the hyperbolic tangent, so no input can drive E without limit. This is the saturation (the tanh
  "speed limit"): however extreme the observation, the engine's response rate is capped at c = 1.
- **(2) Order.** `μ U (1 − U²)` is a double-well (bistable) drift with two stable basins, U = +1 (healthy) and
  U = -1 (failed), and an unstable ridge at U = 0. A rise in energy (`dE/dt`) pushes U out of the healthy basin. `u` is
  the bounded control input.
- **(3) Integrated need.** I[U] grows while U is below 1 (the system is not settled). It is reduced by energy and stress
  already being dealt with, and it leaks at λ[I] = 0.719. It is the engine's memory of unrelieved pressure.
- **(5)-(6) Stress.** A cubic potential (the "well in the basin"). S rolls downhill to its stable root. This is the
  slowest restoring force.
- **(7) Bath.** A damped harmonic oscillator (natural frequency ω[B] = 1, quality Q[B] = 2.5) driven by stress. It turns
  stress into a smooth, lagged "tide". It is the only second-order element.
- **(8) Audit.** The bath equation is re-checked numerically every step. The check is never fed back.

Integration: classical 4th-order Runge-Kutta, 10 micro-steps of 0.01 per macro step (`rk4_step`, `macro_step`). The C++
twin matches the Python to 3.6e-15 on 500 reference trajectories.

## 3. From telemetry to state (omnicompass/adapter.py, `observe_vector`, `assimilate`)

Each decision the telemetry is normalised to nine observations: q (queue), load, power, thermal, network, drift, stale,
security, conflict. An observed state is computed from them:

```
E[obs]   = 0.25 q + 0.18 max(0, load − 0.85) + 0.16 power + 0.13 thermal + 0.10 network + 0.08 drift + 0.06 conflict + 0.04 stale
U[obs]   = 1 − (0.27 q + 0.18 power + 0.16 thermal + 0.12 network + 0.12 drift + 0.10 conflict + 0.05 stale)
S[obs]   = 0.36 thermal + 0.28 power + 0.18 network + 0.10 security + 0.08 stale − 0.20 q
B[obs]   = 0.52 power + 0.26 thermal + 0.22 drift
I[obs]   = q + drift + conflict
β[int] = 0.58 q + 0.42 max(0, load − 0.75)        β[ext] = 0.33 power + 0.27 thermal + 0.20 network + 0.12 stale + 0.08 security
```

The state is blended toward the observed state with weight a = 0.339: `x ← (1 − a) x + a x[obs]`. It is then evolved
by one macro step (0.1 engine time units) of equations (1)-(7).

## 4. From state to action (the allocation law, `Governor.step`)

```
push     = u(x) / 25,  u(x) = clip(−f[U](x) + 12 (1 − U), −25, 25)        equation (2)'s controller, evaluated, not applied
ρ*     = clamp(ρ₀ − k[I] I[U] − k[E] E, ρ[min], ρ₀)                      target utilisation (the HPA target)
n[req]    = ceil(n load / ρ*) + ceil(k[q] q n)                               machines wanted
release  only while push ≤ push_release (the engine reports convergence), after band and dwell
cap      = clamp(cap_now load (1 + margin), cap_min, 1) when calm, U ≥ U[gate] and the line clean for the governor's
           own clear time (omni-v15: the request cannot switch back and forth at one threshold); 1 under backlog or a breach;
           always ≤ 1 − cap_gain max(0, B − B[cap])                         the bath limits the power cap
change   permitted only while U ≥ U[gate] and no security block
rollback authorised if S ≥ S[rollback], U is falling, or a security block is seen
```

## 5. Which equation drives which muscle

| Muscle | Engine quantity used | Where |
|---|---|---|
| HPA target (pods) | rho* from I[U] and E, equations (1) and (3) | adapter `Governor.step`; live `omni_controller/controller.py` |
| Node pool (machines) | n[req] from load, queue and rho*; release gated by push from equation (2) | same |
| Power cap (pod CPU limits, CPU frequency, GPU limit) | cap from U gate and bath B, equation (7) | same; `omni_controller/muscles.py` |
| Rollout guard | change_permitted (U), rollback (S, dU) | `muscles.py` |
| Security hold | security observation raises S and blocks expansion | adapter, shield |
| Speed-first law | rho* for pods; push gates machine release | `omnicompass/speed.py` |
| Right-sizing | rho* sizes CPU; E widens the memory margin; push gates scale-in | `omnilab/rightsize.py` |
| Cold start | rho* sizes instances; I[U] sets how long to keep warm | `omnilab/coldstart.py` |
| GPU packing | I[U] pre-warms nodes; push gates power-off | `omnilab/gpupack.py` |
| Training power | E tightens the applied ramp limit under sustained grid stress | `omnilab/powersmooth.py` |
| GPU health | S and E shorten the checkpoint interval | `omnilab/health.py` |
| Cooling | E widens the inlet-temperature margin | `omnilab/cooling.py` |
| Inference | the full allocation law (node_delta) sizes replicas | `omnilab/inference.py` |
| Agent containment | I[U] throttles; the security observation contains | `omnilab/containment.py` |
| VM energy | I[U] and E raise the learning rate when attribution goes stale | `omnilab/vmenergy.py` |

## 6. Measured: what the equations actually do inside the governor

Measured on a real observation stream (fleet plant, web services, fleet mode, 360 decisions):

| Mode (eigenvalue of the Jacobian at the operating point) | Time constant | In decisions |
|---|---|---|
| -7.90 | 0.13 | 1.3 |
| -3.10 | 0.32 | 3.2 |
| -0.72 | 1.39 | 13.9 |
| -0.20 +/- 0.98i (the bath) | 5.0, period 6.4 | 50, rings every 64 decisions |
| -0.17 | 6.0 | 60 |

- **Every mode is stable** (all real parts negative). The operating point is a stable equilibrium inside the healthy basin:
  E = 0.095, U = 0.976, S = 0.315, B = 0.10. This is the basin keeping everything in, stated as mathematics.
- **Per decision, the equations and the observation move the state about equally.** Across all six variables the
  equations contribute 45-50% of each step's movement and the observation blend the rest.
- **Equation (2)'s control input u is not applied during governance.** The engine evolves open-loop (u = 0). The control
  law is evaluated only to produce `push`, which decides when capacity may be released.
- **Compute:** about 95 microseconds per decision in Python, and about 2.9 microseconds in the C++ twin.

## 7. What this explains, and what it points to

- **Why "engine off" scores close to "engine on" in the muscle benchmarks.** With the equations frozen, the observation
  blend still moves the state. Both versions are then low-pass filters of the same telemetry. The engine's fast modes
  (1-3 decisions) behave almost like the blend itself. Its distinct contribution is its slow memory: I[U] (14 decisions),
  S (60) and the bath (period 64 decisions). The muscle mappings mostly read E and rho*, which live on the fast modes.
- **The engine clock is not matched to the workload's rhythm.** One decision advances engine time by 0.1. At 60-second
  decisions the bath rings every 64 minutes, but web demand has a 24-hour rhythm and training power a 2-second one. This
  is a wiring choice in the adapter (engine time per decision), not a property of the equations.
- **The controller in equation (2) is unused as an actuator.** Wiring its output u (or U's trajectory under u) directly
  to the actuators is the unexplored way to "let the math do the work".

Three wiring experiments follow directly. None changes a single equation:

1. **Clock matching.** Set engine time per decision so that the bath's natural period equals the workload's rhythm.
   The oscillator in (7) then carries the cycle and can anticipate it.
2. **Slow-mode actuation.** Drive machines from I[U], S and B (the memory modes) rather than E (a fast mode).
3. **Closed-loop actuation.** Apply equation (2)'s u and use its magnitude, not only its sign, as the actuator command.

Each is testable in the existing harness against every platform in the league (tuning/league.py), and will be tested
there.


## One pedal: push, lift off, idle, reset, and the kill switch

Omni-Compass drives a system the way a self-driving car drives itself: it feels, gauges and adjusts, with nobody in
the seat. The words below are used the same way everywhere in this repository.

**Two names only.** **native** is the system as it runs on its own (Kubernetes and its autoscalers, the card's
firmware, CityLearn's controller). **omni** is Omni-Compass on top of native: the same native system, with Omni-Compass
governing it. Omni-Compass never runs instead of native, only on top of it, so every comparison is native against omni.

**The modes.** Off (manual): Omni-Compass not driving, native runs alone. Watching: Omni-Compass reads every gauge and
logs what it would do, and writes nothing. Autopilot: the one pedal below. Cruise and idle at once: for work that comes
as a pile.

| Term | Meaning | In the code |
|---|---|---|
| **Push** | Traffic climbs and capacity is added at once, never held back; the whole cluster can take work the instant it is needed | (8.3); a lower HPA target is never limited |
| **Lift off** | Traffic falls and capacity is eased off a step at a time, handed back toward native, never below idle | (8.4)-(8.5); coasting, rule 6 |
| **Idle** | The pedal lifted all the way: calm traffic, the engine running at its floor (two machines in service, ready) | `MIN_NODES`, the floor of the staging law (8.8) |
| **Reset** | Every setting the governor ever wrote is handed back to where native had it, read back, and the record removed; the next run starts fresh. Every benchmark arm ends with one and checks it | the reset file (`--kill-file`, a name kept for compatibility), `Controller.restore` |
| **Cruise** | A pile of work waiting for a place: machines in service up to the pool's own top, read live (a fixed pool's every machine at once, a growing pool a step a decision), held there without second-guessing, until the line has been empty for two decisions | rule 7, `--cruise-after` |
| **Idle at once** | The work is done and demand is at zero (the service at its least pods, wanting no more, at half its target or less): the pedal lifted all the way in one move, straight to idle (the floor), every safety check still holding | rule 8, `--idle-demand`, amendment 9 |
| **Kill switch** | Security only: one switch in a human hand that turns Omni-Compass's governing off across the whole system at once, for anything rogue or anyone trying to drive a system through Omni-Compass's brain | `omnicompass/master.py`, `tools/omni_switch.py off` |

The floor is a number the operator sets; lifting off never takes the system below it, however far the pedal is
lifted. Earlier dated records, and the sealed original engine files, call the reset a "kill switch"; they
are kept word for word.

## 8. The staging law: machines on and off in order, with demand that moves

Demand climbs, spikes, eases part way, climbs again and settles to idle. The staging law decides how many machines are
in service at every decision, and which ones, so that capacity follows demand up at once and comes back down only as
far as it safely can. It is the compass law (`omnicompass/compass_law.py`) applied to the machine pool
(`omni_controller/controller.py`), the release gate (`omnicompass/nervous_system.py node_release_gate`), the verdict
(`omnicompass/verdict.py`) and the actuator (`scripts/kind_nodepool.sh`). Every symbol below is a line of that code.

**Position and force.** The service reading r (the 95th-percentile response time, or the pressure that stands for it)
is placed in its band [lo, hi], where hi is the response line:

    p = (r - lo) / (hi - lo),      v = s v + (1 - s) (p - p_prev) / dt                       (8.1)
    F = A                                       if p >= 1 - c        (fail up, past the wall)
    F = A tanh( (kp (p - p0) + kd v) / A )      otherwise; F = 0 if F < 0 while v > 0 and p > p0   (8.2)

with the band's center p0 = 0.5, cushion c = 0.05, authority A = 1, kp = 1 and kd = max(0, 2 sqrt(kp tau / dt) - 1) dt
(critical damping for a muscle that answers in tau seconds). F > 0 asks for capacity, F < 0 offers it back.

**How many machines.** With n machines in service now, n[nat] the count native ran, m the floor (two by default, `MIN_NODES`) and M the
machines that exist (every machine usable; an operator may hold whole machines back with `NODE_CUSHION`, off by
default), every count stays in m <= n' <= M. The protection is not a machine sitting out: it is the band inside every
machine. Capacity is added at 95% of the response line, before the line is reached (8.2-8.3), and a machine goes back
only if the ones left still run at or under the engine's utilisation target rho (8.5): a margin spread over all of
them.

    up      n' = min(M, max(m, n + 1))                              if p >= 1 - c                     (8.3)
    down    n' = max(m, n - 1)                                      if F < R and p < p0 and the verdict
                                                                    allows n_nat - (n - 1) and the gate G holds  (8.4)
    hold    n' = n                                                  otherwise

with the release threshold R = -0.2. Up is immediate and is never gated. Down is one machine per decision, never below the floor, and only
when every term of the release gate holds:

    G = [n > 1] and [nothing pending] and [pods not scaling up] and [no breach now] and
        [ used / ((n - 1) x per_node) <= rho ] and [contraction authority] and [every sense live] and
        [the last machine command landed]                                                          (8.5)

rho is the engine's utilisation target: after a machine goes back, what remains runs at or under rho. The verdict
(section 7 of the GPU preregistration, `omnicompass/verdict.py`) allows a machine count below native only after a
paired trial showed the service at that count at most a 2% LOSS than at the count before; that 2% is where the trigger
sits, inside the engine.

**This is hysteresis by construction.** The up condition (p >= 0.95) and the down condition (p < 0.5 with F < -0.2)
are far apart, so a demand that hovers never makes machines flap; a spike crosses the wall and adds a machine at once;
a dip has to be deep, calm and sustained before one goes back, and then only one per decision. Between the two, the
count holds.

**Which machines.** The actuator orders the pool:

    idle   the open machine with the fewest serving pods, then the fewest pods, goes first;
           it is marked prefer-not (PreferNoSchedule) and its pods first to go (pod-deletion-cost), so the
           autoscaler's own scale-down empties whole machines; no pod is moved, evicted or restarted   (8.6)
    wake   the idle machine still carrying the most work goes first (it is warm); the mark comes off and it is in
           service at once, with no boot                                                          (8.7)
    floor  two machines always in service (MIN_NODES, the operator may set more), ready for a spike  (8.8)
    margin  every machine usable; the cushion is the band inside each one (the 5% before the line, and rho), not a
            whole machine held out                                                                 (8.9)

An idled machine stays powered and Ready at its floor (park_frac x idle power), never off: a pod that finds the open
machines full lands on it at once, so no request ever waits on a machine Omni-Compass idled. Where a node autoscaler
underneath really removes an empty machine (Azure's cluster autoscaler, Karpenter), that same order hands it the
emptiest machine first, and the bill falls with the machine.

**The same law on every discrete unit.** Machines are one case. In the muscle models (`realms/compass_arm.py
release_safe`), a cooling plant's chillers and a compute pool's machines follow the same law: one unit back only when
the units left cover the recent peak with headroom (RELEASE_MARGIN 0.6 for machines, 0.8 of a unit's capacity for
chillers), one at a time, and back at once when the wall is reached.

**What is proved, measured and open.** The order (8.6)-(8.8) is checked through the real actuator by
`tests/test_staging_order.py` (the emptiest idles first, the warmest wakes first, two always in service, every machine usable, no pod moved).
The gate (8.5) is checked by `tests/test_node_release_gate.py`. On real Kubernetes, in the single-run sets 22 to 27 of
September (an engine before omni-v1, `results/live/LIVE_REPS_22.md` to `results/live/LIVE_REPS_27.md`: the road, never read
with the engine that stands), the law gave the same work with the 95th percentile down 53% to 65% and the machines in
service down 29% to 37%. On the engine that stands (omni-v25, `results/OMNI_INDEX.md`), all four in one run reads the work
up 43.5% on the same machines (machines STEADY, the same), demand that wanders is `results/live/V25_WANDERING.md`, and,
composed across every layer, the machines read ×0.5626: Omni-Compass's 1.78 times native's, power given
(`results/WHOLE_SYSTEM.md`, section 3). Open: an order across different kinds of
unit (a battery before a generator, a CPU before a GPU) is not wired; each pool is ordered within itself.

## 9. The state each muscle carries, and the modes as a state machine

**9.1 The compass on a muscle is a dynamical system, so its state must persist.** On muscle i the compass carries
zᵢ = (pᵢ, vᵢ, xᵢ): the position of the service in its band, its velocity, and the knob's continuous value. At each
decision k, with reading rₖ:

    pₖ = (rₖ - lo) / (hi - lo),   vₖ = s vₖ₋₁ + (1 - s)(pₖ - pₖ₋₁) / dt,   Fₖ = F(pₖ, vₖ) by (8.2)    (9.1)
    xₖ₊₁ = clamp( xₖ + sigma g(Fₖ) Fₖ (x[hi] - x[lo]), x[lo], x[hi] ),   g = UP if Fₖ > 0 else DOWN          (9.2)

with x₀ the native value and sigma = +1 when a higher value is more capacity. Two properties depend on z persisting:
(a) the knob integrates the force, xₖ - x₀ = sum_j sigma g Fⱼ span (until the cover binds), so a calm muscle eases
step by step toward its cover; and (b) the damping term kd vₖ needs pₖ₋₁. If z were made fresh at every decision
(pₖ₋₁ = pₖ, v = 0, xₖ = x₀), (9.2) would collapse to xₖ₊₁ = clamp(x₀ + sigma g F(pₖ, 0) span): a memoryless map
of the present reading, at most one step from native, with no damping. That is a different, weaker law. A renamed
attribute did exactly that on 2026-10-05; `tests/test_compass_arm.py` now fails if the compass is ever made twice on one
muscle.

**9.2 The modes.** The live controller is in exactly one mode at each decision. With qₖ the pods waiting for a place,
uₖ the scaling-up flag, c the cruise count (`--cruise-after`, 2), M the machine ceiling and m the floor:

    cruise on      q_j > 0 for the last c decisions                                                   (9.3)
    cruise off     q_j = 0 and not u_j for the last c decisions                                       (9.4)
    in cruise      n' = min(M, n + s), M the pool's own top read live, s the step; the service's autoscaler target held at the operator's own; the floor step
                   makes no read and no write                                                         (9.5)
    idle at once   (not cruising) q = 0, no breach, not u, every sensed service idle or at demand
                   <= b, the gate G (8.5) holds, every sense live, the last command landed:
                   n' = max(m, smallest n carrying the CPU in use at rho)                             (9.6)
    idle (a service at its floor)   I(h) := current = min = desired, and u_h <= target_h / 2          (9.7)
    push / lift off / idle         (8.3) / (8.4)-(8.5) / (8.8)

**9.3 Why cruise steps back (9.5).** In cruise the machines climb to the pool's own top (a fixed pool's every machine
at once, n = M; a growing pool a step a decision), so the floor step's only action (raise n to the floor the waiting pods
need) adds nothing the climb does not already give: for a fixed pool floor <= M = n. Its reads (every pod, every node, node
metrics, every HPA, each five seconds) carry no value of information, so removing them cannot change any action; they
only cost CPU and API-server time on the machines the queue is using. The service's response time is also confounded
in cruise: with a queue of other work holding the machines, a request waits on contended CPU, R = S / (1 - u[host]), not on
the service's own pods. Reading that R as the service's own queue and adding pods would answer the wrong cause. So in
cruise Omni holds the machines and leaves the service to its own autoscaler. `tests/test_compass_controller.py` checks
that the floor step makes no API read during cruise; the controller before this rule made the full set of reads every
five seconds.

**9.4 Why idle is read from the autoscaler's floor (9.7).** A served service never reads zero: a health probe or a
client's keep-alive keeps one pod at a few percent of its request. In the batch test, one pod at about 10% of its request
read as demand 0.10, above b = 0.05, and idle waited 15 minutes after the queue emptied. The autoscaler's own
floor is the observable of "no demand beyond the minimum": the pods it keeps are its minimum, it wants no more, and they
run under half the target. In the five frozen-engine web tests the service was never at its floor (0 of 5,102 readings),
so (9.7) changes nothing there.

**9.5 Reporting resolution.** A paired change smaller than one part in a million of the value
(|mean difference| <= 1e-6 |native|) is read "same", the number still shown. Below that, a difference is rounding in
floating point and in the models' accumulators, not behaviour; a deterministic run gives a zero-width interval around
it, which would otherwise read as proven.

**9.6 A lever is moved only where moving it can pay.** The compass decides how far and how fast. Whether a lever may
move at all is a property of the muscle's physics. Four cases, each derived from the muscle's own model and each its own
test:

- *Cooling power.* A zone's heat must leave it: over a run, the heat removed equals the heat made plus what the
  room's mass stores. A cap on cooling power q[max] cannot remove less heat. It only lets the temperature drift above
  setpoint while the PI command grows, and the staging rule, units = ceil(command / (0.8 q[unit])), turns that command
  into more units and more fan power, p = q[c] / COP + units x p[unit]. So a lower cap never saves energy, and the lever
  stays native. (The setpoint, which changes the COP, and the units, which change fan power at the same heat, remain
  levers.)
- *A battery's reserve.* Energy D drawn from the cells below the operator's reserve saves D sqrt(eta) of grid import,
  and the deficit is bought back at D / sqrt(eta). The net, D (1 - eta) / sqrt(eta) (10.5% of D at eta = 0.90), is
  always positive. Spending the reserve is never an energy saving; it is the price of keeping the draw under the
  connection's limit. So the reserve is spent only at the wall (p >= 0.95) and only when the battery can cover the
  excess (0 < imp - p[lim] <= p[batt]). Otherwise the operator's reserve holds, and no round trip is paid for nothing.
- *A backup reserve (a UPS).* It is held for an outage, which the model does not contain, so spending it for a peak
  trades away the reason it exists. Never a lever.
- *A compute pool's power cap.* With throughput mu(c) proportional to c^eps and the autoscaler holding utilisation near its
  target u*, the energy per unit of work is e(c) = (p[idle] / u* + p[dyn] c) / mu(c). At c = 1, de/dc > 0 (a lower cap
  saves) if and only if

      eps < p_dyn / (p_idle / u* + p_dyn)                                                                 (9.8)

  At eps = 0.4 the cap saves on CPU hosts (threshold 0.62), GPUs (0.74), databases (0.51) and radio units (0.54). It
  costs energy where idle power dominates: a quantum computer's cryostat (0.19), a network switch (0.32), storage
  (0.26). There, running slower keeps the machines on longer: race to idle. In a deployment p[idle], p[dyn] and the
  speed curve come from the machine's own specification.

- *A motion axis's effort cap.* It lowers the copper loss of a full-acceleration move, (J a[max] / kt)^2 R, and stretches
  the move, which keeps paying the standing draw p[idle] + b v[max]^2. It moves only where the first exceeds the second: a
  reaction wheel (32 W against 5 W), not EV traction, a flight axis or a robot joint.
- *A machine released from a node pool.* A machine boots in minutes, and a burst that arrives in the meantime is served
  late. So a machine goes back only when the machines left cover the recent peak at 0.3 of the pool's own release level,
  the largest margin at which no pool is later than native (`results/realms/RELEASE_MARGIN_SWEEP.md`). This is the
  verdict of the live controller (section 8) in model form.

What a lever buys is labelled for what it is. Less work per energy, with no work lost and the time over the line
proven lower, is SERVICE IMPROVEMENT WITH ENERGY TRADEOFF, the mirror of ENERGY IMPROVEMENT WITH SERVICE TRADEOFF.
Without that proof it reads LESS WORK PER ENERGY.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
