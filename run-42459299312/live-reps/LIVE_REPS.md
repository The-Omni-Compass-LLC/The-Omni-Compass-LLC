# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.811 | 5.931 |
| node-hours | 2.517 | 2.516 | 2.015 | 2.493 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.3 | 271.7 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 272.3 | 234.4 | 269.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 313.5 | 149.4 | 302 | 103.2 |
| response time (ms), 95th percentile | 1051 | 264 | 1222 | 217.5 |
| response time (ms), 99th percentile | 1512 | 375 | 1721 | 339 |
| time over the response line (% of samples) | 13.89 | 0.281 | 14.06 | 0.1942 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 0 | 9.5 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 123.2 | 114 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.03 | 1278 | 8.783 | 1082 |
| utilisation (used / allocatable) | 0.05861 | 0.05994 | 0.07289 | 0.05807 |
| CPU used (cores), mean | 1.407 | 1.439 | 1.39 | 1.379 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07326 | 0.06668 |
| CPU used with Omni's own (cores), mean | 1.407 | 1.439 | 1.463 | 1.446 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.9 | 451.9 | 405.9 | 467.3 |
| HPA replicas, mean | 2.045 | 2.099 | 2.378 | 2.181 |
| pods started | 0 | 0 | 2 | 1 |
| pod start wait, total (s) | 0 | 0 | 4.7 | 1.8 |
| pod start wait, mean (s) | 0 | 0 | 1.933 | 0.7333 |
| host CPU busy, the real machine under kind (%) | 39.72 | 45.48 | 43.04 | 45.25 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 766.6 | 1510 | 775.4 | 1441 |
| batch: worker machines in service after the queue finished, mean | 6 | nan | 4.014 | 4.545 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 171.5 | 0.0625 | 134.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 634.8 | 0.4 | 663 |
| queue: job turnaround, submitted to done, mean (s) | 72.35 | 931.8 | 81.59 | 802.2 |
| queue: jobs unfinished at the window's end | 0 | 13.83 | 0 | 10.4 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.519 | 2.526 | +0.3% | −0.0185 to +0.0319 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.2 | +0.1% | −4.5280 to +5.2613 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 273.2 | +0.1% | −4.5280 to +5.2613 | no |
| response time (ms), mean | 147.1 | 116.1 | −21.1% | −43.1850 to −18.8490 | yes: GAIN |
| response time (ms), 95th percentile | 261.1 | 249.8 | −4.3% | −25.7786 to +3.1786 | no |
| response time (ms), 99th percentile | 382.9 | 386.5 | +1.0% | −62.4248 to +69.7755 | no |
| time over the response line (% of samples) | 0.3315 | 0.2498 | −24.6% | −0.3972 to +0.2339 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 127.7 | +127.667 (native is 0) | +74.1332 to +181.2002 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1228 | 1305 | +6.3% | −370.3242 to +525.7464 | no |
| utilisation (used / allocatable) | 0.06066 | 0.05992 | −1.2% | −0.0063 to +0.0048 | no |
| CPU used (cores), mean | 1.456 | 1.438 | −1.2% | −0.1502 to +0.1148 | no |
| Omni's own CPU (cores), mean | 0 | 0.0713 | +0.071 (native is 0) | +0.0528 to +0.0898 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.456 | 1.509 | +3.7% | −0.0873 to +0.1945 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.2 | 451.5 | +1.0% | −32.8742 to +41.4215 | no |
| HPA replicas, mean | 2.103 | 2.268 | +7.9% | −0.3811 to +0.7116 | no |
| pods started | 0 | 1.667 | +1.667 (native is 0) | −2.1282 to +5.4616 | no |
| pod start wait, total (s) | 0 | 3 | +3.000 (native is 0) | −3.5729 to +9.5729 | no |
| pod start wait, mean (s) | 0 | 1.222 | +1.222 (native is 0) | −1.4398 to +3.8842 | no |
| host CPU busy, the real machine under kind (%) | 45.55 | 47.38 | +4.0% | −1.7840 to +5.4297 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1512 | 1516 | +0.3% | −9.8322 to +17.8322 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 174.5 | 156.5 | −10.3% | −173.9001 to +137.8168 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 654.7 | 755.3 | +15.4% | +47.1332 to +154.2002 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 917.9 | 942.8 | +2.7% | −285.3778 to +335.1278 | no |
| queue: jobs unfinished at the window's end | 12.67 | 15 | +18.4% | −19.9335 to +24.6002 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 6 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.516 | −0.1% | −0.0139 to +0.0089 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 272.3 | −0.5% | −5.2134 to +2.6055 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 272.3 | −0.5% | −5.2134 to +2.6055 | no |
| response time (ms), mean | 368.1 | 149.4 | −59.4% | −415.0451 to −22.2888 | yes: GAIN |
| response time (ms), 95th percentile | 1279 | 264 | −79.4% | −1950.6978 to −78.4755 | yes: GAIN |
| response time (ms), 99th percentile | 1806 | 375 | −79.2% | −2765.1866 to −96.9380 | yes: GAIN |
| time over the response line (% of samples) | 17.35 | 0.281 | −98.4% | −32.5312 to −1.6120 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.17 | 0 | −100.0% | −14.8278 to −7.5056 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.883 | 1278 | +12828.9% | +1082.4475 to +1453.4080 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06233 | 0.05994 | −3.8% | −0.0113 to +0.0065 | no |
| CPU used (cores), mean | 1.496 | 1.439 | −3.8% | −0.2713 to +0.1569 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.496 | 1.439 | −3.8% | −0.2713 to +0.1569 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 440.4 | 451.9 | +2.6% | −46.7925 to +69.9527 | no |
| HPA replicas, mean | 2.007 | 2.099 | +4.5% | −0.0732 to +0.2558 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.6 | 45.48 | +6.8% | −1.8954 to +7.6570 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.2 | 1510 | +93.5% | +662.8382 to +796.4951 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05556 | 171.5 | +308600.0% | +100.3215 to +242.5674 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1667 | 634.8 | +380800.0% | +379.4774 to +889.8559 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 86.24 | 931.8 | +980.4% | +793.5071 to +897.5207 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 13.83 | +13.833 (native is 0) | +8.5054 to +19.1612 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.811 | −19.8% | −1.9550 to −0.4233 | yes: GAIN |
| node-hours | 2.517 | 2.015 | −19.9% | −0.8268 to −0.1771 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.7 | −0.2% | −1.6765 to +0.7785 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 234.4 | −13.9% | −62.5748 to −12.9399 | yes: GAIN |
| response time (ms), mean | 313.5 | 302 | −3.6% | −26.2016 to +3.3415 | no |
| response time (ms), 95th percentile | 1051 | 1222 | +16.3% | +36.4981 to +305.3179 | yes: LOSS |
| response time (ms), 99th percentile | 1512 | 1721 | +13.8% | +58.1341 to +359.4161 | yes: LOSS |
| time over the response line (% of samples) | 13.89 | 14.06 | +1.2% | −0.3026 to +0.6470 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.5 | +6.7% | −0.1689 to +1.3689 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 123.2 | +123.200 (native is 0) | +50.2365 to +196.1635 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.03 | 8.783 | −2.7% | −1.8295 to +1.3362 | no |
| utilisation (used / allocatable) | 0.05861 | 0.07289 | +24.4% | +0.0053 to +0.0233 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.407 | 1.39 | −1.2% | −0.0518 to +0.0186 | no |
| Omni's own CPU (cores), mean | 0 | 0.07326 | +0.073 (native is 0) | +0.0673 to +0.0792 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.463 | +4.0% | +0.0183 to +0.0950 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 472.9 | 405.9 | −14.2% | −113.3115 to −20.8233 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.045 | 2.378 | +16.3% | +0.1222 to +0.5445 | yes: power given |
| pods started | 0 | 2 | +2.000 (native is 0) | +0.9884 to +3.0116 | yes: power given |
| pod start wait, total (s) | 0 | 4.7 | +4.700 (native is 0) | +2.1755 to +7.2245 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.933 | +1.933 (native is 0) | +1.0673 to +2.7993 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.72 | 43.04 | +8.3% | +3.0192 to +3.6085 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 766.6 | 775.4 | +1.1% | +1.0386 to +16.5614 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.014 | −33.1% | −3.1062 to −0.8661 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.0625 | +15.4% | −0.0309 to +0.0476 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 72.35 | 81.59 | +12.8% | +1.4677 to +17.0073 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 6 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.168 | −13.9% | −1.5665 to −0.0972 | yes: GAIN |
| node-hours | 2.516 | 2.166 | −13.9% | −0.6614 to −0.0383 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 273.6 | +0.5% | −3.2004 to +5.6918 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 247.4 | −9.1% | −51.2652 to +1.4510 | no |
| response time (ms), mean | 149.4 | 357.9 | +139.5% | −9.4916 to +426.4641 | no |
| response time (ms), 95th percentile | 264 | 1446 | +447.7% | +68.5751 to +2295.1749 | yes: LOSS |
| response time (ms), 99th percentile | 375 | 2057 | +448.5% | +121.3189 to +3242.4571 | yes: LOSS |
| time over the response line (% of samples) | 0.281 | 17.47 | +6117.6% | +2.1117 to +32.2740 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.5 | +11.500 (native is 0) | +7.4757 to +15.5243 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.33 | +81.333 (native is 0) | +2.2132 to +160.4535 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1278 | 9.947 | −99.2% | −1452.7889 to −1082.9389 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05994 | 0.07278 | +21.4% | +0.0065 to +0.0192 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.5 | +4.3% | −0.1756 to +0.2993 | no |
| Omni's own CPU (cores), mean | 0 | 0.07618 | +0.076 (native is 0) | +0.0706 to +0.0818 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.577 | +9.6% | −0.1035 to +0.3796 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.9 | 395.4 | −12.5% | −91.6105 to −21.4199 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.099 | 2.451 | +16.8% | +0.0687 to +0.6356 | yes: power given |
| pods started | 0 | 2.167 | +2.167 (native is 0) | +0.4851 to +3.8482 | yes: power given |
| pod start wait, total (s) | 0 | 5.167 | +5.167 (native is 0) | +0.8945 to +9.4388 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.083 | +2.083 (native is 0) | +0.6882 to +3.4784 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.48 | 46.04 | +1.2% | −4.3971 to +5.5109 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1510 | 791.2 | −47.6% | −795.1157 to −642.2177 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 171.5 | 0.06944 | −100.0% | −242.4823 to −100.3789 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 634.8 | 0.5 | −99.9% | −889.0922 to −379.5745 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 931.8 | 97.97 | −89.5% | −888.3902 to −779.1792 | yes: GAIN |
| queue: jobs unfinished at the window's end | 13.83 | 0 | −100.0% | −19.1612 to −8.5054 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 5 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.931 | −1.2% | −0.2623 to +0.1234 | no |
| node-hours | 2.52 | 2.493 | −1.1% | −0.1183 to +0.0649 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.9 | +0.2% | −2.1495 to +3.4132 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 269.7 | −0.6% | −8.2675 to +5.1729 | no |
| response time (ms), mean | 236.2 | 103.2 | −56.3% | −309.1614 to +43.1100 | no |
| response time (ms), 95th percentile | 696.4 | 217.5 | −68.8% | −1268.1499 to +310.4299 | no |
| response time (ms), 99th percentile | 1033 | 339 | −67.2% | −1915.4373 to +527.4293 | no |
| time over the response line (% of samples) | 8.726 | 0.1942 | −97.8% | −24.2342 to +7.1701 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 0 | −100.0% | −14.5103 to −1.4897 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114 | +114.000 (native is 0) | +84.0115 to +143.9885 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 7.867 | 1082 | +13648.8% | +547.9982 to +1599.4085 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05556 | 0.05807 | +4.5% | −0.0064 to +0.0114 | no |
| CPU used (cores), mean | 1.333 | 1.379 | +3.4% | −0.1465 to +0.2383 | no |
| Omni's own CPU (cores), mean | 0 | 0.06668 | +0.067 (native is 0) | +0.0564 to +0.0770 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.333 | 1.446 | +8.4% | −0.0709 to +0.2961 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 495.4 | 467.3 | −5.7% | −100.9204 to +44.5560 | no |
| HPA replicas, mean | 2.02 | 2.181 | +8.0% | −0.2488 to +0.5719 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | −0.7557 to +2.7557 | no |
| pod start wait, total (s) | 0 | 1.8 | +1.800 (native is 0) | −1.2912 to +4.8912 | no |
| pod start wait, mean (s) | 0 | 0.7333 | +0.733 (native is 0) | −0.5218 to +1.9885 | no |
| host CPU busy, the real machine under kind (%) | 37.62 | 45.25 | +20.3% | +3.3247 to +11.9385 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 743.4 | 1441 | +93.9% | +504.2161 to +891.7839 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.545 | −24.2% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 134.7 | +269216.7% | +82.3542 to +186.8625 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 663 | +331400.0% | +453.3795 to +872.2205 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 49.87 | 802.2 | +1508.4% | +476.7891 to +1027.7942 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.4 | +10.400 (native is 0) | −0.8625 to +21.6625 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*