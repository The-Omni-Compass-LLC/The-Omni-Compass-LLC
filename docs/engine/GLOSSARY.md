# The Live Benchmark Engine's Glossary and Index

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

This is the back of the live benchmark engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`): every term a reader of the page meets, the 10 organisms it shows, its 2 arms and their 20 combinations, every one of the catalog's 1,107 muscles bulked by its realms, and an index of where each term stands on the page. Every definition is drawn from the file it names, and the file still carries the words quoted from it; nothing here is typed twice. It is written by `tools/live_glossary.py`, which writes the same content as `docs/engine/glossary.json` for the page. Engine: omni-v23 (digest c96ea4105d8747db).

The organisms and the muscles' plants are our own models (evidence class S) unless a line says otherwise; a model is a statement about the model, and nothing here is a result. See `DISCLOSURES.md`.

## Contents

1. The terms
2. The arms
3. The organisms
4. The scenarios: every organism under every arm
5. The muscles, bulked by their realms
6. The index

## 1. The terms

### Result Readings

- **GAIN.** The gauge moved toward its declared aim against native: more work done, a shorter wait, fewer misses or failures, or a resource cut. Decided by what the gauge is for, never by the plus or minus sign of its number; its size is printed without a sign (GAIN 73.0%), the raw change apart with its true sign. G.A.I.N.: Growth, Advantage, Improvement, Net-positive. Green. *Source: `tools/readings.py`.*
- **STEADY.** A change under 0.5% (the mean of the three runs' changes under the floor), no change at all, or a knob native already runs at the top of its range (at its limit on native). A change of 0.5% or more is never STEADY. Of three kinds: exactly the same (to nine decimal places), under the floor (a measured change under 0.5%), and, in a table read by an older key, no difference beyond the noise. Its size is printed without a sign (STEADY 0.3%), the raw change apart. S.T.E.A.D.Y.: Stable, True to baseline, Equilibrium, At par, Drift-free, Yield held. Yellow, and the yellow of the traffic signal on every monitor carries the same word. *Source: `tools/readings.py`.*
- **LOSS.** The gauge moved away from its declared aim against native: less work done, a longer wait, more misses or failures. A LOSS row is never cut: its cause is found and fixed (our own wiring first, then native's setup, then the scoring) and the test is run again. Its size is printed without a sign (LOSS 16.8%), the raw change apart with its true sign. L.O.S.S.: Leakage, Off-track, Setback, Subpar. Red. *Source: `tools/readings.py`.*
- **power given.** A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that rose: what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. The same resource falling is a cut, a GAIN. Work per energy that falls is power given too. Blue on a reading. *Source: `tools/readings.py`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **the runs disagree.** Runs that moved 0.5% or more in opposite directions: the test is unstable there and is looked into. *Source: `tools/readings.py`.*
- **shown, not judged.** A gauge declared in advance as shown only, such as the knob's own setting; counted in no total. Grey. *Source: `tools/readings.py`.*
- **the 0.5% floor.** A change of half of one percent (0.5%) or more either way is a change: GAIN, LOSS or power given by what the gauge is for. The change is the mean of the three runs' changes, each in percent of native; a mean under 0.5% reads STEADY, under the floor, with its size; every change of 0.5% or more shows its word. *Source: `tools/readings.py`.*
- **the raw change and the word.** Two numbers, never mixed: every row shows native's value, Omni-Compass's value and the raw change, (Omni-Compass − native) / native, with its true sign; the word beside it is judged by what the gauge is for, and the size printed beside a word carries no sign. A wait that fell 3% prints raw −3.0% and GAIN 3.0%; failed requests that rose 2% print raw +2.0% and LOSS 2.0%. *Source: `tools/readings.py`.*
- **the key.** GAIN, STEADY and LOSS, with power given and the letters behind each word: The Omni-Compass LLC's own convention for reading its own results, in the words of underwriting and actuarial work, where every outcome is graded as surplus, break-even or deficit. Not an actuarial, financial or insurance opinion; no outside body defined, reviewed or approved it. *Source: `tools/readings.py`.*
- **do no harm.** Omni-Compass's one goal: to strengthen the organism it governs and keep it healthy, working at the best state its own muscles can carry. Harm is judged at the organism: less output than native (less work; more time waited, missed or failed) or less health (a muscle past its own limit, a service over its own line, anything made to fail). Every muscle only as far as it can go, never past. The engine that stands keeps the strictest form: every muscle judged on itself, never below native, nothing traded between muscles; where it cannot bring a knob a GAIN, that knob stays native. *Source: `DISCLOSURES.md`.*
- **at its limit on native.** A knob native already runs at the top of its range: the max has nothing above native to give it, so Omni-Compass reads it and leaves it native. It reads STEADY. *Source: `CLAUDE.md`; `realms/compass_arm_v5.py`.*
- **alert minute.** A whole minute whose 95th percentile, failed requests counted over, was over the line: a minute over the line wakes a person. In the cloud the aim is no alert minute at all; one on Omni-Compass's side is found and fixed, never accepted. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `CLAUDE.md`.*
- **health.** The explicit operating requirements: correctness, service limits, resource bounds and every applicable hardware limit. *Source: `docs/FACTORY_PROFILE.md`.*
- **the bill of a route.** C(r, a) = Σₖ c(r, a, k), the sum of a route's cost components inside the declared boundary, and the saving S(r, a) = (C(r, native) − C(r, a)) / C(r, native); a component with no recorded price leaves the total unresolved. *Source: `docs/FACTORY_PROFILE.md`.*

### Arms and Placement

- **Omni-Compass.** A supervisory governor. It always sits on top of a native controller and never in its place: the Kubernetes pod autoscaler, GPU firmware, cooling, batteries, a grid's tap changer, a robot's servo. It treats each setting a native controller already exposes as a muscle and the whole stack as one body. Headline: more work, faster, on fewer machines, with less energy. *Source: `CLAUDE.md`.*
- **native.** The whole system by itself with everything it ships with: every muscle under its own native controller. Every benchmark's baseline, and the controller Omni-Compass always sits on top of. Amber on the page. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `CLAUDE.md`.*
- **Omni-Compass on native.** The same system with Omni-Compass on top of all of it, every native controller still running underneath. On Kubernetes, Omni-Compass on top of Kubernetes on top of the muscles. The arm every table carried as "omni", its machine key unchanged. Blue on the page. *Source: `CLAUDE.md`.*
- **the yardstick.** Kubernetes' published autoscaling rule, written by us from its documentation (a description of a rule, not Kubernetes' code): the native that Omni-Compass on native is read against in the real three-run test of section 2a, the Scorecard. *Source: `docs/OMNI_ORCHESTRATOR.md`.*
- **the three places Omni-Compass lives.** Omni-Compass sits at both ends of the cloud's wire and at every layer between: the software end (the cluster, Kubernetes, its add-ons, its governors and the services on it), the cloud between them (the machines it bills, metered) and the bare metal (the card, the chip, and the machine: the kernel, bare metal, Kepler). *Source: `tools/whole_system.py`.*
- **the cloud as the wire.** The cloud is the wire between the chip at one end and the software at the other, and makes no benefit of its own. Through the cloud the bare metal belongs to the provider (no tenant can read its meters or write its chips' limits), so a cloud run shows two things: that the engine holds on the cloud's machines as it does on site, and how much of the software end's gain comes through the wire, read as work per dollar beside the bill (the machines counted every fifteen seconds, the bill at list price): more work for the same money, never a smaller bill as the aim. Every cloud set runs the whole engine at the max from 31 October (the founder's order of that day struck the tune-down on the machines alone); the work and the speed are made on the software end and the bare-metal end. *Source: `tools/whole_system.py`; `DISCLOSURES.md`; `CLAUDE.md`.*
- **a governor's way.** The third arm in our models: a governor or orchestrator (the Kubernetes scheduler and its bin-packing profile, Kueue, Volcano, KAI, Koordinator, CruiseKube, Crane, KubeRay, Gödel, Armada, Karmada, Open Cluster Management, KubeEdge, Nephio) as the body of the catalog muscles that stand for its knobs, sitting on the organism's clock on the same injections; Omni-Compass on top of the governor governs both bodies. Read per muscle, like for like. Its knobs run under their own native controllers, so it reads native's work index by construction; the governors as their projects ship them run on real Kubernetes in section 4e (class L). *Source: `tools/injection_grid.py`.*
- **governing engine.** The executable mathematical rules that turn observations and internal state into governing decisions. *Source: `docs/FACTORY_PROFILE.md`.*
- **native baseline.** The system's documented configuration and behaviour with no Omni-Compass governing it: every muscle under its own native controller, as its vendor ships it. *Source: `docs/FACTORY_PROFILE.md`.*

### Compass Law and Plug

- **the compass.** The word for the band every reading is held in and for the whole mechanism drawn as one picture (the Omni-Compass rose). The law is omnicompass/compass_law.py (CompassLaw): a band with 5% cushions, two antagonist forces, smooth (tanh), not hammering. *Source: `CLAUDE.md`; `docs/book/THEORY.md`.*
- **the compass law.** One smooth law for every muscle: the service reading is placed as a position in its band, p = (r − lo)/(hi − lo) (0 calm, 1 the service line), and the force is F = A·tanh((k[p]·(p − centre) + k[d]·v)/A). It fails up past the 0.95 wall; a positive force adds capacity, power, cooling or speed, a negative force takes it back. *Source: `omnicompass/compass_law.py`.*
- **the band.** A reading's safe range, from calm (p = 0) through its centre (p = 0.5) to its line (p = 1); the walls run to 0.05 and 0.95, and the last 5% on each side is cushion (10% in all) before the line. Where a reading sits in it is its compass position. *Source: `omnicompass/compass_law.py`.*
- **the cushion.** The last 5% of the band on each side before the line; from 1 − cushion the force is the whole authority A, so a muscle is never let past the line. In the max the cushion moves with each muscle's own risk (the edge). *Source: `omnicompass/compass_law.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the centre.** The bottom of the compass, 0.5 by default, where the two forces balance: below it the force pulls capacity back, above it pushes capacity in. *Source: `omnicompass/compass_law.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the two antagonist forces.** Up: a positive force adds capacity, power, cooling or speed (scale out, raise a clock, start a chiller). Down: a negative force takes it back (scale in, lower a limit, warm a setpoint). Each side has its own gain, because adding and taking back do not cost the same. *Source: `omnicompass/compass_law.py`.*
- **k[p].** The spring: the pull k[p] × (position − centre), gentle near the bottom, harder up the walls. *Source: `omnicompass/compass_law.py`.*
- **k[d].** The damping: k[d] × velocity meets whatever is shoving the position (a load rising, heat building) with an equal and opposite push. Chosen for critical damping, k[d] = max(0, 2√(k[p]·τ/dt) − 1)·dt, the reading glides to the centre and stops, no overshoot, no ringing. Some wires set it at three times that, so a rising load is met before it reaches the wall (the Kubernetes governor, the GPU governors, the realms' arms and the grid's runner); the data stores' runners, the orchestrator's brain and the other simulators keep the class's critical damping. The page's section 5h lists every wire, read from the repository at each build. *Source: `omnicompass/compass_law.py`; `omni_controller/controller.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **A.** The authority: the force's ceiling. The force is A × tanh(raw / A), a spring near the centre that bends over and flattens into its maximum A, never a corner, never a hammer. *Source: `omnicompass/compass_law.py`.*
- **tanh.** The hyperbolic tangent the force is passed through so that it is smooth and never hammers: the same shape the engine already uses for v_eff (omnicompass/core.py). *Source: `omnicompass/compass_law.py`.*
- **fail up.** Past the 0.95 wall the up side goes to its full force at once, and the down side may not act until the position is back inside the compass. *Source: `omnicompass/compass_law.py`.*
- **the two-way plug.** A muscle is a plug with one wire in and one wire out: it reads its meters and writes its lever, clips each write to the cover, reads back what the device took, restores the snapshot at the end, and stops writing if it finds the lever at a value the brain did not write (one writer). All the thinking is in the brain, written once for every muscle. *Source: `omnicompass/compass_law.py`; `CLAUDE.md`.*
- **the snapshot.** The lever's value read once, before the first write; restore puts the lever back to it, and it never moves after that. Reset hands everything back to it. *Source: `omnicompass/compass_law.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the cover.** The outer band: the lever's hard range (the device's or the buyer's lowest and highest setting). Every write is clipped to it, so nothing the math does can set the lever outside. *Source: `omnicompass/compass_law.py`.*

### Brain and Nervous System

- **the four pieces.** The engine is built in four pieces, each feeding the next. In the software they are the engine's state equations (piece 1: deviation, alignment, memory and basin), the basin potential and its flow (piece 2), the bath that absorbs and redistributes (piece 3), and the one governor that couples every muscle to one law with no outside authority (piece 4). The mechanism panel turns each piece's constants live. *Source: `docs/book/THEORY.md`.*
- **piece 1, the state and the basin.** Energy E (dE/dt = −α_E E + β_int + β_ext + v_eff: how fast stress energy drains), unity U on a double well with two basins at U = ±1 (dU/dt = μU(1 − U²) − (dE/dt)/E_max − λ_U U + u), and its integral I[U], the remembered shortfall (dI_U/dt = (1 − U) − σ₁E − δS − λ_I I_U). The command u = −U̇ + K[P]·(1 − U), bounded by U[auth], brings unity back to its basin at U = 1. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `omnicompass/core.py`.*
- **piece 2, the basin's potential and flow.** dS/dt = δ − α_s S − ¾β_s S² = −Φ′(S), with Φ(S) = α_s S²/2 + β_s S³/4 − δS: the basin state S rolls down its potential Φ(S) to a stable bottom, S*, the root of dS/dt = 0. *Source: `omnicompass/core.py`; `docs/book/THEORY.md`.*
- **piece 3, the bath.** A damped oscillator driven by the flow: dB/dt = Ḃ, dḂ/dt = γ_c δS − (ω_B/Q_B)Ḃ − ω_B² B; its beat enters energy through v_eff = cos(ω_B t/2)·c·tanh(λ₀ + λ₁(U − ½) + λ₂S). In the theory, the bath that absorbs and redistributes. *Source: `omnicompass/core.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **piece 4, the governor's law.** The governor's law (omnicompass/adapter.py, nervous_system.py): push and the utilisation target ρ* from the state, and the nerves' grants to every organ: one law for every muscle, with no outside authority. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `docs/book/THEORY.md`.*
- **RK4.** The fourth-order Runge–Kutta step that integrates the engine's six states (E, U, I_U, S, B, Ḃ): ten micro steps over 0.1·k of the engine's time a decision, k = the decision's period over 60 s (omni-v16's period rule; 0.01 each at one decision a minute); 20 macro steps of 10 micro steps in the core's Monte Carlo, the bounded command held across the four stages. *Source: `omnicompass/core.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `tools/core_runs.py`.*
- **push.** The command the brain asks for to bring unity back to its basin, as a share of its authority: push = clip(−f_U + 12(1 − U), ±25)/25. A push above κ's knee holds every give-back. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **ρ*.** The engine's utilisation target: how full a muscle may run after a give-back, ρ* = clamp(ρ₀ − k_I I_U − k_E E, ρ_min, ρ₀); the live controller reads it clamped to 0.5 to 0.95. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `realms/plants.py`.*
- **κ.** Convergence, the first of the nerves' four scalars: κ = 1 while push ≤ push_release, else push_release / push. The further the engine is from its basin, the less it may give back. *Source: `omnicompass/nervous_system.py`.*
- **h.** Basin health: h = clamp((U − U_gate)/(1 − U_gate), 0, 1). *Source: `omnicompass/nervous_system.py`.*
- **σ.** The stress ratio σ = S/S*, where S* solves δ − α_s S − ¾β_s S² = 0; above 1 it holds every give-back. (On the console σ also names the noise knob's spread, 1 + σ·z.) *Source: `omnicompass/nervous_system.py`.*
- **ν.** Unmet need: ν = max(0, I_U). *Source: `omnicompass/nervous_system.py`.*
- **calm.** The nerves' one number, calm = κ·h·(1 − (σ − 1)⁺)·(1 − min(ν, 1)), in [0, 1]; 1 means fully settled. An organ may hand capacity back only while calm ≥ its threshold θ, the line is clean and every sense is live; continuous organs shed at most the calm share of their surplus a decision. *Source: `omnicompass/nervous_system.py`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **the organs and their grants.** The organ families the nerves grant authority to: pods, nodes, cpufreq, gpu, power, batch, routing and rollback. Expanding is always allowed except during a security hold; contracting (giving capacity back) only when calm ≥ the organ's reversibility threshold θ (pods 0.5; nodes 0.7, since a node costs a boot to reverse; cpufreq, gpu and power 0.3; routing 0.5) and the service is clean. *Source: `omnicompass/nervous_system.py`.*
- **the nervous system.** One evolving engine state granting authority to every organ family. Omni-Compass does not replace the specialist controllers (the HPA and VPA size pods, the Cluster Autoscaler and Karpenter size node pools, Linux schedutil picks CPU frequency, NVIDIA DCGM manages GPUs); the nervous system decides, from one shared state, the envelope inside which each of them may act. *Source: `omnicompass/nervous_system.py`.*
- **the immune system.** Omni-Compass's own: native twins of every room and pool, the heat debt, the cure on the spot, the pools' give-back and the bone's grant (V6 to V13). Reactive and proactive: it answers a breach at once, and it acts before a line is crossed. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `DISCLOSURES.md`.*
- **the heat debt.** The body's power that would carry, over one decision, the heat by which the rooms that cannot cure themselves stand warmer than their twins. The pools hand it back (the other muscles kick in): the max's added machines go back until no such room is warmer than native's. *Source: `realms/compass_arm_v5.py`.*
- **the twin.** The brain's model of native: what the operator's own autoscaler would have had with no cap, on the same arrivals and the same rules (the HPA's tolerance, its scale-down window, the machines' start time); every room wired by its setpoint has one too, under its operator's setpoint and native's heat. The max never leaves a pool with fewer machines than its twin, nor a room warmer. *Source: `realms/compass_arm_v5.py`.*
- **the bone.** The body's skeleton for the max: the lines every muscle stands on (a site's grid line, a room's cooling), loaded by the whole body. What the max adds is granted only out of the room the most loaded line has left, read one decision ahead; with no room, the machines this brain added go back at once, never below the pool's twin. *Source: `realms/compass_arm_v5.py`.*
- **the edge.** The compass's balance point is not a fixed middle: it moves with each muscle's own risk, at 1 − cushion, cushion = climb × reaction + z × wobble (z = 3.09: 99.9% of steps inside the cushion), widened at once when the need rises and narrowed slowly when it falls, as a driver doubles the following distance the moment rain starts. *Source: `omnicompass/edge.py`.*
- **the reflex rule.** A new setting is earned by a trial on the muscle itself, read from the muscle's own reaction: the urge proposes, the reaction disposes. A trial runs to its full measurement and is never ended by the calm it causes; one trial at a time inside a body; nothing permanent; the wall belongs to the body. *Source: `docs/book/THEORY.md`.*
- **the release gate.** Giving a unit back only when nothing is waiting and, after the release, the rest runs at or under the engine's utilisation target. *Source: `realms/plants.py`.*
- **defensive system.** Constraint enforcement, fault detection, containment, recovery and restoration: the bone and the twins, the lease's walk back, the kill switch. *Source: `docs/FACTORY_PROFILE.md`.*

### Controls and Tuning

- **the max.** The default brain: every muscle runs at its own limit, never past it and never below native; it rides the edge, not the middle. The energy it takes is power given, shown beside the work, the speed and the wear it bought, never called a loss. *Source: `CLAUDE.md`.*
- **the tune-down.** The dial's other setting (V5SAVE): never more than native, capacity handed back only with the organ's grant and the release gate: the same work with less. Every cloud set runs at the tune-down. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `CLAUDE.md`.*
- **the dial.** The choice between the max (every muscle to its own limit, never below native; the default) and the tune-down (never more than native). Anyone can tune Omni-Compass down from the max. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `CLAUDE.md`.*
- **one pedal.** Like an electric car, one pedal: push for more, lift off for less; lifting hands the setting back toward native; idle is the pedal lifted all the way; reset hands everything back to native. *Source: `CLAUDE.md`.*
- **lift-off.** Lifting the pedal: a force below zero moves the setting toward native's by min(1, base + slope·|F|) a decision. Under the max, lifting off toward native never needs the nerves' grant; going below native does. *Source: `CLAUDE.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **cruise.** One of the pedal's states beside idle and reset, with autopilot, watching and off: cruise is for a known queue waiting. The Kubernetes governor's cruise wait is never fewer than two readings (omni-v17). *Source: `CLAUDE.md`.*
- **the lease.** The governor's proof of life, renewed every decision. If a governor dies without handing back (killed outright, the machine crashed, it hung), the watchdog finds any governor whose process is gone or whose lease is older than its limit and walks every setting back to native, gradually (in the models over 24 decisions). *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `omnicompass/master.py`; `realms/harness.py`.*
- **the kill switch.** The master switch, for security only and instant: one switch in a human hand turns Omni-Compass's governing off everywhere at once. At its next decision every governor puts every setting it ever wrote back to the value it read before its first write, reads each one back, writes its last audit line and exits. Separate from the lease's gradual walk back after a crash. *Source: `omnicompass/master.py`.*
- **the heartbeat.** The governor's full decision, one turn of its loop: read, decide, write, renew the lease. The main engine takes it every 20 s from omni-v24 (60 s from omni-v17 to omni-v23); the controller takes any beat from 5 to 120 s (--interval), and the page offers 10, 15, 20, 30, 60, 90 and 120 s, each shown beside native with what it buys and what it costs. *Source: `docs/FACTORY_PROFILE.md`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **the fast checks.** The governor's checks between its beats, every 5 s at every beat: the scheduling floor, the pod reflex, and the conveyance every 15 s. Native's pod autoscaler checks every 15 s. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `CLAUDE.md`.*
- **the conveyance.** Moving a conserved budget between organs (site watts, cluster cores): moved, never created, down the gradient of need. On Kubernetes the governor raises a running pod's processor limit in place to the room its machine can still give under 75% busy, bounded by the namespace's quota, and hands every limit back to the operator's on a shared host at its top: the unit answers at its machine's speed, not its paper quota's, with no unit and no machine added. *Source: `docs/CONVEYANCE_LAW.md`; `docs/OMNI_ORCHESTRATOR.md`; `CLAUDE.md`.*
- **the factory tune.** The engine as The Omni-Compass LLC tuned and ships it, every muscle on the setting found for it (its own card where one was kept, the engine's own setting otherwise). Every published benchmark result is one engine at its one factory tune; a changed tune's results are the tuner's own. One button returns every knob to it. *Source: `DISCLOSURES.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the live tuning engine.** The live benchmark engine page and its control panel: every knob, button and monitor turns in real time to show the mechanism of action with native alone, with Omni-Compass on top, or both; what it shows at any other setting is the engine's range, never a benchmark result. *Source: `DISCLOSURES.md`.*
- **the heartbeat's seven buttons.** On the page the governor's full decision comes at one of seven beats, 10, 15, 20, 30, 60, 90 or 120 s; 10 s shows a beat below the 15 s standard. The factory's beat is the engine's own: 20 s from omni-v24 (the founder's order of 31 October), 60 s from omni-v17 to omni-v23. The page's live model steps every 15 s, so at 10 s two full decisions land in every other step, both on that step's reading, and at 20 s one full decision lands in three steps of four. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `docs/FACTORY_PROFILE.md`.*
- **factory profile.** The complete, versioned set of Omni-Compass default settings shipped together: the governing rules, gains, margins, decision interval and every other default. Selected after the mechanisms are verified, candidates are tested together and the choice is validated on fresh workloads; frozen at release, while the engine's state, commands and allocations go on responding. Today's is omni-v19's; the best validated factory profile is not yet established. *Source: `docs/FACTORY_PROFILE.md`.*
- **candidate profile.** A proposed combination of settings under evaluation; on the page, the best beat of a sweep with the factory's other knobs ("Try the candidate"). It becomes a factory profile only after validation and a new release. *Source: `docs/FACTORY_PROFILE.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **active profile.** The settings actually governing the current run, named on the page as factory, candidate or custom with its fingerprint. *Source: `docs/FACTORY_PROFILE.md`.*
- **custom profile.** An identifiable configuration that differs from the released factory profile; its fingerprint names it and its results are its own. *Source: `docs/FACTORY_PROFILE.md`.*
- **Restore factory profile.** The control that reapplies the released Omni-Compass configuration: every knob of the mechanism and the heartbeat back to the factory's, Omni-Compass still on. *Source: `docs/FACTORY_PROFILE.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **Return to native.** The control that hands governance back and restores the recorded native settings, as the adapter supports. *Source: `docs/FACTORY_PROFILE.md`.*
- **governor request.** The row under the fuse box's master switches: after every press, the request a running governor takes for it through its control panel (tools/omni_control.py), with its role; the page sends nothing. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **Commands.** The fuse box's tab that lists every control beside the request a running governor takes for it and its role; the mechanism's knobs and the plant's conditions have none. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*

### Proof and Evidence

- **the verdict.** Omni-Compass moves a knob only where it measures that the muscle loses nothing by it. The trial step is read as a report reads a row: the 95% interval of its change in cost, on the logarithm of each piece of work's cost. Wholly above zero is a LOSS: refused and undone. A GAIN or a STEADY step is kept only within the 2% allowance. The 2% verdict is the engine's trigger, not a stamp on a report. *Source: `omnicompass/verdict.py`; `CLAUDE.md`.*
- **the give-back trial.** Every give-back is tried in its own paired trial, while the service is calm: the muscle with and without it, under the same load (the knob at native first, the reference, then one step past the deepest step already allowed), and undone if the muscle loses by it. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `omnicompass/verdict.py`.*
- **the model gate.** Every change to the engine or a live controller runs first in our own models (class S), against the engine that stands, on the same seeds, before any real run is started. A change goes on to real runs only where it reads no LOSS there and shows promise; a LOSS there is root-caused and fixed in the model. *Source: `tools/model_gate.py`.*
- **the fingerprint and its digest.** Every engine version fingerprinted file by file: one SHA-256 per file and one over the sorted list, its digest. A result belongs to a version only if the commit it ran on carries exactly that version's bytes; no result is read across versions. *Source: `tools/omni_version.py`.*
- **the seal.** Every law that exists in Python and in C++, locked together: results/SEAL.json records each twin's Python and C++ files and the parity test that proved them equal, so a change to either side breaks the seal until its parity test passes again. *Source: `tools/seal.py`.*
- **the C++ twin.** The engine's laws written again in C++ (the core, the governor, the compass law, the verdict), each held equal to its Python by a parity test under the seal; the Python's runs fed through the C++ engine give the same digest. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `tools/seal.py`.*
- **evidence classes P, L, S.** The class every number carries: P a physical meter (a real card's own power meter), L live software (real Kubernetes on GitHub's machines), S our own models (modelled). A model is a statement about the model; only a meter speaks for hardware. S is never presented as proof. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `DISCLOSURES.md`.*
- **modelled.** The word for our own models (class S) in every report; live software is the real thing (class L); a meter is class P. *Source: `CLAUDE.md`.*
- **three runs A, B and C.** Each benchmark runs three times as separate GitHub runs, A, B and C, on the same frozen engine. "GAIN in all three of our runs" means A, B and C moved the same way with every 95% interval clear of zero; otherwise a change of 0.5% or more reads by the mean of our three runs, with the count of runs beyond the noise. Run and scored by The Omni-Compass LLC's own code; no outside party has reviewed or approved these results. *Source: `tools/readings.py`; `tools/confirm_abc.py`.*
- **the 95% interval on Student's t.** Every interval is the two-sided 95% point of Student's t for its degrees of freedom, computed (no table) by bisection on the distribution's own CDF and rounded to three decimals as the printed tables are. *Source: `omnicompass/student_t.py`.*
- **Monte Carlo.** The Python's Monte Carlo of the engine's core: N runs from the jump generator, each through the six states and the RK4 step, controlled, uncontrolled (native), aimed at the wrong basin and with the double well's μ at 0; a run is conveyed when its U has stayed in one basin for 5 macro steps in a row and certified at 10. One digest, and the live benchmark engine's own port and the C++ twin held to it. Class S. *Source: `tools/core_runs.py`.*
- **the jump generator.** The seed of run k: seed_k = base + k·0x9E3779B9, mod 2³², feeding a mulberry32 stream (the page's own generator), so the Python, the C++ and the page draw the same runs and prove each other receipt by receipt. *Source: `tools/engine_runs.py`.*
- **the engine that stands.** The engine version on main, named on the page's title block and printed by python3 tools/omni_version.py (this glossary's engine field names it); every benchmark runs again on it. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **harness.** The machinery that supplies workloads, executes comparisons, checks requirements and records results. *Source: `docs/FACTORY_PROFILE.md`.*

### Runs and Grid

- **the injection.** One seed of the Python's batch, seed_k = base + k·0x9E3779B9 mod 2³² (the jump generator): every plant of every organism draws its demand noise, its weather and its disturbances from it, under the climb, for 240 decisions of 15 s. The same injection reaches every organism and every way, native, Omni-Compass on native, each governor on the organism and Omni-Compass on top of each governor, so each one's reaction to the same thing is read side by side. *Source: `tools/injection_grid.py`.*
- **the injection batch.** One set of the Python's 500 injections, named by its base and by the SHA-256 digest of the Python's runs of it; the C++ engine runs the same seeds and must give the same digest (section 5a). Every cell of the injection grid is drawn from one batch; another batch is another run in the key's sense, and three batches make a three-run reading. *Source: `tools/injection_grid.py`.*
- **the injection grid.** Every organism with a plant, each native and with Omni-Compass on native, and each of the fourteen governors sitting on it, on one injection batch, at 1, 10, 100 and 500 runs × 1, 10, 100 and 500 organisms stacked (section 5c). Run k of a cell stacks M copies, copy c on injection k + c (mod 500); each cell is read by the key over its N runs. The page re-hashes the record and recomputes every cell's mean from the runs' means. Class S. *Source: `tools/injection_grid.py`.*
- **organisms stacked.** In the injection grid, M copies of one organism run side by side on one clock, each on its own injection: separate clusters sharing no power line or room, every gauge the mean of the copies' per muscle. The scale grid of section 5e stacks its copies in one body instead. *Source: `tools/injection_grid.py`.*
- **a cell's reference.** IG/base/organism/way|against/NxM/gauge: the name of one cell of the injection grid (for example IG/1488855732/tower/on_native|native/500x1/work), printed under the cell, copied by its button and typed back into the reference box to reach the same cell on any copy of the page that holds that batch. *Source: `tools/injection_grid.py`.*
- **the line.** The limit a reading must not cross: a response time, a temperature, a feed's rating. Over the line, work is waiting or failing. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the climb.** A load stepping by one, up and down (1 2 3 2 3 4 …): level 4 is the organism's own load and level 8 twice it, so the organism is pushed past what native can carry and the most each arm can do shows. *Source: `realms/harness.py`.*
- **work waiting in line.** The third load: work already waiting when the run starts, a quarter of the work the run itself brings, so the arm that clears it sooner is faster. *Source: `realms/harness.py`; `tools/run_realms_v5.py`.*
- **the grid.** Each organism native and with Omni-Compass at 1, 10 and 100 copies × 1, 10 and 100 paired runs, modelled and with the real cluster inside, both values in every square; the 1,000 tier on GitHub's own machines only; paid cloud and GPU runs stay at 1, 10 and 100 copies with at most 100 repetitions. Copies is the size of the body one brain governs; runs is the number of independent paired trials. *Source: `CLAUDE.md`; `docs/book/THEORY.md`.*
- **protocol 4.** With the cluster inside, only runs of protocol 4 count: the governor never below the organism's CPU priority, its decisions counted inside the window; the model of the organism on the runner's last core and the kind nodes on the others, the same in both arms; the served image pulled onto every worker before each arm. *Source: `CLAUDE.md`.*
- **the conductor.** The program that starts the runs (scripts/dispatch_grid.py, every 15 minutes): it starts every run not yet started, reads started runs back from their names, never starts one twice, and keeps the queue at what GitHub runs plus a margin; it also releases every benchmark's reruns on the engine that stands and the cloud sets. *Source: `CLAUDE.md`.*
- **Omni index.** One number for more for the same, or the same for less: every measure of every test turned into a ratio oriented so that above 1 is a GAIN (work, speed, machines, energy or the bill); a test's index is the geometric mean of its ratios, minus one, in percent; the headline is the geometric mean of the real categories, each weighted the same. The modelled muscles are shown beside it, never inside it. *Source: `tools/omni_index.py`.*

### Catalog and Organisms

- **the organism.** A set of muscles stepped together on one clock, each muscle from its own plant model with its own native controller, the whole fed one demand from one seed, so that the heat the machines make is load on the rooms, the body's power swing is load on every site's line, and one brain judges every step against every other muscle's cushion. *Source: `docs/book/THEORY.md`.*
- **muscle.** One setting on one machine that already has its own control: a replica target, a node pool's size, a GPU's clock ceiling, a chiller's setpoint, a battery's reserve, a joint's effort. Omni-Compass may hold that knob and only that one; the native controller keeps the rest. The muscle's name is the setting's own name on its controller. *Source: `docs/MUSCLE_CATALOG.md`; `realms/plants.py`.*
- **realm.** One of the four trades the catalog is cut into: Compute / AI / Cloud; Physics / Robotics / Autonomous; Energy / Facility / Industrial; Distribution / Specialized. A muscle sits in one realm, or, as a spine muscle, in all four; each realm's organism is its own families on the spine. *Source: `docs/REALMS.md`.*
- **family.** A group of muscles on one kind of machine with one native controller and one wiring recipe; 70 in the catalog. docs/wiring_recipes.csv gives each family's native controller, wire out, wire in, restore, and whether that wire has run live. *Source: `docs/MUSCLE_CATALOG.md`.*
- **template.** The plant model a muscle is modelled on, one of five (realms/plants.py): compute_pool, thermal_zone, energy_storage, motion_axis and process_loop. Each carries its own native controller and runs correctly with no Omni at all. *Source: `realms/plants.py`.*
- **knob.** Which of four kinds of setting a muscle is: capacity (how much of the machine is in service), admission (what is let in), power (the power share or limit the machine may draw) or setpoint (the target the machine's own loop holds). *Source: `docs/MUSCLE_CATALOG.md`.*
- **preset.** The parameter set of a muscle's plant, one per class of machine (server, node, gpu, data_hall, microgrid, robot_joint and the rest): round engineering figures for the class of machine, not measurements of any product. The class also decides how such a muscle is reached in a real stack. *Source: `realms/presets.py`.*
- **the spine.** The muscles every real stack runs on: the 267 of the catalog whose realm list names all four realms, in 13 families (scheduling, placement, processors and memory, network, storage, observability, security, power and cooling). An organism in its own right, the seventh: the base every stack runs on, as an operating system is the base of every program. *Source: `docs/THE_SPINE.md`.*
- **the stack.** The four realms stacked on one clock, every duplicate of the spine kept: 1,908 muscles, the spine once in each realm's body. *Source: `CLAUDE.md`.*
- **the tower.** The whole catalog as one body, every muscle once: 1,107 distinct muscles in 70 families. *Source: `CLAUDE.md`.*
- **the orchestra.** The eighth organism: every catalog muscle that stands for a knob of the fourteen governors and orchestrators (the Kubernetes scheduler, Kueue, Volcano, the KAI scheduler, Koordinator, CruiseKube, Crane, KubeRay, Gödel, Armada, Karmada, Open Cluster Management, KubeEdge, Nephio), each governor's muscles a body of its own and all together one body, native and with Omni-Compass on top, modelled. *Source: `tools/run_orchestra.py`.*
- **the seven organisms.** The spine, the four realms, the four stacked and the whole tower: each run native and with Omni-Compass on top of native on the same seed, the same load and the same clock. *Source: `docs/book/THEORY.md`.*
- **the stress-test model.** A model drawn for the page so the body can be stressed by hand (a surge, a blind sense, a security hold, the kill switch), class S: sixty muscles named from the catalog, each a capacity lever with its own response time and sensing delay under an HPA-style native controller, run native and Omni-Compass side by side on the same demand. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*

### Page and Monitors

- **the benefit board.** Every benchmark's measured effect in one board, native against Omni-Compass on top of native, by domain and by gauge family, with the Omni index that weighs them together; every bar is its table's own word (GAIN green, STEADY yellow, LOSS red, power given blue) beside its size. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the traffic signal.** Every monitor's light, read on its band: green GAINING, low in its band with room to climb; yellow STEADY, inside its band; red REDLINING, at the top of its band and holding there, blinking red and black; red OVER THE LINE, past its band, blinking red and white; grey, and said so, where there is no line. On a record the colour is the reading's word: GAIN green, STEADY yellow, LOSS red. A needle that falls is not a LOSS and one that rises is not a GAIN: each light reads what its gauge is for. The light moves with its monitor: it reads the series the monitor draws. Every signal shows all four live words, the lit one bright and the rest dim, on native's side and on Omni-Compass's side alike: Omni-Compass's redline reflex is built never to let a muscle redline, and the red is still wired, so that if one does (a fault, a bug) it is seen at once, and the kill switch hands everything back to native in the same instant. The engine that stands carries the rule in its immune system, knob by knob, landed on 25 October (omnicompass/immune.py and its C++ twin cpp/src/immune.cpp): over its line three decisions, stuck, and native's twin lower by more than 5%, the knob is handed to native for 10 decisions, doubling up to 160; where native is not stronger Omni-Compass stays. The page's live model applies the same rule, with the engine's own numbers, to every muscle it draws. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **GAINING.** Green on the traffic signal: low in its band with room to climb, or Omni-Compass ahead of native now (a GAIN). *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **REDLINING.** Red on the traffic signal, blinking red and black: at the top of its band and holding there, or Omni-Compass behind native now (a LOSS). Red means LOSS and the alarm only, never native. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **OVER THE LINE.** Red on the traffic signal, blinking red and white: past the top of its band, the alarm. Omni-Compass's own law hands a muscle back toward native before its line (the fail-up at the band's 95% wall), so this light is what a line crossed looks like, on whichever side crossed it. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **AWAITING.** A dark light, never green: the run that fills this monitor has not landed yet, and the light stays dark until it does. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **native's colour.** Orange (#ff8a1f, the page's --steel): the word native and every line, bar, lane, tile and number that belongs to native's side wear it. Red is only a LOSS and the alarm. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **live tuning bench.** The interface that operates the engine's controls and displays their effects through the connected backend: the live benchmark engine's main control panel. *Source: `docs/FACTORY_PROFILE.md`.*
- **observer.** A tool that stores readings and draws them and raises an alert when a line is crossed; a person decides. Prometheus, Grafana, Datadog and the like. Omni-Compass's exporter serves its readings to any of them. *Source: `docs/FACTORY_PROFILE.md`.*
- **collector.** A tool that gathers metrics, logs, traces and profiles and forwards them, deciding nothing: Grafana Alloy, the OpenTelemetry Collector, node_exporter, Kepler. *Source: `docs/FACTORY_PROFILE.md`.*
- **console.** One screen to deploy, scale, restart and set rules across clusters, where a person decides: Rancher, Portainer, Lens, the OpenShift console. The rules set there are the native Omni-Compass sits on top of. *Source: `docs/FACTORY_PROFILE.md`.*
- **automatic optimizer.** A product that watches one layer and changes its settings itself, mostly for a cloud bill: the comparable, benchmarked as native with it and then with Omni-Compass on top. *Source: `docs/FACTORY_PROFILE.md`.*
- **supervisory governor.** What Omni-Compass is: it reads the whole body every beat, decides with one law across every muscle, writes through a two-way plug, reads each write back, audits, hands back gradually and stops at the kill switch, on top of every native controller. *Source: `docs/FACTORY_PROFILE.md`.*
- **the dashboards.** The page's section 3i: the live benchmark engine in nine forms an operations team reads (a board of panels, a host map, a graph, an event stream, a cluster console, a one-line diagram, a wall of numbers, the cost by body part, and Omni-Compass's own two-way pipeline), by muscle, body part or the whole organism. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **contract, this decision.** The decision on screen in the symbols of the factory profile's mathematics: k, Δ, θ, the settings requested u[req](k), commanded u[cmd](k) = Π[C](u[req](k)) and acknowledged u[ack](k) = R(u[cmd](k)), computed on the live model. *Source: `docs/FACTORY_PROFILE.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **Prometheus Metrics.** The fuse box's tab that prints the live model in Prometheus's text exposition format, with the series a running system serves beside each one and the PromQL the Grafana wall draws it with. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **the monitor wall stack.** deploy/wall: Prometheus, Grafana with the Omni-Compass wall loaded, Alertmanager with the governor's alert rules, node_exporter and the governor's exporter, in one command; it reads and writes nothing. *Source: `deploy/wall/README.md`.*
- **actuation feedback.** Each decision's requested settings, those that landed as asked, those held at a muscle's limit, and those still moving toward their setting; requested, commanded and acknowledged settings are kept distinct. *Source: `docs/FACTORY_PROFILE.md`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **Omni-Compass's blue.** Blue (#4e97d1, the page's --brass and --omni): Omni-Compass's side and its name; on a reading, blue always means power given. While the master switch is OFF, Omni-Compass's side follows native in a lighter tint of native's own colour. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`; `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*
- **a changed tune's violet.** Violet (#c77dff, the page's --tuned): a knob or a profile turned from the factory tune; never a side and never a reading's colour. *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **Mechanism Knobs.** The engine's own knobs, live: the four pieces of the brain, the compass law, Omni-Compass's hand on each muscle (the max's push and lift-off, the tune-down's floor, step and dwell), native's own controller (its target, tolerance, step and window) and every muscle's scale out, scale in, scale up, response time and sensing delay. They turn the engine's own equations while it runs, on both governed arms; a knob turned from the factory turns violet, ↺ puts it back, and the factory button puts every one back. A tune other than the factory's is a variation of the mechanism (class S). *Source: `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*
- **Variation Switchboard.** One set of knobs that sets the arm, the organism, the copies, the runs, the run letter and the beat on every monitor that carries that variation, and names the ones that do not. *Source: `CLAUDE.md`.*
- **the monitor wall.** Every monitor of the page in one view (section 0), numbered 1 upward in five blocks of about twelve, each its own subject (Benefit and Organism; Real Runs on GitHub; Brain and Mechanism; Clouds, Chips, Orchestrators and Scale; Proof and Telemetry), read left to right; every canvas the page draws is one monitor, its small copy on the wall a tile. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `docs/engine/monitors.json`.*
- **golden signals.** Latency, traffic, errors and saturation: on the wall, the work waiting, the work done, the decisions past their line and the capacity held. *Source: `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`.*

## 2. The arms

| Arm | Colour | What it is | Source |
|---|---|---|---|
| **native** | orange (#ff8a1f) | The whole system by itself with everything it ships with: every muscle under its own native controller (the Kubernetes pod autoscaler, the GPU's firmware, the cooling, the batteries, a grid's tap changer, a robot's servo). In the models, the plant and its native controller alone. | `docs/OMNI_COMPASS_LIVE_ENGINE_MANUAL.md`; `realms/harness.py` |
| **Omni-Compass on native** | blue (#4e97d1) | The same system with Omni-Compass on top of all of it: every native controller still running underneath, Omni-Compass setting only the knobs those controllers already expose. On Kubernetes, Omni-Compass on top of Kubernetes on top of the muscles. The arm every table carried as "omni", its machine key unchanged. | `CLAUDE.md` |

## 3. The organisms

### Spine (267 muscles)

The 267 muscles every real stack runs on, every one in all four realms: the computers' scheduling, placement, processors and memory, network, storage, observability, security, power and cooling, 13 families. An organism in its own right, the seventh, run native and with Omni-Compass on top of native like the other six: the base every stack runs on, as an operating system is the base of every program. Each spine muscle is also part of every realm's organism, counted once in the tower and four times in the stack.

Families: Kubernetes Workload Scaling (32); Host CPU & Memory (26); Container Resources (25); Node Fleet & Karpenter-Class Control (24); GPU Hardware (22); Kubernetes Placement & Scheduling (21); Cloud VM & Capacity (21); Storage Block/File/Object (20); Network Routing & Switching (19); PDU, UPS & Electrical Distribution (18); Cooling, Chillers & Thermodynamics (18); Reliability, Security & Recovery (12); Observability & Telemetry (9).

*Source: `docs/THE_SPINE.md`; `docs/MUSCLE_CATALOG.md`.*

### Compute / AI / Cloud (540 muscles)

Every muscle whose realm list includes Compute / AI / Cloud, the spine among them: its own 273 muscles in 20 families of its trade (the largest: AI Inference Serving, Linux Kernel & OS Control, Work Admission & Demand Shaping, HPC & Distributed Compute) on the spine's 267, 540 in all, one organism on one clock, run native and with Omni-Compass on top of native.

Families: Kubernetes Workload Scaling (32); Host CPU & Memory (26); Container Resources (25); Node Fleet & Karpenter-Class Control (24); AI Inference Serving (24); GPU Hardware (22); Kubernetes Placement & Scheduling (21); Cloud VM & Capacity (21); Storage Block/File/Object (20); Linux Kernel & OS Control (20); Work Admission & Demand Shaping (19); HPC & Distributed Compute (19); Network Routing & Switching (19); GPU Fabric & RDMA (18); AI Training (18); PDU, UPS & Electrical Distribution (18); Cooling, Chillers & Thermodynamics (18); Cross-Cluster, Multi-Region & Edge (18); Quantum Computing Control Simulation (16); Distributed Cluster Managers (15); Media Streaming & CDN (14); Reliability, Security & Recovery (12); Game Servers & Real-Time Interactive (12); DPU SmartNIC & Programmable IO (12); Blockchain & Ledger Nodes (10); CI/CD & Build Farms (10); OpenShift & Machine API (9); Observability & Telemetry (9); Serverless & Functions (FaaS) (9); Virtualization & Hypervisor (9); Gut: Data-plane Intake & Waste (8); Kubernetes Dynamic Device Allocation (8); Skin: Perimeter & Admission (5).

*Source: `docs/MUSCLE_CATALOG.md`; `docs/REALMS.md`.*

### Physics / Robotics / Autonomous (404 muscles)

Every muscle whose realm list includes Physics / Robotics / Autonomous, the spine among them: its own 137 muscles in 8 families of its trade (the largest: Aviation & Autonomous Flight, Robotics Motion Control, Robotics Fleet & Warehouse Automation, Spacecraft & Flight Software) on the spine's 267, 404 in all, one organism on one clock, run native and with Omni-Compass on top of native.

Families: Kubernetes Workload Scaling (32); Aviation & Autonomous Flight (28); Host CPU & Memory (26); Robotics Motion Control (26); Container Resources (25); Node Fleet & Karpenter-Class Control (24); GPU Hardware (22); Kubernetes Placement & Scheduling (21); Cloud VM & Capacity (21); Storage Block/File/Object (20); Network Routing & Switching (19); PDU, UPS & Electrical Distribution (18); Cooling, Chillers & Thermodynamics (18); Robotics Fleet & Warehouse Automation (17); Spacecraft & Flight Software (14); Rail Traction & Train Control (14); Automotive EV & Mobile Powertrain (14); Reliability, Security & Recovery (12); Marine Propulsion & Vessel Automation (12); Elevators & Vertical Transport (12); Observability & Telemetry (9).

*Source: `docs/MUSCLE_CATALOG.md`; `docs/REALMS.md`.*

### Energy / Facility / Industrial (480 muscles)

Every muscle whose realm list includes Energy / Facility / Industrial, the spine among them: its own 213 muscles in 15 families of its trade (the largest: Energy Storage & Microgrid, Industrial PLC & Process Automation, Facility & Grid Optimization, Building & Critical Environment HVAC) on the spine's 267, 480 in all, one organism on one clock, run native and with Omni-Compass on top of native.

Families: Kubernetes Workload Scaling (32); Host CPU & Memory (26); Container Resources (25); Node Fleet & Karpenter-Class Control (24); GPU Hardware (22); Kubernetes Placement & Scheduling (21); Cloud VM & Capacity (21); Storage Block/File/Object (20); Network Routing & Switching (19); Energy Storage & Microgrid (19); Industrial PLC & Process Automation (18); PDU, UPS & Electrical Distribution (18); Cooling, Chillers & Thermodynamics (18); Facility & Grid Optimization (15); Building & Critical Environment HVAC (15); Agriculture & Irrigation (14); Oil & Gas Pipelines (14); Mining & Mineral Processing (14); Power Generation & Turbine Control (14); Pharmaceutical & Food Manufacturing (14); Healthcare Critical Environments (13); District Heating & Cooling (13); Renewable Generation & Inverter Control (13); Semiconductor Fab & Precision Manufacturing (13); Reliability, Security & Recovery (12); Grid Transmission & Distribution (12); Water Wastewater & Pumping (12); Observability & Telemetry (9).

*Source: `docs/MUSCLE_CATALOG.md`; `docs/REALMS.md`.*

### Distribution / Specialized (484 muscles)

Every muscle whose realm list includes Distribution / Specialized, the spine among them: its own 217 muscles in 15 families of its trade (the largest: Messaging & Streaming, Runtime & Application, Database & Transactions, Service Mesh & API Reliability) on the spine's 267, 484 in all, one organism on one clock, run native and with Omni-Compass on top of native.

Families: Kubernetes Workload Scaling (32); Host CPU & Memory (26); Container Resources (25); Node Fleet & Karpenter-Class Control (24); GPU Hardware (22); Messaging & Streaming (22); Kubernetes Placement & Scheduling (21); Cloud VM & Capacity (21); Runtime & Application (21); Storage Block/File/Object (20); Network Routing & Switching (19); Database & Transactions (19); Reliability, Security & Recovery (18); PDU, UPS & Electrical Distribution (18); Cooling, Chillers & Thermodynamics (18); Service Mesh & API Reliability (16); Cache & Memory Services (16); Search, Indexing & Vector DB (16); Data Analytics & ETL (15); Commerce & Payment Systems (15); Workflow, Logistics & Fulfillment (15); Financial Markets & Trading Systems (14); Medical Imaging & Clinical Systems (12); Ports & Maritime Logistics (12); Telecom RAN & Edge Radio (12); Observability & Telemetry (9); Content Delivery & Edge Cache (6).

*Source: `docs/MUSCLE_CATALOG.md`; `docs/REALMS.md`.*

### Four Stacked (1,908 muscles)

The four realms stacked on one clock with every duplicate of the spine kept (1,908 muscles: the spine once in each realm's body). Each realm keeps its own body, so every muscle in the stack runs exactly the native it runs in its own realm, plant by plant.

Families: Kubernetes Workload Scaling (128); Host CPU & Memory (104); Container Resources (100); Node Fleet & Karpenter-Class Control (96); GPU Hardware (88); Kubernetes Placement & Scheduling (84); Cloud VM & Capacity (84); Storage Block/File/Object (80); Network Routing & Switching (76); PDU, UPS & Electrical Distribution (72); Cooling, Chillers & Thermodynamics (72); Reliability, Security & Recovery (54); Observability & Telemetry (36); Aviation & Autonomous Flight (28); Robotics Motion Control (26); AI Inference Serving (24); Messaging & Streaming (22); Runtime & Application (21); Linux Kernel & OS Control (20); Work Admission & Demand Shaping (19); HPC & Distributed Compute (19); Database & Transactions (19); Energy Storage & Microgrid (19); GPU Fabric & RDMA (18); AI Training (18); Industrial PLC & Process Automation (18); Cross-Cluster, Multi-Region & Edge (18); Robotics Fleet & Warehouse Automation (17); Service Mesh & API Reliability (16); Cache & Memory Services (16); Search, Indexing & Vector DB (16); Quantum Computing Control Simulation (16); Distributed Cluster Managers (15); Data Analytics & ETL (15); Commerce & Payment Systems (15); Workflow, Logistics & Fulfillment (15); Facility & Grid Optimization (15); Building & Critical Environment HVAC (15); Spacecraft & Flight Software (14); Agriculture & Irrigation (14); Oil & Gas Pipelines (14); Rail Traction & Train Control (14); Mining & Mineral Processing (14); Power Generation & Turbine Control (14); Pharmaceutical & Food Manufacturing (14); Financial Markets & Trading Systems (14); Media Streaming & CDN (14); Automotive EV & Mobile Powertrain (14); Healthcare Critical Environments (13); District Heating & Cooling (13); Renewable Generation & Inverter Control (13); Semiconductor Fab & Precision Manufacturing (13); Medical Imaging & Clinical Systems (12); Marine Propulsion & Vessel Automation (12); Ports & Maritime Logistics (12); Elevators & Vertical Transport (12); Game Servers & Real-Time Interactive (12); DPU SmartNIC & Programmable IO (12); Telecom RAN & Edge Radio (12); Grid Transmission & Distribution (12); Water Wastewater & Pumping (12); Blockchain & Ledger Nodes (10); CI/CD & Build Farms (10); OpenShift & Machine API (9); Serverless & Functions (FaaS) (9); Virtualization & Hypervisor (9); Gut: Data-plane Intake & Waste (8); Kubernetes Dynamic Device Allocation (8); Content Delivery & Edge Cache (6); Skin: Perimeter & Admission (5).

*Source: `tools/run_realms_v5.py`; `CLAUDE.md`.*

### Whole Tower (1,107 muscles)

The whole catalog as one body, every muscle once: 1,107 distinct muscles in 70 families, nine open-source pieces among them (Kepler, Climatik, EAR, CruiseKube, Goldilocks, the Kubernetes Power Manager, PEAKS, Adaptive GPU Power Capping, NVIDIA's platform power manager).

Families: Kubernetes Workload Scaling (32); Aviation & Autonomous Flight (28); Host CPU & Memory (26); Robotics Motion Control (26); Container Resources (25); Node Fleet & Karpenter-Class Control (24); AI Inference Serving (24); GPU Hardware (22); Messaging & Streaming (22); Kubernetes Placement & Scheduling (21); Cloud VM & Capacity (21); Runtime & Application (21); Storage Block/File/Object (20); Linux Kernel & OS Control (20); Work Admission & Demand Shaping (19); HPC & Distributed Compute (19); Network Routing & Switching (19); Database & Transactions (19); Energy Storage & Microgrid (19); GPU Fabric & RDMA (18); AI Training (18); Reliability, Security & Recovery (18); Industrial PLC & Process Automation (18); PDU, UPS & Electrical Distribution (18); Cooling, Chillers & Thermodynamics (18); Cross-Cluster, Multi-Region & Edge (18); Robotics Fleet & Warehouse Automation (17); Service Mesh & API Reliability (16); Cache & Memory Services (16); Search, Indexing & Vector DB (16); Quantum Computing Control Simulation (16); Distributed Cluster Managers (15); Data Analytics & ETL (15); Commerce & Payment Systems (15); Workflow, Logistics & Fulfillment (15); Facility & Grid Optimization (15); Building & Critical Environment HVAC (15); Spacecraft & Flight Software (14); Agriculture & Irrigation (14); Oil & Gas Pipelines (14); Rail Traction & Train Control (14); Mining & Mineral Processing (14); Power Generation & Turbine Control (14); Pharmaceutical & Food Manufacturing (14); Financial Markets & Trading Systems (14); Media Streaming & CDN (14); Automotive EV & Mobile Powertrain (14); Healthcare Critical Environments (13); District Heating & Cooling (13); Renewable Generation & Inverter Control (13); Semiconductor Fab & Precision Manufacturing (13); Medical Imaging & Clinical Systems (12); Marine Propulsion & Vessel Automation (12); Ports & Maritime Logistics (12); Elevators & Vertical Transport (12); Game Servers & Real-Time Interactive (12); DPU SmartNIC & Programmable IO (12); Telecom RAN & Edge Radio (12); Grid Transmission & Distribution (12); Water Wastewater & Pumping (12); Blockchain & Ledger Nodes (10); CI/CD & Build Farms (10); OpenShift & Machine API (9); Observability & Telemetry (9); Serverless & Functions (FaaS) (9); Virtualization & Hypervisor (9); Gut: Data-plane Intake & Waste (8); Kubernetes Dynamic Device Allocation (8); Content Delivery & Edge Cache (6); Skin: Perimeter & Admission (5).

*Source: `CLAUDE.md`; `tools/run_realms_v5.py`.*

### Orchestra Organism (55 muscles)

The eighth organism: every catalog muscle that stands for a knob of one of 14 governors and orchestrators (The Kubernetes scheduler (vanilla, and its bin-packing profile), Kueue, Volcano, KAI scheduler, Koordinator, CruiseKube, Crane, KubeRay, Gödel scheduler, Armada, Karmada, Open Cluster Management, KubeEdge, Nephio), each governor's muscles a body of its own and all of them together one body, 55 muscles, native and with Omni-Compass on top, modelled. The governors themselves run live on real Kubernetes, each as its project ships it with Omni-Compass on top.

Families: Kubernetes Placement & Scheduling (12); Distributed Cluster Managers (11); Cross-Cluster, Multi-Region & Edge (11); Work Admission & Demand Shaping (5); Kubernetes Workload Scaling (5); Container Resources (4); Telecom RAN & Edge Radio (4); AI Training (3).

Governors: The Kubernetes scheduler (vanilla, and its bin-packing profile) (12); Kueue (5); Volcano (5); KAI scheduler (4); Koordinator (4); CruiseKube (4); Crane (5); KubeRay (3); Gödel scheduler (4); Armada (3); Karmada (4); Open Cluster Management (3); KubeEdge (4); Nephio (4).

*Source: `tools/run_orchestra.py`; `CLAUDE.md`.*

### Live Organism (60 muscles)

The sixty muscles the page draws, twelve from the spine and twelve from each realm, put in one organism of the realms harness (the plants of realms/plants.py coupled through their heat and their power) under the climb, on seeds 3000, 3001 and 3002 (runs A, B and C). Native is the plants and their native controllers alone; Omni-Compass on native is the max with the body's bone, its twins and the muscles' cards, and at 80% of the run the brain goes silent and the lease walks every setting back to native over 24 decisions. On the page each body part answers to one organ: the spine to nodes (θ 0.7), compute to pods (0.5), physics to cpufreq (0.3), energy to power (0.3), distribution to routing (0.5). The recorder takes each muscle by its name; the name transparent_hugepages is carried by two catalog rows, and the catalog's last row of that name is the one in the record.

Families: Workflow, Logistics & Fulfillment (4); Aviation & Autonomous Flight (4); Container Resources (3); AI Training (3); Data Analytics & ETL (3); Kubernetes Workload Scaling (2); Host CPU & Memory (2); Robotics Motion Control (2); Energy Storage & Microgrid (2); Cross-Cluster, Multi-Region & Edge (2); Mining & Mineral Processing (2); Power Generation & Turbine Control (2); Elevators & Vertical Transport (2); Grid Transmission & Distribution (2); Kubernetes Placement & Scheduling (1); Node Fleet & Karpenter-Class Control (1); OpenShift & Machine API (1); AI Inference Serving (1); Distributed Cluster Managers (1); Service Mesh & API Reliability (1); Database & Transactions (1); Messaging & Streaming (1); Cache & Memory Services (1); Runtime & Application (1); Robotics Fleet & Warehouse Automation (1); Industrial PLC & Process Automation (1); Spacecraft & Flight Software (1); PDU, UPS & Electrical Distribution (1); Cooling, Chillers & Thermodynamics (1); Quantum Computing Control Simulation (1); Oil & Gas Pipelines (1); Rail Traction & Train Control (1); District Heating & Cooling (1); Pharmaceutical & Food Manufacturing (1); Linux Kernel & OS Control (1); Virtualization & Hypervisor (1); Gut: Data-plane Intake & Waste (1); Skin: Perimeter & Admission (1); Automotive EV & Mobile Powertrain (1).

Body parts: spine (12 muscles, the organ nodes, θ 0.7); compute (12 muscles, the organ pods, θ 0.5); physics (12 muscles, the organ cpufreq, θ 0.3); energy (12 muscles, the organ power, θ 0.3); distribution (12 muscles, the organ routing, θ 0.5).

*Source: `docs/engine/export_harness_trace.py`; `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`.*

### Whole Organism (5 layers)

Omni-Compass at every layer of a stack, each layer measured against its own native with the layer under it as native runs it, composed by the product law into one benefit for the whole stack. Three sectors: the software at one end (the cluster, its add-ons, its governors and the services on it), the bare metal at the other (the card and the machine), and the cloud as the wire between them (the machines it bills, metered). No run has stacked the layers yet: the composition is class S of class P and L measurements. It is the tenth of the ten organisms, read like each of the others native and with Omni-Compass on top of native. It has layers, not catalog muscles.

Sectors: Software (3. the cluster (Kubernetes, its add-ons, its governors), class L, 4. the services on the cluster, class L); Cloud (5. the cloud (Azure, the bill metered), class L); Bare Metal (1. the card (the chip), class P, the machine (the kernel, bare metal, Kepler): not yet run (register row 79), enters as exactly 1).

Every way it is bought: On-Site Bare Metal; Through the Cloud; In the Device; As a Service.

*Source: `DISCLOSURES.md`; `tools/whole_system.py`.*

## 4. The scenarios: every organism under every arm

10 organisms × 2 arms = 20 scenarios.

| Scenario | What runs |
|---|---|
| Spine · native | 267 muscles, each under its own native controller alone. |
| Spine · Omni-Compass on native | the same 267 muscles, every native controller running, Omni-Compass on top of all of them. |
| Compute / AI / Cloud · native | 540 muscles, each under its own native controller alone. |
| Compute / AI / Cloud · Omni-Compass on native | the same 540 muscles, every native controller running, Omni-Compass on top of all of them. |
| Physics / Robotics / Autonomous · native | 404 muscles, each under its own native controller alone. |
| Physics / Robotics / Autonomous · Omni-Compass on native | the same 404 muscles, every native controller running, Omni-Compass on top of all of them. |
| Energy / Facility / Industrial · native | 480 muscles, each under its own native controller alone. |
| Energy / Facility / Industrial · Omni-Compass on native | the same 480 muscles, every native controller running, Omni-Compass on top of all of them. |
| Distribution / Specialized · native | 484 muscles, each under its own native controller alone. |
| Distribution / Specialized · Omni-Compass on native | the same 484 muscles, every native controller running, Omni-Compass on top of all of them. |
| Four Stacked · native | 1,908 muscles, each under its own native controller alone. |
| Four Stacked · Omni-Compass on native | the same 1,908 muscles, every native controller running, Omni-Compass on top of all of them. |
| Whole Tower · native | 1,107 muscles, each under its own native controller alone. |
| Whole Tower · Omni-Compass on native | the same 1,107 muscles, every native controller running, Omni-Compass on top of all of them. |
| Orchestra Organism · native | 55 muscles, each under its own native controller alone. |
| Orchestra Organism · Omni-Compass on native | the same 55 muscles, every native controller running, Omni-Compass on top of all of them. |
| Live Organism · native | 60 muscles, each under its own native controller alone. |
| Live Organism · Omni-Compass on native | the same 60 muscles, every native controller running, Omni-Compass on top of all of them. |
| Whole Organism · native | every layer as native runs it. |
| Whole Organism · Omni-Compass on native | Omni-Compass on top of every piece, composed layer by layer. |

## 5. The muscles, bulked by their realms

Every muscle of `realms/catalog_v5.csv` once: the spine's families first, then each realm's own. Each family names its plant, its class of machine, the native controller that runs it and how it is reached; each muscle its knob, what Omni-Compass does with it (the max, the default) and the organisms it belongs to (spine; the realms; stack; tower; orchestra, with its governors; the live benchmark engine's sixty, with its body part).

**The four kinds of knob.** **capacity**: how much of the machine is in service (replicas, instances, units, speed). At the max Omni-Compass pushes it to the machine's own limit for the most work, never past it and never below native. **admission**: what is let in (queues, rate limits, admission control). Native already lets everything in: the knob is at its limit on native, and Omni-Compass reads it and leaves it native. **power**: the power share or limit the machine may draw. Native already runs it at full: at its limit on native, read and left native. **setpoint**: the target the machine's own loop holds (a temperature, a reserve, a process value). At the max a room is cooled ahead of the heat and a battery's charge is held for its line, inside the safe band, never behind native on its line.

**The five plants.** `compute_pool`: a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; native: the Kubernetes HPA rule (desired = ceil(n * utilisation / target), 10% tolerance, scale-down stabilisation window, start-up delay), a fixed admission limit, full clock. `thermal_zone`: a data hall or building zone cooled by chillers, air handlers or fans; native: PI on a fixed setpoint, units staged to the load, chiller COP from supply and outdoor temperature. `energy_storage`: a battery, UPS or microgrid store with a load and a grid connection; native: self-consumption above a fixed reserve. `motion_axis`: a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; native: PID with feedforward at full speed, motor heating and derating. `process_loop`: a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; native: PI on a fixed setpoint, pump or heater power from the actuator.

### Spine

#### Cloud VM & Capacity (21 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `node`, a fleet of machines or VMs that boot in minutes, reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Native: the cloud's autoscaling group or scale set: AWS Auto Scaling, Azure VMSS, GCP MIG. Run live? on AKS through the node pool (family 5); the cloud SDK path itself is written, not yet run live.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 97 | vm count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 98 | vm size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 99 | vm start stop | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 100 | vm migrate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 101 | instance family | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 102 | asg min | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 103 | asg max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 104 | spot mix | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 105 | reservation mix | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 106 | zone selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 107 | region selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 108 | architecture selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 109 | accelerator selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 110 | boot disk class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 111 | placement group | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 112 | interruption response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1038 | target tracking policy | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1039 | scaling cooldown warmup | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1114 | vm cpu cap by priority | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1120 | predictive scaling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1121 | instance refresh | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Container Resources (25 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the pod's own resource requests and limits (the Deployment template) and, where it runs, the VPA, Goldilocks or CruiseKube recommender. Run live? yes, omni_controller/muscles.py convey() (conveyance); KEDA and Goldilocks tables.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 33 | cpu request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (cruisekube) |
| 34 | cpu limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 35 | memory request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (cruisekube) |
| 36 | memory limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 37 | ephemeral storage | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 38 | hugepages | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 39 | io weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 40 | pids limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 41 | memory high | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 42 | memory reclaim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 43 | swap limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 44 | cgroup io max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 45 | cpu weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 46 | cpu quota | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 47 | cpuset | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 48 | runtime class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1017 | in place resize | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (cruisekube) |
| 1019 | namespace quota | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1020 | default limits | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1022 | memory hard limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1023 | memory protection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1024 | io latency target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1025 | freeze | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2176 | cruisekube request rightsizing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (cruisekube) |
| 2177 | goldilocks vpa request recommendation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Host CPU & Memory (26 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `cpu_host`, a CPU host whose clock and power can be set, reached through Linux cpufreq and RAPL. Native: the Linux kernel's own governors: cpufreq (schedutil or the processor driver), RAPL, cpuidle, the memory manager. Run live? written and tested on the modelled machine (tools/run_cpu_power.py, cpu-power.yml); GitHub's machines are virtual and cannot write the governor: the live run needs a real Linux machine.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 113 | cpufreq min | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 114 | cpufreq max | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 115 | rapl package power | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 116 | uncore frequency | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 117 | energy perf preference | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 118 | cpu idle policy | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 119 | memory bandwidth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 120 | numa balance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 121 | irq affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 122 | llc allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 123 | memory pressure gate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 124 | page reclaim rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 125 | transparent hugepages | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 126 | core online offline | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 127 | thermal throttle policy | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 128 | host power profile | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1040 | frequency governor | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1041 | turbo boost | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1042 | dram power limit | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1043 | swappiness reclaim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1112 | core packing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1115 | per pod cpu frequency range and c state access | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1116 | uncore frequency per node | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2174 | ear cpu frequency policy | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 2175 | ear global energy budget | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2178 | k8s power manager core profile | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Kubernetes Placement & Scheduling (21 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: kube-scheduler and its profiles, the descheduler, PriorityClasses, scheduling gates. Run live? modelled; the API path is the same kubectl patch the live controller uses for the HPA.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 49 | node selector | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler); the sixty (spine) |
| 50 | node affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 51 | pod anti affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 52 | topology spread | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 53 | numa placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 54 | gpu topology | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 55 | storage locality | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 56 | network locality | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 57 | taint toleration | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 58 | priority class | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 59 | preemption policy | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 60 | device claim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 61 | failure domain spread | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 62 | scheduler backoff | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 63 | gang admission | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 64 | deschedule | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 1026 | scheduler scoring strategy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 1027 | scheduler plugin weights | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 1028 | scheduling gates | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (scheduler) |
| 1029 | cpu manager | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2179 | peaks power aware placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Kubernetes Workload Scaling (32 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the HorizontalPodAutoscaler, KEDA ScaledObject or VPA that owns the workload's scale. Run live? yes, scripts/kind_bench.sh and omni_controller (HPA target, KEDA, Goldilocks, CruiseKube), three-run tables in results/live.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 17 | replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 18 | hpa cpu target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (crane) |
| 19 | hpa memory target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 20 | hpa custom target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (crane) |
| 21 | vpa apply | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 22 | scale to zero | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 23 | keda threshold | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 24 | rollout rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 25 | max surge | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 26 | max unavailable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 27 | deployment pause resume | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 28 | rollout abort | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 29 | pod eviction | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 30 | pdb policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 31 | scheduler queue priority | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 32 | api priority fairness | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1001 | hpa min replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (crane) |
| 1002 | hpa max replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (crane) |
| 1003 | hpa scale down stabilisation window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1004 | hpa scale up stabilisation window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1005 | hpa scaling rate policies | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; orchestra (crane) |
| 1006 | hpa policy selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1007 | hpa tolerance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1008 | hpa sync period | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1009 | vpa minmax allowed resources | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1010 | keda polling interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1011 | rollout progress deadline | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1012 | rollout readiness delay | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1014 | unhealthy pod eviction policy | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 1015 | graceful termination | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1016 | probes | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2172 | kepler energy target autoscaling | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### GPU Hardware (22 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `gpu`, GPU serving with a response-time target, reached through nvidia-smi (clock ceiling and power limit) or the serving autoscaler. Native: the card's own firmware limits through NVML and nvidia-smi (power limit, application clocks, MIG, compute mode). Run live? yes, omni_controller/gpu_governor.py and scripts/gpu_paired.sh on a rented A10 (results/gpu); the new card runs wait on Lambda.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 129 | gpu allocate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 130 | gpu power limit | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 131 | gpu sm clock | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 132 | gpu memory clock | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 133 | gpu persistence mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 134 | gpu compute mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 135 | mig mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 136 | mig geometry | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 137 | gpu timeslice | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 138 | gpu mps | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 139 | gpu quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 140 | gpu reset | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 141 | gpu thermal limit | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 142 | gpu ecc response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 143 | gpu job power budget | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1044 | application clocks | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1045 | gpu temperature target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1117 | sync boost | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1118 | target clocks | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2173 | climatik inference power cap | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2180 | adaptive gpu power cap | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 2181 | nvidia platform power budget | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Node Fleet & Karpenter-Class Control (24 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `node`, a fleet of machines or VMs that boot in minutes, reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Native: the cluster's own node autoscaler: Karpenter (NodePool), the Cluster Autoscaler, a MachineSet, a cloud node pool. Run live? yes, omni_controller nodepool mode on kind and on AKS (results/live/V1_AKS_*, the capacity and steady tables).

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 65 | node desired | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 66 | node pool min | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 67 | node pool max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 68 | node provision | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 69 | node cordon | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 70 | node drain | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 71 | node consolidate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 72 | node replace | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 73 | node shutdown | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 74 | node power on | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 75 | nodepool weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 76 | disruption budget | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 77 | consolidation policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 78 | consolidate after | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 79 | expire after | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 80 | capacity class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1030 | scale down utilisation threshold | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1031 | scale down unneeded time | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1032 | scale down delay after add | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1033 | expander | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1034 | node pool limits | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1035 | kubelet eviction thresholds | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1036 | kubelet reserved resources | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1037 | max pods per node | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Network Routing & Switching (19 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `network`, network routing and switching, reached through the network controller (SDN, routing API). Native: the network controller: the load balancer's weights, the SDN controller, the NIC's ethtool and tc settings. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 225 | lb weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 226 | route weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 227 | rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 228 | bandwidth limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 229 | qos class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 230 | connection limit | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 231 | failover route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 232 | nic rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 233 | nic queue count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 234 | queue discipline | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 235 | congestion control | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 236 | egress budget | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 237 | ingress budget | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 238 | ecmp weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 239 | path selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 240 | network isolation | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1046 | nic interrupt coalescing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1047 | nic ring size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1048 | port link power | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Observability & Telemetry (9 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the collector's own configuration: the OpenTelemetry Collector, Prometheus scrape and remote-write settings. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 373 | collector memory limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 374 | export concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 376 | cardinality budget | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 377 | retention window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 378 | remote write queue | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 379 | telemetry shed | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1053 | metric scrape interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1054 | batching | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1119 | per pod energy attribution | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Reliability, Security & Recovery (12 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the platform's own recovery and security controls: rollout and rollback, PodDisruptionBudgets, the security hold, a kill switch. Run live? in part, the security hold and kill switch run in every Kubernetes benchmark (omnicompass/master.py).

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 385 | restart | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 386 | rollback | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 388 | traffic divert recovery | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 389 | degraded mode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 390 | actuator freeze | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 391 | workload isolate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 393 | credential rotation gate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 394 | policy enforcement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 395 | rate abuse gate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 396 | fault domain isolate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 397 | backup trigger | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 400 | kill switch | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Storage Block/File/Object (20 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `storage`, block, file or object storage, reached through the storage system's QoS and tiering API. Native: the storage system's QoS and tiering: Ceph (ceph osd pool set, QoS), a cloud volume's IOPS class, S3 lifecycle. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 257 | volume size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 258 | iops limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 259 | throughput limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 260 | replica count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 261 | storage tier | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 262 | volume placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 263 | snapshot trigger | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 264 | rebalance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 265 | recovery rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 266 | backfill rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 267 | compaction pressure | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 268 | cache allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 269 | object replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 270 | erasure code profile | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 271 | storage admission | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 272 | degraded storage gate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1049 | scrub schedule | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1050 | io scheduler | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1051 | disk power spin down | power | at its limit on native (the full clock): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1052 | lifecycle tiering | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### Cooling, Chillers & Thermodynamics (18 muscles)

Plant `thermal_zone`, a data hall or building zone cooled by chillers, air handlers or fans; class `data_hall`, a data hall cooling plant, reached through the building management system (BACnet, Modbus) or its command line. Native: the building management system and the chiller plant's own supervisory controller (BACnet, Modbus). Run live? modelled (the data-hall plant); the BACnet path is written.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 545 | supply air temperature | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 546 | return air target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 547 | coolant supply temperature | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 548 | coolant flow | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 549 | pump speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 550 | fan speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 551 | chiller setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 552 | compressor authority | power | at its limit on native (the site envelope at full): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 553 | cooling tower fan | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 554 | cooling capacity | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 555 | rack thermal budget | power | at its limit on native (the site envelope at full): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 556 | gpu thermal envelope | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 557 | cpu thermal envelope | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 558 | thermal workload migrate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 559 | thermal load shed | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1055 | server fan speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1056 | economiser | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1122 | chiller plant supervisory control rl with safety layer | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | spine; Compute; Physics; Energy; Distribution; stack; tower |

#### PDU, UPS & Electrical Distribution (18 muscles)

Plant `energy_storage`, a battery, UPS or microgrid store with a load and a grid connection; class `ups`, an uninterruptible power supply, reached through the UPS and PDU management interface (SNMP, Modbus). Native: the UPS and PDU management interfaces (SNMP, Modbus) and the servers' BMC power caps (IPMI DCMI, Redfish). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 529 | server power cap | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 530 | rack power cap | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 531 | pdu branch power limit | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 532 | pdu outlet control | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 534 | ups operating mode | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 535 | ups charge rate | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 536 | ups discharge rate | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 537 | phase balance | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 538 | load transfer | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 539 | reactive power target | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 540 | voltage target | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 541 | generator dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower; the sixty (spine) |
| 542 | electrical isolation | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 543 | breaker trip gate | admission | at its limit on native (nothing paced or turned away): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1057 | ups shutdown battery test | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1110 | hierarchical power budget row pdu switchboard controllers | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1111 | priority aware capping throttle low priority first | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |
| 1113 | power oversubscription with prediction | power | at its limit on native (full battery power): read and left native | spine; Compute; Physics; Energy; Distribution; stack; tower |

### Compute / AI / Cloud

#### AI Inference Serving (24 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `gpu`, GPU serving with a response-time target, reached through nvidia-smi (clock ceiling and power limit) or the serving autoscaler. Native: the serving engine's own autoscaler and batcher (vLLM, Triton, KServe, Ray Serve): replicas, batch size, concurrency, KV cache. Run live? in part, GPU serving under the card governor (results/gpu); the vLLM run is ready and waits on Lambda.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 161 | model replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| 162 | model route weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 163 | model load | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 164 | model unload | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 165 | model instance count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 166 | continuous batching | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 167 | max batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 168 | batch queue delay | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 169 | inference concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 170 | inference max tokens | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 171 | kv cache budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 172 | prefix cache budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 173 | speculative decode budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 174 | model precision | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| 175 | inference priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 176 | inference slo gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1058 | autoscaling target concurrency qps | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1059 | scale to zero panic window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1060 | request priority levels | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1061 | kv cache swap space | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1062 | chunked prefill | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1063 | tensor parallel degree | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1064 | disaggregated prefill decode | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1065 | lora adapter load | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### AI Training (18 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `gpu_batch`, GPU training and batch work, reached through nvidia-smi, the job scheduler's pause and resume. Native: the training job's launcher and scheduler (Kubeflow, Ray Train, Slurm, torchrun). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 177 | training workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (kuberay) |
| 178 | global batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 179 | microbatch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 180 | gradient accumulation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 181 | data parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 182 | tensor parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 183 | pipeline parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 184 | expert parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 185 | checkpoint interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 186 | checkpoint trigger | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| 187 | training preempt | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 188 | training gang size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (kuberay) |
| 189 | elastic worker count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (kuberay) |
| 190 | straggler mitigation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 191 | training precision | power | at its limit on native (the full clock): read and left native | Compute; stack; tower; the sixty (compute) |
| 192 | compute comm overlap | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| 1066 | activation checkpointing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1067 | dataloader workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### Cross-Cluster, Multi-Region & Edge (18 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `node`, a fleet of machines or VMs that boot in minutes, reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Native: the global load balancer and the fleet manager (Karmada, Fleet, the cloud's global LB). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 609 | multi cluster dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (armada, karmada, ocm) |
| 610 | region dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (karmada) |
| 611 | zone dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 612 | edge dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (kubeedge); the sixty (compute) |
| 613 | cloud capacity class | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 614 | workload migrate region | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (ocm) |
| 615 | data residency gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 616 | latency region gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 617 | cost region gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 618 | carbon region gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 619 | global failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (karmada) |
| 620 | federation quota | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (armada, ocm) |
| 621 | cross cluster replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (karmada) |
| 622 | edge offload | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (kubeedge) |
| 623 | global admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (armada); the sixty (compute) |
| V5-5128 | edge site node pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (kubeedge) |
| V5-5129 | edge inference gpu clocks | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| V5-5130 | edge sync interval | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower; orchestra (kubeedge) |

#### DPU SmartNIC & Programmable IO (12 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `fabric`, a high-speed fabric (RDMA, DPU, SmartNIC), reached through the fabric manager's API. Native: the DPU's own management (NVIDIA DOCA, the SmartNIC's SDK) and SR-IOV. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| AUDIT-0021 | dpu pf tx rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0022 | dpu vf tx rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0023 | dpu sf tx rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0024 | dpu bandwidth share | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0025 | dpu qos group | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0026 | sriov vf count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0027 | smartnic flow steering | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0028 | smartnic offload enable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0029 | dpu cpu budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| AUDIT-0030 | dpu memory budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| AUDIT-0031 | dpu service placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0032 | dpu failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### Distributed Cluster Managers (15 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `batch`, batch and queued jobs, reached through the job queue (Kubernetes Jobs, Slurm, Spark). Native: the cluster manager's scheduler: YARN, Mesos, Nomad, Ray. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 209 | task admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (godel) |
| 210 | task priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (volcano) |
| 211 | resource reservation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (godel) |
| 212 | cluster quota | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (kai) |
| 213 | task preemption | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (volcano, kai); the sixty (compute) |
| 214 | binpack pressure | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (volcano, koordinator, godel) |
| 215 | spread pressure | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (koordinator) |
| 216 | gang schedule | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (volcano, kai, godel) |
| 217 | worker allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 218 | maintenance evacuation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 219 | oversubscription | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (koordinator) |
| 220 | resource reclaim | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; orchestra (koordinator) |
| 221 | queue fairness | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (volcano, kai) |
| 222 | deadline pressure | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 223 | scheduler retry | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |

#### GPU Fabric & RDMA (18 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `fabric`, a high-speed fabric (RDMA, DPU, SmartNIC), reached through the fabric manager's API. Native: the fabric manager and the collective library (NVIDIA Fabric Manager, NCCL settings, RDMA CM). Run live? modelled; written against NCCL and Fabric Manager documentation.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 145 | nvlink placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 146 | nvswitch route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 147 | gpu fabric quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 148 | rdma bandwidth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 149 | rdma route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 150 | nic affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 151 | collective concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 152 | collective algorithm | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 153 | collective chunk size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 154 | rank placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 155 | gpudirect policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 156 | congestion response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 157 | rail selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 158 | fabric failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 159 | communication priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 160 | fabric isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1068 | collective protocol | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1069 | nic hca selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### HPC & Distributed Compute (19 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `batch`, batch and queued jobs, reached through the job queue (Kubernetes Jobs, Slurm, Spark). Native: the batch scheduler: Slurm (scontrol, sacctmgr), PBS, LSF. Run live? modelled; EAR (family 8) is the live energy path on HPC.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 193 | job slots | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 194 | mpi ranks | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 195 | rank mapping | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 196 | node allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 197 | job walltime | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 198 | job priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 199 | job preemption | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 200 | checkpoint restart | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 201 | parallel io budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 202 | collective budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 203 | accelerator share | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 204 | cpu gpu ratio | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 205 | memory per rank | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 206 | scratch budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 207 | scheduler fair share | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 208 | backfill policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 1070 | node power saving | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| 1071 | cpu frequency per job | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| 1072 | partition limits | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### Kubernetes Dynamic Device Allocation (8 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `gpu`, GPU serving with a response-time target, reached through nvidia-smi (clock ceiling and power limit) or the serving autoscaler. Native: Kubernetes DRA: DeviceClass, ResourceClaim, ResourceSlice. Run live? modelled; the API path is kubectl.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| AUDIT-0001 | dra device class selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0002 | dra claim capacity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0003 | dra claim sharing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0004 | dra device taint | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0005 | dra device eviction | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| AUDIT-0006 | dra binding readiness | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0007 | dra binding failure response | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| AUDIT-0008 | dra device configuration | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### OpenShift & Machine API (9 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `node`, a fleet of machines or VMs that boot in minutes, reached through the node pool's size command (Karpenter, Cluster Autoscaler, MachineSet, cloud ASG). Native: OpenShift's Machine API operators: MachineHealthCheck, MachineConfigPool, the Cluster Version Operator. Run live? modelled; written against the documented OpenShift API, not yet run live.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 85 | machine remediation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| 88 | machine health gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 89 | mcp pause | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 90 | mcp max unavailable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 91 | node config rollout | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 92 | operator reconcile budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 93 | cluster version pacing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 94 | infra machine admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 95 | machine failure domain | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### Quantum Computing Control Simulation (16 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `qpu`, a quantum or specialised accelerator queue, reached through the accelerator's job queue. Native: the quantum control stack's job queue and pulse schedules (Qiskit Runtime, the vendor's control software). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 593 | qubit mapping | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| 594 | circuit admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 595 | shot allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 596 | circuit scheduling | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 597 | gate scheduling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 598 | pulse amplitude | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 599 | pulse duration | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 600 | pulse phase | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 601 | pulse frequency | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| 602 | coupling control | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 603 | reset scheduling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 604 | measurement scheduling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 605 | dynamical decoupling | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 606 | noise aware routing | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| 607 | error mitigation budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 608 | quantum queue priority | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |

#### Work Admission & Demand Shaping (19 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the service's own admission layer: its API gateway, queue or admission controller (Envoy, NGINX, Kong, a job queue's concurrency setting). Run live? at its limit on native: read and left native in every run (nothing is paced or turned away); the wire is read-only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 1 | api concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 2 | queue concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (kueue) |
| 3 | queue backpressure | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (kueue) |
| 4 | job admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (kueue) |
| 5 | batch admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (kueue) |
| 6 | inference admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 7 | load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 8 | priority gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 9 | tenant admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower; orchestra (kueue) |
| 10 | burst limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 11 | deadline admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 12 | work budget | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 13 | request queue limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 14 | retry admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 15 | background work gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 16 | maintenance work gate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1074 | request concurrency limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1123 | adaptive concurrency limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| 1124 | priority request queue under limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |

#### Linux Kernel & OS Control (20 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `cpu_host`, a CPU host whose clock and power can be set, reached through Linux cpufreq and RAPL. Native: the Linux kernel's own tunables: cgroup v2 files, /proc/sys/vm and net, the cpufreq and cpuidle governors, the I/O scheduler. Run live? the CPU frequency path is written (tools/run_cpu_power.py); the other knobs are registered and queued, they need a real Linux machine.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5001 | cgroup cpu weight | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5002 | cgroup cpu quota | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5003 | cgroup memory high | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5004 | cfs scheduler latency | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5005 | cpufreq dvfs governor | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| V5-5006 | transparent hugepages | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower; the sixty (spine) |
| V5-5007 | io scheduler depth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5008 | numa auto balancing | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5009 | dirty ratio writeback | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5010 | vm swappiness | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5011 | tcp buffer autotune | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5012 | block nr requests | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5013 | ksm memory dedup | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |
| V5-5014 | net rx coalesce | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5015 | cpu cstate governor | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| V5-5016 | zswap pool fraction | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5017 | page cache reclaim | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5018 | irqbalance affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5019 | net qdisc codel target | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5020 | hugepage pool reserve | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### Serverless & Functions (FaaS) (9 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the function platform's concurrency settings (Knative autoscaling annotations, AWS Lambda concurrency, OpenFaaS). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5021 | fn concurrency limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5022 | fn provisioned concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5023 | fn scale to zero idle | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5024 | fn memory size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5025 | fn prewarm pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5026 | fn reserved concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5027 | fn burst admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5028 | fn snapstart restore | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5029 | fn timeout budget | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |

#### Virtualization & Hypervisor (9 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `cpu_host`, a CPU host whose clock and power can be set, reached through Linux cpufreq and RAPL. Native: the hypervisor's management API (libvirt, vSphere, Hyper-V). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5030 | vcpu allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5031 | memory ballooning | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| V5-5032 | vm overcommit density | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5033 | live migration pacing | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5034 | numa vcpu pinning | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5035 | sriov vf allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5036 | vgpu partition | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5037 | vm memory dedup ksm | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |
| V5-5038 | hypervisor cpu pinning | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

#### Gut: Data-plane Intake & Waste (8 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `process`, an industrial process loop, reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Native: the data plane's own intake pacing and compaction settings (the ingress, the queue, the store's compactor). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5045 | ingress intake pacing | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |
| V5-5046 | dead letter retry cap | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5047 | gc compaction pacing | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |
| V5-5048 | ttl eviction waste | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5049 | backpressure threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5050 | queue drain rate | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |
| V5-5051 | retry budget window | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower; the sixty (compute) |
| V5-5052 | compaction debt drain | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |

#### Skin: Perimeter & Admission (5 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the perimeter's own controls: the WAF, the DDoS shield, the TLS terminator. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5053 | rate limit token bucket | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5054 | connection admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5055 | waf inspection sampling | capacity | at its limit on native (the full actuator): read and left native | Compute; stack; tower |
| V5-5056 | tls session cache | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower; the sixty (compute) |
| V5-5057 | ddos shield admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |

#### Media Streaming & CDN (14 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `process`, an industrial process loop, reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Native: the streaming stack's transcoder pools, packager and CDN settings. Run live? modelled; the GPU path is live (family 9).

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5072 | abr bitrate ladder cap | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5073 | player buffer target | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5074 | transcoder worker pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5075 | live transcode gpu clocks | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| V5-5076 | vod transcode batch power | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| V5-5077 | packager workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5078 | origin shield cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5079 | edge cache ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5080 | segment duration target | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5081 | cdn request coalescing | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5082 | drm license server pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5083 | thumbnail sprite batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5084 | media ingest admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5085 | encoder lookahead frames | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |

#### Game Servers & Real-Time Interactive (12 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: Agones Fleets and the matchmaker, the game node pool. Run live? modelled; the API path is kubectl patch.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5086 | agones fleet buffer size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5087 | agones fleet min replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5088 | agones fleet max replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5089 | game server tick rate | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5090 | players per server cap | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5091 | matchmaking admission rate | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5092 | matchmaking wait window | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5093 | relay server pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5094 | voice chat mixer pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5095 | game node pool autoscaler | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5096 | replay render batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5097 | cloud gaming gpu clocks | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |

#### Blockchain & Ledger Nodes (10 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `storage`, block, file or object storage, reached through the storage system's QoS and tiering API. Native: the node's configuration (cache sizes, peer limits, mempool) and its host's power profile. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5098 | node db cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5099 | mempool max size | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5100 | max peer connections | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5101 | script validation threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5102 | block relay admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5103 | rpc work queue depth | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5104 | utxo cache flush interval | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5105 | indexer batch workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5106 | archive node storage tier | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5107 | validator host power profile | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |

#### CI/CD & Build Farms (10 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `batch`, batch and queued jobs, reached through the job queue (Kubernetes Jobs, Slurm, Spark). Native: the runner scale set (actions-runner-controller, GitLab runners) and the build cache. Run live? modelled; the API path is kubectl patch.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5108 | runner scale set min runners | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5109 | runner scale set max runners | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5110 | build concurrency limit | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5111 | build cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5112 | test shard parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5113 | job queue admission | admission | at its limit on native (nothing paced or turned away): read and left native | Compute; stack; tower |
| V5-5114 | artifact retention ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Compute; stack; tower |
| V5-5115 | build node cpu frequency | power | at its limit on native (the full clock): read and left native | Compute; stack; tower |
| V5-5116 | remote execution workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |
| V5-5117 | warm runner pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Compute; stack; tower |

### Physics / Robotics / Autonomous

#### Automotive EV & Mobile Powertrain (14 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `ev_traction`, an electric vehicle traction motor, reached through the vehicle's motor controller (CAN; modelled only). Native: the vehicle's motor and battery controllers (CAN, the OEM's diagnostic interface). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 1083 | state of charge limits | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 1084 | smart charging schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower; the sixty (physics) |
| AUDIT-0045 | traction torque limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0046 | regen braking level | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0047 | battery charge limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0048 | battery discharge limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0049 | battery thermal target | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0050 | motor thermal limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0051 | vehicle speed envelope | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| AUDIT-0052 | energy recovery target | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0053 | auxiliary power budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0054 | fast charge current | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0055 | fast charge voltage | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| AUDIT-0056 | vehicle safe state | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |

#### Aviation & Autonomous Flight (28 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `flight_axis`, a flight-control axis, reached through the flight controller (modelled only). Native: the flight controller's own parameters: PX4 (MPC_XY_VEL_MAX, MPC_Z_VEL_MAX_UP, MPC_ACC_HOR, MC_ROLLRATE_MAX) and ArduPilot (WPNAV_SPEED, ATC_ACCEL_R_MAX), the battery failsafe. Run live? modelled: the swarm cells (results/live/V3_SWARM.md); the MAVLink path is written, not yet flown.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 481 | throttle envelope | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 482 | attitude target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 483 | attitude rate target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 484 | velocity target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower; the sixty (physics) |
| 485 | altitude target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower; the sixty (physics) |
| 486 | waypoint authority | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 487 | flight hold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 488 | return to home | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 489 | land action | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 490 | mission admission | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 491 | geofence response | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 492 | failsafe selection | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 493 | battery reserve threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 494 | actuator saturation envelope | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 495 | flight mode transition | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 496 | flight termination safe state | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 1079 | attitude rate gains | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 1080 | horizontal speed limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower; the sixty (physics) |
| 1081 | vertical speed limits | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 1082 | acceleration jerk limits | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| V5-5143 | px4 mpc xy vel max | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower; the sixty (physics) |
| V5-5144 | px4 mpc z vel max up | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5145 | px4 mpc acc hor | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5146 | px4 mc rollrate max | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5147 | ardupilot wpnav speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5148 | ardupilot atc accel r max | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| V5-5149 | drone battery failsafe reserve | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Physics; stack; tower |
| V5-5150 | swarm formation spacing | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |

#### Robotics Fleet & Warehouse Automation (17 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `robot_fleet`, a fleet of robots or vehicles taking tasks, reached through the fleet manager's dispatch API. Native: the fleet manager's dispatch and charging rules (Open-RMF, the vendor fleet manager). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 449 | robot dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 450 | task assignment | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 451 | traffic reservation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 452 | robot route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 453 | charging dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 454 | battery reserve | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 455 | elevator request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 456 | door request | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 457 | conveyor speed | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 458 | agv speed | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 459 | warehouse zone admission | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 460 | robot quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 461 | fleet failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 462 | human safe stop | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower |
| 463 | fleet concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| V5-5151 | amr fleet charge threshold | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Physics; stack; tower |
| V5-5152 | amr fleet active robots | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower; the sixty (physics) |

#### Robotics Motion Control (26 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `robot_joint`, a robot joint servo, reached through the robot controller (ROS 2, EtherCAT, the drive's fieldbus). Native: the robot's own controller: ros2_control and MoveIt parameters, the drive's limits over EtherCAT or the vendor fieldbus. Run live? modelled: MuJoCo (results/live/V3_MUJOCO.md); the ROS 2 path is written, not yet run on a physical arm.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 433 | joint position | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 434 | joint velocity | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 435 | joint acceleration | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 436 | joint effort | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 437 | cartesian velocity | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 438 | trajectory speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 439 | trajectory acceleration | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 440 | jerk limit | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 441 | collision margin | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 442 | force limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower; the sixty (physics) |
| 443 | gripper force | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 444 | locomotion speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 445 | steering angle | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 446 | braking force | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 447 | balance correction | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 1076 | trajectory tolerances | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 1077 | velocity acceleration scaling | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 1078 | controller update rate | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5135 | ros2 executor threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Physics; stack; tower; the sixty (physics) |
| V5-5136 | ros2 qos history depth | setpoint | left native: native already holds it inside its band (nothing to win) | Physics; stack; tower |
| V5-5137 | ros2 control loop rate | setpoint | left native: native already holds it inside its band (nothing to win) | Physics; stack; tower |
| V5-5138 | humanoid balance margin | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5139 | humanoid gait speed | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5140 | humanoid joint torque limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| V5-5141 | humanoid step height | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| V5-5142 | manipulator payload speed scaling | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |

#### Spacecraft & Flight Software (14 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `reaction_wheel`, a spacecraft reaction wheel, reached through the attitude controller (modelled only). Native: the flight software's command and mode tables (cFS, F Prime). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 497 | space command admission | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 499 | flight task schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 500 | space mode transition | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 501 | payload duty cycle | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 502 | communication allocation | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 503 | space power budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower; the sixty (physics) |
| 504 | space thermal command | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 505 | attitude command envelope | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 506 | reaction wheel allocation | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 507 | rcs authority | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 508 | safe mode transition | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 509 | watchdog recovery | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 510 | instrument activation | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 511 | fault isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |

#### Rail Traction & Train Control (14 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `rail_traction`, a train's traction and auxiliary systems, reached through the train control and management system and ATO (modelled only). Native: the train control and management system and ATO. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2054 | traction effort limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2055 | regenerative braking share | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2056 | coasting speed target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2057 | dwell time schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2058 | hvac duty cycle | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2059 | train auxiliary power budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2060 | platform approach speed | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2061 | acceleration rate setpoint | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2062 | wheel slip protection mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2063 | traction motor thermal derate | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2064 | catenary voltage limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2065 | timetable recovery margin | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower; the sixty (physics) |
| 2066 | headway target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2067 | door release hold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |

#### Marine Propulsion & Vessel Automation (12 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `marine_propulsion`, a ship's propulsion shaft and power plant, reached through the vessel automation and power management system (modelled only). Native: the vessel's automation and power management system. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2068 | shaft speed target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 2069 | propeller pitch limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2070 | shaft power limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2071 | bow thruster duty | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2072 | ballast pump mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2073 | engine load sharing setpoint | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 2074 | slow steaming speed target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 2075 | auxiliary engine staging | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 2076 | shore power mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2077 | hotel load budget | power | at its limit on native (full torque): read and left native | Physics; stack; tower |
| 2078 | trim target | capacity | its own peak speed while tasks wait, back to its everyday speed near its heat limit or when its tracking strains (alone; inside a body, its everyday speed) | Physics; stack; tower |
| 2079 | rudder rate limit | power | at its limit on native (full torque): read and left native | Physics; stack; tower |

#### Elevators & Vertical Transport (12 muscles)

Plant `motion_axis`, a motor-driven axis: a robot joint, a flight-control surface, a reaction wheel, a traction motor; class `elevator_hoist`, an elevator or escalator drive and its group control, reached through the lift controller and destination dispatch (modelled only). Native: the lift controller and destination dispatch. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2146 | hoist speed target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2147 | acceleration limit | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2148 | regen drive mode | power | at its limit on native (full torque): read and left native | Physics; stack; tower; the sixty (physics) |
| 2149 | standby power mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2150 | destination dispatch schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2151 | car parking mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2152 | door dwell hold | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2153 | escalator speed target | capacity | at its limit on native (its everyday speed is the machine's limit): read and left native | Physics; stack; tower |
| 2154 | group capacity mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2155 | motor thermal derate | power | at its limit on native (full torque): read and left native | Physics; stack; tower; the sixty (physics) |
| 2156 | brake test schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |
| 2157 | fire recall mode | admission | at its limit on native (nothing paced or turned away): read and left native | Physics; stack; tower |

### Energy / Facility / Industrial

#### Building & Critical Environment HVAC (15 muscles)

Plant `thermal_zone`, a data hall or building zone cooled by chillers, air handlers or fans; class `building`, a building zone, reached through the building management system. Native: the building management system (BACnet) and the AHU and zone controllers. Run live? modelled: CityLearn districts (results/live/V3_CITYLEARN.md); the BACnet path is written.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 1094 | setpoint reset trim and respond | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 1095 | duct static pressure setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 1096 | optimal start stop | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| AUDIT-0081 | zone temperature target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| AUDIT-0082 | zone airflow | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| AUDIT-0083 | ahu fan speed | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| AUDIT-0084 | damper position | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| AUDIT-0085 | economizer position | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| AUDIT-0086 | boiler setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| AUDIT-0087 | heat pump mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0088 | humidity target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| AUDIT-0089 | occupancy ventilation | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0090 | building demand limit | power | at its limit on native (the site envelope at full): read and left native | Energy; stack; tower |
| AUDIT-0091 | thermal storage dispatch | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| AUDIT-0092 | hvac emergency mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Energy Storage & Microgrid (19 muscles)

Plant `energy_storage`, a battery, UPS or microgrid store with a load and a grid connection; class `microgrid`, a microgrid battery and loads, reached through the inverter or energy management system (IEEE 2030.5, SunSpec, OpenADR). Native: the battery's or site's energy management system and inverter (SunSpec, IEEE 2030.5, OpenADR, Modbus). Run live? modelled: CityLearn (results/live/V3_CITYLEARN.md) for the districts; the register path is written.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 513 | battery charge power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 514 | battery discharge power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 515 | battery soc reserve | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 516 | grid import limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 517 | grid export limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 518 | pv curtailment | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 519 | ev charge power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 520 | heat pump power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 521 | electrolyzer power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 522 | microgrid demand limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 523 | peak shaving | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 524 | time of use schedule | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 525 | energy load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower; the sixty (energy) |
| 526 | flex load admission | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 527 | storage dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower; the sixty (energy) |
| 528 | microgrid emergency reserve | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 1085 | volt var | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 1086 | volt watt | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 1087 | constant power factor reactive power | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |

#### Facility & Grid Optimization (15 muscles)

Plant `energy_storage`, a battery, UPS or microgrid store with a load and a grid connection; class `facility`, a facility battery behind the meter, reached through the energy management system. Native: the facility's energy management system and demand-response gateway (OpenADR). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 561 | facility power budget | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 562 | utility demand limit | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 563 | demand response | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 564 | electricity price gate | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 565 | carbon intensity gate | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 566 | renewable dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 567 | generator start stop | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 568 | site battery dispatch | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 569 | pue target | setpoint | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 570 | cooling power budget | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 571 | it power budget | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 572 | rack power allocation | power | at its limit on native (full battery power): read and left native | Energy; stack; tower |
| 573 | facility peak guard | capacity | holds the charge for the line and clips only the draw that would cross it; a UPS lends only the charge above its outage floor | Energy; stack; tower |
| 574 | grid frequency response | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 575 | facility islanding | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Grid Transmission & Distribution (12 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `feeder_voltage`, a distribution feeder's voltage, reached through the distribution management system (IEC 61850, DNP3; modelled only). Native: the distribution management system and the devices' own controllers (IEC 61850, DNP3): regulators, capacitor banks, inverters. Run live? modelled: SimBench grids (results/live/V3_PANDAPOWER.md).

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| AUDIT-0033 | capacitor bank switch | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0034 | voltage regulator tap | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0035 | transformer tap | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0036 | inverter real power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower; the sixty (energy) |
| AUDIT-0037 | inverter reactive power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0038 | feeder voltage target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower; the sixty (energy) |
| AUDIT-0039 | feeder load transfer | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0040 | distribution storage dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0041 | demand response dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0042 | frequency droop setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0043 | grid protection mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0044 | grid restoration sequence | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Industrial PLC & Process Automation (18 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `process`, an industrial process loop, reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Native: the PLC or DCS loop (OPC UA, EtherNet/IP, PROFINET): the setpoint and the mode of each loop. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 465 | plc cycle authority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 466 | machine cell admission | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 467 | valve position | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 468 | pump flow | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 469 | compressor speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 470 | heater power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 471 | furnace setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 472 | pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 473 | temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 474 | mass flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 475 | tank level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 476 | conveyor rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 477 | feed rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 478 | purge vent action | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 1088 | controller mode | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower; the sixty (energy) |
| 1089 | alarm limits | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 1090 | safety interlock trip | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 1091 | opc ua writes | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |

#### Semiconductor Fab & Precision Manufacturing (13 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `chamber`, a controlled chamber (clean room, kiln, reactor), reached through the PLC or DCS. Native: the fab's MES and each tool's controller (SECS/GEM). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 1092 | run to run control | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 1093 | idle sleep mode | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0057 | tool job dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0058 | wafer route | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0059 | chamber recipe selection | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0060 | chamber temperature | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0061 | chamber pressure | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0062 | gas flow | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0063 | rf power | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0064 | vacuum pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0065 | robot transfer rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0066 | lot priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0068 | tool quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Water Wastewater & Pumping (12 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `water`, a water or pumping process, reached through the SCADA system (Modbus, DNP3). Native: the utility's SCADA (Modbus, DNP3) and the pump station controllers. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| AUDIT-0069 | pump speed water | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0070 | valve position water | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0071 | reservoir level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0072 | line pressure target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0073 | flow target water | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| AUDIT-0074 | aeration rate | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0075 | chemical dose rate | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| AUDIT-0076 | filtration backwash | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0077 | lift station dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0078 | leak isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0079 | water demand shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| AUDIT-0080 | water emergency shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Healthcare Critical Environments (13 muscles)

Plant `thermal_zone`, a data hall or building zone cooled by chillers, air handlers or fans; class `hospital`, a hospital's critical rooms (operating rooms, isolation, pharmacy, imaging suites), reached through the hospital's building management system (BACnet). Native: the hospital's building management system (BACnet) with its clinical limits. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2001 | operating room air change setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2002 | isolation room pressure target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2003 | patient room temperature setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2004 | surgical suite humidity target | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2005 | ahu supply air temperature | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2006 | pharmacy cold room setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2007 | sterile storage humidity setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Energy; stack; tower |
| 2008 | imaging suite cooling capacity | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| 2009 | chiller plant staging | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| 2010 | exhaust fan capacity | capacity | left to its own staging (native already has the cooling it needs: nothing to win) | Energy; stack; tower |
| 2011 | ward night setback mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2012 | medical gas plant demand limit | power | at its limit on native (the site envelope at full): read and left native | Energy; stack; tower |
| 2013 | emergency power load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Agriculture & Irrigation (14 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `irrigation`, pumps, pressure and climate on a farm or in a greenhouse, reached through the pump station controller, the pivot panel or the climate computer (Modbus, the vendor cloud). Native: the pump station controller, pivot panel or climate computer (Modbus, the vendor cloud). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2026 | irrigation pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2027 | mainline pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2028 | soil moisture target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2029 | pivot speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2030 | fertigation dose | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2031 | greenhouse temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2032 | greenhouse co2 target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2033 | vent position setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2034 | grain dryer temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2035 | cold storage temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2036 | barn ventilation rate | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2037 | milking vacuum level setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2038 | well drawdown level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2039 | drip zone dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Oil & Gas Pipelines (14 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `pipeline`, a pipeline segment with its compressors, pumps and valves, reached through pipeline SCADA (DNP3, Modbus, OPC UA). Native: pipeline SCADA (DNP3, Modbus, OPC UA). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2040 | compressor discharge pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2041 | pump station suction pressure target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2042 | line pack target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2043 | pipeline flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2044 | compressor unit staging | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2045 | vfd pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2046 | terminal tank level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2047 | leak detection shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2048 | batch interface dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2049 | heater outlet temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower; the sixty (energy) |
| 2050 | drag reducing agent dose | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2051 | valve position target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2052 | cathodic protection voltage | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2053 | pressure protection priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Mining & Mineral Processing (14 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `mill`, a grinding, flotation or materials-handling circuit, reached through the plant DCS or PLC (OPC UA). Native: the plant DCS or PLC (OPC UA). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2092 | sag mill load setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2093 | mill speed target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower; the sixty (energy) |
| 2094 | crusher gap setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2095 | flotation aeration rate | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower; the sixty (energy) |
| 2096 | cyclone feed pressure target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2097 | thickener underflow density target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2098 | reagent dose | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2099 | conveyor speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2100 | dewatering pump level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2101 | ventilation on demand airflow | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2102 | stockpile level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2103 | slurry pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2104 | tailings discharge shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2105 | ore blend dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### District Heating & Cooling (13 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `district_heat`, a district heating or cooling network, reached through the network control system and substation controllers (Modbus, M-Bus). Native: the network control system and substation controllers (Modbus, M-Bus). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2106 | supply temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2107 | return temperature target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2108 | differential pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2109 | network pump speed | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2110 | heat pump staging | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower; the sixty (energy) |
| 2111 | chp dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2112 | thermal storage level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2113 | peak boiler heater output | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2114 | substation flow limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2115 | peak demand shed | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2116 | outdoor reset setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2117 | cooling network supply temperature | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2118 | cooling storage level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |

#### Power Generation & Turbine Control (14 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `turbine`, a generating unit's governor, boiler or excitation loop, reached through the plant DCS and governor (OPC UA, IEC 61850; modelled only). Native: the plant DCS and the unit's governor (OPC UA, IEC 61850). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2119 | turbine speed droop setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2120 | unit load setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2121 | boiler steam pressure setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower; the sixty (energy) |
| 2122 | feedwater level target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2123 | agc participation limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2124 | excitation voltage setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2125 | hydro gate position target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2126 | combustion air ratio setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2127 | cooling water flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2128 | inlet guide vane position | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2129 | reserve dispatch priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower; the sixty (energy) |
| 2130 | turbine ramp rate limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2131 | emissions shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2132 | nuclear rod position target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |

#### Renewable Generation & Inverter Control (13 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `inverter`, a plant of grid-support inverters or wind turbines, reached through the plant controller and inverter settings (SunSpec, IEC 61850, IEEE 1547). Native: the plant controller and inverter settings (SunSpec, IEC 61850, IEEE 1547). Run live? modelled: SimBench grids solved by pandapower (results/live/V3_PANDAPOWER.md); the register path is written.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2133 | inverter volt var setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2134 | inverter volt watt setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2135 | active power curtailment | power | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2136 | plant reactive power target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2137 | wind turbine yaw offset | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2138 | pitch angle limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2139 | rotor speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2140 | inverter frequency droop setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2141 | ramp rate limit | capacity | at its limit on native (the full actuator): read and left native | Energy; stack; tower |
| 2142 | tracker stow mode | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2143 | string mppt voltage setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2144 | noise mode schedule | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2145 | ice detection shutdown | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

#### Pharmaceutical & Food Manufacturing (14 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `batch_reactor`, a GMP batch reactor, fermenter or food process, reached through the batch control system (ISA-88, OPC UA). Native: the batch control system (ISA-88, OPC UA) with the validated recipe limits. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2158 | reactor temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2159 | agitator speed setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2160 | fermenter dissolved oxygen target | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2161 | ph setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2162 | pasteurizer holding temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2163 | freezer tunnel temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2164 | cip cycle dispatch | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2165 | cleanroom pressure cascade setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2166 | lyophilizer shelf temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2167 | chromatography flow setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower; the sixty (energy) |
| 2168 | steam sterilizer cycle priority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2169 | oven zone temperature setpoint | setpoint | left native: native already holds it inside its band (nothing to win) | Energy; stack; tower |
| 2170 | refrigerant compressor authority | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |
| 2171 | batch hold quarantine | admission | at its limit on native (nothing paced or turned away): read and left native | Energy; stack; tower |

### Distribution / Specialized

#### Cache & Memory Services (16 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the cache's own configuration: Redis CONFIG SET, Memcached runtime settings. Run live? yes, tools/run_redis.py, V3_REDIS.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 305 | cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 306 | cache ttl | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 307 | cache eviction policy | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 308 | cache replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 309 | cache sharding | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 310 | cache prefetch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 311 | cache writeback rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 312 | cache admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 313 | hot key isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 314 | cache connection limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 315 | cache memory limit | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 316 | cache compression | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 317 | cache warmup | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 318 | cache failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 319 | cache flush rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1106 | memory size threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |

#### Commerce & Payment Systems (15 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `commerce`, a customer-facing service with bursts, reached through the Kubernetes API. Native: the payment platform's gateway and its routing rules. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 401 | payment admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 402 | payment concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 403 | payment retry | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 404 | payment timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 405 | fraud review gate | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 406 | authorization route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 407 | processor route weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 408 | transaction queue limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 409 | idempotency window | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 410 | order reservation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 411 | inventory hold | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 412 | checkout load shed | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 413 | refund queue rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 414 | settlement batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 415 | payment failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |

#### Data Analytics & ETL (15 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `batch`, batch and queued jobs, reached through the job queue (Kubernetes Jobs, Slurm, Spark). Native: Spark's dynamic allocation and the SQL engine's slots (spark.dynamicAllocation, Flink's parallelism, warehouse slots). Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 338 | executor size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 339 | dynamic allocation min | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 340 | dynamic allocation max | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 341 | shuffle partitions | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 342 | shuffle bandwidth | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 343 | etl concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 344 | stage parallelism | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 345 | query slots | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 346 | spill threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 347 | cache fraction | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 348 | batch interval | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 349 | stream backpressure | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 350 | data locality wait | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 351 | speculation policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 352 | analytics admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

#### Database & Transactions (19 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `database`, a database cluster, reached through the database operator (replicas, connection pools). Native: the database's own pooler and server settings: PgBouncer's admin console, MySQL SET GLOBAL, MongoDB setParameter, the database operator. Run live? yes, tools/run_pgbench.py, run_sysbench.py, run_ycsb.py, three-run tables V3_PGBENCH, V3_SYSBENCH, V3_YCSB.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 273 | db replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 275 | db memory | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 276 | db cache | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 277 | query concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 278 | read route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 279 | shard placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 280 | db failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 281 | replication lag gate | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 282 | db write throttle | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 283 | db pool resize | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 284 | transaction concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 285 | lock timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower; the sixty (distribution) |
| 286 | checkpoint rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 287 | vacuum compaction rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1099 | parallel workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1100 | background writer | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1101 | synchronous replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1102 | buffer pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1103 | io capacity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |

#### Messaging & Streaming (22 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the broker's own controls: Kafka's admin API and consumer group, RabbitMQ policies, MQTT broker settings. Run live? yes, tools/run_kafka.py, V3_KAFKA.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 289 | partition count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 290 | partition placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 291 | producer quota | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 292 | consumer quota | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 293 | broker io quota | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 294 | message retention | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 295 | queue depth limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 296 | consumer concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 297 | producer batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 298 | fetch batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 299 | rebalance rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 300 | replication factor | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 301 | retry backoff | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 302 | dead letter divert | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 303 | stream priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 304 | broker failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 1104 | prefetch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1105 | memory disk alarm | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5124 | mqtt broker max connections | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5125 | mqtt max inflight messages | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5126 | mqtt session expiry | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5127 | broker cluster nodes | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |

#### Runtime & Application (21 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the application runtime's own settings: thread pools, JVM heap and GC, worker counts, connection pools. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 353 | worker count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 354 | thread pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 355 | jvm heap | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 356 | gc budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower; the sixty (distribution) |
| 357 | connection pool runtime | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 358 | application cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 359 | runtime memory | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 360 | async concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 361 | event loop workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 362 | process count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 363 | request timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 364 | background workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 365 | runtime cpu budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 366 | runtime io budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 367 | runtime restart | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1108 | go runtime | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1109 | keepalive connection reuse | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5131 | dns resolver cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5132 | dns negative cache ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5133 | mail queue concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5134 | mail retry interval | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |

#### Search, Indexing & Vector DB (16 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the search engine's settings API: OpenSearch/Elasticsearch cluster and index settings, the vector database's config. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 321 | index workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 322 | index refresh rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 323 | segment merge rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 324 | search concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 325 | search timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 326 | shard count | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 327 | shard replication | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 328 | shard rebalance | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 329 | vector search k | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 330 | vector batch size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 331 | embedding workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 332 | index memory budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 333 | query route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 334 | hot shard isolation | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 335 | search admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 1107 | circuit breakers | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

#### Service Mesh & API Reliability (16 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the mesh's own policies: Istio DestinationRule and VirtualService, Linkerd ServiceProfile, Envoy filters. Run live? modelled; the API path is kubectl patch.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 241 | circuit breaker | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 242 | retry budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 243 | service timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower; the sixty (distribution) |
| 244 | service concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 245 | connection pool | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 246 | traffic divert | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 247 | traffic mirror | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 248 | canary weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 249 | outlier ejection | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 250 | health threshold | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 251 | dns traffic weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 252 | session affinity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 253 | request hedging | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 254 | fault injection gate | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 255 | service failover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 1097 | load balancing policy | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |

#### Telecom RAN & Edge Radio (12 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `ran`, a radio access network cell or site, reached through the RAN controller (O-RAN interfaces). Native: the RAN's near-real-time RIC and O-RAN interfaces (E2, O1). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| AUDIT-0009 | ran connection admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| AUDIT-0010 | ran ue handover | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| AUDIT-0011 | ran cell traffic steering | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| AUDIT-0012 | ran slice resource budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower; orchestra (nephio) |
| AUDIT-0013 | ran prb allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| AUDIT-0014 | ran scheduler weight | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| AUDIT-0015 | ran tx power | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower |
| AUDIT-0016 | ran antenna tilt | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| AUDIT-0017 | ran carrier enable | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; orchestra (nephio) |
| AUDIT-0018 | ran cell sleep | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; orchestra (nephio) |
| AUDIT-0019 | ran du cu placement | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; orchestra (nephio) |
| AUDIT-0020 | ran fronthaul budget | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

#### Workflow, Logistics & Fulfillment (15 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `workflow`, a workflow or pipeline engine, reached through the workflow engine's concurrency settings. Native: the workflow engine (Temporal, Airflow, Camunda) and the fulfilment system's dispatch rules. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 417 | workflow admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 418 | workflow worker rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 419 | task queue rate | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 420 | workflow retry | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 421 | workflow backoff | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 422 | workflow timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 423 | inventory allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 424 | fulfillment route | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 425 | warehouse queue | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 426 | carrier selection | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 427 | dispatch priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower; the sixty (distribution) |
| 428 | shipment batch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |
| 429 | route replan | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 430 | sla escalation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 431 | compensation action | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower; the sixty (distribution) |

#### Medical Imaging & Clinical Systems (12 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `clinical`, clinical systems: imaging archives, records, interface engines, monitoring gateways, reached through the application's own scaling and admission settings (Kubernetes, the vendor console). Native: the clinical application's own scaling and admission settings (Kubernetes, the vendor console). Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2014 | pacs archive tier target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2015 | dicom router concurrency | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2016 | ehr application replicas | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2017 | hl7 interface queue limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2018 | fhir api rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2019 | reconstruction gpu workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2020 | modality worklist timeout | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2021 | patient monitoring gateway capacity | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2022 | lab analyzer batch window | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2023 | telehealth session admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2024 | clinical backup window | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2025 | imaging prefetch priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

#### Ports & Maritime Logistics (12 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `port`, a container terminal's cranes and vehicles taking moves, reached through the terminal operating system and fleet controllers. Native: the terminal operating system and the equipment fleet controllers. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| 2080 | quay crane allocation | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2081 | yard crane fleet size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2082 | berth window admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2083 | truck gate rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2084 | horizontal transport fleet size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2085 | reefer plug power budget | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower |
| 2086 | shore power connection capacity | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2087 | rail mounted gantry dispatch | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2088 | container dwell priority | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2089 | vessel arrival pacing | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| 2090 | stacking height target | setpoint | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| 2091 | equipment charging window | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

#### Content Delivery & Edge Cache (6 muscles)

Plant `process_loop`, a regulated process: a temperature, pressure, flow, level, voltage or composition held at a setpoint; class `process`, an industrial process loop, reached through the PLC or DCS (OPC UA, EtherNet/IP, PROFINET). Native: the CDN's configuration API and the edge cache's settings. Run live? modelled.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5039 | cdn cache ttl | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5040 | edge cache size | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5041 | origin shield concurrency | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5042 | prefetch aggressiveness | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5043 | tiered cache promotion | capacity | at its limit on native (the full actuator): read and left native | Distribution; stack; tower |
| V5-5044 | edge pop admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

#### Financial Markets & Trading Systems (14 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the trading platform's gateway, matching engine and risk settings, the colocation BMS. Run live? modelled only.

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5058 | matching engine threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5059 | order gateway sessions | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5060 | order admission rate limit | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| V5-5061 | pre trade risk check workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5062 | market data fanout threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5063 | market data conflation interval | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5064 | fix session heartbeat interval | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5065 | kernel bypass poll cores | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower |
| V5-5066 | tick store write batch | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5067 | post trade settlement workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5068 | end of day risk batch power | power | at its limit on native (the full clock): read and left native | Distribution; stack; tower |
| V5-5069 | colocation rack cooling setpoint | setpoint | cools the room ahead of the heat as it nears its limit or its cooling nears flat out; never warmer than native | Distribution; stack; tower |
| V5-5070 | backtest grid nodes | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5071 | surveillance alert queue workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |

#### Reliability, Security & Recovery (6 muscles)

Plant `compute_pool`, a pool of servers, pods, GPUs, links or disks serving a stream of requests or jobs; class `server`, an application service on servers or pods, reached through the Kubernetes API (HPA target and floor, pod resize). Native: the platform's own recovery and security controls: rollout and rollback, PodDisruptionBudgets, the security hold, a kill switch. Run live? in part, the security hold and kill switch run in every Kubernetes benchmark (omnicompass/master.py).

| # | Muscle | Knob | What Omni-Compass does with it | Organisms |
|---:|---|---|---|---|
| V5-5118 | ids capture threads | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5119 | ids ring buffer size | setpoint | left native: native already holds it inside its band (nothing to win) | Distribution; stack; tower |
| V5-5120 | ids rule group admission | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |
| V5-5121 | waf inspection workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5122 | siem ingest pipeline workers | capacity | starts the machines the forecast needs before the rush lands and clears work waiting in line within one machine start, never fewer than native runs; hands back what it no longer needs at once | Distribution; stack; tower |
| V5-5123 | endpoint scan scheduling | admission | at its limit on native (nothing paced or turned away): read and left native | Distribution; stack; tower |

## 6. The index

Every term, organism and arm with the sections of the page that print it, by the section's number and anchor (the page's address followed by the anchor opens the section). The sections, in the page's order:

| Section | Anchor | Title |
|---|---|---|
| 0 | #s-wall | Monitor Wall |
| 1 | #s-health | Control Panel |
| 2a | #s-bottom | Scorecard |
| 2b | #s-answer | Benefit Against Native |
| 2c | #s-board | Benefit Board |
| 2d | #s-loss | LOSS Register |
| 2e | #s-status | Status Board |
| 3a | #s-engines | Live Organism |
| 3b | #s-feed | Golden Signals and Event Log |
| 3c | #s-desk | Control Console |
| 3d | #s-dial | Heartbeat Dial |
| 3e | #s-decision | Control Cycle |
| 3f | #s-plane | Phase Plane and Scoreboard |
| 3g | #s-brain | Brain State |
| 3h | #s-verdict | Verdict |
| 3i | #s-dash | Dashboards |
| 4a | #s-ops | Kubernetes Run Playback |
| 4b | #s-runs | Repetition Telemetry |
| 4c | #s-live | Controller Decision Trace |
| 4d | #s-cloud | Cloud Providers |
| 4e | #s-orch | Orchestrators and Governors |
| 4f | #s-stacks | GPU and CPU Hardware |
| 4g | #s-github | CI Pipeline |
| 5a | #s-proof | Python Runs and Monte Carlo |
| 5b | #s-cpp | C++ Twin |
| 5c | #s-scn | Scenarios and Injection Grid |
| 5d | #s-whole | Whole Organism |
| 5e | #s-fleet | Measured Effect |
| 5f | #s-lab | Telemetry Analytics |
| 5g | #s-master | Master Switch Wiring |
| 5h | #s-math | Specification and Mathematics |
| 5i | #s-fail | Failure Modes and Controls |
| 5j | #s-self | Self-Governed Rendering |
| B | #s-guide | Reading Guide |
| C | #s-problem | Problem and Answer |
| D | #s-read | Executive Summary and Reading Key |
| E | #s-monlist | Monitor List |
| G | #s-disclose | Disclosures, Law and Contact |

| Term | Kind | Where on the page |
|---|---|---|
| the 0.5% floor | term | 2a (#s-bottom); 3d (#s-dial); 3f (#s-plane); 4c (#s-live); 4d (#s-cloud); 5h (#s-math); B (#s-guide); D (#s-read) |
| the 95% interval on Student's t | term | 2b (#s-answer); 2c (#s-board); 3f (#s-plane); 3h (#s-verdict); 4a (#s-ops); 4c (#s-live); 4d (#s-cloud); 4f (#s-stacks); 5d (#s-whole); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read) |
| A | term | 5h (#s-math) |
| a changed tune's violet | term | B (#s-guide) |
| a governor's way | term | B (#s-guide) |
| active profile | term | B (#s-guide) |
| actuation feedback | term | 3b (#s-feed); B (#s-guide) |
| alert minute | term | C (#s-problem); D (#s-read) |
| at its limit on native | term | 4f (#s-stacks); 5e (#s-fleet); B (#s-guide); D (#s-read) |
| automatic optimizer | term | 3i (#s-dash) |
| AWAITING | term | B (#s-guide) |
| the band | term | 3a (#s-engines); 3b (#s-feed); 3e (#s-decision); 3f (#s-plane); 4a (#s-ops); 4b (#s-runs); 5d (#s-whole); 5f (#s-lab); 5h (#s-math); 5j (#s-self); B (#s-guide); C (#s-problem) |
| the benefit board | term | 2c (#s-board); B (#s-guide); C (#s-problem) |
| the bill of a route | term | 2b (#s-answer); 4d (#s-cloud); 5d (#s-whole); 5h (#s-math); B (#s-guide); C (#s-problem) |
| the bone | term | 3a (#s-engines); 5h (#s-math); B (#s-guide) |
| the C++ twin | term | 1 (#s-health); 4g (#s-github); 5a (#s-proof); 5b (#s-cpp); 5h (#s-math); B (#s-guide); E (#s-monlist); G (#s-disclose) |
| calm | term | 3e (#s-decision); 3g (#s-brain); 4a (#s-ops); 4b (#s-runs); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem) |
| the centre | term | 3a (#s-engines); 5f (#s-lab); 5h (#s-math); B (#s-guide) |
| the climb | term | 5e (#s-fleet); 5h (#s-math); B (#s-guide) |
| the cloud as the wire | term | 2b (#s-answer); 4a (#s-ops); 4d (#s-cloud); 5d (#s-whole); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read) |
| collector | term | 3i (#s-dash) |
| Commands | term | 1 (#s-health); 5h (#s-math); B (#s-guide); C (#s-problem) |
| the compass | term | 1 (#s-health); 3a (#s-engines); 3e (#s-decision); 3f (#s-plane); 4a (#s-ops); 4b (#s-runs); 4c (#s-live); 5a (#s-proof); 5b (#s-cpp); 5f (#s-lab); 5h (#s-math); 5j (#s-self); B (#s-guide); G (#s-disclose) |
| the compass law | term | 1 (#s-health); 3a (#s-engines); 3f (#s-plane); 4c (#s-live); 5a (#s-proof); 5b (#s-cpp); 5h (#s-math); 5j (#s-self); B (#s-guide); G (#s-disclose) |
| Compute / AI / Cloud | organism | 3c (#s-desk); C (#s-problem) |
| the conductor | term | 3c (#s-desk) |
| console | term | 1 (#s-health); 2c (#s-board); 3a (#s-engines); 3c (#s-desk); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3i (#s-dash); 4d (#s-cloud); 5e (#s-fleet); 5f (#s-lab); 5i (#s-fail); B (#s-guide) |
| the conveyance | term | 3d (#s-dial); 5a (#s-proof); 5h (#s-math); B (#s-guide); G (#s-disclose) |
| the cover | term | 5h (#s-math) |
| the cushion | term | 3a (#s-engines); 3e (#s-decision); 4a (#s-ops); 5j (#s-self) |
| the dashboards | term | 3i (#s-dash); B (#s-guide) |
| the dial | term | 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3d (#s-dial); 3e (#s-decision); 4a (#s-ops); B (#s-guide); C (#s-problem); G (#s-disclose) |
| Distribution / Specialized | organism | C (#s-problem) |
| do no harm | term | 2b (#s-answer); 3c (#s-desk); C (#s-problem); G (#s-disclose) |
| the edge | term | 2c (#s-board); 3a (#s-engines) |
| Energy / Facility / Industrial | organism | 3c (#s-desk); C (#s-problem) |
| the engine that stands | term | 2b (#s-answer); 3a (#s-engines); 3b (#s-feed); 4a (#s-ops); 4e (#s-orch); 4f (#s-stacks); 4g (#s-github); 5a (#s-proof); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5h (#s-math); B (#s-guide); C (#s-problem); G (#s-disclose) |
| evidence classes P, L, S | term | 1 (#s-health); 2a (#s-bottom); 2b (#s-answer); 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3d (#s-dial); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3h (#s-verdict); 3i (#s-dash); 4a (#s-ops); 4b (#s-runs); 4c (#s-live); 4d (#s-cloud); 4e (#s-orch); 4f (#s-stacks); 5a (#s-proof); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); 5j (#s-self); B (#s-guide); C (#s-problem); E (#s-monlist); G (#s-disclose) |
| factory profile | term | B (#s-guide); G (#s-disclose) |
| the factory tune | term | 1 (#s-health); 3c (#s-desk); 4f (#s-stacks); B (#s-guide); G (#s-disclose) |
| fail up | term | 5h (#s-math); B (#s-guide) |
| family | term | 2c (#s-board); 3b (#s-feed); 5e (#s-fleet); B (#s-guide) |
| the fast checks | term | 3d (#s-dial); 4a (#s-ops); C (#s-problem) |
| the fingerprint and its digest | term | 1 (#s-health); 3b (#s-feed); 5a (#s-proof); 5b (#s-cpp); 5h (#s-math); B (#s-guide); G (#s-disclose) |
| the four pieces | term | B (#s-guide) |
| Four Stacked | organism | B (#s-guide) |
| GAIN | term | 2a (#s-bottom); 2b (#s-answer); 2c (#s-board); 2d (#s-loss); 3d (#s-dial); 3f (#s-plane); 3h (#s-verdict); 4a (#s-ops); 4c (#s-live); 4d (#s-cloud); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| GAINING | term | 2a (#s-bottom); 2b (#s-answer); B (#s-guide) |
| the give-back trial | term | 1 (#s-health); 3c (#s-desk); 3h (#s-verdict); 4a (#s-ops); 5a (#s-proof); 5b (#s-cpp); B (#s-guide); C (#s-problem) |
| golden signals | term | 3b (#s-feed); C (#s-problem) |
| governor request | term | 1 (#s-health) |
| the grid | term | 2b (#s-answer); 5a (#s-proof); 5c (#s-scn); 5e (#s-fleet); 5g (#s-master); B (#s-guide); G (#s-disclose) |
| h | term | 3g (#s-brain) |
| harness | term | 3a (#s-engines); 3b (#s-feed); 3f (#s-plane); 3g (#s-brain); 4d (#s-cloud); 4f (#s-stacks); 5a (#s-proof); 5b (#s-cpp); 5f (#s-lab); 5h (#s-math); B (#s-guide); D (#s-read); G (#s-disclose) |
| health | term | 3g (#s-brain); 4a (#s-ops); 5d (#s-whole) |
| the heartbeat | term | 1 (#s-health); 3a (#s-engines); 3c (#s-desk); 3d (#s-dial); 3i (#s-dash); 4a (#s-ops); 4b (#s-runs); 5h (#s-math); B (#s-guide); C (#s-problem); G (#s-disclose) |
| the heat debt | term | 3a (#s-engines); 5h (#s-math); B (#s-guide) |
| the immune system | term | 3a (#s-engines); 3c (#s-desk); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| the injection | term | 3c (#s-desk); 5a (#s-proof); 5b (#s-cpp); 5c (#s-scn); 5i (#s-fail); B (#s-guide) |
| the injection grid | term | 5c (#s-scn); B (#s-guide) |
| the jump generator | term | 1 (#s-health); 5a (#s-proof); 5b (#s-cpp); B (#s-guide) |
| k[d] | term | 5h (#s-math); B (#s-guide) |
| k[p] | term | 5h (#s-math) |
| the key | term | 2a (#s-bottom); 2e (#s-status); 3d (#s-dial); 3i (#s-dash); 4a (#s-ops); 4d (#s-cloud); 4f (#s-stacks); 5c (#s-scn); 5d (#s-whole); B (#s-guide); C (#s-problem); D (#s-read) |
| the kill switch | term | 1 (#s-health); 2c (#s-board); 3b (#s-feed); 3c (#s-desk); 3e (#s-decision); 3f (#s-plane); 3i (#s-dash); 5g (#s-master); 5h (#s-math); B (#s-guide) |
| knob | term | 1 (#s-health); 2d (#s-loss); 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3h (#s-verdict); 3i (#s-dash); 4a (#s-ops); 4f (#s-stacks); 5a (#s-proof); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); B (#s-guide); D (#s-read); E (#s-monlist); G (#s-disclose) |
| the lease | term | 1 (#s-health); 3a (#s-engines); 3f (#s-plane); 4a (#s-ops); 5e (#s-fleet); 5h (#s-math); B (#s-guide) |
| lift-off | term | 3g (#s-brain); 5h (#s-math); B (#s-guide) |
| the line | term | 3a (#s-engines); 3c (#s-desk); 3f (#s-plane); 3g (#s-brain); 4a (#s-ops); 4b (#s-runs); 4c (#s-live); 4f (#s-stacks); 5a (#s-proof); 5c (#s-scn); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); 5j (#s-self); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| Live Organism | organism | 3a (#s-engines); 3b (#s-feed); 3f (#s-plane); 5f (#s-lab); 5g (#s-master); 5h (#s-math); B (#s-guide) |
| the live tuning engine | term | G (#s-disclose) |
| LOSS | term | 2a (#s-bottom); 2b (#s-answer); 2c (#s-board); 2d (#s-loss); 2e (#s-status); 3c (#s-desk); 3d (#s-dial); 3f (#s-plane); 3h (#s-verdict); 4a (#s-ops); 4c (#s-live); 4d (#s-cloud); 4f (#s-stacks); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| the max | term | 3a (#s-engines); 3c (#s-desk); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3h (#s-verdict); 4c (#s-live); 4d (#s-cloud); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); B (#s-guide); G (#s-disclose) |
| Mechanism Knobs | term | 1 (#s-health); B (#s-guide) |
| the model gate | term | 3h (#s-verdict); G (#s-disclose) |
| modelled | term | 3a (#s-engines); 3d (#s-dial); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3h (#s-verdict); 4a (#s-ops); 4c (#s-live); 4d (#s-cloud); 4f (#s-stacks); 5a (#s-proof); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| the monitor wall | term | 0 (#s-wall); 1 (#s-health); 3a (#s-engines); 3i (#s-dash); 4a (#s-ops); 4d (#s-cloud); 4f (#s-stacks); 5a (#s-proof); 5b (#s-cpp); 5g (#s-master); 5h (#s-math); B (#s-guide); E (#s-monlist); G (#s-disclose) |
| Monte Carlo | term | 1 (#s-health); 5a (#s-proof); B (#s-guide) |
| muscle | term | 1 (#s-health); 2b (#s-answer); 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3h (#s-verdict); 3i (#s-dash); 5b (#s-cpp); 5e (#s-fleet); 5f (#s-lab); 5g (#s-master); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| native | term, arm | 1 (#s-health); 2a (#s-bottom); 2b (#s-answer); 2c (#s-board); 2d (#s-loss); 2e (#s-status); 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3d (#s-dial); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3h (#s-verdict); 3i (#s-dash); 4a (#s-ops); 4b (#s-runs); 4c (#s-live); 4d (#s-cloud); 4e (#s-orch); 4f (#s-stacks); 5a (#s-proof); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5g (#s-master); 5h (#s-math); 5i (#s-fail); 5j (#s-self); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| native's colour | term | 1 (#s-health); 3a (#s-engines); 3b (#s-feed); 3f (#s-plane); 3i (#s-dash); 4d (#s-cloud); 5g (#s-master); B (#s-guide); D (#s-read) |
| the nervous system | term | 3a (#s-engines); 3e (#s-decision); 3g (#s-brain); 4c (#s-live); 5b (#s-cpp); 5h (#s-math); B (#s-guide); D (#s-read); G (#s-disclose) |
| observer | term | 3i (#s-dash) |
| Omni index | term | 2b (#s-answer); B (#s-guide); D (#s-read) |
| Omni-Compass | term | 1 (#s-health); 2a (#s-bottom); 2b (#s-answer); 2c (#s-board); 2d (#s-loss); 2e (#s-status); 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3d (#s-dial); 3e (#s-decision); 3f (#s-plane); 3g (#s-brain); 3h (#s-verdict); 3i (#s-dash); 4a (#s-ops); 4b (#s-runs); 4c (#s-live); 4d (#s-cloud); 4e (#s-orch); 4f (#s-stacks); 5a (#s-proof); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5g (#s-master); 5h (#s-math); 5i (#s-fail); 5j (#s-self); B (#s-guide); C (#s-problem); D (#s-read); E (#s-monlist); G (#s-disclose) |
| Omni-Compass on native | term, arm | 1 (#s-health); 2b (#s-answer); 3c (#s-desk); 3f (#s-plane); 3i (#s-dash); 4a (#s-ops); 5c (#s-scn); 5d (#s-whole); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| Omni-Compass's blue | term | 2c (#s-board); 3a (#s-engines); 3b (#s-feed); 3e (#s-decision); 3f (#s-plane); 3i (#s-dash); 4d (#s-cloud); 4g (#s-github); 5d (#s-whole); B (#s-guide); D (#s-read) |
| one pedal | term | 3c (#s-desk); 4a (#s-ops); B (#s-guide); G (#s-disclose) |
| the orchestra | term | 4e (#s-orch); 5d (#s-whole); 5e (#s-fleet); B (#s-guide) |
| Orchestra Organism | organism | 4e (#s-orch); 5d (#s-whole); 5e (#s-fleet); B (#s-guide) |
| the organism | term | 1 (#s-health); 2b (#s-answer); 3a (#s-engines); 3b (#s-feed); 3e (#s-decision); 3f (#s-plane); 3i (#s-dash); 4e (#s-orch); 4f (#s-stacks); 5b (#s-cpp); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5g (#s-master); 5h (#s-math); B (#s-guide); C (#s-problem); G (#s-disclose) |
| organisms stacked | term | 5c (#s-scn) |
| the organs and their grants | term | 3a (#s-engines); 3b (#s-feed); 3c (#s-desk); 3e (#s-decision); 3g (#s-brain); 4c (#s-live); 5a (#s-proof); 5h (#s-math); B (#s-guide); C (#s-problem) |
| OVER THE LINE | term | 4a (#s-ops); 5c (#s-scn); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read) |
| Physics / Robotics / Autonomous | organism | 3c (#s-desk); C (#s-problem) |
| piece 1, the state and the basin | term | 3a (#s-engines); 3g (#s-brain); 5a (#s-proof); 5h (#s-math); B (#s-guide) |
| piece 2, the basin's potential and flow | term | 3g (#s-brain) |
| piece 3, the bath | term | 3g (#s-brain); 5a (#s-proof) |
| piece 4, the governor's law | term | B (#s-guide) |
| power given | term | 2b (#s-answer); 2c (#s-board); 2d (#s-loss); 3d (#s-dial); 3e (#s-decision); 3f (#s-plane); 4a (#s-ops); 4c (#s-live); 4d (#s-cloud); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| Prometheus Metrics | term | 3b (#s-feed); 3d (#s-dial); 3i (#s-dash); 4g (#s-github); B (#s-guide); E (#s-monlist) |
| push | term | 4d (#s-cloud); 5h (#s-math); B (#s-guide) |
| the raw change and the word | term | 2a (#s-bottom); 2b (#s-answer); 2d (#s-loss); 4a (#s-ops); B (#s-guide); D (#s-read) |
| realm | term | 3a (#s-engines); 3b (#s-feed); 3e (#s-decision); 3g (#s-brain); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| REDLINING | term | 2a (#s-bottom); 2b (#s-answer); B (#s-guide) |
| the reflex rule | term | 3a (#s-engines); 3d (#s-dial); 5h (#s-math); B (#s-guide) |
| the release gate | term | 3c (#s-desk); 3e (#s-decision); 4c (#s-live); 5h (#s-math) |
| Restore factory profile | term | B (#s-guide) |
| Return to native | term | B (#s-guide) |
| RK4 | term | 1 (#s-health); 3a (#s-engines); 5a (#s-proof); 5h (#s-math); B (#s-guide) |
| the runs disagree | term | 2c (#s-board); 2d (#s-loss); 2e (#s-status); 5e (#s-fleet); D (#s-read) |
| the seven organisms | term | 3a (#s-engines); 5e (#s-fleet); B (#s-guide) |
| shown, not judged | term | 5e (#s-fleet); D (#s-read) |
| the snapshot | term | 3a (#s-engines); 5h (#s-math) |
| Spine | organism | 1 (#s-health); 3a (#s-engines); 3c (#s-desk); 5h (#s-math); B (#s-guide) |
| the spine | term | 1 (#s-health); 3a (#s-engines); 3c (#s-desk); 5h (#s-math); B (#s-guide) |
| the stack | term | B (#s-guide) |
| STEADY | term | 2a (#s-bottom); 2b (#s-answer); 2c (#s-board); 2d (#s-loss); 3d (#s-dial); 3f (#s-plane); 3h (#s-verdict); 4a (#s-ops); 4c (#s-live); 4d (#s-cloud); 4f (#s-stacks); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| the stress-test model | term | 3a (#s-engines); 3e (#s-decision); 3f (#s-plane); 5f (#s-lab); 5h (#s-math); B (#s-guide) |
| supervisory governor | term | 1 (#s-health); 3a (#s-engines); 3c (#s-desk); 3d (#s-dial); 3i (#s-dash); 4a (#s-ops); 4b (#s-runs); 4c (#s-live); 4e (#s-orch); 4f (#s-stacks); 5b (#s-cpp); 5c (#s-scn); 5d (#s-whole); 5e (#s-fleet); 5f (#s-lab); 5g (#s-master); 5h (#s-math); 5j (#s-self); B (#s-guide); C (#s-problem); E (#s-monlist); G (#s-disclose) |
| tanh | term | 5h (#s-math) |
| template | term | 5e (#s-fleet) |
| the three places Omni-Compass lives | term | 2b (#s-answer); 5d (#s-whole); 5h (#s-math); B (#s-guide) |
| three runs A, B and C | term | 2a (#s-bottom); 2b (#s-answer); 2c (#s-board); 3d (#s-dial); 3e (#s-decision); 3f (#s-plane); 3i (#s-dash); 4b (#s-runs); 4c (#s-live); 4d (#s-cloud); 4e (#s-orch); 4f (#s-stacks); 4g (#s-github); 5c (#s-scn); 5d (#s-whole); 5h (#s-math); 5i (#s-fail); B (#s-guide); C (#s-problem); D (#s-read) |
| the tower | term | 1 (#s-health); B (#s-guide) |
| the traffic signal | term | 0 (#s-wall); 2a (#s-bottom); B (#s-guide) |
| the tune-down | term | 3c (#s-desk); 3e (#s-decision); 4d (#s-cloud); 5b (#s-cpp); 5h (#s-math); B (#s-guide); G (#s-disclose) |
| the twin | term | 3a (#s-engines); 5h (#s-math); B (#s-guide) |
| the two antagonist forces | term | 3a (#s-engines); 3e (#s-decision) |
| the two-way plug | term | 3a (#s-engines); 3e (#s-decision); 3i (#s-dash); 4a (#s-ops); 4c (#s-live); 5a (#s-proof); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read) |
| Variation Switchboard | term | 1 (#s-health); 5c (#s-scn) |
| the verdict | term | 2a (#s-bottom); 2d (#s-loss); 3a (#s-engines); 3b (#s-feed); 3h (#s-verdict); 4a (#s-ops); 4c (#s-live); 4f (#s-stacks); 5a (#s-proof); 5b (#s-cpp); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| Whole Organism | organism | 3i (#s-dash); 4f (#s-stacks); 5d (#s-whole); 5g (#s-master); 5h (#s-math); B (#s-guide); C (#s-problem); D (#s-read); G (#s-disclose) |
| Whole Tower | organism | B (#s-guide) |
| work waiting in line | term | 3b (#s-feed); B (#s-guide) |
| κ | term | 3g (#s-brain); 5h (#s-math) |
| ν | term | 3g (#s-brain); 5h (#s-math) |
| ρ* | term | 5h (#s-math) |
| σ | term | 3c (#s-desk); 3g (#s-brain); 3h (#s-verdict); 5a (#s-proof); 5h (#s-math) |

Not printed in the page's own words at this build (defined above, not yet on the page): a cell's reference; candidate profile; contract, this decision; cruise; custom profile; defensive system; governing engine; the heartbeat's seven buttons; the injection batch; live tuning bench; the monitor wall stack; native baseline; preset; protocol 4; the seal; the yardstick.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
