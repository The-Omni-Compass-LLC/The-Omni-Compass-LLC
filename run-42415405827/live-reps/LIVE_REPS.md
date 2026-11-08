# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.513 | 1.514 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.3 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.3 | 159.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan |
| response time (ms), mean | 175.9 | 86.79 | 91.49 |
| response time (ms), 95th percentile | 401.8 | 134.7 | 132.9 |
| response time (ms), 99th percentile | 677.5 | 186.8 | 170.1 |
| time over the response line (% of samples) | 3.226 | 0.0241 | 0.2328 |
| failed requests (%) | 0 | 0 | 0.1113 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.5 | 24.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2733 | 0.22 | 0.05333 |
| utilisation (used / allocatable) | 0.04223 | 0.03963 | 0.04069 |
| CPU used (cores), mean | 1.014 | 0.9512 | 0.9766 |
| Omni's own CPU (cores), mean | 0 | 0.03967 | 0.03958 |
| CPU used with Omni's own (cores), mean | 1.014 | 0.9908 | 1.016 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 654.3 | 686.3 | 673.1 |
| HPA replicas, mean | 8.68 | 9.418 | 9.624 |
| pods started | 5.2 | 3.9 | 9.6 |
| pod start wait, total (s) | 8.3 | 5.5 | 18.2 |
| pod start wait, mean (s) | 1.593 | 1.456 | 1.911 |
| host CPU busy, the real machine under kind (%) | 30.61 | 30.52 | 31.35 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0001 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.3 | −0.3% | −0.8615 to −0.1047 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.3 | −0.3% | −0.8615 to −0.1047 | yes: GAIN |
| response time (ms), mean | 175.9 | 86.79 | −50.7% | −111.6976 to −66.5200 | yes: GAIN |
| response time (ms), 95th percentile | 401.8 | 134.7 | −66.5% | −329.8382 to −204.5398 | yes: GAIN |
| response time (ms), 99th percentile | 677.5 | 186.8 | −72.4% | −592.4552 to −388.9644 | yes: GAIN |
| time over the response line (% of samples) | 3.226 | 0.0241 | −99.3% | −4.6175 to −1.7867 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0 | −100.0% | −4.0064 to −1.5936 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.5 | +20.500 (native is 0) | +17.0571 to +23.9429 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2733 | 0.22 | −19.5% | −0.3631 to +0.2564 | no |
| utilisation (used / allocatable) | 0.04223 | 0.03963 | −6.1% | −0.0039 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.014 | 0.9512 | −6.1% | −0.0925 to −0.0321 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03967 | +0.040 (native is 0) | +0.0355 to +0.0439 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.014 | 0.9908 | −2.2% | −0.0495 to +0.0042 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 654.3 | 686.3 | +4.9% | +16.5094 to +47.5711 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.68 | 9.418 | +8.5% | +0.2447 to +1.2308 | yes: power given |
| pods started | 5.2 | 3.9 | −25.0% | −2.7326 to +0.1326 | no |
| pod start wait, total (s) | 8.3 | 5.5 | −33.7% | −5.2502 to −0.3498 | yes: GAIN |
| pod start wait, mean (s) | 1.593 | 1.456 | −8.6% | −0.4402 to +0.1652 | no |
| host CPU busy, the real machine under kind (%) | 30.61 | 30.52 | −0.3% | −0.5726 to +0.4095 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself (the pod autoscaler removed, its own pod muscle) vs native, 10 paired repetitions

| Gauge | native | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.0% | −0.0103 to +0.0093 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.8 | 159.3 | −0.3% | −1.3726 to +0.4536 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.8 | 159.3 | −0.3% | −1.3726 to +0.4536 | no |
| response time (ms), mean | 175.9 | 91.49 | −48.0% | −106.2354 to −62.5649 | yes: GAIN |
| response time (ms), 95th percentile | 401.8 | 132.9 | −66.9% | −331.5811 to −206.3619 | yes: GAIN |
| response time (ms), 99th percentile | 677.5 | 170.1 | −74.9% | −619.0207 to −395.7349 | yes: GAIN |
| time over the response line (% of samples) | 3.226 | 0.2328 | −92.8% | −4.3979 to −1.5889 | yes: GAIN |
| failed requests (%) | 0 | 0.1113 | +0.111 (native is 0) | +0.0458 to +0.1769 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2.8 | 0.2 | −92.9% | −3.9572 to −1.2428 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 24.4 | +24.400 (native is 0) | +18.4420 to +30.3580 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2733 | 0.05333 | −80.5% | −0.5113 to +0.0713 | no |
| utilisation (used / allocatable) | 0.04223 | 0.04069 | −3.6% | −0.0023 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.014 | 0.9766 | −3.6% | −0.0553 to −0.0184 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03958 | +0.040 (native is 0) | +0.0357 to +0.0435 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.014 | 1.016 | +0.3% | −0.0132 to +0.0186 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 654.3 | 673.1 | +2.9% | +9.5805 to +28.0473 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.68 | 9.624 | +10.9% | +0.8285 to +1.0596 | yes: power given |
| pods started | 5.2 | 9.6 | +84.6% | +2.9615 to +5.8385 | yes: power given |
| pod start wait, total (s) | 8.3 | 18.2 | +119.3% | +6.2926 to +13.5074 | yes: LOSS |
| pod start wait, mean (s) | 1.593 | 1.911 | +19.9% | −0.0192 to +0.6541 | no |
| host CPU busy, the real machine under kind (%) | 30.61 | 31.35 | +2.4% | +0.5000 to +0.9904 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## Omni-Compass by itself vs Omni-Compass and native, 10 paired repetitions

| Gauge | omni | Omni-Compass by itself (no pod autoscaler; its own pod muscle) | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.514 | 1.512 | −0.1% | −0.0123 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.3 | 159.3 | +0.0% | −1.1871 to +1.2343 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.3 | 159.3 | +0.0% | −1.1871 to +1.2343 | no |
| response time (ms), mean | 86.79 | 91.49 | +5.4% | +0.9590 to +8.4582 | yes: LOSS |
| response time (ms), 95th percentile | 134.7 | 132.9 | −1.3% | −5.4563 to +1.8913 | no |
| response time (ms), 99th percentile | 186.8 | 170.1 | −8.9% | −30.5742 to −2.7618 | yes: GAIN |
| time over the response line (% of samples) | 0.0241 | 0.2328 | +866.1% | +0.1377 to +0.2798 | yes: LOSS |
| failed requests (%) | 0 | 0.1113 | +0.111 (native is 0) | +0.0458 to +0.1769 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 20.5 | 24.4 | +19.0% | −3.2646 to +11.0646 | no |
| governor's additions decided while the service was still inside its line (% of its additions) | 90 | 73.33 | −18.5% | −59.5167 to +26.1833 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.22 | 0.05333 | −75.8% | −0.4707 to +0.1374 | no |
| utilisation (used / allocatable) | 0.03963 | 0.04069 | +2.7% | +0.0002 to +0.0019 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.9512 | 0.9766 | +2.7% | +0.0057 to +0.0453 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0.03967 | 0.03958 | −0.2% | −0.0007 to +0.0005 | no |
| CPU used with Omni's own (cores), mean | 0.9908 | 1.016 | +2.6% | +0.0054 to +0.0453 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 686.3 | 673.1 | −1.9% | −24.4391 to −2.0136 | yes, down (shown, not judged) |
| HPA replicas, mean | 9.418 | 9.624 | +2.2% | −0.3755 to +0.7881 | no |
| pods started | 3.9 | 9.6 | +146.2% | +4.0463 to +7.3537 | yes: power given |
| pod start wait, total (s) | 5.5 | 18.2 | +230.9% | +8.3548 to +17.0452 | yes: LOSS |
| pod start wait, mean (s) | 1.456 | 1.911 | +31.3% | +0.1547 to +0.7552 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 30.52 | 31.35 | +2.7% | +0.3070 to +1.3466 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*