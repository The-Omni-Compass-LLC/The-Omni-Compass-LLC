# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.363 | 4.419 |
| node-hours | 2.51 | 2.516 | 1.828 | 1.855 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.7 | 271.2 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.7 | 219.8 | 222.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 246.2 | 262.6 | 230.8 | 255.7 |
| response time (ms), 95th percentile | 797.8 | 967.1 | 885.7 | 1100 |
| response time (ms), 99th percentile | 1108 | 1390 | 1244 | 1545 |
| time over the response line (% of samples) | 8.227 | 7.746 | 9.6 | 8.843 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 4.9 | 7 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 186.3 | 110.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 4 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.853 | 18.15 | 8.667 | 18.53 |
| utilisation (used / allocatable) | 0.05685 | 0.05731 | 0.07971 | 0.07875 |
| CPU used (cores), mean | 1.364 | 1.375 | 1.348 | 1.376 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0717 | 0.07545 |
| CPU used with Omni's own (cores), mean | 1.364 | 1.375 | 1.42 | 1.452 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.7 | 480.4 | 389.4 | 386.9 |
| HPA replicas, mean | 1.986 | 2.005 | 2.268 | 2.154 |
| pods started | 0.1 | 0.4 | 1.7 | 0.8 |
| pod start wait, total (s) | 0.3 | 0.5 | 4 | 1.6 |
| pod start wait, mean (s) | 0.3 | 0.5 | 1.883 | 0.6 |
| host CPU busy, the real machine under kind (%) | 39.06 | 41.29 | 42.04 | 44.46 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 755.4 | 776.8 | 759.6 | 784.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.52 | 3.136 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.8667 | 0.03333 | 0.9333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | 0.2 | 2.8 |
| queue: job turnaround, submitted to done, mean (s) | 61.04 | 82.29 | 66.06 | 87.46 |
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
| worker nodes in service, mean | 6 | 4.419 | −26.3% | −2.1834 to −0.9783 | yes: GAIN |
| node-hours | 2.516 | 1.855 | −26.3% | −0.9127 to −0.4095 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.1 | +0.2% | −0.4344 to +1.3323 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 222.4 | −18.1% | −68.1401 to −30.4788 | yes: GAIN |
| response time (ms), mean | 262.6 | 255.7 | −2.6% | −26.3399 to +12.5536 | no |
| response time (ms), 95th percentile | 967.1 | 1100 | +13.7% | −14.2861 to +279.7101 | no |
| response time (ms), 99th percentile | 1390 | 1545 | +11.2% | +5.1455 to +306.1663 | yes: LOSS |
| time over the response line (% of samples) | 7.746 | 8.843 | +14.2% | −0.0134 to +2.2066 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 6.3 | +28.6% | −0.5429 to +3.3429 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.4 | +110.400 (native is 0) | +63.9152 to +156.8848 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.15 | 18.53 | +2.0% | −2.1187 to +2.8620 | no |
| utilisation (used / allocatable) | 0.05731 | 0.07875 | +37.4% | +0.0119 to +0.0310 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.375 | 1.376 | +0.1% | −0.0189 to +0.0205 | no |
| Omni's own CPU (cores), mean | 0 | 0.07545 | +0.075 (native is 0) | +0.0679 to +0.0830 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.375 | 1.452 | +5.5% | +0.0574 to +0.0951 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.4 | 386.9 | −19.5% | −132.9350 to −54.0719 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.154 | +7.4% | −0.0910 to +0.3881 | no |
| pods started | 0.4 | 0.8 | +100.0% | −0.7285 to +1.5285 | no |
| pod start wait, total (s) | 0.5 | 1.6 | +220.0% | −1.1227 to +3.3227 | no |
| pod start wait, mean (s) | 0.5 | 0.6 | +20.0% | −0.8204 to +1.0204 | no |
| host CPU busy, the real machine under kind (%) | 41.29 | 44.46 | +7.7% | +2.6567 to +3.6821 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.8 | 784.7 | +1.0% | +1.5248 to +14.2752 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.136 | −47.7% | −3.6520 to −2.0760 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8667 | 0.9333 | +7.7% | −0.3202 to +0.4535 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 2.8 | +47.4% | −2.5790 to +4.3790 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.29 | 87.46 | +6.3% | +0.7765 to +9.5568 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.516 | +0.2% | +0.0008 to +0.0112 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.7 | +0.3% | +0.1101 to +1.7382 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.7 | +0.3% | +0.1101 to +1.7382 | yes: power given |
| response time (ms), mean | 246.2 | 262.6 | +6.7% | −17.2754 to +50.0415 | no |
| response time (ms), 95th percentile | 797.8 | 967.1 | +21.2% | −108.5799 to +447.1499 | no |
| response time (ms), 99th percentile | 1108 | 1390 | +25.4% | −99.8232 to +663.5612 | no |
| time over the response line (% of samples) | 8.227 | 7.746 | −5.8% | −3.3035 to +2.3431 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 4.9 | −5.8% | −1.4209 to +0.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.853 | 18.16 | +131.2% | +3.3716 to +17.2317 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05685 | 0.05731 | +0.8% | −0.0008 to +0.0017 | no |
| CPU used (cores), mean | 1.364 | 1.375 | +0.8% | −0.0192 to +0.0412 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.364 | 1.375 | +0.8% | −0.0192 to +0.0412 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.7 | 480.4 | −0.3% | −11.0131 to +8.3887 | no |
| HPA replicas, mean | 1.986 | 2.005 | +1.0% | −0.0537 to +0.0925 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0.3 | 0.5 | +66.7% | −0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.3 | 0.5 | +66.7% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 39.06 | 41.29 | +5.7% | +1.4712 to +2.9949 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.4 | 776.8 | +2.8% | −1.2858 to +44.0858 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.8667 | +1633.3% | +0.5266 to +1.1067 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.9 | +375.0% | +0.0995 to +2.9005 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 61.04 | 82.29 | +34.8% | −0.1839 to +42.6922 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.363 | −27.3% | −2.4777 to −0.7962 | yes: GAIN |
| node-hours | 2.51 | 1.828 | −27.2% | −1.0336 to −0.3296 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.2 | +0.2% | −0.7721 to +1.5880 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 219.8 | −18.8% | −77.7649 to −24.2358 | yes: GAIN |
| response time (ms), mean | 246.2 | 230.8 | −6.3% | −33.1909 to +2.3359 | no |
| response time (ms), 95th percentile | 797.8 | 885.7 | +11.0% | +19.1026 to +156.7394 | yes: LOSS |
| response time (ms), 99th percentile | 1108 | 1244 | +12.3% | +28.0473 to +244.6211 | yes: LOSS |
| time over the response line (% of samples) | 8.227 | 9.6 | +16.7% | −0.6217 to +3.3691 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 7 | +34.6% | +0.1899 to +3.4101 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 186.3 | +186.300 (native is 0) | +109.3417 to +263.2583 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.853 | 8.667 | +10.4% | +0.2319 to +1.3948 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05685 | 0.07971 | +40.2% | +0.0105 to +0.0352 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.364 | 1.348 | −1.2% | −0.0625 to +0.0298 | no |
| Omni's own CPU (cores), mean | 0 | 0.0717 | +0.072 (native is 0) | +0.0649 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.364 | 1.42 | +4.1% | +0.0056 to +0.1052 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.7 | 389.4 | −19.1% | −137.0730 to −47.4018 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.268 | +14.2% | +0.0876 to +0.4771 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | +0.5772 to +2.6228 | yes: power given |
| pod start wait, total (s) | 0.3 | 4 | +1233.3% | +1.1755 to +6.2245 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.883 | +527.8% | +0.2953 to +2.8713 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.06 | 42.04 | +7.6% | +2.4374 to +3.5272 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.4 | 759.6 | +0.6% | −1.5896 to +9.9896 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.52 | −41.3% | −3.6206 to −1.3402 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.03333 | −33.3% | −0.0455 to +0.0121 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.2 | −50.0% | −0.6524 to +0.2524 | no |
| queue: job turnaround, submitted to done, mean (s) | 61.04 | 66.06 | +8.2% | −0.0229 to +10.0729 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.363 | −27.3% | −2.4777 to −0.7962 | yes: GAIN |
| node-hours | 2.516 | 1.828 | −27.3% | −1.0389 to −0.3363 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.2 | −0.2% | −1.7532 to +0.7208 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 219.8 | −19.1% | −78.3210 to −25.5281 | yes: GAIN |
| response time (ms), mean | 262.6 | 230.8 | −12.1% | −71.4019 to +7.7808 | no |
| response time (ms), 95th percentile | 967.1 | 885.7 | −8.4% | −324.5387 to +161.8107 | no |
| response time (ms), 99th percentile | 1390 | 1244 | −10.5% | −487.3017 to +196.2321 | no |
| time over the response line (% of samples) | 7.746 | 9.6 | +23.9% | +0.5813 to +3.1264 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.9 | 7 | +42.9% | −0.2471 to +4.4471 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 186.3 | +186.300 (native is 0) | +109.3417 to +263.2583 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.15 | 8.667 | −52.3% | −16.6347 to −2.3420 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05731 | 0.07971 | +39.1% | +0.0092 to +0.0356 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.375 | 1.348 | −2.0% | −0.0560 to +0.0013 | no |
| Omni's own CPU (cores), mean | 0 | 0.0717 | +0.072 (native is 0) | +0.0649 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.375 | 1.42 | +3.2% | +0.0150 to +0.0737 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 480.4 | 389.4 | −18.9% | −141.5619 to −40.2884 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.268 | +13.1% | +0.0369 to +0.4890 | yes: power given |
| pods started | 0.4 | 1.7 | +325.0% | +0.1295 to +2.4705 | yes: power given |
| pod start wait, total (s) | 0.5 | 4 | +700.0% | +1.0394 to +5.9606 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.883 | +276.7% | +0.3140 to +2.4527 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.29 | 42.04 | +1.8% | +0.1725 to +1.3260 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.8 | 759.6 | −2.2% | −35.3111 to +0.9111 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.52 | −41.3% | −3.6206 to −1.3402 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8667 | 0.03333 | −96.2% | −1.1327 to −0.5340 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.2 | −89.5% | −3.3189 to −0.0811 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 82.29 | 66.06 | −19.7% | −33.6246 to +1.1663 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.419 | −26.3% | −2.1834 to −0.9783 | yes: GAIN |
| node-hours | 2.51 | 1.855 | −26.1% | −0.9069 to −0.4034 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 272.1 | +0.5% | +0.6629 to +2.0833 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 222.4 | −17.9% | −67.5265 to −29.2440 | yes: GAIN |
| response time (ms), mean | 246.2 | 255.7 | +3.9% | −25.0171 to +43.9970 | no |
| response time (ms), 95th percentile | 797.8 | 1100 | +37.9% | −37.2265 to +641.2205 | no |
| response time (ms), 99th percentile | 1108 | 1545 | +39.5% | +26.2962 to +848.7536 | yes: LOSS |
| time over the response line (% of samples) | 8.227 | 8.843 | +7.5% | −2.4010 to +3.6339 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.2 | 6.3 | +21.2% | +0.0634 to +2.1366 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.4 | +110.400 (native is 0) | +63.9152 to +156.8848 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.853 | 18.53 | +135.9% | +2.1443 to +19.2024 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05685 | 0.07875 | +38.5% | +0.0132 to +0.0306 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.364 | 1.376 | +0.9% | −0.0202 to +0.0438 | no |
| Omni's own CPU (cores), mean | 0 | 0.07545 | +0.075 (native is 0) | +0.0679 to +0.0830 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.364 | 1.452 | +6.4% | +0.0507 to +0.1238 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 481.7 | 386.9 | −19.7% | −127.8696 to −61.7618 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.986 | 2.154 | +8.5% | −0.0970 to +0.4328 | no |
| pods started | 0.1 | 0.8 | +700.0% | −0.2567 to +1.6567 | no |
| pod start wait, total (s) | 0.3 | 1.6 | +433.3% | −0.5485 to +3.1485 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 39.06 | 44.46 | +13.8% | +4.2859 to +6.5189 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.4 | 784.7 | +3.9% | +0.9571 to +57.6429 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.136 | −47.7% | −3.6520 to −2.0760 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.9333 | +1766.7% | +0.3811 to +1.3856 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 2.8 | +600.0% | −0.7847 to +5.5847 | no |
| queue: job turnaround, submitted to done, mean (s) | 61.04 | 87.46 | +43.3% | +3.1705 to +49.6712 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*