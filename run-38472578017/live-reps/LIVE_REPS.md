# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 515 | 514.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515 | 514.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 285.1 | 178 |
| response time (ms), 95th percentile | 756.8 | 425.9 |
| response time (ms), 99th percentile | 2866 | 2187 |
| time over the response line (% of samples) | 18.08 | 13.28 |
| failed requests (%) | 10.06 | 9.808 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5883 | 0.67 |
| utilisation (used / allocatable) | 0.09919 | 0.09872 |
| CPU used (cores), mean | 2.381 | 2.369 |
| Omni's own CPU (cores), mean | 0 | 0.00944 |
| CPU used with Omni's own (cores), mean | 2.381 | 2.379 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313.3 | 317.6 |
| HPA replicas, mean | 9.61 | 12.56 |
| pods started | 4.4 | 8.8 |
| pod start wait, total (s) | 16 | 27.8 |
| pod start wait, mean (s) | 3.052 | 3.122 |
| host CPU busy, the real machine under kind (%) | 67.05 | 67.24 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.338e-16 to +4.785e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.512 | -0.0% | -0.006658 to +0.005658 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515 | 514.8 | -0.0% | -1.107 to +0.6849 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515 | 514.8 | -0.0% | -1.107 to +0.6849 | no |
| response time (ms), mean | 285.1 | 178 | -37.6% | -138.3 to -76.09 | yes: GAIN |
| response time (ms), 95th percentile | 756.8 | 425.9 | -43.7% | -419.7 to -242.2 | yes: GAIN |
| response time (ms), 99th percentile | 2866 | 2187 | -23.7% | -1492 to +135 | no |
| time over the response line (% of samples) | 18.08 | 13.28 | -26.6% | -6.426 to -3.19 | yes: GAIN |
| failed requests (%) | 10.06 | 9.808 | -2.5% | -0.8436 to +0.3343 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5883 | 0.67 | +13.9% | -0.3512 to +0.5146 | no |
| utilisation (used / allocatable) | 0.09919 | 0.09872 | -0.5% | -0.001902 to +0.0009667 | no |
| CPU used (cores), mean | 2.381 | 2.369 | -0.5% | -0.04564 to +0.0232 | no |
| Omni's own CPU (cores), mean | 0 | 0.00944 | +0.00944 (native is 0) | +0.007961 to +0.01092 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.381 | 2.379 | -0.1% | -0.03707 to +0.03351 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 313.3 | 317.6 | +1.4% | -0.977 to +9.6 | no |
| HPA replicas, mean | 9.61 | 12.56 | +30.7% | +1.311 to +4.585 | yes: power given |
| pods started | 4.4 | 8.8 | +100.0% | +2.289 to +6.511 | yes: power given |
| pod start wait, total (s) | 16 | 27.8 | +73.8% | +1.272 to +22.33 | yes: LOSS |
| pod start wait, mean (s) | 3.052 | 3.122 | +2.3% | -0.998 to +1.139 | no |
| host CPU busy, the real machine under kind (%) | 67.05 | 67.24 | +0.3% | -0.8544 to +1.245 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*