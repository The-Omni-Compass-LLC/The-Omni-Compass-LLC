# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.824 | 4.834 |
| node-hours | 2.517 | 2.518 | 2.02 | 2.029 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.1 | 273.2 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 274.1 | 236.3 | 237.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 422 | 423.9 | 443.8 | 459.4 |
| response time (ms), 95th percentile | 1610 | 1671 | 1697 | 1889 |
| response time (ms), 99th percentile | 2264 | 2409 | 2354 | 2605 |
| time over the response line (% of samples) | 19.15 | 17.91 | 19.57 | 18.95 |
| failed requests (%) | 0 | 0 | 0.0355 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10 | 10.5 | 10.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 23.6 | 27 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 41.25 | 77.78 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.85 | 20.6 | 18.29 | 24.28 |
| utilisation (used / allocatable) | 0.06415 | 0.06435 | 0.07975 | 0.07778 |
| CPU used (cores), mean | 1.54 | 1.545 | 1.52 | 1.511 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06242 | 0.06918 |
| CPU used with Omni's own (cores), mean | 1.54 | 1.545 | 1.582 | 1.58 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.6 | 433.2 | 372.9 | 380.9 |
| HPA replicas, mean | 2.068 | 2.1 | 2.339 | 2.323 |
| pods started | 0 | 0 | 0.9 | 0.2 |
| pod start wait, total (s) | 0 | 0 | 2.5 | 0.4 |
| pod start wait, mean (s) | 0 | 0 | 0.775 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.08 | 44.94 | 46.54 | 47.63 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 814.4 | 821.1 | 822.4 | 833 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.973 | 3.735 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.225 | 0.2542 | 0.6875 | 0.5083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.3 | 5.2 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 120.1 | 129.9 | 128.4 | 138.7 |
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
| worker nodes in service, mean | 6 | 4.834 | −19.4% | −1.8136 to −0.5183 | yes: GAIN |
| node-hours | 2.518 | 2.029 | −19.4% | −0.7553 to −0.2227 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 274 | −0.0% | −1.6227 to +1.3566 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 237.2 | −13.4% | −57.3499 to −16.3413 | yes: GAIN |
| response time (ms), mean | 423.9 | 459.4 | +8.4% | +15.7862 to +55.1420 | yes: LOSS |
| response time (ms), 95th percentile | 1671 | 1889 | +13.0% | +56.3010 to +379.1180 | yes: LOSS |
| response time (ms), 99th percentile | 2409 | 2605 | +8.1% | −49.0367 to +441.3375 | no |
| time over the response line (% of samples) | 17.91 | 18.95 | +5.8% | −0.8569 to +2.9510 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.4 | +4.0% | −1.1888 to +1.9888 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +17.4864 to +36.5136 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.6 | 24.28 | +17.9% | +0.1040 to +7.2660 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06435 | 0.07778 | +20.9% | +0.0070 to +0.0198 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.545 | 1.511 | −2.2% | −0.0948 to +0.0275 | no |
| Omni's own CPU (cores), mean | 0 | 0.06918 | +0.069 (native is 0) | +0.0619 to +0.0765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.545 | 1.58 | +2.3% | −0.0299 to +0.1009 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.2 | 380.9 | −12.1% | −78.8028 to −25.6510 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.1 | 2.323 | +10.6% | −0.0264 to +0.4724 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.94 | 47.63 | +6.0% | +2.1671 to +3.2134 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.1 | 833 | +1.4% | +4.0537 to +19.7463 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.735 | −37.7% | −3.3691 to −1.1606 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.5083 | +100.0% | −0.2842 to +0.7926 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.8 | −38.5% | −1.6802 to +0.6802 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.9 | 138.7 | +6.8% | +2.6707 to +14.9043 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.518 | +0.0% | −0.0078 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.1 | +0.1% | −0.8988 to +1.2680 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 274.1 | +0.1% | −0.8988 to +1.2680 | no |
| response time (ms), mean | 422 | 423.9 | +0.5% | −17.8089 to +21.6356 | no |
| response time (ms), 95th percentile | 1610 | 1671 | +3.8% | −132.2773 to +254.7823 | no |
| response time (ms), 99th percentile | 2264 | 2409 | +6.4% | −51.0557 to +340.7683 | no |
| time over the response line (% of samples) | 19.15 | 17.91 | −6.5% | −2.5956 to +0.1009 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10 | −2.9% | −1.6081 to +1.0081 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.85 | 20.6 | +30.0% | +1.2711 to +8.2323 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06415 | 0.06435 | +0.3% | −0.0007 to +0.0012 | no |
| CPU used (cores), mean | 1.54 | 1.545 | +0.3% | −0.0180 to +0.0280 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.54 | 1.545 | +0.3% | −0.0180 to +0.0280 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.6 | 433.2 | −0.1% | −7.6212 to +6.6404 | no |
| HPA replicas, mean | 2.068 | 2.1 | +1.5% | −0.0412 to +0.1046 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 44.08 | 44.94 | +1.9% | +0.5266 to +1.1827 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.4 | 821.1 | +0.8% | −0.5168 to +13.9168 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.225 | 0.2542 | +13.0% | −0.0788 to +0.1371 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.3 | −13.3% | −1.4972 to +1.0972 | no |
| queue: job turnaround, submitted to done, mean (s) | 120.1 | 129.9 | +8.2% | +1.7303 to +17.9280 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.824 | −19.6% | −1.9668 to −0.3853 | yes: GAIN |
| node-hours | 2.517 | 2.02 | −19.7% | −0.8272 to −0.1665 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.2 | −0.3% | −1.5942 to +0.1540 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 236.3 | −13.7% | −62.4935 to −12.7508 | yes: GAIN |
| response time (ms), mean | 422 | 443.8 | +5.2% | +10.7833 to +32.8436 | yes: LOSS |
| response time (ms), 95th percentile | 1610 | 1697 | +5.4% | +31.7807 to +142.8813 | yes: LOSS |
| response time (ms), 99th percentile | 2264 | 2354 | +4.0% | −7.1417 to +187.3191 | no |
| time over the response line (% of samples) | 19.15 | 19.57 | +2.2% | −0.1679 to +0.9959 | no |
| failed requests (%) | 0 | 0.0355 | +0.036 (native is 0) | −0.0448 to +0.1158 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.5 | +1.9% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.6 | +23.600 (native is 0) | +13.6701 to +33.5299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.85 | 18.29 | +15.4% | −0.4273 to +5.3073 | no |
| utilisation (used / allocatable) | 0.06415 | 0.07975 | +24.3% | +0.0051 to +0.0261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.54 | 1.52 | −1.3% | −0.0503 to +0.0111 | no |
| Omni's own CPU (cores), mean | 0 | 0.06242 | +0.062 (native is 0) | +0.0562 to +0.0687 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.54 | 1.582 | +2.8% | +0.0074 to +0.0782 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.6 | 372.9 | −14.0% | −102.3079 to −19.1708 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.068 | 2.339 | +13.1% | −0.0028 to +0.5452 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.2898 to +2.0898 | no |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | −0.9263 to +5.9263 | no |
| pod start wait, mean (s) | 0 | 0.775 | +0.775 (native is 0) | −0.1347 to +1.6847 | no |
| host CPU busy, the real machine under kind (%) | 44.08 | 46.54 | +5.6% | +2.1156 to +2.8044 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.4 | 822.4 | +1.0% | +2.8198 to +13.1802 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.973 | −33.8% | −3.2187 to −0.8356 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.225 | 0.6875 | +205.6% | −0.4832 to +1.4082 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 5.2 | +246.7% | −4.2012 to +11.6012 | no |
| queue: job turnaround, submitted to done, mean (s) | 120.1 | 128.4 | +7.0% | +2.5364 to +14.1969 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.824 | −19.6% | −1.9668 to −0.3853 | yes: GAIN |
| node-hours | 2.518 | 2.02 | −19.8% | −0.8251 to −0.1706 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.1 | 273.2 | −0.3% | −2.2722 to +0.4628 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.1 | 236.3 | −13.8% | −62.2481 to −13.3655 | yes: GAIN |
| response time (ms), mean | 423.9 | 443.8 | +4.7% | +3.4853 to +36.3149 | yes: LOSS |
| response time (ms), 95th percentile | 1671 | 1697 | +1.6% | −121.8425 to +173.9995 | no |
| response time (ms), 99th percentile | 2409 | 2354 | −2.3% | −244.9731 to +135.4379 | no |
| time over the response line (% of samples) | 17.91 | 19.57 | +9.3% | +0.2520 to +3.0707 | yes: LOSS |
| failed requests (%) | 0 | 0.0355 | +0.036 (native is 0) | −0.0448 to +0.1158 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 10.5 | +5.0% | −0.9005 to +1.9005 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 23.6 | +23.600 (native is 0) | +13.6701 to +33.5299 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.6 | 18.29 | −11.2% | −5.1951 to +0.5718 | no |
| utilisation (used / allocatable) | 0.06435 | 0.07975 | +23.9% | +0.0046 to +0.0262 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.545 | 1.52 | −1.6% | −0.0547 to +0.0055 | no |
| Omni's own CPU (cores), mean | 0 | 0.06242 | +0.062 (native is 0) | +0.0562 to +0.0687 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.545 | 1.582 | +2.4% | +0.0055 to +0.0702 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.2 | 372.9 | −13.9% | −103.0607 to −17.4372 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.1 | 2.339 | +11.4% | +0.0114 to +0.4677 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.2898 to +2.0898 | no |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | −0.9263 to +5.9263 | no |
| pod start wait, mean (s) | 0 | 0.775 | +0.775 (native is 0) | −0.1347 to +1.6847 | no |
| host CPU busy, the real machine under kind (%) | 44.94 | 46.54 | +3.6% | +1.3024 to +1.9083 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 821.1 | 822.4 | +0.2% | −4.4130 to +7.0130 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.973 | −33.8% | −3.2187 to −0.8356 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2542 | 0.6875 | +170.5% | −0.4973 to +1.3639 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 5.2 | +300.0% | −3.8222 to +11.6222 | no |
| queue: job turnaround, submitted to done, mean (s) | 129.9 | 128.4 | −1.1% | −7.9079 to +4.9829 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.834 | −19.4% | −1.8136 to −0.5183 | yes: GAIN |
| node-hours | 2.517 | 2.029 | −19.4% | −0.7568 to −0.2192 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274 | +0.0% | −1.6269 to +1.7299 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 237.2 | −13.4% | −57.5338 to −15.7882 | yes: GAIN |
| response time (ms), mean | 422 | 459.4 | +8.9% | +13.7321 to +61.0228 | yes: LOSS |
| response time (ms), 95th percentile | 1610 | 1889 | +17.3% | +94.6572 to +463.2668 | yes: LOSS |
| response time (ms), 99th percentile | 2264 | 2605 | +15.1% | +76.5871 to +605.4263 | yes: LOSS |
| time over the response line (% of samples) | 19.15 | 18.95 | −1.0% | −1.5798 to +1.1792 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.3 | 10.4 | +1.0% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27 | +27.000 (native is 0) | +17.4864 to +36.5136 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.85 | 24.28 | +53.2% | +2.2411 to +14.6322 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06415 | 0.07778 | +21.2% | +0.0076 to +0.0197 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.54 | 1.511 | −1.9% | −0.0900 to +0.0327 | no |
| Omni's own CPU (cores), mean | 0 | 0.06918 | +0.069 (native is 0) | +0.0619 to +0.0765 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.54 | 1.58 | +2.6% | −0.0267 to +0.1077 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 433.6 | 380.9 | −12.2% | −77.1459 to −28.2887 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.068 | 2.323 | +12.3% | −0.0086 to +0.5180 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 44.08 | 47.63 | +8.0% | +2.9912 to +4.0986 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.4 | 833 | +2.3% | +8.1893 to +29.0107 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.735 | −37.7% | −3.3691 to −1.1606 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.225 | 0.5083 | +125.9% | −0.2755 to +0.8421 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.8 | −46.7% | −2.2099 to +0.8099 | no |
| queue: job turnaround, submitted to done, mean (s) | 120.1 | 138.7 | +15.5% | +8.8614 to +28.3719 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*