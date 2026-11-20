# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 5.997 | 6 | 4.874 | 4.746 |
| node-hours | 2.516 | 2.514 | 2.042 | 1.989 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.3 | 273.1 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273.3 | 237.7 | 234.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 406.6 | 426.1 | 391 | 409.8 |
| response time (ms), 95th percentile | 1511 | 1616 | 1663 | 1728 |
| response time (ms), 99th percentile | 2148 | 2249 | 2378 | 2397 |
| time over the response line (% of samples) | 17.31 | 17.55 | 17.27 | 17.62 |
| failed requests (%) | 0.02186 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.2 | 9.8 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 119.8 | 134.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 10 | 3.704 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.24 | 11.76 | 14.1 | 16.04 |
| utilisation (used / allocatable) | 0.06225 | 0.06267 | 0.07706 | 0.08027 |
| CPU used (cores), mean | 1.493 | 1.504 | 1.477 | 1.493 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07478 | 0.07598 |
| CPU used with Omni's own (cores), mean | 1.493 | 1.504 | 1.551 | 1.569 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 446.7 | 387.8 | 375.4 |
| HPA replicas, mean | 1.997 | 1.974 | 2.215 | 2.356 |
| pods started | 0.1 | 0 | 1.2 | 1.6 |
| pod start wait, total (s) | 0.3 | 0 | 2.5 | 4 |
| pod start wait, mean (s) | 0.3 | 0 | 1.233 | 1.165 |
| host CPU busy, the real machine under kind (%) | 42.64 | 43.52 | 45.86 | 46.61 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 807.3 | 814.3 | 815.7 | 824.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.264 | 3.999 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.2792 | 0.1708 | 1.067 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | 0.8 | 6.3 |
| queue: job turnaround, submitted to done, mean (s) | 112.3 | 117.8 | 119.4 | 128.1 |
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
| worker nodes in service, mean | 6 | 4.746 | −20.9% | −2.1753 to −0.3333 | yes: GAIN |
| node-hours | 2.514 | 1.989 | −20.9% | −0.9071 to −0.1414 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.6 | +0.1% | −0.2667 to +0.9611 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 234.1 | −14.3% | −67.9805 to −10.3626 | yes: GAIN |
| response time (ms), mean | 426.1 | 409.8 | −3.8% | −30.0740 to −2.4707 | yes: GAIN |
| response time (ms), 95th percentile | 1616 | 1728 | +6.9% | +18.3563 to +204.5207 | yes: LOSS |
| response time (ms), 99th percentile | 2249 | 2397 | +6.6% | −99.4189 to +395.1145 | no |
| time over the response line (% of samples) | 17.55 | 17.62 | +0.4% | −0.2990 to +0.4443 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.4 | +2.2% | −0.8003 to +1.2003 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.2 | +134.200 (native is 0) | +28.6552 to +239.7448 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.76 | 16.04 | +36.3% | +0.2050 to +8.3450 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06267 | 0.08027 | +28.1% | +0.0048 to +0.0304 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.504 | 1.493 | −0.8% | −0.0451 to +0.0219 | no |
| Omni's own CPU (cores), mean | 0 | 0.07598 | +0.076 (native is 0) | +0.0693 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.504 | 1.569 | +4.3% | +0.0262 to +0.1026 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 375.4 | −16.0% | −123.8438 to −18.6482 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.974 | 2.356 | +19.4% | +0.0146 to +0.7495 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.1615 to +3.0385 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | −0.0883 to +8.0883 | no |
| pod start wait, mean (s) | 0 | 1.165 | +1.165 (native is 0) | +0.2400 to +2.0900 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.52 | 46.61 | +7.1% | +2.3483 to +3.8290 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.3 | 824.4 | +1.2% | +1.6132 to +18.5868 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.999 | −33.4% | −3.3256 to −0.6772 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2792 | 1.067 | +282.1% | −0.2441 to +1.8191 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 6.3 | +472.7% | −2.8208 to +13.2208 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.8 | 128.1 | +8.8% | +2.2040 to +18.5377 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.997 | 6 | +0.0% | −0.0033 to +0.0086 | no |
| node-hours | 2.516 | 2.514 | −0.1% | −0.0118 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.3 | −0.0% | −1.0604 to +0.8435 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 273.3 | −0.0% | −1.0084 to +0.9582 | no |
| response time (ms), mean | 406.6 | 426.1 | +4.8% | +5.3768 to +33.6141 | yes: LOSS |
| response time (ms), 95th percentile | 1511 | 1616 | +6.9% | +2.2728 to +207.4672 | yes: LOSS |
| response time (ms), 99th percentile | 2148 | 2249 | +4.7% | −50.8841 to +254.6079 | no |
| time over the response line (% of samples) | 17.31 | 17.55 | +1.4% | −0.1622 to +0.6338 | no |
| failed requests (%) | 0.02186 | 0 | −100.0% | −0.0713 to +0.0276 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.2 | +5.7% | −0.4079 to +1.4079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.24 | 11.76 | −3.9% | −2.4416 to +1.4916 | no |
| utilisation (used / allocatable) | 0.06225 | 0.06267 | +0.7% | −0.0005 to +0.0013 | no |
| CPU used (cores), mean | 1.493 | 1.504 | +0.7% | −0.0097 to +0.0315 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.493 | 1.504 | +0.7% | −0.0097 to +0.0315 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 446.7 | −0.8% | −11.1481 to +4.3634 | no |
| HPA replicas, mean | 1.997 | 1.974 | −1.2% | −0.1775 to +0.1309 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 42.64 | 43.52 | +2.1% | +0.4606 to +1.3026 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 807.3 | 814.3 | +0.9% | +0.7915 to +13.2085 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.2792 | +346.7% | −0.0120 to +0.4453 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 1.1 | +266.7% | −0.0793 to +1.6793 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.3 | 117.8 | +4.8% | +0.7387 to +10.1363 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.997 | 4.874 | −18.7% | −2.0002 to −0.2471 | yes: GAIN |
| node-hours | 2.516 | 2.042 | −18.8% | −0.8386 to −0.1098 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.1 | −0.1% | −1.7620 to +1.0963 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 237.7 | −13.0% | −63.1812 to −8.0636 | yes: GAIN |
| response time (ms), mean | 406.6 | 391 | −3.8% | −26.0788 to −5.0653 | yes: GAIN |
| response time (ms), 95th percentile | 1511 | 1663 | +10.0% | +41.3303 to +261.2507 | yes: LOSS |
| response time (ms), 99th percentile | 2148 | 2378 | +10.8% | +37.6912 to +424.1628 | yes: LOSS |
| time over the response line (% of samples) | 17.31 | 17.27 | −0.2% | −0.7130 to +0.6327 | no |
| failed requests (%) | 0.02186 | 0 | −100.0% | −0.0713 to +0.0276 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.8 | +12.6% | −0.0410 to +2.2410 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 119.8 | +119.800 (native is 0) | +39.7901 to +199.8099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.24 | 14.1 | +15.2% | −1.1919 to +4.9152 | no |
| utilisation (used / allocatable) | 0.06225 | 0.07706 | +23.8% | +0.0030 to +0.0266 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.493 | 1.477 | −1.1% | −0.0664 to +0.0329 | no |
| Omni's own CPU (cores), mean | 0 | 0.07478 | +0.075 (native is 0) | +0.0688 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.493 | 1.551 | +3.9% | +0.0074 to +0.1087 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 387.8 | −13.8% | −111.8596 to −12.6318 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.215 | +10.9% | +0.0153 to +0.4217 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.1198 to +2.0802 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.5 | +733.3% | −0.0316 to +4.4316 | no |
| pod start wait, mean (s) | 0.3 | 1.233 | +311.1% | −0.2879 to +2.1546 | no |
| host CPU busy, the real machine under kind (%) | 42.64 | 45.86 | +7.6% | +2.9511 to +3.5046 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 807.3 | 815.7 | +1.0% | +2.5479 to +14.2521 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.264 | −28.9% | −2.9107 to −0.5611 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.1708 | +173.3% | +0.0193 to +0.1974 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.8 | +166.7% | −0.0058 to +1.0058 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.3 | 119.4 | +6.3% | +1.6807 to +12.5610 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.874 | −18.8% | −2.0012 to −0.2514 | yes: GAIN |
| node-hours | 2.514 | 2.042 | −18.8% | −0.8380 to −0.1062 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.1 | −0.1% | −1.2075 to +0.7587 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 237.7 | −13.0% | −63.3371 to −7.8575 | yes: GAIN |
| response time (ms), mean | 426.1 | 391 | −8.2% | −50.7155 to −19.4195 | yes: GAIN |
| response time (ms), 95th percentile | 1616 | 1663 | +2.9% | −25.0689 to +117.9099 | no |
| response time (ms), 99th percentile | 2249 | 2378 | +5.7% | −83.9923 to +342.1225 | no |
| time over the response line (% of samples) | 17.55 | 17.27 | −1.6% | −0.9720 to +0.4202 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.2 | 9.8 | +6.5% | −0.3048 to +1.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 119.8 | +119.800 (native is 0) | +39.7901 to +199.8099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.76 | 14.1 | +19.9% | +0.7521 to +3.9212 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06267 | 0.07706 | +23.0% | +0.0026 to +0.0262 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.504 | 1.477 | −1.8% | −0.0685 to +0.0132 | no |
| Omni's own CPU (cores), mean | 0 | 0.07478 | +0.075 (native is 0) | +0.0688 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.504 | 1.551 | +3.1% | +0.0043 to +0.0900 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.7 | 387.8 | −13.2% | −106.7618 to −10.9448 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.974 | 2.215 | +12.3% | +0.0838 to +0.3999 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0 | 2.5 | +2.500 (native is 0) | +0.5851 to +4.4149 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.233 | +1.233 (native is 0) | +0.4522 to +2.0145 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.52 | 45.86 | +5.4% | +1.9406 to +2.7519 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 814.3 | 815.7 | +0.2% | −2.0913 to +4.8913 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.264 | −28.9% | −2.9107 to −0.5611 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2792 | 0.1708 | −38.8% | −0.2995 to +0.0829 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 0.8 | −27.3% | −1.3144 to +0.7144 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.8 | 119.4 | +1.4% | −1.4275 to +4.7942 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.997 | 4.746 | −20.9% | −2.1747 to −0.3286 | yes: GAIN |
| node-hours | 2.516 | 1.989 | −20.9% | −0.9085 to −0.1441 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 | +0.1% | −0.9486 to +1.4262 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 234.1 | −14.3% | −67.8820 to −10.5113 | yes: GAIN |
| response time (ms), mean | 406.6 | 409.8 | +0.8% | −16.3536 to +22.7998 | no |
| response time (ms), 95th percentile | 1511 | 1728 | +14.3% | +76.7695 to +355.8475 | yes: LOSS |
| response time (ms), 99th percentile | 2148 | 2397 | +11.6% | +41.3022 to +458.1172 | yes: LOSS |
| time over the response line (% of samples) | 17.31 | 17.62 | +1.8% | −0.0368 to +0.6537 | no |
| failed requests (%) | 0.02186 | 0 | −100.0% | −0.0713 to +0.0276 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 9.4 | +8.0% | +0.1111 to +1.2889 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.2 | +134.200 (native is 0) | +28.6552 to +239.7448 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.24 | 16.04 | +31.1% | −1.1831 to +8.7831 | no |
| utilisation (used / allocatable) | 0.06225 | 0.08027 | +28.9% | +0.0051 to +0.0309 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.493 | 1.493 | −0.0% | −0.0373 to +0.0359 | no |
| Omni's own CPU (cores), mean | 0 | 0.07598 | +0.076 (native is 0) | +0.0693 to +0.0827 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.493 | 1.569 | +5.0% | +0.0361 to +0.1145 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 375.4 | −16.6% | −128.8050 to −20.4718 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.356 | +18.0% | +0.0510 to +0.6664 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | −0.0174 to +3.0174 | no |
| pod start wait, total (s) | 0.3 | 4 | +1233.3% | −0.6057 to +8.0057 | no |
| pod start wait, mean (s) | 0.3 | 1.165 | +288.3% | −0.4440 to +2.1740 | no |
| host CPU busy, the real machine under kind (%) | 42.64 | 46.61 | +9.3% | +3.4515 to +4.4890 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 807.3 | 824.4 | +2.1% | +3.9559 to +30.2441 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.999 | −33.4% | −3.3256 to −0.6772 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1.067 | +1606.7% | −0.2130 to +2.2214 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 6.3 | +2000.0% | −2.6299 to +14.6299 | no |
| queue: job turnaround, submitted to done, mean (s) | 112.3 | 128.1 | +14.1% | +4.1092 to +27.5074 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*