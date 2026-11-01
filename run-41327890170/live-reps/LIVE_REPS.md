# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.012 | 4.94 |
| node-hours | 2.515 | 2.516 | 2.1 | 2.068 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | 272.1 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | 241 | 238.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 349.4 | 328.7 | 316.8 | 280 |
| response time (ms), 95th percentile | 1272 | 1366 | 1309 | 1330 |
| response time (ms), 99th percentile | 1730 | 1977 | 1862 | 1923 |
| time over the response line (% of samples) | 13.96 | 10.21 | 13.52 | 9.904 |
| failed requests (%) | 0 | 0 | 0 | 0.01058 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 6.8 | 7.7 | 6.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 50 | 45.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.41 | 12.3 | 9.722 | 11.73 |
| utilisation (used / allocatable) | 0.05953 | 0.0584 | 0.07092 | 0.07256 |
| CPU used (cores), mean | 1.429 | 1.402 | 1.416 | 1.423 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01729 | 0.01612 |
| CPU used with Omni's own (cores), mean | 1.429 | 1.402 | 1.434 | 1.44 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 487.6 | 413 | 405.3 |
| HPA replicas, mean | 1.995 | 2.016 | 2.11 | 2.231 |
| pods started | 0.1 | 0.3 | 0.3 | 0.5 |
| pod start wait, total (s) | 0.2 | 0.4 | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.4 | 0.2 | 0.75 |
| host CPU busy, the real machine under kind (%) | 40.82 | 40.9 | 41.83 | 41.62 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 786.1 | 792 | 790.8 | 793.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.251 | 4.19 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1083 | 0.0625 | 0.1167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | 0.3 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 92.95 | 97.55 | 96.15 | 98.84 |
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
| worker nodes in service, mean | 6 | 4.94 | −17.7% | −1.8570 to −0.2628 | yes: GAIN |
| node-hours | 2.516 | 2.068 | −17.8% | −0.7782 to −0.1189 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | −0.0% | −1.0831 to +0.9779 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 238.8 | −12.2% | −57.6395 to −8.9949 | yes: GAIN |
| response time (ms), mean | 328.7 | 280 | −14.8% | −66.9969 to −30.4377 | yes: GAIN |
| response time (ms), 95th percentile | 1366 | 1330 | −2.7% | −74.7405 to +2.1885 | no |
| response time (ms), 99th percentile | 1977 | 1923 | −2.7% | −207.3462 to +99.5318 | no |
| time over the response line (% of samples) | 10.21 | 9.904 | −3.0% | −1.1499 to +0.5318 | no |
| failed requests (%) | 0 | 0.01058 | +0.011 (native is 0) | −0.0134 to +0.0345 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 6.6 | −2.9% | −1.2556 to +0.8556 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.8 | +45.800 (native is 0) | +27.7361 to +63.8639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.3 | 11.73 | −4.6% | −2.8854 to +1.7488 | no |
| utilisation (used / allocatable) | 0.0584 | 0.07256 | +24.2% | +0.0036 to +0.0247 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.402 | 1.423 | +1.5% | −0.0286 to +0.0720 | no |
| Omni's own CPU (cores), mean | 0 | 0.01612 | +0.016 (native is 0) | +0.0146 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.402 | 1.44 | +2.7% | −0.0120 to +0.0876 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.6 | 405.3 | −16.9% | −156.9188 to −7.6734 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.231 | +10.7% | −0.0272 to +0.4586 | no |
| pods started | 0.3 | 0.5 | +66.7% | −0.4573 to +0.8573 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | −0.5796 to +1.5796 | no |
| pod start wait, mean (s) | 0.4 | 0.75 | +87.5% | −0.5742 to +1.2742 | no |
| host CPU busy, the real machine under kind (%) | 40.9 | 41.62 | +1.8% | +0.2970 to +1.1475 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 792 | 793.1 | +0.1% | −5.5970 to +7.7970 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.19 | −30.2% | −3.1390 to −0.4813 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.1167 | +7.7% | −0.1816 to +0.1983 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.55 | 98.84 | +1.3% | −3.9226 to +6.5060 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.516 | +0.1% | −0.0014 to +0.0040 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −1.1088 to +0.7895 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 272.1 | −0.1% | −1.1088 to +0.7895 | no |
| response time (ms), mean | 349.4 | 328.7 | −5.9% | −47.7186 to +6.4275 | no |
| response time (ms), 95th percentile | 1272 | 1366 | +7.4% | −98.7524 to +287.1024 | no |
| response time (ms), 99th percentile | 1730 | 1977 | +14.3% | −50.8782 to +544.0336 | no |
| time over the response line (% of samples) | 13.96 | 10.21 | −26.8% | −7.0354 to −0.4602 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 6.8 | −9.3% | −1.2889 to −0.1111 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.41 | 12.3 | +18.1% | −0.6158 to +4.3892 | no |
| utilisation (used / allocatable) | 0.05953 | 0.0584 | −1.9% | −0.0031 to +0.0008 | no |
| CPU used (cores), mean | 1.429 | 1.402 | −1.9% | −0.0732 to +0.0194 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.429 | 1.402 | −1.9% | −0.0732 to +0.0194 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 487.6 | +3.6% | −15.8686 to +49.6073 | no |
| HPA replicas, mean | 1.995 | 2.016 | +1.0% | −0.1367 to +0.1772 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| host CPU busy, the real machine under kind (%) | 40.82 | 40.9 | +0.2% | −0.2948 to +0.4582 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.1 | 792 | +0.8% | −0.0221 to +11.8221 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1083 | +136.4% | −0.0602 to +0.1852 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.3372 to +0.3372 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.95 | 97.55 | +4.9% | −0.6397 to +9.8313 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.012 | −16.5% | −1.7218 to −0.2541 | yes: GAIN |
| node-hours | 2.515 | 2.1 | −16.5% | −0.7192 to −0.1115 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −0.7906 to +0.4185 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 241 | −11.5% | −53.8882 to −8.5880 | yes: GAIN |
| response time (ms), mean | 349.4 | 316.8 | −9.3% | −42.0846 to −22.9412 | yes: GAIN |
| response time (ms), 95th percentile | 1272 | 1309 | +2.9% | −63.5923 to +137.5853 | no |
| response time (ms), 99th percentile | 1730 | 1862 | +7.6% | +1.4710 to +262.6296 | yes: LOSS |
| time over the response line (% of samples) | 13.96 | 13.52 | −3.1% | −1.1243 to +0.2474 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 7.7 | +2.7% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50 | +50.000 (native is 0) | +24.0247 to +75.9753 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.41 | 9.722 | −6.6% | −2.0083 to +0.6317 | no |
| utilisation (used / allocatable) | 0.05953 | 0.07092 | +19.1% | +0.0023 to +0.0205 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.416 | −0.9% | −0.0354 to +0.0111 | no |
| Omni's own CPU (cores), mean | 0 | 0.01729 | +0.017 (native is 0) | +0.0156 to +0.0190 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.434 | +0.4% | −0.0187 to +0.0289 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 413 | −12.3% | −103.8727 to −11.5170 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.11 | +5.7% | −0.0214 to +0.2502 | no |
| pods started | 0.1 | 0.3 | +200.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| host CPU busy, the real machine under kind (%) | 40.82 | 41.83 | +2.5% | +0.6587 to +1.3574 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.1 | 790.8 | +0.6% | −0.2334 to +9.6334 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.251 | −29.2% | −2.9898 to −0.5083 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.0625 | +36.4% | −0.0344 to +0.0677 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.95 | 96.15 | +3.4% | −2.0082 to +8.4082 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.012 | −16.5% | −1.7218 to −0.2541 | yes: GAIN |
| node-hours | 2.516 | 2.1 | −16.6% | −0.7198 to −0.1136 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 272.1 | −0.0% | −1.1248 to +1.0720 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 241 | −11.4% | −53.3965 to −8.7604 | yes: GAIN |
| response time (ms), mean | 328.7 | 316.8 | −3.6% | −33.8156 to +10.0809 | no |
| response time (ms), 95th percentile | 1366 | 1309 | −4.2% | −207.9145 to +93.5575 | no |
| response time (ms), 99th percentile | 1977 | 1862 | −5.8% | −294.1912 to +65.1364 | no |
| time over the response line (% of samples) | 10.21 | 13.52 | +32.4% | +0.5678 to +6.0508 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.7 | +13.2% | −0.0204 to +1.8204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50 | +50.000 (native is 0) | +24.0247 to +75.9753 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.3 | 9.722 | −20.9% | −4.1116 to −1.0384 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0584 | 0.07092 | +21.4% | +0.0029 to +0.0221 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.402 | 1.416 | +1.1% | −0.0196 to +0.0491 | no |
| Omni's own CPU (cores), mean | 0 | 0.01729 | +0.017 (native is 0) | +0.0156 to +0.0190 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.402 | 1.434 | +2.3% | −0.0018 to +0.0659 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 487.6 | 413 | −15.3% | −141.3225 to −7.8060 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.016 | 2.11 | +4.7% | −0.1093 to +0.2975 | no |
| pods started | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.4 | 0.2 | −50.0% | −0.8573 to +0.4573 | no |
| pod start wait, mean (s) | 0.4 | 0.2 | −50.0% | −0.8573 to +0.4573 | no |
| host CPU busy, the real machine under kind (%) | 40.9 | 41.83 | +2.3% | +0.6827 to +1.1699 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 792 | 790.8 | −0.2% | −4.0968 to +1.6968 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.251 | −29.2% | −2.9898 to −0.5083 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.0625 | −42.3% | −0.2075 to +0.1159 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.3 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.55 | 96.15 | −1.4% | −2.8191 to +0.0275 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.94 | −17.7% | −1.8570 to −0.2628 | yes: GAIN |
| node-hours | 2.515 | 2.068 | −17.8% | −0.7777 to −0.1167 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −0.8067 to +0.3822 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 238.8 | −12.3% | −58.1341 to −8.8195 | yes: GAIN |
| response time (ms), mean | 349.4 | 280 | −19.9% | −99.9160 to −38.8097 | yes: GAIN |
| response time (ms), 95th percentile | 1272 | 1330 | +4.6% | −105.8189 to +221.6169 | no |
| response time (ms), 99th percentile | 1730 | 1923 | +11.1% | −57.0554 to +442.3964 | no |
| time over the response line (% of samples) | 13.96 | 9.904 | −29.1% | −7.3490 to −0.7647 | yes: GAIN |
| failed requests (%) | 0 | 0.01058 | +0.011 (native is 0) | −0.0134 to +0.0345 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.5 | 6.6 | −12.0% | −2.3086 to +0.5086 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 45.8 | +45.800 (native is 0) | +27.7361 to +63.8639 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.41 | 11.73 | +12.7% | −0.6075 to +3.2442 | no |
| utilisation (used / allocatable) | 0.05953 | 0.07256 | +21.9% | +0.0032 to +0.0229 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.429 | 1.423 | −0.4% | −0.0237 to +0.0132 | no |
| Omni's own CPU (cores), mean | 0 | 0.01612 | +0.016 (native is 0) | +0.0146 to +0.0176 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.429 | 1.44 | +0.8% | −0.0081 to +0.0299 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 405.3 | −13.9% | −117.1278 to −13.7256 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.995 | 2.231 | +11.8% | +0.1142 to +0.3577 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.3690 to +1.7690 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | −0.3804 to +1.4804 | no |
| host CPU busy, the real machine under kind (%) | 40.82 | 41.62 | +2.0% | +0.2341 to +1.3739 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.1 | 793.1 | +0.9% | +2.2792 to +11.7208 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.19 | −30.2% | −3.1390 to −0.4813 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1167 | +154.5% | −0.0344 to +0.1760 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.95 | 98.84 | +6.3% | +0.5572 to +11.2178 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*