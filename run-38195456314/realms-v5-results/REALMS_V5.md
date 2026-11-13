# The realms on Omni v5: 1097 muscles on modelled plants, native against the v5 law on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class **S** (modelled). Run 2026-10-12 02:35 UTC, commit `c0bc70570862`, seeds 3000-3009 (10 paired seeds per muscle and per organism), catalog `realms/catalog_v5.csv`. The engine is **omni-v5** (`tools/omni_version.py`, `OMNI_V5.json`): the v5 compass law `realms/compass_arm_v5.py` at its default `V5CFG`, on top of each plant's own native controller. Harness `realms/`.

The v5 law carries two math-only guardrails: the **edge** (a per-knob cushion from how fast service has climbed and how far it wobbles, so nothing riding its limit falls off) and the **centre/hole** (a machine or a cooled zone is eased only while it can still climb back). Otherwise every knob is free, and a knob stays native wherever the law cannot improve it without harm. Every process loop moves inside its band, generating units included, but never closer to its band's edge than its own largest swing toward that edge (the loop reach); a cooled zone never warmer than its cooling can recover, nor while its cooling headroom is falling toward empty; a power cap only on a pool whose response line outlasts one decision (an interactive pool's cap is proven on the metered GPU, class P, not here), never below the largest jump in demand nor past the line; the battery shave and a cloud pool's machine hand-back held native (round-trip energy bought for service; a hand-back the autoscaler never undoes).

Amendment (12 Oct): this table replaces the first v5 table (commit `c0e80a852`, the whole tower +0.0%). That engine held every generating unit's loop, every power cap and every inverter native by blanket gates, which threw away most of what v5 saves. v5 was re-declared with those gates replaced by physics floors (the loop reach, the cooling headroom's fall read ahead, the latency floor, the power cap only where a pool's line outlasts a decision, a cloud pool's machine hand-back left to its autoscaler, a motion axis slowed only while the wake forecast over a whole deadline still finishes inside it), developed on seeds 7100-7209 only; the preregistered seeds 3000-3009 are run again unchanged.

Primary outcome: work per energy, v5 against native, with its 95% interval over seeds. Guardrails: work not lower by more than 1%, share of periods in violation not higher by more than 1 percentage point. Labels by rule. These are models; a model's energy is not a meter's, and a plant written by the same people who wrote the law is not an independent test. What a row shows is whether the v5 law, applied to that knob, helps or hurts the model.

## The six organisms

Native, the v5 law and the v3 law on the same seeds. Energy saved is native's energy minus the arm's, as a share of native's (95% interval over seeds); times v3 is v5's saving over v3's. The four stacked keep each realm's own body on one clock, so every muscle in the stack runs exactly the native it runs in its own realm, plant by plant: the native is identical in all six.

| Organism | Muscles | Label | Work per energy | Work | Energy saved, v5 | Energy saved, v3 | Times v3 | Violations (pp) | Valid |
|---|---:|---|---:|---:|---:|---:|---:|---:|---|
| Compute / AI / Cloud | 530 | **SUPERIOR WITHIN GUARDRAILS** | +0.5% (+0.5 to +0.5) | +0.0% (-0.0 to +0.0) | 0.48% (0.46 to 0.50) | 0.45% (0.44 to 0.46) | 1.1x | -0.0 (-0.0 to -0.0) | yes |
| Physics / Robotics / Autonomous | 394 | **SUPERIOR WITHIN GUARDRAILS** | +0.1% (+0.1 to +0.1) | +0.0% (-0.0 to +0.0) | 0.09% (0.08 to 0.10) | 0.08% (0.07 to 0.09) | 1.2x | -0.0 (-0.0 to -0.0) | yes |
| Energy / Facility / Industrial | 470 | **SUPERIOR WITHIN GUARDRAILS** | +1.0% (+1.0 to +1.1) | +0.0% (-0.0 to +0.0) | 1.00% (0.94 to 1.05) | 0.33% (0.23 to 0.42) | 3.0x | -0.0 (-0.0 to -0.0) | yes |
| Distribution / Specialized | 474 | **SUPERIOR WITHIN GUARDRAILS** | +0.3% (+0.3 to +0.4) | +0.0% (-0.0 to +0.0) | 0.31% (0.25 to 0.36) | 0.20% (0.18 to 0.23) | 1.5x | -0.0 (-0.0 to -0.0) | yes |
| The four stacked, every shared muscle in each | 1868 | **SUPERIOR WITHIN GUARDRAILS** | +1.0% (+0.9 to +1.1) | +0.0% (-0.0 to +0.0) | 0.99% (0.94 to 1.05) | 0.33% (0.23 to 0.42) | 3.0x | -0.0 (-0.0 to -0.0) | yes |
| The whole tower, every muscle once | 1097 | **SUPERIOR WITHIN GUARDRAILS** | +1.0% (+0.9 to +1.1) | +0.0% (-0.0 to +0.0) | 0.99% (0.94 to 1.05) | 0.33% (0.23 to 0.42) | 3.0x | -0.0 (-0.0 to -0.0) | yes |

## Inside the organisms: every plant that did worse than native

A stricter look than the organism's total: every plant inside each organism, over all seeds, that did less work than native or spent more decisions over its own line, for v5 and for v3. Reported whatever it shows. A plant can do worse without Omni ever touching it: the body couples its plants (heat into rooms, the body's power swing onto its UPS and distribution), so a move on one muscle reaches the others. Holding the body's shared lines (its UPS and distribution) as one gauge every move answers to is the next engine item.

| Organism | Plants | Plants worse, v5 | Plants worse, v3 | The v5 plants (work change, extra decisions over the line, all seeds) |
|---|---:|---:|---:|---|
| Compute / AI / Cloud | 530 | 3 | 20 | 540 (+0.000%, +1); 541 (+0.000%, +1); 530 (+0.000%, +1) |
| Physics / Robotics / Autonomous | 394 | 2 | 34 | 538 (+0.000%, +1); 1110 (+0.000%, +1) |
| Energy / Facility / Industrial | 470 | 1 | 13 | 531 (+0.000%, +1) |
| Distribution / Specialized | 474 | 2 | 16 | 1111 (+0.000%, +1); 1113 (+0.000%, +1) |
| The four stacked, every shared muscle in each | 1868 | 8 | 83 | 540@compute_ai_cloud (+0.000%, +1); 541@compute_ai_cloud (+0.000%, +1); 538@physics_robotics_autonomous (+0.000%, +1); 1110@physics_robotics_autonomous (+0.000%, +1); 1111@distribution_specialized (+0.000%, +1); 531@energy_facility_industrial (+0.000%, +1); 1113@distribution_specialized (+0.000%, +1); 530@compute_ai_cloud (+0.000%, +1) |
| The whole tower, every muscle once | 1097 | 1 | 35 | 531 (+0.000%, +1) |

## Every muscle alone, by home realm

| Realm | Muscles | SUPERIOR WITHIN GUARDRAILS | ENERGY IMPROVEMENT WITH SERVICE TRADEOFF | NONINFERIOR / INCONCLUSIVE | NOT ESTABLISHED | WORSE | INVALID |
|---|---:|---:|---:|---:|---:|---:|---:|
| Compute / AI / Cloud | 434 | 29 | 0 | 405 | 0 | 0 | 0 |
| Physics / Robotics / Autonomous | 137 | 10 | 0 | 127 | 0 | 0 | 0 |
| Energy / Facility / Industrial | 249 | 88 | 0 | 161 | 0 | 0 | 0 |
| Distribution / Specialized | 277 | 13 | 0 | 264 | 0 | 0 | 0 |
| **All** | 1097 | **140** | **0** | **957** | **0** | **0** | **0** |

## No-harm check: muscles worse than native on any axis

- Omni acts on **208** of 1097 muscles; the rest are wired and watched but held native (no signal pushed where none helps).
- Muscles labelled **WORSE**: **0**.
- The v5 arm hands every knob back to native on the kill (the dead-man lease): 1097 of 1097 muscles, 6 of 6 organisms.

## Largest gains and largest losses (single muscles, by mean work per energy)

| Muscle | Family | Knob | Label | Work per energy | Work | Violations (pp) |
|---|---|---|---|---:|---:|---:|
| artifact_retention_ttl | CI/CD & Build Farms | setpoint | SUPERIOR WITHIN GUARDRAILS | +34.0% (+32.4 to +35.6) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| ros2_control_loop_rate | Robotics Motion Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.9% (+32.5 to +35.2) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| zswap_pool_fraction | Linux Kernel & OS Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.7% (+31.8 to +35.6) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| edge_sync_interval | Cross-Cluster, Multi-Region & Edge | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.6% (+31.9 to +35.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| tank_level_target | Industrial PLC & Process Automation | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.6% (+31.6 to +35.5) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| market_data_conflation_interval | Financial Markets & Trading Systems | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.4% (+32.0 to +34.8) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| transparent_hugepages | Linux Kernel & OS Control | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.4% (+31.5 to +35.3) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| segment_duration_target | Media Streaming & CDN | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.4% (+32.0 to +34.7) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| prefetch_aggressiveness | Content Delivery & Edge Cache | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.1% (+31.4 to +34.8) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| ttl_eviction_waste | Gut: Data-plane Intake & Waste | setpoint | SUPERIOR WITHIN GUARDRAILS | +33.1% (+31.3 to +34.9) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| humanoid_balance_margin | Robotics Motion Control | capacity | NONINFERIOR / INCONCLUSIVE | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| wind_turbine_yaw_offset | Renewable Generation & Inverter Control | capacity | NONINFERIOR / INCONCLUSIVE | -0.0% (-0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_replicas | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_route_weight | AI Inference Serving | setpoint | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_load | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_unload | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| model_instance_count | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| continuous_batching | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| max_batch_size | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |
| batch_queue_delay | AI Inference Serving | capacity | NONINFERIOR / INCONCLUSIVE | +0.0% (+0.0 to +0.0) | +0.0% (+0.0 to +0.0) | +0.0 (+0.0 to +0.0) |

Raw per-seed contrasts: `REALMS_V5.json`. One row per muscle: `MUSCLES_V5.csv`. Fingerprints: `RUN.json`, `SHA256SUMS.txt`.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
