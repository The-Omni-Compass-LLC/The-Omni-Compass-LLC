# GPU Physical Evidence Contract

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


## Purpose
This contract defines what must exist before Omni-Compass may describe a Native / Watch / Omni GPU experiment as physical evidence. It does not declare a performance result before hardware execution.

## Physical causal chain

```text
frozen workload -> measured demand -> canonical six-state step -> bounded u_hold
-> requested GPU board-power limit -> driver return -> immediate readback
-> enforced board-power limit -> clock-event attribution -> physical GPU response
-> successful frozen work + latency -> device joules -> optional CPU/wall joules
-> restoration -> immutable evidence folder
```

A command is not an effect. `requested != enforced` is an authority discrepancy. A lower energy number is not a benefit if useful work or the preregistered service guardrails fail.

## Arms

**Native:** no Omni process and zero Omni power writes.

**Watch:** the same Omni observation/decision path runs, but power writes are forbidden. Watch is an observer-effect control. If Watch differs materially from Native on the preregistered primary outcome, attribution to granted Omni authority is rejected.

**Omni:** the identical frozen workload runs while the canonical governor receives bounded write authority. `nvidia-smi -pl` remains the sole experiment power-limit writer. DCGM/NVML are observers.

## Required preflight
`tools/gpu_physical_preflight.py` produces `PHYSICAL_PREFLIGHT.json`. A counted run requires:

- NVIDIA GPU identity and UUID;
- persistence enabled;
- power management enabled;
- enforced power limit readable;
- clock-event reason telemetry readable;
- one-job-per-GPU declaration for the scored workload;
- the exact driver and VBIOS recorded.

RAPL and DCGM are recorded when available. A wall meter may be made mandatory with `--require-wall`. The local DCGM field catalogue is frozen because field availability is hardware/version dependent.

## Attribution states

- `SwPowerCap` with requested approximately equal to enforced under useful load is compatible with the software cap being operative.
- software/hardware thermal slowdown causes fail-up and prevents crediting a reduction to Omni.
- hardware power brake is an external board/system power-delivery constraint and prevents causal credit to Omni for that interval.
- GPU idle is evidence of absent work, not a power-efficiency victory.
- application/user clock constraints indicate a second clock authority and must be reported.

Clock-event reasons explain constraint state; they do not replace energy or work measurement.

## Energy hierarchy

1. whole-node wall joules, when an independent wall meter is fitted and qualified;
2. GPU cumulative device energy counter, when supported;
3. independently integrated GPU board-power samples as cross-check;
4. CPU package RAPL energy as a separate secondary scope.

No missing physical meter is replaced by a model. GPU joules, CPU package joules and wall joules are different scopes and are never relabeled as one another.

## Evidence folder minimum
Each repetition must contain all three arms. Each arm preserves sampled GPU telemetry, window boundaries, workload requests, device counter snapshots, RAPL snapshots, power-limit start/end and workload output. Watch and Omni additionally preserve governor audit, exit receipt and independent watchdog receipt. Root provenance includes the preflight, source freeze at start/end, statistical report and SHA-256 manifest.

`tools/validate_gpu_physical_evidence.py RUN_DIR` validates this structure and provenance after the run. It does not replace `tools/gpu_reps.py`, which applies the preregistered statistical rules.

## Claims boundary
Before a qualifying hardware folder exists, the correct status is **PHYSICAL GPU EVIDENCE OPEN**. Harness readiness, stand-in-device tests, simulation, C++ parity and Kubernetes tests do not satisfy this contract.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
