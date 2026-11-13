# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.515 | 4.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 517.9 | 518.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.9 | 518.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 279.8 | 194.4 |
| response time (ms), 95th percentile | 769.6 | 430.7 |
| response time (ms), 99th percentile | 2375 | 3123 |
| time over the response line (% of samples) | 19.38 | 14.05 |
| failed requests (%) | 10.63 | 10.71 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.7467 |
| utilisation (used / allocatable) | 0.103 | 0.103 |
| CPU used (cores), mean | 2.471 | 2.473 |
| Omni's own CPU (cores), mean | 0 | 0.00879 |
| CPU used with Omni's own (cores), mean | 2.471 | 2.481 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 297.6 | 301.8 |
| HPA replicas, mean | 9.528 | 12.72 |
| pods started | 4.5 | 8.9 |
| pod start wait, total (s) | 16.1 | 26.8 |
| pod start wait, mean (s) | 3.077 | 3.017 |
| host CPU busy, the real machine under kind (%) | 69.13 | 69.87 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.738e-15 to -2.164e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.515 | 4.517 | +0.1% | -0.007174 to +0.01184 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 517.9 | 518.3 | +0.1% | -1.376 to +2.214 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 517.9 | 518.3 | +0.1% | -1.376 to +2.214 | no |
| response time (ms), mean | 279.8 | 194.4 | -30.5% | -105.6 to -65.28 | yes: GAIN |
| response time (ms), 95th percentile | 769.6 | 430.7 | -44.0% | -406.3 to -271.4 | yes: GAIN |
| response time (ms), 99th percentile | 2375 | 3123 | +31.5% | -194.9 to +1692 | no |
| time over the response line (% of samples) | 19.38 | 14.05 | -27.5% | -7.018 to -3.644 | yes: GAIN |
| failed requests (%) | 10.63 | 10.71 | +0.7% | -0.4547 to +0.6131 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.505 | 0.7467 | +47.9% | -0.2456 to +0.7289 | no |
| utilisation (used / allocatable) | 0.103 | 0.103 | +0.1% | -0.00219 to +0.002304 | no |
| CPU used (cores), mean | 2.471 | 2.473 | +0.1% | -0.05255 to +0.0553 | no |
| Omni's own CPU (cores), mean | 0 | 0.00879 | +0.00879 (native is 0) | +0.00725 to +0.01033 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.471 | 2.481 | +0.4% | -0.04512 to +0.06545 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 297.6 | 301.8 | +1.4% | -5.966 to +14.26 | no |
| HPA replicas, mean | 9.528 | 12.72 | +33.5% | +1.706 to +4.684 | yes: power given |
| pods started | 4.5 | 8.9 | +97.8% | +2.578 to +6.222 | yes: power given |
| pod start wait, total (s) | 16.1 | 26.8 | +66.5% | +1.192 to +20.21 | yes: LOSS |
| pod start wait, mean (s) | 3.077 | 3.017 | -2.0% | -0.9167 to +0.796 | no |
| host CPU busy, the real machine under kind (%) | 69.13 | 69.87 | +1.1% | -0.8313 to +2.298 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.2 |  |  | 10 |
| compass | 27.6 | +43.8% | +6.2 to +10.6 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*