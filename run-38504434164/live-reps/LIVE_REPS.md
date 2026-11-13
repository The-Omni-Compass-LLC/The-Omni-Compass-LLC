# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.333 | 4.336 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.5 | 478.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.5 | 478.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 260.1 | 133.4 |
| response time (ms), 95th percentile | 670.4 | 255.1 |
| response time (ms), 99th percentile | 1306 | 710.2 |
| time over the response line (% of samples) | 11.76 | 2.768 |
| failed requests (%) | 1.204 | 1.003 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8783 | 0.84 |
| utilisation (used / allocatable) | 0.07751 | 0.07409 |
| CPU used (cores), mean | 1.86 | 1.778 |
| Omni's own CPU (cores), mean | 0 | 0.00905 |
| CPU used with Omni's own (cores), mean | 1.86 | 1.787 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 394.4 | 408.1 |
| HPA replicas, mean | 9.663 | 10.91 |
| pods started | 6.4 | 15.7 |
| pod start wait, total (s) | 24.6 | 37.8 |
| pod start wait, mean (s) | 3.793 | 2.488 |
| host CPU busy, the real machine under kind (%) | 53.45 | 51.82 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.84e-16 to +9.583e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.333 | 4.336 | +0.1% | -0.004018 to +0.01035 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.5 | 478.6 | -0.4% | -2.978 to -0.7442 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.5 | 478.6 | -0.4% | -2.978 to -0.7442 | yes: GAIN |
| response time (ms), mean | 260.1 | 133.4 | -48.7% | -166.9 to -86.63 | yes: GAIN |
| response time (ms), 95th percentile | 670.4 | 255.1 | -61.9% | -538.3 to -292.2 | yes: GAIN |
| response time (ms), 99th percentile | 1306 | 710.2 | -45.6% | -776.8 to -415.3 | yes: GAIN |
| time over the response line (% of samples) | 11.76 | 2.768 | -76.5% | -13.08 to -4.903 | yes: GAIN |
| failed requests (%) | 1.204 | 1.003 | -16.7% | -0.357 to -0.04489 | yes: GAIN |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.8783 | 0.84 | -4.4% | -0.7784 to +0.7017 | no |
| utilisation (used / allocatable) | 0.07751 | 0.07409 | -4.4% | -0.005122 to -0.001725 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.86 | 1.778 | -4.4% | -0.1229 to -0.04139 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00905 | +0.00905 (native is 0) | +0.007281 to +0.01082 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.86 | 1.787 | -3.9% | -0.1132 to -0.03305 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 394.4 | 408.1 | +3.5% | +7.976 to +19.56 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.663 | 10.91 | +12.9% | -0.2514 to +2.75 | no |
| pods started | 6.4 | 15.7 | +145.3% | +5.779 to +12.82 | yes: power given |
| pod start wait, total (s) | 24.6 | 37.8 | +53.7% | +4.053 to +22.35 | yes: LOSS |
| pod start wait, mean (s) | 3.793 | 2.488 | -34.4% | -2.044 to -0.5644 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 53.45 | 51.82 | -3.1% | -2.651 to -0.6124 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*