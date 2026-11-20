# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.43 | 5.945 |
| node-hours | 2.516 | 2.512 | 1.854 | 2.494 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.2 | 270.9 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 271.2 | 221.5 | 269.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 326.6 | 128.4 | 304.4 | 129.8 |
| response time (ms), 95th percentile | 1164 | 227.8 | 1259 | 238.1 |
| response time (ms), 99th percentile | 1636 | 324 | 1848 | 347.8 |
| time over the response line (% of samples) | 13.46 | 0.2154 | 13.4 | 0.2951 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 0.1 | 8.6 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 142.7 | 47.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 2.222 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.808 | 1047 | 10.93 | 1122 |
| utilisation (used / allocatable) | 0.05677 | 0.05809 | 0.07768 | 0.0577 |
| CPU used (cores), mean | 1.363 | 1.394 | 1.349 | 1.374 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07252 | 0.06616 |
| CPU used with Omni's own (cores), mean | 1.363 | 1.394 | 1.422 | 1.44 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.4 | 467.8 | 395 | 470.3 |
| HPA replicas, mean | 1.92 | 2.077 | 2.095 | 1.978 |
| pods started | 0.1 | 0.1 | 0.8 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.2 | 1.7 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.2 | 0.8333 | 0.2 |
| host CPU busy, the real machine under kind (%) | 39.73 | 43.75 | 42.7 | 45.51 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 775.1 | 1413 | 779.7 | 1431 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.621 | 5.346 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 154.1 | 0.05417 | 170.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 696.1 | 0.3 | 735.6 |
| queue: job turnaround, submitted to done, mean (s) | 80.47 | 795.1 | 86.08 | 803.7 |
| queue: jobs unfinished at the window's end | 0 | 10 | 0 | 10.6 |
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
| worker nodes in service, mean | 6 | 5.945 | −0.9% | −0.1804 to +0.0698 | no |
| node-hours | 2.512 | 2.494 | −0.7% | −0.0697 to +0.0344 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.4 | +0.1% | −0.8389 to +1.2581 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 269.6 | −0.6% | −5.5680 to +2.4955 | no |
| response time (ms), mean | 128.4 | 129.8 | +1.1% | −2.6446 to +5.4833 | no |
| response time (ms), 95th percentile | 227.8 | 238.1 | +4.5% | −0.8032 to +21.4432 | no |
| response time (ms), 99th percentile | 324 | 347.8 | +7.3% | +0.6986 to +46.9244 | yes: LOSS |
| time over the response line (% of samples) | 0.2154 | 0.2951 | +37.0% | −0.0693 to +0.2287 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.8 | +47.800 (native is 0) | +4.4915 to +91.1085 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1047 | 1122 | +7.1% | +12.8590 to +136.3810 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05809 | 0.0577 | −0.7% | −0.0022 to +0.0014 | no |
| CPU used (cores), mean | 1.394 | 1.374 | −1.4% | −0.0594 to +0.0190 | no |
| Omni's own CPU (cores), mean | 0 | 0.06616 | +0.066 (native is 0) | +0.0587 to +0.0736 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.44 | +3.3% | +0.0106 to +0.0813 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.8 | 470.3 | +0.5% | −10.4583 to +15.5294 | no |
| HPA replicas, mean | 2.077 | 1.978 | −4.8% | −0.2926 to +0.0940 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 43.75 | 45.51 | +4.0% | +1.4460 to +2.0611 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1413 | 1431 | +1.3% | −2.3039 to +38.5039 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.346 | −10.9% | −3.4673 to +2.1597 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 154.1 | 170.2 | +10.5% | −9.7607 to +42.0190 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696.1 | 735.6 | +5.7% | −67.5182 to +146.5182 | no |
| queue: job turnaround, submitted to done, mean (s) | 795.1 | 803.7 | +1.1% | −45.2822 to +62.5405 | no |
| queue: jobs unfinished at the window's end | 10 | 10.6 | +6.0% | −0.9526 to +2.1526 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.512 | −0.2% | −0.0103 to +0.0017 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.2 | −0.0% | −3.0598 to +2.8913 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 271.2 | −0.0% | −3.0598 to +2.8913 | no |
| response time (ms), mean | 326.6 | 128.4 | −60.7% | −355.4224 to −41.0187 | yes: GAIN |
| response time (ms), 95th percentile | 1164 | 227.8 | −80.4% | −1675.2530 to −196.2640 | yes: GAIN |
| response time (ms), 99th percentile | 1636 | 324 | −80.2% | −2340.4968 to −283.7106 | yes: GAIN |
| time over the response line (% of samples) | 13.46 | 0.2154 | −98.4% | −24.3603 to −2.1341 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 0.1 | −98.6% | −11.6845 to −2.3155 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.808 | 1047 | +10573.6% | +745.6734 to +1328.5132 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05677 | 0.05809 | +2.3% | −0.0056 to +0.0082 | no |
| CPU used (cores), mean | 1.363 | 1.394 | +2.3% | −0.1338 to +0.1970 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.363 | 1.394 | +2.3% | −0.1338 to +0.1970 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.4 | 467.8 | −6.1% | −89.8070 to +28.6356 | no |
| HPA replicas, mean | 1.92 | 2.077 | +8.2% | +0.0112 to +0.3028 | yes: power given |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 39.73 | 43.75 | +10.1% | +0.5475 to +7.5007 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.1 | 1413 | +82.3% | +538.0114 to +737.7886 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 154.1 | +231081.2% | +103.3381 to +204.7702 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 696.1 | +139120.0% | +497.8310 to +893.3690 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.47 | 795.1 | +888.1% | +550.9251 to +878.3166 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10 | +10.000 (native is 0) | +4.2379 to +15.7621 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.43 | −26.2% | −2.5224 to −0.6175 | yes: GAIN |
| node-hours | 2.516 | 1.854 | −26.3% | −1.0588 to −0.2665 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 270.9 | −0.1% | −1.4312 to +0.6813 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 221.5 | −18.3% | −79.2281 to −20.2384 | yes: GAIN |
| response time (ms), mean | 326.6 | 304.4 | −6.8% | −38.5729 to −5.9723 | yes: GAIN |
| response time (ms), 95th percentile | 1164 | 1259 | +8.2% | +2.4385 to +188.5515 | yes: LOSS |
| response time (ms), 99th percentile | 1636 | 1848 | +12.9% | +15.3719 to +407.5843 | yes: LOSS |
| time over the response line (% of samples) | 13.46 | 13.4 | −0.5% | −0.8999 to +0.7691 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 8.6 | +21.1% | −0.1259 to +3.1259 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.7 | +142.700 (native is 0) | +60.6289 to +224.7711 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.808 | 10.93 | +11.4% | −0.5568 to +2.8002 | no |
| utilisation (used / allocatable) | 0.05677 | 0.07768 | +36.8% | +0.0078 to +0.0340 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.363 | 1.349 | −1.0% | −0.0502 to +0.0237 | no |
| Omni's own CPU (cores), mean | 0 | 0.07252 | +0.073 (native is 0) | +0.0638 to +0.0813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.422 | +4.3% | +0.0256 to +0.0929 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.4 | 395 | −20.7% | −176.2899 to −30.4496 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.92 | 2.095 | +9.1% | −0.0698 to +0.4198 | no |
| pods started | 0.1 | 0.8 | +700.0% | −0.1953 to +1.5953 | no |
| pod start wait, total (s) | 0.2 | 1.7 | +750.0% | −0.5580 to +3.5580 | no |
| pod start wait, mean (s) | 0.2 | 0.8333 | +316.7% | −0.4178 to +1.6844 | no |
| host CPU busy, the real machine under kind (%) | 39.73 | 42.7 | +7.5% | +2.5824 to +3.3640 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.1 | 779.7 | +0.6% | −2.5148 to +11.7148 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.621 | −39.6% | −3.7541 to −1.0031 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.05417 | −18.7% | −0.0370 to +0.0120 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.3 | −40.0% | −0.5016 to +0.1016 | no |
| queue: job turnaround, submitted to done, mean (s) | 80.47 | 86.08 | +7.0% | −1.4198 to +12.6531 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.43 | −26.2% | −2.5224 to −0.6175 | yes: GAIN |
| node-hours | 2.512 | 1.854 | −26.2% | −1.0582 to −0.2584 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 270.9 | −0.1% | −2.9512 to +2.3699 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 221.5 | −18.3% | −82.0299 to −17.2681 | yes: GAIN |
| response time (ms), mean | 128.4 | 304.4 | +137.0% | +21.6587 to +330.2373 | yes: LOSS |
| response time (ms), 95th percentile | 227.8 | 1259 | +452.8% | +246.8358 to +1815.6712 | yes: LOSS |
| response time (ms), 99th percentile | 324 | 1848 | +470.2% | +359.4014 to +2687.7622 | yes: LOSS |
| time over the response line (% of samples) | 0.2154 | 13.4 | +6120.7% | +2.5864 to +23.7771 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 8.6 | +8500.0% | +3.9729 to +13.0271 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 142.7 | +142.700 (native is 0) | +60.6289 to +224.7711 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1047 | 10.93 | −99.0% | −1327.1493 to −744.7941 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05809 | 0.07768 | +33.7% | +0.0129 to +0.0262 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.394 | 1.349 | −3.2% | −0.2198 to +0.1300 | no |
| Omni's own CPU (cores), mean | 0 | 0.07252 | +0.073 (native is 0) | +0.0638 to +0.0813 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.394 | 1.422 | +2.0% | −0.1518 to +0.2071 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.8 | 395 | −15.6% | −91.3526 to −54.2155 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.077 | 2.095 | +0.9% | −0.2883 to +0.3243 | no |
| pods started | 0.1 | 0.8 | +700.0% | −0.1953 to +1.5953 | no |
| pod start wait, total (s) | 0.2 | 1.7 | +750.0% | −0.5580 to +3.5580 | no |
| pod start wait, mean (s) | 0.2 | 0.8333 | +316.7% | −0.4178 to +1.6844 | no |
| host CPU busy, the real machine under kind (%) | 43.75 | 42.7 | −2.4% | −4.7244 to +2.6227 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1413 | 779.7 | −44.8% | −733.5213 to −533.0787 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 154.1 | 0.05417 | −100.0% | −204.7752 to −103.3581 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696.1 | 0.3 | −100.0% | −893.6168 to −497.9832 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 795.1 | 86.08 | −89.2% | −870.1201 to −547.8882 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10 | 0 | −100.0% | −15.7621 to −4.2379 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.945 | −0.9% | −0.1804 to +0.0698 | no |
| node-hours | 2.516 | 2.494 | −0.9% | −0.0732 to +0.0293 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.4 | +0.0% | −3.1569 to +3.4075 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 269.6 | −0.6% | −6.0106 to +2.7696 | no |
| response time (ms), mean | 326.6 | 129.8 | −60.3% | −350.4340 to −43.1685 | yes: GAIN |
| response time (ms), 95th percentile | 1164 | 238.1 | −79.5% | −1658.2497 to −192.6273 | yes: GAIN |
| response time (ms), 99th percentile | 1636 | 347.8 | −78.7% | −2299.6752 to −276.9092 | yes: GAIN |
| time over the response line (% of samples) | 13.46 | 0.2951 | −97.8% | −24.1745 to −2.1604 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.1 | 0.3 | −95.8% | −11.3215 to −2.2785 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 47.8 | +47.800 (native is 0) | +4.4915 to +91.1085 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.808 | 1122 | +11334.4% | +819.7986 to +1403.6280 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05677 | 0.0577 | +1.6% | −0.0074 to +0.0093 | no |
| CPU used (cores), mean | 1.363 | 1.374 | +0.8% | −0.1815 to +0.2043 | no |
| Omni's own CPU (cores), mean | 0 | 0.06616 | +0.066 (native is 0) | +0.0587 to +0.0736 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.363 | 1.44 | +5.7% | −0.1084 to +0.2635 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 498.4 | 470.3 | −5.6% | −98.0787 to +41.9784 | no |
| HPA replicas, mean | 1.92 | 1.978 | +3.0% | −0.0907 to +0.2061 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 39.73 | 45.51 | +14.5% | +2.2706 to +9.2846 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.1 | 1431 | +84.6% | +565.2684 to +746.7316 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.346 | −10.9% | −3.4673 to +2.1597 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 170.2 | +255275.0% | +120.7465 to +219.6201 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 735.6 | +147020.0% | +554.8273 to +915.3727 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 80.47 | 803.7 | +898.8% | +571.1407 to +875.3593 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.6 | +10.600 (native is 0) | +4.2360 to +16.9640 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*