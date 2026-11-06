# Domain Adapter Map

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

> **Specification, carried from the package XPASS27 (2026-10-01).** It specifies a contract or a measurement; any result
> it quotes is as of that package. Current results: `docs/STATE_OF_PLAY.md` and the tables in `results/`.

> **License notice:** Omni-Compass is source-available for **evaluation and simulation only** under the root `LICENSE`; it is **not open source**. Production use, commercialization, monetization, hosted/SaaS/API use, customer-facing use, and commercial embedding/integration require a separate written paid license from **The Omni-Compass LLC**. The root `LICENSE` controls.


The radial Omni-Compass image is treated as an architectural coverage map, not validation evidence. Each domain must supply h(z)->x observation, bounded actuator map M(a), readback, admissibility, meter/work metric, and restoration before it can move beyond conceptual status.

| Domain shown | Candidate observation | Candidate muscles | Required independent evidence | Current status |
|---|---|---|---|---|
| Applications / DevOps | queue, latency, replicas, errors | replicas, requests, rollout | Kind/production-like software plant | PARTIAL: Kubernetes model; Kind current-brain OPEN |
| Data systems | queue depth, IO latency, replication lag | concurrency, replicas, placement | real DB/storage workload | OPEN |
| Cloud platforms | utilization, pending capacity, cost/power telemetry | provision, suspend, resize, placement | cloud account receipts + workload/SLO | MODEL ONLY |
| AI & analytics | throughput, latency, GPU telemetry | GPU power envelope, replicas, placement | physical NVIDIA paired experiment | READY, PHYSICAL OPEN |
| Networking | loss, RTT, queue, link utilization | routing/QoS/rate limits | network testbed | OPEN |
| Power grids | frequency/voltage/load state | bounded setpoints only under certified interface | HIL/physical grid testbed + safety review | OPEN |
| Autonomous vehicles | state estimate, trajectory error | bounded supervisory constraints | simulator then HIL/vehicle safety program | OPEN |
| Robotics & automation | pose/error/load/thermal | bounded joint/task envelopes | robot simulator/HIL/physical cell | OPEN |
| Healthcare | device/workflow telemetry | only domain-approved bounded interfaces | regulated validation and clinical/safety review | OPEN |

No row authorizes deployment merely because the generic six-state governor can be mapped onto its variables.

---
## CURRENT RELEASE SYNCHRONIZATION — XPASS25

This living document is synchronized to XPASS25. Historical receipts and prior-run artifacts remain frozen and are not rewritten. The canonical six-state/eight-line CLAIM1 core, held-u law, C++ core, GPU writer/watchdog, causal evidence gate, and physical evidence contracts are unchanged from XPASS15.


Open external evidence remains: 500-scenario counted run, Kind CLAIM1-23, and physical NVIDIA. Simulation results are not physical meter results or proprietary-product executions.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
