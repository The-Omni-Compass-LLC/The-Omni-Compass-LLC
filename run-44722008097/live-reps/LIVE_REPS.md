# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.066 | 4.229 |
| node-hours | 2.515 | 2.519 | 1.705 | 1.774 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 272 | 271.1 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 272 | 210.3 | 215.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 299.6 | 303.5 | 282 | 284.8 |
| response time (ms), 95th percentile | 922.5 | 933.1 | 1010 | 1002 |
| response time (ms), 99th percentile | 1245 | 1238 | 1332 | 1382 |
| time over the response line (% of samples) | 8.729 | 8.924 | 8.971 | 9.057 |
| failed requests (%) | 0.04724 | 0 | 0.01538 | 0.01538 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 4.9 | 5.8 | 6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 197.4 | 180.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 11.11 | 35 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.91 | 11.21 | 21.25 | 12.32 |
| utilisation (used / allocatable) | 0.05647 | 0.05719 | 0.08288 | 0.08163 |
| CPU used (cores), mean | 1.355 | 1.373 | 1.336 | 1.352 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.072 | 0.07124 |
| CPU used with Omni's own (cores), mean | 1.355 | 1.373 | 1.408 | 1.423 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.4 | 489.6 | 381.7 | 386.8 |
| HPA replicas, mean | 1.957 | 1.962 | 2.186 | 2.274 |
| pods started | 0.1 | 0 | 1.5 | 1.1 |
| pod start wait, total (s) | 0.2 | 0 | 3.2 | 2.7 |
| pod start wait, mean (s) | 0.2 | 0 | 1.097 | 0.7583 |
| host CPU busy, the real machine under kind (%) | 39.17 | 39.36 | 42.17 | 42.66 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 779.4 | 780.8 | 782.9 | 786.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.057 | 3.363 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5125 | 4.629 | 2.475 | 5.875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 15.3 | 1.2 | 21.6 |
| queue: job turnaround, submitted to done, mean (s) | 83.75 | 81.83 | 86.8 | 87.04 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan | nan | nan |

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
| worker nodes in service, mean | 6 | 4.229 | −29.5% | −2.6528 to −0.8892 | yes: GAIN |
| node-hours | 2.519 | 1.774 | −29.6% | −1.1102 to −0.3802 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | −0.1% | −0.8694 to +0.2452 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 215.9 | −20.6% | −83.6352 to −28.4891 | yes: GAIN |
| response time (ms), mean | 303.5 | 284.8 | −6.1% | −30.6490 to −6.6417 | yes: GAIN |
| response time (ms), 95th percentile | 933.1 | 1002 | +7.4% | −16.5139 to +154.3019 | no |
| response time (ms), 99th percentile | 1238 | 1382 | +11.6% | −48.1254 to +335.7074 | no |
| time over the response line (% of samples) | 8.924 | 9.057 | +1.5% | −0.5613 to +0.8278 | no |
| failed requests (%) | 0 | 0.01538 | +0.015 (native is 0) | −0.0194 to +0.0502 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 6 | +22.4% | +0.1198 to +2.0802 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 180.4 | +180.400 (native is 0) | +105.9773 to +254.8227 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.21 | 12.32 | +9.9% | −1.5452 to +3.7585 | no |
| utilisation (used / allocatable) | 0.05719 | 0.08163 | +42.7% | +0.0117 to +0.0372 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.373 | 1.352 | −1.5% | −0.0531 to +0.0110 | no |
| Omni's own CPU (cores), mean | 0 | 0.07124 | +0.071 (native is 0) | +0.0626 to +0.0799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.373 | 1.423 | +3.7% | +0.0123 to +0.0881 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.6 | 386.8 | −21.0% | −153.3692 to −52.1881 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.962 | 2.274 | +15.9% | +0.0498 to +0.5734 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | −0.1818 to +2.3818 | no |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | −0.4280 to +5.8280 | no |
| pod start wait, mean (s) | 0 | 0.7583 | +0.758 (native is 0) | −0.1472 to +1.6639 | no |
| host CPU busy, the real machine under kind (%) | 39.36 | 42.66 | +8.4% | +2.4658 to +4.1356 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.8 | 786.4 | +0.7% | −0.7462 to +11.9462 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.363 | −43.9% | −3.8156 to −1.4575 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.629 | 5.875 | +26.9% | −1.6146 to +4.1062 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 15.3 | 21.6 | +41.2% | −7.4553 to +20.0553 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.83 | 87.04 | +6.4% | −1.6435 to +12.0518 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.515 | 2.519 | +0.2% | −0.0025 to +0.0115 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 272 | +0.3% | +0.0548 to +1.7653 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 272 | +0.3% | +0.0548 to +1.7653 | yes: power given |
| response time (ms), mean | 299.6 | 303.5 | +1.3% | −3.8504 to +11.6372 | no |
| response time (ms), 95th percentile | 922.5 | 933.1 | +1.2% | −2.7453 to +24.1123 | no |
| response time (ms), 99th percentile | 1245 | 1238 | −0.5% | −30.8749 to +17.5691 | no |
| time over the response line (% of samples) | 8.729 | 8.924 | +2.2% | −0.2511 to +0.6394 | no |
| failed requests (%) | 0.04724 | 0 | −100.0% | −0.1541 to +0.0596 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 4.9 | −5.8% | −0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.91 | 11.21 | −46.4% | −30.3477 to +10.9610 | no |
| utilisation (used / allocatable) | 0.05647 | 0.05719 | +1.3% | −0.0008 to +0.0022 | no |
| CPU used (cores), mean | 1.355 | 1.373 | +1.3% | −0.0182 to +0.0530 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.355 | 1.373 | +1.3% | −0.0182 to +0.0530 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.4 | 489.6 | −1.6% | −22.0452 to +6.4802 | no |
| HPA replicas, mean | 1.957 | 1.962 | +0.3% | −0.1634 to +0.1744 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 39.17 | 39.36 | +0.5% | −0.6693 to +1.0456 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.4 | 780.8 | +0.2% | −2.5208 to +5.3208 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5125 | 4.629 | +803.3% | −5.0174 to +13.2507 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 15.3 | +537.5% | −15.2767 to +41.0767 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.75 | 81.83 | −2.3% | −9.6624 to +5.8374 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.066 | −32.2% | −2.7279 to −1.1396 | yes: GAIN |
| node-hours | 2.515 | 1.705 | −32.2% | −1.1413 to −0.4790 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.1 | +0.0% | −0.7322 to +0.8557 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 210.3 | −22.4% | −85.7123 to −35.7600 | yes: GAIN |
| response time (ms), mean | 299.6 | 282 | −5.9% | −24.6340 to −10.4752 | yes: GAIN |
| response time (ms), 95th percentile | 922.5 | 1010 | +9.5% | +39.0993 to +136.4247 | yes: LOSS |
| response time (ms), 99th percentile | 1245 | 1332 | +7.0% | +52.7755 to +121.6565 | yes: LOSS |
| time over the response line (% of samples) | 8.729 | 8.971 | +2.8% | −0.3291 to +0.8121 | no |
| failed requests (%) | 0.04724 | 0.01538 | −67.4% | −0.1039 to +0.0402 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 5.8 | +11.5% | −0.9888 to +2.1888 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 197.4 | +197.400 (native is 0) | +110.6453 to +284.1547 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.91 | 21.25 | +1.6% | −3.1396 to +3.8163 | no |
| utilisation (used / allocatable) | 0.05647 | 0.08288 | +46.8% | +0.0150 to +0.0378 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.355 | 1.336 | −1.4% | −0.0550 to +0.0175 | no |
| Omni's own CPU (cores), mean | 0 | 0.072 | +0.072 (native is 0) | +0.0623 to +0.0817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.355 | 1.408 | +3.9% | +0.0172 to +0.0893 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.4 | 381.7 | −23.3% | −167.4015 to −64.0498 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.186 | +11.7% | −0.1190 to +0.5771 | no |
| pods started | 0.1 | 1.5 | +1400.0% | +0.0428 to +2.7572 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.2 | +1500.0% | +0.2194 to +5.7806 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.097 | +448.3% | −0.1845 to +1.9778 | no |
| host CPU busy, the real machine under kind (%) | 39.17 | 42.17 | +7.7% | +2.3675 to +3.6395 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.4 | 782.9 | +0.4% | −1.6499 to +8.6499 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.057 | −49.0% | −3.9775 to −1.9078 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5125 | 2.475 | +382.9% | −2.4767 to +6.4017 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 1.2 | −50.0% | −3.9144 to +1.5144 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.75 | 86.8 | +3.7% | −1.1026 to +7.2193 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.066 | −32.2% | −2.7279 to −1.1396 | yes: GAIN |
| node-hours | 2.519 | 1.705 | −32.3% | −1.1437 to −0.4856 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.1 | −0.3% | −1.6595 to −0.0370 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 210.3 | −22.7% | −86.7830 to −36.5093 | yes: GAIN |
| response time (ms), mean | 303.5 | 282 | −7.1% | −32.5920 to −10.3040 | yes: GAIN |
| response time (ms), 95th percentile | 933.1 | 1010 | +8.3% | +38.3510 to +115.8060 | yes: LOSS |
| response time (ms), 99th percentile | 1238 | 1332 | +7.6% | +47.7071 to +140.0307 | yes: LOSS |
| time over the response line (% of samples) | 8.924 | 8.971 | +0.5% | −0.8407 to +0.9354 | no |
| failed requests (%) | 0 | 0.01538 | +0.015 (native is 0) | −0.0194 to +0.0502 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 5.8 | +18.4% | −0.5871 to +2.3871 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 197.4 | +197.400 (native is 0) | +110.6453 to +284.1547 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.21 | 21.25 | +89.4% | −13.6566 to +33.7199 | no |
| utilisation (used / allocatable) | 0.05719 | 0.08288 | +44.9% | +0.0150 to +0.0363 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.373 | 1.336 | −2.6% | −0.0921 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0.072 | +0.072 (native is 0) | +0.0623 to +0.0817 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.373 | 1.408 | +2.6% | −0.0229 to +0.0946 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 489.6 | 381.7 | −22.0% | −153.8056 to −62.0807 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.962 | 2.186 | +11.4% | −0.0268 to +0.4739 | no |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.2271 to +2.7729 | yes: power given |
| pod start wait, total (s) | 0 | 3.2 | +3.200 (native is 0) | +0.5924 to +5.8076 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.097 | +1.097 (native is 0) | +0.2512 to +1.9422 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.36 | 42.17 | +7.2% | +2.0851 to +3.5455 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.8 | 782.9 | +0.3% | −0.0709 to +4.2709 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.057 | −49.0% | −3.9775 to −1.9078 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.629 | 2.475 | −46.5% | −6.8491 to +2.5408 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 15.3 | 1.2 | −92.2% | −44.9909 to +16.7909 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.83 | 86.8 | +6.1% | −2.7544 to +12.6961 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.229 | −29.5% | −2.6528 to −0.8892 | yes: GAIN |
| node-hours | 2.515 | 1.774 | −29.5% | −1.1079 to −0.3734 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.7 | +0.2% | −0.3402 to +1.5360 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 215.9 | −20.3% | −82.7078 to −27.5964 | yes: GAIN |
| response time (ms), mean | 299.6 | 284.8 | −4.9% | −27.0132 to −2.4907 | yes: GAIN |
| response time (ms), 95th percentile | 922.5 | 1002 | +8.6% | −13.4711 to +172.6261 | no |
| response time (ms), 99th percentile | 1245 | 1382 | +11.0% | −45.1735 to +319.4497 | no |
| time over the response line (% of samples) | 8.729 | 9.057 | +3.8% | −0.2150 to +0.8698 | no |
| failed requests (%) | 0.04724 | 0.01538 | −67.4% | −0.1039 to +0.0402 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 6 | +15.4% | −0.4064 to +2.0064 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 180.4 | +180.400 (native is 0) | +105.9773 to +254.8227 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.91 | 12.32 | −41.1% | −28.2966 to +11.1233 | no |
| utilisation (used / allocatable) | 0.05647 | 0.08163 | +44.6% | +0.0118 to +0.0385 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.355 | 1.352 | −0.3% | −0.0373 to +0.0300 | no |
| Omni's own CPU (cores), mean | 0 | 0.07124 | +0.071 (native is 0) | +0.0626 to +0.0799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.355 | 1.423 | +5.0% | +0.0308 to +0.1044 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 497.4 | 386.8 | −22.2% | −167.0452 to −54.0771 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.274 | +16.2% | +0.0594 to +0.5748 | yes: power given |
| pods started | 0.1 | 1.1 | +1000.0% | −0.1681 to +2.1681 | no |
| pod start wait, total (s) | 0.2 | 2.7 | +1250.0% | −0.4251 to +5.4251 | no |
| pod start wait, mean (s) | 0.2 | 0.7583 | +279.2% | −0.2696 to +1.3862 | no |
| host CPU busy, the real machine under kind (%) | 39.17 | 42.66 | +8.9% | +2.1593 to +4.8184 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 779.4 | 786.4 | +0.9% | −2.4776 to +16.4776 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.363 | −43.9% | −3.8156 to −1.4575 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5125 | 5.875 | +1046.3% | −6.6314 to +17.3564 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 21.6 | +800.0% | −22.7238 to +61.1238 | no |
| queue: job turnaround, submitted to done, mean (s) | 83.75 | 87.04 | +3.9% | −4.0131 to +10.5965 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*