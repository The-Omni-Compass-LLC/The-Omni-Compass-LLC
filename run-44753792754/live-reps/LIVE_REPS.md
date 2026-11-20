# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.192 | 6 |
| node-hours | 2.516 | 2.517 | 1.761 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 272.4 | 270.2 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 272.4 | 213.3 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 162 | 120.6 | 137.8 | 121.8 |
| response time (ms), 95th percentile | 395.8 | 207.6 | 435 | 214.6 |
| response time (ms), 99th percentile | 572.8 | 306.5 | 628.2 | 309.1 |
| time over the response line (% of samples) | 2.663 | 0.06064 | 3.418 | 0.1289 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 0 | 6.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 226.5 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.722 | 924.7 | 6.3 | 1037 |
| utilisation (used / allocatable) | 0.05258 | 0.06075 | 0.07605 | 0.05855 |
| CPU used (cores), mean | 1.262 | 1.458 | 1.243 | 1.405 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06969 | 0.0592 |
| CPU used with Omni's own (cores), mean | 1.262 | 1.458 | 1.313 | 1.464 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 511.9 | 445.7 | 407.4 | 461.1 |
| HPA replicas, mean | 2.035 | 1.997 | 2.286 | 2.119 |
| pods started | 0 | 0.1 | 1.5 | 0.9 |
| pod start wait, total (s) | 0 | 0.2 | 2.8 | 2.1 |
| pod start wait, mean (s) | 0 | 0.2 | 1.1 | 0.8167 |
| host CPU busy, the real machine under kind (%) | 36.83 | 44.27 | 39.56 | 45.59 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 725.1 | 1455 | 727.1 | 1488 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.001 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0125 | 135.8 | 0.02917 | 151.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 588.2 | 0 | 726.1 |
| queue: job turnaround, submitted to done, mean (s) | 30.44 | 729.5 | 32.04 | 777.7 |
| queue: jobs unfinished at the window's end | 0 | 4.4 | 0 | 8.3 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.515 | −0.1% | −0.0087 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.5 | −0.4% | −1.8273 to −0.1475 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.5 | −0.4% | −1.8273 to −0.1475 | yes: GAIN |
| response time (ms), mean | 120.6 | 121.8 | +0.9% | −2.4621 to +4.7468 | no |
| response time (ms), 95th percentile | 207.6 | 214.6 | +3.4% | −3.3974 to +17.4144 | no |
| response time (ms), 99th percentile | 306.5 | 309.1 | +0.8% | −20.8474 to +25.9954 | no |
| time over the response line (% of samples) | 0.06064 | 0.1289 | +112.5% | −0.0289 to +0.1654 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +25.4595 to +42.1405 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 924.7 | 1037 | +12.2% | +33.4561 to +191.5472 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06075 | 0.05855 | −3.6% | −0.0034 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.458 | 1.405 | −3.6% | −0.0827 to −0.0231 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0592 | +0.059 (native is 0) | +0.0561 to +0.0623 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.458 | 1.464 | +0.4% | −0.0238 to +0.0363 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.7 | 461.1 | +3.4% | +6.5821 to +24.1599 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.119 | +6.1% | −0.0742 to +0.3178 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.3081 to +1.9081 | no |
| pod start wait, total (s) | 0.2 | 2.1 | +950.0% | −0.8898 to +4.6898 | no |
| pod start wait, mean (s) | 0.2 | 0.8167 | +308.3% | −0.4105 to +1.6438 | no |
| host CPU busy, the real machine under kind (%) | 44.27 | 45.59 | +3.0% | +0.7501 to +1.8880 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 1488 | +2.3% | −18.1670 to +84.5670 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 135.8 | 151.5 | +11.5% | −10.6716 to +42.0049 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 588.2 | 726.1 | +23.4% | −2.4386 to +278.2386 | no |
| queue: job turnaround, submitted to done, mean (s) | 729.5 | 777.7 | +6.6% | −1.6120 to +97.8620 | no |
| queue: jobs unfinished at the window's end | 4.4 | 8.3 | +88.6% | +1.0101 to +6.7899 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.517 | +0.0% | −0.0083 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 272.4 | +1.0% | +1.1180 to +4.1866 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 272.4 | +1.0% | +1.1180 to +4.1866 | yes: power given |
| response time (ms), mean | 162 | 120.6 | −25.6% | −52.9770 to −29.8513 | yes: GAIN |
| response time (ms), 95th percentile | 395.8 | 207.6 | −47.6% | −238.7880 to −137.6560 | yes: GAIN |
| response time (ms), 99th percentile | 572.8 | 306.5 | −46.5% | −327.6018 to −204.9150 | yes: GAIN |
| time over the response line (% of samples) | 2.663 | 0.06064 | −97.7% | −4.0472 to −1.1571 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 0 | −100.0% | −8.9596 to −2.6404 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.722 | 924.7 | +13657.3% | +764.8871 to +1071.1096 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05258 | 0.06075 | +15.6% | +0.0059 to +0.0105 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.262 | 1.458 | +15.6% | +0.1408 to +0.2517 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.262 | 1.458 | +15.6% | +0.1408 to +0.2517 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 511.9 | 445.7 | −12.9% | −87.3826 to −44.9623 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.035 | 1.997 | −1.9% | −0.1856 to +0.1094 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 36.83 | 44.27 | +20.2% | +6.3457 to +8.5411 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 725.1 | 1455 | +100.7% | +655.2168 to +805.1832 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0125 | 135.8 | +1086333.3% | +107.7439 to +163.8394 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 588.2 | +588.200 (native is 0) | +490.7758 to +685.6242 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 30.44 | 729.5 | +2296.5% | +601.4399 to +796.7518 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 4.4 | +4.400 (native is 0) | +0.3649 to +8.4351 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.192 | −30.1% | −2.4031 to −1.2129 | yes: GAIN |
| node-hours | 2.516 | 1.761 | −30.0% | −1.0064 to −0.5033 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 270.2 | +0.1% | −0.6456 to +1.4194 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 213.3 | −21.0% | −75.6372 to −37.4223 | yes: GAIN |
| response time (ms), mean | 162 | 137.8 | −15.0% | −35.4571 to −13.0210 | yes: GAIN |
| response time (ms), 95th percentile | 395.8 | 435 | +9.9% | −14.8270 to +93.1850 | no |
| response time (ms), 99th percentile | 572.8 | 628.2 | +9.7% | −7.2387 to +118.0389 | no |
| time over the response line (% of samples) | 2.663 | 3.418 | +28.4% | −0.5348 to +2.0454 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 6.3 | +8.6% | −1.1259 to +2.1259 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 226.5 | +226.500 (native is 0) | +174.2665 to +278.7335 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.722 | 6.3 | −6.3% | −1.3980 to +0.5546 | no |
| utilisation (used / allocatable) | 0.05258 | 0.07605 | +44.6% | +0.0139 to +0.0330 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.262 | 1.243 | −1.5% | −0.0482 to +0.0113 | no |
| Omni's own CPU (cores), mean | 0 | 0.06969 | +0.070 (native is 0) | +0.0662 to +0.0731 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.262 | 1.313 | +4.1% | +0.0203 to +0.0822 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 511.9 | 407.4 | −20.4% | −142.2021 to −66.7940 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.035 | 2.286 | +12.3% | −0.1081 to +0.6095 | no |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.3690 to +2.6310 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.5430 to +5.0570 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | +0.4038 to +1.7962 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.83 | 39.56 | +7.4% | +2.0290 to +3.4437 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 725.1 | 727.1 | +0.3% | −0.7601 to +4.7601 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.001 | −50.0% | −3.7231 to −2.2748 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0125 | 0.02917 | +133.3% | +0.0013 to +0.0321 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 30.44 | 32.04 | +5.2% | −1.3872 to +4.5789 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.192 | −30.1% | −2.4031 to −1.2129 | yes: GAIN |
| node-hours | 2.517 | 1.761 | −30.0% | −1.0090 to −0.5031 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 270.2 | −0.8% | −3.5632 to −0.9675 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 213.3 | −21.7% | −78.7768 to −39.5873 | yes: GAIN |
| response time (ms), mean | 120.6 | 137.8 | +14.2% | +2.3180 to +32.0323 | yes: LOSS |
| response time (ms), 95th percentile | 207.6 | 435 | +109.5% | +155.6010 to +299.2010 | yes: LOSS |
| response time (ms), 99th percentile | 306.5 | 628.2 | +104.9% | +234.5690 to +408.7480 | yes: LOSS |
| time over the response line (% of samples) | 0.06064 | 3.418 | +5537.0% | +1.0712 to +5.6436 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 6.3 | +6.300 (native is 0) | +3.6438 to +8.9562 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 226.5 | +226.500 (native is 0) | +174.2665 to +278.7335 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 924.7 | 6.3 | −99.3% | −1071.3276 to −765.5124 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06075 | 0.07605 | +25.2% | +0.0068 to +0.0238 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.458 | 1.243 | −14.7% | −0.2775 to −0.1519 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06969 | +0.070 (native is 0) | +0.0662 to +0.0731 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.458 | 1.313 | −9.9% | −0.2093 to −0.0807 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.7 | 407.4 | −8.6% | −65.7422 to −10.9090 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.286 | +14.5% | +0.0129 to +0.5648 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.1749 to +2.6251 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.8 | +1300.0% | +0.1638 to +5.0362 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.1 | +450.0% | −0.0693 to +1.8693 | no |
| host CPU busy, the real machine under kind (%) | 44.27 | 39.56 | −10.6% | −5.8540 to −3.5601 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 727.1 | −50.0% | −802.6239 to −653.7761 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.177 | −63.7% | −4.3864 to −3.2594 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 135.8 | 0.02917 | −100.0% | −163.8205 to −107.7295 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 588.2 | 0 | −100.0% | −685.6242 to −490.7758 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 729.5 | 32.04 | −95.6% | −793.5991 to −601.4009 | yes: GAIN |
| queue: jobs unfinished at the window's end | 4.4 | 0 | −100.0% | −8.4351 to −0.3649 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.515 | −0.0% | −0.0091 to +0.0078 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 269.8 | 271.5 | +0.6% | +0.4400 to +2.8897 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 269.8 | 271.5 | +0.6% | +0.4400 to +2.8897 | yes: power given |
| response time (ms), mean | 162 | 121.8 | −24.9% | −51.3310 to −29.2126 | yes: GAIN |
| response time (ms), 95th percentile | 395.8 | 214.6 | −45.8% | −229.2429 to −133.1841 | yes: GAIN |
| response time (ms), 99th percentile | 572.8 | 309.1 | −46.0% | −330.3642 to −197.0046 | yes: GAIN |
| time over the response line (% of samples) | 2.663 | 0.1289 | −95.2% | −3.9801 to −1.0877 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 0 | −100.0% | −8.9596 to −2.6404 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +25.4595 to +42.1405 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 6.722 | 1037 | +15331.0% | +904.2315 to +1156.7685 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05258 | 0.05855 | +11.4% | +0.0037 to +0.0082 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.262 | 1.405 | +11.4% | +0.0895 to +0.1970 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0592 | +0.059 (native is 0) | +0.0561 to +0.0623 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.262 | 1.464 | +16.0% | +0.1507 to +0.2543 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 511.9 | 461.1 | −9.9% | −71.6338 to −29.9691 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.035 | 2.119 | +4.1% | −0.2009 to +0.3683 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.1366 to +1.9366 | no |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | −0.5647 to +4.7647 | no |
| pod start wait, mean (s) | 0 | 0.8167 | +0.817 (native is 0) | +0.0014 to +1.6320 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 36.83 | 45.59 | +23.8% | +7.5749 to +9.9499 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 725.1 | 1488 | +105.3% | +713.7318 to +813.0682 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0125 | 151.5 | +1211666.7% | +129.2551 to +173.6616 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 726.1 | +726.100 (native is 0) | +610.8556 to +841.3444 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 30.44 | 777.7 | +2454.6% | +668.2481 to +826.1935 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.3 | +8.300 (native is 0) | +4.8770 to +11.7230 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*