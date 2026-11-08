# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.65 | 6.152 |
| node-hours | 5.038 | 5.03 | 4.468 | 2.578 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 504.8 | 527 | 504.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 504.8 | 484.3 | 320.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 527.9 | 122.2 | 615.5 | 70.94 |
| response time (ms), 95th percentile | 2024 | 171.3 | 2508 | 92.03 |
| response time (ms), 99th percentile | 2783 | 198 | 3462 | 119.4 |
| time over the response line (% of samples) | 21.65 | 0 | 25.74 | 0 |
| failed requests (%) | 0 | 0 | 0.02587 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.11 | 0 | 14.22 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 109.9 | 32.89 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 24.15 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 0.05926 | 20.98 | 0.05926 |
| utilisation (used / allocatable) | 0.03449 | 0.005956 | 0.03933 | 0.00964 |
| CPU used (cores), mean | 1.656 | 0.2859 | 1.672 | 0.2374 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05562 | 0.03084 |
| CPU used with Omni's own (cores), mean | 1.656 | 0.2859 | 1.728 | 0.2682 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.2 | 4258 | 697.8 | 3277 |
| HPA replicas, mean | 3.961 | 4.148 | 4.859 | 4.444 |
| pods started | 0.1111 | 0.5556 | 3.444 | 1.667 |
| pod start wait, total (s) | 0.2222 | 0.8889 | 8.667 | 2.222 |
| pod start wait, mean (s) | 0.2222 | 0.6667 | 2.126 | 1.093 |
| host CPU busy, the real machine under kind (%) | 50.65 | 14.61 | 56.06 | 17.38 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 845.7 | 1506 | 888 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.292 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1160 | 0.1019 | 1160 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1476 | 0.5556 | 1476 |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 1160 | 194.2 | 1160 |
| queue: jobs unfinished at the window's end | 0 | 24 | 0 | 24 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.152 | −48.7% | −5.8816 to −5.8136 | yes: GAIN |
| node-hours | 5.03 | 2.578 | −48.7% | −2.4770 to −2.4270 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.8 | 504.7 | −0.0% | −1.8902 to +1.6945 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.8 | 320.9 | −36.4% | −186.1431 to −181.5803 | yes: GAIN |
| response time (ms), mean | 122.2 | 70.94 | −41.9% | −60.2468 to −42.2853 | yes: GAIN |
| response time (ms), 95th percentile | 171.3 | 92.03 | −46.3% | −91.7493 to −66.7274 | yes: GAIN |
| response time (ms), 99th percentile | 198 | 119.4 | −39.7% | −85.7739 to −71.4334 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.89 | +32.889 (native is 0) | +30.9502 to +34.8276 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05926 | 0.05926 | ±0.0% | −0.1025 to +0.1025 | no |
| utilisation (used / allocatable) | 0.005956 | 0.00964 | +61.9% | +0.0032 to +0.0041 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2859 | 0.2374 | −17.0% | −0.0525 to −0.0445 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03084 | +0.031 (native is 0) | +0.0276 to +0.0341 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2859 | 0.2682 | −6.2% | −0.0220 to −0.0133 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4258 | 3277 | −23.0% | −1044.2124 to −918.0433 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.148 | 4.444 | +7.1% | +0.0140 to +0.5788 | yes: power given |
| pods started | 0.5556 | 1.667 | +200.0% | +0.1354 to +2.0868 | yes: power given |
| pod start wait, total (s) | 0.8889 | 2.222 | +150.0% | +0.0586 to +2.6080 | yes: LOSS |
| pod start wait, mean (s) | 0.6667 | 1.093 | +63.9% | −0.0365 to +0.8883 | no |
| host CPU busy, the real machine under kind (%) | 14.61 | 17.38 | +18.9% | +2.2155 to +3.3186 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1507 | +0.0% | −4.9796 to +5.2018 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1160 | +0.0% | −5.0290 to +5.1308 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1476 | ±0.0% | −5.0988 to +5.0988 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1160 | +0.0% | −5.0290 to +5.1308 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.038 | 5.03 | −0.2% | −0.0210 to +0.0047 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 504.8 | −4.1% | −24.6995 to −18.7559 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 504.8 | −4.1% | −24.6995 to −18.7559 | yes: GAIN |
| response time (ms), mean | 527.9 | 122.2 | −76.8% | −700.7978 to −110.5734 | yes: GAIN |
| response time (ms), 95th percentile | 2024 | 171.3 | −91.5% | −3245.8288 to −459.1790 | yes: GAIN |
| response time (ms), 99th percentile | 2783 | 198 | −92.9% | −4465.3689 to −704.1933 | yes: GAIN |
| time over the response line (% of samples) | 21.65 | 0 | −100.0% | −31.8290 to −11.4702 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.11 | 0 | −100.0% | −16.2203 to −10.0019 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 0.05926 | −99.6% | −23.7116 to −4.3995 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03449 | 0.005956 | −82.7% | −0.0315 to −0.0256 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.656 | 0.2859 | −82.7% | −1.5107 to −1.2288 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.656 | 0.2859 | −82.7% | −1.5107 to −1.2288 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.2 | 4258 | +455.0% | +3180.8189 to +3800.5925 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.961 | 4.148 | +4.7% | −0.0491 to +0.4232 | no |
| pods started | 0.1111 | 0.5556 | +400.0% | −0.1140 to +1.0029 | no |
| pod start wait, total (s) | 0.2222 | 0.8889 | +300.0% | −0.4863 to +1.8197 | no |
| pod start wait, mean (s) | 0.2222 | 0.6667 | +200.0% | −0.3348 to +1.2237 | no |
| host CPU busy, the real machine under kind (%) | 50.65 | 14.61 | −71.2% | −40.6761 to −31.3974 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.7 | 1506 | +78.1% | +555.6117 to +765.9439 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1160 | +1391916.7% | +1156.7635 to +1163.0976 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1476 | +265640.0% | +1472.5673 to +1478.9882 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 1160 | +637.1% | +899.6824 to +1105.5861 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.65 | −11.3% | −2.5089 to −0.2010 | yes: GAIN |
| node-hours | 5.038 | 4.468 | −11.3% | −1.0553 to −0.0847 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 527 | +0.1% | −0.9890 to +1.8973 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 484.3 | −8.0% | −79.3074 to −5.1130 | yes: GAIN |
| response time (ms), mean | 527.9 | 615.5 | +16.6% | +1.8823 to +173.3551 | yes: LOSS |
| response time (ms), 95th percentile | 2024 | 2508 | +23.9% | +151.4637 to +816.6574 | yes: LOSS |
| response time (ms), 99th percentile | 2783 | 3462 | +24.4% | +142.4727 to +1216.0291 | yes: LOSS |
| time over the response line (% of samples) | 21.65 | 25.74 | +18.9% | +1.8673 to +6.3198 | yes: LOSS |
| failed requests (%) | 0 | 0.02587 | +0.026 (native is 0) | −0.0164 to +0.0681 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.11 | 14.22 | +8.5% | +0.3978 to +1.8244 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109.9 | +109.889 (native is 0) | +44.6830 to +175.0948 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 20.98 | +48.7% | +1.1905 to +12.5466 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03449 | 0.03933 | +14.0% | +0.0018 to +0.0079 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.656 | 1.672 | +1.0% | −0.0571 to +0.0898 | no |
| Omni's own CPU (cores), mean | 0 | 0.05562 | +0.056 (native is 0) | +0.0500 to +0.0612 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.656 | 1.728 | +4.3% | −0.0044 to +0.1483 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.2 | 697.8 | −9.1% | −109.5751 to −29.3210 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.961 | 4.859 | +22.7% | +0.5200 to +1.2760 | yes: power given |
| pods started | 0.1111 | 3.444 | +3000.0% | +1.5307 to +5.1360 | yes: power given |
| pod start wait, total (s) | 0.2222 | 8.667 | +3800.0% | +3.1452 to +13.7437 | yes: LOSS |
| pod start wait, mean (s) | 0.2222 | 2.126 | +856.5% | +0.6567 to +3.1501 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.65 | 56.06 | +10.7% | +3.5818 to +7.2381 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.7 | 888 | +5.0% | +9.9397 to +74.7270 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.292 | −22.6% | −4.9361 to −0.4805 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 0.1019 | +22.2% | −0.0416 to +0.0787 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 0.5556 | ±0.0% | −0.5435 to +0.5435 | no |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 194.2 | +23.4% | +11.8501 to +61.7888 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 9 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.65 | −11.3% | −2.5089 to −0.2010 | yes: GAIN |
| node-hours | 5.03 | 4.468 | −11.2% | −1.0520 to −0.0716 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.8 | 527 | +4.4% | +18.3949 to +25.9688 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.8 | 484.3 | −4.1% | −59.8121 to +18.8471 | no |
| response time (ms), mean | 122.2 | 615.5 | +403.7% | +114.8870 to +871.7216 | yes: LOSS |
| response time (ms), 95th percentile | 171.3 | 2508 | +1364.2% | +631.0663 to +4042.0626 | yes: LOSS |
| response time (ms), 99th percentile | 198 | 3462 | +1648.5% | +903.0206 to +5625.0434 | yes: LOSS |
| time over the response line (% of samples) | 0 | 25.74 | +25.743 (native is 0) | +15.1717 to +36.3146 | yes: LOSS |
| failed requests (%) | 0 | 0.02587 | +0.026 (native is 0) | −0.0164 to +0.0681 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14.22 | +14.222 (native is 0) | +11.1289 to +17.3155 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109.9 | +109.889 (native is 0) | +44.6830 to +175.0948 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.05926 | 20.98 | +35309.4% | +5.9080 to +35.9402 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005956 | 0.03933 | +560.3% | +0.0305 to +0.0362 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2859 | 1.672 | +484.8% | +1.1886 to +1.5835 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05562 | +0.056 (native is 0) | +0.0500 to +0.0612 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2859 | 1.728 | +504.3% | +1.2404 to +1.6430 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4258 | 697.8 | −83.6% | −3900.8008 to −3219.5068 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.148 | 4.859 | +17.1% | +0.3795 to +1.0424 | yes: power given |
| pods started | 0.5556 | 3.444 | +520.0% | +1.0280 to +4.7498 | yes: power given |
| pod start wait, total (s) | 0.8889 | 8.667 | +875.0% | +2.3591 to +13.1964 | yes: LOSS |
| pod start wait, mean (s) | 0.6667 | 2.126 | +218.8% | +0.2724 to +2.6456 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.61 | 56.06 | +283.7% | +35.1171 to +47.7762 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 888 | −41.1% | −755.1073 to −481.7816 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.1019 | −100.0% | −1163.1014 to −1156.7227 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.5556 | −100.0% | −1479.0790 to −1472.4766 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 194.2 | −83.3% | −1092.9915 to −838.6381 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.152 | −48.7% | −5.8816 to −5.8136 | yes: GAIN |
| node-hours | 5.038 | 2.578 | −48.8% | −2.4799 to −2.4405 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.5 | 504.7 | −4.1% | −24.1148 to −19.5363 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.5 | 320.9 | −39.0% | −207.5784 to −203.6004 | yes: GAIN |
| response time (ms), mean | 527.9 | 70.94 | −86.6% | −759.0869 to −154.8163 | yes: GAIN |
| response time (ms), 95th percentile | 2024 | 92.04 | −95.5% | −3330.2107 to −533.2738 | yes: GAIN |
| response time (ms), 99th percentile | 2783 | 119.4 | −95.7% | −4546.1540 to −780.6155 | yes: GAIN |
| time over the response line (% of samples) | 21.65 | 0 | −100.0% | −31.8290 to −11.4702 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.11 | 0 | −100.0% | −16.2203 to −10.0019 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.89 | +32.889 (native is 0) | +30.9502 to +34.8276 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 0.05926 | −99.6% | −23.6766 to −4.4345 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03449 | 0.00964 | −72.1% | −0.0275 to −0.0222 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.656 | 0.2374 | −85.7% | −1.5605 to −1.2760 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03084 | +0.031 (native is 0) | +0.0276 to +0.0341 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.656 | 0.2682 | −83.8% | −1.5269 to −1.2480 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 767.2 | 3277 | +327.1% | +2220.9806 to +2798.1750 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.961 | 4.444 | +12.2% | +0.2901 to +0.6767 | yes: power given |
| pods started | 0.1111 | 1.667 | +1400.0% | +0.6867 to +2.4244 | yes: power given |
| pod start wait, total (s) | 0.2222 | 2.222 | +900.0% | +0.9129 to +3.0871 | yes: LOSS |
| pod start wait, mean (s) | 0.2222 | 1.093 | +391.7% | +0.2210 to +1.5198 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 50.65 | 17.38 | −65.7% | −37.6393 to −28.9000 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.7 | 1507 | +78.2% | +557.7038 to +764.0739 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.08333 | 1160 | +1391977.8% | +1157.1874 to +1162.7756 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5556 | 1476 | +265640.0% | +1472.9857 to +1478.5699 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 157.4 | 1160 | +637.1% | +901.7303 to +1103.6401 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*