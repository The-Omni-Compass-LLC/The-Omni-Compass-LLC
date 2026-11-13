# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.338 |
| energy, parked workers still on at idle power (Wh, declared model) | 477.5 | 476.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.5 | 476.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 236.1 | 119.5 |
| response time (ms), 95th percentile | 607.3 | 228.5 |
| response time (ms), 99th percentile | 1222 | 576 |
| time over the response line (% of samples) | 10.31 | 2.367 |
| failed requests (%) | 1.014 | 0.8966 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6567 | 1.098 |
| utilisation (used / allocatable) | 0.07294 | 0.06993 |
| CPU used (cores), mean | 1.751 | 1.678 |
| Omni's own CPU (cores), mean | 0 | 0.00878 |
| CPU used with Omni's own (cores), mean | 1.751 | 1.687 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.6 | 429.4 |
| HPA replicas, mean | 9.685 | 10.51 |
| pods started | 6.4 | 13.9 |
| pod start wait, total (s) | 19.2 | 38.3 |
| pod start wait, mean (s) | 2.674 | 2.795 |
| host CPU busy, the real machine under kind (%) | 50.71 | 49.3 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.614e-15 to +7.255e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.338 | +0.1% | -0.002424 to +0.01276 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 477.5 | 476.2 | -0.3% | -2.366 to -0.2924 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.5 | 476.2 | -0.3% | -2.366 to -0.2924 | yes: GAIN |
| response time (ms), mean | 236.1 | 119.5 | -49.4% | -160.8 to -72.42 | yes: GAIN |
| response time (ms), 95th percentile | 607.3 | 228.5 | -62.4% | -511.7 to -245.9 | yes: GAIN |
| response time (ms), 99th percentile | 1222 | 576 | -52.9% | -909.2 to -383.1 | yes: GAIN |
| time over the response line (% of samples) | 10.31 | 2.367 | -77.0% | -12.78 to -3.105 | yes: GAIN |
| failed requests (%) | 1.014 | 0.8966 | -11.6% | -0.2299 to -0.00566 | yes: GAIN |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.6567 | 1.098 | +67.3% | -0.16 to +1.043 | no |
| utilisation (used / allocatable) | 0.07294 | 0.06993 | -4.1% | -0.004259 to -0.001764 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.751 | 1.678 | -4.1% | -0.1022 to -0.04234 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00878 | +0.00878 (native is 0) | +0.007164 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.751 | 1.687 | -3.6% | -0.09225 to -0.03474 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 415.6 | 429.4 | +3.3% | +7.623 to +19.95 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.685 | 10.51 | +8.5% | -0.5831 to +2.239 | no |
| pods started | 6.4 | 13.9 | +117.2% | +3.408 to +11.59 | yes: power given |
| pod start wait, total (s) | 19.2 | 38.3 | +99.5% | +6.708 to +31.49 | yes: LOSS |
| pod start wait, mean (s) | 2.674 | 2.795 | +4.5% | -0.6429 to +0.8856 | no |
| host CPU busy, the real machine under kind (%) | 50.71 | 49.3 | -2.8% | -2.097 to -0.711 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*