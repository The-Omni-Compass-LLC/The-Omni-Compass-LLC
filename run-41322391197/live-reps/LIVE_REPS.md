# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.898 | 5.573 |
| node-hours | 2.516 | 2.519 | 2.472 | 2.33 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.4 | 273.9 | 273.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 274.4 | 270.7 | 260.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 421.3 | 391.2 | 381.8 | 352.2 |
| response time (ms), 95th percentile | 1566 | 1640 | 1544 | 1672 |
| response time (ms), 99th percentile | 2174 | 2287 | 2205 | 2463 |
| time over the response line (% of samples) | 18.24 | 13.19 | 17.63 | 12.61 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 8.3 | 10.8 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 36.8 | 35.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.21 | 12.63 | 11.5 | 12.23 |
| utilisation (used / allocatable) | 0.06433 | 0.06397 | 0.06556 | 0.06918 |
| CPU used (cores), mean | 1.544 | 1.535 | 1.545 | 1.542 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01592 | 0.01713 |
| CPU used with Omni's own (cores), mean | 1.544 | 1.535 | 1.561 | 1.56 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.5 | 433.2 | 425.8 | 407.9 |
| HPA replicas, mean | 1.98 | 1.963 | 2.487 | 2.224 |
| pods started | 0.1 | 0.2 | 1.7 | 0.5 |
| pod start wait, total (s) | 0.4 | 0.3 | 3.2 | 1 |
| pod start wait, mean (s) | 0.4 | 0.3 | 1.39 | 1 |
| host CPU busy, the real machine under kind (%) | 43.93 | 44.01 | 44.97 | 45.08 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 806.1 | 808.6 | 810.7 | 812.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.766 | 5.151 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.07917 | 0.0625 | 0.1125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | 0.4 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 111 | 114.4 | 114.8 | 118 |
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
| worker nodes in service, mean | 6 | 5.573 | −7.1% | −0.7523 to −0.1018 | yes: GAIN |
| node-hours | 2.519 | 2.33 | −7.5% | −0.3273 to −0.0505 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.4 | 273.5 | −0.3% | −2.1885 to +0.3579 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.4 | 260.1 | −5.2% | −24.6336 to −3.9553 | yes: GAIN |
| response time (ms), mean | 391.2 | 352.2 | −10.0% | −54.5087 to −23.3689 | yes: GAIN |
| response time (ms), 95th percentile | 1640 | 1672 | +2.0% | −89.3441 to +154.3361 | no |
| response time (ms), 99th percentile | 2287 | 2463 | +7.7% | −19.8989 to +371.5111 | no |
| time over the response line (% of samples) | 13.19 | 12.61 | −4.4% | −1.8568 to +0.6857 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.2 | −1.2% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.5 | +35.500 (native is 0) | +18.4714 to +52.5286 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.63 | 12.23 | −3.1% | −2.5893 to +1.7959 | no |
| utilisation (used / allocatable) | 0.06397 | 0.06918 | +8.1% | +0.0011 to +0.0094 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.535 | 1.542 | +0.5% | −0.0085 to +0.0227 | no |
| Omni's own CPU (cores), mean | 0 | 0.01713 | +0.017 (native is 0) | +0.0160 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.535 | 1.56 | +1.6% | +0.0087 to +0.0397 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.2 | 407.9 | −5.9% | −45.0626 to −5.6299 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 2.224 | +13.3% | +0.1165 to +0.4045 | yes: power given |
| pods started | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.3 | 1 | +233.3% | −0.0578 to +1.4578 | no |
| pod start wait, mean (s) | 0.3 | 1 | +233.3% | −0.0578 to +1.4578 | no |
| host CPU busy, the real machine under kind (%) | 44.01 | 45.08 | +2.4% | +0.8766 to +1.2679 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 808.6 | 812.2 | +0.4% | +0.0442 to +7.1558 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.151 | −14.1% | −1.4759 to −0.2221 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.1125 | +42.1% | −0.0407 to +0.1074 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.5 | −28.6% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 114.4 | 118 | +3.2% | +0.4496 to +6.8504 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.519 | +0.1% | −0.0048 to +0.0108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274.4 | +0.1% | −0.6217 to +1.2183 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 274.4 | +0.1% | −0.6217 to +1.2183 | no |
| response time (ms), mean | 421.3 | 391.2 | −7.1% | −42.3844 to −17.8465 | yes: GAIN |
| response time (ms), 95th percentile | 1566 | 1640 | +4.7% | −56.3097 to +202.6927 | no |
| response time (ms), 99th percentile | 2174 | 2287 | +5.2% | −52.0819 to +279.8093 | no |
| time over the response line (% of samples) | 18.24 | 13.19 | −27.7% | −7.6992 to −2.4026 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 8.3 | −22.4% | −4.4841 to −0.3159 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.21 | 12.63 | +12.6% | −0.6545 to +3.4878 | no |
| utilisation (used / allocatable) | 0.06433 | 0.06397 | −0.6% | −0.0012 to +0.0004 | no |
| CPU used (cores), mean | 1.544 | 1.535 | −0.6% | −0.0277 to +0.0105 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.544 | 1.535 | −0.6% | −0.0277 to +0.0105 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.5 | 433.2 | +0.6% | −3.6596 to +9.1334 | no |
| HPA replicas, mean | 1.98 | 1.963 | −0.8% | −0.1849 to +0.1523 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.4 | 0.3 | −25.0% | −1.1900 to +0.9900 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −1.1900 to +0.9900 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 44.01 | +0.2% | −0.3315 to +0.4841 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.1 | 808.6 | +0.3% | −0.7034 to +5.7034 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.07917 | +72.7% | +0.0059 to +0.0607 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.7 | +133.3% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 111 | 114.4 | +3.1% | −0.5003 to +7.3670 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.898 | −1.7% | −0.1963 to −0.0072 | yes: GAIN |
| node-hours | 2.516 | 2.472 | −1.7% | −0.0839 to −0.0041 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.9 | −0.0% | −0.9988 to +0.7277 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 270.7 | −1.2% | −6.3399 to −0.3313 | yes: GAIN |
| response time (ms), mean | 421.3 | 381.8 | −9.4% | −49.4176 to −29.4761 | yes: GAIN |
| response time (ms), 95th percentile | 1566 | 1544 | −1.4% | −113.6109 to +69.1279 | no |
| response time (ms), 99th percentile | 2174 | 2205 | +1.5% | −109.9116 to +173.1954 | no |
| time over the response line (% of samples) | 18.24 | 17.63 | −3.4% | −1.1900 to −0.0343 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.8 | +0.9% | −0.7564 to +0.9564 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.8 | +36.800 (native is 0) | +20.1853 to +53.4147 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.21 | 11.5 | +2.5% | −1.6248 to +2.1915 | no |
| utilisation (used / allocatable) | 0.06433 | 0.06556 | +1.9% | −0.0002 to +0.0026 | no |
| CPU used (cores), mean | 1.544 | 1.545 | +0.1% | −0.0106 to +0.0127 | no |
| Omni's own CPU (cores), mean | 0 | 0.01592 | +0.016 (native is 0) | +0.0144 to +0.0174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.544 | 1.561 | +1.1% | +0.0044 to +0.0296 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.5 | 425.8 | −1.1% | −11.8778 to +2.5833 | no |
| HPA replicas, mean | 1.98 | 2.487 | +25.6% | +0.0164 to +0.9988 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | −0.5905 to +3.7905 | no |
| pod start wait, total (s) | 0.4 | 3.2 | +700.0% | −1.5288 to +7.1288 | no |
| pod start wait, mean (s) | 0.4 | 1.39 | +247.5% | −0.4761 to +2.4561 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 44.97 | +2.4% | +0.8667 to +1.2147 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.1 | 810.7 | +0.6% | +1.5615 to +7.6385 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.766 | −3.9% | −0.4512 to −0.0168 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.0625 | +36.4% | −0.0121 to +0.0455 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 111 | 114.8 | +3.5% | −0.2325 to +7.9658 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.898 | −1.7% | −0.1963 to −0.0072 | yes: GAIN |
| node-hours | 2.519 | 2.472 | −1.9% | −0.0865 to −0.0075 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.4 | 273.9 | −0.2% | −1.4463 to +0.5785 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.4 | 270.7 | −1.3% | −6.5847 to −0.6831 | yes: GAIN |
| response time (ms), mean | 391.2 | 381.8 | −2.4% | −22.1723 to +3.5096 | no |
| response time (ms), 95th percentile | 1640 | 1544 | −5.8% | −256.6641 to +65.7981 | no |
| response time (ms), 99th percentile | 2287 | 2205 | −3.6% | −246.0307 to +81.5871 | no |
| time over the response line (% of samples) | 13.19 | 17.63 | +33.6% | +2.0601 to +6.8174 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 10.8 | +30.1% | +0.4145 to +4.5855 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.8 | +36.800 (native is 0) | +20.1853 to +53.4147 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.63 | 11.5 | −9.0% | −3.1202 to +0.8536 | no |
| utilisation (used / allocatable) | 0.06397 | 0.06556 | +2.5% | +0.0001 to +0.0030 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.535 | 1.545 | +0.6% | −0.0076 to +0.0270 | no |
| Omni's own CPU (cores), mean | 0 | 0.01592 | +0.016 (native is 0) | +0.0144 to +0.0174 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.535 | 1.561 | +1.7% | +0.0081 to +0.0432 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.2 | 425.8 | −1.7% | −14.6594 to −0.1088 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 2.487 | +26.7% | +0.0350 to +1.0129 | yes: power given |
| pods started | 0.2 | 1.7 | +750.0% | −0.6918 to +3.6918 | no |
| pod start wait, total (s) | 0.3 | 3.2 | +966.7% | −1.2084 to +7.0084 | no |
| pod start wait, mean (s) | 0.3 | 1.39 | +363.3% | +0.3855 to +1.7945 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.01 | 44.97 | +2.2% | +0.6325 to +1.2963 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 808.6 | 810.7 | +0.3% | −0.3882 to +4.5882 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.766 | −3.9% | −0.4512 to −0.0168 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.0625 | −21.1% | −0.0517 to +0.0183 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.4 | −42.9% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 114.4 | 114.8 | +0.4% | −1.9562 to +2.8229 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.573 | −7.1% | −0.7523 to −0.1018 | yes: GAIN |
| node-hours | 2.516 | 2.33 | −7.4% | −0.3239 to −0.0479 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.5 | −0.2% | −1.6136 to +0.3796 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 260.1 | −5.1% | −24.1315 to −3.8608 | yes: GAIN |
| response time (ms), mean | 421.3 | 352.2 | −16.4% | −86.7920 to −51.3166 | yes: GAIN |
| response time (ms), 95th percentile | 1566 | 1672 | +6.7% | −79.0806 to +290.4556 | no |
| response time (ms), 99th percentile | 2174 | 2463 | +13.3% | −18.3944 to +597.7340 | no |
| time over the response line (% of samples) | 18.24 | 12.61 | −30.9% | −8.8122 to −2.4607 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 8.2 | −23.4% | −4.7431 to −0.2569 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.5 | +35.500 (native is 0) | +18.4714 to +52.5286 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.21 | 12.23 | +9.1% | −0.5232 to +2.5632 | no |
| utilisation (used / allocatable) | 0.06433 | 0.06918 | +7.5% | +0.0004 to +0.0093 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.544 | 1.542 | −0.1% | −0.0272 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.01713 | +0.017 (native is 0) | +0.0160 to +0.0183 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.544 | 1.56 | +1.0% | −0.0099 to +0.0410 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.5 | 407.9 | −5.3% | −44.3164 to −0.9024 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.224 | +12.3% | +0.0002 to +0.4883 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.4 | 1 | +150.0% | −0.6251 to +1.8251 | no |
| pod start wait, mean (s) | 0.4 | 1 | +150.0% | −0.6251 to +1.8251 | no |
| host CPU busy, the real machine under kind (%) | 43.93 | 45.08 | +2.6% | +0.7278 to +1.5694 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.1 | 812.2 | +0.8% | +2.0473 to +10.1527 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.151 | −14.1% | −1.4759 to −0.2221 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1125 | +145.5% | −0.0155 to +0.1488 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.5 | +66.7% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 111 | 118 | +6.4% | +2.3144 to +11.8523 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*