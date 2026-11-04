# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.03 | 11.35 |
| node-hours | 5.035 | 5.03 | 4.623 | 4.757 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 527.7 | 527.7 | 527 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 527.7 | 497.3 | 506.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 775.8 | 1088 | 872.5 | 1256 |
| response time (ms), 95th percentile | 3104 | 3912 | 3688 | 4261 |
| response time (ms), 99th percentile | 4122 | 5170 | 4905 | 5461 |
| time over the response line (% of samples) | 26.55 | 35.18 | 29.06 | 43.53 |
| failed requests (%) | 0 | 0.09779 | 0.0244 | 0.1575 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 16.5 | 15 | 18.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 143.4 | 79.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 15.78 | 10 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.69 | 35.7 | 29.67 | 94.26 |
| utilisation (used / allocatable) | 0.03626 | 0.03712 | 0.04045 | 0.0379 |
| CPU used (cores), mean | 1.741 | 1.782 | 1.781 | 1.718 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06029 | 0.05947 |
| CPU used with Omni's own (cores), mean | 1.741 | 1.782 | 1.841 | 1.777 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.9 | 720.9 | 676.7 | 719.2 |
| HPA replicas, mean | 3.95 | 4.043 | 5.169 | 5.721 |
| pods started | 0.2 | 0 | 3 | 4.8 |
| pod start wait, total (s) | 0.6 | 0 | 8.2 | 14.9 |
| pod start wait, mean (s) | 0.6 | 0 | 2.777 | 2.568 |
| host CPU busy, the real machine under kind (%) | 54.77 | 61.45 | 60.51 | 68.05 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 934.7 | 1043 | 975.7 | 1114 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 10.24 | 10.49 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 15.42 | 0.1833 | 19 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 103.3 | 1 | 98.6 |
| queue: job turnaround, submitted to done, mean (s) | 240.9 | 315.8 | 275.6 | 392.1 |
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
| worker nodes in service, mean | 12 | 11.35 | −5.5% | −1.3430 to +0.0344 | no |
| node-hours | 5.03 | 4.757 | −5.4% | −0.5661 to +0.0198 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.7 | 527 | −0.1% | −4.6604 to +3.2835 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.7 | 506.4 | −4.0% | −42.5240 to +0.0721 | no |
| response time (ms), mean | 1088 | 1256 | +15.4% | +81.4762 to +253.7643 | yes: LOSS |
| response time (ms), 95th percentile | 3912 | 4261 | +8.9% | −67.9760 to +766.2860 | no |
| response time (ms), 99th percentile | 5170 | 5461 | +5.6% | −458.7500 to +1040.2262 | no |
| time over the response line (% of samples) | 35.18 | 43.53 | +23.7% | +4.1465 to +12.5470 | yes: LOSS |
| failed requests (%) | 0.09779 | 0.1575 | +61.1% | −0.1857 to +0.3052 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.5 | 18.5 | +12.1% | +0.5302 to +3.4698 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.9 | +79.900 (native is 0) | +51.5022 to +108.2978 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.7 | 94.26 | +164.0% | −13.6609 to +130.7709 | no |
| utilisation (used / allocatable) | 0.03712 | 0.0379 | +2.1% | −0.0054 to +0.0070 | no |
| CPU used (cores), mean | 1.782 | 1.718 | −3.6% | −0.3096 to +0.1817 | no |
| Omni's own CPU (cores), mean | 0 | 0.05947 | +0.059 (native is 0) | +0.0520 to +0.0669 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.782 | 1.777 | −0.3% | −0.2480 to +0.2390 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 719.2 | −0.2% | −124.5067 to +120.9890 | no |
| HPA replicas, mean | 4.043 | 5.721 | +41.5% | +0.6526 to +2.7020 | yes: power given |
| pods started | 0 | 4.8 | +4.800 (native is 0) | +2.8688 to +6.7312 | yes: power given |
| pod start wait, total (s) | 0 | 14.9 | +14.900 (native is 0) | +7.3415 to +22.4585 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.568 | +2.568 (native is 0) | +1.6123 to +3.5231 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.45 | 68.05 | +10.7% | +5.5279 to +7.6762 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1043 | 1114 | +6.7% | +46.3079 to +93.8921 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.49 | −12.6% | −3.0032 to −0.0120 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 15.42 | 19 | +23.3% | −15.4898 to +22.6648 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 103.3 | 98.6 | −4.5% | −86.1160 to +76.7160 | no |
| queue: job turnaround, submitted to done, mean (s) | 315.8 | 392.1 | +24.2% | +38.2903 to +114.3347 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.035 | 5.03 | −0.1% | −0.0176 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 527.7 | +0.0% | −2.1778 to +2.3277 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 527.7 | +0.0% | −2.1778 to +2.3277 | no |
| response time (ms), mean | 775.8 | 1088 | +40.2% | +167.8735 to +456.4190 | yes: LOSS |
| response time (ms), 95th percentile | 3104 | 3912 | +26.0% | +464.7583 to +1150.5097 | yes: LOSS |
| response time (ms), 99th percentile | 4122 | 5170 | +25.4% | +580.6897 to +1516.0971 | yes: LOSS |
| time over the response line (% of samples) | 26.55 | 35.18 | +32.5% | +5.3673 to +11.8939 | yes: LOSS |
| failed requests (%) | 0 | 0.09779 | +0.098 (native is 0) | −0.0132 to +0.2088 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 16.5 | +25.0% | +2.1791 to +4.4209 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.69 | 35.7 | +50.7% | −4.7747 to +28.8080 | no |
| utilisation (used / allocatable) | 0.03626 | 0.03712 | +2.4% | −0.0017 to +0.0034 | no |
| CPU used (cores), mean | 1.741 | 1.782 | +2.4% | −0.0814 to +0.1633 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.741 | 1.782 | +2.4% | −0.0814 to +0.1633 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.9 | 720.9 | −2.7% | −63.8651 to +23.9158 | no |
| HPA replicas, mean | 3.95 | 4.043 | +2.4% | −0.1665 to +0.3522 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.6 | 0 | −100.0% | −1.5656 to +0.3656 | no |
| pod start wait, mean (s) | 0.6 | 0 | −100.0% | −1.5656 to +0.3656 | no |
| host CPU busy, the real machine under kind (%) | 54.77 | 61.45 | +12.2% | +5.3457 to +8.0153 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 934.7 | 1043 | +11.6% | +61.2890 to +156.1110 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 15.42 | +9900.0% | +3.2180 to +27.3070 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 103.3 | +12812.5% | +25.7880 to +179.2120 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 240.9 | 315.8 | +31.1% | +38.9915 to +110.9335 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −2.2517 to +0.3196 | no |
| node-hours | 5.035 | 4.623 | −8.2% | −0.9487 to +0.1252 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 527.7 | +0.0% | −1.4907 to +1.6745 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 497.3 | −5.7% | −71.0256 to +10.3968 | no |
| response time (ms), mean | 775.8 | 872.5 | +12.5% | +28.0204 to +165.2874 | yes: LOSS |
| response time (ms), 95th percentile | 3104 | 3688 | +18.8% | +159.6309 to +1006.7761 | yes: LOSS |
| response time (ms), 99th percentile | 4122 | 4905 | +19.0% | +246.1238 to +1320.6330 | yes: LOSS |
| time over the response line (% of samples) | 26.55 | 29.06 | +9.4% | +0.5687 to +4.4475 | yes: LOSS |
| failed requests (%) | 0 | 0.0244 | +0.024 (native is 0) | −0.0152 to +0.0640 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 15 | +13.6% | +0.5936 to +3.0064 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.4 | +143.400 (native is 0) | +53.3280 to +233.4720 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.69 | 29.67 | +25.2% | −1.4500 to +13.4100 | no |
| utilisation (used / allocatable) | 0.03626 | 0.04045 | +11.5% | +0.0002 to +0.0082 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.741 | 1.781 | +2.3% | −0.0152 to +0.0950 | no |
| Omni's own CPU (cores), mean | 0 | 0.06029 | +0.060 (native is 0) | +0.0557 to +0.0649 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.741 | 1.841 | +5.8% | +0.0421 to +0.1583 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.9 | 676.7 | −8.7% | −124.2843 to −4.2052 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.95 | 5.169 | +30.8% | +0.9655 to +1.4714 | yes: power given |
| pods started | 0.2 | 3 | +1400.0% | +1.5474 to +4.0526 | yes: power given |
| pod start wait, total (s) | 0.6 | 8.2 | +1266.7% | +3.7083 to +11.4917 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.777 | +362.8% | +1.1593 to +3.1940 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.77 | 60.51 | +10.5% | +4.6446 to +6.8340 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 934.7 | 975.7 | +4.4% | +16.4376 to +65.5624 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.24 | −14.7% | −3.8381 to +0.3139 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.1833 | +18.9% | −0.0466 to +0.1049 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1 | +25.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 240.9 | 275.6 | +14.4% | +15.4775 to +54.0808 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.03 | −8.1% | −2.2517 to +0.3196 | no |
| node-hours | 5.03 | 4.623 | −8.1% | −0.9460 to +0.1325 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.7 | 527.7 | +0.0% | −2.6424 to +2.6762 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.7 | 497.3 | −5.8% | −71.6674 to +10.8887 | no |
| response time (ms), mean | 1088 | 872.5 | −19.8% | −313.9853 to −116.9995 | yes: GAIN |
| response time (ms), 95th percentile | 3912 | 3688 | −5.7% | −532.0588 to +83.1978 | no |
| response time (ms), 99th percentile | 5170 | 4905 | −5.1% | −655.0119 to +124.9819 | no |
| time over the response line (% of samples) | 35.18 | 29.06 | −17.4% | −8.9554 to −3.2896 | yes: GAIN |
| failed requests (%) | 0.09779 | 0.0244 | −75.0% | −0.1724 to +0.0256 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.5 | 15 | −9.1% | −2.0058 to −0.9942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 143.4 | +143.400 (native is 0) | +53.3280 to +233.4720 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 35.7 | 29.67 | −16.9% | −26.4604 to +14.3870 | no |
| utilisation (used / allocatable) | 0.03712 | 0.04045 | +9.0% | −0.0012 to +0.0078 | no |
| CPU used (cores), mean | 1.782 | 1.781 | −0.1% | −0.1617 to +0.1595 | no |
| Omni's own CPU (cores), mean | 0 | 0.06029 | +0.060 (native is 0) | +0.0557 to +0.0649 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.782 | 1.841 | +3.3% | −0.1035 to +0.2219 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.9 | 676.7 | −6.1% | −106.0671 to +17.5269 | no |
| HPA replicas, mean | 4.043 | 5.169 | +27.8% | +0.7922 to +1.4590 | yes: power given |
| pods started | 0 | 3 | +3.000 (native is 0) | +1.7383 to +4.2617 | yes: power given |
| pod start wait, total (s) | 0 | 8.2 | +8.200 (native is 0) | +4.3288 to +12.0712 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.777 | +2.777 (native is 0) | +2.2285 to +3.3248 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 61.45 | 60.51 | −1.5% | −1.6652 to −0.2172 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1043 | 975.7 | −6.5% | −92.9608 to −42.4392 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 10.24 | −14.7% | −3.8381 to +0.3139 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 15.42 | 0.1833 | −98.8% | −27.2869 to −3.1798 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 103.3 | 1 | −99.0% | −179.1629 to −25.4371 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 315.8 | 275.6 | −12.7% | −59.1066 to −21.2601 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.35 | −5.5% | −1.3430 to +0.0344 | no |
| node-hours | 5.035 | 4.757 | −5.5% | −0.5702 to +0.0139 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.6 | 527 | −0.1% | −4.1267 to +2.8997 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.6 | 506.4 | −4.0% | −42.0757 to −0.2263 | yes: GAIN |
| response time (ms), mean | 775.8 | 1256 | +61.8% | +277.8009 to +681.7322 | yes: LOSS |
| response time (ms), 95th percentile | 3104 | 4261 | +37.3% | +685.8212 to +1627.7568 | yes: LOSS |
| response time (ms), 99th percentile | 4122 | 5461 | +32.5% | +574.5449 to +2103.7181 | yes: LOSS |
| time over the response line (% of samples) | 26.55 | 43.53 | +63.9% | +11.5047 to +22.4501 | yes: LOSS |
| failed requests (%) | 0 | 0.1575 | +0.158 (native is 0) | −0.0665 to +0.3816 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 18.5 | +40.2% | +3.2200 to +7.3800 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 79.9 | +79.900 (native is 0) | +51.5022 to +108.2978 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.69 | 94.26 | +297.9% | +0.4593 to +140.6840 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03626 | 0.0379 | +4.5% | −0.0044 to +0.0077 | no |
| CPU used (cores), mean | 1.741 | 1.718 | −1.3% | −0.2463 to +0.2003 | no |
| Omni's own CPU (cores), mean | 0 | 0.05947 | +0.059 (native is 0) | +0.0520 to +0.0669 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.741 | 1.777 | +2.1% | −0.1834 to +0.2563 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 740.9 | 719.2 | −2.9% | −149.3910 to +105.9240 | no |
| HPA replicas, mean | 3.95 | 5.721 | +44.8% | +0.6654 to +2.8749 | yes: power given |
| pods started | 0.2 | 4.8 | +2300.0% | +2.8093 to +6.3907 | yes: power given |
| pod start wait, total (s) | 0.6 | 14.9 | +2383.3% | +7.3236 to +21.2764 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 2.568 | +328.0% | +0.9250 to +3.0105 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.77 | 68.05 | +24.3% | +11.2999 to +15.2652 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 934.7 | 1114 | +19.1% | +118.0285 to +239.5715 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.49 | −12.6% | −3.0032 to −0.0120 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 19 | +12227.0% | −0.2511 to +37.9511 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 98.6 | +12225.0% | +12.8440 to +182.7560 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 240.9 | 392.1 | +62.8% | +100.7052 to +201.8448 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*