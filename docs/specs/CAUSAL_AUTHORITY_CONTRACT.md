# Causal authority contract

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


This branch formalizes what software can prove before an independent plant is available. It does **not** manufacture a plant result.

## Claim ladder

`COMPUTED -> REQUESTED -> ENFORCED -> ATTRIBUTED -> BENEFIT CANDIDATE -> RESTORED CANDIDATE -> CROSS-ARM STATISTICAL RESULT`

No stage may be inferred from a later-looking log line. A zero-return actuator call proves only that a request was accepted by the command path. Physical authority requires readback/enforcement. Attribution additionally requires absence of a conflicting writer or hostile limiter. Benefit requires physical energy + useful work + guardrails. The preregistered paired analysis, not the per-arm gate, decides whether benefit is statistically supported.

## Muscle interface

Every real muscle must declare:

1. resource and scope
2. sole/cooperative writer
3. command and hard bounds
4. readback/effective enforcement
5. conflict set
6. independent response/meter
7. work/health guardrails
8. restoration/handback
9. evidence class

The executable catalogue is `omnicompass/authority_contract.py`; `tools/authority_matrix.py` prints it.

## Current contracts

* NVIDIA board power: physical actuator candidate. `nvidia-smi -pl` remains the writer; requested and enforced limits are distinct evidence.
* Intel RAPL: physical **meter only** in the GPU experiment. `energy_uj` is not PL1 authority.
* Kubernetes replicas: external-software actuator. Historical Set-22 is not current CLAIM1 evidence.

## Cross-actuator dependency rule

An actuator must not be scored as independent when it changes the semantics of another controller. Examples: GPU power cap can alter service rate and therefore queue/HPA demand; VPA requests alter HPA utilization denominators; replica contraction can create node-off opportunity. Future multi-muscle runs must record the dependency edge and either freeze the dependent controller or score the coupled policy explicitly.

## Non-claims

This contract does not establish that Omni outperforms any competitor, that 128 simulated contracts are 128 deployed APIs, or that a physical plant has validated the governor. Those require external evidence.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
