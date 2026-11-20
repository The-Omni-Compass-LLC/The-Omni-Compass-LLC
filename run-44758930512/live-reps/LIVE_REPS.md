# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.58 | 6 |
| node-hours | 2.514 | 2.517 | 2.337 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.6 | 273.3 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.6 | 260.1 | 271.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 392.2 | 146.4 | 389.4 | 151.6 |
| response time (ms), 95th percentile | 1404 | 252.7 | 1631 | 269.8 |
| response time (ms), 99th percentile | 2013 | 358.4 | 2319 | 385.7 |
| time over the response line (% of samples) | 17.23 | 0.2009 | 17.56 | 0.2939 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 0 | 11.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 109.8 | 22.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.86 | 1265 | 11.39 | 1336 |
| utilisation (used / allocatable) | 0.06215 | 0.06011 | 0.06771 | 0.05785 |
| CPU used (cores), mean | 1.492 | 1.443 | 1.516 | 1.388 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07824 | 0.06971 |
| CPU used with Omni's own (cores), mean | 1.492 | 1.443 | 1.594 | 1.458 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.2 | 450.5 | 414.5 | 466.8 |
| HPA replicas, mean | 2.004 | 1.975 | 2.4 | 2.111 |
| pods started | 0.1 | 0.1 | 1.5 | 0.6 |
| pod start wait, total (s) | 0.2 | 0.2 | 3.3 | 1.4 |
| pod start wait, mean (s) | 0.2 | 0.2 | 1.8 | 0.6667 |
| host CPU busy, the real machine under kind (%) | 43.06 | 45.8 | 46.67 | 47.28 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 788.2 | 1509 | 803.7 | 1509 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.277 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 180.1 | 0.0875 | 190.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 734.7 | 0.5 | 829.1 |
| queue: job turnaround, submitted to done, mean (s) | 94.09 | 907 | 108.3 | 932.1 |
| queue: jobs unfinished at the window's end | 0 | 13.2 | 0 | 15 |
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
| node-hours | 2.517 | 2.514 | −0.1% | −0.0142 to +0.0069 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.4 | −0.4% | −2.4244 to +0.0766 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.4 | −0.4% | −2.4244 to +0.0766 | no |
| response time (ms), mean | 146.4 | 151.6 | +3.6% | +2.4294 to +8.0172 | yes: LOSS |
| response time (ms), 95th percentile | 252.7 | 269.8 | +6.8% | +6.0831 to +28.0409 | yes: LOSS |
| response time (ms), 99th percentile | 358.4 | 385.7 | +7.6% | +12.6280 to +42.0564 | yes: LOSS |
| time over the response line (% of samples) | 0.2009 | 0.2939 | +46.3% | −0.0287 to +0.2148 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.6 | +22.600 (native is 0) | +14.3942 to +30.8058 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1265 | 1336 | +5.6% | +11.9772 to +130.4828 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06011 | 0.05785 | −3.8% | −0.0034 to −0.0011 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.388 | −3.8% | −0.0811 to −0.0275 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06971 | +0.070 (native is 0) | +0.0639 to +0.0755 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.458 | +1.1% | −0.0134 to +0.0443 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.5 | 466.8 | +3.6% | +8.3913 to +24.1406 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.975 | 2.111 | +6.9% | −0.0502 to +0.3233 | no |
| pods started | 0.1 | 0.6 | +500.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.2 | 1.4 | +600.0% | −0.8456 to +3.2456 | no |
| pod start wait, mean (s) | 0.2 | 0.6667 | +233.3% | −0.5145 to +1.4478 | no |
| host CPU busy, the real machine under kind (%) | 45.8 | 47.28 | +3.2% | +0.4141 to +2.5561 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1509 | 1509 | +0.0% | −8.7430 to +9.5430 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 180.1 | 190.6 | +5.8% | −44.8025 to +65.6358 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 734.7 | 829.1 | +12.8% | −62.4183 to +251.2183 | no |
| queue: job turnaround, submitted to done, mean (s) | 907 | 932.1 | +2.8% | −26.8669 to +77.1085 | no |
| queue: jobs unfinished at the window's end | 13.2 | 15 | +13.6% | −1.1358 to +4.7358 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.517 | +0.1% | −0.0021 to +0.0088 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 272.6 | −0.2% | −2.7618 to +1.6719 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 272.6 | −0.2% | −2.7618 to +1.6719 | no |
| response time (ms), mean | 392.2 | 146.4 | −62.7% | −397.1892 to −94.4748 | yes: GAIN |
| response time (ms), 95th percentile | 1404 | 252.7 | −82.0% | −1869.9486 to −433.5404 | yes: GAIN |
| response time (ms), 99th percentile | 2013 | 358.4 | −82.2% | −2690.7213 to −617.7469 | yes: GAIN |
| time over the response line (% of samples) | 17.23 | 0.2009 | −98.8% | −27.6775 to −6.3892 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 0 | −100.0% | −13.3954 to −7.0046 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.86 | 1265 | +11548.7% | +1079.4623 to +1428.1444 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06215 | 0.06011 | −3.3% | −0.0082 to +0.0041 | no |
| CPU used (cores), mean | 1.492 | 1.443 | −3.3% | −0.1969 to +0.0991 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.492 | 1.443 | −3.3% | −0.1969 to +0.0991 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.2 | 450.5 | +1.4% | −34.7180 to +47.3769 | no |
| HPA replicas, mean | 2.004 | 1.975 | −1.5% | −0.1409 to +0.0810 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 43.06 | 45.8 | +6.4% | −0.3407 to +5.8205 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.2 | 1509 | +91.4% | +675.5446 to +765.4554 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 180.1 | +254217.6% | +118.0352 to +242.1065 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 734.7 | +146840.0% | +545.4487 to +922.9513 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 94.09 | 907 | +864.0% | +755.2865 to +870.5635 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.2 | +13.200 (native is 0) | +8.9642 to +17.4358 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.58 | −7.0% | −0.7496 to −0.0900 | yes: GAIN |
| node-hours | 2.514 | 2.337 | −7.0% | −0.3139 to −0.0405 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.3 | +0.1% | −0.8484 to +1.2226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 260.1 | −4.8% | −23.3369 to −2.6890 | yes: GAIN |
| response time (ms), mean | 392.2 | 389.4 | −0.7% | −32.6368 to +26.9311 | no |
| response time (ms), 95th percentile | 1404 | 1631 | +16.1% | +30.5727 to +422.9953 | yes: LOSS |
| response time (ms), 99th percentile | 2013 | 2319 | +15.2% | +20.6555 to +591.7107 | yes: LOSS |
| time over the response line (% of samples) | 17.23 | 17.56 | +1.9% | −0.3591 to +1.0134 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 11.9 | +16.7% | +0.8706 to +2.5294 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109.8 | +109.800 (native is 0) | +32.4095 to +187.1905 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.86 | 11.39 | +4.9% | −1.0645 to +2.1312 | no |
| utilisation (used / allocatable) | 0.06215 | 0.06771 | +9.0% | +0.0023 to +0.0088 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.492 | 1.516 | +1.6% | +0.0021 to +0.0462 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07824 | +0.078 (native is 0) | +0.0727 to +0.0837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.492 | 1.594 | +6.9% | +0.0774 to +0.1273 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.2 | 414.5 | −6.7% | −47.1808 to −12.1337 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.4 | +19.7% | +0.2300 to +0.5604 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.4952 to +2.3048 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.3 | +1550.0% | +1.1791 to +5.0209 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.8 | +800.0% | +0.7604 to +2.4396 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.06 | 46.67 | +8.4% | +2.8355 to +4.3970 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.2 | 803.7 | +2.0% | +2.0744 to +28.9256 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.277 | −12.0% | −1.3750 to −0.0705 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.0875 | +23.5% | −0.0304 to +0.0637 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.5 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 94.09 | 108.3 | +15.1% | +1.1610 to +27.3140 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.58 | −7.0% | −0.7496 to −0.0900 | yes: GAIN |
| node-hours | 2.517 | 2.337 | −7.2% | −0.3153 to −0.0457 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 273.3 | +0.3% | −1.5367 to +3.0008 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 260.1 | −4.6% | −24.4432 to −0.4928 | yes: GAIN |
| response time (ms), mean | 146.4 | 389.4 | +166.0% | +70.8256 to +415.1327 | yes: LOSS |
| response time (ms), 95th percentile | 252.7 | 1631 | +545.5% | +498.1436 to +2258.9134 | yes: LOSS |
| response time (ms), 99th percentile | 358.4 | 2319 | +547.0% | +717.1424 to +3203.6920 | yes: LOSS |
| time over the response line (% of samples) | 0.2009 | 17.56 | +8642.6% | +7.0827 to +27.6383 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.9 | +11.900 (native is 0) | +9.3891 to +14.4109 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109.8 | +109.800 (native is 0) | +32.4095 to +187.1905 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1265 | 11.39 | −99.1% | −1427.3375 to −1079.2025 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06011 | 0.06771 | +12.6% | +0.0033 to +0.0119 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.516 | +5.1% | −0.0860 to +0.2320 | no |
| Omni's own CPU (cores), mean | 0 | 0.07824 | +0.078 (native is 0) | +0.0727 to +0.0837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.594 | +10.5% | −0.0108 to +0.3133 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.5 | 414.5 | −8.0% | −63.5833 to −8.3901 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.975 | 2.4 | +21.5% | +0.2601 to +0.5902 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.6311 to +2.1689 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.3 | +1550.0% | +1.4327 to +4.7673 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.8 | +800.0% | +0.7604 to +2.4396 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.8 | 46.67 | +1.9% | −2.6876 to +4.4403 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1509 | 803.7 | −46.7% | −761.1272 to −648.8728 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 4.146 | −30.9% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 180.1 | 0.0875 | −100.0% | −242.0719 to −118.0364 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 734.7 | 0.5 | −99.9% | −922.9010 to −545.4990 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 907 | 108.3 | −88.1% | −856.3654 to −741.0096 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13.2 | 0 | −100.0% | −17.4358 to −8.9642 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.514 | −0.0% | −0.0088 to +0.0081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 271.4 | −0.6% | −4.3153 to +0.8777 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 271.4 | −0.6% | −4.3153 to +0.8777 | no |
| response time (ms), mean | 392.2 | 151.6 | −61.3% | −390.9617 to −90.2559 | yes: GAIN |
| response time (ms), 95th percentile | 1404 | 269.8 | −80.8% | −1849.1682 to −420.1968 | yes: GAIN |
| response time (ms), 99th percentile | 2013 | 385.7 | −80.8% | −2661.8163 to −591.9675 | yes: GAIN |
| time over the response line (% of samples) | 17.23 | 0.2939 | −98.3% | −27.5729 to −6.3077 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 0 | −100.0% | −13.3954 to −7.0046 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 22.6 | +22.600 (native is 0) | +14.3942 to +30.8058 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.86 | 1336 | +12204.8% | +1164.3786 to +1485.6881 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06215 | 0.05785 | −6.9% | −0.0105 to +0.0019 | no |
| CPU used (cores), mean | 1.492 | 1.388 | −6.9% | −0.2516 to +0.0452 | no |
| Omni's own CPU (cores), mean | 0 | 0.06971 | +0.070 (native is 0) | +0.0639 to +0.0755 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.492 | 1.458 | −2.2% | −0.1768 to +0.1099 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.2 | 466.8 | +5.1% | −18.8448 to +64.0355 | no |
| HPA replicas, mean | 2.004 | 2.111 | +5.3% | −0.0756 to +0.2887 | no |
| pods started | 0.1 | 0.6 | +500.0% | −0.3430 to +1.3430 | no |
| pod start wait, total (s) | 0.2 | 1.4 | +600.0% | −0.8456 to +3.2456 | no |
| pod start wait, mean (s) | 0.2 | 0.6667 | +233.3% | −0.5145 to +1.4478 | no |
| host CPU busy, the real machine under kind (%) | 43.06 | 47.28 | +9.8% | +1.0530 to +7.3970 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 788.2 | 1509 | +91.5% | +672.8548 to +768.9452 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 190.6 | +268923.5% | +144.8351 to +236.1399 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 829.1 | +165720.0% | +687.1322 to +970.0678 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 94.09 | 932.1 | +890.7% | +786.0030 to +890.0887 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 15 | +15.000 (native is 0) | +11.7657 to +18.2343 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*