# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.54 | 6.221 |
| node-hours | 5.017 | 5.03 | 4.419 | 2.61 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 504.9 | 527.8 | 505.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 504.9 | 481.8 | 323.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 634.8 | 123 | 756.4 | 72.19 |
| response time (ms), 95th percentile | 2495 | 171.9 | 3165 | 97.17 |
| response time (ms), 99th percentile | 3357 | 205.4 | 4198 | 128.4 |
| time over the response line (% of samples) | 22.96 | 0 | 25.67 | 0 |
| failed requests (%) | 0 | 0 | 0.04818 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 0 | 14 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 99.9 | 34.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 34.24 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.3 | 0.08 | 20.23 | 0.2667 |
| utilisation (used / allocatable) | 0.03546 | 0.006111 | 0.04189 | 0.009742 |
| CPU used (cores), mean | 1.702 | 0.2933 | 1.752 | 0.2424 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05528 | 0.03161 |
| CPU used with Omni's own (cores), mean | 1.702 | 0.2933 | 1.808 | 0.274 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.4 | 4201 | 664.8 | 3271 |
| HPA replicas, mean | 3.999 | 4.134 | 4.69 | 4.571 |
| pods started | 0.3 | 1.2 | 3 | 2.6 |
| pod start wait, total (s) | 0.3 | 1.6 | 7 | 3.3 |
| pod start wait, mean (s) | 0.3 | 1.1 | 1.742 | 1.027 |
| host CPU busy, the real machine under kind (%) | 52.06 | 14.9 | 58.39 | 17.54 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 883 | 1507 | 941.3 | 1509 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.402 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1161 | 0.125 | 1163 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1477 | 0.9 | 1479 |
| queue: job turnaround, submitted to done, mean (s) | 192.8 | 1161 | 240.2 | 1163 |
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
| worker nodes in service, mean | 12 | 6.221 | −48.2% | −5.9304 to −5.6273 | yes: GAIN |
| node-hours | 5.03 | 2.61 | −48.1% | −2.4843 to −2.3556 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.9 | 505.5 | +0.1% | −0.9004 to +2.1453 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.9 | 323.6 | −35.9% | −186.1942 to −176.2526 | yes: GAIN |
| response time (ms), mean | 123 | 72.19 | −41.3% | −61.3192 to −40.3329 | yes: GAIN |
| response time (ms), 95th percentile | 171.9 | 97.17 | −43.5% | −89.9624 to −59.4916 | yes: GAIN |
| response time (ms), 99th percentile | 205.4 | 128.4 | −37.5% | −95.2668 to −58.8134 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.6 | +34.600 (native is 0) | +30.9651 to +38.2349 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.2667 | +233.3% | −0.0685 to +0.4418 | no |
| utilisation (used / allocatable) | 0.006111 | 0.009742 | +59.4% | +0.0031 to +0.0041 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2933 | 0.2424 | −17.3% | −0.0562 to −0.0455 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03161 | +0.032 (native is 0) | +0.0276 to +0.0357 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2933 | 0.274 | −6.6% | −0.0235 to −0.0151 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4201 | 3271 | −22.1% | −1025.0809 to −834.9824 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.134 | 4.571 | +10.6% | +0.2261 to +0.6489 | yes: power given |
| pods started | 1.2 | 2.6 | +116.7% | +0.0015 to +2.7985 | yes: power given |
| pod start wait, total (s) | 1.6 | 3.3 | +106.2% | −0.1790 to +3.5790 | no |
| pod start wait, mean (s) | 1.1 | 1.027 | −6.7% | −0.7689 to +0.6222 | no |
| host CPU busy, the real machine under kind (%) | 14.9 | 17.54 | +17.7% | +2.0007 to +3.2833 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1509 | +0.1% | −2.6842 to +7.0842 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1161 | 1163 | +0.2% | −2.5616 to +6.9116 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1477 | 1479 | +0.1% | −2.6491 to +7.0491 | no |
| queue: job turnaround, submitted to done, mean (s) | 1161 | 1163 | +0.2% | −2.5616 to +6.9116 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.017 | 5.03 | +0.3% | +0.0005 to +0.0262 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 504.9 | −3.9% | −23.7300 to −16.7052 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 504.9 | −3.9% | −23.7300 to −16.7052 | yes: GAIN |
| response time (ms), mean | 634.8 | 123 | −80.6% | −821.3113 to −202.1948 | yes: GAIN |
| response time (ms), 95th percentile | 2495 | 171.9 | −93.1% | −3763.2502 to −883.2508 | yes: GAIN |
| response time (ms), 99th percentile | 3357 | 205.4 | −93.9% | −5038.5369 to −1264.4813 | yes: GAIN |
| time over the response line (% of samples) | 22.96 | 0 | −100.0% | −34.2809 to −11.6428 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 0 | −100.0% | −16.6057 to −8.3943 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.3 | 0.08 | −99.5% | −25.2428 to −9.2072 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03546 | 0.006111 | −82.8% | −0.0328 to −0.0259 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.702 | 0.2933 | −82.8% | −1.5765 to −1.2412 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.702 | 0.2933 | −82.8% | −1.5765 to −1.2412 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.4 | 4201 | +456.2% | +3021.3933 to +3870.8174 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.999 | 4.134 | +3.4% | −0.1265 to +0.3957 | no |
| pods started | 0.3 | 1.2 | +300.0% | +0.1887 to +1.6113 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.6 | +433.3% | +0.4047 to +2.1953 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.1 | +266.7% | +0.2111 to +1.3889 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.06 | 14.9 | −71.4% | −42.0966 to −32.2247 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 883 | 1507 | +70.7% | +516.1448 to +731.8552 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1161 | +1638335.3% | +1157.2757 to +1163.6993 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1477 | +246033.3% | +1472.7811 to +1479.6189 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 192.8 | 1161 | +502.0% | +862.7287 to +1072.8463 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.54 | −12.2% | −2.9279 to −0.0002 | yes: GAIN |
| node-hours | 5.017 | 4.419 | −11.9% | −1.2134 to +0.0187 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 527.8 | +0.5% | +1.1341 to +4.3910 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 481.8 | −8.2% | −90.1671 to +3.6422 | no |
| response time (ms), mean | 634.8 | 756.4 | +19.2% | +22.3909 to +220.9565 | yes: LOSS |
| response time (ms), 95th percentile | 2495 | 3165 | +26.8% | +208.3172 to +1130.5948 | yes: LOSS |
| response time (ms), 99th percentile | 3357 | 4198 | +25.1% | +257.6386 to +1424.2278 | yes: LOSS |
| time over the response line (% of samples) | 22.96 | 25.67 | +11.8% | +1.0109 to +4.3992 | yes: LOSS |
| failed requests (%) | 0 | 0.04818 | +0.048 (native is 0) | −0.0255 to +0.1219 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 14 | +12.0% | −1.1174 to +4.1174 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.9 | +99.900 (native is 0) | +36.1609 to +163.6391 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.3 | 20.23 | +16.9% | −1.1416 to +6.9949 | no |
| utilisation (used / allocatable) | 0.03546 | 0.04189 | +18.1% | +0.0014 to +0.0114 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.702 | 1.752 | +2.9% | −0.0332 to +0.1335 | no |
| Omni's own CPU (cores), mean | 0 | 0.05528 | +0.055 (native is 0) | +0.0498 to +0.0608 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.702 | 1.808 | +6.2% | +0.0180 to +0.1929 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.4 | 664.8 | −12.0% | −156.9472 to −24.0778 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.999 | 4.69 | +17.3% | +0.4068 to +0.9752 | yes: power given |
| pods started | 0.3 | 3 | +900.0% | +1.0463 to +4.3537 | yes: power given |
| pod start wait, total (s) | 0.3 | 7 | +2233.3% | +2.5557 to +10.8443 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.742 | +480.6% | +0.4859 to +2.3975 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.06 | 58.39 | +12.2% | +4.4064 to +8.2557 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 883 | 941.3 | +6.6% | +24.1145 to +92.4855 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.402 | −21.7% | −4.9410 to −0.2552 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.125 | +76.5% | +0.0075 to +0.1009 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 192.8 | 240.2 | +24.6% | +17.3804 to +77.5113 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.54 | −12.2% | −2.9279 to −0.0002 | yes: GAIN |
| node-hours | 5.03 | 4.419 | −12.1% | −1.2336 to +0.0122 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.9 | 527.8 | +4.6% | +18.6596 to +27.3006 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.9 | 481.8 | −4.6% | −72.8048 to +26.7150 | no |
| response time (ms), mean | 123 | 756.4 | +514.9% | +231.1473 to +1035.7063 | yes: LOSS |
| response time (ms), 95th percentile | 171.9 | 3165 | +1741.0% | +1141.9153 to +4843.4977 | yes: LOSS |
| response time (ms), 99th percentile | 205.4 | 4198 | +1943.7% | +1596.6033 to +6388.2813 | yes: LOSS |
| time over the response line (% of samples) | 0 | 25.67 | +25.667 (native is 0) | +13.9104 to +37.4234 | yes: LOSS |
| failed requests (%) | 0 | 0.04818 | +0.048 (native is 0) | −0.0255 to +0.1219 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14 | +14.000 (native is 0) | +9.5520 to +18.4480 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 99.9 | +99.900 (native is 0) | +36.1609 to +163.6391 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 20.23 | +25189.6% | +11.0721 to +29.2312 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006111 | 0.04189 | +585.5% | +0.0321 to +0.0394 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2933 | 1.752 | +497.4% | +1.2319 to +1.6862 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05528 | +0.055 (native is 0) | +0.0498 to +0.0608 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2933 | 1.808 | +516.3% | +1.2822 to +1.7465 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4201 | 664.8 | −84.2% | −4021.9874 to −3051.2483 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.134 | 4.69 | +13.5% | +0.2245 to +0.8883 | yes: power given |
| pods started | 1.2 | 3 | +150.0% | +0.2256 to +3.3744 | yes: power given |
| pod start wait, total (s) | 1.6 | 7 | +337.5% | +1.5524 to +9.2476 | yes: LOSS |
| pod start wait, mean (s) | 1.1 | 1.742 | +58.3% | −0.1175 to +1.4008 | no |
| host CPU busy, the real machine under kind (%) | 14.9 | 58.39 | +291.9% | +36.8891 to +50.0943 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 941.3 | −37.5% | −706.7927 to −424.6073 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1161 | 0.125 | −100.0% | −1163.6662 to −1157.2004 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1477 | 0.9 | −99.9% | −1479.1771 to −1472.6229 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1161 | 240.2 | −79.3% | −1053.9496 to −786.7337 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.221 | −48.2% | −5.9304 to −5.6273 | yes: GAIN |
| node-hours | 5.017 | 2.61 | −48.0% | −2.4725 to −2.3407 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.1 | 505.5 | −3.7% | −22.1169 to −17.0733 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.1 | 323.6 | −38.4% | −207.0400 to −195.8419 | yes: GAIN |
| response time (ms), mean | 634.8 | 72.19 | −88.6% | −881.3264 to −243.8319 | yes: GAIN |
| response time (ms), 95th percentile | 2495 | 97.17 | −96.1% | −3848.9012 to −947.0538 | yes: GAIN |
| response time (ms), 99th percentile | 3357 | 128.4 | −96.2% | −5129.5040 to −1327.5944 | yes: GAIN |
| time over the response line (% of samples) | 22.96 | 0 | −100.0% | −34.2809 to −11.6428 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.5 | 0 | −100.0% | −16.6057 to −8.3943 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.6 | +34.600 (native is 0) | +30.9651 to +38.2349 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.3 | 0.2667 | −98.5% | −24.9759 to −9.1007 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03546 | 0.009742 | −72.5% | −0.0288 to −0.0227 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.702 | 0.2424 | −85.8% | −1.6307 to −1.2888 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03161 | +0.032 (native is 0) | +0.0276 to +0.0357 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.702 | 0.274 | −83.9% | −1.5953 to −1.2610 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 755.4 | 3271 | +333.1% | +2162.0147 to +2870.1327 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.999 | 4.571 | +14.3% | +0.2389 to +0.9053 | yes: power given |
| pods started | 0.3 | 2.6 | +766.7% | +0.5790 to +4.0210 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.3 | +1000.0% | +0.7633 to +5.2367 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.027 | +242.2% | −0.0184 to +1.4718 | no |
| host CPU busy, the real machine under kind (%) | 52.06 | 17.54 | −66.3% | −38.9387 to −30.0987 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 883 | 1509 | +70.9% | +521.3713 to +731.0287 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 1163 | +1641405.9% | +1158.9791 to +1166.3459 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 1479 | +246400.0% | +1474.8442 to +1481.9558 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 192.8 | 1163 | +503.2% | +867.8368 to +1072.0882 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*