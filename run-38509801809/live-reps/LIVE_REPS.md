# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.917 | 5.917 |
| node-hours | 1.493 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 163.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.5 | 162 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 203.4 | 126.3 |
| response time (ms), 95th percentile | 386 | 192.2 |
| response time (ms), 99th percentile | 1414 | 938.5 |
| time over the response line (% of samples) | 6.845 | 5.106 |
| failed requests (%) | 3.727 | 3.281 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.57 | 0.9267 |
| utilisation (used / allocatable) | 0.06375 | 0.06309 |
| CPU used (cores), mean | 1.509 | 1.493 |
| Omni's own CPU (cores), mean | 0 | 0.00999 |
| CPU used with Omni's own (cores), mean | 1.509 | 1.503 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 447.3 |
| HPA replicas, mean | 8.475 | 11.48 |
| pods started | 4.6 | 10.9 |
| pod start wait, total (s) | 21.7 | 47.1 |
| pod start wait, mean (s) | 3.808 | 4.109 |
| host CPU busy, the real machine under kind (%) | 43.28 | 43.11 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.917 | 5.917 | -0.0% | -0.006444 to +0.005589 | no |
| node-hours | 1.493 | 1.489 | -0.2% | -0.01185 to +0.004401 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 164 | 163.5 | -0.3% | -1.533 to +0.579 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 162.5 | 162 | -0.3% | -1.514 to +0.5516 | no |
| response time (ms), mean | 203.4 | 126.3 | -37.9% | -155.7 to +1.633 | no |
| response time (ms), 95th percentile | 386 | 192.2 | -50.2% | -291.3 to -96.29 | yes: GAIN |
| response time (ms), 99th percentile | 1414 | 938.5 | -33.6% | -1186 to +235.5 | no |
| time over the response line (% of samples) | 6.845 | 5.106 | -25.4% | -3.339 to -0.1402 | yes: GAIN |
| failed requests (%) | 3.727 | 3.281 | -12.0% | -0.9065 to +0.01329 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.57 | 0.9267 | +62.6% | -0.1914 to +0.9047 | no |
| utilisation (used / allocatable) | 0.06375 | 0.06309 | -1.0% | -0.003291 to +0.001985 | no |
| CPU used (cores), mean | 1.509 | 1.493 | -1.0% | -0.07705 to +0.04644 | no |
| Omni's own CPU (cores), mean | 0 | 0.00999 | +0.00999 (native is 0) | +0.008689 to +0.01129 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.509 | 1.503 | -0.4% | -0.06613 to +0.0555 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 447.3 | -1.0% | -23.7 to +14.87 | no |
| HPA replicas, mean | 8.475 | 11.48 | +35.5% | +2.565 to +3.449 | yes: power given |
| pods started | 4.6 | 10.9 | +137.0% | +4.992 to +7.608 | yes: power given |
| pod start wait, total (s) | 21.7 | 47.1 | +117.1% | -5.311 to +56.11 | no |
| pod start wait, mean (s) | 3.808 | 4.109 | +7.9% | -3.093 to +3.695 | no |
| host CPU busy, the real machine under kind (%) | 43.28 | 43.11 | -0.4% | -1.727 to +1.387 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 57 | 12.8 |  |
| machine down | omni | 42 | 9.9 | -15 s (-26%) |
| spike | native | 212 | 47.6 |  |
| spike | omni | 195 | 45.2 | -16 s (-8%) |
| runaway pod started | native | 95 | 9.1 |  |
| runaway pod started | omni | 57 | 5.4 | -38 s (-40%) |
| probe blind | native | 61 | 0.7 |  |
| probe blind | omni | 61 | 0.1 | -0 s (-0%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*