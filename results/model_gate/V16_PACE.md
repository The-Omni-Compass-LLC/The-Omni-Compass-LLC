# The model gate: the candidate against the engine that stands, in our own models

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Seeds 1 to 8, 1.0 day each where a day is run; the standing engine omni-v15, the candidate omni-v16. Evidence class S, our own models: a reading here says whether a change shows promise before a real run, never what a benchmark found. Each candidate reading is paired by seed with the standing engine's (the mean change, its 95% interval over the seeds, the word by the gauge's aim: tools/readings.py).

The pace study of omni-v16 (`docs/OMNI_V16.md`; `docs/PACE_PREREGISTRATION.md`, read before any real run): the candidate alone on a plant that moves every 5 s (the model cluster's step cut to 5 s, three of them to one of the 15 s steps the other models take), a full decision every 60, 15, 10 and 5 s, eight seeds of a day each; each faster pace is paired by seed against the same engine deciding every 60 s, every engine's period before omni-v16, and against native. Two settings: the cloud's (the compass law at the tune-down, the machines alone, `--give-back-only`) and the kind benchmark's (the compass law at the max, every autoscaler sensed). The standing engine named above is not run here. Each run sets its decision period and its fast checks' period on the command line, so it reads the same on omni-v16 as landed, whose one other byte against the tree these runs used is the parser's default period, 15 s since the founder's word of 22 October ("15 sec all over heart beat"; the default as shipped is read in `results/model_gate/V16_VS_V15.md`, model `cluster_shipped`). A row against native that reads LOSS here is the engine's at every pace, the old 60 s default included, and is on the next version's list (`docs/CHANGE_CONTROL.md`).

## pace_cloud

The cloud setting on the plant that moves every 5 s; the candidate decides every 60, 15, 10, 5 s, each faster pace read against a decision every 60 s and against native.

A decision every 60 s against native:

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| machine_hours | 133.076 | 131.983 | 0.82% GAIN |
| kwh_per_core_hour | 0.036 | 0.035 | 1.95% GAIN |
| pending_pod_minutes_per_hour | 8.183 | 20.883 | 155.21% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.205 | 0.22% STEADY |
| p95_ms | 79.937 | 80.333 | 0.49% STEADY |
| alert_minutes | 27.000 | 27.500 | 1.85% LOSS |
| power_cap_moves | 0.000 | 63.500 | power given |
| power_cap_reversals | 0.000 | 62.500 | power given |
| power_cap_travel | 0.000 | 19.225 | power given |
| governor_cpu_s_per_hour | 0.000 | 1.686 |  |
| reads_per_hour | 0.000 | 1653.792 |  |

A decision every 15 s:

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| machine_hours | 133.076 | 131.983 | 131.483 | 0.38% STEADY | 1.20% GAIN |
| kwh_per_core_hour | 0.036 | 0.035 | 0.034 | 2.57% GAIN | 4.46% GAIN |
| pending_pod_minutes_per_hour | 8.183 | 20.883 | 18.361 | 12.08% GAIN | 124.39% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.205 | 1.203 | 0.18% STEADY | 0.04% STEADY |
| p95_ms | 79.937 | 80.333 | 80.313 | 0.02% STEADY | 0.47% STEADY |
| alert_minutes | 27.000 | 27.500 | 27.625 | 0.45% STEADY | 2.31% LOSS |
| power_cap_moves | 0.000 | 63.500 | 104.125 | 63.98% power given | power given |
| power_cap_reversals | 0.000 | 62.500 | 101.625 | 62.60% power given | power given |
| power_cap_travel | 0.000 | 19.225 | 31.005 | 61.27% power given | power given |
| governor_cpu_s_per_hour | 0.000 | 1.686 | 2.682 | 59.14% power given |  |
| reads_per_hour | 0.000 | 1653.792 | 2189.375 | 32.39% power given |  |

A decision every 10 s:

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| machine_hours | 133.076 | 131.983 | 133.402 | 1.08% power given | 0.24% STEADY |
| kwh_per_core_hour | 0.036 | 0.035 | 0.035 | 1.12% GAIN | 3.04% GAIN |
| pending_pod_minutes_per_hour | 8.183 | 20.883 | 15.923 | 23.75% GAIN | 94.59% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.205 | 1.203 | 0.14% STEADY | 0.07% STEADY |
| p95_ms | 79.937 | 80.333 | 80.109 | 0.28% STEADY | 0.21% STEADY |
| alert_minutes | 27.000 | 27.500 | 27.125 | 1.36% GAIN | 0.46% STEADY |
| power_cap_moves | 0.000 | 63.500 | 115.875 | 82.48% power given | power given |
| power_cap_reversals | 0.000 | 62.500 | 113.625 | 81.80% power given | power given |
| power_cap_travel | 0.000 | 19.225 | 33.954 | 76.61% power given | power given |
| governor_cpu_s_per_hour | 0.000 | 1.686 | 3.379 | 100.45% power given |  |
| reads_per_hour | 0.000 | 1653.792 | 2538.521 | 53.50% power given |  |

A decision every 5 s:

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| machine_hours | 133.076 | 131.983 | 129.670 | 1.75% GAIN | 2.56% GAIN |
| kwh_per_core_hour | 0.036 | 0.035 | 0.034 | 1.79% GAIN | 3.70% GAIN |
| pending_pod_minutes_per_hour | 8.183 | 20.883 | 16.516 | 20.91% GAIN | 101.84% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.205 | 1.204 | 0.11% STEADY | 0.11% STEADY |
| p95_ms | 79.937 | 80.333 | 80.178 | 0.19% STEADY | 0.30% STEADY |
| alert_minutes | 27.000 | 27.500 | 27.500 | 0.00% STEADY | 1.85% LOSS |
| power_cap_moves | 0.000 | 63.500 | 114.375 | 80.12% power given | power given |
| power_cap_reversals | 0.000 | 62.500 | 111.875 | 79.00% power given | power given |
| power_cap_travel | 0.000 | 19.225 | 33.278 | 73.10% power given | power given |
| governor_cpu_s_per_hour | 0.000 | 1.686 | 5.514 | 227.12% power given |  |
| reads_per_hour | 0.000 | 1653.792 | 3600.500 | 117.71% power given |  |

Counts over all seeds, by decision period: decisions {'60': 11520, '15': 46080, '10': 69120, '5': 138240}, machines_parked {'60': 1486, '15': 1712, '10': 1706, '5': 1654}, errors {'60': 0, '15': 0, '10': 0, '5': 0}, steps_allowed {'60': 54, '15': 73, '10': 67, '5': 66}, steps_refused {'60': 78, '15': 68, '10': 76, '5': 78}, trials_abandoned {'60': 125, '15': 259, '10': 137, '5': 127}

## pace_kind

The kind setting on the plant that moves every 5 s; the candidate decides every 60, 15, 10, 5 s, each faster pace read against a decision every 60 s and against native.

A decision every 60 s against native:

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| machine_hours | 133.076 | 151.289 | 13.69% power given |
| kwh_per_core_hour | 0.036 | 0.039 | 8.58% power given |
| pending_pod_minutes_per_hour | 8.183 | 31.960 | 290.57% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.187 | 1.26% GAIN |
| p95_ms | 79.937 | 77.184 | 3.44% GAIN |
| alert_minutes | 27.000 | 23.750 | 12.04% GAIN |
| power_cap_moves | 0.000 | 33.250 | power given |
| power_cap_reversals | 0.000 | 32.250 | power given |
| power_cap_travel | 0.000 | 10.141 | power given |
| governor_cpu_s_per_hour | 0.000 | 1.581 |  |
| reads_per_hour | 0.000 | 1643.500 |  |

A decision every 15 s:

| Gauge | Native | Every 60 s | Every 15 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| machine_hours | 133.076 | 151.289 | 151.781 | 0.33% STEADY | 14.06% power given |
| kwh_per_core_hour | 0.036 | 0.039 | 0.039 | 0.30% STEADY | 8.91% power given |
| pending_pod_minutes_per_hour | 8.183 | 31.960 | 33.506 | 4.84% LOSS | 309.47% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.187 | 1.138 | 4.13% GAIN | 5.34% GAIN |
| p95_ms | 79.937 | 77.184 | 76.929 | 0.33% STEADY | 3.76% GAIN |
| alert_minutes | 27.000 | 23.750 | 20.250 | 14.74% GAIN | 25.00% GAIN |
| power_cap_moves | 0.000 | 33.250 | 33.375 | 0.38% STEADY | power given |
| power_cap_reversals | 0.000 | 32.250 | 32.375 | 0.39% STEADY | power given |
| power_cap_travel | 0.000 | 10.141 | 10.179 | 0.38% STEADY | power given |
| governor_cpu_s_per_hour | 0.000 | 1.581 | 2.657 | 68.11% power given |  |
| reads_per_hour | 0.000 | 1643.500 | 2187.083 | 33.07% power given |  |

A decision every 10 s:

| Gauge | Native | Every 60 s | Every 10 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| machine_hours | 133.076 | 151.289 | 149.172 | 1.40% GAIN | 12.10% power given |
| kwh_per_core_hour | 0.036 | 0.039 | 0.038 | 0.92% GAIN | 7.58% power given |
| pending_pod_minutes_per_hour | 8.183 | 31.960 | 28.799 | 9.89% GAIN | 251.95% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.187 | 1.116 | 6.00% GAIN | 7.18% GAIN |
| p95_ms | 79.937 | 77.184 | 76.847 | 0.44% STEADY | 3.87% GAIN |
| alert_minutes | 27.000 | 23.750 | 19.375 | 18.42% GAIN | 28.24% GAIN |
| power_cap_moves | 0.000 | 33.250 | 32.875 | 1.13% GAIN | power given |
| power_cap_reversals | 0.000 | 32.250 | 31.875 | 1.16% GAIN | power given |
| power_cap_travel | 0.000 | 10.141 | 10.027 | 1.13% GAIN | power given |
| governor_cpu_s_per_hour | 0.000 | 1.581 | 3.432 | 117.14% power given |  |
| reads_per_hour | 0.000 | 1643.500 | 2539.229 | 54.50% power given |  |

A decision every 5 s:

| Gauge | Native | Every 60 s | Every 5 s | Against every 60 s | Against native |
|---|---:|---:|---:|---|---|
| machine_hours | 133.076 | 151.289 | 149.673 | 1.07% GAIN | 12.47% power given |
| kwh_per_core_hour | 0.036 | 0.039 | 0.039 | 0.66% GAIN | 7.86% power given |
| pending_pod_minutes_per_hour | 8.183 | 31.960 | 28.553 | 10.66% GAIN | 248.94% LOSS |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.187 | 1.118 | 5.78% GAIN | 6.97% GAIN |
| p95_ms | 79.937 | 77.184 | 76.884 | 0.39% STEADY | 3.82% GAIN |
| alert_minutes | 27.000 | 23.750 | 19.375 | 18.42% GAIN | 28.24% GAIN |
| power_cap_moves | 0.000 | 33.250 | 33.625 | 1.13% power given | power given |
| power_cap_reversals | 0.000 | 32.250 | 32.625 | 1.16% power given | power given |
| power_cap_travel | 0.000 | 10.141 | 10.256 | 1.13% power given | power given |
| governor_cpu_s_per_hour | 0.000 | 1.581 | 5.548 | 250.98% power given |  |
| reads_per_hour | 0.000 | 1643.500 | 3600.500 | 119.08% power given |  |

Counts over all seeds, by decision period: decisions {'60': 11520, '15': 46080, '10': 69120, '5': 138240}, machines_parked {'60': 329, '15': 338, '10': 357, '5': 341}, errors {'60': 0, '15': 0, '10': 0, '5': 0}, steps_allowed {'60': 56, '15': 68, '10': 65, '5': 80}, steps_refused {'60': 85, '15': 88, '10': 90, '5': 87}, trials_abandoned {'60': 21, '15': 12, '10': 7, '5': 15}

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
