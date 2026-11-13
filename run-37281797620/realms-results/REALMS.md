# The realms, round 3: 656 muscles on modelled plants, native against Omni on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


Evidence class **S** (simulation). Run 2026-10-05 08:09 UTC, commit `7a536480eaf5`, seeds 3000-3009 (10 paired seeds per muscle and per organism). Preregistered in `docs/REALMS_PREREGISTRATION.md` (round 3); rounds 1 and 2 are kept in `round1/` and `round2/`. Each realm organism is its own families plus the shared spine (Kubernetes, machines, GPUs and CPUs, network, storage, observability, security, cooling, electrical distribution), as every real stack runs on it; harness `realms/`; every plant and its native controller in `realms/plants.py`, every number in `realms/presets.py`. The governor is the frozen `omnicompass.adapter.Governor`, unchanged, and every knob obeys the shipped nervous system (`omnicompass/nervous_system.py`) the way the live controller's organs do.

Primary outcome: work per energy, Omni against native, with its 95% interval over seeds. Guardrails: work not lower by more than 1%, share of periods in violation not higher by more than 1 percentage point. Labels by rule.

These are models. A model's energy is not a meter's, and a plant written by the same people who wrote the governor is not an independent test. What a row here can show is whether the governor's law, applied to that knob, helps or hurts the model, and where it breaks.

## The five organisms

| Organism | Muscles | Label | Work per energy | Work | Energy | Violations (pp) | Valid |
|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 345 | **WORSE** | -0.1% (-0.1 to -0.1) | -0.0% (-0.0 to -0.0) | +0.1% (+0.1 to +0.1) | +0.0 (-0.0 to +0.0) | yes |
| Physics / Robotics / Autonomous | 262 | **WORSE** | -0.7% (-0.8 to -0.6) | -0.0% (-0.0 to +0.0) | +0.7% (+0.6 to +0.8) | -0.1 (-0.1 to -0.1) | yes |
| Energy / Facility / Industrial | 282 | **ENERGY IMPROVEMENT WITH SERVICE TRADEOFF** | +0.4% (+0.3 to +0.4) | -0.0% (-0.0 to -0.0) | -0.4% (-0.4 to -0.4) | +0.0 (+0.0 to +0.1) | yes |
| Distribution / Specialized | 337 | **WORSE** | -0.1% (-0.1 to -0.1) | -0.0% (-0.0 to -0.0) | +0.1% (+0.1 to +0.1) | -0.0 (-0.0 to -0.0) | yes |
| The whole tower (656 muscles) | 656 | **ENERGY IMPROVEMENT WITH SERVICE TRADEOFF** | +0.1% (+0.1 to +0.2) | -0.0% (-0.0 to -0.0) | -0.1% (-0.2 to -0.1) | +0.0 (-0.0 to +0.0) | yes |

## Every muscle alone, by home realm

| Realm | Muscles | SUPERIOR WITHIN GUARDRAILS | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | NONINFERIOR / INCONCLUSIVE | NOT ESTABLISHED | WORSE | INVALID |
|---|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 266 | 1 | 43 | 181 | 2 | 39 | 0 |
| Physics / Robotics / Autonomous | 72 | 16 | 13 | 34 | 8 | 1 | 0 |
| Energy / Facility / Industrial | 121 | 32 | 5 | 53 | 3 | 28 | 0 |
| Distribution / Specialized | 197 | 0 | 0 | 155 | 2 | 40 | 0 |
| **All** | 656 | **49** | **61** | **423** | **15** | **108** | **0** |

## By knob: what kind of authority Omni held

| Knob | Muscles | SUPERIOR WITHIN GUARDRAILS | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | NONINFERIOR / INCONCLUSIVE | NOT ESTABLISHED | WORSE | INVALID | Median work per energy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| capacity | 344 | 26 | 46 | 202 | 6 | 64 | 0 | -0.0% |
| setpoint | 55 | 18 | 2 | 17 | 0 | 18 | 0 | -0.0% |
| power | 63 | 2 | 4 | 56 | 0 | 1 | 0 | +0.0% |
| admission | 194 | 3 | 9 | 148 | 9 | 25 | 0 | +0.0% |

## Setpoint muscles: Omni against simply fixing the setpoint at the band's calm end

For 54 of 55 setpoint muscles, a fixed setpoint at the calm end of the declared band gave more work per energy than Omni moving it. On those muscles the gain is the band, not the governor. The fixed setpoint's own label (with its service guardrails) is in `MUSCLES.csv`.

## By family

| Realm | Family | Plant | Muscles | Superior | Tradeoff | Inconclusive | Not established | Worse | Invalid | Median work per energy |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | AI Inference Serving | compute_pool (gpu) | 16 | 0 | 0 | 12 | 0 | 4 | 0 | -0.1% |
| Compute / AI / Cloud | AI Training | compute_pool (gpu_batch) | 16 | 1 | 0 | 14 | 0 | 1 | 0 | -0.0% |
| Compute / AI / Cloud | Cloud VM & Capacity | compute_pool (node) | 16 | 0 | 16 | 0 | 0 | 0 | 0 | +6.7% |
| Compute / AI / Cloud | Container Resources | compute_pool (server) | 16 | 0 | 0 | 12 | 0 | 4 | 0 | -0.1% |
| Compute / AI / Cloud | Cross-Cluster, Multi-Region & Edge | compute_pool (node) | 15 | 0 | 9 | 6 | 0 | 0 | 0 | +6.0% |
| Compute / AI / Cloud | DPU SmartNIC & Programmable IO | compute_pool (fabric) | 12 | 0 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Distributed Cluster Managers | compute_pool (batch) | 15 | 0 | 0 | 7 | 0 | 8 | 0 | -0.2% |
| Compute / AI / Cloud | GPU Fabric & RDMA | compute_pool (fabric) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | HPC & Distributed Compute | compute_pool (batch) | 16 | 0 | 0 | 10 | 0 | 6 | 0 | -0.1% |
| Compute / AI / Cloud | Host CPU & Memory | compute_pool (cpu_host) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Kubernetes Dynamic Device Allocation | compute_pool (gpu) | 8 | 0 | 0 | 5 | 1 | 2 | 0 | -0.1% |
| Compute / AI / Cloud | Kubernetes Placement & Scheduling | compute_pool (server) | 16 | 0 | 0 | 13 | 0 | 3 | 0 | -0.0% |
| Compute / AI / Cloud | Kubernetes Workload Scaling | compute_pool (server) | 16 | 0 | 0 | 14 | 0 | 2 | 0 | -0.0% |
| Compute / AI / Cloud | NVIDIA GPU Hardware | compute_pool (gpu) | 15 | 0 | 0 | 8 | 1 | 6 | 0 | -0.1% |
| Compute / AI / Cloud | Node Fleet & Karpenter-Class Control | compute_pool (node) | 16 | 0 | 13 | 3 | 0 | 0 | 0 | +6.6% |
| Compute / AI / Cloud | OpenShift & Machine API | compute_pool (node) | 9 | 0 | 5 | 4 | 0 | 0 | 0 | +5.6% |
| Compute / AI / Cloud | Quantum Computing Control Simulation | compute_pool (qpu) | 16 | 0 | 0 | 13 | 0 | 3 | 0 | -0.1% |
| Compute / AI / Cloud | Work Admission & Demand Shaping | compute_pool (server) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Cache & Memory Services | compute_pool (server) | 15 | 0 | 0 | 12 | 0 | 3 | 0 | -0.0% |
| Distribution / Specialized | Commerce & Payment Systems | compute_pool (commerce) | 15 | 0 | 0 | 9 | 1 | 5 | 0 | +0.0% |
| Distribution / Specialized | Data Analytics & ETL | compute_pool (batch) | 15 | 0 | 0 | 10 | 0 | 5 | 0 | -0.1% |
| Distribution / Specialized | Database & Transactions | compute_pool (database) | 14 | 0 | 0 | 6 | 0 | 8 | 0 | -0.3% |
| Distribution / Specialized | Messaging & Streaming | compute_pool (server) | 16 | 0 | 0 | 14 | 0 | 2 | 0 | -0.0% |
| Distribution / Specialized | Network Routing & Switching | compute_pool (network) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Observability & Telemetry | compute_pool (server) | 6 | 0 | 0 | 6 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Reliability, Security & Recovery | compute_pool (server) | 12 | 0 | 0 | 10 | 1 | 1 | 0 | +0.0% |
| Distribution / Specialized | Runtime & Application | compute_pool (server) | 15 | 0 | 0 | 10 | 0 | 5 | 0 | -0.1% |
| Distribution / Specialized | Search, Indexing & Vector DB | compute_pool (server) | 15 | 0 | 0 | 9 | 0 | 6 | 0 | -0.1% |
| Distribution / Specialized | Service Mesh & API Reliability | compute_pool (server) | 15 | 0 | 0 | 12 | 0 | 3 | 0 | -0.0% |
| Distribution / Specialized | Storage Block/File/Object | compute_pool (storage) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | -0.0% |
| Distribution / Specialized | Telecom RAN & Edge Radio | compute_pool (ran) | 12 | 0 | 0 | 11 | 0 | 1 | 0 | -0.0% |
| Distribution / Specialized | Workflow, Logistics & Fulfillment | compute_pool (workflow) | 15 | 0 | 0 | 14 | 0 | 1 | 0 | -0.0% |
| Energy / Facility / Industrial | Building & Critical Environment HVAC | thermal_zone (building) | 12 | 8 | 0 | 1 | 1 | 2 | 0 | +0.1% |
| Energy / Facility / Industrial | Cooling, Chillers & Thermodynamics | thermal_zone (data_hall) | 15 | 5 | 0 | 2 | 2 | 6 | 0 | -0.1% |
| Energy / Facility / Industrial | Energy Storage & Microgrid | energy_storage (microgrid) | 16 | 3 | 0 | 8 | 0 | 5 | 0 | -0.0% |
| Energy / Facility / Industrial | Facility & Grid Optimization | energy_storage (facility) | 15 | 1 | 4 | 4 | 0 | 6 | 0 | -0.0% |
| Energy / Facility / Industrial | Grid Transmission & Distribution | process_loop (feeder_voltage) | 12 | 4 | 0 | 8 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Industrial PLC & Process Automation | process_loop (process) | 14 | 6 | 0 | 8 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | PDU, UPS & Electrical Distribution | energy_storage (ups) | 14 | 0 | 0 | 5 | 0 | 9 | 0 | -0.0% |
| Energy / Facility / Industrial | Semiconductor Fab & Precision Manufacturing | process_loop (chamber) | 11 | 2 | 0 | 9 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Water Wastewater & Pumping | process_loop (water) | 12 | 3 | 1 | 8 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Automotive EV & Mobile Powertrain | motion_axis (ev_traction) | 12 | 0 | 0 | 11 | 1 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Aviation & Autonomous Flight | motion_axis (flight_axis) | 16 | 6 | 5 | 1 | 4 | 0 | 0 | +0.2% |
| Physics / Robotics / Autonomous | Robotics Fleet & Warehouse Automation | compute_pool (robot_fleet) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Robotics Motion Control | motion_axis (robot_joint) | 15 | 6 | 4 | 4 | 1 | 0 | 0 | +0.6% |
| Physics / Robotics / Autonomous | Spacecraft & Flight Software | motion_axis (reaction_wheel) | 14 | 4 | 4 | 3 | 2 | 1 | 0 | +1.1% |

## Largest gains and largest losses (single muscles, by mean work per energy)

| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) |
|---|---|---|---|---:|---:|---:|
| tank_level_target | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +37.7% (+35.4 to +39.9) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| temperature_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +36.2% (+34.2 to +38.2) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| pressure_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +35.9% (+33.6 to +38.1) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| furnace_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +35.7% (+33.8 to +37.7) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| valve_position | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +35.5% (+33.3 to +37.7) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| mass_flow_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +35.3% (+33.3 to +37.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| reservoir_level_target | Water Wastewater & Pumping | setpoint | SUPERIOR WITHIN GUARDRAILS | +14.1% (+12.7 to +15.6) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| flow_target_water | Water Wastewater & Pumping | setpoint | SUPERIOR WITHIN GUARDRAILS | +14.1% (+12.8 to +15.4) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| valve_position_water | Water Wastewater & Pumping | setpoint | SUPERIOR WITHIN GUARDRAILS | +13.7% (+12.5 to +15.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| instrument_activation | Spacecraft & Flight Software | capacity | SUPERIOR WITHIN GUARDRAILS | +13.7% (+11.1 to +16.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| task_admission | Distributed Cluster Managers | admission | WORSE | -5.1% (-6.9 to -3.4) | +0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| job_priority | HPC & Distributed Compute | admission | WORSE | -4.7% (-6.2 to -3.2) | +0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| scratch_budget | HPC & Distributed Compute | admission | WORSE | -4.4% (-5.8 to -2.9) | -0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| scheduler_fair_share | HPC & Distributed Compute | admission | WORSE | -4.2% (-5.6 to -2.8) | -0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| spill_threshold | Data Analytics & ETL | admission | WORSE | -4.2% (-5.3 to -3.1) | -0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| job_preemption | HPC & Distributed Compute | admission | WORSE | -4.1% (-5.9 to -2.4) | -0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| analytics_admission | Data Analytics & ETL | admission | WORSE | -4.1% (-5.6 to -2.7) | -0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| parallel_io_budget | HPC & Distributed Compute | admission | WORSE | -4.1% (-6.3 to -1.8) | +0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| cluster_quota | Distributed Cluster Managers | admission | WORSE | -3.9% (-4.7 to -3.1) | +0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| stream_backpressure | Data Analytics & ETL | admission | WORSE | -3.7% (-5.6 to -1.9) | -0.0% (-0.0 to +0.0) | +0.0 (+0.0 to +0.0) |

## Validity

- Watch equal to native and the reset handing back the knob: 656 of 656 muscles; 5 of 5 organisms.
- Raw per-seed contrasts: `REALMS.json`. One row per muscle: `MUSCLES.csv`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*
