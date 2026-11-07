# Three columns: Kubernetes alone | Omni-Compass on top | Omni-Compass alone

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Fresh scenarios 713001-713030 (30 per workload, never used before). THEORETICAL SIMULATION (fleet/sim_slo.py).
Settings frozen before the run. Marks: **toward its aim** / *away from its aim* = paired 95% interval vs Kubernetes excludes 0 and the difference is over 0.5%; otherwise equal.

## web

| Gauge | Kubernetes alone | Omni on top | Omni alone |
|---|---:|---:|---:|
| Energy (kWh) | 14.24 | 14.26 (+0%, equal) | 11.24 (-21%, **higher**) |
| Machine-hours | 38.15 | 38.15 (+0%, equal) | 24.28 (-36%, **lower**) |
| Response time p95 (ms) | 124 | 124 (-0%, equal) | 147.4 (+19%, *higher*) |
| Response time p99 (ms) | 577.5 | 577.4 (-0%, equal) | 314.2 (-46%, equal) |
| Response time mean (ms) | 202.9 | 202.9 (-0%, equal) | 187.8 (-7%, **lower**) |
| Time over backlog limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Time over power limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Time over heat limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Machine starts+stops | 8.7 | 8.433 (-3%, **lower**) | 11.17 (+28%, *lower*) |
| Scale reversals | 1.3 | 1.167 (-10%, equal) | 1.433 (+10%, equal) |
| Pod changes | 633.5 | 633.5 (+0%, equal) | 596.7 (-6%, **lower**) |
| Work completed | 1 | 1 (+0%, equal) | 1 (+0%, equal) |
| Time healthy | 1 | 1 (+0%, equal) | 1 (+0%, equal) |
| Controllers fighting (per day) | 0.3333 | 0.4 (+20%, equal) | 0.1667 (-50%, equal) |

## multi

| Gauge | Kubernetes alone | Omni on top | Omni alone |
|---|---:|---:|---:|
| Energy (kWh) | 56.04 | 56.13 (+0%, equal) | 41.84 (-25%, **higher**) |
| Machine-hours | 150.2 | 150.2 (+0%, equal) | 87.83 (-42%, **lower**) |
| Response time p95 (ms) | 124.7 | 124.7 (-0%, equal) | 149.7 (+20%, *higher*) |
| Response time p99 (ms) | 516.2 | 516.2 (-0%, equal) | 394.7 (-24%, equal) |
| Response time mean (ms) | 231.1 | 231.1 (-0%, equal) | 198.3 (-14%, **lower**) |
| Time over backlog limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Time over power limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Time over heat limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Machine starts+stops | 37.47 | 36.67 (-2%, **lower**) | 48.7 (+30%, *lower*) |
| Scale reversals | 5.433 | 4.967 (-9%, **lower**) | 7.5 (+38%, *lower*) |
| Pod changes | 2625 | 2625 (+0%, equal) | 2452 (-7%, **lower**) |
| Work completed | 1 | 1 (+0%, equal) | 1 (+0%, equal) |
| Time healthy | 1 | 1 (+0%, equal) | 1 (+0%, equal) |
| Controllers fighting (per day) | 1.7 | 1.733 (+2%, equal) | 0.9333 (-45%, **higher**) |

## batch

| Gauge | Kubernetes alone | Omni on top | Omni alone |
|---|---:|---:|---:|
| Energy (kWh) | 64.94 | 65.12 (+0%, equal) | 61.26 (-6%, **higher**) |
| Machine-hours | 93.02 | 93.58 (+1%, equal) | 77.08 (-17%, **higher**) |
| Response time p95 (ms) | 100 | 100 (+0%, equal) | 100 (+0%, equal) |
| Response time p99 (ms) | 1386 | 101.6 (-93%, **lower**) | 612.7 (-56%, **lower**) |
| Response time mean (ms) | 136.5 | 101.9 (-25%, **lower**) | 130.1 (-5%, **lower**) |
| Time over backlog limit | 0 | 0 (+0%, equal) | 0.0001389 (+13888889%, equal) |
| Time over power limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Time over heat limit | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Machine starts+stops | 13.53 | 10.87 (-20%, **lower**) | 18.77 (+39%, *lower*) |
| Scale reversals | 1.167 | 0.1667 (-86%, **lower**) | 1.367 (+17%, equal) |
| Pod changes | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Work completed | 1 | 1 (+0%, equal) | 1 (+0%, equal) |
| Time healthy | 1 | 1 (+0%, equal) | 0.9998 (-0%, equal) |
| Controllers fighting (per day) | 0 | 0 (+0%, equal) | 0.06667 (+6666666667%, equal) |

## gpu

| Gauge | Kubernetes alone | Omni on top | Omni alone |
|---|---:|---:|---:|
| Energy (kWh) | 194.7 | 194.8 (+0%, equal) | 191.9 (-1%, **higher**) |
| Machine-hours | 59.88 | 59.51 (-1%, equal) | 53.85 (-10%, **lower**) |
| Response time p95 (ms) | 1.804e+06 | 1.803e+06 (-0%, equal) | 1.804e+06 (-0%, equal) |
| Response time p99 (ms) | 1.913e+06 | 1.912e+06 (-0%, equal) | 1.912e+06 (-0%, equal) |
| Response time mean (ms) | 6.927e+05 | 6.922e+05 (-0%, equal) | 6.924e+05 (-0%, equal) |
| Time over backlog limit | 0.328 | 0.3274 (-0%, equal) | 0.3297 (+1%, *lower*) |
| Time over power limit | 0.5456 | 0.5419 (-1%, equal) | 0.5392 (-1%, equal) |
| Time over heat limit | 0.4812 | 0.4808 (-0%, equal) | 0.467 (-3%, **lower**) |
| Machine starts+stops | 15.5 | 11.4 (-26%, **lower**) | 14.2 (-8%, equal) |
| Scale reversals | 2.3 | 0.7333 (-68%, **lower**) | 1.2 (-48%, **lower**) |
| Pod changes | 0 | 0 (+0%, equal) | 0 (+0%, equal) |
| Work completed | 0.9131 | 0.9131 (+0%, equal) | 0.9131 (+0%, equal) |
| Time healthy | 0.4176 | 0.4208 (+1%, equal) | 0.4272 (+2%, **higher**) |
| Controllers fighting (per day) | 0.1 | 0.06667 (-33%, equal) | 0.1 (+0%, equal) |

## Tally across all workloads and gauges

| | toward its aim | equal | away from its aim |
|---|---:|---:|---:|
| Omni on top | 9 | 47 | 0 |
| Omni alone | 18 | 31 | 7 |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
