# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.537 | 5.565 |
| node-hours | 2.517 | 2.517 | 2.319 | 2.334 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275 | 274.5 | 274.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 275 | 260 | 261.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 498.6 | 537.9 | 464.4 | 488 |
| response time (ms), 95th percentile | 1893 | 2165 | 1971 | 2121 |
| response time (ms), 99th percentile | 2706 | 3035 | 2797 | 2958 |
| time over the response line (% of samples) | 23.7 | 23.71 | 23.02 | 23.08 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.5 | 11.5 | 11.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 28.1 | 36.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.67 | 13.32 | 12.64 | 13.4 |
| utilisation (used / allocatable) | 0.06617 | 0.0664 | 0.07194 | 0.07198 |
| CPU used (cores), mean | 1.588 | 1.594 | 1.587 | 1.589 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01668 | 0.01707 |
| CPU used with Omni's own (cores), mean | 1.588 | 1.594 | 1.604 | 1.606 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.4 | 421.3 | 394.2 | 395.3 |
| HPA replicas, mean | 1.985 | 2.012 | 2.298 | 2.159 |
| pods started | 0.2 | 0 | 0.6 | 0.2 |
| pod start wait, total (s) | 0.5 | 0 | 0.7 | 0.3 |
| pod start wait, mean (s) | 0.5 | 0 | 0.7 | 0.3 |
| host CPU busy, the real machine under kind (%) | 45.23 | 46.28 | 46.25 | 47.15 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 833.3 | 847.2 | 836.7 | 849.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 5.154 | 5.296 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.3958 | 0.0875 | 0.3375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | 0.8 | 1 |
| queue: job turnaround, submitted to done, mean (s) | 139.7 | 149.8 | 140.8 | 153.5 |
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
| worker nodes in service, mean | 6 | 5.565 | −7.2% | −1.1191 to +0.2496 | no |
| node-hours | 2.517 | 2.334 | −7.3% | −0.4682 to +0.1014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.9 | −0.0% | −0.7913 to +0.5995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 261.2 | −5.0% | −35.1855 to +7.6354 | no |
| response time (ms), mean | 537.9 | 488 | −9.3% | −70.5519 to −29.1594 | yes: GAIN |
| response time (ms), 95th percentile | 2165 | 2121 | −2.0% | −163.3529 to +75.1459 | no |
| response time (ms), 99th percentile | 3035 | 2958 | −2.5% | −190.4611 to +36.2831 | no |
| time over the response line (% of samples) | 23.71 | 23.08 | −2.7% | −1.3585 to +0.0968 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 11.1 | −3.5% | −0.9001 to +0.1001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.4 | +36.400 (native is 0) | +11.8766 to +60.9234 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.32 | 13.4 | +0.6% | −2.3570 to +2.5237 | no |
| utilisation (used / allocatable) | 0.0664 | 0.07198 | +8.4% | −0.0035 to +0.0147 | no |
| CPU used (cores), mean | 1.594 | 1.589 | −0.3% | −0.0245 to +0.0144 | no |
| Omni's own CPU (cores), mean | 0 | 0.01707 | +0.017 (native is 0) | +0.0161 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.594 | 1.606 | +0.8% | −0.0076 to +0.0316 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.3 | 395.3 | −6.2% | −67.4686 to +15.4702 | no |
| HPA replicas, mean | 2.012 | 2.159 | +7.3% | −0.0929 to +0.3878 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 46.28 | 47.15 | +1.9% | +0.6091 to +1.1397 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.2 | 849.1 | +0.2% | −3.1405 to +6.9405 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.296 | −11.7% | −1.7783 to +0.3699 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3958 | 0.3375 | −14.7% | −0.2659 to +0.1492 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 1 | −23.1% | −0.9786 to +0.3786 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.8 | 153.5 | +2.5% | −2.9978 to +10.4228 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.517 | 2.517 | +0.0% | −0.0074 to +0.0080 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 275 | +0.0% | −0.8318 to +0.9799 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 275 | +0.0% | −0.8318 to +0.9799 | no |
| response time (ms), mean | 498.6 | 537.9 | +7.9% | +13.3700 to +65.0867 | yes: LOSS |
| response time (ms), 95th percentile | 1893 | 2165 | +14.4% | +117.7537 to +425.7613 | yes: LOSS |
| response time (ms), 99th percentile | 2706 | 3035 | +12.2% | +84.6072 to +574.1504 | yes: LOSS |
| time over the response line (% of samples) | 23.7 | 23.71 | +0.1% | −0.5576 to +0.5835 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.5 | +2.7% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.67 | 13.32 | +5.1% | −1.9063 to +3.2063 | no |
| utilisation (used / allocatable) | 0.06617 | 0.0664 | +0.3% | −0.0006 to +0.0010 | no |
| CPU used (cores), mean | 1.588 | 1.594 | +0.3% | −0.0143 to +0.0252 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.588 | 1.594 | +0.3% | −0.0143 to +0.0252 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.4 | 421.3 | −0.0% | −5.6246 to +5.4634 | no |
| HPA replicas, mean | 1.985 | 2.012 | +1.4% | −0.1377 to +0.1916 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| pod start wait, mean (s) | 0.5 | 0 | −100.0% | −1.2726 to +0.2726 | no |
| host CPU busy, the real machine under kind (%) | 45.23 | 46.28 | +2.3% | +0.7292 to +1.3662 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.3 | 847.2 | +1.7% | +6.3793 to +21.4207 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.3958 | +493.8% | +0.0647 to +0.5937 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.3 | +225.0% | +0.2737 to +1.5263 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 139.7 | 149.8 | +7.2% | +1.5136 to +18.7364 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.537 | −7.7% | −1.0748 to +0.1485 | no |
| node-hours | 2.517 | 2.319 | −7.9% | −0.4539 to +0.0581 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.5 | −0.1% | −1.2360 to +0.4210 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 260 | −5.4% | −34.2395 to +4.3620 | no |
| response time (ms), mean | 498.6 | 464.4 | −6.9% | −50.2202 to −18.1805 | yes: GAIN |
| response time (ms), 95th percentile | 1893 | 1971 | +4.1% | −22.0161 to +177.1621 | no |
| response time (ms), 99th percentile | 2706 | 2797 | +3.4% | −77.0362 to +258.9970 | no |
| time over the response line (% of samples) | 23.7 | 23.02 | −2.9% | −1.2775 to −0.0891 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.5 | +2.7% | −0.6567 to +1.2567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.1 | +28.100 (native is 0) | +12.0186 to +44.1814 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.67 | 12.64 | −0.2% | −1.4041 to +1.3441 | no |
| utilisation (used / allocatable) | 0.06617 | 0.07194 | +8.7% | −0.0018 to +0.0133 | no |
| CPU used (cores), mean | 1.588 | 1.587 | −0.0% | −0.0146 to +0.0131 | no |
| Omni's own CPU (cores), mean | 0 | 0.01668 | +0.017 (native is 0) | +0.0153 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.588 | 1.604 | +1.0% | +0.0018 to +0.0300 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.4 | 394.2 | −6.4% | −62.8471 to +8.5114 | no |
| HPA replicas, mean | 1.985 | 2.298 | +15.8% | +0.0643 to +0.5623 | yes: power given |
| pods started | 0.2 | 0.6 | +200.0% | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0.5 | 0.7 | +40.0% | −0.6121 to +1.0121 | no |
| pod start wait, mean (s) | 0.5 | 0.7 | +40.0% | −0.6121 to +1.0121 | no |
| host CPU busy, the real machine under kind (%) | 45.23 | 46.25 | +2.3% | +0.7709 to +1.2709 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.3 | 836.7 | +0.4% | −0.6492 to +7.4492 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.154 | −14.1% | −1.9167 to +0.2248 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.0875 | +31.2% | −0.0340 to +0.0757 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.8 | +100.0% | +0.0306 to +0.7694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 139.7 | 140.8 | +0.8% | −4.6088 to +6.9171 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.537 | −7.7% | −1.0748 to +0.1485 | no |
| node-hours | 2.517 | 2.319 | −7.9% | −0.4536 to +0.0571 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275 | 274.5 | −0.2% | −1.0632 to +0.1002 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275 | 260 | −5.5% | −34.1169 to +4.0914 | no |
| response time (ms), mean | 537.9 | 464.4 | −13.7% | −101.9372 to −44.9203 | yes: GAIN |
| response time (ms), 95th percentile | 2165 | 1971 | −9.0% | −340.7408 to −47.6282 | yes: GAIN |
| response time (ms), 99th percentile | 3035 | 2797 | −7.9% | −424.7235 to −52.0733 | yes: GAIN |
| time over the response line (% of samples) | 23.71 | 23.02 | −2.9% | −1.2516 to −0.1408 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.5 | 11.5 | ±0.0% | −0.5840 to +0.5840 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 28.1 | +28.100 (native is 0) | +12.0186 to +44.1814 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.32 | 12.64 | −5.1% | −2.8149 to +1.4549 | no |
| utilisation (used / allocatable) | 0.0664 | 0.07194 | +8.3% | −0.0024 to +0.0135 | no |
| CPU used (cores), mean | 1.594 | 1.587 | −0.4% | −0.0223 to +0.0098 | no |
| Omni's own CPU (cores), mean | 0 | 0.01668 | +0.017 (native is 0) | +0.0153 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.594 | 1.604 | +0.7% | −0.0052 to +0.0261 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.3 | 394.2 | −6.4% | −66.5799 to +12.4053 | no |
| HPA replicas, mean | 2.012 | 2.298 | +14.2% | +0.0515 to +0.5211 | yes: power given |
| pods started | 0 | 0.6 | +0.600 (native is 0) | +0.2306 to +0.9694 | yes: power given |
| pod start wait, total (s) | 0 | 0.7 | +0.700 (native is 0) | +0.2172 to +1.1828 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.7 | +0.700 (native is 0) | +0.2172 to +1.1828 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.28 | 46.25 | −0.1% | −0.3671 to +0.3135 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.2 | 836.7 | −1.2% | −17.5187 to −3.4813 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 5.154 | −14.1% | −1.9167 to +0.2248 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3958 | 0.0875 | −77.9% | −0.5367 to −0.0800 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.8 | −38.5% | −1.1952 to +0.1952 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.8 | 140.8 | −6.0% | −15.9124 to −2.0293 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.565 | −7.2% | −1.1191 to +0.2496 | no |
| node-hours | 2.517 | 2.334 | −7.3% | −0.4694 to +0.1033 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.9 | 274.9 | −0.0% | −0.9073 to +0.8636 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.9 | 261.2 | −5.0% | −35.4110 to +8.0090 | no |
| response time (ms), mean | 498.6 | 488 | −2.1% | −27.2713 to +6.0168 | no |
| response time (ms), 95th percentile | 1893 | 2121 | +12.0% | +68.7368 to +386.5712 | yes: LOSS |
| response time (ms), 99th percentile | 2706 | 2958 | +9.3% | +39.3435 to +465.2361 | yes: LOSS |
| time over the response line (% of samples) | 23.7 | 23.08 | −2.6% | −1.2917 to +0.0558 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 11.1 | −0.9% | −0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 36.4 | +36.400 (native is 0) | +11.8766 to +60.9234 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.67 | 13.4 | +5.8% | −1.3481 to +2.8147 | no |
| utilisation (used / allocatable) | 0.06617 | 0.07198 | +8.8% | −0.0028 to +0.0145 | no |
| CPU used (cores), mean | 1.588 | 1.589 | +0.0% | −0.0232 to +0.0240 | no |
| Omni's own CPU (cores), mean | 0 | 0.01707 | +0.017 (native is 0) | +0.0161 to +0.0180 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.588 | 1.606 | +1.1% | −0.0065 to +0.0414 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.4 | 395.3 | −6.2% | −63.6590 to +11.4995 | no |
| HPA replicas, mean | 1.985 | 2.159 | +8.8% | −0.0625 to +0.4114 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.5 | 0.3 | −40.0% | −1.2003 to +0.8003 | no |
| pod start wait, mean (s) | 0.5 | 0.3 | −40.0% | −1.2003 to +0.8003 | no |
| host CPU busy, the real machine under kind (%) | 45.23 | 47.15 | +4.2% | +1.5710 to +2.2731 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.3 | 849.1 | +1.9% | +8.4835 to +23.1165 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.296 | −11.7% | −1.7783 to +0.3699 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.3375 | +406.3% | +0.1174 to +0.4243 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1 | +150.0% | +0.2306 to +0.9694 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 139.7 | 153.5 | +9.9% | +6.8118 to +20.8632 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*