# GPU causal attribution specification

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


A successful `nvidia-smi -pl` command is not by itself a physical efficiency result.

## Authority chain
`canonical held u -> bounded requested limit -> driver return -> immediate/readback limit -> enforced limit -> clock-event attribution -> physical work + energy -> restoration`

The bench records both sampled board power and cumulative device energy when supported. NVIDIA DCGM/NVML clock-event reasons distinguish software power capping from GPU idle, application-clock constraints, software/hardware thermal slowdown and external hardware power brake. These are attribution evidence, not substitutes for work and joule measurements.

## Credit rule
An Omni efficiency interpretation requires the frozen workload and service guardrails to hold while the authority chain is intact. `SwPowerCap` can support that the software cap was operative. Thermal slowdown or hardware power brake is adverse/confounding evidence and is not credited to Omni. GPU idle can indicate workload starvation. Application-clock limitation identifies another authority.

## One writer
The harness uses a cooperative filesystem lock for its own power-limit writes and retains independent hardware readback because foreign writers need not honor that lock. Watch has zero write authority. DCGM is observer-only in this experiment.

## Energy hierarchy
1. GPU device counter when supported.
2. Integrated board-power samples as a cross-check.
3. CPU package RAPL as separate node-side energy evidence.
4. Independent wall/PDU energy as whole-machine evidence when fitted.

No arithmetic combination of GPU and RAPL counters is labeled wall energy.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
