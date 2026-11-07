# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.06 | 5.999 |
| node-hours | 2.515 | 2.514 | 2.119 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | 272.3 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | 242.7 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 342.7 | 140 | 324.2 | 115.5 |
| response time (ms), 95th percentile | 1195 | 244.7 | 1327 | 254.6 |
| response time (ms), 99th percentile | 1700 | 355.5 | 1901 | 370.7 |
| time over the response line (% of samples) | 14.32 | 0.2076 | 13.78 | 0.2948 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.1 | 9.7 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 152.9 | 114.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.915 | 1175 | 9.653 | 1261 |
| utilisation (used / allocatable) | 0.05977 | 0.05961 | 0.07187 | 0.05843 |
| CPU used (cores), mean | 1.434 | 1.431 | 1.429 | 1.402 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07369 | 0.07066 |
| CPU used with Omni's own (cores), mean | 1.434 | 1.431 | 1.503 | 1.473 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 454.2 | 407.6 | 462.8 |
| HPA replicas, mean | 1.882 | 1.978 | 2.432 | 2.185 |
| pods started | 0.1 | 0 | 1.5 | 0.6 |
| pod start wait, total (s) | 0.3 | 0 | 3.7 | 1.1 |
| pod start wait, mean (s) | 0.3 | 0 | 1.475 | 0.4833 |
| host CPU busy, the real machine under kind (%) | 41.11 | 45.25 | 44.42 | 47.03 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 775.6 | 1487 | 781.7 | 1488 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.335 | 5.923 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 176.3 | 0.0625 | 186.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 708.1 | 0.4 | 747.9 |
| queue: job turnaround, submitted to done, mean (s) | 80.52 | 869.4 | 88.07 | 902 |
| queue: jobs unfinished at the window's end | 0 | 11 | 0 | 12.2 |
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
| worker nodes in service, mean | 6 | 5.999 | −0.0% | −0.0035 to +0.0013 | no |
| node-hours | 2.514 | 2.514 | −0.0% | −0.0086 to +0.0067 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.6 | −0.2% | −1.3275 to +0.3050 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.5 | −0.2% | −1.3432 to +0.2540 | no |
| response time (ms), mean | 140 | 115.5 | −17.5% | −28.6802 to −20.3488 | yes: GAIN |
| response time (ms), 95th percentile | 244.7 | 254.6 | +4.0% | −3.6407 to +23.3547 | no |
| response time (ms), 99th percentile | 355.5 | 370.7 | +4.3% | −9.4531 to +39.7191 | no |
| time over the response line (% of samples) | 0.2076 | 0.2948 | +42.0% | −0.1086 to +0.2831 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.7 | +114.700 (native is 0) | +100.0675 to +129.3325 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1175 | 1261 | +7.3% | +12.2728 to +159.1106 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05961 | 0.05843 | −2.0% | −0.0033 to +0.0010 | no |
| CPU used (cores), mean | 1.431 | 1.402 | −2.0% | −0.0796 to +0.0225 | no |
| Omni's own CPU (cores), mean | 0 | 0.07066 | +0.071 (native is 0) | +0.0627 to +0.0786 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.473 | +2.9% | −0.0062 to +0.0904 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.2 | 462.8 | +1.9% | −7.0508 to +24.1640 | no |
| HPA replicas, mean | 1.978 | 2.185 | +10.5% | −0.0191 to +0.4339 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.5329 to +2.7329 | no |
| pod start wait, mean (s) | 0 | 0.4833 | +0.483 (native is 0) | −0.1179 to +1.0846 | no |
| host CPU busy, the real machine under kind (%) | 45.25 | 47.03 | +3.9% | +0.8363 to +2.7160 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1487 | 1488 | +0.1% | −3.7050 to +6.5050 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.923 | −1.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 176.3 | 186.6 | +5.8% | −29.7739 to +50.2822 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 708.1 | 747.9 | +5.6% | −76.1130 to +155.7130 | no |
| queue: job turnaround, submitted to done, mean (s) | 869.4 | 902 | +3.7% | −14.1970 to +79.3553 | no |
| queue: jobs unfinished at the window's end | 11 | 12.2 | +10.9% | −1.5969 to +3.9969 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.515 | −0.0% | −0.0092 to +0.0085 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −2.4410 to +2.0059 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | −0.1% | −2.4410 to +2.0059 | no |
| response time (ms), mean | 342.7 | 140 | −59.2% | −356.5034 to −49.0100 | yes: GAIN |
| response time (ms), 95th percentile | 1195 | 244.7 | −79.5% | −1666.9291 to −232.9249 | yes: GAIN |
| response time (ms), 99th percentile | 1700 | 355.5 | −79.1% | −2364.7383 to −325.0071 | yes: GAIN |
| time over the response line (% of samples) | 14.32 | 0.2076 | −98.6% | −25.0145 to −3.2133 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.1 | −98.9% | −12.2349 to −4.9651 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.915 | 1175 | +13083.0% | +957.1421 to +1375.5546 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05977 | 0.05961 | −0.3% | −0.0064 to +0.0060 | no |
| CPU used (cores), mean | 1.434 | 1.431 | −0.3% | −0.1526 to +0.1448 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.434 | 1.431 | −0.3% | −0.1526 to +0.1448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 454.2 | −1.5% | −48.9552 to +35.1870 | no |
| HPA replicas, mean | 1.882 | 1.978 | +5.1% | −0.0660 to +0.2572 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 41.11 | 45.25 | +10.1% | +0.7516 to +7.5288 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.6 | 1487 | +91.7% | +653.7526 to +769.0474 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 176.3 | +302157.1% | +124.1003 to +228.4163 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 708.1 | +176925.0% | +520.4746 to +894.9254 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.52 | 869.4 | +979.7% | +720.7756 to +856.9827 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11 | +11.000 (native is 0) | +5.3274 to +16.6726 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.06 | −15.7% | −1.6991 to −0.1814 | yes: GAIN |
| node-hours | 2.515 | 2.119 | −15.7% | −0.7085 to −0.0830 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.3 | −0.0% | −0.7101 to +0.6995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 242.7 | −10.9% | −53.2036 to −6.0195 | yes: GAIN |
| response time (ms), mean | 342.7 | 324.2 | −5.4% | −36.9925 to −0.1464 | yes: GAIN |
| response time (ms), 95th percentile | 1195 | 1327 | +11.1% | −5.7827 to +270.6167 | no |
| response time (ms), 99th percentile | 1700 | 1901 | +11.8% | +3.4153 to +397.1997 | yes: LOSS |
| time over the response line (% of samples) | 14.32 | 13.78 | −3.8% | −1.2747 to +0.1906 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.7 | +11.5% | +0.1740 to +1.8260 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 152.9 | +152.900 (native is 0) | +81.7331 to +224.0669 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.915 | 9.653 | +8.3% | −0.5969 to +2.0736 | no |
| utilisation (used / allocatable) | 0.05977 | 0.07187 | +20.2% | +0.0022 to +0.0220 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.434 | 1.429 | −0.3% | −0.0373 to +0.0273 | no |
| Omni's own CPU (cores), mean | 0 | 0.07369 | +0.074 (native is 0) | +0.0677 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.434 | 1.503 | +4.8% | +0.0338 to +0.1037 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 407.6 | −11.6% | −92.9325 to −14.0394 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.882 | 2.432 | +29.2% | +0.3603 to +0.7389 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.4344 to +2.3656 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.7 | +1133.3% | +0.9872 to +5.8128 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.475 | +391.7% | +0.1355 to +2.2145 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.11 | 44.42 | +8.1% | +2.8387 to +3.7822 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.6 | 781.7 | +0.8% | −0.3108 to +12.5108 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.335 | −27.7% | −2.9149 to −0.4145 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.0625 | +7.1% | −0.0286 to +0.0370 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.52 | 88.07 | +9.4% | +0.7081 to +14.3919 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.06 | −15.7% | −1.6991 to −0.1814 | yes: GAIN |
| node-hours | 2.514 | 2.119 | −15.7% | −0.7112 to −0.0796 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.3 | +0.1% | −1.6782 to +2.1028 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 242.7 | −10.8% | −54.8647 to −3.9232 | yes: GAIN |
| response time (ms), mean | 140 | 324.2 | +131.6% | +21.9488 to +346.4257 | yes: LOSS |
| response time (ms), 95th percentile | 244.7 | 1327 | +442.3% | +252.8121 to +1911.8759 | yes: LOSS |
| response time (ms), 99th percentile | 355.5 | 1901 | +434.6% | +363.5675 to +2726.7929 | yes: LOSS |
| time over the response line (% of samples) | 0.2076 | 13.78 | +6538.5% | +3.3476 to +23.7962 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 9.7 | +9600.0% | +6.0282 to +13.1718 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 152.9 | +152.900 (native is 0) | +81.7331 to +224.0669 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1175 | 9.653 | −99.2% | −1374.5887 to −956.6313 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05961 | 0.07187 | +20.6% | +0.0046 to +0.0200 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.429 | −0.1% | −0.1702 to +0.1681 | no |
| Omni's own CPU (cores), mean | 0 | 0.07369 | +0.074 (native is 0) | +0.0677 to +0.0797 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.503 | +5.1% | −0.1008 to +0.2461 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.2 | 407.6 | −10.3% | −77.8706 to −15.3332 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.978 | 2.432 | +23.0% | +0.1551 to +0.7529 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.4204 to +2.5796 | yes: power given |
| pod start wait, total (s) | 0 | 3.7 | +3.700 (native is 0) | +1.0225 to +6.3775 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.475 | +1.475 (native is 0) | +0.5346 to +2.4154 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.25 | 44.42 | −1.8% | −4.5393 to +2.8796 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1487 | 781.7 | −47.4% | −766.6072 to −643.9928 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 176.3 | 0.0625 | −100.0% | −228.3957 to −124.1127 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 708.1 | 0.4 | −99.9% | −894.8680 to −520.5320 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 869.4 | 88.07 | −89.9% | −845.0129 to −717.6455 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11 | 0 | −100.0% | −16.6726 to −5.3274 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.999 | −0.0% | −0.0035 to +0.0013 | no |
| node-hours | 2.515 | 2.514 | −0.1% | −0.0079 to +0.0053 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.6 | −0.3% | −3.3965 to +1.9388 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 271.5 | −0.3% | −3.3991 to +1.8747 | no |
| response time (ms), mean | 342.7 | 115.5 | −66.3% | −379.3757 to −75.1667 | yes: GAIN |
| response time (ms), 95th percentile | 1195 | 254.6 | −78.7% | −1648.1362 to −232.0038 | yes: GAIN |
| response time (ms), 99th percentile | 1700 | 370.7 | −78.2% | −2340.8359 to −318.6435 | yes: GAIN |
| time over the response line (% of samples) | 14.32 | 0.2948 | −97.9% | −24.8782 to −3.1751 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 0.4 | −95.4% | −11.6728 to −4.9272 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.7 | +114.700 (native is 0) | +100.0675 to +129.3325 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.915 | 1261 | +14044.2% | +1029.3935 to +1474.6865 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05977 | 0.05843 | −2.2% | −0.0084 to +0.0057 | no |
| CPU used (cores), mean | 1.434 | 1.402 | −2.3% | −0.2023 to +0.1374 | no |
| Omni's own CPU (cores), mean | 0 | 0.07066 | +0.071 (native is 0) | +0.0627 to +0.0786 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.434 | 1.473 | +2.7% | −0.1243 to +0.2007 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.1 | 462.8 | +0.4% | −47.5481 to +50.8931 | no |
| HPA replicas, mean | 1.882 | 2.185 | +16.1% | +0.0908 to +0.5152 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | −1.0714 to +2.6714 | no |
| pod start wait, mean (s) | 0.3 | 0.4833 | +61.1% | −0.8101 to +1.1767 | no |
| host CPU busy, the real machine under kind (%) | 41.11 | 47.03 | +14.4% | +2.5157 to +9.3170 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.6 | 1488 | +91.9% | +655.9154 to +769.6846 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.923 | −1.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 186.6 | +319735.7% | +136.4900 to +236.5350 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 747.9 | +186875.0% | +620.4429 to +874.5571 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.52 | 902 | +1020.2% | +733.1490 to +909.7677 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.2 | +12.200 (native is 0) | +7.2350 to +17.1650 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*