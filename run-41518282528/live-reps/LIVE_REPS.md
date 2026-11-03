# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.668 | 5.942 |
| node-hours | 2.515 | 2.513 | 1.96 | 2.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.4 | 272.9 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.4 | 231 | 269.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 360.5 | 135 | 354 | 110.1 |
| response time (ms), 95th percentile | 1308 | 235.1 | 1472 | 244.4 |
| response time (ms), 99th percentile | 1891 | 357 | 2097 | 351.3 |
| time over the response line (% of samples) | 16.7 | 0.2795 | 16.6 | 0.2506 |
| failed requests (%) | 0 | 0 | 0.01111 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 0.1 | 9.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 130.8 | 105.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 20 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.858 | 1110 | 11.76 | 1142 |
| utilisation (used / allocatable) | 0.05909 | 0.05831 | 0.07668 | 0.05788 |
| CPU used (cores), mean | 1.418 | 1.399 | 1.421 | 1.378 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07183 | 0.06959 |
| CPU used with Omni's own (cores), mean | 1.418 | 1.399 | 1.492 | 1.447 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479 | 467.2 | 393 | 469.2 |
| HPA replicas, mean | 2.016 | 1.958 | 2.441 | 2.078 |
| pods started | 0 | 0 | 1.9 | 0.6 |
| pod start wait, total (s) | 0 | 0 | 4.9 | 1.1 |
| pod start wait, mean (s) | 0 | 0 | 1.483 | 0.35 |
| host CPU busy, the real machine under kind (%) | 40.31 | 43.87 | 43.65 | 45.83 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 783.4 | 1391 | 796.2 | 1423 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.785 | 5.258 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 128.6 | 0.07917 | 200.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 607.7 | 0.3 | 779.8 |
| queue: job turnaround, submitted to done, mean (s) | 89.92 | 804.3 | 102.6 | 811.4 |
| queue: jobs unfinished at the window's end | 0 | 11.3 | 0 | 9.8 |
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
| worker nodes in service, mean | 6 | 5.942 | −1.0% | −0.1771 to +0.0618 | no |
| node-hours | 2.513 | 2.492 | −0.8% | −0.0696 to +0.0281 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.5 | +0.1% | −0.9240 to +1.2385 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 269.7 | −0.6% | −5.0367 to +1.7095 | no |
| response time (ms), mean | 135 | 110.1 | −18.4% | −32.0857 to −17.6857 | yes: GAIN |
| response time (ms), 95th percentile | 235.1 | 244.4 | +3.9% | −2.8280 to +21.3200 | no |
| response time (ms), 99th percentile | 357 | 351.3 | −1.6% | −28.2336 to +16.7836 | no |
| time over the response line (% of samples) | 0.2795 | 0.2506 | −10.3% | −0.2171 to +0.1594 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.6 | +105.600 (native is 0) | +89.7151 to +121.4849 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1110 | 1143 | +3.0% | −29.5805 to +95.2171 | no |
| utilisation (used / allocatable) | 0.05831 | 0.05788 | −0.7% | −0.0021 to +0.0012 | no |
| CPU used (cores), mean | 1.399 | 1.378 | −1.5% | −0.0463 to +0.0031 | no |
| Omni's own CPU (cores), mean | 0 | 0.06959 | +0.070 (native is 0) | +0.0615 to +0.0777 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.447 | +3.4% | +0.0289 to +0.0671 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.2 | 469.2 | +0.4% | −10.5476 to +14.6658 | no |
| HPA replicas, mean | 1.958 | 2.078 | +6.1% | −0.0783 to +0.3187 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.7607 to +2.9607 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.350 (native is 0) | −0.1845 to +0.8845 | no |
| host CPU busy, the real machine under kind (%) | 43.87 | 45.83 | +4.5% | +1.2863 to +2.6254 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1391 | 1423 | +2.3% | −9.9997 to +73.3997 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.258 | −12.4% | −3.3831 to +1.8987 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 128.6 | 200.2 | +55.7% | +27.9228 to +115.3522 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 607.7 | 779.8 | +28.3% | +58.2638 to +285.9362 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 804.3 | 811.4 | +0.9% | −48.0841 to +62.2841 | no |
| queue: jobs unfinished at the window's end | 11.3 | 9.8 | −13.3% | −3.2922 to +0.2922 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.513 | −0.1% | −0.0115 to +0.0068 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.4 | −0.3% | −2.7564 to +1.1901 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.4 | −0.3% | −2.7564 to +1.1901 | no |
| response time (ms), mean | 360.5 | 135 | −62.6% | −374.9560 to −76.0697 | yes: GAIN |
| response time (ms), 95th percentile | 1308 | 235.1 | −82.0% | −1794.3374 to −352.0886 | yes: GAIN |
| response time (ms), 99th percentile | 1891 | 357 | −81.1% | −2530.9153 to −536.8265 | yes: GAIN |
| time over the response line (% of samples) | 16.7 | 0.2795 | −98.3% | −27.7644 to −5.0857 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 0.1 | −98.8% | −12.8622 to −3.7378 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.858 | 1110 | +12427.0% | +768.5718 to +1433.0748 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05909 | 0.05831 | −1.3% | −0.0074 to +0.0058 | no |
| CPU used (cores), mean | 1.418 | 1.399 | −1.3% | −0.1772 to +0.1398 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.418 | 1.399 | −1.3% | −0.1772 to +0.1398 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479 | 467.2 | −2.5% | −65.5224 to +41.9211 | no |
| HPA replicas, mean | 2.016 | 1.958 | −2.9% | −0.1885 to +0.0728 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 40.31 | 43.87 | +8.8% | +0.1386 to +6.9754 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 1391 | +77.6% | +482.5657 to +733.0343 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 128.6 | +257058.3% | +85.1152 to +171.9431 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 607.7 | +202466.7% | +406.8246 to +807.9754 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.92 | 804.3 | +794.4% | +544.4531 to +884.2969 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.3 | +11.300 (native is 0) | +4.6661 to +17.9339 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.668 | −22.2% | −2.1259 to −0.5377 | yes: GAIN |
| node-hours | 2.515 | 1.96 | −22.1% | −0.8927 to −0.2172 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.9 | +0.3% | −0.4640 to +1.9733 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 231 | −15.1% | −66.6914 to −15.6702 | yes: GAIN |
| response time (ms), mean | 360.5 | 354 | −1.8% | −26.0537 to +13.0160 | no |
| response time (ms), 95th percentile | 1308 | 1472 | +12.5% | +45.2488 to +281.1002 | yes: LOSS |
| response time (ms), 99th percentile | 1891 | 2097 | +10.9% | +38.9314 to +374.1710 | yes: LOSS |
| time over the response line (% of samples) | 16.7 | 16.6 | −0.6% | −0.7138 to +0.5133 | no |
| failed requests (%) | 0 | 0.01111 | +0.011 (native is 0) | −0.0140 to +0.0362 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.1 | +8.3% | −0.1953 to +1.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.8 | +130.800 (native is 0) | +60.1757 to +201.4243 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.858 | 11.76 | +32.8% | +1.4179 to +4.3888 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05909 | 0.07668 | +29.8% | +0.0068 to +0.0284 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.418 | 1.421 | +0.2% | −0.0396 to +0.0447 | no |
| Omni's own CPU (cores), mean | 0 | 0.07183 | +0.072 (native is 0) | +0.0647 to +0.0790 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.492 | +5.2% | +0.0287 to +0.1201 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479 | 393 | −18.0% | −148.8267 to −23.2366 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.441 | +21.1% | +0.1615 to +0.6879 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.4129 to +3.3871 | yes: power given |
| pod start wait, total (s) | 0 | 4.9 | +4.900 (native is 0) | +0.8333 to +8.9667 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.483 | +1.483 (native is 0) | +0.5574 to +2.4093 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.31 | 43.65 | +8.3% | +2.7954 to +3.8778 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 796.2 | +1.6% | +3.2996 to +22.3004 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.785 | −36.9% | −3.2049 to −1.2244 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.07917 | +58.3% | −0.0412 to +0.0995 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 89.92 | 102.6 | +14.1% | +2.3320 to +23.0096 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.668 | −22.2% | −2.1259 to −0.5377 | yes: GAIN |
| node-hours | 2.513 | 1.96 | −22.0% | −0.8853 to −0.2200 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 272.9 | +0.6% | −0.9559 to +4.0314 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 231 | −14.9% | −67.1472 to −13.6482 | yes: GAIN |
| response time (ms), mean | 135 | 354 | +162.2% | +62.5548 to +375.4331 | yes: LOSS |
| response time (ms), 95th percentile | 235.1 | 1472 | +525.8% | +446.6590 to +2026.1160 | yes: LOSS |
| response time (ms), 99th percentile | 357 | 2097 | +487.5% | +620.6910 to +2860.1532 | yes: LOSS |
| time over the response line (% of samples) | 0.2795 | 16.6 | +5841.0% | +5.4661 to +27.1836 | yes: LOSS |
| failed requests (%) | 0 | 0.01111 | +0.011 (native is 0) | −0.0140 to +0.0362 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 9.1 | +9000.0% | +4.4760 to +13.5240 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.8 | +130.800 (native is 0) | +60.1757 to +201.4243 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1110 | 11.76 | −98.9% | −1429.3659 to −766.4741 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05831 | 0.07668 | +31.5% | +0.0116 to +0.0252 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.399 | 1.421 | +1.5% | −0.1450 to +0.1874 | no |
| Omni's own CPU (cores), mean | 0 | 0.07183 | +0.072 (native is 0) | +0.0647 to +0.0790 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.399 | 1.492 | +6.6% | −0.0795 to +0.2656 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.2 | 393 | −15.9% | −101.3743 to −47.0876 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.958 | 2.441 | +24.6% | +0.2333 to +0.7318 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.4129 to +3.3871 | yes: power given |
| pod start wait, total (s) | 0 | 4.9 | +4.900 (native is 0) | +0.8333 to +8.9667 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.483 | +1.483 (native is 0) | +0.5574 to +2.4093 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.87 | 43.65 | −0.5% | −3.8164 to +3.3757 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1391 | 796.2 | −42.8% | −716.8992 to −473.1008 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.034 | −66.1% | −4.0444 to −3.8867 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 128.6 | 0.07917 | −99.9% | −171.8788 to −85.1212 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 607.7 | 0.3 | −100.0% | −808.0712 to −406.7288 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 804.3 | 102.6 | −87.2% | −864.3811 to −539.0272 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.3 | 0 | −100.0% | −17.9339 to −4.6661 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.942 | −1.0% | −0.1771 to +0.0618 | no |
| node-hours | 2.515 | 2.492 | −0.9% | −0.0723 to +0.0261 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.5 | −0.2% | −3.2937 to +2.0419 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 269.7 | −0.9% | −6.1837 to +1.2903 | no |
| response time (ms), mean | 360.5 | 110.1 | −69.5% | −402.2729 to −98.5242 | yes: GAIN |
| response time (ms), 95th percentile | 1308 | 244.4 | −81.3% | −1777.3899 to −350.5441 | yes: GAIN |
| response time (ms), 99th percentile | 1891 | 351.3 | −81.4% | −2532.3749 to −546.8169 | yes: GAIN |
| time over the response line (% of samples) | 16.7 | 0.2506 | −98.5% | −27.7745 to −5.1333 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 0 | −100.0% | −13.0382 to −3.7618 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.6 | +105.600 (native is 0) | +89.7151 to +121.4849 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.858 | 1143 | +12797.5% | +834.0938 to +1433.1895 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05909 | 0.05788 | −2.0% | −0.0089 to +0.0065 | no |
| CPU used (cores), mean | 1.418 | 1.378 | −2.8% | −0.2181 to +0.1375 | no |
| Omni's own CPU (cores), mean | 0 | 0.06959 | +0.070 (native is 0) | +0.0615 to +0.0777 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.418 | 1.447 | +2.1% | −0.1412 to +0.1998 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 479 | 469.2 | −2.0% | −72.3842 to +52.9011 | no |
| HPA replicas, mean | 2.016 | 2.078 | +3.1% | −0.1309 to +0.2556 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.3656 to +1.5656 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.7607 to +2.9607 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.350 (native is 0) | −0.1845 to +0.8845 | no |
| host CPU busy, the real machine under kind (%) | 40.31 | 45.83 | +13.7% | +1.8633 to +9.1624 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 1423 | +81.6% | +552.3530 to +726.6470 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.258 | −12.4% | −3.3831 to +1.8987 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 200.2 | +400333.3% | +127.6765 to +272.6568 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 779.8 | +259833.3% | +558.0207 to +1000.9793 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 89.92 | 811.4 | +802.3% | +586.4808 to +856.4692 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.8 | +9.800 (native is 0) | +3.8458 to +15.7542 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*