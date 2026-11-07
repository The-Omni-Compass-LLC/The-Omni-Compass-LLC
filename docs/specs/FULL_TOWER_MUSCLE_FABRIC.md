# Omni-Compass Full-Tower Muscle Fabric — Pass 2

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


This pass extends the Universal Muscle SDK into a C++ qualification harness with **128 normalized actuator capabilities across 16 families**. The six-state governing engine is not modified.

## Evidence boundary

The 128 catalog entries are normalized actuator **contracts**. They are not claims that 128 production integrations have been physically executed. The C++ harness exercises the common observation/bound/execute/readback/restore path using simulated adapters. Concrete Kubernetes/Linux/NVIDIA/cloud/storage/database/network adapters must independently earn L/P/C evidence.

## Design rule

Any accessible actuator may become an Omni muscle if it supplies observation, bounds, timing, execution, readback, shielding, restoration and receipts. New muscles expand the authority surface; they do not create a new governing brain.

## Harness

`oc_full_tower` instantiates all 128 contracts, routes authority from the existing nervous-system gate, performs an actuation/readback/restore transaction for every muscle, then asserts fail-closed behavior under a global security hold.

The machine-readable catalogs are `muscles/FULL_TOWER_128.csv` and `.json`.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
