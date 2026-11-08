# The realms: 945 muscles on modelled plants, native against Omni on top

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (simulation). Run 2026-11-07 23:29 UTC, commit `84462b32eacc`, seeds 3000-3009 (10 paired seeds per muscle and per organism). Preregistered in `docs/REALMS_PREREGISTRATION.md` (round 3); rounds 1 and 2 are kept in `round1/` and `round2/`. Each realm organism is its own families plus the shared spine (Kubernetes, machines, GPUs and CPUs, network, storage, observability, security, cooling, electrical distribution), as every real stack runs on it; harness `realms/`; every plant and its native controller in `realms/plants.py`, every number in `realms/presets.py`. The governor is the frozen `omnicompass.adapter.Governor`, unchanged, and every knob obeys the shipped nervous system (`omnicompass/nervous_system.py`) the way the live controller's organs do.

Primary outcome: work per energy, Omni against native, with its 95% interval over seeds. Guardrails: work not lower by more than 1%, share of periods in violation not higher by more than 1 percentage point. Labels by rule.

These are models. A model's energy is not a meter's, and a plant written by the same people who wrote the governor is not an independent test. What a row here can show is whether the governor's law, applied to that knob, helps or hurts the model, and where it breaks.

## The five organisms

| Organism | Muscles | Label | Work per energy | Work | Energy | Violations (pp) | Valid |
|---|---:|---|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 430 | **SUPERIOR WITHIN GUARDRAILS** | +0.1% (+0.1 to +0.1) | +0.0% (-0.0 to +0.0) | -0.1% (-0.1 to -0.1) | -0.0 (-0.0 to -0.0) | yes |
| Physics / Robotics / Autonomous | 376 | **SUPERIOR WITHIN GUARDRAILS** | +0.1% (+0.1 to +0.1) | +0.0% (-0.0 to +0.0) | -0.1% (-0.1 to -0.1) | -0.0 (-0.0 to +0.0) | yes |
| Energy / Facility / Industrial | 470 | **SUPERIOR WITHIN GUARDRAILS** | +0.3% (+0.2 to +0.4) | +0.0% (-0.0 to +0.0) | -0.3% (-0.4 to -0.2) | -0.0 (-0.0 to -0.0) | yes |
| Distribution / Specialized | 440 | **SUPERIOR WITHIN GUARDRAILS** | +0.2% (+0.1 to +0.2) | +0.0% (-0.0 to +0.0) | -0.2% (-0.2 to -0.1) | -0.0 (-0.0 to -0.0) | yes |
| The whole tower, every muscle once | 945 | **SUPERIOR WITHIN GUARDRAILS** | +0.3% (+0.2 to +0.4) | +0.0% (-0.0 to +0.0) | -0.3% (-0.4 to -0.2) | -0.0 (-0.0 to -0.0) | yes |

## Every muscle alone, by home realm

| Realm | Muscles | SUPERIOR WITHIN GUARDRAILS | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | NONINFERIOR / INCONCLUSIVE | NOT ESTABLISHED | AWAY FROM ITS AIM | INVALID |
|---|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 334 | 20 | 2 | 312 | 0 | 0 | 0 |
| Physics / Robotics / Autonomous | 119 | 19 | 4 | 96 | 0 | 0 | 0 |
| Energy / Facility / Industrial | 249 | 81 | 4 | 160 | 0 | 0 | 0 |
| Distribution / Specialized | 243 | 2 | 0 | 241 | 0 | 0 | 0 |
| **All** | 945 | **122** | **10** | **809** | **0** | **0** | **0** |

## By knob: what kind of authority Omni held

| Knob | Muscles | SUPERIOR WITHIN GUARDRAILS | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | NONINFERIOR / INCONCLUSIVE | NOT ESTABLISHED | AWAY FROM ITS AIM | INVALID | Median work per energy |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| capacity | 454 | 19 | 0 | 435 | 0 | 0 | 0 | +0.0% |
| setpoint | 134 | 81 | 4 | 45 | 0 | 0 | 0 | +1.0% |
| power | 102 | 22 | 6 | 74 | 0 | 0 | 0 | +0.0% |
| admission | 255 | 0 | 0 | 255 | 0 | 0 | 0 | +0.0% |

## Setpoint muscles: Omni against simply fixing the setpoint at the band's calm end

For 132 of 134 setpoint muscles, a fixed setpoint at the calm end of the declared band gave more work per energy than Omni moving it. On those muscles the gain is the band, not the governor. The fixed setpoint's own label (with its service guardrails) is in `MUSCLES.csv`.

## By family

| Realm | Family | Plant | Muscles | Superior | Tradeoff | Inconclusive | Not established | Worse | Invalid | Median work per energy |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | AI Inference Serving | compute_pool (gpu) | 24 | 1 | 0 | 23 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | AI Training | compute_pool (gpu_batch) | 18 | 1 | 0 | 17 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Cloud VM & Capacity | compute_pool (node) | 21 | 0 | 0 | 21 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Container Resources | compute_pool (server) | 23 | 0 | 0 | 23 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Cross-Cluster, Multi-Region & Edge | compute_pool (node) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | DPU SmartNIC & Programmable IO | compute_pool (fabric) | 12 | 0 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Distributed Cluster Managers | compute_pool (batch) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | GPU Fabric & RDMA | compute_pool (fabric) | 18 | 0 | 0 | 18 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | HPC & Distributed Compute | compute_pool (batch) | 19 | 2 | 0 | 17 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Host CPU & Memory | compute_pool (cpu_host) | 23 | 11 | 1 | 11 | 0 | 0 | 0 | +1.1% |
| Compute / AI / Cloud | Kubernetes Dynamic Device Allocation | compute_pool (gpu) | 8 | 0 | 0 | 8 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Kubernetes Placement & Scheduling | compute_pool (server) | 20 | 0 | 0 | 20 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Kubernetes Workload Scaling | compute_pool (server) | 31 | 0 | 0 | 31 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | NVIDIA GPU Hardware | compute_pool (gpu) | 19 | 5 | 1 | 13 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Node Fleet & Karpenter-Class Control | compute_pool (node) | 24 | 0 | 0 | 24 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | OpenShift & Machine API | compute_pool (node) | 9 | 0 | 0 | 9 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Quantum Computing Control Simulation | compute_pool (qpu) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Compute / AI / Cloud | Work Admission & Demand Shaping | compute_pool (server) | 19 | 0 | 0 | 19 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Cache & Memory Services | compute_pool (server) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Commerce & Payment Systems | compute_pool (commerce) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Data Analytics & ETL | compute_pool (batch) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Database & Transactions | compute_pool (database) | 19 | 0 | 0 | 19 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Medical Imaging & Clinical Systems | compute_pool (clinical) | 12 | 0 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Messaging & Streaming | compute_pool (server) | 18 | 0 | 0 | 18 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Network Routing & Switching | compute_pool (network) | 19 | 0 | 0 | 19 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Observability & Telemetry | compute_pool (server) | 9 | 0 | 0 | 9 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Ports & Maritime Logistics | compute_pool (port) | 12 | 1 | 0 | 11 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Reliability, Security & Recovery | compute_pool (server) | 12 | 0 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Runtime & Application | compute_pool (server) | 17 | 0 | 0 | 17 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Search, Indexing & Vector DB | compute_pool (server) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Service Mesh & API Reliability | compute_pool (server) | 16 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Storage Block/File/Object | compute_pool (storage) | 20 | 0 | 0 | 20 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Telecom RAN & Edge Radio | compute_pool (ran) | 12 | 1 | 0 | 11 | 0 | 0 | 0 | +0.0% |
| Distribution / Specialized | Workflow, Logistics & Fulfillment | compute_pool (workflow) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Agriculture & Irrigation | process_loop (irrigation) | 14 | 10 | 0 | 4 | 0 | 0 | 0 | +15.0% |
| Energy / Facility / Industrial | Building & Critical Environment HVAC | thermal_zone (building) | 15 | 5 | 0 | 10 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Cooling, Chillers & Thermodynamics | thermal_zone (data_hall) | 18 | 6 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | District Heating & Cooling | process_loop (district_heat) | 13 | 3 | 4 | 6 | 0 | 0 | 0 | +3.1% |
| Energy / Facility / Industrial | Energy Storage & Microgrid | energy_storage (microgrid) | 19 | 0 | 0 | 16 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Facility & Grid Optimization | energy_storage (facility) | 15 | 0 | 0 | 14 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Grid Transmission & Distribution | process_loop (feeder_voltage) | 12 | 4 | 0 | 8 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Healthcare Critical Environments | thermal_zone (hospital) | 13 | 7 | 0 | 6 | 0 | 0 | 0 | +4.5% |
| Energy / Facility / Industrial | Industrial PLC & Process Automation | process_loop (process) | 18 | 6 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Mining & Mineral Processing | process_loop (mill) | 14 | 4 | 0 | 10 | 0 | 0 | 0 | +0.6% |
| Energy / Facility / Industrial | Oil & Gas Pipelines | process_loop (pipeline) | 14 | 8 | 0 | 6 | 0 | 0 | 0 | +6.7% |
| Energy / Facility / Industrial | PDU, UPS & Electrical Distribution | energy_storage (ups) | 18 | 0 | 0 | 18 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Pharmaceutical & Food Manufacturing | process_loop (batch_reactor) | 14 | 10 | 0 | 4 | 0 | 0 | 0 | +1.0% |
| Energy / Facility / Industrial | Power Generation & Turbine Control | process_loop (turbine) | 14 | 10 | 0 | 4 | 0 | 0 | 0 | +1.0% |
| Energy / Facility / Industrial | Renewable Generation & Inverter Control | process_loop (inverter) | 13 | 2 | 0 | 11 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Semiconductor Fab & Precision Manufacturing | process_loop (chamber) | 13 | 2 | 0 | 11 | 0 | 0 | 0 | +0.0% |
| Energy / Facility / Industrial | Water Wastewater & Pumping | process_loop (water) | 12 | 4 | 0 | 8 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Automotive EV & Mobile Powertrain | motion_axis (ev_traction) | 14 | 0 | 0 | 14 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Aviation & Autonomous Flight | motion_axis (flight_axis) | 20 | 7 | 0 | 13 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Elevators & Vertical Transport | motion_axis (elevator_hoist) | 12 | 0 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Marine Propulsion & Vessel Automation | motion_axis (marine_propulsion) | 12 | 0 | 0 | 12 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Rail Traction & Train Control | motion_axis (rail_traction) | 14 | 0 | 0 | 14 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Robotics Fleet & Warehouse Automation | compute_pool (robot_fleet) | 15 | 0 | 0 | 15 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Robotics Motion Control | motion_axis (robot_joint) | 18 | 8 | 0 | 10 | 0 | 0 | 0 | +0.0% |
| Physics / Robotics / Autonomous | Spacecraft & Flight Software | motion_axis (reaction_wheel) | 14 | 4 | 4 | 6 | 0 | 0 | 0 | +0.8% |

## Largest gains and largest losses (single muscles, by mean work per energy)

| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) |
|---|---|---|---|---:|---:|---:|
| tank_level_target | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +29.2% (+27.6 to +30.9) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| temperature_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +28.2% (+26.6 to +29.7) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| pressure_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +28.0% (+26.2 to +29.9) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| furnace_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +27.8% (+26.3 to +29.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| valve_position | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +27.7% (+26.0 to +29.5) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| mass_flow_setpoint | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +27.6% (+26.1 to +29.1) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| greenhouse_temperature_setpoint | Agriculture & Irrigation | setpoint | SUPERIOR WITHIN GUARDRAILS | +17.1% (+15.8 to +18.4) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| well_drawdown_level_target | Agriculture & Irrigation | setpoint | SUPERIOR WITHIN GUARDRAILS | +16.2% (+14.7 to +17.8) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| pivot_speed_setpoint | Agriculture & Irrigation | setpoint | SUPERIOR WITHIN GUARDRAILS | +16.1% (+14.6 to +17.5) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| mainline_pressure_setpoint | Agriculture & Irrigation | setpoint | SUPERIOR WITHIN GUARDRAILS | +15.8% (+14.6 to +17.1) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| battery_soc_reserve | Energy Storage & Microgrid | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.2% (-0.2 to -0.2) | +0.0% (+0.0 to +0.0) | -1.4 (-1.6 to -1.2) |
| time_of_use_schedule | Energy Storage & Microgrid | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.2% (-0.2 to -0.2) | +0.0% (+0.0 to +0.0) | -1.4 (-1.5 to -1.3) |
| microgrid_emergency_reserve | Energy Storage & Microgrid | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.2% (-0.2 to -0.2) | +0.0% (+0.0 to +0.0) | -1.4 (-1.5 to -1.3) |
| pue_target | Facility & Grid Optimization | setpoint | SERVICE IMPROVEMENT WITH ENERGY TRADEOFF | -0.1% (-0.1 to -0.1) | +0.0% (+0.0 to +0.0) | -0.8 (-1.0 to -0.6) |
| model_replicas | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_route_weight | AI Inference Serving | setpoint | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_load | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_unload | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_instance_count | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| continuous_batching | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |

## Validity

- Watch equal to native and the reset handing back the knob: 945 of 945 muscles; 5 of 5 organisms.
- Raw per-seed contrasts: `REALMS.json`. One row per muscle: `MUSCLES.csv`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
