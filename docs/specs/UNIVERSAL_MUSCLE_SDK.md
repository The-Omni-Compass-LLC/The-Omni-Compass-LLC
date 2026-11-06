# OmniCompass Universal Muscle SDK

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


## Status

Additive integration layer. It does **not** alter the frozen six-state engine or claim that every listed connector is already implemented or physically verified.

## Architectural invariant

A new controllable domain is a **muscle**, not a new brain:

`plant telemetry -> observation adapter -> same Omni state -> bounded authority -> shield -> actuator -> readback -> plant`

The governing state remains `(E, U, I_U, S, B, Bdot)`.

## Qualification contract

Every automatic muscle must declare and test:

1. observable input and freshness;
2. capability range, units, resolution and rate/step bounds;
3. timing: observation, decision, actuation delay, hold, cooldown, timeout and stale horizon;
4. hard safety bounds and forbidden conditions;
5. requested, bounded and realized authority;
6. independent actuator readback when supported;
7. native snapshot and restoration;
8. deterministic failure behavior;
9. automation mode: disabled, recommend, manual, external approval or automatic;
10. evidence class: design (D), simulation (S), live software (L), physical (P), commercial (C).

## Standard actuator classes

The SDK reserves contracts for Kubernetes replicas/resources/HPA/placement/node pools; host CPUFreq/cgroups/CPU/memory/I/O; GPU power/clock/MIG/admission; cloud instance count/size/placement/start-stop/capacity; storage size/tier/IOPS/throughput/placement; network weights/rate/bandwidth/routing; application concurrency/workers/queues/JVM/thread pools/batch; cooling; rack power; and site power.

A reserved class is **not evidence of implementation**. Each concrete adapter must earn its own evidence class.

## Authority receipt

Every attempted command emits the same fields: muscle identity, automation mode, requested value, bounded value, realized value, units, permit/block result, reason, observation age, actuation latency, actuator residual, evidence class and status.

## Fail-safe rule

No loss of observability, safety permission or approval may increase authority. Stale/invalid observations block writes. Recommendation/manual modes do not write. A registered automatic muscle snapshots native state before its first write and exposes restoration through the registry.

## Extension pattern

Use `FunctionalMuscle` for a small connector or implement the `MuscleAdapter` protocol for a richer one. Register it in `MuscleRegistry`. The adapter owns vendor/API details; the six-state engine does not.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
