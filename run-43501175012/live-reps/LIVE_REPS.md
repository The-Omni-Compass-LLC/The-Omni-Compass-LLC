# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.89 | 11.29 |
| node-hours | 5.034 | 5.039 | 4.564 | 4.728 |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 527.6 | 528.2 | 527 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 527.6 | 493.3 | 504.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 763.9 | 929.5 | 898.2 | 1082 |
| response time (ms), 95th percentile | 3041 | 3976 | 3773 | 4714 |
| response time (ms), 99th percentile | 4124 | 5583 | 5027 | 6468 |
| time over the response line (% of samples) | 27.91 | 31.93 | 32.56 | 37.19 |
| failed requests (%) | 0 | 0.132 | 0.007722 | 0.1728 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 17.6 | 16.3 | 17.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 67.1 | 37.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 12.48 | 20.83 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.9 | 67.8 | 26.83 | 90.01 |
| utilisation (used / allocatable) | 0.03693 | 0.03537 | 0.04131 | 0.03879 |
| CPU used (cores), mean | 1.773 | 1.698 | 1.802 | 1.742 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05701 | 0.048 |
| CPU used with Omni's own (cores), mean | 1.773 | 1.698 | 1.859 | 1.79 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.7 | 747.2 | 658.6 | 695.9 |
| HPA replicas, mean | 3.987 | 4.149 | 4.689 | 5.064 |
| pods started | 0.4 | 0 | 3 | 3.5 |
| pod start wait, total (s) | 1 | 0 | 8.5 | 9.5 |
| pod start wait, mean (s) | 1 | 0 | 2.143 | 2.439 |
| host CPU busy, the real machine under kind (%) | 54.62 | 61.87 | 61.15 | 68.02 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 922.4 | 1054 | 983.4 | 1123 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.767 | 10.52 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 4.667 | 0.1833 | 18.37 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 32.8 | 0.9 | 162.9 |
| queue: job turnaround, submitted to done, mean (s) | 228.6 | 365.6 | 283.8 | 432.9 |
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
| worker nodes in service, mean | 12 | 11.29 | −6.0% | −1.7436 to +0.3143 | no |
| node-hours | 5.039 | 4.728 | −6.2% | −0.7422 to +0.1197 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 527 | −0.1% | −2.6925 to +1.6518 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 504.6 | −4.3% | −55.9052 to +10.0229 | no |
| response time (ms), mean | 929.5 | 1082 | +16.4% | +46.1946 to +258.1265 | yes: LOSS |
| response time (ms), 95th percentile | 3976 | 4714 | +18.6% | +319.5470 to +1158.1710 | yes: LOSS |
| response time (ms), 99th percentile | 5583 | 6468 | +15.9% | +150.0165 to +1620.0849 | yes: LOSS |
| time over the response line (% of samples) | 31.93 | 37.19 | +16.5% | +1.4067 to +9.1143 | yes: LOSS |
| failed requests (%) | 0.132 | 0.1728 | +30.9% | −0.2778 to +0.3594 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 17.5 | −0.6% | −3.1056 to +2.9056 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 | +37.800 (native is 0) | +28.2638 to +47.3362 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 67.8 | 90.01 | +32.8% | −11.5033 to +55.9199 | no |
| utilisation (used / allocatable) | 0.03537 | 0.03879 | +9.7% | +0.0001 to +0.0068 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.698 | 1.742 | +2.6% | −0.0572 to +0.1448 | no |
| Omni's own CPU (cores), mean | 0 | 0.048 | +0.048 (native is 0) | +0.0399 to +0.0561 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.698 | 1.79 | +5.4% | −0.0107 to +0.1943 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747.2 | 695.9 | −6.9% | −98.4143 to −4.1623 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.149 | 5.064 | +22.0% | +0.5105 to +1.3191 | yes: power given |
| pods started | 0 | 3.5 | +3.500 (native is 0) | +1.9826 to +5.0174 | yes: power given |
| pod start wait, total (s) | 0 | 9.5 | +9.500 (native is 0) | +5.0234 to +13.9766 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.439 | +2.439 (native is 0) | +1.7342 to +3.1444 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.87 | 68.02 | +9.9% | +4.3072 to +7.9929 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1054 | 1123 | +6.6% | +38.5523 to +99.8477 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.52 | −12.3% | −3.2094 to +0.2593 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 4.667 | 18.37 | +293.6% | +2.7611 to +24.6389 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 32.8 | 162.9 | +396.6% | +13.4830 to +246.7170 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 365.6 | 432.9 | +18.4% | +33.8133 to +100.7950 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.034 | 5.039 | +0.1% | −0.0100 to +0.0207 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 527.6 | −0.1% | −3.0732 to +2.2800 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 527.6 | −0.1% | −3.0732 to +2.2800 | no |
| response time (ms), mean | 763.9 | 929.5 | +21.7% | +99.5097 to +231.7223 | yes: LOSS |
| response time (ms), 95th percentile | 3041 | 3976 | +30.7% | +531.8723 to +1336.4167 | yes: LOSS |
| response time (ms), 99th percentile | 4124 | 5583 | +35.4% | +924.0510 to +1993.0688 | yes: LOSS |
| time over the response line (% of samples) | 27.91 | 31.93 | +14.4% | +1.5116 to +6.5317 | yes: LOSS |
| failed requests (%) | 0 | 0.132 | +0.132 (native is 0) | −0.0922 to +0.3562 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 17.6 | +22.2% | +1.2108 to +5.1892 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.9 | 67.8 | +258.7% | +6.1244 to +91.6723 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03693 | 0.03537 | −4.2% | −0.0044 to +0.0013 | no |
| CPU used (cores), mean | 1.773 | 1.698 | −4.2% | −0.2109 to +0.0614 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.773 | 1.698 | −4.2% | −0.2109 to +0.0614 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.7 | 747.2 | +3.4% | −30.2601 to +79.2815 | no |
| HPA replicas, mean | 3.987 | 4.149 | +4.1% | −0.1121 to +0.4369 | no |
| pods started | 0.4 | 0 | −100.0% | −0.7694 to −0.0306 | yes: GAIN |
| pod start wait, total (s) | 1 | 0 | −100.0% | −1.9537 to −0.0463 | yes: GAIN |
| pod start wait, mean (s) | 1 | 0 | −100.0% | −1.9537 to −0.0463 | yes: GAIN |
| host CPU busy, the real machine under kind (%) | 54.62 | 61.87 | +13.3% | +6.1686 to +8.3264 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 922.4 | 1054 | +14.2% | +95.4885 to +167.1115 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 4.667 | +3512.9% | −1.8390 to +10.9140 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 32.8 | +4585.7% | −37.4983 to +101.6983 | no |
| queue: job turnaround, submitted to done, mean (s) | 228.6 | 365.6 | +59.9% | +97.8494 to +176.1589 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.2% | −2.1974 to −0.0216 | yes: GAIN |
| node-hours | 5.034 | 4.564 | −9.3% | −0.9241 to −0.0152 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 528.2 | +0.1% | −1.6006 to +2.1352 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 493.3 | −6.6% | −68.8485 to −0.5710 | yes: GAIN |
| response time (ms), mean | 763.9 | 898.2 | +17.6% | +62.9218 to +205.6151 | yes: LOSS |
| response time (ms), 95th percentile | 3041 | 3773 | +24.1% | +394.3235 to +1068.9395 | yes: LOSS |
| response time (ms), 99th percentile | 4124 | 5027 | +21.9% | +525.0646 to +1281.2386 | yes: LOSS |
| time over the response line (% of samples) | 27.91 | 32.56 | +16.7% | +2.7636 to +6.5455 | yes: LOSS |
| failed requests (%) | 0 | 0.007722 | +0.008 (native is 0) | −0.0097 to +0.0252 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 16.3 | +13.2% | +0.1014 to +3.6986 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.1 | +67.100 (native is 0) | +26.3471 to +107.8529 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.9 | 26.83 | +42.0% | +0.1431 to +15.7235 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03693 | 0.04131 | +11.9% | +0.0009 to +0.0078 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.773 | 1.802 | +1.6% | −0.0245 to +0.0824 | no |
| Omni's own CPU (cores), mean | 0 | 0.05701 | +0.057 (native is 0) | +0.0521 to +0.0619 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.773 | 1.859 | +4.9% | +0.0305 to +0.1415 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.7 | 658.6 | −8.9% | −115.3340 to −12.8402 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.987 | 4.689 | +17.6% | +0.3463 to +1.0575 | yes: power given |
| pods started | 0.4 | 3 | +650.0% | +0.9073 to +4.2927 | yes: power given |
| pod start wait, total (s) | 1 | 8.5 | +750.0% | +1.1803 to +13.8197 | yes: LOSS |
| pod start wait, mean (s) | 1 | 2.143 | +114.3% | −0.3786 to +2.6638 | no |
| host CPU busy, the real machine under kind (%) | 54.62 | 61.15 | +12.0% | +5.4390 to +7.6253 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 922.4 | 983.4 | +6.6% | +35.8702 to +86.1298 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.767 | −18.6% | −4.3126 to −0.1536 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 0.1833 | +41.9% | −0.0336 to +0.1420 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 228.6 | 283.8 | +24.1% | +35.5265 to +74.7735 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.2% | −2.1974 to −0.0216 | yes: GAIN |
| node-hours | 5.039 | 4.564 | −9.4% | −0.9258 to −0.0242 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 528.2 | +0.1% | −0.9414 to +2.2693 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 493.3 | −6.5% | −69.3527 to +0.7264 | no |
| response time (ms), mean | 929.5 | 898.2 | −3.4% | −83.8075 to +21.1124 | no |
| response time (ms), 95th percentile | 3976 | 3773 | −5.1% | −454.2349 to +49.2089 | no |
| response time (ms), 99th percentile | 5583 | 5027 | −9.9% | −1100.8712 to −9.9454 | yes: GAIN |
| time over the response line (% of samples) | 31.93 | 32.56 | +2.0% | −2.2617 to +3.5276 | no |
| failed requests (%) | 0.132 | 0.007722 | −94.2% | −0.3316 to +0.0830 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17.6 | 16.3 | −7.4% | −1.6455 to −0.9545 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 67.1 | +67.100 (native is 0) | +26.3471 to +107.8529 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 67.8 | 26.83 | −60.4% | −82.0310 to +0.1010 | no |
| utilisation (used / allocatable) | 0.03537 | 0.04131 | +16.8% | +0.0030 to +0.0089 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.698 | 1.802 | +6.1% | −0.0554 to +0.2628 | no |
| Omni's own CPU (cores), mean | 0 | 0.05701 | +0.057 (native is 0) | +0.0521 to +0.0619 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.698 | 1.859 | +9.5% | −0.0019 to +0.3233 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747.2 | 658.6 | −11.9% | −136.6552 to −40.5402 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.149 | 4.689 | +13.0% | +0.1663 to +0.9127 | yes: power given |
| pods started | 0 | 3 | +3.000 (native is 0) | +1.4548 to +4.5452 | yes: power given |
| pod start wait, total (s) | 0 | 8.5 | +8.500 (native is 0) | +2.5702 to +14.4298 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.143 | +2.143 (native is 0) | +1.1638 to +3.1214 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.87 | 61.15 | −1.2% | −1.2413 to −0.1894 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1054 | 983.4 | −6.7% | −86.4611 to −54.1389 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.767 | −18.6% | −4.3126 to −0.1536 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.667 | 0.1833 | −96.1% | −10.8876 to +1.9209 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 32.8 | 0.9 | −97.3% | −101.5481 to +37.7481 | no |
| queue: job turnaround, submitted to done, mean (s) | 365.6 | 283.8 | −22.4% | −103.8875 to −59.8208 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.29 | −6.0% | −1.7436 to +0.3143 | no |
| node-hours | 5.034 | 4.728 | −6.1% | −0.7431 to +0.1312 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528 | 527 | −0.2% | −3.6124 to +1.7785 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528 | 504.6 | −4.4% | −56.0966 to +9.4210 | no |
| response time (ms), mean | 763.9 | 1082 | +41.6% | +176.3271 to +459.2260 | yes: LOSS |
| response time (ms), 95th percentile | 3041 | 4714 | +55.0% | +1144.9454 to +2201.0616 | yes: LOSS |
| response time (ms), 99th percentile | 4124 | 6468 | +56.8% | +1562.7738 to +3124.4474 | yes: LOSS |
| time over the response line (% of samples) | 27.91 | 37.19 | +33.3% | +5.0047 to +13.5597 | yes: LOSS |
| failed requests (%) | 0 | 0.1728 | +0.173 (native is 0) | −0.0030 to +0.3486 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.4 | 17.5 | +21.5% | +2.0100 to +4.1900 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.8 | +37.800 (native is 0) | +28.2638 to +47.3362 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.9 | 90.01 | +376.2% | +16.0603 to +126.1530 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03693 | 0.03879 | +5.0% | −0.0032 to +0.0069 | no |
| CPU used (cores), mean | 1.773 | 1.742 | −1.7% | −0.1859 to +0.1240 | no |
| Omni's own CPU (cores), mean | 0 | 0.048 | +0.048 (native is 0) | +0.0399 to +0.0561 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.773 | 1.79 | +1.0% | −0.1351 to +0.1692 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.7 | 695.9 | −3.7% | −108.2201 to +54.6649 | no |
| HPA replicas, mean | 3.987 | 5.064 | +27.0% | +0.5790 to +1.5753 | yes: power given |
| pods started | 0.4 | 3.5 | +775.0% | +1.7324 to +4.4676 | yes: power given |
| pod start wait, total (s) | 1 | 9.5 | +850.0% | +4.4924 to +12.5076 | yes: LOSS |
| pod start wait, mean (s) | 1 | 2.439 | +143.9% | +0.3293 to +2.5493 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.62 | 68.02 | +24.5% | +11.1111 to +15.6841 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 922.4 | 1123 | +21.7% | +142.9828 to +258.0172 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.52 | −12.3% | −3.2094 to +0.2593 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1292 | 18.37 | +14119.4% | +5.9944 to +30.4806 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 162.9 | +23171.4% | +41.1541 to +283.2459 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 228.6 | 432.9 | +89.4% | +141.9826 to +266.6340 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*