# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.966 | 6 |
| node-hours | 2.516 | 2.519 | 2.08 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.8 | 271.9 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.8 | 239.4 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 335.4 | 137.9 | 309.3 | 142.3 |
| response time (ms), 95th percentile | 1170 | 236.6 | 1247 | 247.6 |
| response time (ms), 99th percentile | 1683 | 342.6 | 1778 | 361.5 |
| time over the response line (% of samples) | 14.04 | 0.1929 | 13.97 | 0.2406 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 0.1 | 8.9 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 141.7 | 26 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 50 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.388 | 1144 | 9.902 | 1238 |
| utilisation (used / allocatable) | 0.05954 | 0.06054 | 0.07219 | 0.05796 |
| CPU used (cores), mean | 1.429 | 1.453 | 1.412 | 1.391 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07535 | 0.0666 |
| CPU used with Omni's own (cores), mean | 1.429 | 1.453 | 1.488 | 1.458 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 447.3 | 409 | 465.4 |
| HPA replicas, mean | 1.983 | 1.995 | 2.109 | 2.159 |
| pods started | 0.2 | 0.1 | 0.8 | 1 |
| pod start wait, total (s) | 0.4 | 0.1 | 1.6 | 2 |
| pod start wait, mean (s) | 0.4 | 0.1 | 0.7667 | 0.6083 |
| host CPU busy, the real machine under kind (%) | 40.85 | 45.45 | 44.29 | 46.54 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 775.8 | 1486 | 783.3 | 1509 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.215 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 134.7 | 0.1125 | 178.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 658.3 | 0.6 | 779.4 |
| queue: job turnaround, submitted to done, mean (s) | 82.1 | 854.8 | 88.76 | 893.3 |
| queue: jobs unfinished at the window's end | 0 | 9.9 | 0 | 12.8 |
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
| node-hours | 2.519 | 2.516 | −0.1% | −0.0127 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 271.5 | −0.5% | −2.4378 to −0.1033 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 271.5 | −0.5% | −2.4378 to −0.1033 | yes: GAIN |
| response time (ms), mean | 137.9 | 142.3 | +3.2% | +1.4862 to +7.3084 | yes: LOSS |
| response time (ms), 95th percentile | 236.6 | 247.6 | +4.7% | −3.4020 to +25.4220 | no |
| response time (ms), 99th percentile | 342.6 | 361.5 | +5.5% | +4.1968 to +33.5588 | yes: LOSS |
| time over the response line (% of samples) | 0.1929 | 0.2406 | +24.8% | −0.0530 to +0.1485 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26 | +26.000 (native is 0) | +17.4229 to +34.5771 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1144 | 1238 | +8.2% | +53.6223 to +133.9343 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06054 | 0.05796 | −4.3% | −0.0032 to −0.0019 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.453 | 1.391 | −4.3% | −0.0780 to −0.0458 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0666 | +0.067 (native is 0) | +0.0608 to +0.0724 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.458 | +0.3% | −0.0139 to +0.0234 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 465.4 | +4.1% | +13.3555 to +22.9369 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.159 | +8.2% | −0.0554 to +0.3827 | no |
| pods started | 0.1 | 1 | +900.0% | −0.3367 to +2.1367 | no |
| pod start wait, total (s) | 0.1 | 2 | +1900.0% | −0.4712 to +4.2712 | no |
| pod start wait, mean (s) | 0.1 | 0.6083 | +508.3% | −0.2797 to +1.2964 | no |
| host CPU busy, the real machine under kind (%) | 45.45 | 46.54 | +2.4% | +0.6130 to +1.5780 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1486 | 1509 | +1.6% | −27.0196 to +74.6196 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 134.7 | 178.4 | +32.4% | +14.5056 to +72.8444 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 658.3 | 779.4 | +18.4% | −44.9672 to +287.1672 | no |
| queue: job turnaround, submitted to done, mean (s) | 854.8 | 893.3 | +4.5% | +0.5780 to +76.3887 | yes: LOSS |
| queue: jobs unfinished at the window's end | 9.9 | 12.8 | +29.3% | +1.1658 to +4.6342 | yes: LOSS |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.519 | +0.1% | −0.0050 to +0.0116 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 272.8 | +0.2% | −2.2538 to +3.1328 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 272.8 | +0.2% | −2.2538 to +3.1328 | no |
| response time (ms), mean | 335.4 | 137.9 | −58.9% | −348.0602 to −46.9801 | yes: GAIN |
| response time (ms), 95th percentile | 1170 | 236.6 | −79.8% | −1647.4135 to −218.8445 | yes: GAIN |
| response time (ms), 99th percentile | 1683 | 342.6 | −79.6% | −2365.4815 to −315.9323 | yes: GAIN |
| time over the response line (% of samples) | 14.04 | 0.1929 | −98.6% | −24.8119 to −2.8851 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 0.1 | −98.8% | −12.0464 to −3.9536 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.388 | 1144 | +12089.7% | +901.0295 to +1369.0105 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05954 | 0.06054 | +1.7% | −0.0058 to +0.0078 | no |
| CPU used (cores), mean | 1.429 | 1.453 | +1.7% | −0.1386 to +0.1865 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.429 | 1.453 | +1.7% | −0.1386 to +0.1865 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 447.3 | −3.6% | −62.9804 to +29.5907 | no |
| HPA replicas, mean | 1.983 | 1.995 | +0.6% | −0.1608 to +0.1849 | no |
| pods started | 0.2 | 0.1 | −50.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.4 | 0.1 | −75.0% | −0.9786 to +0.3786 | no |
| pod start wait, mean (s) | 0.4 | 0.1 | −75.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 40.85 | 45.45 | +11.2% | +0.7916 to +8.3945 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.8 | 1486 | +91.5% | +649.0238 to +770.3762 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 134.7 | +248607.7% | +105.6249 to +163.7001 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 658.3 | +219333.3% | +523.6851 to +792.3149 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.1 | 854.8 | +941.2% | +695.7934 to +849.6316 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.9 | +9.900 (native is 0) | +4.1731 to +15.6269 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.966 | −17.2% | −1.7615 to −0.3056 | yes: GAIN |
| node-hours | 2.516 | 2.079 | −17.3% | −0.7424 to −0.1296 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.9 | −0.2% | −1.6548 to +0.7407 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 239.4 | −12.1% | −56.4296 to −9.4345 | yes: GAIN |
| response time (ms), mean | 335.4 | 309.3 | −7.8% | −32.1022 to −20.2012 | yes: GAIN |
| response time (ms), 95th percentile | 1170 | 1247 | +6.6% | −2.5528 to +157.7248 | no |
| response time (ms), 99th percentile | 1683 | 1778 | +5.6% | −5.7909 to +194.7567 | no |
| time over the response line (% of samples) | 14.04 | 13.97 | −0.5% | −0.6285 to +0.4942 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.9 | +9.9% | +0.0612 to +1.5388 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 141.7 | +141.700 (native is 0) | +61.3482 to +222.0518 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.388 | 9.902 | +5.5% | −1.4563 to +2.4830 | no |
| utilisation (used / allocatable) | 0.05954 | 0.07219 | +21.2% | +0.0036 to +0.0217 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.412 | −1.2% | −0.0528 to +0.0193 | no |
| Omni's own CPU (cores), mean | 0 | 0.07535 | +0.075 (native is 0) | +0.0696 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.488 | +4.1% | +0.0198 to +0.0974 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 409 | −11.9% | −90.4469 to −19.5265 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.983 | 2.109 | +6.4% | −0.0820 to +0.3341 | no |
| pods started | 0.2 | 0.8 | +300.0% | −0.0911 to +1.2911 | no |
| pod start wait, total (s) | 0.4 | 1.6 | +300.0% | −0.6096 to +3.0096 | no |
| pod start wait, mean (s) | 0.4 | 0.7667 | +91.7% | −0.5901 to +1.3234 | no |
| host CPU busy, the real machine under kind (%) | 40.85 | 44.29 | +8.4% | +3.2004 to +3.6715 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.8 | 783.3 | +1.0% | +1.3722 to +13.6278 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.215 | −29.8% | −3.0091 to −0.5611 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1125 | +107.7% | −0.0585 to +0.1752 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.6 | +100.0% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 82.1 | 88.76 | +8.1% | +1.2415 to +12.0835 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.966 | −17.2% | −1.7615 to −0.3056 | yes: GAIN |
| node-hours | 2.519 | 2.08 | −17.4% | −0.7455 to −0.1332 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 271.9 | −0.3% | −4.0955 to +2.3024 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 239.4 | −12.2% | −58.4669 to −8.2762 | yes: GAIN |
| response time (ms), mean | 137.9 | 309.3 | +124.3% | +20.0625 to +322.6743 | yes: LOSS |
| response time (ms), 95th percentile | 236.6 | 1247 | +427.1% | +253.4569 to +1767.9731 | yes: LOSS |
| response time (ms), 99th percentile | 342.6 | 1778 | +418.9% | +342.6416 to +2527.7380 | yes: LOSS |
| time over the response line (% of samples) | 0.1929 | 13.97 | +7144.7% | +3.0018 to +24.5609 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 8.9 | +8800.0% | +4.8850 to +12.7150 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 141.7 | +141.700 (native is 0) | +61.3482 to +222.0518 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1144 | 9.902 | −99.1% | −1369.2831 to −899.7303 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06054 | 0.07219 | +19.2% | +0.0038 to +0.0195 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.453 | 1.412 | −2.8% | −0.2247 to +0.1433 | no |
| Omni's own CPU (cores), mean | 0 | 0.07535 | +0.075 (native is 0) | +0.0696 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.488 | +2.4% | −0.1514 to +0.2207 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 409 | −8.6% | −71.8544 to −4.7293 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.109 | +5.7% | −0.1196 to +0.3475 | no |
| pods started | 0.1 | 0.8 | +700.0% | +0.0214 to +1.3786 | yes: power given |
| pod start wait, total (s) | 0.1 | 1.6 | +1500.0% | −0.1259 to +3.1259 | no |
| pod start wait, mean (s) | 0.1 | 0.7667 | +666.7% | −0.0873 to +1.4207 | no |
| host CPU busy, the real machine under kind (%) | 45.45 | 44.29 | −2.5% | −4.9423 to +2.6281 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1486 | 783.3 | −47.3% | −766.2135 to −638.1865 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.021 | −66.3% | −4.2491 to −3.7084 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 134.7 | 0.1125 | −99.9% | −163.5868 to −105.6216 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 658.3 | 0.6 | −99.9% | −792.2036 to −523.1964 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 854.8 | 88.76 | −89.6% | −839.4824 to −692.6176 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.9 | 0 | −100.0% | −15.6269 to −4.1731 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.516 | +0.0% | −0.0050 to +0.0066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.4 | 271.5 | −0.3% | −3.2407 to +1.5787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.4 | 271.5 | −0.3% | −3.2407 to +1.5787 | no |
| response time (ms), mean | 335.4 | 142.3 | −57.6% | −341.8415 to −44.4041 | yes: GAIN |
| response time (ms), 95th percentile | 1170 | 247.6 | −78.8% | −1632.9049 to −211.3331 | yes: GAIN |
| response time (ms), 99th percentile | 1683 | 361.5 | −78.5% | −2340.0972 to −303.5610 | yes: GAIN |
| time over the response line (% of samples) | 14.04 | 0.2406 | −98.3% | −24.7433 to −2.8582 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 0.1 | −98.8% | −12.0464 to −3.9536 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26 | +26.000 (native is 0) | +17.4229 to +34.5771 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.388 | 1238 | +13088.6% | +1026.6979 to +1430.8988 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05954 | 0.05796 | −2.7% | −0.0082 to +0.0050 | no |
| CPU used (cores), mean | 1.429 | 1.391 | −2.7% | −0.1965 to +0.1207 | no |
| Omni's own CPU (cores), mean | 0 | 0.0666 | +0.067 (native is 0) | +0.0608 to +0.0724 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.458 | +2.0% | −0.1253 to +0.1826 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 465.4 | +0.3% | −43.5639 to +46.4665 | no |
| HPA replicas, mean | 1.983 | 2.159 | +8.9% | −0.0487 to +0.4002 | no |
| pods started | 0.2 | 1 | +400.0% | −0.3583 to +1.9583 | no |
| pod start wait, total (s) | 0.4 | 2 | +400.0% | −0.4841 to +3.6841 | no |
| pod start wait, mean (s) | 0.4 | 0.6083 | +52.1% | −0.4691 to +0.8858 | no |
| host CPU busy, the real machine under kind (%) | 40.85 | 46.54 | +13.9% | +1.7704 to +9.6067 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 775.8 | 1509 | +94.5% | +683.8673 to +783.1327 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 178.4 | +329238.5% | +145.8601 to +210.8149 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 779.4 | +259700.0% | +647.4112 to +910.7888 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 82.1 | 893.3 | +988.1% | +750.4738 to +871.9179 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.8 | +12.800 (native is 0) | +7.7668 to +17.8332 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*