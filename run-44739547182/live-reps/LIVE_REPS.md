# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.809 | 6.461 |
| node-hours | 5.024 | 5.029 | 4.123 | 2.713 |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 504.7 | 527.1 | 505.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 504.7 | 458.1 | 331.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 487.9 | 116.3 | 575.8 | 68.79 |
| response time (ms), 95th percentile | 1810 | 160.3 | 2315 | 87.88 |
| response time (ms), 99th percentile | 2409 | 182.4 | 3103 | 115.4 |
| time over the response line (% of samples) | 18.97 | 0 | 23.74 | 0.00361 |
| failed requests (%) | 0 | 0 | 0.03213 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 0 | 12.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 161.3 | 35.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 30.42 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.23 | 0 | 15.03 | 0.08 |
| utilisation (used / allocatable) | 0.03344 | 0.005859 | 0.04168 | 0.009187 |
| CPU used (cores), mean | 1.605 | 0.2812 | 1.62 | 0.2372 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05488 | 0.03031 |
| CPU used with Omni's own (cores), mean | 1.605 | 0.2812 | 1.675 | 0.2675 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.3 | 4367 | 681.5 | 3406 |
| HPA replicas, mean | 4.02 | 4.167 | 4.652 | 4.722 |
| pods started | 0.1 | 0.9 | 3.1 | 2.9 |
| pod start wait, total (s) | 0.2 | 1.2 | 8.1 | 8.9 |
| pod start wait, mean (s) | 0.2 | 0.8 | 1.983 | 2.98 |
| host CPU busy, the real machine under kind (%) | 49 | 14.8 | 54.74 | 17.56 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 835.8 | 1507 | 877.2 | 1510 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.198 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1160 | 0.1083 | 1163 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1476 | 0.8 | 1479 |
| queue: job turnaround, submitted to done, mean (s) | 143.6 | 1160 | 182.8 | 1163 |
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
| worker nodes in service, mean | 12 | 6.461 | −46.2% | −6.0639 to −5.0134 | yes: GAIN |
| node-hours | 5.029 | 2.713 | −46.1% | −2.5382 to −2.0947 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.7 | 505.7 | +0.2% | +0.3284 to +1.6916 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.7 | 331.3 | −34.4% | −190.1004 to −156.6463 | yes: GAIN |
| response time (ms), mean | 116.3 | 68.79 | −40.8% | −56.1336 to −38.8236 | yes: GAIN |
| response time (ms), 95th percentile | 160.3 | 87.88 | −45.2% | −86.4426 to −58.4814 | yes: GAIN |
| response time (ms), 99th percentile | 182.4 | 115.4 | −36.7% | −80.4443 to −53.6233 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.00361 | +0.004 (native is 0) | −0.0046 to +0.0118 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.5 | +35.500 (native is 0) | +32.2613 to +38.7387 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.08 | +0.080 (native is 0) | −0.0487 to +0.2087 | no |
| utilisation (used / allocatable) | 0.005859 | 0.009187 | +56.8% | +0.0028 to +0.0039 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2812 | 0.2372 | −15.7% | −0.0533 to −0.0348 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03031 | +0.030 (native is 0) | +0.0267 to +0.0339 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2812 | 0.2675 | −4.9% | −0.0234 to −0.0041 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4367 | 3406 | −22.0% | −1093.5610 to −829.0427 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.167 | 4.722 | +13.3% | +0.2955 to +0.8141 | yes: power given |
| pods started | 0.9 | 2.9 | +222.2% | +0.3140 to +3.6860 | yes: power given |
| pod start wait, total (s) | 1.2 | 8.9 | +641.7% | −1.5717 to +16.9717 | no |
| pod start wait, mean (s) | 0.8 | 2.98 | +272.5% | −0.7870 to +5.1470 | no |
| host CPU busy, the real machine under kind (%) | 14.8 | 17.56 | +18.7% | +2.3107 to +3.2175 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1510 | +0.2% | +1.1333 to +4.6667 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1163 | +0.2% | +0.9194 to +4.4139 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1479 | +0.2% | +0.8056 to +4.1944 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1163 | +0.2% | +0.9194 to +4.4139 | yes: LOSS |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.024 | 5.029 | +0.1% | −0.0047 to +0.0140 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 504.7 | −3.8% | −22.8897 to −16.8133 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 504.7 | −3.8% | −22.8897 to −16.8133 | yes: GAIN |
| response time (ms), mean | 487.9 | 116.3 | −76.2% | −669.9317 to −73.2870 | yes: GAIN |
| response time (ms), 95th percentile | 1810 | 160.3 | −91.1% | −3020.1161 to −278.7929 | yes: GAIN |
| response time (ms), 99th percentile | 2409 | 182.4 | −92.4% | −3999.6276 to −454.4642 | yes: GAIN |
| time over the response line (% of samples) | 18.97 | 0 | −100.0% | −29.7838 to −8.1541 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 0 | −100.0% | −15.5901 to −6.0099 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.23 | 0 | −100.0% | −18.7928 to −7.6739 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03344 | 0.005859 | −82.5% | −0.0313 to −0.0238 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.605 | 0.2812 | −82.5% | −1.5034 to −1.1444 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.605 | 0.2812 | −82.5% | −1.5034 to −1.1444 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.3 | 4367 | +444.3% | +3182.3433 to +3947.0942 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.02 | 4.167 | +3.6% | −0.0101 to +0.3032 | no |
| pods started | 0.1 | 0.9 | +800.0% | +0.2358 to +1.3642 | yes: power given |
| pod start wait, total (s) | 0.2 | 1.2 | +500.0% | +0.3256 to +1.6744 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 0.8 | +300.0% | +0.0999 to +1.1001 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49 | 14.8 | −69.8% | −39.4329 to −28.9587 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.8 | 1507 | +80.3% | +570.2313 to +771.5687 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1160 | +2320308.3% | +1158.0048 to +1162.3035 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1476 | +492033.3% | +1473.8519 to +1478.3481 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.6 | 1160 | +708.2% | +918.2550 to +1115.0533 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.809 | −18.3% | −3.7176 to −0.6644 | yes: GAIN |
| node-hours | 5.024 | 4.123 | −17.9% | −1.5429 to −0.2589 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 527.1 | +0.5% | +1.1951 to +4.0123 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 458.1 | −12.7% | −114.9341 to −17.8460 | yes: GAIN |
| response time (ms), mean | 487.9 | 575.8 | +18.0% | +9.9184 to +165.8862 | yes: LOSS |
| response time (ms), 95th percentile | 1810 | 2315 | +27.9% | +164.2566 to +846.4944 | yes: LOSS |
| response time (ms), 99th percentile | 2409 | 3103 | +28.8% | +314.2552 to +1073.2380 | yes: LOSS |
| time over the response line (% of samples) | 18.97 | 23.74 | +25.2% | +2.4369 to +7.1120 | yes: LOSS |
| failed requests (%) | 0 | 0.03213 | +0.032 (native is 0) | −0.0405 to +0.1048 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 12.1 | +12.0% | −0.0509 to +2.6509 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161.3 | +161.300 (native is 0) | +57.7584 to +264.8416 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.23 | 15.03 | +13.6% | −1.6164 to +5.2064 | no |
| utilisation (used / allocatable) | 0.03344 | 0.04168 | +24.6% | +0.0029 to +0.0136 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.605 | 1.62 | +0.9% | −0.0391 to +0.0691 | no |
| Omni's own CPU (cores), mean | 0 | 0.05488 | +0.055 (native is 0) | +0.0503 to +0.0595 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.675 | +4.4% | +0.0128 to +0.1271 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.3 | 681.5 | −15.1% | −196.9914 to −44.7212 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.02 | 4.652 | +15.7% | +0.3409 to +0.9220 | yes: power given |
| pods started | 0.1 | 3.1 | +3000.0% | +1.4548 to +4.5452 | yes: power given |
| pod start wait, total (s) | 0.2 | 8.1 | +3950.0% | +3.4335 to +12.3665 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.983 | +891.7% | +0.9884 to +2.5782 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49 | 54.74 | +11.7% | +4.5759 to +6.9165 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.8 | 877.2 | +5.0% | +13.3168 to +69.4832 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.198 | −31.7% | −5.9136 to −1.6910 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.1083 | +116.7% | +0.0181 to +0.0986 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | +0.1230 to +0.8770 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.6 | 182.8 | +27.3% | +16.0400 to +62.4266 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.809 | −18.3% | −3.7176 to −0.6644 | yes: GAIN |
| node-hours | 5.029 | 4.123 | −18.0% | −1.5496 to −0.2615 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.7 | 527.1 | +4.4% | +18.6593 to +26.2511 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.7 | 458.1 | −9.2% | −97.8443 to +4.7672 | no |
| response time (ms), mean | 116.3 | 575.8 | +395.2% | +91.8877 to +827.1356 | yes: LOSS |
| response time (ms), 95th percentile | 160.3 | 2315 | +1343.9% | +532.1098 to +3777.5502 | yes: LOSS |
| response time (ms), 99th percentile | 182.4 | 3103 | +1601.1% | +815.6980 to +5025.8870 | yes: LOSS |
| time over the response line (% of samples) | 0 | 23.74 | +23.743 (native is 0) | +12.3801 to +35.1067 | yes: LOSS |
| failed requests (%) | 0 | 0.03213 | +0.032 (native is 0) | −0.0405 to +0.1048 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.1 | +12.100 (native is 0) | +7.1276 to +17.0724 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161.3 | +161.300 (native is 0) | +57.7584 to +264.8416 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 15.03 | +15.028 (native is 0) | +6.9766 to +23.0801 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005859 | 0.04168 | +611.3% | +0.0324 to +0.0393 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2812 | 1.62 | +476.1% | +1.1141 to +1.5639 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05488 | +0.055 (native is 0) | +0.0503 to +0.0595 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2812 | 1.675 | +495.6% | +1.1656 to +1.6220 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4367 | 681.5 | −84.4% | −4141.1917 to −3229.9584 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.167 | 4.652 | +11.6% | +0.1600 to +0.8097 | yes: power given |
| pods started | 0.9 | 3.1 | +244.4% | +0.6256 to +3.7744 | yes: power given |
| pod start wait, total (s) | 1.2 | 8.1 | +575.0% | +2.4208 to +11.3792 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 1.983 | +147.9% | +0.1373 to +2.2294 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.8 | 54.74 | +269.9% | +33.7024 to +46.1816 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 877.2 | −41.8% | −757.1196 to −501.8804 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.1083 | −100.0% | −1162.2481 to −1157.9436 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.8 | −99.9% | −1477.7380 to −1473.4620 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 182.8 | −84.2% | −1097.9628 to −856.8789 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.461 | −46.2% | −6.0639 to −5.0134 | yes: GAIN |
| node-hours | 5.024 | 2.713 | −46.0% | −2.5332 to −2.0904 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524.5 | 505.7 | −3.6% | −21.5784 to −16.1046 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524.5 | 331.3 | −36.8% | −208.9349 to −177.5148 | yes: GAIN |
| response time (ms), mean | 487.9 | 68.79 | −85.9% | −723.2303 to −114.9457 | yes: GAIN |
| response time (ms), 95th percentile | 1810 | 87.88 | −95.1% | −3097.4893 to −346.3437 | yes: GAIN |
| response time (ms), 99th percentile | 2409 | 115.4 | −95.2% | −4070.1327 to −518.0267 | yes: GAIN |
| time over the response line (% of samples) | 18.97 | 0.00361 | −100.0% | −29.7769 to −8.1539 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 0 | −100.0% | −15.5901 to −6.0099 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.5 | +35.500 (native is 0) | +32.2613 to +38.7387 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.23 | 0.08 | −99.4% | −18.7538 to −7.5528 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03344 | 0.009187 | −72.5% | −0.0278 to −0.0207 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.605 | 0.2372 | −85.2% | −1.5473 to −1.1887 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03031 | +0.030 (native is 0) | +0.0267 to +0.0339 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 0.2675 | −83.3% | −1.5137 to −1.1617 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 802.3 | 3406 | +324.5% | +2299.2651 to +2907.5686 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.02 | 4.722 | +17.4% | +0.4296 to +0.9730 | yes: power given |
| pods started | 0.1 | 2.9 | +2800.0% | +1.5028 to +4.0972 | yes: power given |
| pod start wait, total (s) | 0.2 | 8.9 | +4350.0% | −0.6875 to +18.0875 | no |
| pod start wait, mean (s) | 0.2 | 2.98 | +1390.0% | +0.0307 to +5.5293 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49 | 17.56 | −64.2% | −36.2688 to −26.5946 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.8 | 1510 | +80.6% | +572.5685 to +775.0315 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 1163 | +2325641.7% | +1160.1058 to +1165.5358 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1479 | +492866.7% | +1475.9837 to +1481.2163 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 143.6 | 1163 | +710.1% | +920.5282 to +1118.1135 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*