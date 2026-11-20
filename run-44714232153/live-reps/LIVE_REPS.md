# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.306 | 4.376 |
| node-hours | 2.517 | 2.518 | 1.803 | 1.834 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | 270.5 | 271.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.3 | 217.3 | 220.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 255.4 | 281.4 | 239.7 | 266 |
| response time (ms), 95th percentile | 829.5 | 1060 | 944.8 | 1118 |
| response time (ms), 99th percentile | 1156 | 1458 | 1349 | 1560 |
| time over the response line (% of samples) | 8.129 | 8.001 | 9.442 | 9.571 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 6.1 | 7.3 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 155.7 | 115.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 7.917 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.382 | 20.09 | 9.977 | 20.64 |
| utilisation (used / allocatable) | 0.05473 | 0.05584 | 0.07727 | 0.07803 |
| CPU used (cores), mean | 1.314 | 1.34 | 1.31 | 1.338 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07108 | 0.07349 |
| CPU used with Omni's own (cores), mean | 1.314 | 1.34 | 1.381 | 1.412 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.5 | 502.3 | 400.9 | 393.5 |
| HPA replicas, mean | 2.127 | 2.022 | 2.221 | 2.145 |
| pods started | 0 | 0 | 0.8 | 0.7 |
| pod start wait, total (s) | 0 | 0 | 1.9 | 0.9 |
| pod start wait, mean (s) | 0 | 0 | 0.875 | 0.3667 |
| host CPU busy, the real machine under kind (%) | 38.33 | 40.64 | 41.27 | 43.71 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 756.6 | 782.3 | 762.9 | 784.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.411 | 3.343 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.8167 | 0.07917 | 0.8875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 2 | 0.3 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 62.68 | 85.27 | 67.5 | 90.52 |
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
| worker nodes in service, mean | 6 | 4.376 | −27.1% | −2.4479 to −0.8009 | yes: GAIN |
| node-hours | 2.518 | 1.834 | −27.1% | −1.0303 to −0.3366 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.1 | −0.1% | −1.3922 to +1.0554 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 220.1 | −18.9% | −76.9687 to −25.3807 | yes: GAIN |
| response time (ms), mean | 281.4 | 266 | −5.5% | −40.6902 to +9.8668 | no |
| response time (ms), 95th percentile | 1060 | 1118 | +5.5% | −58.9787 to +175.3237 | no |
| response time (ms), 99th percentile | 1458 | 1560 | +7.0% | −95.7439 to +299.0085 | no |
| time over the response line (% of samples) | 8.001 | 9.571 | +19.6% | −0.2823 to +3.4216 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 7.3 | +19.7% | −0.8456 to +3.2456 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.3 | +115.300 (native is 0) | +53.3837 to +177.2163 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.09 | 20.63 | +2.7% | −3.6107 to +4.7073 | no |
| utilisation (used / allocatable) | 0.05584 | 0.07803 | +39.7% | +0.0093 to +0.0351 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.34 | 1.338 | −0.2% | −0.0561 to +0.0519 | no |
| Omni's own CPU (cores), mean | 0 | 0.07349 | +0.073 (native is 0) | +0.0671 to +0.0799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.34 | 1.412 | +5.3% | +0.0178 to +0.1249 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 502.3 | 393.5 | −21.7% | −183.6175 to −34.0137 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.145 | +6.1% | −0.1627 to +0.4081 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.2898 to +2.0898 | no |
| pod start wait, mean (s) | 0 | 0.3667 | +0.367 (native is 0) | −0.0751 to +0.8085 | no |
| host CPU busy, the real machine under kind (%) | 40.64 | 43.71 | +7.5% | +2.5123 to +3.6235 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 784.4 | +0.3% | −7.1926 to +11.3926 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.343 | −44.3% | −3.8443 to −1.4704 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8167 | 0.8875 | +8.7% | −0.0181 to +0.1597 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 2.1 | +5.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 85.27 | 90.52 | +6.2% | −2.5497 to +13.0414 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.518 | +0.0% | −0.0077 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.3 | +0.2% | −0.1084 to +1.0433 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 271.3 | +0.2% | −0.1084 to +1.0433 | no |
| response time (ms), mean | 255.4 | 281.4 | +10.2% | −14.0545 to +65.9240 | no |
| response time (ms), 95th percentile | 829.5 | 1060 | +27.8% | −106.8588 to +567.8038 | no |
| response time (ms), 99th percentile | 1156 | 1458 | +26.2% | −71.6689 to +677.4349 | no |
| time over the response line (% of samples) | 8.129 | 8.001 | −1.6% | −2.7115 to +2.4561 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 6.1 | ±0.0% | −1.7194 to +1.7194 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.382 | 20.09 | +114.1% | +1.2498 to +20.1602 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05473 | 0.05584 | +2.0% | −0.0004 to +0.0026 | no |
| CPU used (cores), mean | 1.314 | 1.34 | +2.0% | −0.0096 to +0.0628 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.314 | 1.34 | +2.0% | −0.0096 to +0.0628 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.5 | 502.3 | −1.2% | −24.5514 to +12.0648 | no |
| HPA replicas, mean | 2.127 | 2.022 | −4.9% | −0.4469 to +0.2367 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 38.33 | 40.64 | +6.0% | +1.2482 to +3.3727 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 756.6 | 782.3 | +3.4% | −2.0653 to +53.4653 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.8167 | +3820.0% | +0.5491 to +1.0426 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 2 | +1900.0% | +0.5324 to +3.2676 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 62.68 | 85.27 | +36.0% | +1.6109 to +43.5641 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.306 | −28.2% | −2.5384 to −0.8496 | yes: GAIN |
| node-hours | 2.517 | 1.803 | −28.4% | −1.0646 to −0.3635 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 270.5 | −0.1% | −0.9324 to +0.3900 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 217.3 | −19.7% | −79.9350 to −27.0116 | yes: GAIN |
| response time (ms), mean | 255.4 | 239.7 | −6.2% | −25.5307 to −5.9000 | yes: GAIN |
| response time (ms), 95th percentile | 829.5 | 944.8 | +13.9% | +13.5700 to +216.9760 | yes: LOSS |
| response time (ms), 99th percentile | 1156 | 1349 | +16.7% | +36.1214 to +349.8574 | yes: LOSS |
| time over the response line (% of samples) | 8.129 | 9.442 | +16.1% | −0.9280 to +3.5530 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 7.3 | +19.7% | +0.5427 to +1.8573 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 155.7 | +155.700 (native is 0) | +70.8229 to +240.5771 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.382 | 9.977 | +6.3% | −0.5863 to +1.7763 | no |
| utilisation (used / allocatable) | 0.05473 | 0.07727 | +41.2% | +0.0117 to +0.0334 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.314 | 1.31 | −0.3% | −0.0343 to +0.0276 | no |
| Omni's own CPU (cores), mean | 0 | 0.07108 | +0.071 (native is 0) | +0.0643 to +0.0778 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.314 | 1.381 | +5.2% | +0.0324 to +0.1030 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.5 | 400.9 | −21.2% | −161.2411 to −54.0142 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.127 | 2.221 | +4.4% | −0.3189 to +0.5072 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | −0.5882 to +4.3882 | no |
| pod start wait, mean (s) | 0 | 0.875 | +0.875 (native is 0) | +0.0523 to +1.6977 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.33 | 41.27 | +7.7% | +2.3940 to +3.4722 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 756.6 | 762.9 | +0.8% | +0.1462 to +12.4538 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.411 | −43.2% | −3.7284 to −1.4501 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.07917 | +280.0% | +0.0036 to +0.1131 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.68 | 67.5 | +7.7% | −0.1909 to +9.8242 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.306 | −28.2% | −2.5384 to −0.8496 | yes: GAIN |
| node-hours | 2.518 | 1.803 | −28.4% | −1.0685 to −0.3602 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 270.5 | −0.3% | −1.5675 to +0.0902 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 217.3 | −19.9% | −80.6038 to −27.2776 | yes: GAIN |
| response time (ms), mean | 281.4 | 239.7 | −14.8% | −78.6357 to −4.6644 | yes: GAIN |
| response time (ms), 95th percentile | 1060 | 944.8 | −10.9% | −368.8849 to +138.4859 | no |
| response time (ms), 99th percentile | 1458 | 1349 | −7.5% | −338.9957 to +119.2085 | no |
| time over the response line (% of samples) | 8.001 | 9.442 | +18.0% | +0.0149 to +2.8655 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 7.3 | +19.7% | −0.7604 to +3.1604 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 155.7 | +155.700 (native is 0) | +70.8229 to +240.5771 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.09 | 9.977 | −50.3% | −20.0550 to −0.1650 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05584 | 0.07727 | +38.4% | +0.0100 to +0.0329 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.34 | 1.31 | −2.2% | −0.0668 to +0.0069 | no |
| Omni's own CPU (cores), mean | 0 | 0.07108 | +0.071 (native is 0) | +0.0643 to +0.0778 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.34 | 1.381 | +3.1% | +0.0028 to +0.0794 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 502.3 | 400.9 | −20.2% | −164.0643 to −38.7045 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.022 | 2.221 | +9.9% | −0.0853 to +0.4839 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.1417 to +1.7417 | no |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | −0.5882 to +4.3882 | no |
| pod start wait, mean (s) | 0 | 0.875 | +0.875 (native is 0) | +0.0523 to +1.6977 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.64 | 41.27 | +1.5% | −0.0463 to +1.2916 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.3 | 762.9 | −2.5% | −41.5455 to +2.7455 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.411 | −43.2% | −3.7284 to −1.4501 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8167 | 0.07917 | −90.3% | −0.9377 to −0.5373 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2 | 0.3 | −85.0% | −2.8705 to −0.5295 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 85.27 | 67.5 | −20.8% | −34.2120 to −1.3297 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.376 | −27.1% | −2.4479 to −0.8009 | yes: GAIN |
| node-hours | 2.517 | 1.834 | −27.1% | −1.0269 to −0.3393 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.8 | 271.1 | +0.1% | −0.5512 to +1.1492 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.8 | 220.1 | −18.7% | −76.3378 to −25.0767 | yes: GAIN |
| response time (ms), mean | 255.4 | 266 | +4.1% | −28.9742 to +50.0202 | no |
| response time (ms), 95th percentile | 829.5 | 1118 | +34.8% | −34.2178 to +611.5078 | no |
| response time (ms), 99th percentile | 1156 | 1560 | +35.0% | +32.4480 to +776.5826 | yes: LOSS |
| time over the response line (% of samples) | 8.129 | 9.571 | +17.7% | −2.0965 to +4.9803 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.1 | 7.3 | +19.7% | +0.2583 to +2.1417 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115.3 | +115.300 (native is 0) | +53.3837 to +177.2163 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.382 | 20.63 | +120.0% | +1.5021 to +21.0045 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05473 | 0.07803 | +42.6% | +0.0110 to +0.0356 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.314 | 1.338 | +1.9% | −0.0089 to +0.0578 | no |
| Omni's own CPU (cores), mean | 0 | 0.07349 | +0.073 (native is 0) | +0.0671 to +0.0799 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.314 | 1.412 | +7.5% | +0.0650 to +0.1308 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 508.5 | 393.5 | −22.6% | −180.7261 to −49.3917 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.127 | 2.145 | +0.8% | −0.3754 to +0.4106 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.2898 to +2.0898 | no |
| pod start wait, mean (s) | 0 | 0.3667 | +0.367 (native is 0) | −0.0751 to +0.8085 | no |
| host CPU busy, the real machine under kind (%) | 38.33 | 43.71 | +14.0% | +4.3315 to +6.4252 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 756.6 | 784.4 | +3.7% | −0.9111 to +56.5111 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.343 | −44.3% | −3.8443 to −1.4704 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 0.8875 | +4160.0% | +0.5826 to +1.1507 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 2.1 | +2000.0% | +0.6512 to +3.3488 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 62.68 | 90.52 | +44.4% | +4.5543 to +51.1123 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*