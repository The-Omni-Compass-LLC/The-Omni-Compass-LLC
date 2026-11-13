# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.512 | 4.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 520.7 | 522.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 520.7 | 522.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 287.9 | 198.3 |
| response time (ms), 95th percentile | 785.2 | 420.4 |
| response time (ms), 99th percentile | 2291 | 2681 |
| time over the response line (% of samples) | 21.53 | 16.22 |
| failed requests (%) | 12.17 | 12.72 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4583 | 0.515 |
| utilisation (used / allocatable) | 0.1079 | 0.1089 |
| CPU used (cores), mean | 2.589 | 2.614 |
| Omni's own CPU (cores), mean | 0 | 0.00961 |
| CPU used with Omni's own (cores), mean | 2.589 | 2.624 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279.8 | 280.2 |
| HPA replicas, mean | 9.561 | 13.2 |
| pods started | 4.5 | 9.6 |
| pod start wait, total (s) | 14.4 | 28.5 |
| pod start wait, mean (s) | 2.805 | 2.976 |
| host CPU busy, the real machine under kind (%) | 72.73 | 74.12 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.614e-15 to +7.255e-16 | EVEN, the same (under one part in a million) |
| node-hours | 4.512 | 4.517 | +0.1% | -0.00184 to +0.01217 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 520.7 | 522.2 | +0.3% | -0.07585 to +3.044 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 520.7 | 522.2 | +0.3% | -0.07585 to +3.044 | no |
| response time (ms), mean | 287.9 | 198.3 | -31.1% | -114.3 to -64.93 | yes: GAIN |
| response time (ms), 95th percentile | 785.2 | 420.4 | -46.5% | -459.3 to -270.4 | yes: GAIN |
| response time (ms), 99th percentile | 2291 | 2681 | +17.1% | -504.4 to +1286 | no |
| time over the response line (% of samples) | 21.53 | 16.22 | -24.7% | -6.85 to -3.782 | yes: GAIN |
| failed requests (%) | 12.17 | 12.72 | +4.6% | -0.1187 to +1.232 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4583 | 0.515 | +12.4% | -0.3371 to +0.4505 | no |
| utilisation (used / allocatable) | 0.1079 | 0.1089 | +1.0% | -0.0009112 to +0.003026 | no |
| CPU used (cores), mean | 2.589 | 2.614 | +1.0% | -0.02187 to +0.07262 | no |
| Omni's own CPU (cores), mean | 0 | 0.00961 | +0.00961 (native is 0) | +0.008222 to +0.011 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.589 | 2.624 | +1.4% | -0.01345 to +0.08342 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 279.8 | 280.2 | +0.1% | -5.001 to +5.82 | no |
| HPA replicas, mean | 9.561 | 13.2 | +38.0% | +2.372 to +4.899 | yes: power given |
| pods started | 4.5 | 9.6 | +113.3% | +3.538 to +6.662 | yes: power given |
| pod start wait, total (s) | 14.4 | 28.5 | +97.9% | +7.428 to +20.77 | yes: LOSS |
| pod start wait, mean (s) | 2.805 | 2.976 | +6.1% | -0.7362 to +1.077 | no |
| host CPU busy, the real machine under kind (%) | 72.73 | 74.12 | +1.9% | -0.1368 to +2.925 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 17.4 |  |  | 10 |
| compass | 25.2 | +44.8% | +5.7 to +9.9 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*