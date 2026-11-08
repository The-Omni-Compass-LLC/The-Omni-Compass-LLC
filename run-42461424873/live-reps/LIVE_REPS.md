# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.876 | 6 |
| node-hours | 2.515 | 2.512 | 2.046 | 2.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.3 | 272.5 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.3 | 237.2 | 272.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 313.4 | 143.8 | 303.4 | 118.5 |
| response time (ms), 95th percentile | 1067 | 249.2 | 1243 | 260.9 |
| response time (ms), 99th percentile | 1548 | 354.6 | 1765 | 384.4 |
| time over the response line (% of samples) | 13.84 | 0.2056 | 13.89 | 0.3008 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 0 | 9.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 138.6 | 110.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.882 | 1264 | 9.64 | 1299 |
| utilisation (used / allocatable) | 0.05857 | 0.06143 | 0.07388 | 0.0598 |
| CPU used (cores), mean | 1.406 | 1.474 | 1.419 | 1.435 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07157 | 0.0721 |
| CPU used with Omni's own (cores), mean | 1.406 | 1.474 | 1.49 | 1.507 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.8 | 441.7 | 401.5 | 452.6 |
| HPA replicas, mean | 1.96 | 2.117 | 2.238 | 2.046 |
| pods started | 0 | 0 | 1.5 | 0 |
| pod start wait, total (s) | 0 | 0 | 4 | 0 |
| pod start wait, mean (s) | 0 | 0 | 2.025 | 0 |
| host CPU busy, the real machine under kind (%) | 40.06 | 45.84 | 43.55 | 47.63 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 767.3 | 1507 | 778.4 | 1512 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 4.037 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 163.5 | 0.05 | 225.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 714.2 | 0.3 | 746.5 |
| queue: job turnaround, submitted to done, mean (s) | 73.82 | 904.5 | 83.61 | 938.4 |
| queue: jobs unfinished at the window's end | 0 | 11.83 | 0 | 14.5 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 1 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw ±nan to ±nan | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.522 | +0.2% | ±nan to ±nan | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.5 | +0.2% | ±nan to ±nan | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.5 | +0.2% | ±nan to ±nan | no |
| response time (ms), mean | 154.8 | 134.8 | −12.9% | ±nan to ±nan | no |
| response time (ms), 95th percentile | 249.5 | 312 | +25.1% | ±nan to ±nan | no |
| response time (ms), 99th percentile | 385.6 | 443.4 | +15.0% | ±nan to ±nan | no |
| time over the response line (% of samples) | 0.2308 | 0.5283 | +128.9% | ±nan to ±nan | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 135 | +135.000 (native is 0) | ±nan to ±nan | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1278 | 1514 | +18.4% | ±nan to ±nan | no |
| utilisation (used / allocatable) | 0.06311 | 0.06097 | −3.4% | ±nan to ±nan | no |
| CPU used (cores), mean | 1.515 | 1.463 | −3.4% | ±nan to ±nan | no |
| Omni's own CPU (cores), mean | 0 | 0.0829 | +0.083 (native is 0) | ±nan to ±nan | no |
| CPU used with Omni's own (cores), mean | 1.515 | 1.546 | +2.1% | ±nan to ±nan | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.8 | 444.7 | +3.5% | ±nan to ±nan | no |
| HPA replicas, mean | 2.184 | 2.154 | −1.4% | ±nan to ±nan | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±nan to ±nan | no |
| host CPU busy, the real machine under kind (%) | 46.33 | 49.56 | +7.0% | ±nan to ±nan | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±nan to ±nan | no |
| batch: queue finished (s) | 1510 | 1514 | +0.3% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 273 | 303.5 | +11.2% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 906 | 872 | −3.8% | ±nan to ±nan | no |
| queue: job turnaround, submitted to done, mean (s) | 872.8 | 1018 | +16.7% | ±nan to ±nan | no |
| queue: jobs unfinished at the window's end | 15 | 20 | +33.3% | ±nan to ±nan | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 6 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.512 | −0.2% | −0.0135 to +0.0051 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 272.3 | −0.5% | −4.3827 to +1.6612 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 272.3 | −0.5% | −4.3827 to +1.6612 | no |
| response time (ms), mean | 415.7 | 143.8 | −65.4% | −469.7727 to −73.9959 | yes: GAIN |
| response time (ms), 95th percentile | 1519 | 249.2 | −83.6% | −2187.6200 to −351.2150 | yes: GAIN |
| response time (ms), 99th percentile | 2206 | 354.6 | −83.9% | −3186.2078 to −517.2782 | yes: GAIN |
| time over the response line (% of samples) | 21.57 | 0.2056 | −99.0% | −37.7767 to −4.9510 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.33 | 0 | −100.0% | −16.6193 to −4.0474 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 1264 | +12177.3% | +980.8723 to +1526.9777 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06293 | 0.06143 | −2.4% | −0.0097 to +0.0067 | no |
| CPU used (cores), mean | 1.51 | 1.474 | −2.4% | −0.2319 to +0.1597 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.51 | 1.474 | −2.4% | −0.2319 to +0.1597 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.9 | 441.7 | +0.2% | −58.5629 to +60.0990 | no |
| HPA replicas, mean | 1.97 | 2.117 | +7.5% | −0.0439 to +0.3391 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.99 | 45.84 | +6.6% | −2.0338 to +7.7387 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 797 | 1507 | +89.1% | +652.0347 to +768.6320 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 163.5 | +261444.4% | +88.3972 to +238.4083 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 714.2 | +142733.3% | +502.1584 to +925.1749 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 103.4 | 904.5 | +774.5% | +716.5282 to +885.6662 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.83 | +11.833 (native is 0) | +3.1675 to +20.4992 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.876 | −18.7% | −1.7914 to −0.4572 | yes: GAIN |
| node-hours | 2.515 | 2.046 | −18.6% | −0.7528 to −0.1851 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.5 | +0.2% | −0.3812 to +1.4905 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 237.2 | −12.8% | −56.2481 to −13.3052 | yes: GAIN |
| response time (ms), mean | 313.4 | 303.4 | −3.2% | −25.5058 to +5.6030 | no |
| response time (ms), 95th percentile | 1067 | 1243 | +16.5% | +42.6282 to +309.6088 | yes: LOSS |
| response time (ms), 99th percentile | 1548 | 1765 | +14.0% | +13.1414 to +420.0998 | yes: LOSS |
| time over the response line (% of samples) | 13.84 | 13.89 | +0.3% | −1.0327 to +1.1266 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 9.5 | +14.5% | +0.0417 to +2.3583 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.6 | +138.600 (native is 0) | +65.3880 to +211.8120 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.882 | 9.64 | +8.5% | −1.3565 to +2.8732 | no |
| utilisation (used / allocatable) | 0.05857 | 0.07388 | +26.1% | +0.0058 to +0.0248 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.406 | 1.419 | +0.9% | −0.0101 to +0.0360 | no |
| Omni's own CPU (cores), mean | 0 | 0.07157 | +0.072 (native is 0) | +0.0655 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.406 | 1.49 | +6.0% | +0.0583 to +0.1107 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.8 | 401.5 | −14.7% | −110.3956 to −28.2069 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.96 | 2.238 | +14.2% | +0.1366 to +0.4205 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.6570 to +2.3430 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +0.9095 to +7.0905 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.025 | +2.025 (native is 0) | +1.0048 to +3.0452 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.06 | 43.55 | +8.7% | +3.1582 to +3.8137 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 767.3 | 778.4 | +1.4% | +2.4935 to +19.7065 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.037 | −32.7% | −2.8941 to −1.0312 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.05 | 0.0% | raw −0.0344 to +0.0344 | STEADY, the same (to nine decimal places) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 73.82 | 83.61 | +13.3% | +1.1174 to +18.4659 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 6 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.108 | −14.9% | −1.7744 to −0.0096 | yes: GAIN |
| node-hours | 2.512 | 2.145 | −14.6% | −0.7422 to +0.0070 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 274.3 | +0.7% | −1.5180 to +5.5382 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 246.3 | −9.6% | −56.4663 to +4.3892 | no |
| response time (ms), mean | 143.8 | 416.9 | +189.8% | +60.8181 to +485.2168 | yes: LOSS |
| response time (ms), 95th percentile | 249.2 | 1795 | +620.3% | +462.3016 to +2629.0784 | yes: LOSS |
| response time (ms), 99th percentile | 354.6 | 2556 | +621.0% | +635.4217 to +3768.1566 | yes: LOSS |
| time over the response line (% of samples) | 0.2056 | 21.24 | +10228.1% | +5.5921 to +36.4719 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.33 | +11.333 (native is 0) | +5.2977 to +17.3690 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.83 | +95.833 (native is 0) | −14.9793 to +206.6460 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1264 | 11.41 | −99.1% | −1526.2111 to −979.4167 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06143 | 0.07539 | +22.7% | +0.0048 to +0.0231 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.474 | 1.531 | +3.8% | −0.1436 to +0.2566 | no |
| Omni's own CPU (cores), mean | 0 | 0.07498 | +0.075 (native is 0) | +0.0659 to +0.0841 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.474 | 1.606 | +8.9% | −0.0770 to +0.3400 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 441.7 | 386.1 | −12.6% | −91.7574 to −19.5707 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.117 | 2.296 | +8.5% | −0.0717 to +0.4296 | no |
| pods started | 0 | 1.833 | +1.833 (native is 0) | +0.4382 to +3.2284 | yes: power given |
| pod start wait, total (s) | 0 | 5.333 | +5.333 (native is 0) | −0.0460 to +10.7127 | no |
| pod start wait, mean (s) | 0 | 2.292 | +2.292 (native is 0) | +0.9190 to +3.6644 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.84 | 46.54 | +1.5% | −4.3738 to +5.7697 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 813.7 | −46.0% | −764.9771 to −622.3562 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 163.5 | 0.07639 | −100.0% | −238.3906 to −88.3872 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 714.2 | 0.5 | −99.9% | −925.0988 to −502.2345 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 904.5 | 119 | −86.8% | −858.6101 to −712.4177 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.83 | 0 | −100.0% | −20.4992 to −3.1675 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 2 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.519 | +0.4% | −0.0014 to +0.0198 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.6 | +0.1% | −33.5500 to +34.1200 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.6 | +0.1% | −33.5500 to +34.1200 | no |
| response time (ms), mean | 377.5 | 118.5 | −68.6% | −2637.9536 to +2119.8417 | no |
| response time (ms), 95th percentile | 1300 | 260.9 | −79.9% | −11780.6924 to +9702.6124 | no |
| response time (ms), 99th percentile | 1840 | 384.4 | −79.1% | −16477.7037 to +13567.3487 | no |
| time over the response line (% of samples) | 18.12 | 0.3008 | −98.3% | −215.3710 to +179.7341 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 0 | −100.0% | −66.6770 to +47.6770 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.5 | +110.500 (native is 0) | −200.7970 to +421.7970 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.583 | 1299 | +13453.1% | −1410.6608 to +3989.1774 | no |
| utilisation (used / allocatable) | 0.06103 | 0.0598 | −2.0% | −0.0955 to +0.0930 | no |
| CPU used (cores), mean | 1.465 | 1.435 | −2.0% | −2.2918 to +2.2327 | no |
| Omni's own CPU (cores), mean | 0 | 0.0721 | +0.072 (native is 0) | −0.0651 to +0.2093 | no |
| CPU used with Omni's own (cores), mean | 1.465 | 1.507 | +2.9% | −2.0824 to +2.1675 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.7 | 452.6 | −0.0% | −644.0223 to +643.7943 | no |
| HPA replicas, mean | 2.069 | 2.046 | −1.1% | −0.0525 to +0.0070 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.15 | 47.63 | +13.0% | −39.7709 to +50.7240 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783 | 1512 | +93.1% | −7.9480 to +1465.9480 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02083 | 225.6 | +1082700.0% | −764.1820 to +1215.3070 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0 | 746.5 | +746.500 (native is 0) | −848.1030 to +2341.1030 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.88 | 938.4 | +921.4% | +621.8251 to +1071.2999 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 14.5 | +14.500 (native is 0) | −55.3830 to +84.3830 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*