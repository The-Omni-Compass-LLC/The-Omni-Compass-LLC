# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.576 | 6 |
| node-hours | 2.516 | 2.514 | 2.336 | 2.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 286.9 | 276.4 | 287.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 286.9 | 263.1 | 287.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 599.9 | 826.6 | 605.4 | 802.1 |
| response time (ms), 95th percentile | 2352 | 1630 | 2655 | 1568 |
| response time (ms), 99th percentile | 3389 | 2112 | 3758 | 2029 |
| time over the response line (% of samples) | 29.95 | 75.72 | 29.29 | 73.73 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 25 | 13.8 | 25 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 58.3 | 27.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.43 | 2.455 | 20.1 | 2.478 |
| utilisation (used / allocatable) | 0.06995 | 0.09895 | 0.07638 | 0.098 |
| CPU used (cores), mean | 1.679 | 2.375 | 1.694 | 2.352 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07898 | 0.04747 |
| CPU used with Omni's own (cores), mean | 1.679 | 2.375 | 1.773 | 2.399 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 397.8 | 288.4 | 372.2 | 290.9 |
| HPA replicas, mean | 2.067 | 2.055 | 2.371 | 2.851 |
| pods started | 0 | 0 | 1.3 | 2 |
| pod start wait, total (s) | 0 | 0 | 3.2 | 7.4 |
| pod start wait, mean (s) | 0 | 0 | 1.65 | 2.275 |
| host CPU busy, the real machine under kind (%) | 47.44 | 77.79 | 51.28 | 79.06 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 864.6 | 1509 | 887 | 1512 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 5.262 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 883.9 | 0.4167 | 884 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1427 | 2.6 | 1397 |
| queue: job turnaround, submitted to done, mean (s) | 170.1 | 1078 | 190.3 | 1084 |
| queue: jobs unfinished at the window's end | 0 | 19.8 | 0 | 19.1 |
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
| node-hours | 2.514 | 2.52 | +0.2% | −0.0031 to +0.0135 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.9 | 287.2 | +0.1% | −0.7438 to +1.2159 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.9 | 287.2 | +0.1% | −0.7438 to +1.2159 | no |
| response time (ms), mean | 826.6 | 802.1 | −3.0% | −61.6417 to +12.7107 | no |
| response time (ms), 95th percentile | 1630 | 1568 | −3.8% | −169.5887 to +44.8537 | no |
| response time (ms), 99th percentile | 2112 | 2029 | −3.9% | −182.5794 to +17.0806 | no |
| time over the response line (% of samples) | 75.72 | 73.73 | −2.6% | −3.8611 to −0.1278 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 25 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.6 | +27.600 (native is 0) | +23.8421 to +31.3579 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.455 | 2.478 | +1.0% | −0.4014 to +0.4481 | no |
| utilisation (used / allocatable) | 0.09895 | 0.098 | −1.0% | −0.0018 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.375 | 2.352 | −1.0% | −0.0437 to −0.0021 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04747 | +0.047 (native is 0) | +0.0440 to +0.0509 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.375 | 2.399 | +1.0% | +0.0040 to +0.0452 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 288.4 | 290.9 | +0.9% | +0.2158 to +4.7237 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.851 | +38.8% | +0.4114 to +1.1811 | yes: power given |
| pods started | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes: power given |
| pod start wait, total (s) | 0 | 7.4 | +7.400 (native is 0) | +0.8510 to +13.9490 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.275 | +2.275 (native is 0) | +0.9477 to +3.6023 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 77.79 | 79.06 | +1.6% | +1.1499 to +1.3902 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1509 | 1512 | +0.2% | −1.8838 to +8.0838 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 883.9 | 884 | +0.0% | −98.6792 to +98.7651 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1427 | 1397 | −2.1% | −92.4055 to +32.0055 | no |
| queue: job turnaround, submitted to done, mean (s) | 1078 | 1084 | +0.6% | −29.3807 to +42.0974 | no |
| queue: jobs unfinished at the window's end | 19.8 | 19.1 | −3.5% | −2.3537 to +0.9537 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0102 to +0.0072 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 286.9 | +3.9% | +7.8831 to +13.5010 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 286.9 | +3.9% | +7.8831 to +13.5010 | yes: power given |
| response time (ms), mean | 599.9 | 826.6 | +37.8% | +179.8850 to +273.4650 | yes: LOSS |
| response time (ms), 95th percentile | 2352 | 1630 | −30.7% | −1126.7461 to −317.5219 | yes: GAIN |
| response time (ms), 99th percentile | 3389 | 2112 | −37.7% | −1859.0859 to −695.1611 | yes: GAIN |
| time over the response line (% of samples) | 29.95 | 75.72 | +152.8% | +43.5757 to +47.9735 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 25 | +85.2% | +8.1070 to +14.8930 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.43 | 2.455 | −80.2% | −11.7197 to −8.2203 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06995 | 0.09895 | +41.5% | +0.0219 to +0.0361 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.679 | 2.375 | +41.5% | +0.5245 to +0.8674 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.679 | 2.375 | +41.5% | +0.5245 to +0.8674 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 397.8 | 288.4 | −27.5% | −152.6511 to −66.1685 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.055 | −0.6% | −0.0946 to +0.0707 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 47.44 | 77.79 | +64.0% | +26.4724 to +34.2181 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 864.6 | 1509 | +74.6% | +606.3770 to +682.8230 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 883.9 | +1178461.6% | +805.2706 to +962.4217 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1427 | +285300.0% | +1402.2703 to +1450.7297 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 170.1 | 1078 | +533.5% | +889.6351 to +925.3482 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 19.8 | +19.800 (native is 0) | +17.8108 to +21.7892 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.576 | −7.1% | −1.0639 to +0.2169 | no |
| node-hours | 2.516 | 2.336 | −7.1% | −0.4487 to +0.0891 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 276.4 | +0.1% | −1.0278 to +1.3996 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 263.1 | −4.8% | −33.6459 to +7.3260 | no |
| response time (ms), mean | 599.9 | 605.4 | +0.9% | −22.0625 to +32.9795 | no |
| response time (ms), 95th percentile | 2352 | 2655 | +12.9% | +158.2985 to +447.4415 | yes: LOSS |
| response time (ms), 99th percentile | 3389 | 3758 | +10.9% | +75.2407 to +663.2885 | yes: LOSS |
| time over the response line (% of samples) | 29.95 | 29.29 | −2.2% | −1.4760 to +0.1489 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 13.8 | +2.2% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.3 | +58.300 (native is 0) | +15.6753 to +100.9247 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.43 | 20.1 | +61.8% | +1.9326 to +13.4241 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06995 | 0.07638 | +9.2% | −0.0011 to +0.0140 | no |
| CPU used (cores), mean | 1.679 | 1.694 | +0.9% | −0.0221 to +0.0519 | no |
| Omni's own CPU (cores), mean | 0 | 0.07898 | +0.079 (native is 0) | +0.0749 to +0.0831 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.679 | 1.773 | +5.6% | +0.0531 to +0.1347 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 397.8 | 372.2 | −6.5% | −57.3646 to +6.0197 | no |
| HPA replicas, mean | 2.067 | 2.371 | +14.7% | +0.1808 to +0.4276 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.4706 to +2.1294 | yes: power given |
| pod start wait, total (s) | 0 | 3.2 | +3.200 (native is 0) | +1.0199 to +5.3801 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.65 | +1.650 (native is 0) | +0.8043 to +2.4957 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.44 | 51.28 | +8.1% | +3.3679 to +4.3062 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 864.6 | 887 | +2.6% | +13.6250 to +31.1750 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.262 | −12.3% | −1.6508 to +0.1748 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.4167 | +455.6% | −0.1052 to +0.7886 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.6 | +420.0% | −0.8483 to +5.0483 | no |
| queue: job turnaround, submitted to done, mean (s) | 170.1 | 190.3 | +11.9% | +9.7892 to +30.5524 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.576 | −7.1% | −1.0639 to +0.2169 | no |
| node-hours | 2.514 | 2.336 | −7.1% | −0.4477 to +0.0911 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 286.9 | 276.4 | −3.7% | −13.4476 to −7.5648 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.9 | 263.1 | −8.3% | −46.8871 to −0.8169 | yes: GAIN |
| response time (ms), mean | 826.6 | 605.4 | −26.8% | −279.0425 to −163.3905 | yes: GAIN |
| response time (ms), 95th percentile | 1630 | 2655 | +62.9% | +546.8484 to +1503.1596 | yes: LOSS |
| response time (ms), 99th percentile | 2112 | 3758 | +78.0% | +959.5762 to +2333.2000 | yes: LOSS |
| time over the response line (% of samples) | 75.72 | 29.29 | −61.3% | −49.1847 to −43.6916 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 13.8 | −44.8% | −14.6848 to −7.7152 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.3 | +58.300 (native is 0) | +15.6753 to +100.9247 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.455 | 20.1 | +718.9% | +11.0039 to +24.2928 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09895 | 0.07638 | −22.8% | −0.0245 to −0.0206 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.375 | 1.694 | −28.7% | −0.8852 to −0.4768 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07898 | +0.079 (native is 0) | +0.0749 to +0.0831 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.375 | 1.773 | −25.4% | −0.8102 to −0.3939 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 288.4 | 372.2 | +29.0% | +70.0668 to +97.4079 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.371 | +15.4% | +0.1489 to +0.4833 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.4706 to +2.1294 | yes: power given |
| pod start wait, total (s) | 0 | 3.2 | +3.200 (native is 0) | +1.0199 to +5.3801 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.65 | +1.650 (native is 0) | +0.8043 to +2.4957 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 77.79 | 51.28 | −34.1% | −30.7405 to −22.2760 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1509 | 887 | −41.2% | −666.8541 to −577.5459 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 883.9 | 0.4167 | −100.0% | −961.9777 to −805.0313 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1427 | 2.6 | −99.8% | −1448.5285 to −1400.2715 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1078 | 190.3 | −82.3% | −913.7085 to −860.9331 | yes: GAIN |
| queue: jobs unfinished at the window's end | 19.8 | 0 | −100.0% | −21.7892 to −17.8108 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.52 | +0.1% | −0.0033 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276.2 | 287.2 | +4.0% | +8.7284 to +13.1279 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.2 | 287.2 | +4.0% | +8.7284 to +13.1279 | yes: power given |
| response time (ms), mean | 599.9 | 802.1 | +33.7% | +146.7093 to +257.7095 | yes: LOSS |
| response time (ms), 95th percentile | 2352 | 1568 | −33.4% | −1203.8538 to −365.1492 | yes: GAIN |
| response time (ms), 99th percentile | 3389 | 2029 | −40.1% | −1991.6401 to −728.1057 | yes: GAIN |
| time over the response line (% of samples) | 29.95 | 73.73 | +146.2% | +41.4448 to +46.1155 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.5 | 25 | +85.2% | +8.1070 to +14.8930 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.6 | +27.600 (native is 0) | +23.8421 to +31.3579 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.43 | 2.478 | −80.1% | −11.5029 to −8.3904 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06995 | 0.098 | +40.1% | +0.0208 to +0.0353 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.679 | 2.352 | +40.1% | +0.4996 to +0.8465 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04747 | +0.047 (native is 0) | +0.0440 to +0.0509 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.679 | 2.399 | +42.9% | +0.5505 to +0.8905 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 397.8 | 290.9 | −26.9% | −150.4222 to −63.4579 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.067 | 2.851 | +38.0% | +0.3951 to +1.1735 | yes: power given |
| pods started | 0 | 2 | +2.000 (native is 0) | +0.5302 to +3.4698 | yes: power given |
| pod start wait, total (s) | 0 | 7.4 | +7.400 (native is 0) | +0.8510 to +13.9490 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.275 | +2.275 (native is 0) | +0.9477 to +3.6023 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.44 | 79.06 | +66.6% | +27.8033 to +35.4273 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 864.6 | 1512 | +74.9% | +612.6945 to +682.7055 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 884 | +1178518.8% | +744.2030 to +1023.5752 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1397 | +279260.0% | +1329.6846 to +1462.9154 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 170.1 | 1084 | +537.3% | +893.7069 to +933.9931 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 19.1 | +19.100 (native is 0) | +16.7288 to +21.4712 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*