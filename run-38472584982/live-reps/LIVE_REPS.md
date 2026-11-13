# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.514 | 4.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 518.2 | 519.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518.2 | 519.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 287.9 | 189 |
| response time (ms), 95th percentile | 788.3 | 426.5 |
| response time (ms), 99th percentile | 2767 | 2476 |
| time over the response line (% of samples) | 21.33 | 16.18 |
| failed requests (%) | 12.45 | 12.95 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3433 | 0.9483 |
| utilisation (used / allocatable) | 0.1038 | 0.1052 |
| CPU used (cores), mean | 2.492 | 2.525 |
| Omni's own CPU (cores), mean | 0 | 0.0094 |
| CPU used with Omni's own (cores), mean | 2.492 | 2.534 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.6 | 301.9 |
| HPA replicas, mean | 9.496 | 12.44 |
| pods started | 4.4 | 7.8 |
| pod start wait, total (s) | 15.8 | 24.6 |
| pod start wait, mean (s) | 2.874 | 3.212 |
| host CPU busy, the real machine under kind (%) | 70.4 | 72.02 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.898e-15 to -5.633e-17 | EVEN, the same (under one part in a million) |
| node-hours | 4.514 | 4.511 | -0.1% | -0.01122 to +0.006556 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 518.2 | 519.1 | +0.2% | -0.8964 to +2.629 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 518.2 | 519.1 | +0.2% | -0.8964 to +2.629 | no |
| response time (ms), mean | 287.9 | 189 | -34.4% | -129.2 to -68.63 | yes: GAIN |
| response time (ms), 95th percentile | 788.3 | 426.5 | -45.9% | -466.8 to -256.8 | yes: GAIN |
| response time (ms), 99th percentile | 2767 | 2476 | -10.5% | -1013 to +431.5 | no |
| time over the response line (% of samples) | 21.33 | 16.18 | -24.2% | -6.912 to -3.401 | yes: GAIN |
| failed requests (%) | 12.45 | 12.95 | +4.1% | +0.2021 to +0.8138 | yes: LOSS |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3433 | 0.9483 | +176.2% | +0.1117 to +1.098 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1038 | 0.1052 | +1.3% | -0.0001272 to +0.002818 | no |
| CPU used (cores), mean | 2.492 | 2.525 | +1.3% | -0.003053 to +0.06763 | no |
| Omni's own CPU (cores), mean | 0 | 0.0094 | +0.0094 (native is 0) | +0.007678 to +0.01112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.492 | 2.534 | +1.7% | +0.004718 to +0.07866 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 301.6 | 301.9 | +0.1% | -4.976 to +5.577 | no |
| HPA replicas, mean | 9.496 | 12.44 | +31.0% | +1.051 to +4.839 | yes: power given |
| pods started | 4.4 | 7.8 | +77.3% | +1.641 to +5.159 | yes: power given |
| pod start wait, total (s) | 15.8 | 24.6 | +55.7% | +0.3646 to +17.24 | yes: LOSS |
| pod start wait, mean (s) | 2.874 | 3.212 | +11.8% | -0.5086 to +1.184 | no |
| host CPU busy, the real machine under kind (%) | 70.4 | 72.02 | +2.3% | +0.3556 to +2.887 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 19.8 |  |  | 10 |
| compass | 27.6 | +39.4% | +4.9 to +10.7 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*