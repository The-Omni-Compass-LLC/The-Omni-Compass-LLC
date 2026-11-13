# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.913 | 5.915 |
| node-hours | 1.496 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 163.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 253.5 | 115.6 |
| response time (ms), 95th percentile | 384.2 | 133.2 |
| response time (ms), 99th percentile | 1569 | 856.1 |
| time over the response line (% of samples) | 8.287 | 5.3 |
| failed requests (%) | 5.192 | 4.376 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 5.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4933 | 0.59 |
| utilisation (used / allocatable) | 0.07233 | 0.07064 |
| CPU used (cores), mean | 1.711 | 1.671 |
| Omni's own CPU (cores), mean | 0 | 0.00978 |
| CPU used with Omni's own (cores), mean | 1.711 | 1.681 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 386.5 | 394 |
| HPA replicas, mean | 8.923 | 10.42 |
| pods started | 4.3 | 6.1 |
| pod start wait, total (s) | 13.9 | 19 |
| pod start wait, mean (s) | 2.758 | 2.983 |
| host CPU busy, the real machine under kind (%) | 48.91 | 48.26 |
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
| worker nodes in service, mean | 5.913 | 5.915 | +0.0% | -0.002491 to +0.006215 | no |
| node-hours | 1.496 | 1.492 | -0.2% | -0.0108 to +0.003522 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 166.3 | 165.5 | -0.5% | -1.638 to +0.07108 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.7 | 163.9 | -0.5% | -1.622 to +0.1348 | no |
| response time (ms), mean | 253.5 | 115.6 | -54.4% | -197.2 to -78.45 | yes: GAIN |
| response time (ms), 95th percentile | 384.2 | 133.2 | -65.3% | -293.8 to -208.2 | yes: GAIN |
| response time (ms), 99th percentile | 1569 | 856.1 | -45.4% | -1089 to -336.5 | yes: GAIN |
| time over the response line (% of samples) | 8.287 | 5.3 | -36.0% | -4.176 to -1.798 | yes: GAIN |
| failed requests (%) | 5.192 | 4.376 | -15.7% | -1.217 to -0.4152 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 5.6 | -23.3% | -2.379 to -1.021 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.8 | +28.8 (native is 0) | +24.52 to +33.08 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4933 | 0.59 | +19.6% | -0.2441 to +0.4374 | no |
| utilisation (used / allocatable) | 0.07233 | 0.07064 | -2.3% | -0.002822 to -0.0005574 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.711 | 1.671 | -2.3% | -0.06604 to -0.01278 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00978 | +0.00978 (native is 0) | +0.008817 to +0.01074 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.711 | 1.681 | -1.7% | -0.05598 to -0.003276 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 386.5 | 394 | +1.9% | +2.121 to +12.8 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.923 | 10.42 | +16.7% | +0.4279 to +2.56 | yes: power given |
| pods started | 4.3 | 6.1 | +41.9% | +0.05436 to +3.546 | yes: power given |
| pod start wait, total (s) | 13.9 | 19 | +36.7% | -2.375 to +12.58 | no |
| pod start wait, mean (s) | 2.758 | 2.983 | +8.2% | -0.9482 to +1.4 | no |
| host CPU busy, the real machine under kind (%) | 48.91 | 48.26 | -1.3% | -1.29 to -0.008582 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 79 | 15.5 |  |
| machine down | omni | 36 | 9.0 | -43 s (-54%) |
| spike | native | 270 | 66.8 |  |
| spike | omni | 264 | 56.0 | -6 s (-2%) |
| runaway pod started | native | 116 | 11.1 |  |
| runaway pod started | omni | 84 | 6.1 | -32 s (-28%) |
| probe blind | native | 70 | 1.1 |  |
| probe blind | omni | 60 | 0.0 | -10 s (-14%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*