# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.337 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 471.5 | 469.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 471.5 | 469.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 185.7 | 89.85 |
| response time (ms), 95th percentile | 469.2 | 157.8 |
| response time (ms), 99th percentile | 856.7 | 305.4 |
| time over the response line (% of samples) | 6.109 | 0.9332 |
| failed requests (%) | 0.4078 | 0.3519 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7667 | 0.76 |
| utilisation (used / allocatable) | 0.06302 | 0.06055 |
| CPU used (cores), mean | 1.513 | 1.453 |
| Omni's own CPU (cores), mean | 0 | 0.0077 |
| CPU used with Omni's own (cores), mean | 1.513 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.9 | 478.6 |
| HPA replicas, mean | 9.57 | 9.377 |
| pods started | 7 | 12.2 |
| pod start wait, total (s) | 25.1 | 32.3 |
| pod start wait, mean (s) | 3.18 | 2.648 |
| host CPU busy, the real machine under kind (%) | 44.09 | 42.82 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.102e-15 to +9.246e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.337 | 4.335 | -0.0% | -0.00702 to +0.00302 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 471.5 | 469.7 | -0.4% | -2.413 to -1.156 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 471.5 | 469.7 | -0.4% | -2.413 to -1.156 | yes: GAIN |
| response time (ms), mean | 185.7 | 89.85 | -51.6% | -139.8 to -51.93 | yes: GAIN |
| response time (ms), 95th percentile | 469.2 | 157.8 | -66.4% | -437.1 to -185.7 | yes: GAIN |
| response time (ms), 99th percentile | 856.7 | 305.4 | -64.4% | -758.4 to -344.4 | yes: GAIN |
| time over the response line (% of samples) | 6.109 | 0.9332 | -84.7% | -9.701 to -0.6513 | yes: GAIN |
| failed requests (%) | 0.4078 | 0.3519 | -13.7% | -0.1419 to +0.03007 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 3 | -74.8% | -14.22 to -3.585 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.5 | +41.5 (native is 0) | +27.02 to +55.98 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7667 | 0.76 | -0.9% | -0.3044 to +0.291 | no |
| utilisation (used / allocatable) | 0.06302 | 0.06055 | -3.9% | -0.003434 to -0.001511 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.513 | 1.453 | -3.9% | -0.08242 to -0.03627 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0077 | +0.0077 (native is 0) | +0.006292 to +0.009108 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.513 | 1.461 | -3.4% | -0.0739 to -0.02939 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.9 | 478.6 | +3.4% | +11.62 to +19.81 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.57 | 9.377 | -2.0% | -1.22 to +0.8339 | no |
| pods started | 7 | 12.2 | +74.3% | +1.448 to +8.952 | yes: power given |
| pod start wait, total (s) | 25.1 | 32.3 | +28.7% | -6.954 to +21.35 | no |
| pod start wait, mean (s) | 3.18 | 2.648 | -16.7% | -1.623 to +0.5582 | no |
| host CPU busy, the real machine under kind (%) | 44.09 | 42.82 | -2.9% | -1.894 to -0.644 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*