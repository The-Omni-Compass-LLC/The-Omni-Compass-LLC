# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.516 | 4.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 522 | 522.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522 | 522.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 314.6 | 213 |
| response time (ms), 95th percentile | 844.6 | 518.2 |
| response time (ms), 99th percentile | 2957 | 3137 |
| time over the response line (% of samples) | 22.05 | 16.4 |
| failed requests (%) | 12.31 | 12.12 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.4417 |
| utilisation (used / allocatable) | 0.1087 | 0.1091 |
| CPU used (cores), mean | 2.61 | 2.618 |
| Omni's own CPU (cores), mean | 0 | 0.00989 |
| CPU used with Omni's own (cores), mean | 2.61 | 2.628 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 280.9 | 281 |
| HPA replicas, mean | 9.714 | 13.43 |
| pods started | 3.8 | 8.3 |
| pod start wait, total (s) | 12.9 | 22.9 |
| pod start wait, mean (s) | 2.586 | 2.779 |
| host CPU busy, the real machine under kind (%) | 73.22 | 74.06 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.063e-16 to +7.286e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.516 | 4.518 | +0.0% | -0.008717 to +0.01138 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522 | 522.4 | +0.1% | -0.7106 to +1.617 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522 | 522.4 | +0.1% | -0.7106 to +1.617 | no |
| response time (ms), mean | 314.6 | 213 | -32.3% | -136.1 to -67.2 | yes: GAIN |
| response time (ms), 95th percentile | 844.6 | 518.2 | -38.7% | -445.6 to -207.3 | yes: GAIN |
| response time (ms), 99th percentile | 2957 | 3137 | +6.1% | -900.7 to +1259 | no |
| time over the response line (% of samples) | 22.05 | 16.4 | -25.6% | -7.773 to -3.521 | yes: GAIN |
| failed requests (%) | 12.31 | 12.12 | -1.6% | -1.044 to +0.6607 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.35 | 0.4417 | +26.2% | -0.3412 to +0.5245 | no |
| utilisation (used / allocatable) | 0.1087 | 0.1091 | +0.3% | -0.001495 to +0.002188 | no |
| CPU used (cores), mean | 2.61 | 2.618 | +0.3% | -0.03588 to +0.0525 | no |
| Omni's own CPU (cores), mean | 0 | 0.00989 | +0.00989 (native is 0) | +0.008756 to +0.01102 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.61 | 2.628 | +0.7% | -0.02619 to +0.06259 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 280.9 | 281 | +0.0% | -3.461 to +3.72 | no |
| HPA replicas, mean | 9.714 | 13.43 | +38.3% | +2.355 to +5.079 | yes: power given |
| pods started | 3.8 | 8.3 | +118.4% | +2.772 to +6.228 | yes: power given |
| pod start wait, total (s) | 12.9 | 22.9 | +77.5% | +3.222 to +16.78 | yes: LOSS |
| pod start wait, mean (s) | 2.586 | 2.779 | +7.5% | -0.7832 to +1.17 | no |
| host CPU busy, the real machine under kind (%) | 73.22 | 74.06 | +1.2% | -0.3411 to +2.031 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*