# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.518 | 4.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 521.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 521.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 286.6 | 204 |
| response time (ms), 95th percentile | 762.5 | 420.6 |
| response time (ms), 99th percentile | 2164 | 3257 |
| time over the response line (% of samples) | 22.49 | 16.93 |
| failed requests (%) | 13.25 | 13.8 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4083 | 0.9167 |
| utilisation (used / allocatable) | 0.1074 | 0.1091 |
| CPU used (cores), mean | 2.577 | 2.618 |
| Omni's own CPU (cores), mean | 0 | 0.00962 |
| CPU used with Omni's own (cores), mean | 2.577 | 2.628 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 289 | 286.6 |
| HPA replicas, mean | 9.513 | 13.07 |
| pods started | 4.6 | 9.3 |
| pod start wait, total (s) | 17.6 | 28.1 |
| pod start wait, mean (s) | 3.161 | 3.008 |
| host CPU busy, the real machine under kind (%) | 72.48 | 74.35 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.449e-15 to -3.801e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.518 | 4.511 | -0.2% | -0.01354 to -0.0001257 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 521.2 | 521.7 | +0.1% | -0.7211 to +1.771 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 521.2 | 521.7 | +0.1% | -0.7211 to +1.771 | no |
| response time (ms), mean | 286.6 | 204 | -28.8% | -121.3 to -43.76 | yes: GAIN |
| response time (ms), 95th percentile | 762.5 | 420.6 | -44.8% | -458.7 to -225.2 | yes: GAIN |
| response time (ms), 99th percentile | 2164 | 3257 | +50.5% | -196.9 to +2383 | no |
| time over the response line (% of samples) | 22.49 | 16.93 | -24.7% | -7.472 to -3.66 | yes: GAIN |
| failed requests (%) | 13.25 | 13.8 | +4.2% | -0.03549 to +1.141 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.4083 | 0.9167 | +124.5% | +0.04979 to +0.9669 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1074 | 0.1091 | +1.6% | +0.0002966 to +0.003144 | yes, up (shown, not judged) |
| CPU used (cores), mean | 2.577 | 2.618 | +1.6% | +0.007118 to +0.07545 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00962 | +0.00962 (native is 0) | +0.008066 to +0.01117 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.577 | 2.628 | +2.0% | +0.01557 to +0.08624 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 289 | 286.6 | -0.8% | -8.809 to +4.016 | no |
| HPA replicas, mean | 9.513 | 13.07 | +37.4% | +2.235 to +4.879 | yes: power given |
| pods started | 4.6 | 9.3 | +102.2% | +2.979 to +6.421 | yes: power given |
| pod start wait, total (s) | 17.6 | 28.1 | +59.7% | +0.5927 to +20.41 | yes: LOSS |
| pod start wait, mean (s) | 3.161 | 3.008 | -4.8% | -1.39 to +1.084 | no |
| host CPU busy, the real machine under kind (%) | 72.48 | 74.35 | +2.6% | +0.8348 to +2.909 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 18.0 |  |  | 10 |
| compass | 24.6 | +36.7% | +4.2 to +9.0 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*