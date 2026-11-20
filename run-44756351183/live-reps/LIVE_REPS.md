# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.574 | 6 |
| node-hours | 2.516 | 2.513 | 1.918 | 2.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 272.1 | 271.6 | 272 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 272.1 | 226.8 | 272 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 260.7 | 132.8 | 240.9 | 136.5 |
| response time (ms), 95th percentile | 810.4 | 224.3 | 897.2 | 240.8 |
| response time (ms), 99th percentile | 1152 | 328 | 1316 | 352.2 |
| time over the response line (% of samples) | 9.97 | 0.1751 | 10.6 | 0.1609 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 0.2 | 8.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 182.4 | 33.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.555 | 1078 | 8.758 | 1186 |
| utilisation (used / allocatable) | 0.05647 | 0.0604 | 0.07567 | 0.05831 |
| CPU used (cores), mean | 1.355 | 1.45 | 1.358 | 1.399 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0734 | 0.06461 |
| CPU used with Omni's own (cores), mean | 1.355 | 1.45 | 1.432 | 1.464 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 448.1 | 398.8 | 463 |
| HPA replicas, mean | 2.003 | 1.98 | 2.278 | 2.206 |
| pods started | 0 | 0.2 | 1.2 | 0.9 |
| pod start wait, total (s) | 0 | 0.4 | 2.6 | 2.1 |
| pod start wait, mean (s) | 0 | 0.2 | 1.067 | 1.017 |
| host CPU busy, the real machine under kind (%) | 39.47 | 45.34 | 42.66 | 46.43 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 749.8 | 1484 | 756.7 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.482 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 129.1 | 0.0625 | 168.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 600.8 | 0.6 | 772.3 |
| queue: job turnaround, submitted to done, mean (s) | 56.29 | 816.8 | 61.65 | 864.4 |
| queue: jobs unfinished at the window's end | 0 | 7.9 | 0 | 11.3 |
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
| node-hours | 2.513 | 2.519 | +0.2% | −0.0045 to +0.0162 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272 | −0.0% | −0.9757 to +0.8024 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 272 | −0.0% | −0.9757 to +0.8024 | no |
| response time (ms), mean | 132.8 | 136.5 | +2.7% | +1.4026 to +5.9013 | yes: LOSS |
| response time (ms), 95th percentile | 224.3 | 240.8 | +7.4% | +8.8113 to +24.2127 | yes: LOSS |
| response time (ms), 99th percentile | 328 | 352.2 | +7.4% | +10.0600 to +38.3536 | yes: LOSS |
| time over the response line (% of samples) | 0.1751 | 0.1609 | −8.1% | −0.1314 to +0.1030 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.1 | −50.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.5 | +33.500 (native is 0) | +22.2089 to +44.7911 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1078 | 1186 | +10.1% | +18.5648 to +199.1885 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0604 | 0.05831 | −3.5% | −0.0034 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.45 | 1.399 | −3.5% | −0.0821 to −0.0184 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06461 | +0.065 (native is 0) | +0.0595 to +0.0697 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.464 | +1.0% | −0.0194 to +0.0482 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.1 | 463 | +3.3% | +5.5290 to +24.2683 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.206 | +11.4% | −0.0544 to +0.5055 | no |
| pods started | 0.2 | 0.9 | +350.0% | −0.4209 to +1.8209 | no |
| pod start wait, total (s) | 0.4 | 2.1 | +425.0% | −0.7560 to +4.1560 | no |
| pod start wait, mean (s) | 0.2 | 1.017 | +408.3% | −0.0215 to +1.6549 | no |
| host CPU busy, the real machine under kind (%) | 45.34 | 46.43 | +2.4% | +0.3487 to +1.8330 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1484 | 1510 | +1.8% | −22.3423 to +74.5423 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 129.1 | 168.1 | +30.2% | +2.0266 to +75.9317 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 600.8 | 772.3 | +28.5% | −15.8201 to +358.8201 | no |
| queue: job turnaround, submitted to done, mean (s) | 816.8 | 864.4 | +5.8% | +1.3595 to +93.8905 | yes: LOSS |
| queue: jobs unfinished at the window's end | 7.9 | 11.3 | +43.0% | −0.0913 to +6.8913 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.513 | −0.1% | −0.0127 to +0.0084 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 272.1 | +0.3% | −1.2582 to +3.0029 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 272.1 | +0.3% | −1.2582 to +3.0029 | no |
| response time (ms), mean | 260.7 | 132.8 | −49.1% | −237.4533 to −18.2775 | yes: GAIN |
| response time (ms), 95th percentile | 810.4 | 224.3 | −72.3% | −1105.9228 to −66.2702 | yes: GAIN |
| response time (ms), 99th percentile | 1152 | 328 | −71.5% | −1552.4172 to −95.7024 | yes: GAIN |
| time over the response line (% of samples) | 9.97 | 0.1751 | −98.2% | −18.8525 to −0.7370 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 0.2 | −97.1% | −10.5367 to −3.0633 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.555 | 1078 | +12495.7% | +844.2139 to +1293.8028 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05647 | 0.0604 | +7.0% | −0.0015 to +0.0094 | no |
| CPU used (cores), mean | 1.355 | 1.45 | +7.0% | −0.0367 to +0.2254 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.355 | 1.45 | +7.0% | −0.0367 to +0.2254 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 448.1 | −7.3% | −74.8163 to +3.9324 | no |
| HPA replicas, mean | 2.003 | 1.98 | −1.2% | −0.1630 to +0.1168 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 39.47 | 45.34 | +14.9% | +3.1823 to +8.5649 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.8 | 1484 | +97.9% | +676.6365 to +790.7635 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 129.1 | +344111.1% | +101.3919 to +156.6914 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 600.8 | +200166.7% | +435.4345 to +765.5655 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 56.29 | 816.8 | +1351.1% | +663.5521 to +857.4312 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 7.9 | +7.900 (native is 0) | +1.7703 to +14.0297 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.574 | −23.8% | −2.1284 to −0.7232 | yes: GAIN |
| node-hours | 2.516 | 1.918 | −23.7% | −0.8897 to −0.3046 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.6 | +0.2% | −0.3549 to +1.2088 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 226.8 | −16.4% | −66.4879 to −22.3541 | yes: GAIN |
| response time (ms), mean | 260.7 | 240.9 | −7.6% | −31.2573 to −8.2993 | yes: GAIN |
| response time (ms), 95th percentile | 810.4 | 897.2 | +10.7% | +16.6521 to +156.8059 | yes: LOSS |
| response time (ms), 99th percentile | 1152 | 1316 | +14.2% | −70.0132 to +397.6796 | no |
| time over the response line (% of samples) | 9.97 | 10.6 | +6.3% | +0.1780 to +1.0824 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 8.1 | +15.7% | +0.1198 to +2.0802 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 182.4 | +182.400 (native is 0) | +83.5793 to +281.2207 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.555 | 8.758 | +2.4% | −0.8928 to +1.2995 | no |
| utilisation (used / allocatable) | 0.05647 | 0.07567 | +34.0% | +0.0095 to +0.0289 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.355 | 1.358 | +0.2% | −0.0185 to +0.0241 | no |
| Omni's own CPU (cores), mean | 0 | 0.0734 | +0.073 (native is 0) | +0.0684 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.355 | 1.432 | +5.6% | +0.0520 to +0.1004 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 398.8 | −17.5% | −125.4079 to −44.2300 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.278 | +13.7% | +0.0291 to +0.5210 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.2583 to +2.1417 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.4356 to +4.7644 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.067 | +1.067 (native is 0) | +0.2327 to +1.9006 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.47 | 42.66 | +8.1% | +2.8314 to +3.5416 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.8 | 756.7 | +0.9% | −0.4216 to +14.2216 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.482 | −42.0% | −3.5857 to −1.4498 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 0.0625 | +66.7% | −0.0038 to +0.0538 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 56.29 | 61.65 | +9.5% | +0.1296 to +10.6037 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.574 | −23.8% | −2.1284 to −0.7232 | yes: GAIN |
| node-hours | 2.513 | 1.918 | −23.7% | −0.8906 to −0.2994 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.6 | −0.2% | −2.4869 to +1.5960 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 226.8 | −16.6% | −69.1281 to −21.4586 | yes: GAIN |
| response time (ms), mean | 132.8 | 240.9 | +81.4% | −7.5141 to +223.6882 | no |
| response time (ms), 95th percentile | 224.3 | 897.2 | +299.9% | +86.3501 to +1259.3009 | yes: LOSS |
| response time (ms), 99th percentile | 328 | 1316 | +301.2% | +123.4440 to +1852.3420 | yes: LOSS |
| time over the response line (% of samples) | 0.1751 | 10.6 | +5952.3% | +1.2190 to +19.6309 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 8.1 | +3950.0% | +4.5542 to +11.2458 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 182.4 | +182.400 (native is 0) | +83.5793 to +281.2207 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1078 | 8.758 | −99.2% | −1293.4166 to −844.1934 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0604 | 0.07567 | +25.3% | +0.0084 to +0.0222 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.45 | 1.358 | −6.3% | −0.2368 to +0.0537 | no |
| Omni's own CPU (cores), mean | 0 | 0.0734 | +0.073 (native is 0) | +0.0684 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.45 | 1.432 | −1.3% | −0.1666 to +0.1303 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.1 | 398.8 | −11.0% | −72.8595 to −25.8946 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.98 | 2.278 | +15.1% | +0.0370 to +0.5593 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | +0.1740 to +1.8260 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.6 | +550.0% | +0.4544 to +3.9456 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.067 | +433.3% | +0.1343 to +1.5990 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.34 | 42.66 | −5.9% | −5.5208 to +0.1466 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1484 | 756.7 | −49.0% | −786.1104 to −667.4896 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 129.1 | 0.0625 | −100.0% | −156.6744 to −101.3589 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 600.8 | 0.6 | −99.9% | −765.4763 to −434.9237 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 816.8 | 61.65 | −92.5% | −848.2717 to −661.9783 | yes: GAIN |
| queue: jobs unfinished at the window's end | 7.9 | 0 | −100.0% | −14.0297 to −1.7703 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.519 | +0.1% | −0.0046 to +0.0119 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 272 | +0.3% | −1.1956 to +2.7670 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 272 | +0.3% | −1.1956 to +2.7670 | no |
| response time (ms), mean | 260.7 | 136.5 | −47.7% | −233.1065 to −15.3204 | yes: GAIN |
| response time (ms), 95th percentile | 810.4 | 240.8 | −70.3% | −1086.5954 to −52.5736 | yes: GAIN |
| response time (ms), 99th percentile | 1152 | 352.2 | −69.4% | −1531.1275 to −68.5785 | yes: GAIN |
| time over the response line (% of samples) | 9.97 | 0.1609 | −98.4% | −18.8706 to −0.7473 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 0.1 | −98.6% | −10.5699 to −3.2301 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.5 | +33.500 (native is 0) | +22.2089 to +44.7911 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.555 | 1186 | +13768.4% | +1009.3048 to +1346.4652 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05647 | 0.05831 | +3.3% | −0.0033 to +0.0070 | no |
| CPU used (cores), mean | 1.355 | 1.399 | +3.3% | −0.0801 to +0.1684 | no |
| Omni's own CPU (cores), mean | 0 | 0.06461 | +0.065 (native is 0) | +0.0595 to +0.0697 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.355 | 1.464 | +8.0% | −0.0111 to +0.2286 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 483.6 | 463 | −4.2% | −58.1670 to +17.0804 | no |
| HPA replicas, mean | 2.003 | 2.206 | +10.1% | −0.0924 to +0.4973 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.1366 to +1.9366 | no |
| pod start wait, total (s) | 0 | 2.1 | +2.100 (native is 0) | −0.2712 to +4.4712 | no |
| pod start wait, mean (s) | 0 | 1.017 | +1.017 (native is 0) | +0.0425 to +1.9908 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.47 | 46.43 | +17.6% | +4.3872 to +9.5418 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 749.8 | 1510 | +101.3% | +727.1112 to +792.4888 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0375 | 168.1 | +448055.6% | +122.1005 to +213.9411 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 772.3 | +257333.3% | +548.5573 to +995.4427 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 56.29 | 864.4 | +1435.7% | +737.0892 to +879.1441 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.3 | +11.300 (native is 0) | +7.1420 to +15.4580 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*