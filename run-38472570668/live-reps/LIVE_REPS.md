# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 521.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 521.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 288.6 | 198.6 |
| response time (ms), 95th percentile | 781.2 | 491 |
| response time (ms), 99th percentile | 2334 | 3068 |
| time over the response line (% of samples) | 21.28 | 16.01 |
| failed requests (%) | 12.11 | 12.11 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.56 | 0.43 |
| utilisation (used / allocatable) | 0.1081 | 0.1089 |
| CPU used (cores), mean | 2.595 | 2.613 |
| Omni's own CPU (cores), mean | 0 | 0.00973 |
| CPU used with Omni's own (cores), mean | 2.595 | 2.623 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 281.5 | 280.9 |
| HPA replicas, mean | 9.678 | 13.6 |
| pods started | 4.6 | 8.9 |
| pod start wait, total (s) | 14.6 | 25.5 |
| pod start wait, mean (s) | 2.894 | 2.862 |
| host CPU busy, the real machine under kind (%) | 72.51 | 73.72 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.13e-15 to +2.421e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.513 | 4.512 | -0.0% | -0.008749 to +0.006416 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 521.6 | +0.1% | -0.8894 to +1.771 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 521.6 | +0.1% | -0.8894 to +1.771 | no |
| response time (ms), mean | 288.6 | 198.6 | -31.2% | -108.2 to -71.78 | yes: GAIN |
| response time (ms), 95th percentile | 781.2 | 491 | -37.1% | -403.9 to -176.3 | yes: GAIN |
| response time (ms), 99th percentile | 2334 | 3068 | +31.4% | +55.41 to +1412 | yes: LOSS |
| time over the response line (% of samples) | 21.28 | 16.01 | -24.7% | -6.738 to -3.793 | yes: GAIN |
| failed requests (%) | 12.11 | 12.11 | +0.0% | -0.3697 to +0.3711 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.56 | 0.43 | -23.2% | -0.5478 to +0.2878 | no |
| utilisation (used / allocatable) | 0.1081 | 0.1089 | +0.7% | -0.0004384 to +0.001962 | no |
| CPU used (cores), mean | 2.595 | 2.613 | +0.7% | -0.01052 to +0.04708 | no |
| Omni's own CPU (cores), mean | 0 | 0.00973 | +0.00973 (native is 0) | +0.008372 to +0.01109 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.595 | 2.623 | +1.1% | -0.001733 to +0.05775 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 281.5 | 280.9 | -0.2% | -3.323 to +2.306 | no |
| HPA replicas, mean | 9.678 | 13.6 | +40.5% | +2.8 to +5.047 | yes: power given |
| pods started | 4.6 | 8.9 | +93.5% | +2.753 to +5.847 | yes: power given |
| pod start wait, total (s) | 14.6 | 25.5 | +74.7% | +4.724 to +17.08 | yes: LOSS |
| pod start wait, mean (s) | 2.894 | 2.862 | -1.1% | -0.6571 to +0.5929 | no |
| host CPU busy, the real machine under kind (%) | 72.51 | 73.72 | +1.7% | +0.4462 to +1.974 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*