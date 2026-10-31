# The main engine and the tuning bench: one tuned engine, every knob turnable

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's order of 22 October, evening: the live benchmark engine and the main benchmark engine are two different things. The live
engine gives the buttons, knobs and monitors that turn every muscle and mechanism up or down, in or out, on or off; the real
benchmarks prove one engine at one tune, and every page must say that turning any knob can change every metric in any
direction. The main engine's tune is not a guess: it is the tune found, by measuring every gauge across the knobs, to serve the
organism best, read against native and against every tune tried. This page states both and formalizes the second. Its
rule is in code (`tools/tune_study.py`, tested by `tests/test_tune_study.py`); its first search runs in our own models
(evidence class S) and is read on its own page in `results/model_gate/` when it finishes. Run and scored by The Omni-Compass LLC's own code.
No outside party has reviewed or approved these results.

## 1. Two things, never one

**The main engine** is the engine that stands (omni-v23, `OMNI_V23.json`, `python3 tools/omni_version.py`) at its factory tune:
the settings The Omni-Compass LLC ships, frozen and fingerprinted. For the Kubernetes governor the tune is the full decision
every 60 s with the fast checks every 5 s; the compass law at the max on a cluster of one's own (its balance point 0.3) and at
the tune-down in a cloud (0.4, the machines alone, a bill never bigger than native's); the verdict's 2% allowance on a
give-back trial of 20 minutes; the cruise wait of 120 s, never under two readings; every muscle on its own card where one was
found (`realms/muscle_cards_v5.csv`) and the engine's setting for the rest. **Every published benchmark result is this one
engine at this one tune**, on the systems, loads and harness that benchmark names, native against Omni-Compass on top of native.

**The tuning bench** is the live benchmark engine page (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, read by the Live Benchmark Engine Manual) with
the control panel's buttons (`tools/omni_control.py`): a live tuning engine. Every knob, button and monitor there can be turned
in real time: the heartbeat at its six stops, 10, 15, 30, 60, 90 and 120 s (any value from 5 to 120 s on the control panel), the dial between the max and the tune-down, the pedal, each muscle driven or left
native, up or down, in or out, minus or plus. The bench shows the mechanism of action at each setting with native alone, with
Omni-Compass on top of native, or both side by side. What it shows at any setting other than the factory tune demonstrates the
engine's range. It is not a benchmark result, and nothing read on the bench is published as one.

**Why both exist.** Omni-Compass is an engine, and an engine has many parts that can be turned: on a car's engine the mixture at
the carburettor, the intake, the exhaust, the timing of the firing, the pistons' stroke; on this one the beat, the balance point
and its cushions, the dial, the trial's length and allowance, the waits, each muscle's card, which muscles it drives at all.
Turning any one part changes what the engine delivers, and can move every metric (work, speed, waits, misses, machines,
energy, wear) up or down, in any direction a tuner chooses. That range is the engine's versatility: one engine that can be put
in many vessels (any organism, realm, stack or cluster, whole or fragmented), tuned many ways, and made to produce many
outputs. A tune other than the factory tune is the tuner's own configuration; its results are its own, and they are run again,
native against Omni-Compass, before anything is claimed for it.

## 2. The tune as a mathematical object

**The tune.** θ = (θ₁, …, θₖ) ∈ Θ = Θ₁ × ⋯ × Θₖ, one coordinate a knob and Θᵢ its admissible range (the beat P ∈ [5, 120] s,
the balance point c ∈ (0, 1), …). The factory tune is one point, θ*.

**A run.** An organism S under a load L, run once for each seed s ∈ Ω (the plant's random draw; Ω the set of seeds), gives native's gauge vector
g⁰(s) ∈ ℝⁿ, and Omni-Compass on top of native at tune θ gives g(θ, s) ∈ ℝⁿ, on the same seed.

**The one key.** Each gauge j has an aim aⱼ (`tools/readings.py`): time waited, missed or failed, where lower serves; work,
where higher serves; a resource spent or held, which is power. The paired difference dⱼ(θ; s) = gⱼ(θ, s) − g⁰ⱼ(s) has a mean
d̄ⱼ over the seeds and a 95% interval [ℓⱼ, uⱼ] by Student's t on |Ω| − 1 degrees of freedom (`omnicompass/student_t.py`). Its
size is rⱼ(θ) = d̄ⱼ ⁄ ḡ⁰ⱼ, and the reading Rⱼ(θ), by the founder's order of 24 October (a change of 0.5% or more either way is a
change), is STEADY when |rⱼ(θ)| < 0.005; otherwise GAIN when rⱼ lies on the side the aim serves, and on the other side LOSS for a time
waited, missed or failed or for work and power given for a resource. The interval [ℓⱼ, uⱼ] is printed beside the word and says
how far the seeds' noise reaches; the word does not wait on it. The same key
reads one tune against another, θ′ against θ, with g(θ, s) in the place of g⁰(s).

**The admissible set** (do no harm, in the strict form the engine that stands keeps, `DISCLOSURES.md` section 3):

  A = { θ ∈ Θ : Rⱼ(θ) ≠ LOSS for every gauge j, and every muscle within its own limit },

and in a cloud also R[bill] (θ) ≠ power given: the same work for a bill never bigger than native's.

**What a tune is for.** The max serves the organism's output (its work, and the time it waits, misses or fails) and gives power
to buy it; it never shaves energy for its own sake. Let Jₛ be the service gauges (in a cloud the bill joins them, its aim
lower). On A the tunes are ordered lexicographically by

  F(θ) = ( |{ j ∈ Jₛ : Rⱼ(θ) = GAIN }| ,  Σ { |rⱼ(θ)| : j ∈ Jₛ, Rⱼ(θ) = GAIN } ),

the number of service gauges that read GAIN against native, then their summed improvement; the energy and the machines spent are
shown beside, as power given.

**Dominance.** θ′ dominates θ, written θ′ ≻ θ, when, read against θ seed by seed, no gauge of Jₛ reads LOSS (in a cloud, no
rise in the bill) and at least one reads GAIN. Nothing is traded: θ′ may not buy one service gauge with another.

**The main tune stands** on a searched set Θₛ ⊆ Θ when θ* ∈ A and no θ ∈ Θₛ ∩ A has θ ≻ θ*. In words: the factory
tune harms no gauge against native, and no admissible tune that was tried reads GAIN against it on one service gauge and
LOSS on none.

**What follows, and what does not.**

1. The claim is relative to Θₛ, to the gauges, to the seeds and to the model it was read in. It is non-dominance in the
   searched set, not a global optimum over Θ, which is continuous; no finite search proves a global optimum, and none is claimed.
2. On the engine that stands nothing is traded between service gauges: dominance asks for no LOSS on any of them. The trade
   between muscles judged on the whole organism, which do no harm allows, is the next version's work (`DISCLOSURES.md`, section 3).
3. Power given is shown, never minimized by the max. In a cloud the bill is a service aim, so a tune that raises it is not
   admissible there.
4. The search runs on development seeds and never on the seeds a version is judged on. A tune that dominates the factory tune is
   only a candidate: it is read in the model gate on the untouched seeds 1 to 8 against the engine that stands
   (`tools/model_gate.py`), lands as the next version only where it reads no LOSS there against that engine and against native,
   and is then run three times on every benchmark. Picking the best of many tunes on one set of seeds and reading it again on
   another is what keeps a lucky draw from being shipped.
5. A real benchmark reads the tune that ran. A tune found best in the models is a promise to test, never a result before its
   runs exist (evidence classes: P a physical meter, L live software, S our own models).

## 3. The rule in the code

`tools/tune_study.py` runs every tune of a declared grid on the model's plant that moves every 5 s (`tools/model_gate.py`, whose
worker passes any of the governor's own arguments through `--ctl`), keeps every job's reading so a stopped search resumes,
and applies the rule of section 2 in `judge()`: `admissible`, `dominates_main`, the rank by F, and `stands`. Its tests hold the
rule on readings built for the purpose: a tune with any LOSS against native is not admissible; in a cloud a bigger bill is
not admissible; a tune with a service GAIN and no LOSS dominates, power given beside it; the main tune stands when nothing
dominates it.

The same rule already chose the part of the factory tune that is set muscle by muscle. `tools/tune_cards.py` searched each
muscle's own settings on development seeds (7100 to 7110) and kept a card only where it read beyond the noise on misses, work
or speed against the engine's setting, moved none of the three the other way, and fell behind native on no seed and under no
load; each kept card was read again on other development seeds (7200 to 7210) under the same rule before it was written
(`realms/muscle_cards_v5.csv`, 364 muscles; every other muscle runs the engine's setting; `docs/FORMAL_V5.md`, section 5). The
preregistered seeds were never read by either search.

## 4. The first search (written before its run, 22 October, evening)

- **Engine.** omni-v17 (digest `7c937d09e4031cc7`), the Kubernetes governor in the model cluster.
- **Settings.** The kind benchmark's (the compass law at the max, every autoscaler sensed) and the cloud's (the compass law at the
  tune-down, the machines alone), each on the plant that moves every 5 s.
- **Knobs and values.** The beat P ∈ {15, 30, 60, 75, 90, 120} s; the compass's balance point c ∈ {0.2, 0.3, 0.4} in the kind
  setting and {0.3, 0.4, 0.5} in the cloud's: eighteen tunes in each setting, the factory tune among them (60 s; 0.3 and 0.4).
  The beats 5 and 10 s were read in the ladder (`results/model_gate/V17_LADDER.md`): in the kind setting they read the minutes
  over the line 18.4% lower than 60 s and the autoscaler's shortfall 5.8% and 6.0% lower (GAIN) for 3.5 and 2.2 times its
  processor, and the pods waiting for a place LOSS against native as every beat does; in the cloud's setting no service gauge
  reads GAIN against 60 s. They are left out of this first grid for its running time (a modelled day at 5 s takes about three
  times as long as at 60 s) and join the second search.
- **Seeds.** 101 to 108, one day each, native on the same seeds; the gate's seeds 1 to 8 are kept for the reading on untouched seeds.
- **Gauges.** The model's: machine-hours, energy per core-hour, the pods waiting for a place, the autoscaler's shortfall, the 95th
  percentile, the minutes over the line. Jₛ: the pods waiting, the 95th percentile, the minutes over the line and the
  autoscaler's shortfall; in the cloud's setting the machine-hours as well.
- **Outcome.** Its own page in `results/model_gate/`, written by `tools/tune_study.py --judge`: each tune admissible or not, dominating the factory tune or not, the rank,
  and whether the factory tune stands in each setting. A dominating tune goes to the model gate on seeds 1 to 8; a factory
  tune that is not admissible is root-caused like any LOSS. The founder is told what it read either way.
- **Next searches, in the same rule.** The cruise wait and the trial's length and allowance; the dwell and the wait after an
  addition counted in readings that agree rather than in seconds at the fast beats (the live-engine session's finding of
  22 October); the floor check and a warm reserve in the cloud (the same session's); each muscle's card at each beat (the
  founder's "each beat its own combination").

## 5. The common language: the engine, its profiles, the bench and the bill (the founder's master specification of 24 October)

Omni-Compass consists of a **governing engine**, its **muscle adapters**, a **complete configuration profile** and a **validation
harness**. The factory profile specifies the governing rules, gains, margins, decision interval and other default settings. It is
selected after the mechanisms are verified, candidate configurations are tested together, and the chosen configuration is validated
on fresh workloads. Freezing the factory profile fixes the released rules and default tuning; the engine's internal state, commands
and resource allocations continue responding to changing conditions. The live engine is an interactive tuning bench: its controls
expose the governing mechanism and show how adjustments affect the connected system. An adjustment produces an identifiable active
configuration; it becomes a new factory configuration only after validation and a new release declaration. Every result identifies
the engine version, configuration, hardware or model, workload and measurement boundary that produced it.

| Term | Exact meaning | Where it is in this repository |
|---|---|---|
| Governing engine | The executable mathematical rules that transform observations and internal state into governing decisions. | the fingerprinted files of the engine that stands (`OMNI_V18.json`, `tools/omni_version.py`) |
| Native baseline | The system's documented configuration and behavior without Omni-Compass governing it. | each benchmark's native arm, as its project ships it |
| Factory profile | The complete, versioned set of Omni-Compass default settings shipped together. | θ*, sections 1 and 2: the engine's defaults and `realms/muscle_cards_v5.csv` |
| Candidate profile | A proposed combination of settings undergoing evaluation. | a tune of the search grid (`tools/tune_study.py`) or a candidate engine in the model gate (`tools/model_gate.py`) |
| Active profile | The settings actually governing the current run. | the governor's own audit of its arguments; the live engine's bench line (section 1 of the page's wall) |
| Custom profile | An identifiable configuration differing from the released factory profile. | any knob turned on the bench or set on the control panel (`tools/omni_control.py`) |
| Live tuning bench | The interface that operates the engine's controls and displays their effects through the connected backend. | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html` with `tools/omni_control.py` |
| Harness | The machinery that supplies workloads, executes comparisons, checks requirements and records results. | `scripts/kind_bench.sh`, the paired cloud scripts, `tools/live_reps.py`, `tools/confirm_abc.py`, `cpp/` |
| Muscle | A specific controllable mechanism, with its own actuator, observations, limits and read-back. | `omni_controller/muscles.py`, the catalog `realms/` |
| Organism | The complete declared system whose useful output, health and resource costs are assessed together. | the seven organisms and the orchestra (`docs/THE_SPINE.md`, `tools/run_realms_v5.py`) |
| Nervous system | Observation, signal propagation, coordination and authority pathways. | the governor's reads, its audit, the kill file and the control panel's roles |
| Defensive system | Constraint enforcement, fault detection, containment, recovery and restoration mechanisms. | the compass's wall and fail-up, the verdict, the lease's walk back, the kill switch (`omnicompass/master.py`) |
| Health | Explicit operating requirements: correctness, service limits, resource bounds and applicable hardware limits. | each benchmark's service line and each muscle's own limit |

The physiological terms are engineering analogies; each points to concrete code, signals, actuators and checks, named in the right
column.

**Fixed tuning, continuously changing behavior.** Let x be the governed system's state, z the governor's internal state, y its
observations, θ the complete configuration profile and Δ the full governing decision interval, Δ ∈ {10, 15, 30, 60, 90, 120} s on
the bench's six buttons (60 s the factory's). At decision k:

```
y[k] = h(x[k]),   z[k+1] = F[θ](z[k], y[k]),   u[req][k] = G[θ](z[k], y[k]),   u[cmd][k] = Π[C](u[req][k]),

x[k+1] = Φ(x[k], u[ack][k], w[k]),
```

where G[θ] supplies the governing authority, Π[C] enforces the applicable constraints (C holds the operating limits: each muscle's own
range, the do-no-harm floor at native, the operator's caps), u[ack] is the command the system acknowledged (read back), and w is the
workload and its disturbances. The system evolves on the command that actually landed: the requested u[req], the commanded u[cmd] and
the acknowledged u[ack] are kept apart in the governor's audit. After release θ = θ* is fixed while x, z and y keep changing: that is
how one fixed factory tune governs a changing workload.

**"One setting" means one complete profile.** The factory profile is a configuration vector, θ = (Δ, the compass's balance point
and cushions, the dial, the trial's length and allowance, the waits, each muscle's card, which muscles are driven, …), more than the
choice of a heartbeat. Its coordinates are evaluated jointly, because changing one mechanism can affect others; the search
establishes the best validated combination under a declared workload, hardware and service contract. Two benchmark objectives stay
explicit, and every reported result names its objective and its exact profile:

  maximize P(θ), the healthy production (work done inside every health requirement), or
  minimize B(θ) ⁄ P(θ), the cost of the production completed.

**The sequence for establishing the factory baseline.**

1. Verify the mechanisms: observations, units, authority, actuation, read-back, limits and recovery.
2. Exercise the six governing intervals and the relevant knob combinations.
3. Tune on development workloads, examining interactions between muscles.
4. Validate the selected profile on fresh workloads, including bursts, sustained demand and declared failure conditions.
5. Record every adverse result and resolve whether the candidate meets the release requirements.
6. Freeze the complete factory profile, its engine identity and its validation receipts.
7. Verify the corresponding implementations and adapters, the C++ harness included.
8. Release that identified package as the factory baseline: the best validated factory profile for the declared operating
   conditions, which gives "optimal" an assessable meaning.

The final factory tune is not yet established: the engine that stands carries the factory profile of sections 1 and 2, and the
searches of section 4 continue under this sequence.

## 6. The same behavior in C++ and in every port

Python, C++ and the browser port share one behavioral contract: the same profile values, meanings and units; the same governing
intervals and time-based rules; the same authority and constraint decisions; the same handling of stale observations, refused
commands and recovery; exact agreement for discrete decisions, and predefined numerical tolerances where floating-point arithmetic
requires them. The C++ twins are checked against the Python to the last bit on every push (`tools/seal.py`, `results/SEAL.json`,
the parity tests under `tests/test_cpp_*`, each with a negative control). A release record names the engine's fingerprint, the
profile, the implementations and their parity receipts: a matching fingerprint establishes identity, and the validation receipts
establish what that identified implementation demonstrated.

## 7. What the bench shows, and its two controls

The live engine shows the architecture (native, Omni-Compass on top of native, or Omni-Compass direct); the deployment route
(on-site hardware or cloud); the engine and profile identity (factory, candidate or custom); the cadence, the six buttons; each
muscle's controls with their bounds and authority; the actuation feedback (the requested setting, the accepted one, and changes
pending or refused); the system's response (useful output, service health and whole-workload cost where available); and the backend
(simulation, running software, attached hardware or recorded playback). The controls operate the stated backend and show its
response; a physical energy reading requires an identified meter or device counter.

| Control | Effect |
|---|---|
| Restore factory profile | Reapply the released Omni-Compass configuration. |
| Return to native | Hand governance back and restore the recorded native settings as supported by the adapter (the kill switch). |

## 8. The first financial result: the whole-workload bill

For each deployment route r (on-site hardware; cloud) and arm a (native, Omni-Compass on top of native, Omni-Compass direct), the bill
is the sum of its non-overlapping cost components inside the declared boundary:

  Bᵣ(a) = Σᵢ cᵣ,ᵢ(a),   and the saving   Sᵣ(a) = 1 − Bᵣ(a) ⁄ Bᵣ(native),

for a positive native cost and a valid, matched workload comparison. The two headline views are on-site hardware (native total →
Omni-Compass total → percentage saving) and the cloud (the same). A component's percentage is a supporting measurement; the bill's
percentage comes from adding the actual costs within the boundary, and a missing price or an incomplete workload stays visibly
unresolved. The README and the live engine page carry both views at the top (`tools/headline.py`), each read from the engine that
stands's own runs.

**Where each explanation lives.** The README explains the engine, the factory profile, the tuning bench and the two deployment
routes at once; the Operator's Manual, starting from the factory profile, making a custom one, reading the command acknowledgements
and using the two restoring controls; the Owner's Manual, healthy production, choosing the configuration, the whole-workload benefit
and the scope of validation (this page, bound in); the Live Engine Manual, every control, its backend, its effects, its limits and
the difference between the factory and the active settings; the C++ harness's documentation, the equations, units, profile loading,
timing, parity checks and release fingerprints (`cpp/`); the reading guide (`docs/HOW_TO_READ_THE_RESULTS.md`), the workload
contract, the measurement boundary, the profile's identity, the costs, the requirements and the rules for the words.

## 9. Where it is written

The disclosure of section 1 stands in `DISCLOSURES.md` section 3 (the factory tune), near the top of the README and of the
live benchmark engine page, and in all three manuals: the Operator's Manual (section 3.1, the factory tune and the bench, without the engine's internals), the Owner's Manual
(the tune and its mathematics, this page's sections 1 and 2) and the Live Benchmark Engine Manual (its opening: the page is a tuning bench).

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
