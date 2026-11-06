# How steadily the governor steered: its own moves on every omni-v11 Kubernetes table

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Evidence class L, the omni arm only (native has no governor): shown, not judged. Each cell is the omni arm's own gauge per hour of its audit, averaged over the run's repetitions, for runs A / B / C of the table named; the runs are never pooled. A recommendation is what a decision asks for; a write is a command that changed a setting. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Made by `tools/steering.py` from the archived audits; the same gauges are served live by `tools/omni_exporter.py`.

## On top of Goldilocks and the VPA's recommender (`results/live/V11_GOLDILOCKS.md`)

Runs 39171064099, 39175675418, 39177950720; 10, 10 and 10 omni repetitions.

| Gauge | A | B | C |
|---|---:|---:|---:|
| decisions an hour | 63.6 | 63.6 | 63.7 |
| settings commands written an hour | 67.5 | 72.1 | 74.3 |
| HPA target recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| HPA target recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| power cap recommendation: moves an hour (not written on Kubernetes) | 1.7 | 0.0 | 2.5 |
| power cap recommendation: reversals an hour (not written on Kubernetes) | 0.8 | 0.0 | 1.3 |
| HPA target recommendation: distance travelled an hour | 0.000 | 0.000 | 0.000 |
| machines recommendation: distance travelled an hour | 0.00 | 0.00 | 0.00 |
| decisions with the compass in its band (%) | 78.0 | 54.0 | 48.0 |
| decisions with the compass under its lower cushion, the service far from its line (%) | 14.0 | 40.0 | 43.3 |
| decisions with the compass at or past the line (%) | 8.0 | 6.0 | 8.7 |
| time from the line back into the band, mean (s) | 61 | 61 | 61 |
| time from the line back into the band, longest (s) | 62 | 61 | 61 |
| errors recorded an hour | 0.0 | 0.0 | 0.0 |
| decision time, mean (s) | 0.36 | 0.35 | 0.32 |
| decision time, longest (s) | 0.63 | 0.54 | 0.57 |
| the governor's own processor (cores) | 0.0082 | 0.0079 | 0.0074 |

Writes an hour by the head of their reason, run A: convey 59.0; record original target 4.2; HPA target 4.2.

## On top of KEDA's HTTP add-on (`results/live/V11_KEDA_REQUESTS.md`)

Runs 39173411511, 39176842679, 39180252225; 10, 10 and 10 omni repetitions.

| Gauge | A | B | C |
|---|---:|---:|---:|
| decisions an hour | 63.5 | 63.6 | 63.6 |
| settings commands written an hour | 19.9 | 17.4 | 17.4 |
| HPA target recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| HPA target recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| power cap recommendation: moves an hour (not written on Kubernetes) | 0.8 | 0.0 | 0.0 |
| power cap recommendation: reversals an hour (not written on Kubernetes) | 0.4 | 0.0 | 0.0 |
| HPA target recommendation: distance travelled an hour | 0.000 | 0.000 | 0.000 |
| machines recommendation: distance travelled an hour | 0.00 | 0.00 | 0.00 |
| decisions with the compass in its band (%) | 66.7 | 49.3 | 69.3 |
| decisions with the compass under its lower cushion, the service far from its line (%) | 26.7 | 44.7 | 24.7 |
| decisions with the compass at or past the line (%) | 6.7 | 6.0 | 6.0 |
| time from the line back into the band, mean (s) | 61 | 61 | 61 |
| time from the line back into the band, longest (s) | 61 | 61 | 61 |
| errors recorded an hour | 0.0 | 0.0 | 0.0 |
| decision time, mean (s) | 0.52 | 0.45 | 0.48 |
| decision time, longest (s) | 1.21 | 0.76 | 0.73 |
| the governor's own processor (cores) | 0.0097 | 0.0087 | 0.0094 |

Writes an hour by the head of their reason, run A: convey 19.9.

## On top of KEDA on CPU and requests (`results/live/V11_KEDA_CPU_REQUESTS.md`)

Runs 39173411511, 39176842679, 39180252225; 10, 10 and 10 omni repetitions.

| Gauge | A | B | C |
|---|---:|---:|---:|
| decisions an hour | 63.3 | 63.3 | 63.3 |
| settings commands written an hour | 76.0 | 76.0 | 74.7 |
| HPA target recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| HPA target recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| power cap recommendation: moves an hour (not written on Kubernetes) | 3.4 | 0.8 | 0.0 |
| power cap recommendation: reversals an hour (not written on Kubernetes) | 1.7 | 0.4 | 0.0 |
| HPA target recommendation: distance travelled an hour | 0.000 | 0.000 | 0.000 |
| machines recommendation: distance travelled an hour | 0.00 | 0.00 | 0.00 |
| decisions with the compass in its band (%) | 53.3 | 58.7 | 68.0 |
| decisions with the compass under its lower cushion, the service far from its line (%) | 39.3 | 36.0 | 28.0 |
| decisions with the compass at or past the line (%) | 7.3 | 5.3 | 4.0 |
| time from the line back into the band, mean (s) | 62 | 62 | 62 |
| time from the line back into the band, longest (s) | 62 | 62 | 62 |
| errors recorded an hour | 0.0 | 0.0 | 0.0 |
| decision time, mean (s) | 0.62 | 0.61 | 0.61 |
| decision time, longest (s) | 2.51 | 2.22 | 2.16 |
| the governor's own processor (cores) | 0.0113 | 0.0117 | 0.0120 |

Writes an hour by the head of their reason, run A: convey 67.6; record original target 4.2; HPA target 4.2.

## Fixed capacity, four caps (`results/live/V11_CAPACITY.md`)

Runs 39171068872, 39175679247, 39179020367; 20, 20 and 20 omni repetitions.

| Gauge | A | B | C |
|---|---:|---:|---:|
| decisions an hour | 61.5 | 61.5 | 61.5 |
| settings commands written an hour | 966.7 | 997.9 | 986.0 |
| HPA target recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| HPA target recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| power cap recommendation: moves an hour (not written on Kubernetes) | 5.8 | 7.7 | 6.6 |
| power cap recommendation: reversals an hour (not written on Kubernetes) | 3.2 | 4.8 | 3.7 |
| HPA target recommendation: distance travelled an hour | 0.000 | 0.000 | 0.000 |
| machines recommendation: distance travelled an hour | 0.00 | 0.00 | 0.00 |
| decisions with the compass in its band (%) | 35.0 | 41.0 | 39.0 |
| decisions with the compass under its lower cushion, the service far from its line (%) | 11.5 | 1.8 | 5.2 |
| decisions with the compass at or past the line (%) | 53.5 | 57.2 | 55.8 |
| time from the line back into the band, mean (s) | 65 | 64 | 66 |
| time from the line back into the band, longest (s) | 74 | 68 | 71 |
| errors recorded an hour | 940.0 | 966.9 | 961.1 |
| decision time, mean (s) | 0.59 | 0.62 | 0.60 |
| decision time, longest (s) | 1.06 | 1.10 | 0.99 |
| the governor's own processor (cores) | 0.0222 | 0.0232 | 0.0227 |

Writes an hour by the head of their reason, run A: convey 943.1; rollout 10.1; replica room 5.2; record original target 4.2.

## The governor killed outright mid-run (`results/live/V11_ROBUST_KILL.md`)

Runs 39173416105, 39177935888, 39182898753; 10, 10 and 10 omni repetitions.

| Gauge | A | B | C |
|---|---:|---:|---:|
| decisions an hour | 56.5 | 56.6 | 56.7 |
| settings commands written an hour | 194.9 | 195.5 | 214.4 |
| HPA target recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| HPA target recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| power cap recommendation: moves an hour (not written on Kubernetes) | 13.9 | 13.5 | 12.6 |
| power cap recommendation: reversals an hour (not written on Kubernetes) | 9.6 | 9.6 | 8.3 |
| HPA target recommendation: distance travelled an hour | 0.000 | 0.000 | 0.000 |
| machines recommendation: distance travelled an hour | 0.00 | 0.00 | 0.00 |
| decisions with the compass in its band (%) | 26.2 | 30.0 | 32.3 |
| decisions with the compass under its lower cushion, the service far from its line (%) | 4.6 | 6.9 | 12.3 |
| decisions with the compass at or past the line (%) | 69.2 | 63.1 | 55.4 |
| time from the line back into the band, mean (s) | 128 | 159 | 132 |
| time from the line back into the band, longest (s) | 192 | 256 | 205 |
| errors recorded an hour | 0.0 | 0.0 | 0.0 |
| decision time, mean (s) | 1.61 | 1.46 | 1.30 |
| decision time, longest (s) | 3.67 | 3.30 | 3.21 |
| the governor's own processor (cores) | 0.0133 | 0.0126 | 0.0132 |

Writes an hour by the head of their reason, run A: convey 74.5; reset 60.0; rollout 34.8; record original target 12.2.

## The long run, two hours an arm (`results/live/V11_ROBUST_LONG.md`)

Runs 39173420146, 39177939062, 39182902844; 3, 3 and 3 omni repetitions.

| Gauge | A | B | C |
|---|---:|---:|---:|
| decisions an hour | 58.1 | 58.1 | 57.7 |
| settings commands written an hour | 88.0 | 95.6 | 63.5 |
| HPA target recommendation: moves an hour | 12.0 | 6.6 | 3.2 |
| HPA target recommendation: reversals an hour | 5.8 | 3.2 | 2.2 |
| machines recommendation: moves an hour | 0.0 | 0.0 | 0.0 |
| machines recommendation: reversals an hour | 0.0 | 0.0 | 0.0 |
| power cap recommendation: moves an hour (not written on Kubernetes) | 20.9 | 19.6 | 21.4 |
| power cap recommendation: reversals an hour (not written on Kubernetes) | 20.4 | 19.1 | 20.9 |
| HPA target recommendation: distance travelled an hour | 0.169 | 0.087 | 0.051 |
| machines recommendation: distance travelled an hour | 0.00 | 0.00 | 0.00 |
| decisions with the compass in its band (%) | 34.5 | 31.1 | 21.0 |
| decisions with the compass under its lower cushion, the service far from its line (%) | 3.1 | 3.4 | 0.0 |
| decisions with the compass at or past the line (%) | 62.4 | 65.6 | 79.0 |
| time from the line back into the band, mean (s) | 337 | 317 | 406 |
| time from the line back into the band, longest (s) | 607 | 647 | 777 |
| errors recorded an hour | 0.0 | 0.0 | 0.0 |
| decision time, mean (s) | 1.48 | 1.54 | 1.82 |
| decision time, longest (s) | 4.30 | 4.46 | 4.91 |
| the governor's own processor (cores) | 0.0104 | 0.0108 | 0.0107 |

Writes an hour by the head of their reason, run A: convey 41.5; rollout 27.9; reset 10.6; record original target 3.2.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
