# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.03 | 10.89 |
| node-hours | 5.029 | 5.025 | 4.214 | 4.569 |
| energy, parked workers still on at idle power (Wh, declared model) | 526 | 526.4 | 528.1 | 527.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526 | 526.4 | 466.2 | 493 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 635.5 | 947.6 | 784.6 | 1157 |
| response time (ms), 95th percentile | 2533 | 3429 | 3246 | 4136 |
| response time (ms), 99th percentile | 3383 | 4602 | 4216 | 5463 |
| time over the response line (% of samples) | 21.43 | 31.73 | 26.64 | 40.53 |
| failed requests (%) | 0.02926 | 0.1171 | 0.03188 | 0.3685 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 14.5 | 13.9 | 18.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 155.5 | 78.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 20.64 | 15.65 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.38 | 30.76 | 30.41 | 52.38 |
| utilisation (used / allocatable) | 0.03494 | 0.036 | 0.04286 | 0.03994 |
| CPU used (cores), mean | 1.677 | 1.728 | 1.709 | 1.737 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05853 | 0.05656 |
| CPU used with Omni's own (cores), mean | 1.677 | 1.728 | 1.767 | 1.794 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.4 | 748.3 | 656.9 | 679.7 |
| HPA replicas, mean | 3.936 | 3.971 | 4.705 | 4.796 |
| pods started | 0 | 0.3 | 3.4 | 3.2 |
| pod start wait, total (s) | 0 | 0.8 | 8.9 | 8.2 |
| pod start wait, mean (s) | 0 | 0.5 | 1.993 | 2.072 |
| host CPU busy, the real machine under kind (%) | 52.01 | 59.02 | 58.88 | 65.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 887.5 | 1015 | 950.3 | 1075 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.49 | 9.535 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 12.41 | 0.1375 | 17.98 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 63.9 | 0.9 | 112 |
| queue: job turnaround, submitted to done, mean (s) | 195 | 286.9 | 251.5 | 360 |
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
| worker nodes in service, mean | 12 | 10.89 | −9.2% | −2.0706 to −0.1463 | yes: GAIN |
| node-hours | 5.025 | 4.569 | −9.1% | −0.8526 to −0.0591 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 527.8 | +0.3% | −1.3615 to +4.2822 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 493 | −6.4% | −61.9624 to −4.8918 | yes: GAIN |
| response time (ms), mean | 947.6 | 1157 | +22.1% | +126.3088 to +292.2247 | yes: LOSS |
| response time (ms), 95th percentile | 3429 | 4136 | +20.6% | +394.5355 to +1019.8655 | yes: LOSS |
| response time (ms), 99th percentile | 4602 | 5463 | +18.7% | +292.5813 to +1430.0027 | yes: LOSS |
| time over the response line (% of samples) | 31.73 | 40.53 | +27.7% | +4.4161 to +13.1853 | yes: LOSS |
| failed requests (%) | 0.1171 | 0.3685 | +214.6% | −0.0436 to +0.5464 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.5 | 18.1 | +24.8% | +0.3273 to +6.8727 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.6 | +78.600 (native is 0) | +38.4915 to +118.7085 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 30.76 | 52.38 | +70.3% | −1.0356 to +44.2589 | no |
| utilisation (used / allocatable) | 0.036 | 0.03994 | +11.0% | −0.0012 to +0.0091 | no |
| CPU used (cores), mean | 1.728 | 1.737 | +0.5% | −0.1158 to +0.1346 | no |
| Omni's own CPU (cores), mean | 0 | 0.05656 | +0.057 (native is 0) | +0.0489 to +0.0643 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.728 | 1.794 | +3.8% | −0.0545 to +0.1865 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 679.7 | −9.2% | −152.4044 to +15.2159 | no |
| HPA replicas, mean | 3.971 | 4.796 | +20.8% | +0.2492 to +1.4003 | yes: power given |
| pods started | 0.3 | 3.2 | +966.7% | +1.3023 to +4.4977 | yes: power given |
| pod start wait, total (s) | 0.8 | 8.2 | +925.0% | +3.2674 to +11.5326 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 2.072 | +314.3% | +0.6486 to +2.4948 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.02 | 65.75 | +11.4% | +5.8908 to +7.5870 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1015 | 1075 | +5.9% | +28.9722 to +90.4278 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.535 | −20.5% | −4.5547 to −0.3751 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 12.41 | 17.98 | +44.9% | −9.4909 to +20.6326 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 63.9 | 112 | +75.3% | −78.4712 to +174.6712 | no |
| queue: job turnaround, submitted to done, mean (s) | 286.9 | 360 | +25.5% | +51.0476 to +95.1524 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.029 | 5.025 | −0.1% | −0.0227 to +0.0160 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526 | 526.4 | +0.1% | −1.1450 to +1.9157 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526 | 526.4 | +0.1% | −1.1450 to +1.9157 | no |
| response time (ms), mean | 635.5 | 947.6 | +49.1% | +119.2594 to +504.9449 | yes: LOSS |
| response time (ms), 95th percentile | 2533 | 3429 | +35.3% | +371.4795 to +1419.3695 | yes: LOSS |
| response time (ms), 99th percentile | 3383 | 4602 | +36.0% | +443.3919 to +1995.0981 | yes: LOSS |
| time over the response line (% of samples) | 21.43 | 31.73 | +48.1% | +6.2105 to +14.3972 | yes: LOSS |
| failed requests (%) | 0.02926 | 0.1171 | +300.3% | −0.0619 to +0.2377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 14.5 | +28.3% | +0.4031 to +5.9969 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.38 | 30.76 | +58.7% | −3.5418 to +26.3018 | no |
| utilisation (used / allocatable) | 0.03494 | 0.036 | +3.0% | −0.0007 to +0.0028 | no |
| CPU used (cores), mean | 1.677 | 1.728 | +3.0% | −0.0339 to +0.1354 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.677 | 1.728 | +3.0% | −0.0339 to +0.1354 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.4 | 748.3 | −3.0% | −51.1706 to +4.9040 | no |
| HPA replicas, mean | 3.936 | 3.971 | +0.9% | −0.1383 to +0.2079 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.5821 to +2.1821 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.2726 to +1.2726 | no |
| host CPU busy, the real machine under kind (%) | 52.01 | 59.02 | +13.5% | +4.7579 to +9.2590 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 887.5 | 1015 | +14.4% | +54.9350 to +199.8650 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 12.41 | +11812.0% | +0.4803 to +24.1280 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 63.9 | +10550.0% | −12.5061 to +139.1061 | no |
| queue: job turnaround, submitted to done, mean (s) | 195 | 286.9 | +47.1% | +37.3615 to +146.4969 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.03 | −16.4% | −3.5371 to −0.3969 | yes: GAIN |
| node-hours | 5.029 | 4.214 | −16.2% | −1.4717 to −0.1578 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526 | 528.1 | +0.4% | +0.8750 to +3.3505 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526 | 466.2 | −11.4% | −109.1748 to −10.5164 | yes: GAIN |
| response time (ms), mean | 635.5 | 784.6 | +23.5% | +39.3394 to +258.8482 | yes: LOSS |
| response time (ms), 95th percentile | 2533 | 3246 | +28.1% | +298.6791 to +1125.9839 | yes: LOSS |
| response time (ms), 99th percentile | 3383 | 4216 | +24.6% | +321.2462 to +1345.0660 | yes: LOSS |
| time over the response line (% of samples) | 21.43 | 26.64 | +24.3% | +3.0969 to +7.3225 | yes: LOSS |
| failed requests (%) | 0.02926 | 0.03188 | +9.0% | −0.0409 to +0.0461 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 13.9 | +23.0% | +0.3330 to +4.8670 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 155.5 | +155.500 (native is 0) | +47.6415 to +263.3585 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.38 | 30.41 | +56.9% | −6.2664 to +28.3264 | no |
| utilisation (used / allocatable) | 0.03494 | 0.04286 | +22.7% | +0.0022 to +0.0136 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.677 | 1.709 | +1.9% | −0.0567 to +0.1199 | no |
| Omni's own CPU (cores), mean | 0 | 0.05853 | +0.059 (native is 0) | +0.0525 to +0.0646 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.677 | 1.767 | +5.4% | +0.0006 to +0.1797 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.4 | 656.9 | −14.8% | −198.9406 to −30.0909 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.936 | 4.705 | +19.5% | +0.3665 to +1.1708 | yes: power given |
| pods started | 0 | 3.4 | +3.400 (native is 0) | +1.7758 to +5.0242 | yes: power given |
| pod start wait, total (s) | 0 | 8.9 | +8.900 (native is 0) | +3.8370 to +13.9630 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.993 | +1.993 (native is 0) | +1.1750 to +2.8103 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.01 | 58.88 | +13.2% | +4.8661 to +8.8803 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 887.5 | 950.3 | +7.1% | +19.9667 to +105.6333 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.49 | −29.3% | −6.1078 to −0.9126 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.1375 | +32.0% | −0.0189 to +0.0855 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 195 | 251.5 | +29.0% | +19.2784 to +93.6716 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.03 | −16.4% | −3.5371 to −0.3969 | yes: GAIN |
| node-hours | 5.025 | 4.214 | −16.1% | −1.4656 to −0.1573 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 528.1 | +0.3% | −0.2638 to +3.7187 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 466.2 | −11.4% | −109.1605 to −11.3013 | yes: GAIN |
| response time (ms), mean | 947.6 | 784.6 | −17.2% | −253.1628 to −72.8539 | yes: GAIN |
| response time (ms), 95th percentile | 3429 | 3246 | −5.3% | −393.7096 to +27.5236 | no |
| response time (ms), 99th percentile | 4602 | 4216 | −8.4% | −868.1602 to +95.9824 | no |
| time over the response line (% of samples) | 31.73 | 26.64 | −16.1% | −8.2401 to −1.9482 | yes: GAIN |
| failed requests (%) | 0.1171 | 0.03188 | −72.8% | −0.2529 to +0.0824 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.5 | 13.9 | −4.1% | −2.3260 to +1.1260 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 155.5 | +155.500 (native is 0) | +47.6415 to +263.3585 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 30.76 | 30.41 | −1.1% | −27.0620 to +26.3620 | no |
| utilisation (used / allocatable) | 0.036 | 0.04286 | +19.1% | +0.0008 to +0.0130 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.728 | 1.709 | −1.1% | −0.1492 to +0.1109 | no |
| Omni's own CPU (cores), mean | 0 | 0.05853 | +0.059 (native is 0) | +0.0525 to +0.0646 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.728 | 1.767 | +2.3% | −0.0921 to +0.1708 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 748.3 | 656.9 | −12.2% | −176.5103 to −6.2546 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.971 | 4.705 | +18.5% | +0.3258 to +1.1418 | yes: power given |
| pods started | 0.3 | 3.4 | +1033.3% | +1.3658 to +4.8342 | yes: power given |
| pod start wait, total (s) | 0.8 | 8.9 | +1012.5% | +2.7106 to +13.4894 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.993 | +298.5% | +0.5216 to +2.4637 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 59.02 | 58.88 | −0.2% | −0.8936 to +0.6231 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1015 | 950.3 | −6.4% | −111.8334 to −17.3666 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.49 | −29.3% | −6.1078 to −0.9126 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 12.41 | 0.1375 | −98.9% | −24.0768 to −0.4649 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 63.9 | 0.9 | −98.6% | −138.9477 to +12.9477 | no |
| queue: job turnaround, submitted to done, mean (s) | 286.9 | 251.5 | −12.4% | −70.5355 to −0.3728 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.89 | −9.2% | −2.0706 to −0.1463 | yes: GAIN |
| node-hours | 5.029 | 4.569 | −9.1% | −0.8607 to −0.0577 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526 | 527.8 | +0.4% | −0.2330 to +3.9244 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526 | 493 | −6.3% | −62.1656 to −3.9180 | yes: GAIN |
| response time (ms), mean | 635.5 | 1157 | +82.0% | +287.4482 to +755.2896 | yes: LOSS |
| response time (ms), 95th percentile | 2533 | 4136 | +63.3% | +1073.0261 to +2132.2239 | yes: LOSS |
| response time (ms), 99th percentile | 3383 | 5463 | +61.5% | +1436.4977 to +2724.5763 | yes: LOSS |
| time over the response line (% of samples) | 21.43 | 40.53 | +89.2% | +15.7008 to +22.5083 | yes: LOSS |
| failed requests (%) | 0.02926 | 0.3685 | +1159.4% | −0.0118 to +0.6904 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 18.1 | +60.2% | +3.9828 to +9.6172 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 78.6 | +78.600 (native is 0) | +38.4915 to +118.7085 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 19.38 | 52.38 | +170.2% | +9.4567 to +56.5266 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03494 | 0.03994 | +14.3% | −0.0001 to +0.0101 | no |
| CPU used (cores), mean | 1.677 | 1.737 | +3.6% | −0.0651 to +0.1855 | no |
| Omni's own CPU (cores), mean | 0 | 0.05656 | +0.057 (native is 0) | +0.0489 to +0.0643 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.677 | 1.794 | +7.0% | −0.0031 to +0.2367 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 771.4 | 679.7 | −11.9% | −182.1205 to −1.3347 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.936 | 4.796 | +21.8% | +0.2592 to +1.4599 | yes: power given |
| pods started | 0 | 3.2 | +3.200 (native is 0) | +1.6256 to +4.7744 | yes: power given |
| pod start wait, total (s) | 0 | 8.2 | +8.200 (native is 0) | +4.0455 to +12.3545 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.072 | +2.072 (native is 0) | +1.2364 to +2.9069 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.01 | 65.75 | +26.4% | +11.5012 to +15.9936 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 887.5 | 1075 | +21.1% | +120.1319 to +254.0681 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.535 | −20.5% | −4.5547 to −0.3751 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 17.98 | +17160.0% | +0.9169 to +34.8331 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 112 | +18566.7% | −4.5000 to +227.3000 | no |
| queue: job turnaround, submitted to done, mean (s) | 195 | 360 | +84.6% | +111.4276 to +218.6308 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*