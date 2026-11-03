# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.008 | 5.995 |
| node-hours | 2.517 | 2.518 | 2.099 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 287.2 | 273.7 | 286.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 287.2 | 242.5 | 286.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 407.6 | 692.2 | 383.2 | 681.3 |
| response time (ms), 95th percentile | 1477 | 1402 | 1542 | 1373 |
| response time (ms), 99th percentile | 2068 | 1841 | 2149 | 1832 |
| time over the response line (% of samples) | 17.69 | 62.12 | 17.96 | 60.83 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 24.4 | 10.5 | 24.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 124.7 | 31.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 12.5 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.63 | 2.3 | 14.55 | 2.552 |
| utilisation (used / allocatable) | 0.06344 | 0.09847 | 0.07641 | 0.0976 |
| CPU used (cores), mean | 1.523 | 2.363 | 1.518 | 2.341 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07224 | 0.04193 |
| CPU used with Omni's own (cores), mean | 1.523 | 2.363 | 1.59 | 2.383 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438 | 290.4 | 384.4 | 292.5 |
| HPA replicas, mean | 2.027 | 2.009 | 2.464 | 2.771 |
| pods started | 0.1 | 0.1 | 1.6 | 1.3 |
| pod start wait, total (s) | 0.2 | 0.2 | 3.9 | 4.2 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.817 | 1.658 |
| host CPU busy, the real machine under kind (%) | 43.18 | 75.76 | 46.39 | 76.97 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806 | 1476 | 811.6 | 1476 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.189 | 5.773 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 638.5 | 0.1667 | 676.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1235 | 0.6 | 1247 |
| queue: job turnaround, submitted to done, mean (s) | 111.6 | 946.7 | 116.2 | 968.9 |
| queue: jobs unfinished at the window's end | 0 | 14.2 | 0 | 15.6 |
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
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0172 to +0.0067 | no |
| node-hours | 2.518 | 2.513 | −0.2% | −0.0126 to +0.0015 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 287.2 | 286.5 | −0.2% | −1.6440 to +0.2548 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.2 | 286.4 | −0.3% | −1.6556 to −0.0669 | yes: GAIN |
| response time (ms), mean | 692.2 | 681.3 | −1.6% | −42.9076 to +21.0375 | no |
| response time (ms), 95th percentile | 1402 | 1373 | −2.1% | −84.9936 to +27.0046 | no |
| response time (ms), 99th percentile | 1841 | 1832 | −0.5% | −168.8603 to +150.9135 | no |
| time over the response line (% of samples) | 62.12 | 60.83 | −2.1% | −2.9272 to +0.3619 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.4 | 24.3 | −0.4% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.1 | +31.100 (native is 0) | +27.3534 to +34.8466 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.3 | 2.552 | +10.9% | −0.1122 to +0.6156 | no |
| utilisation (used / allocatable) | 0.09847 | 0.0976 | −0.9% | −0.0016 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.363 | 2.341 | −1.0% | −0.0372 to −0.0078 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04193 | +0.042 (native is 0) | +0.0373 to +0.0465 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.363 | 2.383 | +0.8% | +0.0072 to +0.0316 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.4 | 292.5 | +0.7% | +0.0673 to +4.2488 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.009 | 2.771 | +37.9% | +0.5185 to +1.0040 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | −0.0972 to +2.4972 | no |
| pod start wait, total (s) | 0.2 | 4.2 | +2000.0% | −0.1160 to +8.1160 | no |
| pod start wait, mean (s) | 0.2 | 1.658 | +729.2% | −0.1080 to +3.0247 | no |
| host CPU busy, the real machine under kind (%) | 75.76 | 76.97 | +1.6% | +1.1097 to +1.3119 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1476 | 1476 | +0.0% | −3.9246 to +4.1246 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.773 | −3.8% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 638.5 | 676.6 | +6.0% | −10.0403 to +86.2693 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1235 | 1247 | +1.0% | −30.7499 to +55.4893 | no |
| queue: job turnaround, submitted to done, mean (s) | 946.7 | 968.9 | +2.3% | −4.4441 to +48.9275 | no |
| queue: jobs unfinished at the window's end | 14.2 | 15.6 | +9.9% | +0.3772 to +2.4228 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.518 | +0.1% | −0.0051 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 287.2 | +4.9% | +10.4653 to +16.3582 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 287.2 | +4.9% | +10.4653 to +16.3582 | yes: power given |
| response time (ms), mean | 407.6 | 692.2 | +69.8% | +196.7648 to +372.3528 | yes: LOSS |
| response time (ms), 95th percentile | 1477 | 1402 | −5.0% | −736.7641 to +588.4361 | no |
| response time (ms), 99th percentile | 2068 | 1841 | −11.0% | −1204.3207 to +750.0273 | no |
| time over the response line (% of samples) | 17.69 | 62.12 | +251.1% | +36.4152 to +52.4350 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 24.4 | +156.8% | +11.0783 to +18.7217 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.63 | 2.3 | −80.2% | −14.0653 to −4.5914 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06344 | 0.09847 | +55.2% | +0.0272 to +0.0428 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.523 | 2.363 | +55.2% | +0.6529 to +1.0283 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.523 | 2.363 | +55.2% | +0.6529 to +1.0283 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438 | 290.4 | −33.7% | −192.2390 to −102.9396 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.027 | 2.009 | −0.8% | −0.1674 to +0.1329 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 43.18 | 75.76 | +75.4% | +28.5265 to +36.6350 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 1476 | +83.2% | +588.4071 to +752.3929 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 638.5 | +666171.3% | +417.4241 to +859.4041 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1235 | +176280.5% | +948.7820 to +1519.1457 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 111.6 | 946.7 | +748.2% | +726.3098 to +943.8735 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.2 | +14.200 (native is 0) | +9.4337 to +18.9663 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.008 | −16.5% | −1.6451 to −0.3387 | yes: GAIN |
| node-hours | 2.517 | 2.099 | −16.6% | −0.6918 to −0.1437 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 273.7 | −0.0% | −1.1783 to +0.9724 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 242.5 | −11.4% | −52.0107 to −10.5826 | yes: GAIN |
| response time (ms), mean | 407.6 | 383.2 | −6.0% | −53.0639 to +4.1649 | no |
| response time (ms), 95th percentile | 1477 | 1542 | +4.4% | −102.8222 to +234.2092 | no |
| response time (ms), 99th percentile | 2068 | 2149 | +3.9% | −127.2696 to +288.4180 | no |
| time over the response line (% of samples) | 17.69 | 17.96 | +1.5% | −0.7703 to +1.3029 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 10.5 | +10.5% | −0.3903 to +2.3903 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.7 | +124.700 (native is 0) | +60.5373 to +188.8627 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.63 | 14.55 | +25.2% | +0.3276 to +5.5224 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06344 | 0.07641 | +20.5% | +0.0039 to +0.0220 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.523 | 1.518 | −0.3% | −0.0330 to +0.0234 | no |
| Omni's own CPU (cores), mean | 0 | 0.07224 | +0.072 (native is 0) | +0.0667 to +0.0778 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.523 | 1.59 | +4.4% | +0.0364 to +0.0984 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438 | 384.4 | −12.2% | −89.5327 to −17.5366 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.027 | 2.464 | +21.6% | +0.1816 to +0.6939 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.4744 to +2.5256 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.9 | +1850.0% | +0.9804 to +6.4196 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.817 | +808.3% | +0.6863 to +2.5470 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.18 | 46.39 | +7.4% | +2.6688 to +3.7424 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 811.6 | +0.7% | −5.4053 to +16.6053 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.189 | −30.2% | −2.8173 to −0.8041 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 0.1667 | +73.9% | −0.0587 to +0.2004 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 111.6 | 116.2 | +4.1% | −6.6085 to +15.7585 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.008 | −16.5% | −1.6451 to −0.3387 | yes: GAIN |
| node-hours | 2.518 | 2.099 | −16.7% | −0.6924 to −0.1471 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 287.2 | 273.7 | −4.7% | −16.4660 to −10.5633 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.2 | 242.5 | −15.6% | −66.9310 to −22.4859 | yes: GAIN |
| response time (ms), mean | 692.2 | 383.2 | −44.6% | −402.4877 to −215.5288 | yes: GAIN |
| response time (ms), 95th percentile | 1402 | 1542 | +10.0% | −569.0280 to +848.7430 | no |
| response time (ms), 99th percentile | 1841 | 2149 | +16.7% | −733.7675 to +1349.2093 | no |
| time over the response line (% of samples) | 62.12 | 17.96 | −71.1% | −51.9481 to −36.3695 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24.4 | 10.5 | −57.0% | −17.1246 to −10.6754 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.7 | +124.700 (native is 0) | +60.5373 to +188.8627 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.3 | 14.55 | +532.8% | +5.7665 to +18.7401 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09847 | 0.07641 | −22.4% | −0.0316 to −0.0125 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.363 | 1.518 | −35.8% | −1.0453 to −0.6456 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07224 | +0.072 (native is 0) | +0.0667 to +0.0778 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.363 | 1.59 | −32.7% | −0.9763 to −0.5700 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.4 | 384.4 | +32.4% | +64.3229 to +123.7864 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.009 | 2.464 | +22.6% | +0.2193 to +0.6906 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.4744 to +2.5256 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.9 | +1850.0% | +0.9804 to +6.4196 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.817 | +808.3% | +0.6863 to +2.5470 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 75.76 | 46.39 | −38.8% | −33.6291 to −25.1211 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1476 | 811.6 | −45.0% | −751.7600 to −577.8400 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 638.5 | 0.1667 | −100.0% | −859.3008 to −417.3858 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1235 | 0.6 | −100.0% | −1519.2693 to −948.8584 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 946.7 | 116.2 | −87.7% | −939.7682 to −721.2651 | yes: GAIN |
| queue: jobs unfinished at the window's end | 14.2 | 0 | −100.0% | −18.9663 to −9.4337 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0172 to +0.0067 | no |
| node-hours | 2.517 | 2.513 | −0.1% | −0.0111 to +0.0040 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.8 | 286.5 | +4.6% | +9.6008 to +15.8335 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.8 | 286.4 | +4.6% | +9.4354 to +15.6656 | yes: power given |
| response time (ms), mean | 407.6 | 681.3 | +67.1% | +184.0819 to +363.1656 | yes: LOSS |
| response time (ms), 95th percentile | 1477 | 1373 | −7.0% | −741.1843 to +534.8673 | no |
| response time (ms), 99th percentile | 2068 | 1832 | −11.4% | −1168.3833 to +696.1431 | no |
| time over the response line (% of samples) | 17.69 | 60.83 | +243.9% | +35.5761 to +50.7090 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 24.3 | +155.8% | +11.0330 to +18.5670 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.1 | +31.100 (native is 0) | +27.3534 to +34.8466 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.63 | 2.552 | −78.1% | −13.9516 to −4.2017 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06344 | 0.0976 | +53.9% | +0.0262 to +0.0422 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.523 | 2.341 | +53.7% | +0.6263 to +1.0099 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04193 | +0.042 (native is 0) | +0.0373 to +0.0465 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.523 | 2.383 | +56.5% | +0.6720 to +1.0480 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438 | 292.5 | −33.2% | −191.1664 to −99.6960 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.027 | 2.771 | +36.7% | +0.4068 to +1.0813 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.0919 to +2.3081 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.2 | +2000.0% | +0.3216 to +7.6784 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.658 | +729.2% | +0.1931 to +2.7235 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.18 | 76.97 | +78.3% | +29.8237 to +37.7595 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806 | 1476 | +83.2% | +589.9523 to +751.0477 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.773 | −3.8% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09583 | 676.6 | +705942.9% | +448.0944 to +904.9628 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1247 | +178047.6% | +950.4385 to +1542.2286 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 111.6 | 968.9 | +768.1% | +739.5877 to +975.0790 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15.6 | +15.600 (native is 0) | +10.5736 to +20.6264 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*