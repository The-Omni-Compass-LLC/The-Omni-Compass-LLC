# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.332 | 4.066 |
| node-hours | 2.515 | 2.515 | 1.813 | 1.706 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271 | 270.8 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 271 | 218.3 | 210.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 282 | 265.7 | 272.6 | 241.3 |
| response time (ms), 95th percentile | 980.5 | 1077 | 1099 | 1122 |
| response time (ms), 99th percentile | 1381 | 1528 | 1619 | 1552 |
| time over the response line (% of samples) | 10.5 | 7.505 | 10.62 | 7.263 |
| failed requests (%) | 0.01093 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 4.6 | 6.1 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 168.9 | 138.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 22 | 77.38 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.032 | 9.335 | 10.36 | 10.31 |
| utilisation (used / allocatable) | 0.05692 | 0.05598 | 0.07835 | 0.08286 |
| CPU used (cores), mean | 1.366 | 1.344 | 1.328 | 1.328 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0716 | 0.07055 |
| CPU used with Omni's own (cores), mean | 1.366 | 1.344 | 1.4 | 1.398 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.5 | 499.2 | 400.7 | 382 |
| HPA replicas, mean | 1.984 | 1.999 | 2.211 | 2.112 |
| pods started | 0.2 | 0.3 | 1.3 | 0.4 |
| pod start wait, total (s) | 0.5 | 0.5 | 3.3 | 0.7 |
| pod start wait, mean (s) | 0.25 | 0.35 | 1.45 | 0.5 |
| host CPU busy, the real machine under kind (%) | 38.7 | 38.63 | 41.73 | 41.63 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 771.2 | 773 | 776.8 | 777.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.516 | 3.062 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.03333 | 0.05 | 0.1708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | 0.3 | 0.5 |
| queue: job turnaround, submitted to done, mean (s) | 75.52 | 79.44 | 81.56 | 83.83 |
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
| worker nodes in service, mean | 6 | 4.066 | −32.2% | −2.7823 to −1.0858 | yes: GAIN |
| node-hours | 2.515 | 1.706 | −32.1% | −1.1616 to −0.4550 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.5 | +0.2% | −0.4683 to +1.3818 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 210.6 | −22.3% | −87.0153 to −33.8129 | yes: GAIN |
| response time (ms), mean | 265.7 | 241.3 | −9.2% | −46.4323 to −2.3949 | yes: GAIN |
| response time (ms), 95th percentile | 1077 | 1122 | +4.2% | −29.9158 to +120.3248 | no |
| response time (ms), 99th percentile | 1528 | 1552 | +1.6% | −28.9267 to +76.6471 | no |
| time over the response line (% of samples) | 7.505 | 7.263 | −3.2% | −1.1428 to +0.6597 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 4.7 | +2.2% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.1 | +138.100 (native is 0) | +72.3406 to +203.8594 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.335 | 10.31 | +10.4% | −1.2733 to +3.2167 | no |
| utilisation (used / allocatable) | 0.05598 | 0.08286 | +48.0% | +0.0149 to +0.0388 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.344 | 1.328 | −1.2% | −0.0499 to +0.0181 | no |
| Omni's own CPU (cores), mean | 0 | 0.07055 | +0.071 (native is 0) | +0.0608 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.344 | 1.398 | +4.1% | +0.0127 to +0.0966 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.2 | 382 | −23.5% | −170.7638 to −63.4718 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.112 | +5.6% | −0.0532 to +0.2786 | no |
| pods started | 0.3 | 0.4 | +33.3% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.5 | 0.7 | +40.0% | −1.0526 to +1.4526 | no |
| pod start wait, mean (s) | 0.35 | 0.5 | +42.9% | −0.6768 to +0.9768 | no |
| host CPU busy, the real machine under kind (%) | 38.63 | 41.63 | +7.8% | +2.4594 to +3.5413 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773 | 777.4 | +0.6% | −1.4131 to +10.2131 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.062 | −49.0% | −4.0565 to −1.8194 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.1708 | +412.5% | −0.0463 to +0.3213 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.44 | 83.83 | +5.5% | −0.4934 to +9.2767 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.515 | −0.0% | −0.0038 to +0.0024 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271 | −0.1% | −0.9103 to +0.2693 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 271 | −0.1% | −0.9103 to +0.2693 | no |
| response time (ms), mean | 282 | 265.7 | −5.8% | −38.9698 to +6.2814 | no |
| response time (ms), 95th percentile | 980.5 | 1077 | +9.9% | −82.5821 to +275.9581 | no |
| response time (ms), 99th percentile | 1381 | 1528 | +10.6% | −96.0943 to +388.4615 | no |
| time over the response line (% of samples) | 10.5 | 7.505 | −28.5% | −5.6952 to −0.2997 | yes: GAIN |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 4.6 | −20.7% | −2.6226 to +0.2226 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.032 | 9.335 | +3.4% | −2.0221 to +2.6288 | no |
| utilisation (used / allocatable) | 0.05692 | 0.05598 | −1.6% | −0.0020 to +0.0001 | no |
| CPU used (cores), mean | 1.366 | 1.344 | −1.6% | −0.0483 to +0.0034 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.366 | 1.344 | −1.6% | −0.0483 to +0.0034 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.5 | 499.2 | +2.2% | +0.5148 to +20.9012 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.984 | 1.999 | +0.8% | −0.1120 to +0.1425 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.5 | 0.5 | ±0.0% | −1.4698 to +1.4698 | no |
| pod start wait, mean (s) | 0.25 | 0.35 | +40.0% | −0.7396 to +0.9396 | no |
| host CPU busy, the real machine under kind (%) | 38.7 | 38.63 | −0.2% | −0.4877 to +0.3591 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 771.2 | 773 | +0.2% | −1.8129 to +5.4129 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.03333 | ±0.0% | −0.0444 to +0.0444 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.52 | 79.44 | +5.2% | −0.7607 to +8.6024 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.332 | −27.8% | −2.5702 to −0.7663 | yes: GAIN |
| node-hours | 2.515 | 1.813 | −27.9% | −1.0762 to −0.3274 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 270.8 | −0.2% | −1.4247 to +0.2657 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 218.3 | −19.5% | −81.4615 to −24.5432 | yes: GAIN |
| response time (ms), mean | 282 | 272.6 | −3.4% | −25.9192 to +7.0200 | no |
| response time (ms), 95th percentile | 980.5 | 1099 | +12.0% | +21.0399 to +215.1751 | yes: LOSS |
| response time (ms), 99th percentile | 1381 | 1619 | +17.2% | −29.1835 to +503.8467 | no |
| time over the response line (% of samples) | 10.5 | 10.62 | +1.1% | −0.2374 to +0.4666 | no |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 6.1 | +5.2% | −0.7690 to +1.3690 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 168.9 | +168.900 (native is 0) | +86.7206 to +251.0794 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.032 | 10.36 | +14.7% | −0.0154 to +2.6721 | no |
| utilisation (used / allocatable) | 0.05692 | 0.07835 | +37.7% | +0.0091 to +0.0337 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.328 | −2.8% | −0.0930 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0 | 0.0716 | +0.072 (native is 0) | +0.0628 to +0.0804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.4 | +2.5% | −0.0278 to +0.0949 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.5 | 400.7 | −18.0% | −133.1062 to −42.3617 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 2.211 | +11.4% | +0.0166 to +0.4374 | yes: power given |
| pods started | 0.2 | 1.3 | +550.0% | −0.0410 to +2.2410 | no |
| pod start wait, total (s) | 0.5 | 3.3 | +560.0% | −0.4131 to +6.0131 | no |
| pod start wait, mean (s) | 0.25 | 1.45 | +480.0% | +0.1891 to +2.2109 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 38.7 | 41.73 | +7.8% | +2.5366 to +3.5235 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 771.2 | 776.8 | +0.7% | −1.7506 to +12.9506 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.516 | −41.4% | −3.6984 to −1.2691 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.05 | +50.0% | −0.0324 to +0.0657 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.3 | +50.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.52 | 81.56 | +8.0% | −1.5654 to +13.6488 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.332 | −27.8% | −2.5702 to −0.7663 | yes: GAIN |
| node-hours | 2.515 | 1.813 | −27.9% | −1.0750 to −0.3272 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 270.8 | −0.1% | −1.2031 to +0.6851 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 218.3 | −19.4% | −80.8757 to −24.4881 | yes: GAIN |
| response time (ms), mean | 265.7 | 272.6 | +2.6% | −21.6926 to +35.4819 | no |
| response time (ms), 95th percentile | 1077 | 1099 | +2.0% | −70.1221 to +112.9611 | no |
| response time (ms), 99th percentile | 1528 | 1619 | +6.0% | −31.0641 to +213.3601 | no |
| time over the response line (% of samples) | 7.505 | 10.62 | +41.5% | +0.4981 to +5.7260 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 6.1 | +32.6% | −0.3546 to +3.3546 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 168.9 | +168.900 (native is 0) | +86.7206 to +251.0794 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.335 | 10.36 | +11.0% | −0.9903 to +3.0403 | no |
| utilisation (used / allocatable) | 0.05598 | 0.07835 | +39.9% | +0.0092 to +0.0355 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.344 | 1.328 | −1.2% | −0.0643 to +0.0331 | no |
| Omni's own CPU (cores), mean | 0 | 0.0716 | +0.072 (native is 0) | +0.0628 to +0.0804 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.344 | 1.4 | +4.2% | +0.0005 to +0.1115 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.2 | 400.7 | −19.7% | −152.1573 to −44.7267 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.211 | +10.6% | +0.0262 to +0.3973 | yes: power given |
| pods started | 0.3 | 1.3 | +333.3% | −0.3488 to +2.3488 | no |
| pod start wait, total (s) | 0.5 | 3.3 | +560.0% | −0.5855 to +6.1855 | no |
| pod start wait, mean (s) | 0.35 | 1.45 | +314.3% | −0.0253 to +2.2253 | no |
| host CPU busy, the real machine under kind (%) | 38.63 | 41.73 | +8.0% | +2.5685 to +3.6202 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773 | 776.8 | +0.5% | −2.9085 to +10.5085 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.516 | −41.4% | −3.6984 to −1.2691 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.05 | +50.0% | −0.0042 to +0.0375 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.3 | +50.0% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.44 | 81.56 | +2.7% | −4.0480 to +8.2896 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.066 | −32.2% | −2.7823 to −1.0858 | yes: GAIN |
| node-hours | 2.515 | 1.706 | −32.2% | −1.1620 to −0.4559 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.5 | +0.1% | −0.5132 to +0.7858 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 210.6 | −22.4% | −87.4472 to −34.0219 | yes: GAIN |
| response time (ms), mean | 282 | 241.3 | −14.5% | −51.8505 to −29.6651 | yes: GAIN |
| response time (ms), 95th percentile | 980.5 | 1122 | +14.5% | −72.6909 to +356.4759 | no |
| response time (ms), 99th percentile | 1381 | 1552 | +12.3% | −102.8282 to +442.9158 | no |
| time over the response line (% of samples) | 10.5 | 7.263 | −30.8% | −6.2439 to −0.2342 | yes: GAIN |
| failed requests (%) | 0.01093 | 0 | −100.0% | −0.0357 to +0.0138 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.8 | 4.7 | −19.0% | −2.7329 to +0.5329 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.1 | +138.100 (native is 0) | +72.3406 to +203.8594 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.032 | 10.31 | +14.1% | −0.0638 to +2.6138 | no |
| utilisation (used / allocatable) | 0.05692 | 0.08286 | +45.6% | +0.0147 to +0.0372 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.366 | 1.328 | −2.8% | −0.0774 to +0.0008 | no |
| Omni's own CPU (cores), mean | 0 | 0.07055 | +0.071 (native is 0) | +0.0608 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.366 | 1.398 | +2.4% | −0.0149 to +0.0794 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.5 | 382 | −21.8% | −153.1995 to −59.6201 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.984 | 2.112 | +6.4% | −0.0851 to +0.3410 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.5 | 0.7 | +40.0% | −1.4101 to +1.8101 | no |
| pod start wait, mean (s) | 0.25 | 0.5 | +100.0% | −0.6618 to +1.1618 | no |
| host CPU busy, the real machine under kind (%) | 38.7 | 41.63 | +7.6% | +2.3408 to +3.5313 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 771.2 | 777.4 | +0.8% | −1.5247 to +13.9247 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.062 | −49.0% | −4.0565 to −1.8194 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.1708 | +412.5% | −0.0719 to +0.3469 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | −0.3786 to +0.9786 | no |
| queue: job turnaround, submitted to done, mean (s) | 75.52 | 83.83 | +11.0% | +0.0269 to +16.5981 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*