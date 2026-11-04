# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.355 | 6 |
| node-hours | 2.512 | 2.514 | 2.247 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.5 | 273.4 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.5 | 253.1 | 271.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 370.9 | 143.3 | 356.7 | 119 |
| response time (ms), 95th percentile | 1343 | 245.6 | 1497 | 258.5 |
| response time (ms), 99th percentile | 1892 | 361.2 | 2085 | 365.8 |
| time over the response line (% of samples) | 16.51 | 0.1691 | 17.06 | 0.3024 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 0 | 10.8 | 0.5556 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 143.4 | 107.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.47 | 1202 | 11.41 | 1272 |
| utilisation (used / allocatable) | 0.06105 | 0.06062 | 0.07038 | 0.05849 |
| CPU used (cores), mean | 1.465 | 1.455 | 1.482 | 1.404 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07445 | 0.07069 |
| CPU used with Omni's own (cores), mean | 1.465 | 1.455 | 1.557 | 1.474 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.2 | 447.4 | 411.3 | 461.8 |
| HPA replicas, mean | 1.998 | 2.065 | 2.654 | 2.153 |
| pods started | 0.1 | 0.1 | 2.1 | 0.2222 |
| pod start wait, total (s) | 0.3 | 0.1 | 5.4 | 0.4444 |
| pod start wait, mean (s) | 0.3 | 0.1 | 2.07 | 0.2222 |
| host CPU busy, the real machine under kind (%) | 42.03 | 45.87 | 45.25 | 47.08 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 782.7 | 1493 | 792.3 | 1484 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.937 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 164.1 | 0.04583 | 190.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 735.3 | 0.3 | 775.3 |
| queue: job turnaround, submitted to done, mean (s) | 89.47 | 904.8 | 98.41 | 887.2 |
| queue: jobs unfinished at the window's end | 0 | 12.9 | 0 | 12.67 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.511 | −0.2% | −0.0151 to +0.0054 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 271.1 | −0.5% | −2.5379 to −0.1760 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 271.1 | −0.5% | −2.5379 to −0.1760 | yes: GAIN |
| response time (ms), mean | 141.7 | 119 | −16.0% | −32.2210 to −13.2459 | yes: GAIN |
| response time (ms), 95th percentile | 242.8 | 258.5 | +6.5% | −5.6234 to +37.0879 | no |
| response time (ms), 99th percentile | 357.2 | 365.8 | +2.4% | −21.3688 to +38.7062 | no |
| time over the response line (% of samples) | 0.1793 | 0.3024 | +68.7% | −0.1673 to +0.4136 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.5556 | +0.556 (native is 0) | −0.4693 to +1.5804 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.2 | +107.222 (native is 0) | +91.7160 to +122.7284 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1185 | 1272 | +7.3% | −7.9377 to +181.5451 | no |
| utilisation (used / allocatable) | 0.06022 | 0.05849 | −2.9% | −0.0033 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.445 | 1.404 | −2.9% | −0.0798 to −0.0032 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07069 | +0.071 (native is 0) | +0.0623 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.474 | +2.0% | −0.0042 to +0.0625 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 461.8 | +2.6% | +0.5787 to +23.0802 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.053 | 2.153 | +4.9% | −0.0125 to +0.2131 | no |
| pods started | 0.1111 | 0.2222 | +100.0% | −0.4898 to +0.7120 | no |
| pod start wait, total (s) | 0.1111 | 0.4444 | +300.0% | −0.7537 to +1.4204 | no |
| pod start wait, mean (s) | 0.1111 | 0.2222 | +100.0% | −0.4898 to +0.7120 | no |
| host CPU busy, the real machine under kind (%) | 45.66 | 47.08 | +3.1% | +0.9110 to +1.9361 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1491 | 1484 | −0.5% | −16.8057 to +1.2502 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 158 | 190.7 | +20.7% | −17.7548 to +83.2270 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 710 | 775.3 | +9.2% | −169.1384 to +299.8050 | no |
| queue: job turnaround, submitted to done, mean (s) | 895.4 | 887.2 | −0.9% | −53.6085 to +37.3215 | no |
| queue: jobs unfinished at the window's end | 12.44 | 12.67 | +1.8% | −1.4870 to +1.9314 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.514 | +0.1% | −0.0086 to +0.0132 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.5 | +0.0% | −1.2622 to +1.2872 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.5 | +0.0% | −1.2622 to +1.2872 | no |
| response time (ms), mean | 370.9 | 143.3 | −61.4% | −371.9019 to −83.2105 | yes: GAIN |
| response time (ms), 95th percentile | 1343 | 245.6 | −81.7% | −1796.4302 to −398.1208 | yes: GAIN |
| response time (ms), 99th percentile | 1892 | 361.2 | −80.9% | −2499.8952 to −561.3954 | yes: GAIN |
| time over the response line (% of samples) | 16.51 | 0.1691 | −99.0% | −27.1576 to −5.5277 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 0 | −100.0% | −12.9898 to −5.0102 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.47 | 1202 | +12597.8% | +1020.4813 to +1365.5420 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06105 | 0.06062 | −0.7% | −0.0059 to +0.0050 | no |
| CPU used (cores), mean | 1.465 | 1.455 | −0.7% | −0.1418 to +0.1212 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.465 | 1.455 | −0.7% | −0.1418 to +0.1212 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.2 | 447.4 | −1.1% | −43.2602 to +33.6954 | no |
| HPA replicas, mean | 1.998 | 2.065 | +3.3% | −0.0884 to +0.2213 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| pod start wait, mean (s) | 0.3 | 0.1 | −66.7% | −0.9388 to +0.5388 | no |
| host CPU busy, the real machine under kind (%) | 42.03 | 45.87 | +9.2% | +0.7211 to +6.9728 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.7 | 1493 | +90.7% | +664.4744 to +755.5256 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 164.1 | +302769.2% | +123.9680 to +204.0320 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 735.3 | +183725.0% | +569.6341 to +900.1659 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.47 | 904.8 | +911.3% | +749.0609 to +881.6557 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.9 | +12.900 (native is 0) | +8.2222 to +17.5778 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.355 | −10.7% | −1.2706 to −0.0189 | yes: GAIN |
| node-hours | 2.512 | 2.247 | −10.6% | −0.5319 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 273.4 | +0.3% | −0.3481 to +2.0141 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 253.1 | −7.1% | −39.7959 to +0.9494 | no |
| response time (ms), mean | 370.9 | 356.7 | −3.8% | −37.6948 to +9.3742 | no |
| response time (ms), 95th percentile | 1343 | 1497 | +11.5% | +3.9392 to +304.0008 | yes: LOSS |
| response time (ms), 99th percentile | 1892 | 2085 | +10.2% | +10.8783 to +375.3561 | yes: LOSS |
| time over the response line (% of samples) | 16.51 | 17.06 | +3.3% | −0.2348 to +1.3329 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9 | 10.8 | +20.0% | +0.4597 to +3.1403 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.4 | +143.400 (native is 0) | +73.0423 to +213.7577 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.47 | 11.41 | +20.5% | +0.0822 to +3.8011 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06105 | 0.07038 | +15.3% | +0.0005 to +0.0182 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.465 | 1.482 | +1.2% | −0.0120 to +0.0460 | no |
| Omni's own CPU (cores), mean | 0 | 0.07445 | +0.074 (native is 0) | +0.0675 to +0.0814 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.465 | 1.557 | +6.2% | +0.0600 to +0.1229 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.2 | 411.3 | −9.0% | −76.2915 to −5.3506 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.654 | +32.8% | +0.2699 to +1.0427 | yes: power given |
| pods started | 0.1 | 2.1 | +2000.0% | +0.9884 to +3.0116 | yes: power given |
| pod start wait, total (s) | 0.3 | 5.4 | +1700.0% | +1.5884 to +8.6116 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.07 | +590.0% | +0.6994 to +2.8406 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.03 | 45.25 | +7.7% | +2.7347 to +3.7148 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.7 | 792.3 | +1.2% | −1.5592 to +20.7592 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.937 | −17.7% | −1.9560 to −0.1696 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.04583 | −15.4% | −0.0476 to +0.0309 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.47 | 98.41 | +10.0% | −1.3579 to +19.2246 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.355 | −10.7% | −1.2706 to −0.0189 | yes: GAIN |
| node-hours | 2.514 | 2.247 | −10.6% | −0.5286 to −0.0063 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 273.4 | +0.3% | −1.3133 to +2.9543 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 253.1 | −7.1% | −40.1884 to +1.3169 | no |
| response time (ms), mean | 143.3 | 356.7 | +148.9% | +59.8695 to +366.9223 | yes: LOSS |
| response time (ms), 95th percentile | 245.6 | 1497 | +509.5% | +458.3407 to +2044.1503 | yes: LOSS |
| response time (ms), 99th percentile | 361.2 | 2085 | +477.2% | +637.0154 to +2810.5096 | yes: LOSS |
| time over the response line (% of samples) | 0.1691 | 17.06 | +9991.3% | +6.4247 to +27.3587 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.8 | +10.800 (native is 0) | +7.4996 to +14.1004 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.4 | +143.400 (native is 0) | +73.0423 to +213.7577 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1202 | 11.41 | −99.1% | −1363.1051 to −1019.0349 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06062 | 0.07038 | +16.1% | +0.0018 to +0.0177 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.455 | 1.482 | +1.9% | −0.1185 to +0.1732 | no |
| Omni's own CPU (cores), mean | 0 | 0.07445 | +0.074 (native is 0) | +0.0675 to +0.0814 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.455 | 1.557 | +7.0% | −0.0503 to +0.2538 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.4 | 411.3 | −8.1% | −68.6087 to −3.4687 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.065 | 2.654 | +28.6% | +0.2400 to +0.9397 | yes: power given |
| pods started | 0.1 | 2.1 | +2000.0% | +0.9884 to +3.0116 | yes: power given |
| pod start wait, total (s) | 0.1 | 5.4 | +5300.0% | +1.9441 to +8.6559 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.07 | +1970.0% | +1.2281 to +2.7119 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.87 | 45.25 | −1.4% | −4.0421 to +2.7978 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1493 | 792.3 | −46.9% | −751.7143 to −649.0857 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 164.1 | 0.04583 | −100.0% | −204.0233 to −123.9933 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 735.3 | 0.3 | −100.0% | −900.2760 to −569.7240 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 904.8 | 98.41 | −89.1% | −868.8669 to −743.9831 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.9 | 0 | −100.0% | −17.5778 to −8.2222 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.511 | −0.1% | −0.0089 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.1 | −0.4% | −3.1212 to +0.9769 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.1 | −0.4% | −3.1212 to +0.9769 | no |
| response time (ms), mean | 347.1 | 119 | −65.7% | −382.7535 to −73.5413 | yes: GAIN |
| response time (ms), 95th percentile | 1238 | 258.5 | −79.1% | −1716.8611 to −242.6667 | yes: GAIN |
| response time (ms), 99th percentile | 1724 | 365.8 | −78.8% | −2372.0902 to −343.8744 | yes: GAIN |
| time over the response line (% of samples) | 14.88 | 0.3024 | −98.0% | −26.1038 to −3.0600 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.444 | 0.5556 | −93.4% | −12.0184 to −3.7594 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.2 | +107.222 (native is 0) | +91.7160 to +122.7284 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.274 | 1272 | +13616.6% | +1029.3571 to +1496.2762 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06013 | 0.05849 | −2.7% | −0.0086 to +0.0053 | no |
| CPU used (cores), mean | 1.443 | 1.404 | −2.7% | −0.2069 to +0.1278 | no |
| Omni's own CPU (cores), mean | 0 | 0.07069 | +0.071 (native is 0) | +0.0623 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.474 | +2.2% | −0.1280 to +0.1903 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.4 | 461.8 | +0.7% | −45.5273 to +52.2253 | no |
| HPA replicas, mean | 2.003 | 2.153 | +7.5% | −0.0417 to +0.3431 | no |
| pods started | 0.1111 | 0.2222 | +100.0% | −0.1451 to +0.3673 | no |
| pod start wait, total (s) | 0.3333 | 0.4444 | +33.3% | −0.1451 to +0.3673 | no |
| pod start wait, mean (s) | 0.3333 | 0.2222 | −33.3% | −0.3673 to +0.1451 | no |
| host CPU busy, the real machine under kind (%) | 41.41 | 47.08 | +13.7% | +2.2154 to +9.1196 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.1 | 1484 | +91.2% | +651.2277 to +763.6611 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06019 | 190.7 | +316800.0% | +148.4666 to +232.8668 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4444 | 775.3 | +174350.0% | +642.9929 to +906.7849 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.72 | 887.2 | +972.6% | +736.1162 to +872.8930 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.67 | +12.667 (native is 0) | +7.5390 to +17.7943 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*