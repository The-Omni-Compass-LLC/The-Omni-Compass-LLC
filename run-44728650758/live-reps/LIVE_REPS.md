# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.293 | 6 |
| node-hours | 2.515 | 2.515 | 2.216 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 287.3 | 273.3 | 287.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 287.3 | 251 | 287.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 386.2 | 734.6 | 361.9 | 708.7 |
| response time (ms), 95th percentile | 1396 | 1467 | 1478 | 1432 |
| response time (ms), 99th percentile | 1978 | 1953 | 2085 | 1857 |
| time over the response line (% of samples) | 15.73 | 67.09 | 16.43 | 64.67 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 25 | 10.8 | 25 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 77.3 | 41.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 46.25 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 2.475 | 12.22 | 2.525 |
| utilisation (used / allocatable) | 0.06322 | 0.09969 | 0.0711 | 0.09947 |
| CPU used (cores), mean | 1.517 | 2.392 | 1.507 | 2.387 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07455 | 0.0441 |
| CPU used with Omni's own (cores), mean | 1.517 | 2.392 | 1.582 | 2.431 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.8 | 286.6 | 400.8 | 287.1 |
| HPA replicas, mean | 2.004 | 2.053 | 2.206 | 2.554 |
| pods started | 0.1 | 0.3 | 0.9 | 1.6 |
| pod start wait, total (s) | 0.3 | 0.7 | 2.1 | 5.2 |
| pod start wait, mean (s) | 0.3 | 0.4 | 1.2 | 3.35 |
| host CPU busy, the real machine under kind (%) | 43.33 | 77.59 | 46.41 | 78.77 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 794.2 | 1510 | 801.3 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 4.652 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 695 | 0.1042 | 719.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1336 | 0.4 | 1343 |
| queue: job turnaround, submitted to done, mean (s) | 98.74 | 1018 | 105.2 | 1024 |
| queue: jobs unfinished at the window's end | 0 | 16.1 | 0 | 16.5 |
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
| node-hours | 2.515 | 2.514 | −0.0% | −0.0097 to +0.0087 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 287.3 | 287.1 | −0.1% | −1.4061 to +1.0683 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.3 | 287.1 | −0.1% | −1.4061 to +1.0683 | no |
| response time (ms), mean | 734.6 | 708.7 | −3.5% | −84.6628 to +32.8933 | no |
| response time (ms), 95th percentile | 1467 | 1432 | −2.4% | −165.3552 to +95.9572 | no |
| response time (ms), 99th percentile | 1953 | 1857 | −4.9% | −295.2640 to +102.7934 | no |
| time over the response line (% of samples) | 67.09 | 64.67 | −3.6% | −6.3714 to +1.5218 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 25 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +39.2673 to +44.1327 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.475 | 2.525 | +2.0% | −0.1450 to +0.2450 | no |
| utilisation (used / allocatable) | 0.09969 | 0.09947 | −0.2% | −0.0009 to +0.0005 | no |
| CPU used (cores), mean | 2.392 | 2.387 | −0.2% | −0.0211 to +0.0110 | no |
| Omni's own CPU (cores), mean | 0 | 0.0441 | +0.044 (native is 0) | +0.0398 to +0.0484 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.392 | 2.431 | +1.6% | +0.0228 to +0.0553 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.6 | 287.1 | +0.2% | −1.1714 to +2.1733 | no |
| HPA replicas, mean | 2.053 | 2.554 | +24.4% | +0.2773 to +0.7244 | yes: power given |
| pods started | 0.3 | 1.6 | +433.3% | +0.4047 to +2.1953 | yes: power given |
| pod start wait, total (s) | 0.7 | 5.2 | +642.9% | +1.6939 to +7.3061 | yes: LOSS |
| pod start wait, mean (s) | 0.4 | 3.35 | +737.5% | +1.7161 to +4.1839 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 77.59 | 78.77 | +1.5% | +0.9585 to +1.3941 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 1510 | +0.0% | −4.7383 to +5.5383 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 695 | 719.3 | +3.5% | −54.9399 to +103.6089 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1336 | 1343 | +0.5% | −57.1567 to +70.3567 | no |
| queue: job turnaround, submitted to done, mean (s) | 1018 | 1024 | +0.6% | −20.2539 to +32.8873 | no |
| queue: jobs unfinished at the window's end | 16.1 | 16.5 | +2.5% | −0.5048 to +1.3048 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.515 | +0.0% | −0.0084 to +0.0091 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 287.3 | +5.0% | +10.8810 to +16.5486 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 287.3 | +5.0% | +10.8810 to +16.5486 | yes: power given |
| response time (ms), mean | 386.2 | 734.6 | +90.2% | +242.3256 to +454.4299 | yes: LOSS |
| response time (ms), 95th percentile | 1396 | 1467 | +5.1% | −643.7560 to +784.9620 | no |
| response time (ms), 99th percentile | 1978 | 1953 | −1.3% | −1135.9738 to +1085.2884 | no |
| time over the response line (% of samples) | 15.73 | 67.09 | +326.6% | +47.4087 to +55.3268 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 25 | +174.7% | +11.8193 to +19.9807 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 2.475 | −79.0% | −12.7906 to −5.8561 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06322 | 0.09969 | +57.7% | +0.0287 to +0.0442 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.517 | 2.392 | +57.7% | +0.6890 to +1.0614 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.517 | 2.392 | +57.7% | +0.6890 to +1.0614 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.8 | 286.6 | −34.4% | −192.1698 to −108.3595 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.053 | +2.4% | −0.1163 to +0.2140 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | −1.1888 to +1.9888 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.9366 to +1.1366 | no |
| host CPU busy, the real machine under kind (%) | 43.33 | 77.59 | +79.1% | +30.4765 to +38.0465 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.2 | 1510 | +90.1% | +656.9421 to +773.6579 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 695 | +877787.2% | +512.9558 to +876.8739 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1336 | +267140.0% | +1269.7062 to +1401.6938 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 98.74 | 1018 | +930.7% | +881.4983 to +956.4017 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 16.1 | +16.100 (native is 0) | +12.5243 to +19.6757 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.293 | −11.8% | −1.1807 to −0.2333 | yes: GAIN |
| node-hours | 2.515 | 2.216 | −11.9% | −0.4954 to −0.1007 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.3 | −0.1% | −0.9388 to +0.3651 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 251 | −8.2% | −37.4989 to −7.5081 | yes: GAIN |
| response time (ms), mean | 386.2 | 361.9 | −6.3% | −34.7129 to −13.9259 | yes: GAIN |
| response time (ms), 95th percentile | 1396 | 1478 | +5.8% | +4.7216 to +158.5744 | yes: LOSS |
| response time (ms), 99th percentile | 1978 | 2085 | +5.4% | −24.7769 to +237.3585 | no |
| time over the response line (% of samples) | 15.73 | 16.43 | +4.5% | −0.5583 to +1.9647 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 10.8 | +18.7% | +0.4819 to +2.9181 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 77.3 | +77.300 (native is 0) | +36.1147 to +118.4853 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 12.22 | +3.5% | −1.2254 to +2.0620 | no |
| utilisation (used / allocatable) | 0.06322 | 0.0711 | +12.5% | +0.0027 to +0.0131 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.517 | 1.507 | −0.7% | −0.0305 to +0.0102 | no |
| Omni's own CPU (cores), mean | 0 | 0.07455 | +0.075 (native is 0) | +0.0705 to +0.0786 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 1.582 | +4.2% | +0.0425 to +0.0863 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.8 | 400.8 | −8.2% | −59.4180 to −12.6494 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.206 | +10.1% | +0.0274 to +0.3759 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | +0.0612 to +1.5388 | yes: power given |
| pod start wait, total (s) | 0.3 | 2.1 | +600.0% | +0.1899 to +3.4101 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.2 | +300.0% | −0.0357 to +1.8357 | no |
| host CPU busy, the real machine under kind (%) | 43.33 | 46.41 | +7.1% | +2.6922 to +3.4622 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.2 | 801.3 | +0.9% | +0.6450 to +13.5550 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.652 | −22.5% | −2.2303 to −0.4658 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.1042 | +31.6% | −0.0663 to +0.1163 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.4 | −20.0% | −0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 98.74 | 105.2 | +6.6% | +0.5154 to +12.4846 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.293 | −11.8% | −1.1807 to −0.2333 | yes: GAIN |
| node-hours | 2.515 | 2.216 | −11.9% | −0.4952 to −0.1016 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 287.3 | 273.3 | −4.9% | −16.8194 to −11.1839 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.3 | 251 | −12.6% | −53.7266 to −18.7100 | yes: GAIN |
| response time (ms), mean | 734.6 | 361.9 | −50.7% | −480.3625 to −265.0319 | yes: GAIN |
| response time (ms), 95th percentile | 1467 | 1478 | +0.8% | −756.2566 to +778.3466 | no |
| response time (ms), 99th percentile | 1953 | 2085 | +6.7% | −1043.2289 to +1306.4959 | no |
| time over the response line (% of samples) | 67.09 | 16.43 | −75.5% | −54.0587 to −47.2705 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25 | 10.8 | −56.8% | −17.1163 to −11.2837 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 77.3 | +77.300 (native is 0) | +36.1147 to +118.4853 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.475 | 12.22 | +393.6% | +5.1678 to +14.3155 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09969 | 0.0711 | −28.7% | −0.0326 to −0.0245 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.392 | 1.507 | −37.0% | −1.0815 to −0.6892 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07455 | +0.075 (native is 0) | +0.0705 to +0.0786 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.392 | 1.582 | −33.9% | −1.0103 to −0.6114 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 286.6 | 400.8 | +39.9% | +91.8115 to +136.6504 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.053 | 2.206 | +7.4% | −0.0989 to +0.4044 | no |
| pods started | 0.3 | 0.9 | +200.0% | −0.4769 to +1.6769 | no |
| pod start wait, total (s) | 0.7 | 2.1 | +200.0% | −1.1725 to +3.9725 | no |
| pod start wait, mean (s) | 0.4 | 1.2 | +200.0% | −0.5718 to +2.1718 | no |
| host CPU busy, the real machine under kind (%) | 77.59 | 46.41 | −40.2% | −35.1243 to −27.2444 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 801.3 | −46.9% | −771.1794 to −645.2206 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 695 | 0.1042 | −100.0% | −876.8107 to −512.9690 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1336 | 0.4 | −100.0% | −1401.5251 to −1270.0749 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1018 | 105.2 | −89.7% | −949.9453 to −874.9547 | yes: GAIN |
| queue: jobs unfinished at the window's end | 16.1 | 0 | −100.0% | −19.6757 to −12.5243 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.514 | −0.0% | −0.0112 to +0.0109 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 287.1 | +5.0% | +10.3546 to +16.7371 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 287.1 | +5.0% | +10.3546 to +16.7371 | yes: power given |
| response time (ms), mean | 386.2 | 708.7 | +83.5% | +224.6590 to +420.3269 | yes: LOSS |
| response time (ms), 95th percentile | 1396 | 1432 | +2.6% | −677.0112 to +748.8192 | no |
| response time (ms), 99th percentile | 1978 | 1857 | −6.1% | −1184.4271 to +941.2711 | no |
| time over the response line (% of samples) | 15.73 | 64.67 | +311.2% | +45.5784 to +52.3075 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 25 | +174.7% | +11.8193 to +19.9807 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.7 | +41.700 (native is 0) | +39.2673 to +44.1327 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.8 | 2.525 | −78.6% | −12.7007 to −5.8460 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06322 | 0.09947 | +57.4% | +0.0284 to +0.0441 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.517 | 2.387 | +57.4% | +0.6818 to +1.0585 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0441 | +0.044 (native is 0) | +0.0398 to +0.0484 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.517 | 2.431 | +60.3% | +0.7301 to +1.0984 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.8 | 287.1 | −34.3% | −191.8732 to −107.6542 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.554 | +27.4% | +0.3729 to +0.7265 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.8921 to +2.1079 | yes: power given |
| pod start wait, total (s) | 0.3 | 5.2 | +1633.3% | +2.8091 to +6.9909 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 3.35 | +1016.7% | +1.8873 to +4.2127 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.33 | 78.77 | +81.8% | +31.7225 to +39.1531 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.2 | 1510 | +90.1% | +657.7664 to +773.6336 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 719.3 | +908525.5% | +521.6874 to +916.8113 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1343 | +268460.0% | +1251.9495 to +1432.6505 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 98.74 | 1024 | +937.1% | +891.0993 to +959.4340 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 16.5 | +16.500 (native is 0) | +12.8332 to +20.1668 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*