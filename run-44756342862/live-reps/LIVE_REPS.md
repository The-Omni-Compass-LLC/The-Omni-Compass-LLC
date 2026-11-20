# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.234 | 5.993 |
| node-hours | 2.51 | 2.515 | 1.776 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 272 | 271.5 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 272 | 215.9 | 270.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 280.4 | 121.7 | 263.6 | 124.8 |
| response time (ms), 95th percentile | 967.7 | 209.2 | 1080 | 222.1 |
| response time (ms), 99th percentile | 1380 | 307.4 | 1557 | 326.5 |
| time over the response line (% of samples) | 10.53 | 0.1385 | 10.49 | 0.1164 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 0 | 6.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 184.9 | 35.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.91 | 1005 | 10.07 | 1126 |
| utilisation (used / allocatable) | 0.05627 | 0.05954 | 0.08121 | 0.05733 |
| CPU used (cores), mean | 1.35 | 1.429 | 1.343 | 1.374 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07017 | 0.06299 |
| CPU used with Omni's own (cores), mean | 1.35 | 1.429 | 1.413 | 1.437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.1 | 454.6 | 383.9 | 470.4 |
| HPA replicas, mean | 1.976 | 1.973 | 2.068 | 1.982 |
| pods started | 0.1 | 0.1 | 0.9 | 0.3 |
| pod start wait, total (s) | 0.2 | 0.1 | 2.2 | 0.6 |
| pod start wait, mean (s) | 0.2 | 0.1 | 1.517 | 0.35 |
| host CPU busy, the real machine under kind (%) | 39.02 | 44.23 | 41.83 | 45.49 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 763.9 | 1410 | 772.3 | 1481 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.288 | 5.781 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 134.9 | 0.09167 | 157.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 643 | 0.4 | 688.2 |
| queue: job turnaround, submitted to done, mean (s) | 70.12 | 754 | 78.4 | 816.8 |
| queue: jobs unfinished at the window's end | 0 | 7.7 | 0 | 8.4 |
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
| worker nodes in service, mean | 6 | 5.993 | −0.1% | −0.0243 to +0.0094 | no |
| node-hours | 2.515 | 2.513 | −0.1% | −0.0138 to +0.0092 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.2 | −0.3% | −1.7408 to +0.1787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 270.9 | −0.4% | −2.0350 to +0.0021 | no |
| response time (ms), mean | 121.7 | 124.8 | +2.6% | +0.0811 to +6.1828 | yes: LOSS |
| response time (ms), 95th percentile | 209.2 | 222.1 | +6.2% | +7.3641 to +18.4589 | yes: LOSS |
| response time (ms), 99th percentile | 307.4 | 326.5 | +6.2% | +1.6356 to +36.6126 | yes: LOSS |
| time over the response line (% of samples) | 0.1385 | 0.1164 | −16.0% | −0.1300 to +0.0858 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +19.2642 to +52.3358 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1005 | 1126 | +12.0% | +21.6370 to +219.5363 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05954 | 0.05733 | −3.7% | −0.0042 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.374 | −3.8% | −0.1010 to −0.0084 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06299 | +0.063 (native is 0) | +0.0559 to +0.0701 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.437 | +0.6% | −0.0346 to +0.0511 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.6 | 470.4 | +3.5% | +1.5129 to +30.2279 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.973 | 1.982 | +0.5% | −0.1457 to +0.1640 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.1 | 0.6 | +500.0% | −0.6802 to +1.6802 | no |
| pod start wait, mean (s) | 0.1 | 0.35 | +250.0% | −0.4084 to +0.9084 | no |
| host CPU busy, the real machine under kind (%) | 44.23 | 45.49 | +2.8% | +0.4700 to +2.0320 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1410 | 1481 | +5.0% | −7.9270 to +149.7270 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.781 | −3.6% | −2.9982 to +2.5607 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 134.9 | 157.5 | +16.7% | −14.8084 to +59.9417 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 643 | 688.2 | +7.0% | −147.5649 to +237.9649 | no |
| queue: job turnaround, submitted to done, mean (s) | 754 | 816.8 | +8.3% | −7.6003 to +133.0586 | no |
| queue: jobs unfinished at the window's end | 7.7 | 8.4 | +9.1% | −0.6509 to +2.0509 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.515 | +0.2% | −0.0035 to +0.0138 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 272 | +0.5% | −1.5972 to +4.3564 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 272 | +0.5% | −1.5972 to +4.3564 | no |
| response time (ms), mean | 280.4 | 121.7 | −56.6% | −306.5817 to −10.9640 | yes: GAIN |
| response time (ms), 95th percentile | 967.7 | 209.2 | −78.4% | −1456.3405 to −60.6445 | yes: GAIN |
| response time (ms), 99th percentile | 1380 | 307.4 | −77.7% | −2064.2315 to −80.1891 | yes: GAIN |
| time over the response line (% of samples) | 10.53 | 0.1385 | −98.7% | −21.0548 to +0.2782 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 0 | −100.0% | −10.6480 to −1.3520 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.91 | 1005 | +11180.0% | +711.8356 to +1280.4411 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05627 | 0.05954 | +5.8% | −0.0031 to +0.0096 | no |
| CPU used (cores), mean | 1.35 | 1.429 | +5.8% | −0.0745 to +0.2315 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.35 | 1.429 | +5.8% | −0.0745 to +0.2315 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.1 | 454.6 | −7.6% | −84.6072 to +9.5371 | no |
| HPA replicas, mean | 1.976 | 1.973 | −0.2% | −0.1544 to +0.1476 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 39.02 | 44.23 | +13.4% | +1.9320 to +8.5067 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.9 | 1410 | +84.6% | +565.7135 to +727.4865 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 134.9 | +269783.3% | +113.1984 to +156.5850 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 643 | +214233.3% | +512.7606 to +772.6394 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 70.12 | 754 | +975.4% | +555.3492 to +812.4925 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 7.7 | +7.700 (native is 0) | +1.4454 to +13.9546 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.234 | −29.4% | −2.6692 to −0.8637 | yes: GAIN |
| node-hours | 2.51 | 1.776 | −29.2% | −1.1119 to −0.3563 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 271.5 | +0.3% | −0.5059 to +2.2595 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 215.9 | −20.2% | −83.2616 to −26.0223 | yes: GAIN |
| response time (ms), mean | 280.4 | 263.6 | −6.0% | −28.7831 to −4.9658 | yes: GAIN |
| response time (ms), 95th percentile | 967.7 | 1080 | +11.6% | −3.7987 to +227.6757 | no |
| response time (ms), 99th percentile | 1380 | 1557 | +12.8% | +10.5082 to +343.7744 | yes: LOSS |
| time over the response line (% of samples) | 10.53 | 10.49 | −0.4% | −0.5045 to +0.4272 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6.3 | +5.0% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 184.9 | +184.900 (native is 0) | +104.4680 to +265.3320 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.91 | 10.06 | +13.0% | −0.4991 to +2.8091 | no |
| utilisation (used / allocatable) | 0.05627 | 0.08121 | +44.3% | +0.0124 to +0.0375 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.35 | 1.343 | −0.6% | −0.0617 to +0.0464 | no |
| Omni's own CPU (cores), mean | 0 | 0.07017 | +0.070 (native is 0) | +0.0619 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.35 | 1.413 | +4.6% | +0.0043 to +0.1207 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.1 | 383.9 | −22.0% | −163.4602 to −53.0174 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.068 | +4.7% | −0.1114 to +0.2953 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0.2 | 2.2 | +1000.0% | +0.0338 to +3.9662 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.517 | +658.3% | +0.0771 to +2.5562 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.02 | 41.83 | +7.2% | +2.0947 to +3.5247 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.9 | 772.3 | +1.1% | −0.4266 to +17.2266 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.288 | −45.2% | −4.0048 to −1.4202 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.09167 | +83.3% | −0.0716 to +0.1549 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.5263 to +0.7263 | no |
| queue: job turnaround, submitted to done, mean (s) | 70.12 | 78.4 | +11.8% | −1.5291 to +18.1041 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.234 | −29.4% | −2.6692 to −0.8637 | yes: GAIN |
| node-hours | 2.515 | 1.776 | −29.4% | −1.1236 to −0.3549 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.5 | −0.2% | −3.6215 to +2.6159 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 215.9 | −20.6% | −87.3097 to −24.7334 | yes: GAIN |
| response time (ms), mean | 121.7 | 263.6 | +116.6% | −14.1543 to +297.9511 | no |
| response time (ms), 95th percentile | 209.2 | 1080 | +416.0% | +62.1945 to +1678.6675 | yes: LOSS |
| response time (ms), 99th percentile | 307.4 | 1557 | +406.4% | +92.5107 to +2406.1925 | yes: LOSS |
| time over the response line (% of samples) | 0.1385 | 10.49 | +7471.0% | −0.1740 to +20.8734 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 6.3 | +6.300 (native is 0) | +1.4715 to +11.1285 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 184.9 | +184.900 (native is 0) | +104.4680 to +265.3320 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1005 | 10.06 | −99.0% | −1278.1830 to −711.7836 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05954 | 0.08121 | +36.4% | +0.0146 to +0.0288 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.343 | −6.0% | −0.2609 to +0.0885 | no |
| Omni's own CPU (cores), mean | 0 | 0.07017 | +0.070 (native is 0) | +0.0619 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.413 | −1.1% | −0.1957 to +0.1637 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.6 | 383.9 | −15.6% | −85.5908 to −55.8169 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.068 | +4.8% | −0.1159 to +0.3067 | no |
| pods started | 0.1 | 0.9 | +800.0% | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0.1 | 2.2 | +2100.0% | +0.2393 to +3.9607 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.517 | +1416.7% | +0.3165 to +2.5169 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.23 | 41.83 | −5.4% | −6.1302 to +1.3108 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1410 | 772.3 | −45.2% | −718.4405 to −557.9595 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 134.9 | 0.09167 | −99.9% | −156.5018 to −113.1982 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 643 | 0.4 | −99.9% | −772.1754 to −513.0246 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 754 | 78.4 | −89.6% | −798.6364 to −552.6303 | yes: GAIN |
| queue: jobs unfinished at the window's end | 7.7 | 0 | −100.0% | −13.9546 to −1.4454 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.993 | −0.1% | −0.0243 to +0.0094 | no |
| node-hours | 2.51 | 2.513 | +0.1% | −0.0044 to +0.0101 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.6 | 271.2 | +0.2% | −2.6076 to +3.8047 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.6 | 270.9 | +0.1% | −2.6644 to +3.3907 | no |
| response time (ms), mean | 280.4 | 124.8 | −55.5% | −301.4086 to −9.8732 | yes: GAIN |
| response time (ms), 95th percentile | 967.7 | 222.1 | −77.0% | −1441.9316 to −49.2304 | yes: GAIN |
| response time (ms), 99th percentile | 1380 | 326.5 | −76.3% | −2048.8583 to −57.3141 | yes: GAIN |
| time over the response line (% of samples) | 10.53 | 0.1164 | −98.9% | −21.0698 to +0.2490 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 0 | −100.0% | −10.6480 to −1.3520 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.8 | +35.800 (native is 0) | +19.2642 to +52.3358 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.91 | 1126 | +12533.4% | +903.1082 to +1330.3418 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05627 | 0.05733 | +1.9% | −0.0066 to +0.0087 | no |
| CPU used (cores), mean | 1.35 | 1.374 | +1.8% | −0.1590 to +0.2066 | no |
| Omni's own CPU (cores), mean | 0 | 0.06299 | +0.063 (native is 0) | +0.0559 to +0.0701 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.35 | 1.437 | +6.4% | −0.0902 to +0.2638 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.1 | 470.4 | −4.4% | −78.5721 to +35.2429 | no |
| HPA replicas, mean | 1.976 | 1.982 | +0.3% | −0.1127 to +0.1241 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.7778 to +1.5778 | no |
| pod start wait, mean (s) | 0.2 | 0.35 | +75.0% | −0.4820 to +0.7820 | no |
| host CPU busy, the real machine under kind (%) | 39.02 | 45.49 | +16.6% | +2.6485 to +10.2922 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 763.9 | 1481 | +93.9% | +651.5147 to +783.4853 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.781 | −3.6% | −2.9982 to +2.5607 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 157.5 | +314916.7% | +114.7964 to +200.1203 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 688.2 | +229300.0% | +511.7357 to +864.0643 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 70.12 | 816.8 | +1064.9% | +667.4266 to +825.8734 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.4 | +8.400 (native is 0) | +2.7656 to +14.0344 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*