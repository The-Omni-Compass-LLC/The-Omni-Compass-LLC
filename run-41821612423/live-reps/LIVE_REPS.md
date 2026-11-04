# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.812 | 5.973 |
| node-hours | 2.517 | 2.514 | 2.017 | 2.504 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 285.5 | 272.8 | 285.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 285.5 | 235.5 | 284.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 332.7 | 638.3 | 327.2 | 633.9 |
| response time (ms), 95th percentile | 1176 | 1315 | 1315 | 1341 |
| response time (ms), 99th percentile | 1667 | 1779 | 1897 | 1840 |
| time over the response line (% of samples) | 14.69 | 56.43 | 15.75 | 56.59 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 23.6 | 8.7 | 23.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 144.1 | 34.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.67 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 2 | 11.19 | 2.46 |
| utilisation (used / allocatable) | 0.06025 | 0.09518 | 0.07761 | 0.0952 |
| CPU used (cores), mean | 1.446 | 2.284 | 1.457 | 2.275 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07224 | 0.04205 |
| CPU used with Omni's own (cores), mean | 1.446 | 2.284 | 1.529 | 2.317 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 299.3 | 387 | 299.2 |
| HPA replicas, mean | 1.921 | 1.987 | 2.408 | 2.61 |
| pods started | 0 | 0.1 | 1.4 | 0.5 |
| pod start wait, total (s) | 0 | 0.1 | 2.7 | 1.4 |
| pod start wait, mean (s) | 0 | 0.1 | 1.1 | 0.7333 |
| host CPU busy, the real machine under kind (%) | 41.42 | 73.65 | 44.87 | 74.66 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 780.6 | 1427 | 791.4 | 1426 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.055 | 5.561 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 592.9 | 0.09583 | 590.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1025 | 0.5 | 1027 |
| queue: job turnaround, submitted to done, mean (s) | 86.83 | 907.4 | 95.32 | 898.6 |
| queue: jobs unfinished at the window's end | 0 | 12.8 | 0 | 12.9 |
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
| worker nodes in service, mean | 6 | 5.973 | −0.5% | −0.0693 to +0.0151 | no |
| node-hours | 2.514 | 2.504 | −0.4% | −0.0272 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 285.5 | 285.5 | +0.0% | −0.9055 to +0.9567 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.5 | 284.7 | −0.3% | −2.1162 to +0.4632 | no |
| response time (ms), mean | 638.3 | 633.9 | −0.7% | −40.3098 to +31.5378 | no |
| response time (ms), 95th percentile | 1315 | 1341 | +2.0% | −79.1564 to +131.1244 | no |
| response time (ms), 99th percentile | 1779 | 1840 | +3.5% | −117.3488 to +240.3432 | no |
| time over the response line (% of samples) | 56.43 | 56.59 | +0.3% | −3.8406 to +4.1616 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 23.6 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.6 | +34.600 (native is 0) | +29.3848 to +39.8152 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2 | 2.46 | +23.0% | −0.0113 to +0.9313 | no |
| utilisation (used / allocatable) | 0.09518 | 0.0952 | +0.0% | −0.0014 to +0.0014 | no |
| CPU used (cores), mean | 2.284 | 2.275 | −0.4% | −0.0354 to +0.0169 | no |
| Omni's own CPU (cores), mean | 0 | 0.04205 | +0.042 (native is 0) | +0.0364 to +0.0477 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.284 | 2.317 | +1.4% | +0.0061 to +0.0596 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.3 | 299.2 | −0.0% | −4.4393 to +4.1929 | no |
| HPA replicas, mean | 1.987 | 2.61 | +31.4% | +0.3671 to +0.8797 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.3689 to +1.1689 | no |
| pod start wait, total (s) | 0.1 | 1.4 | +1300.0% | −0.9882 to +3.5882 | no |
| pod start wait, mean (s) | 0.1 | 0.7333 | +633.3% | −0.3234 to +1.5901 | no |
| host CPU busy, the real machine under kind (%) | 73.65 | 74.66 | +1.4% | +0.0936 to +1.9161 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1427 | 1426 | −0.1% | −19.7092 to +16.5092 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.561 | −7.3% | −1.4181 to +0.5398 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 592.9 | 590.9 | −0.3% | −65.2984 to +61.3175 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1025 | 1027 | +0.2% | −34.1738 to +39.0302 | no |
| queue: job turnaround, submitted to done, mean (s) | 907.4 | 898.6 | −1.0% | −39.2603 to +21.6269 | no |
| queue: jobs unfinished at the window's end | 12.8 | 12.9 | +0.8% | −1.0898 to +1.2898 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.514 | −0.1% | −0.0088 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 285.5 | +4.7% | +10.1795 to +15.3401 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 285.5 | +4.7% | +10.1795 to +15.3401 | yes: power given |
| response time (ms), mean | 332.7 | 638.3 | +91.9% | +205.0985 to +406.1209 | yes: LOSS |
| response time (ms), 95th percentile | 1176 | 1315 | +11.8% | −453.5018 to +730.7238 | no |
| response time (ms), 99th percentile | 1667 | 1779 | +6.7% | −752.6273 to +975.8311 | no |
| time over the response line (% of samples) | 14.69 | 56.43 | +284.2% | +30.6055 to +52.8755 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 23.6 | +195.0% | +12.0442 to +19.1558 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 2 | −80.6% | −11.0487 to −5.5547 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06025 | 0.09518 | +58.0% | +0.0286 to +0.0412 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 2.284 | +58.0% | +0.6871 to +0.9895 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.446 | 2.284 | +58.0% | +0.6871 to +0.9895 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 299.3 | −34.7% | −199.7914 to −118.2446 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.921 | 1.987 | +3.4% | −0.0590 to +0.1910 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, mean (s) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| host CPU busy, the real machine under kind (%) | 41.42 | 73.65 | +77.8% | +29.0528 to +35.4188 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.6 | 1427 | +82.8% | +561.1673 to +732.0327 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 592.9 | +1016333.0% | +293.1228 to +892.5990 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1025 | +256138.5% | +607.2808 to +1441.8276 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 86.83 | 907.4 | +945.1% | +654.0361 to +987.0723 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.8 | +12.800 (native is 0) | +5.9324 to +19.6676 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.812 | −19.8% | −1.9985 to −0.3769 | yes: GAIN |
| node-hours | 2.517 | 2.017 | −19.9% | −0.8376 to −0.1626 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.8 | +0.0% | −0.8046 to +0.9092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 235.5 | −13.7% | −62.8844 to −11.6777 | yes: GAIN |
| response time (ms), mean | 332.7 | 327.2 | −1.6% | −29.9967 to +19.0820 | no |
| response time (ms), 95th percentile | 1176 | 1315 | +11.8% | −10.1237 to +287.0247 | no |
| response time (ms), 99th percentile | 1667 | 1897 | +13.8% | +25.7798 to +434.2470 | yes: LOSS |
| time over the response line (% of samples) | 14.69 | 15.75 | +7.3% | −0.8834 to +3.0145 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 8.7 | +8.7% | −0.0578 to +1.4578 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 144.1 | +144.100 (native is 0) | +67.9748 to +220.2252 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 11.19 | +8.6% | −0.0024 to +1.7824 | no |
| utilisation (used / allocatable) | 0.06025 | 0.07761 | +28.8% | +0.0056 to +0.0291 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.457 | +0.8% | −0.0325 to +0.0548 | no |
| Omni's own CPU (cores), mean | 0 | 0.07224 | +0.072 (native is 0) | +0.0661 to +0.0783 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.529 | +5.8% | +0.0355 to +0.1313 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 387 | −15.6% | −117.1659 to −25.5185 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.921 | 2.408 | +25.4% | +0.3049 to +0.6694 | yes: power given |
| pods started | 0 | 1.4 | +1.400 (native is 0) | +0.2715 to +2.5285 | yes: power given |
| pod start wait, total (s) | 0 | 2.7 | +2.700 (native is 0) | +0.1755 to +5.2245 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | +0.3690 to +1.8310 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.42 | 44.87 | +8.3% | +2.6651 to +4.2371 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.6 | 791.4 | +1.4% | +2.3444 to +19.2556 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.055 | −32.4% | −3.0757 to −0.8141 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.09583 | +64.3% | −0.0008 to +0.0758 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 86.83 | 95.32 | +9.8% | +0.8217 to +16.1617 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.812 | −19.8% | −1.9985 to −0.3769 | yes: GAIN |
| node-hours | 2.514 | 2.017 | −19.8% | −0.8343 to −0.1599 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 285.5 | 272.8 | −4.5% | −15.0146 to −10.4004 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.5 | 235.5 | −17.5% | −76.4681 to −23.6135 | yes: GAIN |
| response time (ms), mean | 638.3 | 327.2 | −48.7% | −411.1440 to −210.9900 | yes: GAIN |
| response time (ms), 95th percentile | 1315 | 1315 | −0.0% | −657.6290 to +657.3080 | no |
| response time (ms), 99th percentile | 1779 | 1897 | +6.7% | −860.5604 to +1097.3834 | no |
| time over the response line (% of samples) | 56.43 | 15.75 | −72.1% | −51.1167 to −30.2332 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 8.7 | −63.1% | −18.2796 to −11.5204 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 144.1 | +144.100 (native is 0) | +67.9748 to +220.2252 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2 | 11.19 | +459.6% | +6.1765 to +12.2068 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09518 | 0.07761 | −18.5% | −0.0292 to −0.0060 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.284 | 1.457 | −36.2% | −0.9934 to −0.6609 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07224 | +0.072 (native is 0) | +0.0661 to +0.0783 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.284 | 1.529 | −33.0% | −0.9255 to −0.5843 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 299.3 | 387 | +29.3% | +54.7756 to +120.5761 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.987 | 2.408 | +21.2% | +0.2365 to +0.6059 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.0819 to +2.5181 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.7 | +2600.0% | +0.0055 to +5.1945 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.1 | +1000.0% | +0.1570 to +1.8430 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 73.65 | 44.87 | −39.1% | −32.2639 to −25.3056 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1427 | 791.4 | −44.5% | −720.6435 to −550.9565 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.299 | −61.7% | −4.9863 to −2.4165 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 592.9 | 0.09583 | −100.0% | −892.5505 to −293.0963 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1025 | 0.5 | −100.0% | −1441.6696 to −607.2388 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 907.4 | 95.32 | −89.5% | −975.8057 to −648.3193 | yes: GAIN |
| queue: jobs unfinished at the window's end | 12.8 | 0 | −100.0% | −19.6676 to −5.9324 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.973 | −0.5% | −0.0693 to +0.0151 | no |
| node-hours | 2.517 | 2.504 | −0.5% | −0.0302 to +0.0045 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 285.5 | +4.7% | +10.6301 to +14.9406 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 284.7 | +4.4% | +9.4631 to +14.4035 | yes: power given |
| response time (ms), mean | 332.7 | 633.9 | +90.5% | +205.6435 to +396.8040 | yes: LOSS |
| response time (ms), 95th percentile | 1176 | 1341 | +14.0% | −450.4159 to +779.6059 | no |
| response time (ms), 99th percentile | 1667 | 1840 | +10.4% | −730.9252 to +1077.1234 | no |
| time over the response line (% of samples) | 14.69 | 56.59 | +285.3% | +33.6228 to +50.1793 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8 | 23.6 | +195.0% | +12.0602 to +19.1398 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.6 | +34.600 (native is 0) | +29.3848 to +39.8152 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 2.46 | −76.1% | −10.8116 to −4.8717 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06025 | 0.0952 | +58.0% | +0.0288 to +0.0411 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.446 | 2.275 | +57.3% | +0.6825 to +0.9756 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04205 | +0.042 (native is 0) | +0.0364 to +0.0477 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 2.317 | +60.2% | +0.7286 to +1.0136 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 299.2 | −34.7% | −200.4704 to −117.8121 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.921 | 2.61 | +35.9% | +0.4260 to +0.9527 | yes: power given |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.1952 to +1.1952 | no |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | −0.8418 to +3.6418 | no |
| pod start wait, mean (s) | 0 | 0.7333 | +0.733 (native is 0) | −0.1503 to +1.6169 | no |
| host CPU busy, the real machine under kind (%) | 41.42 | 74.66 | +80.3% | +30.1144 to +36.3668 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 780.6 | 1426 | +82.6% | +561.3957 to +728.6043 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.561 | −7.3% | −1.4181 to +0.5398 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 590.9 | +1012920.8% | +298.2582 to +883.4828 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1027 | +256745.6% | +607.1830 to +1446.7818 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 86.83 | 898.6 | +934.9% | +648.9857 to +974.4893 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.9 | +12.900 (native is 0) | +6.0187 to +19.7813 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*