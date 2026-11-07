# The second amendment (a raise waits for a steady demand): capacity, fairness and fault tests, 10 paired repetitions each

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Commit `5d2e238`, 2026-10-04, GitHub Actions workflow `benchmark-reps`, arms native / omni / compass, order rotated,
open-loop load. Transcribed from each run's `aggregate` job; each run's artifact `live-reps` holds the same tables.
Design: `docs/K8S_COMPASS_PREREGISTRATION.md`, "The pod record, and the second amendment". Evidence class **L**.

| Test | Run | Aggregate job | `live-reps` zip SHA-256 |
|---|---|---|---|
| capacity (`load_steps` 1 to 8, 1,600 s) | 37176746021 | 111374050394 | `dbe08676ebd0bc8837db684b4ac9db1c4a7c209b6bd87eed43ecd18caaed8d2b` |
| fairness (`two_app` 1, 900 s) | 37176747383 | 111369225045 | `ee9f8c8ba8e023b3190e6926cc46138fb6dff981d4338734fb566000b313f969` |
| faults (`faults` 1, 900 s) | 37176748773 | 111369149841 | `ce683bb91c659e450b937c0e27879a99bc2b230847d6bffb90641b8a14f10967` |

**Result.**

- **Capacity: no LOSS clear of the noise under either law.** The compass law served 24.6 requests a second within
  the line against native's 17.4, **+41.4% (+5.4 to +9.0)**; the allocation law **25.2, +44.8% (+4.9 to +10.7)** (it
  served +0.0% before the amendment). Pods started with the compass law 5.7 against 4.1, interval −0.64 to +3.84, no
  longer significant (before +34.2%, significant); with the allocation law 3.4, −17.1%.
- **Faults: no LOSS clear of the noise under either law.** Recovery faster from every fault in both arms.
- **Fairness: the compass law, no LOSS clear of the noise for either application.** The allocation law cut
  php-apache's response times by a third and its failures by 37%, and **the neighbour's failed requests rose from
  13.80% to 14.54% (+0.19 to +1.28 points), significant**: the allocation law conveys idle CPU to the service it
  senses, and on machines shared with a surging neighbour that CPU is the neighbour's headroom. The allocation law is
  not labelled GAIN in the fairness test; the compass law, the law carried forward, is clean in all three.

## Capacity

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 17.4 |  |  | 10 |
| omni | 25.2 | +44.8% | +4.9 to +10.7 | 10 |
| compass | 24.6 | +41.4% | +5.4 to +9.0 | 10 |

### Capacity, B: the allocation law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.351 | -10.8% | -1.476 to +0.178 | no |
| node-hours | 2.688 | 2.394 | -10.9% | -0.6632 to +0.0768 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.4 | -0.4% | -2.508 to +0.04299 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 283.7 | -7.5% | -50.84 to +4.951 | no |
| response time (ms), mean | 318.8 | 187.9 | -41.1% | -173.5 to -88.19 | yes: GAIN |
| response time (ms), 95th percentile | 868.8 | 417.4 | -52.0% | -602 to -300.9 | yes: GAIN |
| response time (ms), 99th percentile | 2524 | 2301 | -8.8% | -1266 to +820.6 | no |
| time over the response line (% of samples) | 19.2 | 9.727 | -49.3% | -12.63 to -6.32 | yes: GAIN |
| failed requests (%) | 7.518 | 6.337 | -15.7% | -1.801 to -0.5614 | yes: GAIN |
| pending pods, pod-minutes | 0.425 | 0.1583 | -62.7% | -0.5481 to +0.01473 | no |
| utilisation (used / allocatable) | 0.09895 | 0.1084 | +9.6% | -0.004866 to +0.02379 | no |
| CPU used (cores), mean | 2.375 | 2.315 | -2.5% | -0.09532 to -0.0247 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01447 | +0.0145 (native is 0) | +0.0124 to +0.01654 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.375 | 2.329 | -1.9% | -0.0821 to -0.008987 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 300.2 | 277.7 | -7.5% | -58.51 to +13.52 | no |
| HPA replicas, mean | 9.225 | 9.292 | +0.7% | -0.149 to +0.2828 | no |
| pods started | 4.1 | 3.4 | -17.1% | -1.964 to +0.5639 | no |
| pod start wait, total (s) | 12.6 | 5.2 | -58.7% | -13.4 to -1.404 | yes: GAIN |
| pod start wait, mean (s) | 2.583 | 1.346 | -47.9% | -2.043 to -0.4307 | yes: GAIN |

### Capacity, B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.765 | -3.9% | -0.4607 to -0.009241 | yes: GAIN |
| node-hours | 2.688 | 2.579 | -4.0% | -0.2103 to -0.005948 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.5 | -0.4% | -1.916 to -0.4485 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 297.6 | -3.0% | -16.93 to -1.18 | yes: GAIN |
| response time (ms), mean | 318.8 | 179.5 | -43.7% | -173.3 to -105.2 | yes: GAIN |
| response time (ms), 95th percentile | 868.8 | 381.9 | -56.0% | -600.3 to -373.5 | yes: GAIN |
| response time (ms), 99th percentile | 2524 | 1890 | -25.1% | -1306 to +38.73 | no |
| time over the response line (% of samples) | 19.2 | 9.944 | -48.2% | -12.05 to -6.462 | yes: GAIN |
| failed requests (%) | 7.518 | 6.573 | -12.6% | -1.43 to -0.4602 | yes: GAIN |
| pending pods, pod-minutes | 0.425 | 0.6567 | +54.5% | -0.03882 to +0.5022 | no |
| utilisation (used / allocatable) | 0.09895 | 0.09986 | +0.9% | -0.001281 to +0.003086 | no |
| CPU used (cores), mean | 2.375 | 2.32 | -2.3% | -0.0781 to -0.03187 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0103 | +0.0103 (native is 0) | +0.008778 to +0.01182 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.375 | 2.33 | -1.9% | -0.0687 to -0.02067 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 300.2 | 297.9 | -0.7% | -9.618 to +5.124 | no |
| HPA replicas, mean | 9.225 | 8.042 | -12.8% | -2.315 to -0.05011 | yes: GAIN |
| pods started | 4.1 | 5.7 | +39.0% | -0.6418 to +3.842 | no |
| pod start wait, total (s) | 12.6 | 13.6 | +7.9% | -5.53 to +7.53 | no |
| pod start wait, mean (s) | 2.583 | 2.421 | -6.3% | -0.7559 to +0.4328 | no |

## Fairness

### Fairness, B: the allocation law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.79 | -3.5% | -0.6373 to +0.2164 | no |
| node-hours | 1.509 | 1.46 | -3.2% | -0.1576 to +0.06042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.8 | +0.1% | -0.9528 to +1.428 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 168.8 | -2.2% | -12.28 to +4.787 | no |
| response time (ms), mean | 567.9 | 378.4 | -33.4% | -282.5 to -96.54 | yes: GAIN |
| response time (ms), 95th percentile | 2437 | 1522 | -37.5% | -1548 to -281.4 | yes: GAIN |
| response time (ms), 99th percentile | 5913 | 4358 | -26.3% | -2881 to -227 | yes: GAIN |
| time over the response line (% of samples) | 25.28 | 17.59 | -30.4% | -11.11 to -4.282 | yes: GAIN |
| failed requests (%) | 4.515 | 2.848 | -36.9% | -3.322 to -0.01217 | yes: GAIN |
| pending pods, pod-minutes | 1.345 | 1.892 | +40.6% | -0.3097 to +1.403 | no |
| utilisation (used / allocatable) | 0.1002 | 0.1021 | +1.9% | -0.003337 to +0.007241 | no |
| CPU used (cores), mean | 2.404 | 2.377 | -1.1% | -0.05809 to +0.004352 | no |
| Omni's own CPU (cores), mean | 0 | 0.02341 | +0.0234 (native is 0) | +0.02079 to +0.02603 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.404 | 2.4 | -0.1% | -0.03694 to +0.03002 | no |
| energy per core-hour (Wh, the 25 W standby model) | 295.2 | 289.9 | -1.8% | -19.86 to +9.341 | no |
| HPA replicas, mean | 15.31 | 15.5 | +1.2% | -0.119 to +0.4968 | no |
| pods started | 3.9 | 2.8 | -28.2% | -2.19 to -0.009955 | yes: GAIN |
| pod start wait, total (s) | 9.1 | 4.7 | -48.4% | -8.964 to +0.164 | no |
| pod start wait, mean (s) | 2.065 | 1.59 | -23.0% | -1.115 to +0.1648 | no |
| second app: response time (ms), 95th percentile | 280.2 | 263.1 | -6.1% | -54.25 to +20.16 | no |
| second app: response time (ms), 99th percentile | 889.6 | 903.4 | +1.6% | -848 to +875.6 | no |
| second app: time over the response line (% of samples) | 15.5 | 15.28 | -1.4% | -0.8296 to +0.38 | no |
| second app: failed requests (%) | 13.8 | 14.54 | +5.3% | +0.1896 to +1.277 | yes: LOSS |

### Fairness, B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | no |
| node-hours | 1.509 | 1.51 | +0.0% | -0.0007327 to +0.002066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.4 | -0.1% | -0.3724 to +0.07732 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 172.4 | -0.1% | -0.3724 to +0.07732 | no |
| response time (ms), mean | 567.9 | 525.7 | -7.4% | -98.82 to +14.36 | no |
| response time (ms), 95th percentile | 2437 | 2486 | +2.0% | -415 to +512.6 | no |
| response time (ms), 99th percentile | 5913 | 6105 | +3.3% | -633.9 to +1019 | no |
| time over the response line (% of samples) | 25.28 | 23.78 | -5.9% | -3.425 to +0.4179 | no |
| failed requests (%) | 4.515 | 3.789 | -16.1% | -2.177 to +0.7241 | no |
| pending pods, pod-minutes | 1.345 | 1.73 | +28.6% | -0.6722 to +1.442 | no |
| utilisation (used / allocatable) | 0.1002 | 0.09928 | -0.9% | -0.00147 to -0.0002803 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.404 | 2.383 | -0.9% | -0.03527 to -0.006728 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01449 | +0.0145 (native is 0) | +0.0118 to +0.01718 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.404 | 2.397 | -0.3% | -0.01975 to +0.006737 | no |
| energy per core-hour (Wh, the 25 W standby model) | 295.2 | 297.1 | +0.6% | -0.01853 to +3.837 | no |
| HPA replicas, mean | 15.31 | 15.27 | -0.3% | -0.4683 to +0.3897 | no |
| pods started | 3.9 | 3.3 | -15.4% | -1.677 to +0.4769 | no |
| pod start wait, total (s) | 9.1 | 11.1 | +22.0% | -2.781 to +6.781 | no |
| pod start wait, mean (s) | 2.065 | 2.5 | +21.1% | -0.4018 to +1.272 | no |
| second app: response time (ms), 95th percentile | 280.2 | 278.8 | -0.5% | -28.08 to +25.35 | no |
| second app: response time (ms), 99th percentile | 889.6 | 671.5 | -24.5% | -863.5 to +427.3 | no |
| second app: time over the response line (% of samples) | 15.5 | 15.23 | -1.8% | -0.6016 to +0.04964 | no |
| second app: failed requests (%) | 13.8 | 14.1 | +2.1% | -0.2618 to +0.8517 | no |

## Faults

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 52 | 13.5 |  |
| machine down | omni | 41 | 9.0 | -12 s (-22%) |
| machine down | compass | 41 | 9.5 | -11 s (-21%) |
| spike | native | 238 | 50.5 |  |
| spike | omni | 213 | 32.7 | -25 s (-11%) |
| spike | compass | 214 | 45.1 | -25 s (-10%) |
| runaway pod started | native | 76 | 7.7 |  |
| runaway pod started | omni | 56 | 3.7 | -19 s (-26%) |
| runaway pod started | compass | 69 | 5.7 | -7 s (-9%) |
| probe blind | native | 67 | 0.6 |  |
| probe blind | omni | 54 | 0.0 | -13 s (-19%) |
| probe blind | compass | 60 | 0.1 | -7 s (-10%) |

### Faults, B: the allocation law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.916 | 5.043 | -14.8% | -1.631 to -0.1145 | yes: GAIN |
| node-hours | 1.497 | 1.276 | -14.8% | -0.413 to -0.03062 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.6 | -0.4% | -1.158 to -0.1373 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 146.5 | -10.5% | -31.16 to -3.114 | yes: GAIN |
| response time (ms), mean | 202.4 | 115.4 | -43.0% | -121.3 to -52.55 | yes: GAIN |
| response time (ms), 95th percentile | 386 | 163.8 | -57.6% | -265.5 to -178.9 | yes: GAIN |
| response time (ms), 99th percentile | 1779 | 1048 | -41.1% | -2017 to +555.5 | no |
| time over the response line (% of samples) | 6.99 | 4.411 | -36.9% | -3.644 to -1.515 | yes: GAIN |
| failed requests (%) | 3.804 | 3.345 | -12.1% | -1.03 to +0.1125 | no |
| pending pods, pod-minutes | 0.4533 | 0.2767 | -39.0% | -0.4869 to +0.1336 | no |
| utilisation (used / allocatable) | 0.06636 | 0.07494 | +12.9% | -0.002285 to +0.01946 | no |
| CPU used (cores), mean | 1.57 | 1.511 | -3.8% | -0.09287 to -0.02494 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01644 | +0.0164 (native is 0) | +0.01383 to +0.01905 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.57 | 1.528 | -2.7% | -0.07482 to -0.01011 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 430.7 | 387.5 | -10.0% | -97.41 to +11.02 | no |
| HPA replicas, mean | 8.536 | 8.733 | +2.3% | -0.02034 to +0.4139 | no |
| pods started | 5 | 4.1 | -18.0% | -1.99 to +0.19 | no |
| pod start wait, total (s) | 17.2 | 8.5 | -50.6% | -13.42 to -3.979 | yes: GAIN |
| pod start wait, mean (s) | 3.153 | 1.907 | -39.5% | -2.06 to -0.4324 | yes: GAIN |

### Faults, B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.916 | 5.893 | -0.4% | -0.05766 to +0.01113 | no |
| node-hours | 1.497 | 1.491 | -0.4% | -0.01403 to +0.002254 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 165 | -0.1% | -0.8064 to +0.3162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 162.9 | -0.4% | -1.269 to -0.1042 | yes: GAIN |
| response time (ms), mean | 202.4 | 126.7 | -37.4% | -125.4 to -26.04 | yes: GAIN |
| response time (ms), 95th percentile | 386 | 161.5 | -58.2% | -290 to -159 | yes: GAIN |
| response time (ms), 99th percentile | 1779 | 1289 | -27.5% | -1932 to +952.7 | no |
| time over the response line (% of samples) | 6.99 | 4.967 | -28.9% | -3.17 to -0.8767 | yes: GAIN |
| failed requests (%) | 3.804 | 3.658 | -3.8% | -0.6664 to +0.3743 | no |
| pending pods, pod-minutes | 0.4533 | 0.32 | -29.4% | -0.2704 to +0.003753 | no |
| utilisation (used / allocatable) | 0.06636 | 0.06561 | -1.1% | -0.002902 to +0.001407 | no |
| CPU used (cores), mean | 1.57 | 1.546 | -1.5% | -0.06924 to +0.02092 | no |
| Omni's own CPU (cores), mean | 0 | 0.00887 | +0.00887 (native is 0) | +0.007297 to +0.01044 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.57 | 1.555 | -1.0% | -0.06014 to +0.02957 | no |
| energy per core-hour (Wh, the 25 W standby model) | 430.7 | 431.4 | +0.2% | -9.982 to +11.54 | no |
| HPA replicas, mean | 8.536 | 8.588 | +0.6% | -0.3526 to +0.4566 | no |
| pods started | 5 | 4 | -20.0% | -2.216 to +0.2158 | no |
| pod start wait, total (s) | 17.2 | 13.3 | -22.7% | -8.602 to +0.8021 | no |
| pod start wait, mean (s) | 3.153 | 2.538 | -19.5% | -1.537 to +0.3067 | no |

Energy on kind is a declared model, not a meter (see `CAPACITY.md`).

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
