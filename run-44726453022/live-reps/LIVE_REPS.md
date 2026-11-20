# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.87 | 10.13 |
| node-hours | 5.031 | 5.039 | 4.136 | 4.249 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 526.8 | 525.6 | 525.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 526.8 | 458.5 | 466.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 544.3 | 681.5 | 634.1 | 750.4 |
| response time (ms), 95th percentile | 2055 | 2874 | 2598 | 3080 |
| response time (ms), 99th percentile | 2778 | 3943 | 3466 | 4098 |
| time over the response line (% of samples) | 17.25 | 21.94 | 23.31 | 26.86 |
| failed requests (%) | 0 | 0.0331 | 0.007874 | 0.1144 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 13.7 | 12.2 | 15.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 203.6 | 48.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25.6 | 21.79 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.41 | 31.8 | 30.04 | 56.61 |
| utilisation (used / allocatable) | 0.03426 | 0.03427 | 0.0418 | 0.04009 |
| CPU used (cores), mean | 1.645 | 1.645 | 1.621 | 1.595 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05598 | 0.04204 |
| CPU used with Omni's own (cores), mean | 1.645 | 1.645 | 1.677 | 1.637 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 789 | 783.9 | 681.6 | 700.7 |
| HPA replicas, mean | 4.007 | 3.932 | 4.757 | 5.657 |
| pods started | 0.4 | 0.3 | 2.6 | 3.8 |
| pod start wait, total (s) | 1.1 | 0.6 | 6.2 | 14.8 |
| pod start wait, mean (s) | 0.8 | 0.6 | 1.667 | 3.212 |
| host CPU busy, the real machine under kind (%) | 49.98 | 56.25 | 56.05 | 61.99 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 858.2 | 951.4 | 904.4 | 1001 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.431 | 8.654 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 8.121 | 0.1125 | 14.73 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 62.6 | 0.6 | 95.9 |
| queue: job turnaround, submitted to done, mean (s) | 163.6 | 256.1 | 211.9 | 300.3 |
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
| worker nodes in service, mean | 12 | 10.13 | −15.6% | −3.3359 to −0.4028 | yes: GAIN |
| node-hours | 5.039 | 4.249 | −15.7% | −1.4005 to −0.1779 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 525.7 | −0.2% | −4.2073 to +2.1379 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 466.9 | −11.4% | −104.7738 to −14.9247 | yes: GAIN |
| response time (ms), mean | 681.5 | 750.4 | +10.1% | −48.9724 to +186.8302 | no |
| response time (ms), 95th percentile | 2874 | 3080 | +7.2% | −560.4284 to +971.9024 | no |
| response time (ms), 99th percentile | 3943 | 4098 | +3.9% | −720.7700 to +1032.0084 | no |
| time over the response line (% of samples) | 21.94 | 26.86 | +22.4% | +3.1984 to +6.6452 | yes: LOSS |
| failed requests (%) | 0.0331 | 0.1144 | +245.5% | −0.1253 to +0.2878 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 15.8 | +15.3% | +0.8633 to +3.3367 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.4 | +48.400 (native is 0) | +35.5236 to +61.2764 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 31.8 | 56.61 | +78.0% | −20.5371 to +70.1504 | no |
| utilisation (used / allocatable) | 0.03427 | 0.04009 | +17.0% | −0.0017 to +0.0133 | no |
| CPU used (cores), mean | 1.645 | 1.595 | −3.0% | −0.2305 to +0.1316 | no |
| Omni's own CPU (cores), mean | 0 | 0.04204 | +0.042 (native is 0) | +0.0339 to +0.0502 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.637 | −0.5% | −0.1855 to +0.1706 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783.9 | 700.7 | −10.6% | −198.5843 to +32.2630 | no |
| HPA replicas, mean | 3.932 | 5.657 | +43.8% | +0.3437 to +3.1046 | yes: power given |
| pods started | 0.3 | 3.8 | +1166.7% | +1.9094 to +5.0906 | yes: power given |
| pod start wait, total (s) | 0.6 | 14.8 | +2366.7% | +1.6791 to +26.7209 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 3.212 | +435.3% | +0.8545 to +4.3688 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.25 | 61.99 | +10.2% | +4.5367 to +6.9329 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 951.4 | 1001 | +5.3% | +24.0861 to +75.9139 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.654 | −27.9% | −5.7833 to −0.9095 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 8.121 | 14.73 | +81.4% | −3.8814 to +17.0980 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 62.6 | 95.9 | +53.2% | −83.9804 to +150.5804 | no |
| queue: job turnaround, submitted to done, mean (s) | 256.1 | 300.3 | +17.3% | +15.5701 to +72.7966 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.039 | +0.1% | −0.0069 to +0.0215 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 526.8 | +0.2% | −0.7655 to +2.7975 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 526.8 | +0.2% | −0.7655 to +2.7975 | no |
| response time (ms), mean | 544.3 | 681.5 | +25.2% | +24.9396 to +249.4590 | yes: LOSS |
| response time (ms), 95th percentile | 2055 | 2874 | +39.9% | +195.5624 to +1442.8666 | yes: LOSS |
| response time (ms), 99th percentile | 2778 | 3943 | +41.9% | +416.8145 to +1912.9279 | yes: LOSS |
| time over the response line (% of samples) | 17.25 | 21.94 | +27.2% | +1.7000 to +7.6733 | yes: LOSS |
| failed requests (%) | 0 | 0.0331 | +0.033 (native is 0) | −0.0083 to +0.0745 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 13.7 | +52.2% | +1.9595 to +7.4405 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.41 | 31.8 | +137.2% | −2.9152 to +39.7019 | no |
| utilisation (used / allocatable) | 0.03426 | 0.03427 | +0.0% | −0.0016 to +0.0016 | no |
| CPU used (cores), mean | 1.645 | 1.645 | +0.0% | −0.0748 to +0.0752 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.645 | 1.645 | +0.0% | −0.0748 to +0.0752 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 789 | 783.9 | −0.7% | −35.8650 to +25.5483 | no |
| HPA replicas, mean | 4.007 | 3.932 | −1.9% | −0.3528 to +0.2040 | no |
| pods started | 0.4 | 0.3 | −25.0% | −0.6278 to +0.4278 | no |
| pod start wait, total (s) | 1.1 | 0.6 | −45.5% | −1.9005 to +0.9005 | no |
| pod start wait, mean (s) | 0.8 | 0.6 | −25.0% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 49.98 | 56.25 | +12.5% | +4.4960 to +8.0412 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 858.2 | 951.4 | +10.9% | +33.0038 to +153.3962 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 8.121 | +12081.3% | −1.9806 to +18.0889 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 62.6 | +15550.0% | −30.0927 to +154.4927 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.6 | 256.1 | +56.5% | +35.5809 to +149.4024 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.87 | −17.7% | −3.8194 to −0.4405 | yes: GAIN |
| node-hours | 5.031 | 4.136 | −17.8% | −1.6032 to −0.1871 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 525.6 | −0.0% | −2.9965 to +2.6061 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 458.5 | −12.8% | −120.2742 to −14.1412 | yes: GAIN |
| response time (ms), mean | 544.3 | 634.1 | +16.5% | +4.5040 to +175.1683 | yes: LOSS |
| response time (ms), 95th percentile | 2055 | 2598 | +26.5% | +49.5919 to +1037.7741 | yes: LOSS |
| response time (ms), 99th percentile | 2778 | 3466 | +24.8% | −19.1942 to +1395.0588 | no |
| time over the response line (% of samples) | 17.25 | 23.31 | +35.1% | +2.4206 to +9.6975 | yes: LOSS |
| failed requests (%) | 0 | 0.007874 | +0.008 (native is 0) | −0.0099 to +0.0257 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 12.2 | +35.6% | +0.1878 to +6.2122 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 203.6 | +203.600 (native is 0) | +67.7593 to +339.4407 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.41 | 30.04 | +124.1% | −12.4619 to +45.7352 | no |
| utilisation (used / allocatable) | 0.03426 | 0.0418 | +22.0% | +0.0002 to +0.0149 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.645 | 1.621 | −1.4% | −0.1498 to +0.1035 | no |
| Omni's own CPU (cores), mean | 0 | 0.05598 | +0.056 (native is 0) | +0.0507 to +0.0613 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.677 | +2.0% | −0.0932 to +0.1589 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 789 | 681.6 | −13.6% | −214.4896 to −0.4402 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.007 | 4.757 | +18.7% | +0.3616 to +1.1396 | yes: power given |
| pods started | 0.4 | 2.6 | +550.0% | +0.4221 to +3.9779 | yes: power given |
| pod start wait, total (s) | 1.1 | 6.2 | +463.6% | +0.0934 to +10.1066 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 1.667 | +108.3% | −0.1934 to +1.9267 | no |
| host CPU busy, the real machine under kind (%) | 49.98 | 56.05 | +12.1% | +4.7209 to +7.4177 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 858.2 | 904.4 | +5.4% | +13.7801 to +78.6199 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.431 | −29.7% | −6.1821 to −0.9563 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1125 | +68.7% | −0.0424 to +0.1341 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.6 | +50.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.6 | 211.9 | +29.5% | +20.8995 to +75.7421 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.87 | −17.7% | −3.8194 to −0.4405 | yes: GAIN |
| node-hours | 5.039 | 4.136 | −17.9% | −1.6064 to −0.1986 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 525.6 | −0.2% | −3.8452 to +1.4227 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 458.5 | −13.0% | −121.2617 to −15.1857 | yes: GAIN |
| response time (ms), mean | 681.5 | 634.1 | −6.9% | −140.4171 to +45.6908 | no |
| response time (ms), 95th percentile | 2874 | 2598 | −9.6% | −875.0818 to +324.0188 | no |
| response time (ms), 99th percentile | 3943 | 3466 | −12.1% | −1134.0183 to +180.1405 | no |
| time over the response line (% of samples) | 21.94 | 23.31 | +6.3% | −2.6241 to +5.3689 | no |
| failed requests (%) | 0.0331 | 0.007874 | −76.2% | −0.0734 to +0.0230 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.7 | 12.2 | −10.9% | −2.5256 to −0.4744 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 203.6 | +203.600 (native is 0) | +67.7593 to +339.4407 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 31.8 | 30.04 | −5.5% | −32.2734 to +28.7601 | no |
| utilisation (used / allocatable) | 0.03427 | 0.0418 | +22.0% | +0.0007 to +0.0144 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.645 | 1.621 | −1.4% | −0.1539 to +0.1072 | no |
| Omni's own CPU (cores), mean | 0 | 0.05598 | +0.056 (native is 0) | +0.0507 to +0.0613 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.677 | +2.0% | −0.0987 to +0.1640 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 783.9 | 681.6 | −13.1% | −194.6328 to −9.9803 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.932 | 4.757 | +21.0% | +0.4264 to +1.2235 | yes: power given |
| pods started | 0.3 | 2.6 | +766.7% | +0.6463 to +3.9537 | yes: power given |
| pod start wait, total (s) | 0.6 | 6.2 | +933.3% | +0.9374 to +10.2626 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.667 | +177.8% | +0.2103 to +1.9230 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.25 | 56.05 | −0.4% | −1.1503 to +0.7516 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 951.4 | 904.4 | −4.9% | −78.5241 to −15.4759 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.431 | −29.7% | −6.1821 to −0.9563 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 8.121 | 0.1125 | −98.6% | −18.0051 to +1.9884 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 62.6 | 0.6 | −99.0% | −154.3667 to +30.3667 | no |
| queue: job turnaround, submitted to done, mean (s) | 256.1 | 211.9 | −17.2% | −78.6859 to −9.6557 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.13 | −15.6% | −3.3359 to −0.4028 | yes: GAIN |
| node-hours | 5.031 | 4.249 | −15.5% | −1.3974 to −0.1663 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 525.7 | −0.0% | −2.3212 to +2.2837 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 466.9 | −11.2% | −103.6799 to −13.9866 | yes: GAIN |
| response time (ms), mean | 544.3 | 750.4 | +37.9% | +82.4841 to +329.7723 | yes: LOSS |
| response time (ms), 95th percentile | 2055 | 3080 | +49.9% | +458.0602 to +1591.8428 | yes: LOSS |
| response time (ms), 99th percentile | 2778 | 4098 | +47.5% | +555.3999 to +2085.5809 | yes: LOSS |
| time over the response line (% of samples) | 17.25 | 26.86 | +55.7% | +6.3464 to +12.8705 | yes: LOSS |
| failed requests (%) | 0 | 0.1144 | +0.114 (native is 0) | −0.0853 to +0.3140 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 15.8 | +75.6% | +4.1707 to +9.4293 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 48.4 | +48.400 (native is 0) | +35.5236 to +61.2764 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.41 | 56.61 | +322.2% | −2.3338 to +88.7338 | no |
| utilisation (used / allocatable) | 0.03426 | 0.04009 | +17.0% | −0.0019 to +0.0136 | no |
| CPU used (cores), mean | 1.645 | 1.595 | −3.0% | −0.2033 to +0.1047 | no |
| Omni's own CPU (cores), mean | 0 | 0.04204 | +0.042 (native is 0) | +0.0339 to +0.0502 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.637 | −0.4% | −0.1562 to +0.1416 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 789 | 700.7 | −11.2% | −212.8248 to +36.1868 | no |
| HPA replicas, mean | 4.007 | 5.657 | +41.2% | +0.3184 to +2.9811 | yes: power given |
| pods started | 0.4 | 3.8 | +850.0% | +1.8474 to +4.9526 | yes: power given |
| pod start wait, total (s) | 1.1 | 14.8 | +1245.5% | +1.0649 to +26.3351 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 3.212 | +301.5% | +0.5670 to +4.2564 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.98 | 61.99 | +24.0% | +9.8945 to +14.1122 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 858.2 | 1001 | +16.7% | +72.7586 to +213.6414 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.654 | −27.9% | −5.7833 to −0.9095 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 14.73 | +21993.8% | −0.0238 to +29.3488 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 95.9 | +23875.0% | −7.8966 to +198.8966 | no |
| queue: job turnaround, submitted to done, mean (s) | 163.6 | 300.3 | +83.5% | +70.7323 to +202.6177 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*