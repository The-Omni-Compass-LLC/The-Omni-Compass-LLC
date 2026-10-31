# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.465 | 5.398 |
| node-hours | 2.511 | 2.512 | 2.291 | 2.264 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.2 | 274 | 274.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 274.2 | 257.1 | 255.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 427.3 | 496 | 408.6 | 460.9 |
| response time (ms), 95th percentile | 1554 | 2199 | 1719 | 2189 |
| response time (ms), 99th percentile | 2231 | 3051 | 2442 | 3049 |
| time over the response line (% of samples) | 20.41 | 16.9 | 20.06 | 16.93 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.2 | 9.9 | 10.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 36.6 | 37.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.38 | 25.86 | 11.76 | 28 |
| utilisation (used / allocatable) | 0.06469 | 0.06523 | 0.07065 | 0.07375 |
| CPU used (cores), mean | 1.553 | 1.566 | 1.528 | 1.566 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01617 | 0.01821 |
| CPU used with Omni's own (cores), mean | 1.553 | 1.566 | 1.544 | 1.584 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.5 | 429.2 | 406.2 | 392.5 |
| HPA replicas, mean | 2.002 | 2.022 | 2.272 | 2.117 |
| pods started | 0.2 | 0.2 | 0.7 | 0 |
| pod start wait, total (s) | 0.4 | 0.3 | 1.1 | 0 |
| pod start wait, mean (s) | 0.2 | 0.15 | 1 | 0 |
| host CPU busy, the real machine under kind (%) | 43.7 | 46.9 | 44.74 | 47.85 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 812.5 | 863.6 | 821.8 | 866.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.1 | 5.005 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1.137 | 0.0625 | 1.163 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 4.1 | 0.5 | 3.3 |
| queue: job turnaround, submitted to done, mean (s) | 118.3 | 164.4 | 126.5 | 166.9 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.398 | −10.0% | −1.3634 to +0.1599 | no |
| node-hours | 2.512 | 2.264 | −9.9% | −0.5698 to +0.0729 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.7 | +0.2% | −0.1371 to +1.1360 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 255.8 | −6.7% | −42.5004 to +5.6576 | no |
| response time (ms), mean | 496 | 460.9 | −7.1% | −56.2708 to −13.8511 | yes: GAIN |
| response time (ms), 95th percentile | 2199 | 2189 | −0.5% | −135.9936 to +114.8706 | no |
| response time (ms), 99th percentile | 3051 | 3049 | −0.1% | −207.1463 to +202.9751 | no |
| time over the response line (% of samples) | 16.9 | 16.93 | +0.2% | −0.9777 to +1.0413 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 10.8 | +5.9% | −0.3656 to +1.5656 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.100 (native is 0) | +19.9179 to +54.2821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.86 | 28 | +8.3% | −0.6440 to +4.9207 | no |
| utilisation (used / allocatable) | 0.06523 | 0.07375 | +13.1% | −0.0027 to +0.0197 | no |
| CPU used (cores), mean | 1.566 | 1.566 | +0.0% | −0.0240 to +0.0242 | no |
| Omni's own CPU (cores), mean | 0 | 0.01821 | +0.018 (native is 0) | +0.0169 to +0.0195 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.566 | 1.584 | +1.2% | −0.0055 to +0.0421 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.2 | 392.5 | −8.5% | −86.3865 to +12.9979 | no |
| HPA replicas, mean | 2.022 | 2.117 | +4.7% | −0.0805 to +0.2705 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.15 | 0 | −100.0% | −0.4893 to +0.1893 | no |
| host CPU busy, the real machine under kind (%) | 46.9 | 47.85 | +2.0% | +0.3857 to +1.5085 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 863.6 | 866.8 | +0.4% | −2.2975 to +8.6975 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.005 | −16.6% | −2.1483 to +0.1579 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.137 | 1.162 | +2.2% | −0.2072 to +0.2572 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.1 | 3.3 | −19.5% | −3.1556 to +1.5556 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 166.9 | +1.5% | −1.4250 to +6.4667 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.512 | +0.1% | −0.0050 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.2 | +0.2% | −0.1918 to +1.1959 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 274.2 | +0.2% | −0.1918 to +1.1959 | no |
| response time (ms), mean | 427.3 | 496 | +16.1% | +15.5315 to +121.9247 | yes: LOSS |
| response time (ms), 95th percentile | 1554 | 2199 | +41.6% | +218.0700 to +1073.0550 | yes: LOSS |
| response time (ms), 99th percentile | 2231 | 3051 | +36.7% | +290.1212 to +1349.6344 | yes: LOSS |
| time over the response line (% of samples) | 20.41 | 16.9 | −17.2% | −6.0236 to −1.0019 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.2 | +6.2% | −0.0032 to +1.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.38 | 25.86 | +149.0% | +7.8731 to +23.0735 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06469 | 0.06523 | +0.8% | −0.0011 to +0.0022 | no |
| CPU used (cores), mean | 1.553 | 1.566 | +0.8% | −0.0272 to +0.0532 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.553 | 1.566 | +0.8% | −0.0272 to +0.0532 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.5 | 429.2 | −0.1% | −15.6217 to +15.1038 | no |
| HPA replicas, mean | 2.002 | 2.022 | +1.0% | −0.0923 to +0.1311 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, total (s) | 0.4 | 0.3 | −25.0% | −1.2898 to +1.0898 | no |
| pod start wait, mean (s) | 0.2 | 0.15 | −25.0% | −0.6449 to +0.5449 | no |
| host CPU busy, the real machine under kind (%) | 43.7 | 46.9 | +7.3% | +2.0481 to +4.3448 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 863.6 | +6.3% | +20.5273 to +81.6727 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1.137 | +1416.7% | +0.7387 to +1.3863 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 4.1 | +583.3% | +1.2569 to +5.7431 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 118.3 | 164.4 | +39.0% | +20.0903 to +72.1514 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.465 | −8.9% | −1.2621 to +0.1927 | no |
| node-hours | 2.511 | 2.291 | −8.7% | −0.5210 to +0.0818 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274 | +0.1% | −0.2864 to +0.8912 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 257.1 | −6.0% | −39.3978 to +6.3401 | no |
| response time (ms), mean | 427.3 | 408.6 | −4.4% | −43.5015 to +6.1273 | no |
| response time (ms), 95th percentile | 1554 | 1719 | +10.6% | +14.3773 to +315.4737 | yes: LOSS |
| response time (ms), 99th percentile | 2231 | 2442 | +9.4% | +0.5880 to +419.9780 | yes: LOSS |
| time over the response line (% of samples) | 20.41 | 20.06 | −1.7% | −1.0001 to +0.2997 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 9.9 | +3.1% | −0.3786 to +0.9786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.6 | +36.600 (native is 0) | +15.9861 to +57.2139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.38 | 11.76 | +13.3% | −0.1861 to +2.9394 | no |
| utilisation (used / allocatable) | 0.06469 | 0.07065 | +9.2% | −0.0019 to +0.0139 | no |
| CPU used (cores), mean | 1.553 | 1.528 | −1.6% | −0.0691 to +0.0199 | no |
| Omni's own CPU (cores), mean | 0 | 0.01617 | +0.016 (native is 0) | +0.0147 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.553 | 1.544 | −0.5% | −0.0541 to +0.0373 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.5 | 406.2 | −5.4% | −54.6516 to +8.0869 | no |
| HPA replicas, mean | 2.002 | 2.272 | +13.5% | +0.0983 to +0.4418 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 0.4 | 1.1 | +175.0% | −0.5181 to +1.9181 | no |
| pod start wait, mean (s) | 0.2 | 1 | +400.0% | −0.0793 to +1.6793 | no |
| host CPU busy, the real machine under kind (%) | 43.7 | 44.74 | +2.4% | +0.4593 to +1.6118 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 821.8 | +1.1% | +0.7160 to +17.8840 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.1 | −15.0% | −2.0832 to +0.2823 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.0625 | −16.7% | −0.0471 to +0.0221 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.5 | −16.7% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.3 | 126.5 | +7.0% | −0.9456 to +17.3956 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.465 | −8.9% | −1.2621 to +0.1927 | no |
| node-hours | 2.512 | 2.291 | −8.8% | −0.5271 to +0.0846 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274 | −0.1% | −0.8551 to +0.4558 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 257.1 | −6.2% | −39.9491 to +5.8874 | no |
| response time (ms), mean | 496 | 408.6 | −17.6% | −135.0573 to −39.7730 | yes: GAIN |
| response time (ms), 95th percentile | 2199 | 1719 | −21.9% | −821.3730 to −139.9010 | yes: GAIN |
| response time (ms), 99th percentile | 3051 | 2442 | −20.0% | −1042.1996 to −176.9900 | yes: GAIN |
| time over the response line (% of samples) | 16.9 | 20.06 | +18.7% | +1.1447 to +5.1805 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 9.9 | −2.9% | −1.4705 to +0.8705 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.6 | +36.600 (native is 0) | +15.9861 to +57.2139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 25.86 | 11.76 | −54.5% | −21.4831 to −6.7103 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06523 | 0.07065 | +8.3% | −0.0038 to +0.0146 | no |
| CPU used (cores), mean | 1.566 | 1.528 | −2.4% | −0.0726 to −0.0026 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01617 | +0.016 (native is 0) | +0.0147 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.566 | 1.544 | −1.4% | −0.0572 to +0.0143 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.2 | 406.2 | −5.4% | −66.6598 to +20.6130 | no |
| HPA replicas, mean | 2.022 | 2.272 | +12.4% | +0.0706 to +0.4307 | yes: power given |
| pods started | 0.2 | 0.7 | +250.0% | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | +0.1427 to +1.4573 | yes: LOSS |
| pod start wait, mean (s) | 0.15 | 1 | +566.7% | +0.2647 to +1.4353 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.9 | 44.74 | −4.6% | −3.0768 to −1.2451 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 863.6 | 821.8 | −4.8% | −67.6146 to −15.9854 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.1 | −15.0% | −2.0832 to +0.2823 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.137 | 0.0625 | −94.5% | −1.3966 to −0.7534 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.1 | 0.5 | −87.8% | −5.9166 to −1.2834 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 164.4 | 126.5 | −23.1% | −60.4873 to −15.3043 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.398 | −10.0% | −1.3634 to +0.1599 | no |
| node-hours | 2.511 | 2.264 | −9.8% | −0.5637 to +0.0701 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 274.7 | +0.4% | +0.5260 to +1.4769 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 255.8 | −6.5% | −41.9567 to +6.1180 | no |
| response time (ms), mean | 427.3 | 460.9 | +7.9% | −7.2283 to +74.5626 | no |
| response time (ms), 95th percentile | 1554 | 2189 | +40.9% | +247.8736 to +1022.1284 | yes: LOSS |
| response time (ms), 99th percentile | 2231 | 3049 | +36.6% | +346.6110 to +1288.9734 | yes: LOSS |
| time over the response line (% of samples) | 20.41 | 16.93 | −17.1% | −6.4117 to −0.5502 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.8 | +12.5% | +0.1444 to +2.2556 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.100 (native is 0) | +19.9179 to +54.2821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.38 | 28 | +169.6% | +9.3636 to +25.8597 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06469 | 0.07375 | +14.0% | −0.0008 to +0.0190 | no |
| CPU used (cores), mean | 1.553 | 1.566 | +0.8% | −0.0195 to +0.0457 | no |
| Omni's own CPU (cores), mean | 0 | 0.01821 | +0.018 (native is 0) | +0.0169 to +0.0195 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.553 | 1.584 | +2.0% | −0.0021 to +0.0647 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.5 | 392.5 | −8.6% | −74.9857 to +1.0793 | no |
| HPA replicas, mean | 2.002 | 2.117 | +5.7% | −0.0570 to +0.2857 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.4 | 0 | −100.0% | −1.3048 to +0.5048 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 43.7 | 47.85 | +9.5% | +3.0849 to +5.2023 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.5 | 866.8 | +6.7% | +24.7319 to +83.8681 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.005 | −16.6% | −2.1483 to +0.1579 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 1.162 | +1450.0% | +0.7618 to +1.4132 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 3.3 | +450.0% | +0.9462 to +4.4538 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 118.3 | 166.9 | +41.1% | +23.3282 to +73.9551 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*