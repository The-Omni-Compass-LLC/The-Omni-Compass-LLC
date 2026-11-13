# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.9 | 172.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.9 | 172.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 543.1 | 451.6 |
| response time (ms), 95th percentile | 2416 | 2092 |
| response time (ms), 99th percentile | 5317 | 5527 |
| time over the response line (% of samples) | 23.62 | 20.42 |
| failed requests (%) | 3.112 | 3.572 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.585 | 1.118 |
| utilisation (used / allocatable) | 0.09587 | 0.09478 |
| CPU used (cores), mean | 2.301 | 2.275 |
| Omni's own CPU (cores), mean | 0 | 0.01085 |
| CPU used with Omni's own (cores), mean | 2.301 | 2.286 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.6 | 312.3 |
| HPA replicas, mean | 14.91 | 15.23 |
| pods started | 5 | 3.8 |
| pod start wait, total (s) | 11.4 | 10.3 |
| pod start wait, mean (s) | 2.06 | 2.144 |
| host CPU busy, the real machine under kind (%) | 66.69 | 66.83 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 298.9 | 289.1 |
| second app: response time (ms), 99th percentile | 870.4 | 735.5 |
| second app: time over the response line (% of samples) | 14.01 | 14.31 |
| second app: failed requests (%) | 12.43 | 13.03 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.15e-18 to +8.933e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.512 | 1.516 | +0.3% | +0.001871 to +0.006796 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 171.9 | 172.1 | +0.1% | -0.2048 to +0.6788 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.9 | 172.1 | +0.1% | -0.2048 to +0.6788 | no |
| response time (ms), mean | 543.1 | 451.6 | -16.9% | -139.8 to -43.31 | yes: GAIN |
| response time (ms), 95th percentile | 2416 | 2092 | -13.4% | -648.2 to -0.1053 | yes: GAIN |
| response time (ms), 99th percentile | 5317 | 5527 | +4.0% | -471.7 to +891.8 | no |
| time over the response line (% of samples) | 23.62 | 20.42 | -13.5% | -5.359 to -1.037 | yes: GAIN |
| failed requests (%) | 3.112 | 3.572 | +14.8% | -0.4581 to +1.379 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.585 | 1.118 | -29.4% | -1.574 to +0.6405 | no |
| utilisation (used / allocatable) | 0.09587 | 0.09478 | -1.1% | -0.002579 to +0.0004048 | no |
| CPU used (cores), mean | 2.301 | 2.275 | -1.1% | -0.06189 to +0.009716 | no |
| Omni's own CPU (cores), mean | 0 | 0.01085 | +0.0109 (native is 0) | +0.009207 to +0.01249 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.301 | 2.286 | -0.7% | -0.05069 to +0.02022 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 309.6 | 312.3 | +0.9% | -5.355 to +10.83 | no |
| HPA replicas, mean | 14.91 | 15.23 | +2.1% | -0.08933 to +0.7237 | no |
| pods started | 5 | 3.8 | -24.0% | -2.142 to -0.2583 | yes: GAIN |
| pod start wait, total (s) | 11.4 | 10.3 | -9.6% | -5.826 to +3.626 | no |
| pod start wait, mean (s) | 2.06 | 2.144 | +4.1% | -0.5247 to +0.6918 | no |
| host CPU busy, the real machine under kind (%) | 66.69 | 66.83 | +0.2% | -0.351 to +0.6239 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 298.9 | 289.1 | -3.3% | -48.84 to +29.28 | no |
| second app: response time (ms), 99th percentile | 870.4 | 735.5 | -15.5% | -831.8 to +562 | no |
| second app: time over the response line (% of samples) | 14.01 | 14.31 | +2.1% | -0.349 to +0.934 | no |
| second app: failed requests (%) | 12.43 | 13.03 | +4.8% | +0.03888 to +1.155 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*