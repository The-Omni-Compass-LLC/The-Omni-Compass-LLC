# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.196 |
| node-hours | 2.516 | 2.178 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 248.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 530.5 | 465.6 |
| response time (ms), 95th percentile | 3217 | 3116 |
| response time (ms), 99th percentile | 4756 | 4826 |
| time over the response line (% of samples) | 15.88 | 15.11 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.5 | 190.2 |
| utilisation (used / allocatable) | 0.0633 | 0.07227 |
| CPU used (cores), mean | 1.519 | 1.499 |
| Omni's own CPU (cores), mean | 0 | 0.02328 |
| CPU used with Omni's own (cores), mean | 1.519 | 1.522 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.9 | 397 |
| HPA replicas, mean | 2.029 | 1.978 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.3 |
| pod start wait, mean (s) | 0 | 0.3 |
| host CPU busy, the real machine under kind (%) | 43.07 | 43.62 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 585.9 | 587.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.721 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.196 | -13.4% | -1.228 to -0.3806 | yes: GAIN |
| node-hours | 2.516 | 2.178 | -13.4% | -0.5129 to -0.1618 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.6 | -0.0% | -1.173 to +0.9167 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 248.3 | -9.3% | -38.33 to -12.53 | yes: GAIN |
| response time (ms), mean | 530.5 | 465.6 | -12.2% | -88.3 to -41.47 | yes: GAIN |
| response time (ms), 95th percentile | 3217 | 3116 | -3.1% | -269.4 to +67.53 | no |
| response time (ms), 99th percentile | 4756 | 4826 | +1.5% | -140.9 to +281.8 | no |
| time over the response line (% of samples) | 15.88 | 15.11 | -4.9% | -1.206 to -0.3436 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.5 | 190.2 | +0.3% | -3.125 to +4.411 | no |
| utilisation (used / allocatable) | 0.0633 | 0.07227 | +14.2% | +0.003409 to +0.01453 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.519 | 1.499 | -1.3% | -0.05092 to +0.01082 | no |
| Omni's own CPU (cores), mean | 0 | 0.02328 | +0.0233 (native is 0) | +0.01927 to +0.02729 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.519 | 1.522 | +0.2% | -0.02822 to +0.03468 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 434.9 | 397 | -8.7% | -66.84 to -8.923 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.029 | 1.978 | -2.5% | -0.2955 to +0.1925 | no |
| pods started | 0 | 0.1 | +0.1 (native is 0) | -0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.3 (native is 0) | -0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 43.07 | 43.62 | +1.3% | -0.1995 to +1.298 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 585.9 | 587.4 | +0.3% | -6.706 to +9.706 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.721 | -21.3% | -1.882 to -0.6763 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*