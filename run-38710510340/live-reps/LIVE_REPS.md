# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.511 | 4.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 515.9 | 514.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.9 | 514.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 273.1 | 163.5 |
| response time (ms), 95th percentile | 739.6 | 329.1 |
| response time (ms), 99th percentile | 2773 | 2206 |
| time over the response line (% of samples) | 18.98 | 12.08 |
| failed requests (%) | 10.67 | 9.575 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.4 | 20.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 10 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4367 | 0.6683 |
| utilisation (used / allocatable) | 0.1008 | 0.09884 |
| CPU used (cores), mean | 2.419 | 2.372 |
| Omni's own CPU (cores), mean | 0 | 0.00849 |
| CPU used with Omni's own (cores), mean | 2.419 | 2.381 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 306.9 | 314.6 |
| HPA replicas, mean | 9.492 | 9.647 |
| pods started | 4.5 | 5.5 |
| pod start wait, total (s) | 16 | 17.2 |
| pod start wait, mean (s) | 3.007 | 2.836 |
| host CPU busy, the real machine under kind (%) | 68.1 | 67.13 |
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
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.432e-15 to +1.073e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.511 | 4.509 | -0.0% | -0.005803 to +0.001803 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 515.9 | 514.4 | -0.3% | -2.647 to -0.2248 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 515.9 | 514.4 | -0.3% | -2.647 to -0.2248 | yes: GAIN |
| response time (ms), mean | 273.1 | 163.5 | -40.1% | -150.6 to -68.61 | yes: GAIN |
| response time (ms), 95th percentile | 739.6 | 329.1 | -55.5% | -514.6 to -306.4 | yes: GAIN |
| response time (ms), 99th percentile | 2773 | 2206 | -20.4% | -2020 to +885.9 | no |
| time over the response line (% of samples) | 18.98 | 12.08 | -36.3% | -9.983 to -3.816 | yes: GAIN |
| failed requests (%) | 10.67 | 9.575 | -10.3% | -2.091 to -0.1051 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.4 | 20.6 | -22.0% | -7.731 to -3.869 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30 | +30 (native is 0) | +24.15 to +35.85 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4367 | 0.6683 | +53.1% | -0.0363 to +0.4996 | no |
| utilisation (used / allocatable) | 0.1008 | 0.09884 | -2.0% | -0.003159 to -0.0007757 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.419 | 2.372 | -2.0% | -0.07582 to -0.01862 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00849 | +0.00849 (native is 0) | +0.007079 to +0.009901 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.419 | 2.381 | -1.6% | -0.068 to -0.009461 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 306.9 | 314.6 | +2.5% | +2.121 to +13.34 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.492 | 9.647 | +1.6% | -0.9559 to +1.265 | no |
| pods started | 4.5 | 5.5 | +22.2% | -1.237 to +3.237 | no |
| pod start wait, total (s) | 16 | 17.2 | +7.5% | -6.968 to +9.368 | no |
| pod start wait, mean (s) | 3.007 | 2.836 | -5.7% | -0.8878 to +0.5445 | no |
| host CPU busy, the real machine under kind (%) | 68.1 | 67.13 | -1.4% | -1.797 to -0.1589 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 22.2 |  |  | 10 |
| compass | 30.6 | +37.8% | +5.4 to +11.4 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*