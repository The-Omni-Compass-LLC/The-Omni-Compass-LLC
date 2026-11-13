# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 522.1 | 521.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.1 | 521.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 316.6 | 174.4 |
| response time (ms), 95th percentile | 859.1 | 346.9 |
| response time (ms), 99th percentile | 3054 | 1983 |
| time over the response line (% of samples) | 20.81 | 12.29 |
| failed requests (%) | 10.53 | 9.565 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.2 | 25 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4067 | 0.4533 |
| utilisation (used / allocatable) | 0.1094 | 0.1082 |
| CPU used (cores), mean | 2.626 | 2.598 |
| Omni's own CPU (cores), mean | 0 | 0.00883 |
| CPU used with Omni's own (cores), mean | 2.626 | 2.607 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 266.6 | 268.9 |
| HPA replicas, mean | 9.62 | 10.05 |
| pods started | 4.5 | 7.4 |
| pod start wait, total (s) | 14 | 19.2 |
| pod start wait, mean (s) | 2.678 | 2.569 |
| host CPU busy, the real machine under kind (%) | 73.38 | 72.96 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.494e-16 to +6.718e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.515 | +0.0% | -0.003718 to +0.006385 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 522.1 | 521.5 | -0.1% | -1.455 to +0.3324 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 522.1 | 521.5 | -0.1% | -1.455 to +0.3324 | no |
| response time (ms), mean | 316.6 | 174.4 | -44.9% | -161.7 to -122.7 | yes: GAIN |
| response time (ms), 95th percentile | 859.1 | 346.9 | -59.6% | -566.9 to -457.5 | yes: GAIN |
| response time (ms), 99th percentile | 3054 | 1983 | -35.1% | -1688 to -453.1 | yes: GAIN |
| time over the response line (% of samples) | 20.81 | 12.29 | -41.0% | -9.76 to -7.287 | yes: GAIN |
| failed requests (%) | 10.53 | 9.565 | -9.2% | -1.781 to -0.1557 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 31.2 | 25 | -19.9% | -7.358 to -5.042 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.9 (native is 0) | +38.14 to +55.66 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4067 | 0.4533 | +11.5% | -0.2703 to +0.3637 | no |
| utilisation (used / allocatable) | 0.1094 | 0.1082 | -1.1% | -0.002251 to -0.0001307 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.626 | 2.598 | -1.1% | -0.05403 to -0.003137 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00883 | +0.00883 (native is 0) | +0.008094 to +0.009566 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.626 | 2.607 | -0.8% | -0.04484 to +0.005326 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 266.6 | 268.9 | +0.9% | +0.05139 to +4.506 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.62 | 10.05 | +4.5% | +0.1561 to +0.7093 | yes: power given |
| pods started | 4.5 | 7.4 | +64.4% | +0.5288 to +5.271 | yes: power given |
| pod start wait, total (s) | 14 | 19.2 | +37.1% | -2.466 to +12.87 | no |
| pod start wait, mean (s) | 2.678 | 2.569 | -4.1% | -0.8635 to +0.6457 | no |
| host CPU busy, the real machine under kind (%) | 73.38 | 72.96 | -0.6% | -1.088 to +0.2408 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 15.6 |  |  | 10 |
| compass | 25.8 | +65.4% | +7.3 to +13.1 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*