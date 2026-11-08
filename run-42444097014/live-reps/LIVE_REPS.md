# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.201 | 4.909 |
| node-hours | 2.514 | 2.515 | 2.181 | 2.06 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.4 | 273.6 | 273.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273.4 | 248.4 | 239.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 377.1 | 311.8 | 360.5 | 303.9 |
| response time (ms), 95th percentile | 1339 | 1098 | 1494 | 1319 |
| response time (ms), 99th percentile | 1879 | 1757 | 2011 | 1975 |
| time over the response line (% of samples) | 16.04 | 11.16 | 16.59 | 11.76 |
| failed requests (%) | 0 | 0 | 0 | 0.0101 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 6.8 | 10.5 | 7.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 106.9 | 95.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 5 | 66.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.87 | 17.61 | 13.41 | 19.83 |
| utilisation (used / allocatable) | 0.06197 | 0.06285 | 0.07253 | 0.07678 |
| CPU used (cores), mean | 1.487 | 1.508 | 1.491 | 1.5 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07321 | 0.07614 |
| CPU used with Omni's own (cores), mean | 1.487 | 1.508 | 1.564 | 1.576 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.9 | 442.5 | 401.2 | 383 |
| HPA replicas, mean | 2.016 | 2.044 | 2.321 | 2.094 |
| pods started | 0 | 0.1 | 1.6 | 0.8 |
| pod start wait, total (s) | 0 | 0.2 | 3.3 | 2.1 |
| pod start wait, mean (s) | 0 | 0.2 | 1.517 | 0.75 |
| host CPU busy, the real machine under kind (%) | 42.69 | 43.71 | 45.7 | 46.88 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 794.2 | 805.4 | 802 | 813.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.678 | 4.083 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.8417 | 0.25 | 0.8583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.5 | 1.6 | 2.4 |
| queue: job turnaround, submitted to done, mean (s) | 99.91 | 115.4 | 107 | 124 |
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
| worker nodes in service, mean | 6 | 4.909 | −18.2% | −1.8263 to −0.3553 | yes: GAIN |
| node-hours | 2.515 | 2.06 | −18.1% | −0.7646 to −0.1440 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.9 | +0.2% | −0.3638 to +1.4293 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 239.5 | −12.4% | −57.4749 to −10.2305 | yes: GAIN |
| response time (ms), mean | 311.8 | 303.9 | −2.6% | −23.6232 to +7.6920 | no |
| response time (ms), 95th percentile | 1098 | 1319 | +20.1% | +9.6335 to +432.8215 | yes: LOSS |
| response time (ms), 99th percentile | 1757 | 1975 | +12.4% | −5.4233 to +441.4557 | no |
| time over the response line (% of samples) | 11.16 | 11.76 | +5.4% | −0.7268 to +1.9299 | no |
| failed requests (%) | 0 | 0.0101 | +0.010 (native is 0) | −0.0127 to +0.0329 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.8 | +14.7% | −0.6519 to +2.6519 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.4 | +95.400 (native is 0) | +42.1682 to +148.6318 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.61 | 19.83 | +12.6% | −0.7316 to +5.1783 | no |
| utilisation (used / allocatable) | 0.06285 | 0.07678 | +22.2% | +0.0051 to +0.0228 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.508 | 1.5 | −0.6% | −0.0383 to +0.0215 | no |
| Omni's own CPU (cores), mean | 0 | 0.07614 | +0.076 (native is 0) | +0.0690 to +0.0833 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.508 | 1.576 | +4.5% | +0.0310 to +0.1045 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.5 | 383 | −13.4% | −97.4532 to −21.4743 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.044 | 2.094 | +2.5% | −0.1844 to +0.2848 | no |
| pods started | 0.1 | 0.8 | +700.0% | −0.4209 to +1.8209 | no |
| pod start wait, total (s) | 0.2 | 2.1 | +950.0% | −1.0483 to +4.8483 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | −0.5223 to +1.6223 | no |
| host CPU busy, the real machine under kind (%) | 43.71 | 46.88 | +7.3% | +2.7459 to +3.5973 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.4 | 813.7 | +1.0% | +2.9786 to +13.6214 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.083 | −32.0% | −3.1402 to −0.6947 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8417 | 0.8583 | +2.0% | −0.1544 to +0.1877 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 2.4 | −4.0% | −1.0204 to +0.8204 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.4 | 124 | +7.4% | +2.1068 to +14.9766 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.515 | +0.0% | −0.0088 to +0.0095 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.4 | +0.1% | −0.6579 to +1.1356 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 273.4 | +0.1% | −0.6579 to +1.1356 | no |
| response time (ms), mean | 377.1 | 311.8 | −17.3% | −99.4776 to −31.0057 | yes: GAIN |
| response time (ms), 95th percentile | 1339 | 1098 | −17.9% | −355.6500 to −124.8540 | yes: GAIN |
| response time (ms), 99th percentile | 1879 | 1757 | −6.5% | −258.4283 to +14.7599 | no |
| time over the response line (% of samples) | 16.04 | 11.16 | −30.4% | −7.8202 to −1.9468 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 6.8 | −29.2% | −4.9273 to −0.6727 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.87 | 17.6 | +61.9% | +3.1814 to +10.2819 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06197 | 0.06285 | +1.4% | +0.0004 to +0.0014 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.508 | +1.4% | +0.0090 to +0.0336 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.487 | 1.508 | +1.4% | +0.0090 to +0.0336 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.9 | 442.5 | −1.2% | −7.8880 to −2.9805 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.044 | +1.4% | −0.1630 to +0.2187 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 42.69 | 43.71 | +2.4% | +0.5516 to +1.4770 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.2 | 805.4 | +1.4% | +1.4573 to +20.9427 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.8417 | +648.1% | +0.4877 to +0.9706 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.5 | +177.8% | +0.6344 to +2.5656 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 99.91 | 115.4 | +15.5% | +3.3215 to +27.7452 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.201 | −13.3% | −1.4720 to −0.1261 | yes: GAIN |
| node-hours | 2.514 | 2.181 | −13.3% | −0.6156 to −0.0509 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.6 | +0.2% | −0.4393 to +1.3285 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 248.4 | −9.0% | −45.8252 to −3.5731 | yes: GAIN |
| response time (ms), mean | 377.1 | 360.5 | −4.4% | −23.0987 to −10.1691 | yes: GAIN |
| response time (ms), 95th percentile | 1339 | 1494 | +11.6% | +36.4356 to +274.9604 | yes: LOSS |
| response time (ms), 99th percentile | 1879 | 2011 | +7.0% | +25.3932 to +237.8366 | yes: LOSS |
| time over the response line (% of samples) | 16.04 | 16.59 | +3.4% | −0.1459 to +1.2409 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.5 | +9.4% | +0.1128 to +1.6872 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.9 | +106.900 (native is 0) | +40.9791 to +172.8209 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.87 | 13.41 | +23.3% | +0.2314 to +4.8386 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06197 | 0.07253 | +17.0% | +0.0005 to +0.0206 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.491 | +0.2% | −0.0173 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.07321 | +0.073 (native is 0) | +0.0670 to +0.0794 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.564 | +5.2% | +0.0556 to +0.0976 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.9 | 401.2 | −10.4% | −88.5015 to −4.9372 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.321 | +15.1% | +0.0234 to +0.5866 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.5772 to +2.6228 | yes: power given |
| pod start wait, total (s) | 0 | 3.3 | +3.300 (native is 0) | +1.2475 to +5.3525 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.517 | +1.517 (native is 0) | +0.6956 to +2.3377 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.69 | 45.7 | +7.0% | +2.6174 to +3.3949 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.2 | 802 | +1.0% | +0.1048 to +15.4952 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.678 | −22.0% | −2.3496 to −0.2945 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.25 | +122.2% | −0.0079 to +0.2829 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.6 | +77.8% | −0.0578 to +1.4578 | no |
| queue: job turnaround, submitted to done, mean (s) | 99.91 | 107 | +7.1% | +2.4149 to +11.7268 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.201 | −13.3% | −1.4720 to −0.1261 | yes: GAIN |
| node-hours | 2.515 | 2.181 | −13.3% | −0.6195 to −0.0477 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 | +0.1% | −0.6285 to +1.0399 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 248.4 | −9.1% | −46.3612 to −3.5149 | yes: GAIN |
| response time (ms), mean | 311.8 | 360.5 | +15.6% | +11.1597 to +86.0559 | yes: LOSS |
| response time (ms), 95th percentile | 1098 | 1494 | +36.1% | +178.0133 to +613.8867 | yes: LOSS |
| response time (ms), 99th percentile | 1757 | 2011 | +14.4% | +126.2657 to +380.6325 | yes: LOSS |
| time over the response line (% of samples) | 11.16 | 16.59 | +48.7% | +2.3423 to +8.5197 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 10.5 | +54.4% | +0.8180 to +6.5820 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 106.9 | +106.900 (native is 0) | +40.9791 to +172.8209 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.61 | 13.41 | −23.8% | −6.2400 to −2.1533 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06285 | 0.07253 | +15.4% | −0.0005 to +0.0198 | no |
| CPU used (cores), mean | 1.508 | 1.491 | −1.2% | −0.0361 to +0.0003 | no |
| Omni's own CPU (cores), mean | 0 | 0.07321 | +0.073 (native is 0) | +0.0670 to +0.0794 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.508 | 1.564 | +3.7% | +0.0369 to +0.0737 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 442.5 | 401.2 | −9.3% | −82.8435 to +0.2733 | no |
| HPA replicas, mean | 2.044 | 2.321 | +13.6% | +0.0891 to +0.4653 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.3690 to +2.6310 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.3 | +1550.0% | +0.8267 to +5.3733 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.517 | +658.3% | +0.2104 to +2.4229 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.71 | 45.7 | +4.6% | +1.7422 to +2.2415 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 805.4 | 802 | −0.4% | −7.1730 to +0.3730 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.678 | −22.0% | −2.3496 to −0.2945 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8417 | 0.25 | −70.3% | −0.8449 to −0.3385 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.5 | 1.6 | −36.0% | −2.2676 to +0.4676 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.4 | 107 | −7.3% | −16.3976 to −0.5274 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.909 | −18.2% | −1.8263 to −0.3553 | yes: GAIN |
| node-hours | 2.514 | 2.06 | −18.1% | −0.7609 to −0.1471 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.9 | +0.3% | +0.3091 to +1.2341 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 239.5 | −12.3% | −56.9814 to −10.2462 | yes: GAIN |
| response time (ms), mean | 377.1 | 303.9 | −19.4% | −99.6535 to −46.7609 | yes: GAIN |
| response time (ms), 95th percentile | 1339 | 1319 | −1.4% | −151.6009 to +113.5519 | no |
| response time (ms), 99th percentile | 1879 | 1975 | +5.1% | −142.9468 to +335.3108 | no |
| time over the response line (% of samples) | 16.04 | 11.76 | −26.7% | −7.2779 to −1.2859 | yes: GAIN |
| failed requests (%) | 0 | 0.0101 | +0.010 (native is 0) | −0.0127 to +0.0329 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 7.8 | −18.8% | −3.2226 to −0.3774 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.4 | +95.400 (native is 0) | +42.1682 to +148.6318 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.87 | 19.83 | +82.4% | +4.8115 to +13.0985 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06197 | 0.07678 | +23.9% | +0.0062 to +0.0234 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.487 | 1.5 | +0.9% | −0.0222 to +0.0480 | no |
| Omni's own CPU (cores), mean | 0 | 0.07614 | +0.076 (native is 0) | +0.0690 to +0.0833 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.487 | 1.576 | +6.0% | +0.0474 to +0.1306 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.9 | 383 | −14.5% | −102.4289 to −27.3671 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.094 | +3.9% | −0.1309 to +0.2870 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.2556 to +1.8556 | no |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | −0.7303 to +4.9303 | no |
| pod start wait, mean (s) | 0 | 0.75 | +0.750 (native is 0) | −0.1301 to +1.6301 | no |
| host CPU busy, the real machine under kind (%) | 42.69 | 46.88 | +9.8% | +3.4586 to +4.9132 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.2 | 813.7 | +2.5% | +5.5062 to +33.4938 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.083 | −32.0% | −3.1402 to −0.6947 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.8583 | +663.0% | +0.5929 to +0.8987 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.4 | +166.7% | +0.7274 to +2.2726 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 99.91 | 124 | +24.1% | +9.5076 to +38.6424 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*