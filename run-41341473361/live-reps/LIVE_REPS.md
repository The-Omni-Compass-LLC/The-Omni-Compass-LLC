# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.65 | 7.093 |
| node-hours | 5.032 | 5.027 | 4.467 | 2.975 |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 504.6 | 526.9 | 505.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 504.6 | 484.2 | 350.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 646.7 | 124.1 | 639.2 | 72.52 |
| response time (ms), 95th percentile | 2601 | 171.8 | 2719 | 93.59 |
| response time (ms), 99th percentile | 3520 | 197.2 | 3773 | 123.2 |
| time over the response line (% of samples) | 23.76 | 0.007612 | 24.65 | 0 |
| failed requests (%) | 0 | 0 | 0.01389 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 0 | 12.9 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 57.7 | 26.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.93 | 0 | 21.16 | 0.05333 |
| utilisation (used / allocatable) | 0.03578 | 0.006037 | 0.04005 | 0.008827 |
| CPU used (cores), mean | 1.717 | 0.2898 | 1.675 | 0.2511 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01251 | 0.00932 |
| CPU used with Omni's own (cores), mean | 1.717 | 0.2898 | 1.688 | 0.2604 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.5 | 4240 | 691.4 | 3398 |
| HPA replicas, mean | 4.087 | 4.091 | 4.147 | 4.492 |
| pods started | 0 | 0.4 | 0.7 | 2.1 |
| pod start wait, total (s) | 0 | 0.6 | 1 | 2.9 |
| pod start wait, mean (s) | 0 | 0.5 | 0.75 | 1.333 |
| host CPU busy, the real machine under kind (%) | 51.91 | 14.62 | 53.72 | 15.8 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 884.9 | 1505 | 903.6 | 1507 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.804 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1158 | 0.075 | 1161 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1474 | 0.6 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 193.6 | 1158 | 206 | 1161 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.093 | −40.9% | −5.2117 to −4.6024 | yes: GAIN |
| node-hours | 5.027 | 2.975 | −40.8% | −2.1816 to −1.9232 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 505.2 | +0.1% | +0.4275 to +0.9145 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 350.9 | −30.5% | −163.4036 to −143.9627 | yes: GAIN |
| response time (ms), mean | 124.1 | 72.52 | −41.5% | −60.6252 to −42.4547 | yes: GAIN |
| response time (ms), 95th percentile | 171.8 | 93.59 | −45.5% | −90.2227 to −66.2083 | yes: GAIN |
| response time (ms), 99th percentile | 197.2 | 123.2 | −37.6% | −99.4004 to −48.7248 | yes: GAIN |
| time over the response line (% of samples) | 0.007612 | 0 | −100.0% | −0.0191 to +0.0039 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 | +26.800 (native is 0) | +25.4597 to +28.1403 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05333 | +0.053 (native is 0) | −0.0673 to +0.1740 | no |
| utilisation (used / allocatable) | 0.006037 | 0.008827 | +46.2% | +0.0025 to +0.0030 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2898 | 0.2511 | −13.3% | −0.0422 to −0.0351 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00932 | +0.009 (native is 0) | +0.0082 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2898 | 0.2604 | −10.1% | −0.0324 to −0.0263 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4240 | 3398 | −19.9% | −974.6636 to −710.3156 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.091 | 4.492 | +9.8% | +0.2757 to +0.5249 | yes: power given |
| pods started | 0.4 | 2.1 | +425.0% | +1.1111 to +2.2889 | yes: power given |
| pod start wait, total (s) | 0.6 | 2.9 | +383.3% | +1.2310 to +3.3690 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.333 | +166.7% | +0.2280 to +1.4386 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.62 | 15.8 | +8.1% | +0.9872 to +1.3706 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1507 | +0.2% | +1.1749 to +3.6251 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 1161 | +0.2% | +1.1411 to +3.5089 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 1477 | +0.2% | +0.9491 to +3.6509 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 1161 | +0.2% | +1.1411 to +3.5089 | yes: LOSS |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.032 | 5.027 | −0.1% | −0.0166 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 504.6 | −4.2% | −25.0847 to −19.6752 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 504.6 | −4.2% | −25.0847 to −19.6752 | yes: GAIN |
| response time (ms), mean | 646.7 | 124.1 | −80.8% | −818.3767 to −226.9929 | yes: GAIN |
| response time (ms), 95th percentile | 2601 | 171.8 | −93.4% | −3842.6744 to −1016.2716 | yes: GAIN |
| response time (ms), 99th percentile | 3520 | 197.2 | −94.4% | −5207.5642 to −1438.1794 | yes: GAIN |
| time over the response line (% of samples) | 23.76 | 0.007612 | −100.0% | −34.6992 to −12.8030 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 0 | −100.0% | −17.3236 to −7.4764 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.93 | 0 | −100.0% | −20.4788 to −7.3812 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03578 | 0.006037 | −83.1% | −0.0336 to −0.0259 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.717 | 0.2898 | −83.1% | −1.6139 to −1.2414 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.717 | 0.2898 | −83.1% | −1.6139 to −1.2414 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.5 | 4240 | +463.5% | +3098.6236 to +3876.6604 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.087 | 4.091 | +0.1% | −0.1304 to +0.1397 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| host CPU busy, the real machine under kind (%) | 51.91 | 14.62 | −71.8% | −42.5299 to −32.0531 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.9 | 1505 | +70.1% | +516.3000 to +723.5000 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1158 | +1111784.0% | +1156.0342 to +1160.1825 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1474 | +210528.6% | +1471.6754 to +1475.7246 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 193.6 | 1158 | +498.3% | +862.4948 to +1066.7719 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.65 | −11.3% | −2.9524 to +0.2430 | no |
| node-hours | 5.032 | 4.467 | −11.2% | −1.2379 to +0.1076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 526.9 | −0.0% | −1.4907 to +1.3823 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 484.2 | −8.1% | −93.0181 to +7.4847 | no |
| response time (ms), mean | 646.7 | 639.2 | −1.2% | −29.6331 to +14.4465 | no |
| response time (ms), 95th percentile | 2601 | 2719 | +4.5% | −5.6562 to +240.4292 | no |
| response time (ms), 99th percentile | 3520 | 3773 | +7.2% | −23.4392 to +529.2276 | no |
| time over the response line (% of samples) | 23.76 | 24.65 | +3.7% | +0.1829 to +1.5914 | yes: LOSS |
| failed requests (%) | 0 | 0.01389 | +0.014 (native is 0) | −0.0071 to +0.0349 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 12.9 | +4.0% | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.7 | +57.700 (native is 0) | +28.4490 to +86.9510 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.93 | 21.16 | +51.9% | −0.4056 to +14.8589 | no |
| utilisation (used / allocatable) | 0.03578 | 0.04005 | +11.9% | −0.0022 to +0.0108 | no |
| CPU used (cores), mean | 1.717 | 1.675 | −2.4% | −0.0930 to +0.0089 | no |
| Omni's own CPU (cores), mean | 0 | 0.01251 | +0.013 (native is 0) | +0.0113 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.717 | 1.688 | −1.7% | −0.0802 to +0.0211 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.5 | 691.4 | −8.1% | −154.6252 to +32.3832 | no |
| HPA replicas, mean | 4.087 | 4.147 | +1.5% | −0.1736 to +0.2940 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.1111 to +1.2889 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | +0.1740 to +1.8260 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.75 | +0.750 (native is 0) | +0.1363 to +1.3637 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.91 | 53.72 | +3.5% | +1.3114 to +2.3133 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.9 | 903.6 | +2.1% | +4.5978 to +32.8022 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.804 | −18.3% | −4.6636 to +0.2724 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.075 | −28.0% | −0.0855 to +0.0271 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 193.6 | 206 | +6.4% | +3.6252 to +21.2082 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.65 | −11.3% | −2.9524 to +0.2430 | no |
| node-hours | 5.027 | 4.467 | −11.1% | −1.2305 to +0.1108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 526.9 | +4.4% | +19.1614 to +25.4901 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 484.2 | −4.0% | −72.8750 to +32.1015 | no |
| response time (ms), mean | 124.1 | 639.2 | +415.2% | +204.1110 to +826.0719 | yes: LOSS |
| response time (ms), 95th percentile | 171.8 | 2719 | +1482.4% | +1066.2349 to +4027.4841 | yes: LOSS |
| response time (ms), 99th percentile | 197.2 | 3773 | +1812.9% | +1532.7605 to +5618.7715 | yes: LOSS |
| time over the response line (% of samples) | 0.007612 | 24.65 | +323684.6% | +13.3513 to +35.9252 | yes: LOSS |
| failed requests (%) | 0 | 0.01389 | +0.014 (native is 0) | −0.0071 to +0.0349 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 12.9 | +12.900 (native is 0) | +7.9505 to +17.8495 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.7 | +57.700 (native is 0) | +28.4490 to +86.9510 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 21.16 | +21.157 (native is 0) | +8.3790 to +33.9344 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006037 | 0.04005 | +563.4% | +0.0303 to +0.0377 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2898 | 1.675 | +478.2% | +1.2149 to +1.5562 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01251 | +0.013 (native is 0) | +0.0113 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2898 | 1.688 | +482.5% | +1.2275 to +1.5686 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4240 | 691.4 | −83.7% | −4019.5104 to −3078.0156 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.091 | 4.147 | +1.4% | −0.1692 to +0.2803 | no |
| pods started | 0.4 | 0.7 | +75.0% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 0.6 | 1 | +66.7% | −0.5656 to +1.3656 | no |
| pod start wait, mean (s) | 0.5 | 0.75 | +50.0% | −0.4502 to +0.9502 | no |
| host CPU busy, the real machine under kind (%) | 14.62 | 53.72 | +267.5% | +33.4499 to +44.7578 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 903.6 | −40.0% | −717.8615 to −484.5385 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1158 | 0.075 | −100.0% | −1160.2284 to −1156.0466 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1474 | 0.6 | −100.0% | −1475.9273 to −1471.6727 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1158 | 206 | −82.2% | −1062.0297 to −842.4036 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 7.093 | −40.9% | −5.2117 to −4.6024 | yes: GAIN |
| node-hours | 5.032 | 2.975 | −40.9% | −2.1884 to −1.9270 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 527 | 505.2 | −4.1% | −24.3592 to −19.0587 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527 | 350.9 | −33.4% | −184.0581 to −168.0681 | yes: GAIN |
| response time (ms), mean | 646.7 | 72.52 | −88.8% | −877.0418 to −271.4077 | yes: GAIN |
| response time (ms), 95th percentile | 2601 | 93.59 | −96.4% | −3926.7517 to −1088.6253 | yes: GAIN |
| response time (ms), 99th percentile | 3520 | 123.2 | −96.5% | −5289.4440 to −1504.4248 | yes: GAIN |
| time over the response line (% of samples) | 23.76 | 0 | −100.0% | −34.7117 to −12.8057 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.4 | 0 | −100.0% | −17.3236 to −7.4764 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 26.8 | +26.800 (native is 0) | +25.4597 to +28.1403 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.93 | 0.05333 | −99.6% | −20.4711 to −7.2822 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03578 | 0.008827 | −75.3% | −0.0307 to −0.0232 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.717 | 0.2511 | −85.4% | −1.6543 to −1.2783 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00932 | +0.009 (native is 0) | +0.0082 to +0.0104 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.717 | 0.2604 | −84.8% | −1.6439 to −1.2700 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 752.5 | 3398 | +351.5% | +2372.0390 to +2918.2658 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.087 | 4.492 | +9.9% | +0.2211 to +0.5887 | yes: power given |
| pods started | 0 | 2.1 | +2.100 (native is 0) | +1.6940 to +2.5060 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.900 (native is 0) | +1.9198 to +3.8802 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.333 | +1.333 (native is 0) | +1.0638 to +1.6029 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.91 | 15.8 | −69.6% | −41.2262 to −30.9989 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 884.9 | 1507 | +70.3% | +518.3267 to +726.2733 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 1161 | +1114016.0% | +1157.9507 to +1162.9160 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1477 | +210857.1% | +1473.3664 to +1478.6336 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 193.6 | 1161 | +499.5% | +864.4827 to +1069.4340 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*