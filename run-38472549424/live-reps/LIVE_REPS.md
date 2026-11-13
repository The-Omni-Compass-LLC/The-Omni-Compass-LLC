# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.518 | 1.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 150.4 | 77.47 |
| response time (ms), 95th percentile | 340.4 | 118.5 |
| response time (ms), 99th percentile | 546.1 | 162.3 |
| time over the response line (% of samples) | 2.174 | 0.02424 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3917 | 0.2617 |
| utilisation (used / allocatable) | 0.03755 | 0.03591 |
| CPU used (cores), mean | 0.9013 | 0.8618 |
| Omni's own CPU (cores), mean | 0 | 0.00836 |
| CPU used with Omni's own (cores), mean | 0.9013 | 0.8702 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.9 | 767.9 |
| HPA replicas, mean | 8.522 | 8.087 |
| pods started | 4.4 | 3.9 |
| pod start wait, total (s) | 14.9 | 13.6 |
| pod start wait, mean (s) | 3.017 | 2.883 |
| host CPU busy, the real machine under kind (%) | 27.39 | 26.63 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.895e-16 to +2.566e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.518 | 1.518 | -0.0% | -0.008435 to +0.008102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 158.9 | -0.2% | -1.214 to +0.4563 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 158.9 | -0.2% | -1.214 to +0.4563 | no |
| response time (ms), mean | 150.4 | 77.47 | -48.5% | -99.66 to -46.28 | yes: GAIN |
| response time (ms), 95th percentile | 340.4 | 118.5 | -65.2% | -295.7 to -148 | yes: GAIN |
| response time (ms), 99th percentile | 546.1 | 162.3 | -70.3% | -514.6 to -253.1 | yes: GAIN |
| time over the response line (% of samples) | 2.174 | 0.02424 | -98.9% | -3.526 to -0.7736 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3917 | 0.2617 | -33.2% | -0.299 to +0.03896 | no |
| utilisation (used / allocatable) | 0.03755 | 0.03591 | -4.4% | -0.003037 to -0.0002526 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9013 | 0.8618 | -4.4% | -0.07288 to -0.006062 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00836 | +0.00836 (native is 0) | +0.007205 to +0.009515 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9013 | 0.8702 | -3.5% | -0.06377 to +0.001545 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.9 | 767.9 | +2.5% | -2.99 to +41.14 | no |
| HPA replicas, mean | 8.522 | 8.087 | -5.1% | -0.7361 to -0.1331 | yes: GAIN |
| pods started | 4.4 | 3.9 | -11.4% | -1.631 to +0.631 | no |
| pod start wait, total (s) | 14.9 | 13.6 | -8.7% | -6.759 to +4.159 | no |
| pod start wait, mean (s) | 3.017 | 2.883 | -4.4% | -0.9061 to +0.6395 | no |
| host CPU busy, the real machine under kind (%) | 27.39 | 26.63 | -2.8% | -1.63 to +0.1132 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*