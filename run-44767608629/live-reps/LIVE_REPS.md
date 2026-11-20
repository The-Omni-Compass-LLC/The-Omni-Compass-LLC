# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.75 | 9.66 |
| node-hours | 5.027 | 5.033 | 4.086 | 4.048 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 524 | 524.5 | 525.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 524 | 453.9 | 451.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 418.4 | 464 | 467.1 | 588.2 |
| response time (ms), 95th percentile | 1514 | 1796 | 1924 | 2691 |
| response time (ms), 99th percentile | 2095 | 2679 | 2532 | 3979 |
| time over the response line (% of samples) | 15.62 | 17.55 | 19.13 | 21.85 |
| failed requests (%) | 0 | 0.007752 | 0.02372 | 0.1571 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 11.2 | 10.7 | 13.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 219 | 89.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 31.19 | 50.83 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.96 | 38.1 | 12.44 | 33.08 |
| utilisation (used / allocatable) | 0.03191 | 0.03138 | 0.04087 | 0.04168 |
| CPU used (cores), mean | 1.532 | 1.506 | 1.562 | 1.591 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05213 | 0.03795 |
| CPU used with Omni's own (cores), mean | 1.532 | 1.506 | 1.614 | 1.629 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.6 | 844.9 | 702.1 | 682.3 |
| HPA replicas, mean | 4.024 | 4.07 | 4.525 | 5.223 |
| pods started | 0.3 | 0.3 | 1.9 | 2.8 |
| pod start wait, total (s) | 0.7 | 0.5 | 4.4 | 8.5 |
| pod start wait, mean (s) | 0.7 | 0.35 | 1.6 | 2.177 |
| host CPU busy, the real machine under kind (%) | 47.28 | 52.02 | 52.31 | 58.17 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 811.8 | 879.4 | 839.5 | 942.1 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.4 | 7.741 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 5.658 | 0.07917 | 5.888 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 31.3 | 0.5 | 34.2 |
| queue: job turnaround, submitted to done, mean (s) | 122.3 | 188.3 | 146.1 | 245.2 |
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
| worker nodes in service, mean | 12 | 9.66 | −19.5% | −3.8811 to −0.7987 | yes: GAIN |
| node-hours | 5.033 | 4.048 | −19.6% | −1.6350 to −0.3338 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 525.1 | +0.2% | −0.8763 to +3.0275 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 451.6 | −13.8% | −122.1348 to −22.6723 | yes: GAIN |
| response time (ms), mean | 464 | 588.2 | +26.8% | +26.3944 to +221.9876 | yes: LOSS |
| response time (ms), 95th percentile | 1796 | 2691 | +49.9% | +292.4584 to +1497.7006 | yes: LOSS |
| response time (ms), 99th percentile | 2679 | 3979 | +48.5% | +666.0088 to +1933.7934 | yes: LOSS |
| time over the response line (% of samples) | 17.55 | 21.85 | +24.5% | +2.5130 to +6.0840 | yes: LOSS |
| failed requests (%) | 0.007752 | 0.1571 | +1926.7% | −0.1499 to +0.4486 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 13.4 | +19.6% | −0.0820 to +4.4820 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.7 | +89.700 (native is 0) | +19.4006 to +159.9994 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 38.1 | 33.08 | −13.2% | −21.1185 to +11.0852 | no |
| utilisation (used / allocatable) | 0.03138 | 0.04168 | +32.9% | +0.0056 to +0.0150 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 1.591 | +5.6% | +0.0101 to +0.1599 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03795 | +0.038 (native is 0) | +0.0299 to +0.0460 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.629 | +8.2% | +0.0407 to +0.2051 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 844.9 | 682.3 | −19.2% | −231.0066 to −94.2603 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.07 | 5.223 | +28.3% | +0.1123 to +2.1929 | yes: power given |
| pods started | 0.3 | 2.8 | +833.3% | +1.0995 to +3.9005 | yes: power given |
| pod start wait, total (s) | 0.5 | 8.5 | +1600.0% | +2.5524 to +13.4476 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 2.177 | +521.9% | +0.7178 to +2.9355 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.02 | 58.17 | +11.8% | +4.5687 to +7.7170 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 879.4 | 942.1 | +7.1% | +31.0517 to +94.3483 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.741 | −35.5% | −6.5906 to −1.9266 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.658 | 5.888 | +4.1% | −0.3503 to +0.8087 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 31.3 | 34.2 | +9.3% | −3.1644 to +8.9644 | no |
| queue: job turnaround, submitted to done, mean (s) | 188.3 | 245.2 | +30.2% | +27.9277 to +85.6890 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.027 | 5.033 | +0.1% | −0.0044 to +0.0151 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 524 | +0.0% | −2.3528 to +2.8120 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 524 | +0.0% | −2.3528 to +2.8120 | no |
| response time (ms), mean | 418.4 | 464 | +10.9% | +24.8366 to +66.4763 | yes: LOSS |
| response time (ms), 95th percentile | 1514 | 1796 | +18.6% | +145.5391 to +417.3689 | yes: LOSS |
| response time (ms), 99th percentile | 2095 | 2679 | +27.9% | +152.1461 to +1016.7067 | yes: LOSS |
| time over the response line (% of samples) | 15.62 | 17.55 | +12.3% | −1.3368 to +5.1942 | no |
| failed requests (%) | 0 | 0.007752 | +0.008 (native is 0) | −0.0098 to +0.0253 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 11.2 | +19.1% | +0.5028 to +3.0972 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.96 | 38.1 | +194.0% | −16.1036 to +66.3769 | no |
| utilisation (used / allocatable) | 0.03191 | 0.03138 | −1.7% | −0.0033 to +0.0022 | no |
| CPU used (cores), mean | 1.532 | 1.506 | −1.7% | −0.1583 to +0.1068 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.532 | 1.506 | −1.7% | −0.1583 to +0.1068 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.6 | 844.9 | −0.3% | −59.9130 to +54.4165 | no |
| HPA replicas, mean | 4.024 | 4.07 | +1.2% | −0.2073 to +0.3001 | no |
| pods started | 0.3 | 0.3 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.7 | 0.5 | −28.6% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.7 | 0.35 | −50.0% | −0.8845 to +0.1845 | no |
| host CPU busy, the real machine under kind (%) | 47.28 | 52.02 | +10.0% | +3.3605 to +6.1320 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.8 | 879.4 | +8.3% | +24.6879 to +110.5121 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 5.658 | +6690.0% | −3.6025 to +14.7525 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 31.3 | +6160.0% | −37.3633 to +98.9633 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.3 | 188.3 | +54.0% | +24.8982 to +107.1268 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.75 | −18.8% | −3.9900 to −0.5102 | yes: GAIN |
| node-hours | 5.027 | 4.086 | −18.7% | −1.6725 to −0.2110 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 524.5 | +0.1% | −0.6882 to +2.1295 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 453.9 | −13.3% | −125.0847 to −14.6864 | yes: GAIN |
| response time (ms), mean | 418.4 | 467.1 | +11.7% | −12.4580 to +109.9755 | no |
| response time (ms), 95th percentile | 1514 | 1924 | +27.1% | +34.6846 to +785.8314 | yes: LOSS |
| response time (ms), 99th percentile | 2095 | 2532 | +20.9% | +45.5998 to +828.0542 | yes: LOSS |
| time over the response line (% of samples) | 15.62 | 19.13 | +22.5% | +0.8767 to +6.1396 | yes: LOSS |
| failed requests (%) | 0 | 0.02372 | +0.024 (native is 0) | −0.0299 to +0.0774 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 10.7 | +13.8% | −0.0081 to +2.6081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 219 | +219.000 (native is 0) | +97.1544 to +340.8456 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.96 | 12.44 | −4.0% | −3.1543 to +2.1210 | no |
| utilisation (used / allocatable) | 0.03191 | 0.04087 | +28.1% | +0.0026 to +0.0154 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.562 | +2.0% | −0.0166 to +0.0770 | no |
| Omni's own CPU (cores), mean | 0 | 0.05213 | +0.052 (native is 0) | +0.0464 to +0.0579 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.614 | +5.4% | +0.0326 to +0.1320 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.6 | 702.1 | −17.2% | −255.3099 to −35.6965 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.024 | 4.525 | +12.4% | +0.2249 to +0.7769 | yes: power given |
| pods started | 0.3 | 1.9 | +533.3% | +0.5772 to +2.6228 | yes: power given |
| pod start wait, total (s) | 0.7 | 4.4 | +528.6% | +0.9389 to +6.4611 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 1.6 | +128.6% | +0.0186 to +1.7814 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.28 | 52.31 | +10.6% | +3.8406 to +6.2228 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.8 | 839.5 | +3.4% | +5.3580 to +50.0420 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.4 | −30.0% | −5.9980 to −1.2013 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.07917 | −5.0% | −0.0594 to +0.0511 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.5840 to +0.5840 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.3 | 146.1 | +19.4% | +7.6786 to +39.8881 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.75 | −18.8% | −3.9900 to −0.5102 | yes: GAIN |
| node-hours | 5.033 | 4.086 | −18.8% | −1.6810 to −0.2132 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 524.5 | +0.1% | −2.3543 to +3.3364 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 453.9 | −13.4% | −126.3979 to −13.8325 | yes: GAIN |
| response time (ms), mean | 464 | 467.1 | +0.7% | −44.3967 to +50.6013 | no |
| response time (ms), 95th percentile | 1796 | 1924 | +7.2% | −188.1834 to +445.7914 | no |
| response time (ms), 99th percentile | 2679 | 2532 | −5.5% | −632.0186 to +336.8198 | no |
| time over the response line (% of samples) | 17.55 | 19.13 | +9.0% | −1.8258 to +4.9847 | no |
| failed requests (%) | 0.007752 | 0.02372 | +205.9% | −0.0423 to +0.0742 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 10.7 | −4.5% | −2.0906 to +1.0906 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 219 | +219.000 (native is 0) | +97.1544 to +340.8456 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 38.1 | 12.44 | −67.3% | −66.0617 to +14.7551 | no |
| utilisation (used / allocatable) | 0.03138 | 0.04087 | +30.3% | +0.0035 to +0.0155 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 1.562 | +3.7% | −0.0949 to +0.2068 | no |
| Omni's own CPU (cores), mean | 0 | 0.05213 | +0.052 (native is 0) | +0.0464 to +0.0579 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.614 | +7.2% | −0.0468 to +0.2630 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 844.9 | 702.1 | −16.9% | −234.2283 to −51.2817 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.07 | 4.525 | +11.2% | +0.1798 to +0.7292 | yes: power given |
| pods started | 0.3 | 1.9 | +533.3% | +0.4715 to +2.7285 | yes: power given |
| pod start wait, total (s) | 0.5 | 4.4 | +780.0% | +1.0497 to +6.7503 | yes: LOSS |
| pod start wait, mean (s) | 0.35 | 1.6 | +357.1% | +0.4692 to +2.0308 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.02 | 52.31 | +0.5% | −0.3500 to +0.9208 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 879.4 | 839.5 | −4.5% | −62.8356 to −16.9644 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.4 | −30.0% | −5.9980 to −1.2013 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 5.658 | 0.07917 | −98.6% | −14.7452 to +3.5869 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 31.3 | 0.5 | −98.4% | −98.9633 to +37.3633 | no |
| queue: job turnaround, submitted to done, mean (s) | 188.3 | 146.1 | −22.4% | −69.2270 to −15.2313 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.66 | −19.5% | −3.8811 to −0.7987 | yes: GAIN |
| node-hours | 5.027 | 4.048 | −19.5% | −1.6272 to −0.3309 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.8 | 525.1 | +0.2% | −1.2270 to +3.8375 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.8 | 451.6 | −13.8% | −120.8235 to −23.5244 | yes: GAIN |
| response time (ms), mean | 418.4 | 588.2 | +40.6% | +57.1493 to +282.5456 | yes: LOSS |
| response time (ms), 95th percentile | 1514 | 2691 | +77.7% | +463.3669 to +1889.7001 | yes: LOSS |
| response time (ms), 99th percentile | 2095 | 3979 | +89.9% | +950.4191 to +2818.2359 | yes: LOSS |
| time over the response line (% of samples) | 15.62 | 21.85 | +39.9% | +2.0750 to +10.3795 | yes: LOSS |
| failed requests (%) | 0 | 0.1571 | +0.157 (native is 0) | −0.1595 to +0.4737 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.4 | 13.4 | +42.6% | +1.4320 to +6.5680 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.7 | +89.700 (native is 0) | +19.4006 to +159.9994 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.96 | 33.08 | +155.2% | −5.8191 to +46.0591 | no |
| utilisation (used / allocatable) | 0.03191 | 0.04168 | +30.6% | +0.0035 to +0.0160 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.532 | 1.591 | +3.9% | −0.0512 to +0.1696 | no |
| Omni's own CPU (cores), mean | 0 | 0.03795 | +0.038 (native is 0) | +0.0299 to +0.0460 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.532 | 1.629 | +6.3% | −0.0115 to +0.2058 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 847.6 | 682.3 | −19.5% | −272.5935 to −58.1697 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.024 | 5.223 | +29.8% | +0.0395 to +2.3585 | yes: power given |
| pods started | 0.3 | 2.8 | +833.3% | +1.2271 to +3.7729 | yes: power given |
| pod start wait, total (s) | 0.7 | 8.5 | +1114.3% | +2.5242 to +13.0758 | yes: LOSS |
| pod start wait, mean (s) | 0.7 | 2.177 | +211.0% | +0.2820 to +2.6713 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.28 | 58.17 | +23.0% | +8.1721 to +13.6062 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 811.8 | 942.1 | +16.1% | +61.7282 to +198.8718 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.741 | −35.5% | −6.5906 to −1.9266 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 5.887 | +6965.0% | −3.8198 to +15.4281 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 34.2 | +6740.0% | −40.5214 to +107.9214 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.3 | 245.2 | +100.4% | +59.4417 to +186.2000 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*