# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.49 | 6.359 |
| node-hours | 5.021 | 5.028 | 4.388 | 2.667 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 504.7 | 525.4 | 505.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 504.7 | 477.9 | 327.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 728.8 | 123.9 | 840.4 | 73.52 |
| response time (ms), 95th percentile | 2963 | 171.8 | 3466 | 98.83 |
| response time (ms), 99th percentile | 4015 | 202.3 | 4663 | 126.8 |
| time over the response line (% of samples) | 24.39 | 0 | 28.8 | 0.00726 |
| failed requests (%) | 0 | 0 | 0.0689 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 0 | 13.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 142.6 | 31.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 26.67 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.31 | 0.025 | 47.89 | 0.05167 |
| utilisation (used / allocatable) | 0.03632 | 0.006207 | 0.04055 | 0.009666 |
| CPU used (cores), mean | 1.743 | 0.2979 | 1.68 | 0.2463 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05832 | 0.03219 |
| CPU used with Omni's own (cores), mean | 1.743 | 0.2979 | 1.738 | 0.2785 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747 | 4150 | 689.2 | 3272 |
| HPA replicas, mean | 3.923 | 4.217 | 5.155 | 4.435 |
| pods started | 0.1 | 0.3 | 3.9 | 1.3 |
| pod start wait, total (s) | 0.2 | 0.6 | 9.9 | 2.2 |
| pod start wait, mean (s) | 0.2 | 0.4 | 2.198 | 0.775 |
| host CPU busy, the real machine under kind (%) | 53.11 | 15.12 | 59.48 | 17.8 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 916.1 | 1507 | 972.2 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.656 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1160 | 0.1833 | 1161 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1476 | 0.9 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 222.5 | 1160 | 273.7 | 1161 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.359 | −47.0% | −6.0023 to −5.2802 | yes: GAIN |
| node-hours | 5.028 | 2.667 | −46.9% | −2.5138 to −2.2075 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.7 | 505.4 | +0.1% | +0.1110 to +1.1868 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.7 | 327.9 | −35.0% | −188.4340 to −165.2141 | yes: GAIN |
| response time (ms), mean | 123.9 | 73.52 | −40.7% | −61.1279 to −39.6272 | yes: GAIN |
| response time (ms), 95th percentile | 171.8 | 98.83 | −42.5% | −90.1344 to −55.7796 | yes: GAIN |
| response time (ms), 99th percentile | 202.3 | 126.8 | −37.3% | −101.1110 to −49.9908 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.00726 | +0.007 (native is 0) | −0.0037 to +0.0182 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.8 | +31.800 (native is 0) | +29.0856 to +34.5144 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 0.05167 | +106.7% | −0.0770 to +0.1303 | no |
| utilisation (used / allocatable) | 0.006207 | 0.009666 | +55.7% | +0.0030 to +0.0039 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2979 | 0.2463 | −17.3% | −0.0607 to −0.0425 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03219 | +0.032 (native is 0) | +0.0280 to +0.0364 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2979 | 0.2785 | −6.5% | −0.0289 to −0.0100 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4150 | 3272 | −21.2% | −1001.7173 to −755.4514 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.217 | 4.435 | +5.2% | −0.0778 to +0.5130 | no |
| pods started | 0.3 | 1.3 | +333.3% | +0.0463 to +1.9537 | yes: power given |
| pod start wait, total (s) | 0.6 | 2.2 | +266.7% | −0.3134 to +3.5134 | no |
| pod start wait, mean (s) | 0.4 | 0.775 | +93.8% | −0.3265 to +1.0765 | no |
| host CPU busy, the real machine under kind (%) | 15.12 | 17.8 | +17.7% | +1.9074 to +3.4576 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1507 | +0.0% | −1.9053 to +3.1053 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1161 | +0.1% | −1.9461 to +3.3045 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1477 | +0.1% | −1.6335 to +3.4335 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1161 | +0.1% | −1.9461 to +3.3045 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.021 | 5.028 | +0.1% | −0.0112 to +0.0252 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 504.7 | −4.1% | −24.8887 to −17.9906 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 504.7 | −4.1% | −24.8887 to −17.9906 | yes: GAIN |
| response time (ms), mean | 728.8 | 123.9 | −83.0% | −935.1327 to −274.7290 | yes: GAIN |
| response time (ms), 95th percentile | 2963 | 171.8 | −94.2% | −4357.8127 to −1224.5983 | yes: GAIN |
| response time (ms), 99th percentile | 4015 | 202.3 | −95.0% | −5899.6193 to −1724.8381 | yes: GAIN |
| time over the response line (% of samples) | 24.39 | 0 | −100.0% | −36.8277 to −11.9550 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 0 | −100.0% | −17.6108 to −6.9892 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.31 | 0.025 | −99.9% | −25.6012 to −10.9721 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03632 | 0.006207 | −82.9% | −0.0344 to −0.0258 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.743 | 0.2979 | −82.9% | −1.6503 to −1.2407 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.743 | 0.2979 | −82.9% | −1.6503 to −1.2407 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747 | 4150 | +455.6% | +2965.1616 to +3841.8175 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.923 | 4.217 | +7.5% | +0.1410 to +0.4473 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.7285 to +1.5285 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.6121 to +1.0121 | no |
| host CPU busy, the real machine under kind (%) | 53.11 | 15.12 | −71.5% | −44.1768 to −31.8035 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 916.1 | 1507 | +64.5% | +478.2197 to +702.7803 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1160 | +959875.9% | +1157.0280 to +1162.6720 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1476 | +210771.4% | +1472.5348 to +1478.2652 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 222.5 | 1160 | +421.3% | +825.6656 to +1049.2177 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.49 | −12.6% | −3.1918 to +0.1700 | no |
| node-hours | 5.021 | 4.388 | −12.6% | −1.3407 to +0.0738 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 525.4 | −0.2% | −3.0272 to +1.3742 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 477.9 | −9.2% | −101.2494 to +4.7756 | no |
| response time (ms), mean | 728.8 | 840.4 | +15.3% | +24.6092 to +198.6286 | yes: LOSS |
| response time (ms), 95th percentile | 2963 | 3466 | +17.0% | +145.0267 to +860.4913 | yes: LOSS |
| response time (ms), 99th percentile | 4015 | 4663 | +16.2% | +197.4976 to +1099.4520 | yes: LOSS |
| time over the response line (% of samples) | 24.39 | 28.8 | +18.1% | +2.0084 to +6.8142 | yes: LOSS |
| failed requests (%) | 0 | 0.0689 | +0.069 (native is 0) | −0.0368 to +0.1746 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 13.9 | +13.0% | +0.3749 to +2.8251 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.6 | +142.600 (native is 0) | +70.4771 to +214.7229 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.31 | 47.89 | +161.5% | −3.8934 to +63.0534 | no |
| utilisation (used / allocatable) | 0.03632 | 0.04055 | +11.7% | −0.0028 to +0.0112 | no |
| CPU used (cores), mean | 1.743 | 1.68 | −3.7% | −0.2005 to +0.0727 | no |
| Omni's own CPU (cores), mean | 0 | 0.05832 | +0.058 (native is 0) | +0.0535 to +0.0631 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.743 | 1.738 | −0.3% | −0.1419 to +0.1308 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747 | 689.2 | −7.7% | −162.9755 to +47.4163 | no |
| HPA replicas, mean | 3.923 | 5.155 | +31.4% | +0.6166 to +1.8479 | yes: power given |
| pods started | 0.1 | 3.9 | +3800.0% | +1.6996 to +5.9004 | yes: power given |
| pod start wait, total (s) | 0.2 | 9.9 | +4850.0% | +3.8009 to +15.5991 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.198 | +998.8% | +0.9480 to +3.0470 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.11 | 59.48 | +12.0% | +4.9712 to +7.7697 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 916.1 | 972.2 | +6.1% | +22.1207 to +90.0793 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.656 | −19.5% | −4.7531 to +0.0649 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.1833 | +51.7% | −0.0331 to +0.1581 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 222.5 | 273.7 | +23.0% | +22.5618 to +79.8632 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.49 | −12.6% | −3.1918 to +0.1700 | no |
| node-hours | 5.028 | 4.388 | −12.7% | −1.3416 to +0.0606 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.7 | 525.4 | +4.1% | +17.1546 to +24.0718 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.7 | 477.9 | −5.3% | −82.1870 to +28.5925 | no |
| response time (ms), mean | 123.9 | 840.4 | +578.3% | +324.8529 to +1108.2465 | yes: LOSS |
| response time (ms), 95th percentile | 171.8 | 3466 | +1917.4% | +1527.3351 to +5060.5939 | yes: LOSS |
| response time (ms), 99th percentile | 202.3 | 4663 | +2204.8% | +2106.4934 to +6814.9136 | yes: LOSS |
| time over the response line (% of samples) | 0 | 28.8 | +28.803 (native is 0) | +16.0534 to +41.5520 | yes: LOSS |
| failed requests (%) | 0 | 0.0689 | +0.069 (native is 0) | −0.0368 to +0.1746 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 13.9 | +13.900 (native is 0) | +8.5106 to +19.2894 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.6 | +142.600 (native is 0) | +70.4771 to +214.7229 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.025 | 47.89 | +191466.7% | +9.8693 to +85.8641 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006207 | 0.04055 | +553.4% | +0.0304 to +0.0383 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2979 | 1.68 | +463.8% | +1.1486 to +1.6147 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05832 | +0.058 (native is 0) | +0.0535 to +0.0631 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2979 | 1.738 | +483.3% | +1.2033 to +1.6766 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4150 | 689.2 | −83.4% | −3995.9011 to −2926.6371 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.217 | 5.155 | +22.2% | +0.3111 to +1.5650 | yes: power given |
| pods started | 0.3 | 3.9 | +1200.0% | +1.4356 to +5.7644 | yes: power given |
| pod start wait, total (s) | 0.6 | 9.9 | +1550.0% | +3.2675 to +15.3325 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 2.198 | +449.4% | +0.9613 to +2.6337 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.12 | 59.48 | +293.4% | +37.0068 to +51.7144 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 972.2 | −35.5% | −676.5882 to −392.2118 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.1833 | −100.0% | −1162.5736 to −1157.0014 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.9 | −99.9% | −1477.9765 to −1472.4235 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 273.7 | −76.4% | −1021.9468 to −750.5115 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.359 | −47.0% | −6.0023 to −5.2802 | yes: GAIN |
| node-hours | 5.021 | 2.667 | −46.9% | −2.5096 to −2.1977 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.2 | 505.4 | −4.0% | −23.9578 to −17.6238 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.2 | 327.9 | −37.7% | −209.0559 to −187.4715 | yes: GAIN |
| response time (ms), mean | 728.8 | 73.52 | −89.9% | −994.3922 to −316.2245 | yes: GAIN |
| response time (ms), 95th percentile | 2963 | 98.84 | −96.7% | −4437.6698 to −1290.6552 | yes: GAIN |
| response time (ms), 99th percentile | 4015 | 126.8 | −96.8% | −5981.3848 to −1794.1744 | yes: GAIN |
| time over the response line (% of samples) | 24.39 | 0.00726 | −100.0% | −36.8161 to −11.9520 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.3 | 0 | −100.0% | −17.6108 to −6.9892 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 31.8 | +31.800 (native is 0) | +29.0856 to +34.5144 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.31 | 0.05167 | −99.7% | −25.5245 to −10.9955 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03632 | 0.009666 | −73.4% | −0.0306 to −0.0227 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.743 | 0.2463 | −85.9% | −1.7032 to −1.2910 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03219 | +0.032 (native is 0) | +0.0280 to +0.0364 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.743 | 0.2785 | −84.0% | −1.6671 to −1.2627 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 747 | 3272 | +338.0% | +2187.5019 to +2862.3084 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.923 | 4.435 | +13.0% | +0.2471 to +0.7764 | yes: power given |
| pods started | 0.1 | 1.3 | +1200.0% | +0.0417 to +2.3583 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.2 | +1000.0% | −0.1591 to +4.1591 | no |
| pod start wait, mean (s) | 0.2 | 0.775 | +287.5% | +0.0029 to +1.1471 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.11 | 17.8 | −66.5% | −40.9103 to −29.7050 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 916.1 | 1507 | +64.5% | +479.7475 to +702.4525 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 1161 | +960437.9% | +1157.6736 to +1163.3847 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1477 | +210900.0% | +1473.5389 to +1479.0611 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 222.5 | 1161 | +421.6% | +827.2511 to +1048.9906 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*