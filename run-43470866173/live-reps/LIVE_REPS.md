# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.183 | 6 |
| node-hours | 2.519 | 2.513 | 2.17 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.3 | 272.2 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.3 | 246.6 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 340 | 139.2 | 320.1 | 116.7 |
| response time (ms), 95th percentile | 1176 | 247.1 | 1281 | 263.1 |
| response time (ms), 99th percentile | 1662 | 347.1 | 1959 | 377.5 |
| time over the response line (% of samples) | 14.19 | 0.1996 | 14.36 | 0.37 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | 9.6 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 130.3 | 97.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 39.58 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.495 | 1155 | 11.09 | 1257 |
| utilisation (used / allocatable) | 0.06012 | 0.06069 | 0.07023 | 0.05869 |
| CPU used (cores), mean | 1.443 | 1.456 | 1.437 | 1.409 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07596 | 0.07195 |
| CPU used with Omni's own (cores), mean | 1.443 | 1.456 | 1.513 | 1.481 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 446.5 | 413.5 | 460.5 |
| HPA replicas, mean | 1.983 | 2.061 | 2.436 | 2.097 |
| pods started | 0 | 0 | 1.8 | 0.4 |
| pod start wait, total (s) | 0 | 0 | 5 | 0.7 |
| pod start wait, mean (s) | 0 | 0 | 2.367 | 0.5 |
| host CPU busy, the real machine under kind (%) | 41.42 | 45.91 | 44.74 | 47.28 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.4 | 1506 | 780.6 | 1508 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 4.625 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 171.1 | 0.025 | 191.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 714.5 | 0.1 | 855.9 |
| queue: job turnaround, submitted to done, mean (s) | 80.09 | 860.7 | 86.43 | 909 |
| queue: jobs unfinished at the window's end | 0 | 9.9 | 0 | 13.1 |
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
| node-hours | 2.513 | 2.513 | 0.0% | raw −0.0097 to +0.0097 | STEADY, the same (to nine decimal places) |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.6 | −0.3% | −2.0178 to +0.6284 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.6 | −0.3% | −2.0178 to +0.6284 | no |
| response time (ms), mean | 139.2 | 116.7 | −16.2% | −27.6440 to −17.3384 | yes: GAIN |
| response time (ms), 95th percentile | 247.1 | 263.1 | +6.4% | +3.0086 to +28.8514 | yes: LOSS |
| response time (ms), 99th percentile | 347.1 | 377.5 | +8.7% | +9.4532 to +51.2446 | yes: LOSS |
| time over the response line (% of samples) | 0.1996 | 0.37 | +85.4% | −0.0139 to +0.3547 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 97.2 | +97.200 (native is 0) | +80.5921 to +113.8079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1155 | 1257 | +8.9% | +43.8265 to +160.8902 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06069 | 0.05869 | −3.3% | −0.0034 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.456 | 1.409 | −3.3% | −0.0828 to −0.0131 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07195 | +0.072 (native is 0) | +0.0654 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.456 | 1.481 | +1.7% | −0.0132 to +0.0613 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.5 | 460.5 | +3.1% | +3.8959 to +24.1185 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.061 | 2.097 | +1.8% | −0.2275 to +0.2998 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| host CPU busy, the real machine under kind (%) | 45.91 | 47.28 | +3.0% | +0.4139 to +2.3375 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1508 | +0.1% | −2.9670 to +7.3670 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 171.1 | 191.4 | +11.9% | −22.3482 to +63.0065 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 714.5 | 855.9 | +19.8% | −93.1699 to +375.9699 | no |
| queue: job turnaround, submitted to done, mean (s) | 860.7 | 909 | +5.6% | +10.6728 to +85.8772 | yes: LOSS |
| queue: jobs unfinished at the window's end | 9.9 | 13.1 | +32.3% | −0.0483 to +6.4483 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.519 | 2.513 | −0.3% | −0.0146 to +0.0020 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.3 | −0.2% | −2.9446 to +1.6746 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.3 | −0.2% | −2.9446 to +1.6746 | no |
| response time (ms), mean | 340 | 139.2 | −59.1% | −344.4240 to −57.2483 | yes: GAIN |
| response time (ms), 95th percentile | 1176 | 247.1 | −79.0% | −1607.7704 to −250.5626 | yes: GAIN |
| response time (ms), 99th percentile | 1662 | 347.1 | −79.1% | −2263.3293 to −366.1481 | yes: GAIN |
| time over the response line (% of samples) | 14.19 | 0.1996 | −98.6% | −24.5530 to −3.4325 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | −100.0% | −12.9637 to −5.6363 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.495 | 1155 | +13496.3% | +946.7929 to +1346.2305 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.06069 | +0.9% | −0.0055 to +0.0067 | no |
| CPU used (cores), mean | 1.443 | 1.456 | +0.9% | −0.1329 to +0.1599 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.443 | 1.456 | +0.9% | −0.1329 to +0.1599 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 446.5 | −2.5% | −53.5783 to +30.3355 | no |
| HPA replicas, mean | 1.983 | 2.061 | +3.9% | −0.0726 to +0.2286 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 41.42 | 45.91 | +10.8% | +1.0722 to +7.8959 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.4 | 1506 | +94.8% | +689.3851 to +776.4149 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 171.1 | +273680.0% | +129.8256 to +212.2744 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 714.5 | +178525.0% | +543.2607 to +884.9393 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.09 | 860.7 | +974.7% | +722.3299 to +838.9701 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.9 | +9.900 (native is 0) | +3.8169 to +15.9831 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.183 | −13.6% | −1.4810 to −0.1525 | yes: GAIN |
| node-hours | 2.519 | 2.17 | −13.9% | −0.6282 to −0.0707 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.2 | −0.2% | −1.3744 to +0.0925 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 246.6 | −9.6% | −47.3335 to −5.2651 | yes: GAIN |
| response time (ms), mean | 340 | 320.1 | −5.9% | −29.3905 to −10.5714 | yes: GAIN |
| response time (ms), 95th percentile | 1176 | 1281 | +8.9% | +33.7968 to +176.4572 | yes: LOSS |
| response time (ms), 99th percentile | 1662 | 1959 | +17.9% | +50.7925 to +543.9963 | yes: LOSS |
| time over the response line (% of samples) | 14.19 | 14.36 | +1.2% | −1.0203 to +1.3610 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.6 | +3.2% | −0.6567 to +1.2567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.3 | +130.300 (native is 0) | +57.5861 to +203.0139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.495 | 11.09 | +30.5% | +1.0962 to +4.0905 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.07023 | +16.8% | +0.0016 to +0.0186 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.437 | −0.4% | −0.0373 to +0.0258 | no |
| Omni's own CPU (cores), mean | 0 | 0.07596 | +0.076 (native is 0) | +0.0705 to +0.0815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.513 | +4.9% | +0.0356 to +0.1049 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 413.5 | −9.7% | −79.7609 to −9.4120 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.436 | +22.9% | +0.2212 to +0.6850 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.8583 to +2.7417 | yes: power given |
| pod start wait, total (s) | 0 | 5 | +5.000 (native is 0) | +2.0411 to +7.9589 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.367 | +2.367 (native is 0) | +1.5373 to +3.1961 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.42 | 44.74 | +8.0% | +2.8900 to +3.7353 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.4 | 780.6 | +0.9% | +0.1204 to +14.2796 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.625 | −22.9% | −2.3487 to −0.4019 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.025 | −60.0% | −0.0945 to +0.0195 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.1 | −75.0% | −0.7828 to +0.1828 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.09 | 86.43 | +7.9% | +0.4131 to +12.2786 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.183 | −13.6% | −1.4810 to −0.1525 | yes: GAIN |
| node-hours | 2.513 | 2.17 | −13.7% | −0.6240 to −0.0622 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.2 | −0.0% | −2.4361 to +2.4242 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 246.6 | −9.4% | −48.5064 to −2.8222 | yes: GAIN |
| response time (ms), mean | 139.2 | 320.1 | +129.9% | +32.9191 to +328.7912 | yes: LOSS |
| response time (ms), 95th percentile | 247.1 | 1281 | +418.5% | +292.5919 to +1775.9951 | yes: LOSS |
| response time (ms), 99th percentile | 347.1 | 1959 | +464.4% | +446.2606 to +2778.0056 | yes: LOSS |
| time over the response line (% of samples) | 0.1996 | 14.36 | +7096.7% | +4.2077 to +24.1185 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 9.6 | +9.600 (native is 0) | +5.6503 to +13.5497 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 130.3 | +130.300 (native is 0) | +57.5861 to +203.0139 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1155 | 11.09 | −99.0% | −1344.0407 to −943.7959 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06069 | 0.07023 | +15.7% | +0.0027 to +0.0164 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.456 | 1.437 | −1.3% | −0.1880 to +0.1495 | no |
| Omni's own CPU (cores), mean | 0 | 0.07596 | +0.076 (native is 0) | +0.0705 to +0.0815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.456 | 1.513 | +3.9% | −0.1150 to +0.2284 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.5 | 413.5 | −7.4% | −63.8308 to −2.0993 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.061 | 2.436 | +18.2% | +0.1553 to +0.5949 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.8583 to +2.7417 | yes: power given |
| pod start wait, total (s) | 0 | 5 | +5.000 (native is 0) | +2.0411 to +7.9589 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.367 | +2.367 (native is 0) | +1.5373 to +3.1961 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.91 | 44.74 | −2.6% | −4.7003 to +2.3575 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 780.6 | −48.2% | −775.6704 to −675.7296 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 171.1 | 0.025 | −100.0% | −212.3584 to −129.8166 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 714.5 | 0.1 | −100.0% | −885.5086 to −543.2914 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 860.7 | 86.43 | −90.0% | −830.3656 to −718.2427 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.9 | 0 | −100.0% | −15.9831 to −3.8169 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.519 | 2.513 | −0.3% | −0.0131 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.6 | −0.5% | −3.3448 to +0.6854 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 271.6 | −0.5% | −3.3448 to +0.6854 | no |
| response time (ms), mean | 340 | 116.7 | −65.7% | −367.3902 to −79.2644 | yes: GAIN |
| response time (ms), 95th percentile | 1176 | 263.1 | −77.6% | −1586.6295 to −239.8435 | yes: GAIN |
| response time (ms), 99th percentile | 1662 | 377.5 | −77.3% | −2226.2226 to −342.5570 | yes: GAIN |
| time over the response line (% of samples) | 14.19 | 0.37 | −97.4% | −24.2276 to −3.4171 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0.3 | −96.8% | −12.4553 to −5.5447 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 97.2 | +97.200 (native is 0) | +80.5921 to +113.8079 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.495 | 1257 | +14701.2% | +1080.4740 to +1417.2660 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06012 | 0.05869 | −2.4% | −0.0073 to +0.0044 | no |
| CPU used (cores), mean | 1.443 | 1.409 | −2.4% | −0.1744 to +0.1056 | no |
| Omni's own CPU (cores), mean | 0 | 0.07195 | +0.072 (native is 0) | +0.0654 to +0.0785 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.481 | +2.6% | −0.0965 to +0.1716 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.1 | 460.5 | +0.5% | −37.5812 to +42.3528 | no |
| HPA replicas, mean | 1.983 | 2.097 | +5.8% | −0.0991 to +0.3273 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| host CPU busy, the real machine under kind (%) | 41.42 | 47.28 | +14.1% | +2.6751 to +9.0443 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.4 | 1508 | +95.0% | +691.0436 to +779.1564 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 191.4 | +306206.7% | +156.4349 to +226.3234 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 855.9 | +213875.0% | +671.0631 to +1039.9369 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.09 | 909 | +1035.0% | +769.7970 to +888.0530 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.1 | +13.100 (native is 0) | +9.2487 to +16.9513 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*