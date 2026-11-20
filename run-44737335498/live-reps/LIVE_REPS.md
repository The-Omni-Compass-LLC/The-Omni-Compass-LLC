# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.96 | 10.98 |
| node-hours | 5.03 | 5.028 | 4.597 | 4.603 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 526.3 | 527.5 | 527.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 526.3 | 494.8 | 495.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 582.7 | 786.2 | 713.7 | 939.9 |
| response time (ms), 95th percentile | 2254 | 3324 | 2968 | 4053 |
| response time (ms), 99th percentile | 2962 | 4820 | 3987 | 5625 |
| time over the response line (% of samples) | 22.65 | 27.23 | 28.35 | 32.99 |
| failed requests (%) | 0 | 0.03275 | 0.0857 | 0.2334 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 16.5 | 15.2 | 17.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 149.9 | 50.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 20.83 | 40.12 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.08 | 42.27 | 20.46 | 45.24 |
| utilisation (used / allocatable) | 0.03509 | 0.03535 | 0.03969 | 0.04059 |
| CPU used (cores), mean | 1.685 | 1.697 | 1.739 | 1.769 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0563 | 0.04565 |
| CPU used with Omni's own (cores), mean | 1.685 | 1.697 | 1.795 | 1.815 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.6 | 745.8 | 687 | 671.1 |
| HPA replicas, mean | 3.972 | 4.288 | 4.762 | 4.699 |
| pods started | 0 | 0.5 | 3.3 | 2.9 |
| pod start wait, total (s) | 0 | 1 | 9.1 | 8.9 |
| pod start wait, mean (s) | 0 | 0.8 | 2.058 | 2.331 |
| host CPU busy, the real machine under kind (%) | 52.18 | 59.47 | 58.49 | 65.81 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 865.6 | 996.2 | 922 | 1065 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.842 | 9.92 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 3.15 | 0.175 | 16.88 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.8 | 0.9 | 130 |
| queue: job turnaround, submitted to done, mean (s) | 175.1 | 303 | 225.7 | 364.1 |
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
| worker nodes in service, mean | 12 | 10.98 | −8.5% | −2.1316 to +0.0965 | no |
| node-hours | 5.028 | 4.603 | −8.5% | −0.8901 to +0.0401 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.3 | 527.8 | +0.3% | −0.7005 to +3.5825 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.3 | 495.8 | −5.8% | −65.8546 to +4.8408 | no |
| response time (ms), mean | 786.2 | 939.9 | +19.6% | −14.0681 to +321.5781 | no |
| response time (ms), 95th percentile | 3324 | 4053 | +21.9% | +180.7878 to +1277.2522 | yes: LOSS |
| response time (ms), 99th percentile | 4820 | 5625 | +16.7% | +137.9232 to +1472.9402 | yes: LOSS |
| time over the response line (% of samples) | 27.23 | 32.99 | +21.2% | +1.8094 to +9.7102 | yes: LOSS |
| failed requests (%) | 0.03275 | 0.2334 | +612.8% | −0.0753 to +0.4767 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.5 | 17.8 | +7.9% | +0.7111 to +1.8889 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.100 (native is 0) | +40.7343 to +59.4657 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 42.27 | 45.24 | +7.0% | −24.3042 to +30.2442 | no |
| utilisation (used / allocatable) | 0.03535 | 0.04059 | +14.8% | +0.0013 to +0.0092 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.697 | 1.769 | +4.3% | −0.0370 to +0.1818 | no |
| Omni's own CPU (cores), mean | 0 | 0.04565 | +0.046 (native is 0) | +0.0379 to +0.0534 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.697 | 1.815 | +7.0% | +0.0052 to +0.2308 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 671.1 | −10.0% | −123.2937 to −26.1159 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.288 | 4.699 | +9.6% | −0.1333 to +0.9548 | no |
| pods started | 0.5 | 2.9 | +480.0% | +0.4571 to +4.3429 | yes: power given |
| pod start wait, total (s) | 1 | 8.9 | +790.0% | +1.1270 to +14.6730 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 2.331 | +191.3% | +0.6357 to +2.4254 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.47 | 65.81 | +10.7% | +4.5566 to +8.1244 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 996.2 | 1065 | +6.9% | +33.2854 to +104.3146 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.92 | −17.3% | −4.1241 to −0.0352 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.15 | 16.88 | +436.0% | +0.8936 to +26.5731 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 130 | +7122.2% | +10.3376 to +246.0624 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 303 | 364.1 | +20.2% | +27.1355 to +95.0311 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.03 | 5.028 | −0.0% | −0.0157 to +0.0124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 526.3 | +0.0% | −1.3751 to +1.7508 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 526.3 | +0.0% | −1.3751 to +1.7508 | no |
| response time (ms), mean | 582.7 | 786.2 | +34.9% | +85.9305 to +320.9787 | yes: LOSS |
| response time (ms), 95th percentile | 2254 | 3324 | +47.4% | +556.8128 to +1581.4162 | yes: LOSS |
| response time (ms), 99th percentile | 2962 | 4820 | +62.7% | +1287.9559 to +2426.7085 | yes: LOSS |
| time over the response line (% of samples) | 22.65 | 27.23 | +20.2% | +1.6152 to +7.5357 | yes: LOSS |
| failed requests (%) | 0 | 0.03275 | +0.033 (native is 0) | −0.0075 to +0.0730 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 16.5 | +27.9% | +1.4620 to +5.7380 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.08 | 42.27 | +180.4% | +0.4103 to +53.9697 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03509 | 0.03535 | +0.7% | −0.0022 to +0.0028 | no |
| CPU used (cores), mean | 1.685 | 1.697 | +0.7% | −0.1079 to +0.1328 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.685 | 1.697 | +0.7% | −0.1079 to +0.1328 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.6 | 745.8 | −1.7% | −58.4196 to +32.7062 | no |
| HPA replicas, mean | 3.972 | 4.288 | +8.0% | +0.1453 to +0.4882 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.0058 to +1.0058 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −0.0116 to +2.0116 | no |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.18 | 59.47 | +14.0% | +5.8781 to +8.6977 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.6 | 996.2 | +15.1% | +86.2622 to +174.9378 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 3.15 | +2600.0% | −0.9225 to +6.9891 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1.8 | +200.0% | +0.6358 to +1.7642 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 175.1 | 303 | +73.0% | +86.4890 to +169.2694 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.96 | −8.7% | −1.9463 to −0.1356 | yes: GAIN |
| node-hours | 5.03 | 4.597 | −8.6% | −0.8158 to −0.0492 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 527.5 | +0.3% | −0.5274 to +3.3172 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 494.8 | −6.0% | −60.2610 to −2.4200 | yes: GAIN |
| response time (ms), mean | 582.7 | 713.7 | +22.5% | +35.1961 to +226.7309 | yes: LOSS |
| response time (ms), 95th percentile | 2254 | 2968 | +31.6% | +305.0142 to +1121.6888 | yes: LOSS |
| response time (ms), 99th percentile | 2962 | 3987 | +34.6% | +520.6915 to +1528.5923 | yes: LOSS |
| time over the response line (% of samples) | 22.65 | 28.35 | +25.1% | +3.6640 to +7.7283 | yes: LOSS |
| failed requests (%) | 0 | 0.0857 | +0.086 (native is 0) | −0.0733 to +0.2447 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 15.2 | +17.8% | +0.4515 to +4.1485 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 149.9 | +149.900 (native is 0) | +34.6107 to +265.1893 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.08 | 20.46 | +35.7% | −0.0464 to +10.8164 | no |
| utilisation (used / allocatable) | 0.03509 | 0.03969 | +13.1% | +0.0016 to +0.0076 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.685 | 1.739 | +3.2% | +0.0091 to +0.0999 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0563 | +0.056 (native is 0) | +0.0507 to +0.0619 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.685 | 1.795 | +6.6% | +0.0637 to +0.1578 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.6 | 687 | −9.4% | −113.9414 to −29.3703 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.972 | 4.762 | +19.9% | +0.3900 to +1.1904 | yes: power given |
| pods started | 0 | 3.3 | +3.300 (native is 0) | +1.6811 to +4.9189 | yes: power given |
| pod start wait, total (s) | 0 | 9.1 | +9.100 (native is 0) | +3.7424 to +14.4576 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.058 | +2.058 (native is 0) | +1.1287 to +2.9880 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.18 | 58.49 | +12.1% | +4.8815 to +7.7239 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.6 | 922 | +6.5% | +26.1794 to +86.6206 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.842 | −18.0% | −3.9925 to −0.3239 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 0.175 | +50.0% | −0.0432 to +0.1598 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 175.1 | 225.7 | +28.9% | +27.5090 to +73.6910 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.96 | −8.7% | −1.9463 to −0.1356 | yes: GAIN |
| node-hours | 5.028 | 4.597 | −8.6% | −0.8072 to −0.0544 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.3 | 527.5 | +0.2% | −0.7081 to +3.1222 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.3 | 494.8 | −6.0% | −60.6440 to −2.4128 | yes: GAIN |
| response time (ms), mean | 786.2 | 713.7 | −9.2% | −148.0580 to +3.0759 | no |
| response time (ms), 95th percentile | 3324 | 2968 | −10.7% | −746.7931 to +35.2671 | no |
| response time (ms), 99th percentile | 4820 | 3987 | −17.3% | −1258.9391 to −406.4415 | yes: GAIN |
| time over the response line (% of samples) | 27.23 | 28.35 | +4.1% | −2.7513 to +4.9926 | no |
| failed requests (%) | 0.03275 | 0.0857 | +161.7% | −0.0736 to +0.1795 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.5 | 15.2 | −7.9% | −1.6455 to −0.9545 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 149.9 | +149.900 (native is 0) | +34.6107 to +265.1893 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 42.27 | 20.46 | −51.6% | −44.8478 to +1.2378 | no |
| utilisation (used / allocatable) | 0.03535 | 0.03969 | +12.3% | +0.0018 to +0.0069 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.697 | 1.739 | +2.5% | −0.0826 to +0.1666 | no |
| Omni's own CPU (cores), mean | 0 | 0.0563 | +0.056 (native is 0) | +0.0507 to +0.0619 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.697 | 1.795 | +5.8% | −0.0304 to +0.2271 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 745.8 | 687 | −7.9% | −93.5794 to −24.0189 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.288 | 4.762 | +11.0% | +0.0854 to +0.8616 | yes: power given |
| pods started | 0.5 | 3.3 | +560.0% | +1.0872 to +4.5128 | yes: power given |
| pod start wait, total (s) | 1 | 9.1 | +810.0% | +2.4732 to +13.7268 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 2.058 | +157.3% | −0.1266 to +2.6432 | no |
| host CPU busy, the real machine under kind (%) | 59.47 | 58.49 | −1.7% | −1.8320 to −0.1384 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 996.2 | 922 | −7.4% | −95.2629 to −53.1371 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.842 | −18.0% | −3.9925 to −0.3239 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 3.15 | 0.175 | −94.4% | −6.9607 to +1.0107 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.8 | 0.9 | −50.0% | −1.6113 to −0.1887 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 303 | 225.7 | −25.5% | −100.7796 to −53.7787 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.98 | −8.5% | −2.1316 to +0.0965 | no |
| node-hours | 5.03 | 4.603 | −8.5% | −0.9001 to +0.0468 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.1 | 527.8 | +0.3% | −0.3385 to +3.5963 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.1 | 495.8 | −5.8% | −65.9930 to +5.3550 | no |
| response time (ms), mean | 582.7 | 939.9 | +61.3% | +159.5493 to +554.8699 | yes: LOSS |
| response time (ms), 95th percentile | 2254 | 4053 | +79.8% | +1121.5160 to +2474.7530 | yes: LOSS |
| response time (ms), 99th percentile | 2962 | 5625 | +89.9% | +1904.4194 to +3421.1084 | yes: LOSS |
| time over the response line (% of samples) | 22.65 | 32.99 | +45.6% | +5.2958 to +15.3747 | yes: LOSS |
| failed requests (%) | 0 | 0.2334 | +0.233 (native is 0) | −0.0760 to +0.5428 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 17.8 | +38.0% | +2.9791 to +6.8209 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.1 | +50.100 (native is 0) | +40.7343 to +59.4657 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.08 | 45.24 | +200.1% | +6.3889 to +53.9311 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03509 | 0.04059 | +15.7% | +0.0009 to +0.0101 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.685 | 1.769 | +5.0% | −0.0022 to +0.1718 | no |
| Omni's own CPU (cores), mean | 0 | 0.04565 | +0.046 (native is 0) | +0.0379 to +0.0534 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.685 | 1.815 | +7.7% | +0.0465 to +0.2145 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.6 | 671.1 | −11.5% | −150.4615 to −24.6616 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.972 | 4.699 | +18.3% | +0.2426 to +1.2123 | yes: power given |
| pods started | 0 | 2.9 | +2.900 (native is 0) | +1.0393 to +4.7607 | yes: power given |
| pod start wait, total (s) | 0 | 8.9 | +8.900 (native is 0) | +2.2455 to +15.5545 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.331 | +2.331 (native is 0) | +1.3809 to +3.2802 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.18 | 65.81 | +26.1% | +11.2669 to +15.9899 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 865.6 | 1065 | +23.0% | +133.6867 to +265.1133 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.92 | −17.3% | −4.1241 to −0.0352 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1167 | 16.88 | +14371.4% | +1.7313 to +31.8020 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 130 | +21566.7% | +11.1916 to +247.6084 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 175.1 | 364.1 | +107.9% | +123.3741 to +254.5509 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*