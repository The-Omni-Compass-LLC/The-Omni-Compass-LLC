# The third amendment (a lower target never held): capacity, fairness and fault tests, 10 paired repetitions each

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Commit `583c97f` (rules 1 to 4), 2026-10-04, GitHub Actions workflow `benchmark-reps`, arms native / omni / compass, order
rotated, open-loop load. Transcribed from each run's `aggregate` job; each run's artifact `live-reps` holds every table,
the allocation law's in full. Design: `docs/K8S_COMPASS_PREREGISTRATION.md`, "The third amendment". Evidence class **L**.
The first runs to carry the real machine under kind: a GitHub runner of **4 cores, 48% to 70% busy** in every arm,
where "used / allocatable" reads 0.07 to 0.10 because each kind worker reports the same four cores as its own.

| Test | Run | Aggregate job | `live-reps` zip SHA-256 |
|---|---|---|---|
| capacity | 37182800270 | 111392550612 | `0bd093f835d0b3a7218109d2650f2624ccc89fb6e5f1edbf8008d2e202f0e02d` |
| fairness | 37182801578 | 111387185768 | `e97c32c069b7b8bcac2463cc03014a1a4c4e50e2f685076e0c7e4974835062e7` |
| faults | 37182803035 | 111386924282 | `89b6258c26fb11f69b5c054c2fce346e8c692b1a542eea71a275795abf005cf1` |

**Result. The compass law: no LOSS of more than 2% in any of the three tests.**

- **Capacity:** compass law 24.0 against native's 16.2 requests a second, **+48.1% (+5.7 to +9.9)**, no LOSS;
  allocation law 25.2, **+55.6% (+6.7 to +11.3)**, no LOSS.
- **Fairness:** compass law, no LOSS for either application; one row significant, energy per core-hour on the declared 25 W
  standby model **+1.5%**, inside the 2% the rule allows. The allocation law: php-apache's failures −38.5%, response
  times a third lower, and the neighbour no longer higher (+2.2%, not significant; under the previous setting +5.3%).
- **Faults:** compass law, no LOSS; recovery from a lost machine 54 s faster (−61%).

## Capacity

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.2 |  |  | 10 |
| omni | 25.2 | +55.6% | +6.7 to +11.3 | 10 |
| compass | 24.0 | +48.1% | +5.7 to +9.9 | 10 |

### Capacity, B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.92 | -1.3% | -0.1566 to -0.002866 | yes: GAIN |
| node-hours | 2.681 | 2.645 | -1.3% | -0.07159 to +0.0001452 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 306.6 | 305.8 | -0.3% | -1.187 to -0.5505 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.6 | 303.1 | -1.2% | -6.299 to -0.7716 | yes: GAIN |
| response time (ms), mean | 342.3 | 205.5 | -40.0% | -176 to -97.64 | yes: GAIN |
| response time (ms), 95th percentile | 932.6 | 463.8 | -50.3% | -610.8 to -326.8 | yes: GAIN |
| response time (ms), 99th percentile | 3516 | 2805 | -20.2% | -1608 to +184.2 | no |
| time over the response line (% of samples) | 20.11 | 10.66 | -47.0% | -12.14 to -6.759 | yes: GAIN |
| failed requests (%) | 7.518 | 6.545 | -12.9% | -1.345 to -0.601 | yes: GAIN |
| pending pods, pod-minutes | 0.4883 | 0.375 | -23.2% | -0.3437 to +0.1171 | no |
| utilisation (used / allocatable) | 0.1006 | 0.1 | -0.6% | -0.002071 to +0.0008871 | no |
| CPU used (cores), mean | 2.415 | 2.366 | -2.0% | -0.05826 to -0.04048 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01077 | +0.0108 (native is 0) | +0.009532 to +0.01201 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.415 | 2.376 | -1.6% | -0.04782 to -0.02939 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 294.4 | 298.3 | +1.3% | -0.9622 to +8.68 | no |
| HPA replicas, mean | 9.253 | 9.039 | -2.3% | -0.5624 to +0.1344 | no |
| pods started | 4.4 | 4.3 | -2.3% | -1.625 to +1.425 | no |
| pod start wait, total (s) | 15 | 10 | -33.3% | -11.89 to +1.894 | no |
| pod start wait, mean (s) | 2.924 | 2.043 | -30.1% | -1.708 to -0.05219 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 69.77 | 68.62 | -1.6% | -1.491 to -0.7976 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## Fairness, B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | no |
| node-hours | 1.513 | 1.511 | -0.1% | -0.004162 to +0.0001621 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.3 | -0.2% | -0.7523 to -0.1063 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.3 | -0.2% | -0.7523 to -0.1063 | yes: GAIN |
| response time (ms), mean | 493.4 | 433.7 | -12.1% | -112.5 to -6.818 | yes: GAIN |
| response time (ms), 95th percentile | 2105 | 2126 | +1.0% | -363.8 to +406.4 | no |
| response time (ms), 99th percentile | 5284 | 4742 | -10.3% | -1211 to +126.9 | no |
| time over the response line (% of samples) | 22.09 | 20.25 | -8.3% | -3.843 to +0.1811 | no |
| failed requests (%) | 3.524 | 3.275 | -7.0% | -1.527 to +1.03 | no |
| pending pods, pod-minutes | 1.622 | 1.23 | -24.2% | -1.194 to +0.4111 | no |
| utilisation (used / allocatable) | 0.09516 | 0.09397 | -1.3% | -0.001975 to -0.0004052 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.284 | 2.255 | -1.3% | -0.0474 to -0.009724 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01375 | +0.0138 (native is 0) | +0.01097 to +0.01653 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.284 | 2.269 | -0.6% | -0.03517 to +0.005543 | no |
| energy per core-hour (Wh, the 25 W standby model) | 309.8 | 314.3 | +1.5% | +0.726 to +8.324 | yes, up (shown, not judged) |
| HPA replicas, mean | 15.06 | 15.16 | +0.7% | -0.2173 to +0.4135 | no |
| pods started | 4.4 | 3.8 | -13.6% | -1.728 to +0.5285 | no |
| pod start wait, total (s) | 10.4 | 12.2 | +17.3% | -3.084 to +6.684 | no |
| pod start wait, mean (s) | 2.081 | 2.324 | +11.7% | -0.4434 to +0.9296 | no |
| host CPU busy, the real machine under kind (%) | 65.61 | 65.59 | -0.0% | -0.5804 to +0.5357 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 288.1 | 290.7 | +0.9% | -25.83 to +31.08 | no |
| second app: response time (ms), 99th percentile | 1880 | 2076 | +10.5% | -877.6 to +1271 | no |
| second app: time over the response line (% of samples) | 13.73 | 13.36 | -2.7% | -0.8355 to +0.09483 | no |
| second app: failed requests (%) | 11.81 | 11.79 | -0.2% | -0.4397 to +0.392 | no |

## Faults

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 89 | 15.6 |  |
| machine down | omni | 41 | 9.7 | -48 s (-54%) |
| machine down | compass | 35 | 8.0 | -54 s (-61%) |
| spike | native | 263 | 66.8 |  |
| spike | omni | 252 | 48.6 | -10 s (-4%) |
| spike | compass | 241 | 62.9 | -22 s (-8%) |
| runaway pod started | native | 121 | 11.2 |  |
| runaway pod started | omni | 83 | 5.7 | -38 s (-32%) |
| runaway pod started | compass | 96 | 8.6 | -25 s (-20%) |
| probe blind | native | 65 | 0.6 |  |
| probe blind | omni | 48 | 0.0 | -17 s (-26%) |
| probe blind | compass | 54 | 0.0 | -11 s (-17%) |

### Faults, B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.903 | -0.2% | -0.03447 to +0.009988 | no |
| node-hours | 1.494 | 1.49 | -0.2% | -0.01463 to +0.007184 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.9 | 165.5 | -0.2% | -1.067 to +0.3338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.3 | 163.7 | -0.4% | -1.372 to +0.1807 | no |
| response time (ms), mean | 230.3 | 117.5 | -49.0% | -152.5 to -73.13 | yes: GAIN |
| response time (ms), 95th percentile | 441.2 | 164.5 | -62.7% | -306.3 to -247.3 | yes: GAIN |
| response time (ms), 99th percentile | 1245 | 742.5 | -40.4% | -1123 to +118.5 | no |
| time over the response line (% of samples) | 8.494 | 5.382 | -36.6% | -3.814 to -2.409 | yes: GAIN |
| failed requests (%) | 5.006 | 4.335 | -13.4% | -1.152 to -0.1902 | yes: GAIN |
| pending pods, pod-minutes | 0.4917 | 0.305 | -38.0% | -0.4173 to +0.04394 | no |
| utilisation (used / allocatable) | 0.0714 | 0.07029 | -1.6% | -0.002941 to +0.0007209 | no |
| CPU used (cores), mean | 1.689 | 1.66 | -1.7% | -0.07021 to +0.01231 | no |
| Omni's own CPU (cores), mean | 0 | 0.00928 | +0.00928 (native is 0) | +0.008408 to +0.01015 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.689 | 1.67 | -1.2% | -0.06093 to +0.02159 | no |
| energy per core-hour (Wh, the 25 W standby model) | 398.9 | 403.9 | +1.3% | -5.579 to +15.65 | no |
| HPA replicas, mean | 8.728 | 8.752 | +0.3% | -0.2394 to +0.2879 | no |
| pods started | 4.8 | 4 | -16.7% | -1.742 to +0.1417 | no |
| pod start wait, total (s) | 14.7 | 11.4 | -22.4% | -7.389 to +0.789 | no |
| pod start wait, mean (s) | 2.702 | 2.344 | -13.3% | -0.9352 to +0.219 | no |
| host CPU busy, the real machine under kind (%) | 48.26 | 47.66 | -1.3% | -1.398 to +0.185 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

Energy on kind is a declared model, not a meter.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
