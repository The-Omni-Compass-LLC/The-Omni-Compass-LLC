# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.15 | 10.84 |
| node-hours | 5.031 | 5.032 | 4.259 | 4.544 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 525.8 | 527.4 | 526.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 525.8 | 469.3 | 490.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 642.6 | 911.8 | 770.9 | 1068 |
| response time (ms), 95th percentile | 2608 | 3332 | 3333 | 3764 |
| response time (ms), 99th percentile | 3457 | 4495 | 4424 | 4885 |
| time over the response line (% of samples) | 23.58 | 30.92 | 25.95 | 35.73 |
| failed requests (%) | 0.01408 | 0.07929 | 0.02992 | 0.009302 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 12.9 | 12.6 | 15.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 112.2 | 89.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 26 | 26.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.77 | 43.41 | 20.82 | 63.75 |
| utilisation (used / allocatable) | 0.03495 | 0.03426 | 0.04225 | 0.03885 |
| CPU used (cores), mean | 1.677 | 1.644 | 1.711 | 1.684 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05523 | 0.05558 |
| CPU used with Omni's own (cores), mean | 1.677 | 1.644 | 1.766 | 1.74 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.3 | 794.4 | 670.5 | 709.8 |
| HPA replicas, mean | 4.125 | 4.086 | 4.772 | 4.888 |
| pods started | 0 | 0.2 | 2.5 | 3.2 |
| pod start wait, total (s) | 0 | 0.6 | 7.2 | 8.5 |
| pod start wait, mean (s) | 0 | 0.3 | 1.788 | 1.74 |
| host CPU busy, the real machine under kind (%) | 51.19 | 57.4 | 57.1 | 63.71 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 891.9 | 997.2 | 944 | 1060 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.077 | 10.24 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 8.287 | 0.1042 | 16.92 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 71.3 | 0.6 | 90 |
| queue: job turnaround, submitted to done, mean (s) | 197.6 | 282.6 | 243.7 | 341.1 |
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
| worker nodes in service, mean | 12 | 10.84 | −9.6% | −2.5732 to +0.2593 | no |
| node-hours | 5.032 | 4.544 | −9.7% | −1.0839 to +0.1081 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 526.7 | +0.2% | −3.2990 to +4.9789 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 490.2 | −6.8% | −80.6177 to +9.4143 | no |
| response time (ms), mean | 911.8 | 1068 | +17.1% | +67.5537 to +244.7239 | yes: LOSS |
| response time (ms), 95th percentile | 3332 | 3764 | +13.0% | −23.6957 to +888.0997 | no |
| response time (ms), 99th percentile | 4495 | 4885 | +8.7% | −151.0820 to +931.5756 | no |
| time over the response line (% of samples) | 30.92 | 35.73 | +15.5% | +2.2360 to +7.3779 | yes: LOSS |
| failed requests (%) | 0.07929 | 0.009302 | −88.3% | −0.1896 to +0.0496 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 15.2 | +17.8% | +0.0367 to +4.5633 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +20.3179 to +158.8821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 43.41 | 63.75 | +46.9% | −35.2136 to +75.9036 | no |
| utilisation (used / allocatable) | 0.03426 | 0.03885 | +13.4% | −0.0013 to +0.0105 | no |
| CPU used (cores), mean | 1.644 | 1.684 | +2.4% | −0.1619 to +0.2418 | no |
| Omni's own CPU (cores), mean | 0 | 0.05558 | +0.056 (native is 0) | +0.0483 to +0.0629 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.644 | 1.74 | +5.8% | −0.1060 to +0.2971 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 794.4 | 709.8 | −10.7% | −197.4053 to +28.1904 | no |
| HPA replicas, mean | 4.086 | 4.888 | +19.6% | +0.1600 to +1.4443 | yes: power given |
| pods started | 0.2 | 3.2 | +1500.0% | +0.9768 to +5.0232 | yes: power given |
| pod start wait, total (s) | 0.6 | 8.5 | +1316.7% | +1.5695 to +14.2305 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.74 | +480.2% | +0.3356 to +2.5454 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.4 | 63.71 | +11.0% | +4.7420 to +7.8770 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 997.2 | 1060 | +6.3% | +34.6658 to +91.9342 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.24 | −14.7% | −3.7403 to +0.2156 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 8.287 | 16.92 | +104.2% | −7.7418 to +25.0085 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 71.3 | 90 | +26.2% | −86.5348 to +123.9348 | no |
| queue: job turnaround, submitted to done, mean (s) | 282.6 | 341.1 | +20.7% | +19.2854 to +97.7146 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.032 | +0.0% | −0.0127 to +0.0147 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 525.8 | −0.1% | −3.2622 to +2.1826 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 525.8 | −0.1% | −3.2622 to +2.1826 | no |
| response time (ms), mean | 642.6 | 911.8 | +41.9% | +97.2530 to +441.1288 | yes: LOSS |
| response time (ms), 95th percentile | 2608 | 3332 | +27.7% | +212.6099 to +1234.7471 | yes: LOSS |
| response time (ms), 99th percentile | 3457 | 4495 | +30.0% | +367.9545 to +1708.5049 | yes: LOSS |
| time over the response line (% of samples) | 23.58 | 30.92 | +31.1% | +2.8735 to +11.8080 | yes: LOSS |
| failed requests (%) | 0.01408 | 0.07929 | +462.9% | −0.0657 to +0.1961 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 12.9 | +13.2% | +0.5921 to +2.4079 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.77 | 43.41 | +175.3% | −8.8538 to +64.1338 | no |
| utilisation (used / allocatable) | 0.03495 | 0.03426 | −2.0% | −0.0033 to +0.0019 | no |
| CPU used (cores), mean | 1.677 | 1.644 | −2.0% | −0.1574 to +0.0910 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.677 | 1.644 | −2.0% | −0.1574 to +0.0910 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.3 | 794.4 | +1.9% | −36.4161 to +66.6082 | no |
| HPA replicas, mean | 4.125 | 4.086 | −0.9% | −0.2523 to +0.1746 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.7572 to +1.9572 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| host CPU busy, the real machine under kind (%) | 51.19 | 57.4 | +12.1% | +4.1194 to +8.2886 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 891.9 | 997.2 | +11.8% | +43.1336 to +167.4664 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 8.288 | +8940.9% | −0.5457 to +16.9373 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 71.3 | +10085.7% | −13.3539 to +154.5539 | no |
| queue: job turnaround, submitted to done, mean (s) | 197.6 | 282.6 | +43.1% | +32.0053 to +138.1280 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.15 | −15.4% | −3.6468 to −0.0466 | yes: GAIN |
| node-hours | 5.031 | 4.259 | −15.3% | −1.5225 to −0.0214 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 527.4 | +0.2% | −0.3374 to +2.4842 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 469.3 | −10.8% | −114.0186 to −0.1220 | yes: GAIN |
| response time (ms), mean | 642.6 | 770.9 | +20.0% | +28.0998 to +228.5126 | yes: LOSS |
| response time (ms), 95th percentile | 2608 | 3333 | +27.8% | +297.4713 to +1153.0197 | yes: LOSS |
| response time (ms), 99th percentile | 3457 | 4424 | +28.0% | +410.6060 to +1524.3810 | yes: LOSS |
| time over the response line (% of samples) | 23.58 | 25.95 | +10.0% | +0.8221 to +3.9165 | yes: LOSS |
| failed requests (%) | 0.01408 | 0.02992 | +112.4% | −0.0067 to +0.0384 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 12.6 | +10.5% | +0.4612 to +1.9388 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.2 | +112.200 (native is 0) | +32.5833 to +191.8167 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.77 | 20.82 | +32.1% | +2.6909 to +7.4191 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03495 | 0.04225 | +20.9% | +0.0018 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.677 | 1.711 | +2.0% | −0.0439 to +0.1101 | no |
| Omni's own CPU (cores), mean | 0 | 0.05523 | +0.055 (native is 0) | +0.0492 to +0.0613 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.677 | 1.766 | +5.3% | +0.0059 to +0.1707 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.3 | 670.5 | −14.0% | −190.9770 to −26.6664 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.125 | 4.772 | +15.7% | +0.1442 to +1.1500 | yes: power given |
| pods started | 0 | 2.5 | +2.500 (native is 0) | +0.6150 to +4.3850 | yes: power given |
| pod start wait, total (s) | 0 | 7.2 | +7.200 (native is 0) | +0.7508 to +13.6492 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.788 | +1.788 (native is 0) | +0.8362 to +2.7400 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.19 | 57.1 | +11.5% | +4.2783 to +7.5366 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 891.9 | 944 | +5.8% | +18.2145 to +85.9855 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.077 | −24.4% | −5.4270 to −0.4183 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 0.1042 | +13.6% | −0.0488 to +0.0738 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 197.6 | 243.7 | +23.3% | +17.7970 to +74.4614 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.15 | −15.4% | −3.6468 to −0.0466 | yes: GAIN |
| node-hours | 5.032 | 4.259 | −15.4% | −1.5317 to −0.0141 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.8 | 527.4 | +0.3% | −1.2445 to +4.4709 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.8 | 469.3 | −10.8% | −114.5486 to +1.4875 | no |
| response time (ms), mean | 911.8 | 770.9 | −15.5% | −228.0444 to −53.7249 | yes: GAIN |
| response time (ms), 95th percentile | 3332 | 3333 | +0.0% | −294.9189 to +298.0529 | no |
| response time (ms), 99th percentile | 4495 | 4424 | −1.6% | −315.3382 to +173.8658 | no |
| time over the response line (% of samples) | 30.92 | 25.95 | −16.1% | −8.6954 to −1.2475 | yes: GAIN |
| failed requests (%) | 0.07929 | 0.02992 | −62.3% | −0.1656 to +0.0669 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.9 | 12.6 | −2.3% | −1.1953 to +0.5953 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112.2 | +112.200 (native is 0) | +32.5833 to +191.8167 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 43.41 | 20.82 | −52.0% | −57.5233 to +12.3533 | no |
| utilisation (used / allocatable) | 0.03426 | 0.04225 | +23.3% | +0.0024 to +0.0135 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.644 | 1.711 | +4.0% | −0.0831 to +0.2156 | no |
| Omni's own CPU (cores), mean | 0 | 0.05523 | +0.055 (native is 0) | +0.0492 to +0.0613 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.644 | 1.766 | +7.4% | −0.0324 to +0.2753 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 794.4 | 670.5 | −15.6% | −209.4020 to −38.4334 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.086 | 4.772 | +16.8% | +0.2262 to +1.1458 | yes: power given |
| pods started | 0.2 | 2.5 | +1150.0% | +0.3324 to +4.2676 | yes: power given |
| pod start wait, total (s) | 0.6 | 7.2 | +1100.0% | −0.1541 to +13.3541 | no |
| pod start wait, mean (s) | 0.3 | 1.788 | +496.0% | +0.3504 to +2.6258 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 57.4 | 57.1 | −0.5% | −1.2311 to +0.6381 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 997.2 | 944 | −5.3% | −86.7692 to −19.6308 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.077 | −24.4% | −5.4270 to −0.4183 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 8.287 | 0.1042 | −98.7% | −16.9178 to +0.5511 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 71.3 | 0.6 | −99.2% | −154.7303 to +13.3303 | no |
| queue: job turnaround, submitted to done, mean (s) | 282.6 | 243.7 | −13.8% | −70.3057 to −7.5693 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.84 | −9.6% | −2.5732 to +0.2593 | no |
| node-hours | 5.031 | 4.544 | −9.7% | −1.0757 to +0.1019 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526.7 | +0.1% | −2.6265 to +3.2269 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 490.2 | −6.9% | −80.3759 to +8.0929 | no |
| response time (ms), mean | 642.6 | 1068 | +66.2% | +184.5849 to +666.0744 | yes: LOSS |
| response time (ms), 95th percentile | 2608 | 3764 | +44.3% | +613.5316 to +1698.2294 | yes: LOSS |
| response time (ms), 99th percentile | 3457 | 4885 | +41.3% | +769.7944 to +2087.1586 | yes: LOSS |
| time over the response line (% of samples) | 23.58 | 35.73 | +51.5% | +6.3534 to +17.9421 | yes: LOSS |
| failed requests (%) | 0.01408 | 0.009302 | −34.0% | −0.0449 to +0.0353 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 15.2 | +33.3% | +1.5940 to +6.0060 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +20.3179 to +158.8821 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.77 | 63.75 | +304.4% | −2.6707 to +98.6407 | no |
| utilisation (used / allocatable) | 0.03495 | 0.03885 | +11.2% | −0.0015 to +0.0093 | no |
| CPU used (cores), mean | 1.677 | 1.684 | +0.4% | −0.1476 to +0.1611 | no |
| Omni's own CPU (cores), mean | 0 | 0.05558 | +0.056 (native is 0) | +0.0483 to +0.0629 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.677 | 1.74 | +3.7% | −0.0901 to +0.2147 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 779.3 | 709.8 | −8.9% | −173.8481 to +34.8252 | no |
| HPA replicas, mean | 4.125 | 4.888 | +18.5% | +0.1614 to +1.3652 | yes: power given |
| pods started | 0 | 3.2 | +3.200 (native is 0) | +1.2396 to +5.1604 | yes: power given |
| pod start wait, total (s) | 0 | 8.5 | +8.500 (native is 0) | +2.4562 to +14.5438 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.74 | +1.740 (native is 0) | +0.8192 to +2.6618 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.19 | 63.71 | +24.4% | +9.5039 to +15.5230 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 891.9 | 1060 | +18.9% | +90.8018 to +246.3982 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.24 | −14.7% | −3.7403 to +0.2156 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09167 | 16.92 | +18359.1% | −1.0368 to +34.6951 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 90 | +12757.1% | +2.7140 to +175.8860 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 197.6 | 341.1 | +72.7% | +69.7281 to +217.4052 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*