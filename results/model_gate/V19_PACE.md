# The model gate: the candidate against the engine that stands, in our own models

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Seeds 1 to 8, 1.0 day each where a day is run; the standing engine omni-v18, the candidate differs from omni-v18: omni_controller/controller.py, omni_controller/muscles.py, omnicompass/nervous.py. Evidence class S, our own models: a reading here says whether a change shows promise before a real run, never what a benchmark found. Each candidate reading is paired by seed with the standing engine's (the mean change, its 95% interval over the seeds, the word by the gauge's aim: tools/readings.py).

## pace_cloud

The cloud setting on the plant that moves every 5 s; the candidate decides every 60 s, each faster pace read against a decision every 60 s and against native.

A decision every 60 s against native:

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| machine_hours | 133.076 | 133.076 | 0.00% STEADY (identical) |
| kwh_per_core_hour | 0.036 | 0.036 | 0.00% STEADY (identical) |
| pending_pod_minutes_per_hour | 8.183 | 8.183 | 0.00% STEADY (identical) |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.202 | 0.00% STEADY (identical) |
| p95_ms | 79.937 | 79.937 | 0.00% STEADY (identical) |
| alert_minutes | 27.000 | 27.000 | 0.00% STEADY (identical) |
| power_cap_moves | 0.000 | 37.500 | power given |
| power_cap_reversals | 0.000 | 36.500 | power given |
| power_cap_travel | 0.000 | 11.438 | power given |
| governor_cpu_s_per_hour | 0.000 | 1.484 |  |
| reads_per_hour | 0.000 | 1627.927 |  |

Counts over all seeds, by decision period: decisions {'60': 11520}, machines_parked {'60': 8339}, errors {'60': 0}, steps_allowed {'60': 61}, steps_refused {'60': 69}, trials_abandoned {'60': 26}

## pace_kind

The kind setting on the plant that moves every 5 s; the candidate decides every 60 s, each faster pace read against a decision every 60 s and against native.

A decision every 60 s against native:

| Gauge | Native | Every 60 s | Against native |
|---|---:|---:|---|
| machine_hours | 133.076 | 143.263 | 7.65% power given |
| kwh_per_core_hour | 0.036 | 0.037 | 4.86% power given |
| pending_pod_minutes_per_hour | 8.183 | 7.757 | 5.20% GAIN |
| hpa_shortfall_minutes_per_hour | 1.202 | 1.188 | 1.23% GAIN |
| p95_ms | 79.937 | 74.405 | 6.92% GAIN |
| alert_minutes | 27.000 | 19.625 | 27.31% GAIN |
| power_cap_moves | 0.000 | 27.750 | power given |
| power_cap_reversals | 0.000 | 26.750 | power given |
| power_cap_travel | 0.000 | 8.464 | power given |
| governor_cpu_s_per_hour | 0.000 | 1.744 |  |
| reads_per_hour | 0.000 | 1787.542 |  |

Counts over all seeds, by decision period: decisions {'60': 11520}, machines_parked {'60': 7957}, errors {'60': 22}, steps_allowed {'60': 50}, steps_refused {'60': 71}, trials_abandoned {'60': 11}

Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results.

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
