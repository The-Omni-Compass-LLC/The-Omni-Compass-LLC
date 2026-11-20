# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.967 | 6.141 |
| node-hours | 5.035 | 5.035 | 4.179 | 2.575 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 505.3 | 525.8 | 505.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 505.3 | 461.8 | 320.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 541.4 | 111.7 | 582.6 | 66.54 |
| response time (ms), 95th percentile | 2038 | 153.9 | 2410 | 84.6 |
| response time (ms), 99th percentile | 2700 | 177.7 | 3245 | 110.1 |
| time over the response line (% of samples) | 20.62 | 0 | 23.39 | 0 |
| failed requests (%) | 0 | 0 | 0.008386 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.89 | 0 | 11.56 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 219.8 | 32.38 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 29 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.44 | 0 | 20.89 | 0.1 |
| utilisation (used / allocatable) | 0.0341 | 0.005742 | 0.04087 | 0.00929 |
| CPU used (cores), mean | 1.637 | 0.2756 | 1.609 | 0.2285 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05587 | 0.03023 |
| CPU used with Omni's own (cores), mean | 1.637 | 0.2756 | 1.665 | 0.2587 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.8 | 4530 | 690.3 | 3493 |
| HPA replicas, mean | 4.016 | 4.234 | 4.596 | 4.408 |
| pods started | 0 | 0.375 | 2.778 | 2.125 |
| pod start wait, total (s) | 0 | 0.5 | 6.111 | 3.625 |
| pod start wait, mean (s) | 0 | 0.3125 | 1.969 | 1.24 |
| host CPU busy, the real machine under kind (%) | 49.8 | 14.52 | 55.45 | 17.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 853.9 | 1508 | 891 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.508 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1065 | 1162 | 0.1157 | 1160 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7778 | 1478 | 0.8889 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 163.4 | 1162 | 194.6 | 1160 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 8 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.141 | −48.8% | −5.9054 to −5.8127 | yes: GAIN |
| node-hours | 5.035 | 2.575 | −48.9% | −2.4854 to −2.4335 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 505.3 | 505.1 | −0.0% | −2.2514 to +1.8775 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.3 | 320.8 | −36.5% | −186.7504 to −182.1652 | yes: GAIN |
| response time (ms), mean | 111.7 | 66.54 | −40.4% | −60.9314 to −29.4272 | yes: GAIN |
| response time (ms), 95th percentile | 153.9 | 84.6 | −45.0% | −88.1340 to −50.5197 | yes: GAIN |
| response time (ms), 99th percentile | 177.7 | 110.1 | −38.1% | −86.7971 to −48.4284 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.38 | +32.375 (native is 0) | +30.4821 to +34.2679 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1 | +0.100 (native is 0) | −0.0659 to +0.2659 | no |
| utilisation (used / allocatable) | 0.005742 | 0.00929 | +61.8% | +0.0029 to +0.0042 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2756 | 0.2285 | −17.1% | −0.0539 to −0.0404 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03023 | +0.030 (native is 0) | +0.0253 to +0.0351 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2756 | 0.2587 | −6.1% | −0.0226 to −0.0112 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4530 | 3493 | −22.9% | −1193.9309 to −880.4847 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.234 | 4.408 | +4.1% | −0.1321 to +0.4809 | no |
| pods started | 0.375 | 2.125 | +466.7% | +0.1541 to +3.3459 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.625 | +625.0% | +0.3182 to +5.9318 | yes: LOSS |
| pod start wait, mean (s) | 0.3125 | 1.24 | +296.7% | −0.0452 to +1.8993 | no |
| host CPU busy, the real machine under kind (%) | 14.52 | 17.29 | +19.1% | +2.2054 to +3.3397 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 1507 | −0.1% | −7.9275 to +5.1775 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1162 | 1160 | −0.1% | −7.8890 to +5.1078 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1478 | 1477 | −0.1% | −7.6789 to +4.9289 | no |
| queue: job turnaround, submitted to done, mean (s) | 1162 | 1160 | −0.1% | −7.8890 to +5.1078 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 8 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.038 | 5.035 | −0.1% | −0.0221 to +0.0146 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 505.3 | −4.1% | −26.6851 to −16.2392 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 505.3 | −4.1% | −26.6851 to −16.2392 | yes: GAIN |
| response time (ms), mean | 576.4 | 111.7 | −80.6% | −840.7147 to −88.6927 | yes: GAIN |
| response time (ms), 95th percentile | 2197 | 153.9 | −93.0% | −3700.3859 to −384.8016 | yes: GAIN |
| response time (ms), 99th percentile | 2908 | 177.7 | −93.9% | −4868.0974 to −591.5713 | yes: GAIN |
| time over the response line (% of samples) | 21.43 | 0 | −100.0% | −36.3937 to −6.4621 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.62 | 0 | −100.0% | −17.1470 to −4.1030 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.52 | 0 | −100.0% | −21.2505 to −7.7912 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03447 | 0.005742 | −83.3% | −0.0332 to −0.0243 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.654 | 0.2756 | −83.3% | −1.5913 to −1.1661 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.654 | 0.2756 | −83.3% | −1.5913 to −1.1661 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.8 | 4530 | +480.9% | +3065.3267 to +4434.9948 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.023 | 4.234 | +5.2% | +0.0724 to +0.3488 | yes: power given |
| pods started | 0 | 0.375 | +0.375 (native is 0) | −0.2471 to +0.9971 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.3939 to +1.3939 | no |
| pod start wait, mean (s) | 0 | 0.3125 | +0.312 (native is 0) | −0.1841 to +0.8091 | no |
| host CPU busy, the real machine under kind (%) | 50.3 | 14.52 | −71.1% | −42.0131 to −29.5466 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 867.2 | 1508 | +73.9% | +510.2764 to +771.9736 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1094 | 1162 | +1062123.8% | +1157.7542 to +1165.6416 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.75 | 1478 | +196966.7% | +1473.5441 to +1480.9559 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 175.8 | 1162 | +560.9% | +855.4030 to +1116.6179 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.967 | −16.9% | −3.7992 to −0.2661 | yes: GAIN |
| node-hours | 5.035 | 4.179 | −17.0% | −1.5880 to −0.1234 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 525.8 | −0.1% | −2.2321 to +1.6681 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 461.8 | −12.2% | −119.1555 to −9.3714 | yes: GAIN |
| response time (ms), mean | 541.4 | 582.6 | +7.6% | −18.8176 to +101.2947 | no |
| response time (ms), 95th percentile | 2038 | 2410 | +18.2% | +76.3291 to +665.8098 | yes: LOSS |
| response time (ms), 99th percentile | 2700 | 3245 | +20.2% | +88.3419 to +1002.4708 | yes: LOSS |
| time over the response line (% of samples) | 20.62 | 23.39 | +13.4% | −0.0801 to +5.6149 | no |
| failed requests (%) | 0 | 0.008386 | +0.008 (native is 0) | −0.0110 to +0.0277 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.89 | 11.56 | +6.1% | +0.2823 to +1.0510 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 219.8 | +219.778 (native is 0) | +75.1143 to +364.4413 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.44 | 20.89 | +55.5% | −1.1686 to +16.0798 | no |
| utilisation (used / allocatable) | 0.0341 | 0.04087 | +19.8% | +0.0008 to +0.0127 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.637 | 1.609 | −1.7% | −0.1061 to +0.0495 | no |
| Omni's own CPU (cores), mean | 0 | 0.05587 | +0.056 (native is 0) | +0.0505 to +0.0612 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.637 | 1.665 | +1.7% | −0.0518 to +0.1070 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 785.8 | 690.3 | −12.2% | −176.3797 to −14.7098 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.016 | 4.596 | +14.5% | +0.2140 to +0.9467 | yes: power given |
| pods started | 0 | 2.778 | +2.778 (native is 0) | +1.4039 to +4.1516 | yes: power given |
| pod start wait, total (s) | 0 | 6.111 | +6.111 (native is 0) | +3.2236 to +8.9986 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.969 | +1.969 (native is 0) | +1.3419 to +2.5951 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.8 | 55.45 | +11.3% | +4.5848 to +6.7086 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 853.9 | 891 | +4.3% | +13.3276 to +60.8946 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.508 | −29.1% | −6.0996 to −0.8834 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1065 | 0.1157 | +8.7% | −0.0502 to +0.0687 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7778 | 0.8889 | +14.3% | −0.1451 to +0.3673 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.4 | 194.6 | +19.1% | +10.1591 to +52.2297 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 8 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.838 | −18.0% | −4.1869 to −0.1374 | yes: GAIN |
| node-hours | 5.035 | 4.123 | −18.1% | −1.7619 to −0.0603 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 505.3 | 525.8 | +4.1% | +16.3114 to +24.7947 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.3 | 457.8 | −9.4% | −114.6472 to +19.6492 | no |
| response time (ms), mean | 111.7 | 615.7 | +451.1% | +99.4300 to +908.5018 | yes: LOSS |
| response time (ms), 95th percentile | 153.9 | 2570 | +1569.5% | +539.1121 to +4292.6579 | yes: LOSS |
| response time (ms), 99th percentile | 177.7 | 3464 | +1849.3% | +803.8801 to +5768.3299 | yes: LOSS |
| time over the response line (% of samples) | 0 | 23.29 | +23.292 (native is 0) | +7.4406 to +39.1432 | yes: LOSS |
| failed requests (%) | 0 | 0.009434 | +0.009 (native is 0) | −0.0129 to +0.0317 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.38 | +11.375 (native is 0) | +4.8073 to +17.9427 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 233 | +233.000 (native is 0) | +68.5493 to +397.4507 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 22.36 | +22.363 (native is 0) | +7.9339 to +36.7911 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005742 | 0.04161 | +624.6% | +0.0322 to +0.0395 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2756 | 1.618 | +486.9% | +1.0930 to +1.5908 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05694 | +0.057 (native is 0) | +0.0514 to +0.0625 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2756 | 1.674 | +507.5% | +1.1455 to +1.6522 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4530 | 680.9 | −85.0% | −4624.3572 to −3073.7600 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.234 | 4.684 | +10.6% | +0.1123 to +0.7890 | yes: power given |
| pods started | 0.375 | 3 | +700.0% | +1.0808 to +4.1692 | yes: power given |
| pod start wait, total (s) | 0.5 | 6.625 | +1225.0% | +3.0467 to +9.2033 | yes: LOSS |
| pod start wait, mean (s) | 0.3125 | 1.965 | +528.7% | +0.5754 to +2.7288 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.52 | 55.88 | +284.9% | +34.3476 to +48.3796 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 904.1 | −40.1% | −758.0943 to −450.4057 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1162 | 0.1198 | −100.0% | −1165.6085 to −1157.7665 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1478 | 0.875 | −99.9% | −1480.8493 to −1473.4007 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1162 | 206.7 | −82.2% | −1105.3246 to −804.9879 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 8 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.141 | −48.8% | −5.9054 to −5.8127 | yes: GAIN |
| node-hours | 5.038 | 2.575 | −48.9% | −2.4749 to −2.4515 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 505.1 | −4.1% | −26.2847 to −17.0135 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 320.8 | −39.1% | −209.3828 to −202.4571 | yes: GAIN |
| response time (ms), mean | 576.4 | 66.54 | −88.5% | −900.3397 to −119.4262 | yes: GAIN |
| response time (ms), 95th percentile | 2197 | 84.6 | −96.1% | −3785.2444 to −438.5969 | yes: GAIN |
| response time (ms), 99th percentile | 2908 | 110.1 | −96.2% | −4952.3144 to −642.5799 | yes: GAIN |
| time over the response line (% of samples) | 21.43 | 0 | −100.0% | −36.3937 to −6.4621 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.62 | 0 | −100.0% | −17.1470 to −4.1030 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.38 | +32.375 (native is 0) | +30.4821 to +34.2679 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.52 | 0.1 | −99.3% | −21.1315 to −7.7102 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03447 | 0.00929 | −73.0% | −0.0289 to −0.0214 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.654 | 0.2285 | −86.2% | −1.6412 to −1.2104 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03023 | +0.030 (native is 0) | +0.0253 to +0.0351 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.654 | 0.2587 | −84.4% | −1.6063 to −1.1849 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.8 | 3493 | +347.9% | +2172.3013 to +3253.6045 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.023 | 4.408 | +9.6% | +0.1214 to +0.6486 | yes: power given |
| pods started | 0 | 2.125 | +2.125 (native is 0) | +0.9061 to +3.3439 | yes: power given |
| pod start wait, total (s) | 0 | 3.625 | +3.625 (native is 0) | +1.3053 to +5.9447 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.24 | +1.240 (native is 0) | +0.5473 to +1.9318 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.3 | 17.29 | −65.6% | −38.8234 to −27.1912 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 867.2 | 1507 | +73.8% | +510.9344 to +768.5656 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1094 | 1160 | +1060852.4% | +1156.9147 to +1163.6999 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.75 | 1477 | +196783.3% | +1472.2873 to +1479.4627 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 175.8 | 1160 | +560.1% | +855.7214 to +1113.5182 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*