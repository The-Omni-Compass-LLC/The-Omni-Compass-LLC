# The factory profile, the live tuning bench and the bill: the common language

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

The founder's orders of 24 October 2026, late night: one complete factory-tuned profile becomes the packaged baseline, once every
mechanism is verified and every knob has been simulated and tuned together for the most benefit; "we ain't got to the basic yet";
the live benchmark engine shows the governing mechanism so that profile can be moved, demonstrated and studied; and every manual, instruction
and reading guide carries the same words for it. This page is the one place those words are written. The Operator's Manual, the
Owner's Manual, the Live Benchmark Engine Manual, the README, the live benchmark engine's glossary and the reading guide point here.

## 1. What Omni-Compass consists of

Omni-Compass consists of a **governing engine**, its **muscle adapters**, a **complete configuration profile** and a **validation
harness**.

The **factory profile** specifies the governing rules, gains, margins, decision interval and every other default setting. It is
selected after the mechanisms are verified, candidate configurations are tested together, and the chosen configuration is validated
on fresh workloads.

Freezing the factory profile fixes the released rules and default tuning. The engine's internal state, its commands and the
resources it allocates go on responding to changing conditions.

The **live benchmark engine** (`docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`) is an interactive tuning bench. Its controls expose the governing
mechanism and show how an adjustment moves the connected system. An adjustment produces an identifiable active configuration. It
becomes a new factory configuration only after validation and a new release declaration.

Every result identifies the engine version, the configuration, the hardware or model, the workload and the measurement boundary that
produced it.

**Where it stands today.** The released factory profile is omni-v23's (`OMNI_V23.json`, `python3 tools/omni_version.py`): the
governor's full decision every 60 s (`omni_controller/controller.py`, `--interval 60`), the fast checks every 5 s, every muscle on
the card found for it (`realms/muscle_cards_v5.csv`, kept only where it won twice and never fell behind native on any seed) and on
the engine's own setting otherwise. It is the profile every published result ran on. The best validated factory profile for the
declared operating conditions (section 6) has not yet been established: the joint search over every knob comes once every mechanism
is verified, and no other profile is released before it.

## 2. The words, each with its exact meaning

| Term | Exact meaning | Where it is in the repository |
|---|---|---|
| Governing engine | The executable mathematical rules that turn observations and internal state into governing decisions. | `omnicompass/` (the compass law, the core, the nervous system, the verdict), `omni_controller/controller.py`, its C++ twin `cpp/src/governor.cpp` |
| Native baseline | The system's documented configuration and behaviour with no Omni-Compass governing it: every muscle under its own native controller, as its vendor ships it. | the arm `native` in every benchmark; `realms/harness.py`, the plant and its native controller alone |
| Factory profile | The complete, versioned set of Omni-Compass default settings shipped together. | `OMNI_V19.json` (the fingerprint), the controller's defaults, `realms/muscle_cards_v5.csv` |
| Candidate profile | A proposed combination of settings under evaluation. | the live engine's "Try the candidate" (the best beat of a sweep); the model gate's candidates (`tools/model_gate.py`) |
| Active profile | The settings actually governing the current run. | the live engine's "active profile" line, with its fingerprint |
| Custom profile | An identifiable configuration that differs from the released factory profile. | any knob turned on the bench; its fingerprint names it; its results are its own |
| Live tuning bench | The interface that operates the engine's controls and displays their effects through the connected backend. | `docs/engine/OMNI_COMPASS_LIVE_ENGINE.html`, the main control panel |
| Harness | The machinery that supplies workloads, executes comparisons, checks requirements and records results. | `realms/harness.py`, `scripts/kind_bench.sh`, `tools/confirm_abc.py`, the workflows under `.github/workflows/` |
| Muscle | A specific controllable mechanism, with its own actuator, observations, limits and read-back. | a row of `realms/catalog_v5.csv`, its wiring in `docs/wiring_recipes.csv` |
| Organism | The complete declared system whose useful output, health and resource costs are assessed together. | `tools/run_realms_v5.py` (the spine, the realms, the four stacked, the tower), `tools/run_orchestra.py` |
| Nervous system | Observation, signal propagation, coordination and authority pathways. | `omnicompass/nervous_system.py`, `omnicompass/authority_contract.py` |
| Defensive system | Constraint enforcement, fault detection, containment, recovery and restoration. | the bone and the twins (`docs/FORMAL_V5.md` section 4), the lease's walk back, the kill switch (`omnicompass/master.py`) |
| Health | The explicit operating requirements: correctness, service limits, resource bounds and every applicable hardware limit. | the response-time line (`--slo-ms`), each muscle's limits, the power and heat lines |

The physiological words are engineering analogies. Each points to concrete code, signals, actuators and checks, as the third column
shows.

### The tools around Omni-Compass, in plain words

| The word | What it does | Who decides | Examples | Omni-Compass beside it |
|---|---|---|---|---|
| Observer | stores readings and draws them; raises an alert when a line is crossed | a person, after looking | Prometheus, Grafana, Datadog, New Relic, Dynatrace, Kibana, Splunk | beside it: its exporter serves Omni-Compass's readings; none of them moves a setting |
| Collector | gathers metrics, logs, traces and profiles and forwards them | nobody: it carries | Grafana Alloy, the OpenTelemetry Collector, node_exporter, Kepler | beside it: one way the readings travel; Omni-Compass's own pipeline also writes and reads each write back |
| Console | one screen to deploy, scale, restart and set rules across clusters | a person, by clicking or writing a rule | Rancher, Portainer, Lens, the OpenShift console | beside it: the rules set there are the native Omni-Compass sits on top of |
| Native controller | keeps one muscle at the rule it was given | its own fixed rule, one muscle at a time | the Pod Autoscalers, the Cluster Autoscaler, Karpenter, KEDA, GPU firmware, thermostats | underneath, always running; Omni-Compass moves their settings inside each muscle's limits |
| Automatic optimizer | watches a layer and changes its settings itself, mostly for a cloud bill | the product, within its layer | rightsizing and node optimizers for Kubernetes and the cloud | the comparable: benchmarked as native with it, then with Omni-Compass on top (`docs/THE_FIELD.md`) |
| Supervisory governor | reads the whole body every beat, decides with one law across every muscle, writes through a two-way plug, reads each write back, audits, hands back gradually, stops at the kill switch | Omni-Compass's brain, on top of every native controller | Omni-Compass | — |

## 3. The mathematics: a fixed tune governing a changing system

Let x be the governed system's state, z the governor's internal state, y its observations, θ the complete configuration profile,
and Δ the full governing decision interval. The public interval choices on the bench are

  Δ ∈ {10, 15, 20, 30, 60, 90, 120} s

(the controller itself takes any value from 5 to 120 s, `--interval`). At decision k, with tₖ₊₁ = tₖ + Δ, the general contract is

  y(k) = h(x(tₖ)) + ε(k)                        the observation, with its sensing delay and noise ε
  (u[req](k), z(k+1)) = G[θ](z(k), y(k), A(k))    the decision: the requested settings, inside the authority A(k)
  u[cmd](k) = Π[C](u[req](k))                       the constraints C(k): every muscle's own limits, the cover, never below native at the max
  u[ack](k) = R(u[cmd](k))                         the setting that actually landed, read back by the adapter
  x(tₖ₊₁) = Φ(x(tₖ), u[ack](k), w(k))             the system moves with the command that landed, under the workload and disturbances w

G[θ] is the governing engine at profile θ; A supplies the governing authority; C enforces the applicable constraints and holds the
operating limits; w is the workload. The system evolves with the command that actually landed, so the requested, the commanded and
the acknowledged settings are kept distinct and each is logged (the audit; a refused write is held, omni-v12).

After release,

  θ(k + 1) = θ(k) = θ[factory] for every k,

while x, z and u go on changing. That is how one fixed factory tune governs a changing workload.

## 4. "One setting" means one complete profile

The factory profile is a vector of settings,

  θ = (the rules, the gains, the margins and cushions, Δ, the dial, every muscle's card, …),

more than a choice of heartbeat. Its settings are evaluated jointly, because changing one mechanism can move others. The search
establishes the best validated combination under a declared workload, hardware and service contract. Two objectives are kept
explicit:

  maximise E[P(θ)] subject to Hⱼ(θ) ≤ Lⱼ for every health requirement j,

the most healthy production the system can deliver (the max, the default brain), or

  minimise E[C(θ) / P(θ)] subject to the same requirements,

what that completed production costs (the tune-down, the cloud's machines alone). P is the useful output (work done inside the
line), C the whole-workload cost inside the declared boundary, Hⱼ each health reading and Lⱼ its limit. Each reported result names
its objective and its exact profile.

## 5. The sequence that establishes the factory baseline

1. Verify the mechanisms: observations, units, authority, actuation, read-back, limits and recovery.
2. Exercise the six governing intervals and the relevant knob combinations.
3. Tune on development workloads, examining the interactions between muscles.
4. Validate the selected profile on fresh workloads, bursts, sustained demand and the declared failure conditions included.
5. Record every adverse result and resolve whether the candidate meets the release requirements.
6. Freeze the complete factory profile, its engine identity and its validation receipts.
7. Verify every corresponding implementation and adapter, the C++ harness included.
8. Release that identified package as the factory baseline.

The result is called **the best validated factory profile for the declared operating conditions**, which gives "optimal" an
assessable meaning. Today the repository is at step 1 and step 2 for the next profile (the heartbeat sweep and the beat ladder,
`results/model_gate/HEARTBEAT_SWEEP.md`, `results/model_gate/V17_LADDER.md`, class S); steps 3 to 8 come after the founder confirms the
mechanisms. Every engine version already passes the model gate (`tools/model_gate.py`) and the three-run rule before its results stand.

## 6. Carrying it into C++ and every other implementation

The Python, the C++ and the browser port share one behavioural contract: the same profile values, meanings and units; the same
governing intervals and time-based rules; the same authority and constraint decisions; the same handling of stale observations,
refused commands and recovery; exact agreement for discrete decisions, with tolerances fixed in advance where floating-point
arithmetic needs them. The seal holds the twins to it (`tools/seal.py`, `results/SEAL.json`, the parity tests under `tests/`), and
the live benchmark engine is held to the Python and the C++ on every build (`docs/engine/check_live_engine.py`).

A release record identifies the engine version and its fingerprint (`OMNI_V19.json`), the profile, the implementations' parity
receipts and the validation receipts. A matching fingerprint establishes identity; the validation receipts establish what that
identified implementation demonstrated.

## 7. What the live benchmark engine shows

- **Architecture:** native, or Omni-Compass on native; Omni-Compass is never by itself (the founder's order of 25 October).
- **Deployment route:** on-site hardware, or through the cloud.
- **Engine and profile identity:** factory, candidate or custom, with the profile's fingerprint.
- **Cadence:** the seven buttons, 10, 15, 20, 30, 60, 90 and 120 s.
- **Muscle controls:** each adjustment with its bounds and its governing authority.
- **Actuation feedback:** each decision's requested settings, those that landed as asked, those held at a muscle's limit, and those
  still moving toward their setting.
- **System response:** useful output, service health and the whole-workload cost where it is recorded.
- **Backend identity:** the page's own model (class S, modelled), running software (class L), attached hardware (class P) or a
  recorded playback, named on every monitor.

The controls operate the stated backend and show its response. A physical energy reading needs an identified meter or device
counter; the page's live model has neither and says so.

Two controls carry separate meanings:

| Control | Effect |
|---|---|
| Restore factory profile | Reapply the released Omni-Compass configuration. |
| Return to native | Hand governance back and restore the recorded native settings, as the adapter supports. |

Return to native is the reset (`tools/omni_control.py`, `POST /v1/reset`, the operator's role): every setting handed back
to native and the governor stopped, started again by an operator. The kill switch is a third control, separate from both:
for security and instant, re-armed only by two holders of the security role (`omnicompass/master.py`,
`tools/omni_switch.py`). On the live page the reset and the kill switch both end in native alone, and the page names which one was pressed.

## 8. The bill: the first financial result is the whole workload's

For each deployment route r, add its cost components inside the declared boundary, each counted once:

  C(r, a) = Σₖ c(r, a, k),

where a names the arm: native, or Omni-Compass on native. Then

  S(r, a) = (C(r, native) − C(r, a)) / C(r, native),

for a positive native cost and a valid, matched workload comparison. That gives the two headline views:

- **On-site hardware:** the total native cost → the total Omni-Compass cost → the percentage saved.
- **Through the cloud:** the total native cost → the total Omni-Compass cost → the percentage saved.

A component's percentage is a supporting measurement. The bill's percentage comes from adding the actual costs inside the declared
boundary. A missing price or an incomplete workload stays visibly unresolved: today only the cloud's compute is metered in money
(Azure, machine-hours at the list price, `results/live/AKS_BILL.md`); energy, machines, storage, network and operation carry no
recorded price, so neither route's total is resolved yet, and the live benchmark engine shows each component as unresolved beside its measured
change. The company's expected ranges for the three places Omni-Compass lives (`DISCLOSURES.md` section 9) are an expectation, never
a result.

## 9. Where this explanation is carried

| Document | What it carries |
|---|---|
| README | the engine, the factory profile, the tuning bench and the two deployment routes, at once |
| The Operator's Manual | starting from the factory profile, making a custom profile, reading the command acknowledgements, the two restoring controls |
| The Owner's Manual | healthy production, how a configuration is chosen, the whole-workload benefit, the scope of the validation |
| The Live Benchmark Engine Manual | every control, its backend, its effects, its limits, and the factory against the active settings |
| The engine's own pages (`docs/OMNI_V19.md`, `cpp/`, `tools/seal.py`) | the equations, units, profile loading, timing, parity checks and release fingerprints |
| The reading guide (`docs/HOW_TO_READ_THE_RESULTS.md`) | the workload contract, the measurement boundary, the profile's identity, the costs, the requirements and the verdict rules |

That is the common language: build and verify the mechanisms; tune and validate the complete profile; freeze its release identity;
expose deliberate, traceable adjustment through the live benchmark engine.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
