# Bake-off that was actually run

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Covering public set: HPA v2, PID, deadband threshold.
Same 15 s metric. Same replica bounds 1–40.

`frac_over_target` is a property of the frozen metric stream. It does not score SLO.

## PlanetLab recorded (9 traces, mean metric 0.086)

| Controller | Replica-hours | Scale events | Energy proxy |
|---|---|---|---|
| HPA 0.70 | 24.12 | 0.44 | 2.885 |
| Omni observe | 24.12 | 0.44 | 2.885 |
| Omni target | 24.09 | 0.44 | 2.884 |
| PID | 24.01 | 0.33 | 2.880 |
| Deadband | 24.01 | 2.00 | 2.881 |

Everyone sits at one replica.

## Synthetic archetypes (7 shapes, open-loop)

| Controller | Replica-hours | Scale events | Energy proxy |
|---|---|---|---|
| HPA 0.70 | 234.7 | 28.9 | 11.31 |
| Omni observe | 234.7 | 28.9 | 11.31 |
| Omni target | 87.0 | 43.9 | 5.40 |
| PID | 172.2 | 195.1 | 8.81 |
| Deadband | 74.0 | 105.0 | 4.88 |

Omni observe = HPA. Omni target raises ρ* above 0.70, so HPA asks for fewer replicas. PID chatters. Deadband is cheapest on this open-loop cost metric.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
