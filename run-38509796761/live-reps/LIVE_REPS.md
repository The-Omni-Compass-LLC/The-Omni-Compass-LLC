# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.8 | 175 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.8 | 175 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 650 | 548.8 |
| response time (ms), 95th percentile | 2754 | 2634 |
| response time (ms), 99th percentile | 6850 | 6507 |
| time over the response line (% of samples) | 30.02 | 26.53 |
| failed requests (%) | 5.621 | 4.981 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.195 | 1.555 |
| utilisation (used / allocatable) | 0.1073 | 0.1065 |
| CPU used (cores), mean | 2.574 | 2.556 |
| Omni's own CPU (cores), mean | 0 | 0.01207 |
| CPU used with Omni's own (cores), mean | 2.574 | 2.568 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 269.2 | 271 |
| HPA replicas, mean | 15.48 | 15.81 |
| pods started | 4.1 | 2.5 |
| pod start wait, total (s) | 5.8 | 4 |
| pod start wait, mean (s) | 1.43 | 1.508 |
| host CPU busy, the real machine under kind (%) | 75.29 | 75.06 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 247 | 249.6 |
| second app: response time (ms), 99th percentile | 754.6 | 884.8 |
| second app: time over the response line (% of samples) | 17.39 | 17.2 |
| second app: failed requests (%) | 16.57 | 16.39 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.516 | 1.518 | +0.2% | -0.0004879 to +0.005155 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.8 | 175 | +0.1% | -0.275 to +0.5059 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.8 | 175 | +0.1% | -0.275 to +0.5059 | no |
| response time (ms), mean | 650 | 548.8 | -15.6% | -157.9 to -44.31 | yes: GAIN |
| response time (ms), 95th percentile | 2754 | 2634 | -4.4% | -559.1 to +319.3 | no |
| response time (ms), 99th percentile | 6850 | 6507 | -5.0% | -1313 to +627.2 | no |
| time over the response line (% of samples) | 30.02 | 26.53 | -11.6% | -5.516 to -1.462 | yes: GAIN |
| failed requests (%) | 5.621 | 4.981 | -11.4% | -1.868 to +0.5876 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.195 | 1.555 | +30.1% | -0.8245 to +1.545 | no |
| utilisation (used / allocatable) | 0.1073 | 0.1065 | -0.7% | -0.001491 to -5.665e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.574 | 2.556 | -0.7% | -0.03578 to -0.00136 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01207 | +0.0121 (native is 0) | +0.01146 to +0.01268 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.574 | 2.568 | -0.3% | -0.02392 to +0.01092 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 269.2 | 271 | +0.7% | +0.0763 to +3.503 | yes, up (shown, not judged) |
| HPA replicas, mean | 15.48 | 15.81 | +2.1% | +0.06768 to +0.5809 | yes: power given |
| pods started | 4.1 | 2.5 | -39.0% | -2.998 to -0.2015 | yes: GAIN |
| pod start wait, total (s) | 5.8 | 4 | -31.0% | -4.831 to +1.231 | no |
| pod start wait, mean (s) | 1.43 | 1.508 | +5.5% | -0.3751 to +0.5318 | no |
| host CPU busy, the real machine under kind (%) | 75.29 | 75.06 | -0.3% | -0.5273 to +0.06534 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 247 | 249.6 | +1.1% | -13.97 to +19.27 | no |
| second app: response time (ms), 99th percentile | 754.6 | 884.8 | +17.3% | -874.4 to +1135 | no |
| second app: time over the response line (% of samples) | 17.39 | 17.2 | -1.1% | -0.6708 to +0.2919 | no |
| second app: failed requests (%) | 16.57 | 16.39 | -1.1% | -0.7321 to +0.3609 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*