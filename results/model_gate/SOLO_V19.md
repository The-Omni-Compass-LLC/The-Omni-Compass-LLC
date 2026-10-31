# Omni-Compass by itself on the model cluster (omni-v19)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- read again by the rule of 24 October 2026 (tools/reread_key.py) -->
**Read again by the founder's rule of 24 October 2026** (tools/reread_key.py (since folded into tools/readings.py); the one rule, `tools/readings.py` judge_one, as `tools/model_gate.py` reads a model now): a paired change of 0.5% or more either way is a change and never reads STEADY; it reads its word by the gauge's aim, with "(not clear of the noise)" beside it where its 95% interval over the seeds crosses zero; under 0.5% it reads STEADY, under the floor. Each reading was decided again from the JSON twin's own mean, interval and relative change, and every row whose words moved is printed again, its numbers wearing their words' signs; every seed, number and row is as first written. Where a paragraph below says STEADY for an interval across zero, this rule replaces it. Evidence class S, our own models, never a benchmark result.
<!-- end: read again -->

Our own model (evidence class S), never a benchmark result. The founder's order of 23 October: beside native and Omni-Compass and native, a third arm, Omni-Compass by itself, with native's controllers switched off (`docs/SOLO_PREREGISTRATION.md`). This page reads what the engine that stands does by itself on the model cluster: 8 seeds of a day, the same seeds in every arm, read by the model gate's own rule (`tools/model_gate.py`: the mean change over the seeds, its 95% interval by Student t, the word by the gauge's aim; a resource that rose is power given).

Engine: omni-v19 (digest 36ee67284c035235, 62 files). Written by `python3 tools/solo_study.py`; every seed's reading of every arm is in its JSON twin (`per_seed`).

| Arm | What governs |
|---|---|
| native | the pod autoscaler (its target 70%), as Kubernetes ships it, on the machines as the kind rig has them (every worker made at the start, no Cluster Autoscaler: 12 machines) |
| Omni-Compass and native | the shipped governor on top of the pod autoscaler, the compass law at the max (as ARM=compass runs it), on the same 12 machines |
| Omni-Compass by itself | the pod autoscaler switched off: every workload's pods at the operator's own count unless the governor writes it through the workload's own scale, the pool at its starting size (12 machines); the shipped governor the only controller, the compass law at the max |

## The means over the seeds

| Gauge | native | Omni-Compass and native | Omni-Compass by itself |
|---|---:|---:|---:|
| machine-hours | 288.000 | 288.000 | 288.000 |
| energy per used core-hour (kWh) | 0.063 | 0.063 | 0.063 |
| pods waiting for a place (pod-minutes an hour) | 0.000 | 0.000 | 0.000 |
| the pod autoscaler's shortfall (minutes an hour) | 3.585 | 3.625 | 0.000 |
| 95th percentile response (ms) | 79.955 | 76.750 | 64.443 |
| minutes over the response line | 26.375 | 22.000 | 9.250 |

## Omni-Compass by itself against native

| Gauge | Change | 95% interval | Reading |
|---|---:|---:|---|
| machine-hours | =0.0% | ±0.0% to ±0.0% | **STEADY (identical)** |
| energy per used core-hour (kWh) | =0.0% | −0.0% to +0.0% | **STEADY, under the floor** |
| pods waiting for a place (pod-minutes an hour) | — | — | **STEADY (identical)** |
| the pod autoscaler's shortfall (minutes an hour) | — | — | not read: by itself there is no pod autoscaler to fall short |
| 95th percentile response (ms) | +19.4% | +12.2% to +26.6% | **GAIN** |
| minutes over the response line | +64.9% | +32.4% to +97.5% | **GAIN** |

## Omni-Compass by itself against Omni-Compass and native

| Gauge | Change | 95% interval | Reading |
|---|---:|---:|---|
| machine-hours | =0.0% | ±0.0% to ±0.0% | **STEADY (identical)** |
| energy per used core-hour (kWh) | =0.0% | −0.0% to +0.0% | **STEADY, under the floor** |
| pods waiting for a place (pod-minutes an hour) | — | — | **STEADY (identical)** |
| the pod autoscaler's shortfall (minutes an hour) | — | — | not read: by itself there is no pod autoscaler to fall short |
| 95th percentile response (ms) | +16.0% | +9.9% to +22.2% | **GAIN** |
| minutes over the response line | +58.0% | +25.8% to +90.1% | **GAIN** |

## Omni-Compass and native against native

| Gauge | Change | 95% interval | Reading |
|---|---:|---:|---|
| machine-hours | =0.0% | ±0.0% to ±0.0% | **STEADY (identical)** |
| energy per used core-hour (kWh) | =0.0% | −0.0% to +0.0% | **STEADY, under the floor** |
| pods waiting for a place (pod-minutes an hour) | — | — | **STEADY (identical)** |
| the pod autoscaler's shortfall (minutes an hour) | −1.1% | −3.3% to +5.5% | **LOSS (not clear of the noise)** |
| 95th percentile response (ms) | +4.0% | +2.5% to +5.5% | **GAIN** |
| minutes over the response line | +16.6% | +2.6% to +30.6% | **GAIN** |

## What it says

On the engine that stands (omni-v19) the governor has a pod muscle of its own (`--own-replicas`, omni-v19): with the pod autoscaler switched off it sets each named workload's pods itself, through the workload's own scale, at the target the compass moves, reconciled every 15 s on the fast checks: its 95th percentile response 64 ms and 9.2 minutes over the line in the day, against native's 80.0 ms and 26.4 minutes, on the same machines.

Our own model, class S: it shows the mechanism, never a benchmark result. The real arm runs on kind (`ARM=solo`, `scripts/kind_bench.sh`) on omni-v19, the engine that carries the muscle (`docs/SOLO_PREREGISTRATION.md`).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
