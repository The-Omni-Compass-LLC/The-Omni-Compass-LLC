# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.08 | 7.177 |
| node-hours | 5.024 | 5.03 | 4.645 | 3.013 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.3 | 505 | 528.5 | 505.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.3 | 505 | 499.7 | 354 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 845.8 | 129.9 | 873.3 | 75.09 |
| response time (ms), 95th percentile | 3357 | 178.4 | 3711 | 96.38 |
| response time (ms), 99th percentile | 4392 | 205 | 4962 | 130 |
| time over the response line (% of samples) | 28.58 | 0 | 29.01 | 0 |
| failed requests (%) | 0 | 0 | 0.007018 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 0 | 14.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 56.1 | 27 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.76 | 0.08 | 22.51 | 0.1067 |
| utilisation (used / allocatable) | 0.0377 | 0.006363 | 0.04155 | 0.009224 |
| CPU used (cores), mean | 1.81 | 0.3054 | 1.834 | 0.2655 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01356 | 0.01014 |
| CPU used with Omni's own (cores), mean | 1.81 | 0.3054 | 1.847 | 0.2756 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 4032 | 657.2 | 3249 |
| HPA replicas, mean | 4.05 | 4.343 | 4.131 | 4.53 |
| pods started | 0.2 | 1 | 0.5 | 2.2 |
| pod start wait, total (s) | 0.3 | 1.1 | 1.3 | 2.8 |
| pod start wait, mean (s) | 0.15 | 0.6 | 0.9 | 0.95 |
| host CPU busy, the real machine under kind (%) | 56.01 | 15.34 | 58.12 | 16.75 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 955.7 | 1506 | 983.2 | 1509 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 10.43 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 1160 | 0.125 | 1162 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1476 | 0.7 | 1478 |
| queue: job turnaround, submitted to done, mean (s) | 261.4 | 1160 | 279.8 | 1162 |
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
| worker nodes in service, mean | 12 | 7.177 | −40.2% | −5.1659 to −4.4808 | yes: GAIN |
| node-hours | 5.03 | 3.013 | −40.1% | −2.1628 to −1.8709 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 505 | 505.9 | +0.2% | +0.5554 to +1.2501 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505 | 354 | −29.9% | −161.9791 to −139.9904 | yes: GAIN |
| response time (ms), mean | 129.9 | 75.09 | −42.2% | −63.9576 to −45.6435 | yes: GAIN |
| response time (ms), 95th percentile | 178.4 | 96.38 | −46.0% | −94.6302 to −69.3908 | yes: GAIN |
| response time (ms), 99th percentile | 205 | 130 | −36.6% | −88.8370 to −61.1406 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +24.8674 to +29.1326 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 0.1067 | +33.3% | −0.1630 to +0.2164 | no |
| utilisation (used / allocatable) | 0.006363 | 0.009224 | +45.0% | +0.0026 to +0.0031 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3054 | 0.2655 | −13.1% | −0.0495 to −0.0304 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01014 | +0.010 (native is 0) | +0.0090 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3054 | 0.2756 | −9.8% | −0.0392 to −0.0205 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4032 | 3249 | −19.4% | −915.0713 to −650.6111 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.343 | 4.53 | +4.3% | −0.1435 to +0.5181 | no |
| pods started | 1 | 2.2 | +120.0% | −0.2621 to +2.6621 | no |
| pod start wait, total (s) | 1.1 | 2.8 | +154.5% | +0.1166 to +3.2834 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 0.95 | +58.3% | −0.3462 to +1.0462 | no |
| host CPU busy, the real machine under kind (%) | 15.34 | 16.75 | +9.2% | +1.1119 to +1.7007 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1509 | +0.2% | +0.0109 to +4.7891 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1162 | +0.2% | +0.0726 to +4.4858 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1478 | +0.1% | −0.1068 to +4.5068 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1162 | +0.2% | +0.0726 to +4.4858 | yes: LOSS |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.024 | 5.03 | +0.1% | −0.0074 to +0.0201 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.3 | 505 | −4.2% | −25.0937 to −19.4989 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.3 | 505 | −4.2% | −25.0937 to −19.4989 | yes: GAIN |
| response time (ms), mean | 845.8 | 129.9 | −84.6% | −1035.4179 to −396.3755 | yes: GAIN |
| response time (ms), 95th percentile | 3357 | 178.4 | −94.7% | −4609.0106 to −1748.1724 | yes: GAIN |
| response time (ms), 99th percentile | 4392 | 205 | −95.3% | −6058.4950 to −2315.3634 | yes: GAIN |
| time over the response line (% of samples) | 28.58 | 0 | −100.0% | −40.2742 to −16.8902 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 0 | −100.0% | −18.9449 to −8.6551 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.76 | 0.08 | −99.7% | −34.7383 to −12.6217 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0377 | 0.006363 | −83.1% | −0.0350 to −0.0276 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.81 | 0.3054 | −83.1% | −1.6821 to −1.3261 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.81 | 0.3054 | −83.1% | −1.6821 to −1.3261 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 4032 | +464.9% | +2908.3531 to +3727.2837 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.05 | 4.343 | +7.2% | +0.1155 to +0.4712 | yes: power given |
| pods started | 0.2 | 1 | +400.0% | −0.3081 to +1.9081 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | −0.4972 to +2.0972 | no |
| pod start wait, mean (s) | 0.15 | 0.6 | +300.0% | −0.2338 to +1.1338 | no |
| host CPU busy, the real machine under kind (%) | 56.01 | 15.34 | −72.6% | −45.7977 to −35.5376 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 955.7 | 1506 | +57.6% | +440.2961 to +660.9039 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 1160 | +869606.2% | +1157.6923 to +1161.2577 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1476 | +184387.5% | +1473.1791 to +1477.0209 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 261.4 | 1160 | +343.6% | +789.9479 to +1006.4604 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.08 | −7.6% | −2.2218 to +0.3902 | no |
| node-hours | 5.024 | 4.645 | −7.5% | −0.9294 to +0.1727 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.3 | 528.5 | +0.2% | −0.6667 to +3.1193 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.3 | 499.7 | −5.2% | −69.1008 to +13.8492 | no |
| response time (ms), mean | 845.8 | 873.3 | +3.3% | −24.5995 to +79.6808 | no |
| response time (ms), 95th percentile | 3357 | 3711 | +10.5% | +89.4709 to +617.9891 | yes: LOSS |
| response time (ms), 99th percentile | 4392 | 4962 | +13.0% | +91.1349 to +1048.6675 | yes: LOSS |
| time over the response line (% of samples) | 28.58 | 29.01 | +1.5% | −0.4658 to +1.3281 | no |
| failed requests (%) | 0 | 0.007018 | +0.007 (native is 0) | −0.0089 to +0.0229 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 14.4 | +4.3% | +0.2306 to +0.9694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.1 | +56.100 (native is 0) | +13.7316 to +98.4684 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.76 | 22.51 | −5.2% | −7.9848 to +5.4915 | no |
| utilisation (used / allocatable) | 0.0377 | 0.04155 | +10.2% | −0.0010 to +0.0087 | no |
| CPU used (cores), mean | 1.81 | 1.834 | +1.3% | −0.0464 to +0.0947 | no |
| Omni's own CPU (cores), mean | 0 | 0.01356 | +0.014 (native is 0) | +0.0127 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.81 | 1.847 | +2.1% | −0.0332 to +0.1087 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 657.2 | −7.9% | −124.8562 to +11.7863 | no |
| HPA replicas, mean | 4.05 | 4.131 | +2.0% | −0.1692 to +0.3322 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.0455 to +0.6455 | no |
| pod start wait, total (s) | 0.3 | 1.3 | +333.3% | −0.1681 to +2.1681 | no |
| pod start wait, mean (s) | 0.15 | 0.9 | +500.0% | +0.0103 to +1.4897 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.01 | 58.12 | +3.8% | +1.2213 to +3.0085 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 955.7 | 983.2 | +2.9% | +9.3718 to +45.6282 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.43 | −13.1% | −3.6850 to +0.5352 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.125 | −6.2% | −0.0476 to +0.0309 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 0.7 | −12.5% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 261.4 | 279.8 | +7.0% | +2.8281 to +33.9969 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.08 | −7.6% | −2.2218 to +0.3902 | no |
| node-hours | 5.03 | 4.645 | −7.6% | −0.9326 to +0.1632 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 505 | 528.5 | +4.7% | +20.4890 to +26.5562 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505 | 499.7 | −1.1% | −48.9341 to +38.2751 | no |
| response time (ms), mean | 129.9 | 873.3 | +572.3% | +400.3234 to +1086.5512 | yes: LOSS |
| response time (ms), 95th percentile | 178.4 | 3711 | +1980.1% | +1948.8419 to +5115.8011 | yes: LOSS |
| response time (ms), 99th percentile | 205 | 4962 | +2320.0% | +2671.4308 to +6842.2300 | yes: LOSS |
| time over the response line (% of samples) | 0 | 29.01 | +29.013 (native is 0) | +17.4190 to +40.6077 | yes: LOSS |
| failed requests (%) | 0 | 0.007018 | +0.007 (native is 0) | −0.0089 to +0.0229 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14.4 | +14.400 (native is 0) | +9.1848 to +19.6152 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 56.1 | +56.100 (native is 0) | +13.7316 to +98.4684 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.08 | 22.51 | +28041.7% | +13.0035 to +31.8631 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006363 | 0.04155 | +553.0% | +0.0323 to +0.0380 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.3054 | 1.834 | +500.4% | +1.3331 to +1.7235 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01356 | +0.014 (native is 0) | +0.0127 to +0.0144 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.3054 | 1.847 | +504.8% | +1.3467 to +1.7370 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4032 | 657.2 | −83.7% | −3843.1638 to −2905.5430 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.343 | 4.131 | −4.9% | −0.4717 to +0.0480 | no |
| pods started | 1 | 0.5 | −50.0% | −1.5256 to +0.5256 | no |
| pod start wait, total (s) | 1.1 | 1.3 | +18.2% | −1.9539 to +2.3539 | no |
| pod start wait, mean (s) | 0.6 | 0.9 | +50.0% | −0.7144 to +1.3144 | no |
| host CPU busy, the real machine under kind (%) | 15.34 | 58.12 | +278.9% | +37.0859 to +48.4791 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 983.2 | −34.7% | −645.3580 to −400.8420 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.125 | −100.0% | −1161.2522 to −1157.7145 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.7 | −100.0% | −1477.1015 to −1473.2985 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 279.8 | −75.9% | −997.3383 to −762.2451 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.177 | −40.2% | −5.1659 to −4.4808 | yes: GAIN |
| node-hours | 5.024 | 3.013 | −40.0% | −2.1577 to −1.8633 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527.3 | 505.9 | −4.1% | −24.0534 to −18.7337 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.3 | 354 | −32.9% | −182.9305 to −163.6316 | yes: GAIN |
| response time (ms), mean | 845.8 | 75.09 | −91.1% | −1098.2722 to −443.1223 | yes: GAIN |
| response time (ms), 95th percentile | 3357 | 96.38 | −97.1% | −4699.9318 to −1821.2722 | yes: GAIN |
| response time (ms), 99th percentile | 4392 | 130 | −97.0% | −6141.4448 to −2382.3912 | yes: GAIN |
| time over the response line (% of samples) | 28.58 | 0 | −100.0% | −40.2742 to −16.8902 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.8 | 0 | −100.0% | −18.9449 to −8.6551 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +24.8674 to +29.1326 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 23.76 | 0.1067 | −99.6% | −34.6911 to −12.6155 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0377 | 0.009224 | −75.5% | −0.0321 to −0.0249 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.81 | 0.2655 | −85.3% | −1.7235 to −1.3647 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01014 | +0.010 (native is 0) | +0.0090 to +0.0112 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.81 | 0.2756 | −84.8% | −1.7123 to −1.3555 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 713.7 | 3249 | +355.2% | +2229.5820 to +2840.3725 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.05 | 4.53 | +11.9% | +0.1918 to +0.7696 | yes: power given |
| pods started | 0.2 | 2.2 | +1000.0% | +0.6097 to +3.3903 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.8 | +833.3% | +0.9456 to +4.0544 | yes: LOSS |
| pod start wait, mean (s) | 0.15 | 0.95 | +533.3% | +0.3476 to +1.2524 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 56.01 | 16.75 | −70.1% | −44.2871 to −34.2355 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 955.7 | 1509 | +57.9% | +442.7947 to +663.2053 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 1162 | +871315.6% | +1159.6068 to +1163.9015 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 1478 | +184662.5% | +1474.9626 to +1479.6374 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 261.4 | 1162 | +344.5% | +792.1946 to +1008.7721 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*