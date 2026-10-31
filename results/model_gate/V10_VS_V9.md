# The model gate: the candidate against the engine that stands, in our own models

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Seeds 1 to 8, 1.0 day each where a day is run; the standing engine omni-v9, the candidate omni-v10. Evidence class S, our own models: a reading here says whether a change shows promise before a real run, never what a benchmark found. Each candidate reading is paired by seed with the standing engine's (the mean change, its 95% interval over the seeds, the word by the gauge's aim: tools/readings.py).

## cluster (a decision every 60 s)

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| machine_hours | 133.057 | 131.119 | 131.119 | 0.00% STEADY (identical) | 1.46% GAIN | 1.46% GAIN |
| kwh_per_core_hour | 0.036 | 0.035 | 0.035 | 0.00% STEADY (identical) | 2.71% GAIN | 2.71% GAIN |
| pending_pod_minutes_per_hour | 7.311 | 22.651 | 22.651 | 0.00% STEADY (identical) | 209.81% LOSS | 209.81% LOSS |
| hpa_shortfall_minutes_per_hour | 3.605 | 3.612 | 3.612 | 0.00% STEADY (identical) | 0.18% STEADY | 0.18% STEADY |
| p95_ms | 80.147 | 80.653 | 80.653 | 0.00% STEADY (identical) | 0.63% LOSS | 0.63% LOSS |
| alert_minutes | 26.625 | 27.125 | 27.125 | 0.00% STEADY (identical) | 1.88% LOSS | 1.88% LOSS |

Counts over all seeds: steps_allowed {'base': 54, 'cand': 54}, steps_refused {'base': 77, 'cand': 77}, trials_abandoned {'base': 136, 'cand': 136}, machines_parked {'base': 1464, 'cand': 1464}, errors {'base': 0, 'cand': 0}

## cluster15 (a decision every 15 s)

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| machine_hours | 133.057 | 133.505 | 133.505 | 0.00% STEADY (identical) | 0.34% STEADY | 0.34% STEADY |
| kwh_per_core_hour | 0.036 | 0.035 | 0.035 | 0.00% STEADY (identical) | 3.19% GAIN | 3.19% GAIN |
| pending_pod_minutes_per_hour | 7.311 | 15.480 | 15.480 | 0.00% STEADY (identical) | 111.74% LOSS | 111.74% LOSS |
| hpa_shortfall_minutes_per_hour | 3.605 | 3.605 | 3.605 | 0.00% STEADY (identical) | 0.00% STEADY | 0.00% STEADY |
| p95_ms | 80.147 | 80.413 | 80.413 | 0.00% STEADY (identical) | 0.33% STEADY | 0.33% STEADY |
| alert_minutes | 26.625 | 27.000 | 27.000 | 0.00% STEADY (identical) | 1.41% LOSS | 1.41% LOSS |

Counts over all seeds: steps_allowed {'base': 63, 'cand': 63}, steps_refused {'base': 70, 'cand': 70}, trials_abandoned {'base': 225, 'cand': 225}, machines_parked {'base': 4212, 'cand': 4212}, errors {'base': 0, 'cand': 0}

## convey

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| requests_served | 31419.002 | 51593.967 | 51593.967 | 0.00% STEADY (identical) | 64.21% GAIN | 64.21% GAIN |
| start_wait_s | 9.787 | 10.667 | 10.667 | 0.00% STEADY (identical) | 8.99% LOSS | 8.99% LOSS |
| start_wait_p95_s | 10.000 | 11.000 | 11.000 | 0.00% STEADY (identical) | 10.00% LOSS | 10.00% LOSS |
| p95_ms | 228.740 | 107.294 | 107.294 | 0.00% STEADY (identical) | 53.09% GAIN | 53.09% GAIN |
| alert_minutes | 0.000 | 0.000 | 0.000 | STEADY (identical) | STEADY (identical) | STEADY (identical) |
| host_busy | 0.282 | 0.371 | 0.371 | 0.00% STEADY (identical) | 31.53% power given | 31.53% power given |
| limit_given_m | 4134.375 | 11062.167 | 11062.167 | 0.00% STEADY (identical) | 167.57% power given | 167.57% power given |
| pod_seconds | 29767.500 | 35178.750 | 35178.750 | 0.00% STEADY (identical) | 18.18% power given | 18.18% power given |

Counts over all seeds: starts {'native': 216, 'base': 168, 'cand': 168}, starts_past_75 {'native': 0, 'base': 0, 'cand': 0}

## convey_unreadable_quota

| Gauge | Native | Standing | Candidate | Candidate against standing | Standing against native | Candidate against native |
|---|---:|---:|---:|---|---|---|
| requests_served | 31419.002 | 51593.967 | 51593.967 | 0.00% STEADY (identical) | 64.21% GAIN | 64.21% GAIN |
| start_wait_s | 9.787 | 10.667 | 10.667 | 0.00% STEADY (identical) | 8.99% LOSS | 8.99% LOSS |
| start_wait_p95_s | 10.000 | 11.000 | 11.000 | 0.00% STEADY (identical) | 10.00% LOSS | 10.00% LOSS |
| p95_ms | 228.740 | 107.294 | 107.294 | 0.00% STEADY (identical) | 53.09% GAIN | 53.09% GAIN |
| alert_minutes | 0.000 | 0.000 | 0.000 | STEADY (identical) | STEADY (identical) | STEADY (identical) |
| host_busy | 0.282 | 0.371 | 0.371 | 0.00% STEADY (identical) | 31.53% power given | 31.53% power given |
| limit_given_m | 4134.375 | 11062.167 | 11062.167 | 0.00% STEADY (identical) | 167.57% power given | 167.57% power given |
| pod_seconds | 29767.500 | 35178.750 | 35178.750 | 0.00% STEADY (identical) | 18.18% power given | 18.18% power given |

Counts over all seeds: starts {'native': 216, 'base': 168, 'cand': 168}, starts_past_75 {'native': 0, 'base': 0, 'cand': 0}

## verdict

20 pieces of work a decision, their log spread 0.25:

| True extra cost of a give-back step | Allowed, standing | Allowed, candidate |
|---|---|---|
| +0% | 60% | 60% |
| +1% | 50% | 50% |
| +2% | 39% | 39% |
| +3% | 28% | 28% |
| +5% | 14% | 14% |

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

**Correction (18 October).** This gate ran both arms on the candidate's engine. From omni-v9's gate on, `tools/model_gate.py` put its own tree ahead of the checkout under test, so the standing arm imported the candidate's code too. omni-v10 changed no file any model reads (only the CityLearn runner), so the reading above, identical on every model, holds by construction all the same. The gate now places the checkout under test first, and every worker names the tree its engine came from; a reading taken on the wrong tree is refused (`results/model_gate/V11_VS_V10.md` is the first gate run that way).

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
