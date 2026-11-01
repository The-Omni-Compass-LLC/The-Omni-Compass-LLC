# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 11.41 | 11.5 |
| node-hours | 5.027 | 5.036 | 4.785 | 4.821 |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 528.5 | 528.9 | 528.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 528.5 | 510.4 | 513.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 832.5 | 1040 | 866.1 | 1123 |
| response time (ms), 95th percentile | 3390 | 4564 | 3732 | 5022 |
| response time (ms), 99th percentile | 4408 | 6186 | 4926 | 6759 |
| time over the response line (% of samples) | 29.61 | 32.76 | 30.5 | 34.39 |
| failed requests (%) | 0 | 0.1022 | 0.007634 | 0.227 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.8 | 18 | 15.4 | 18 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 43.8 | 29.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.6 | 64.34 | 21.48 | 50.18 |
| utilisation (used / allocatable) | 0.03787 | 0.03709 | 0.04073 | 0.04 |
| CPU used (cores), mean | 1.818 | 1.78 | 1.84 | 1.84 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0126 | 0.01059 |
| CPU used with Omni's own (cores), mean | 1.818 | 1.78 | 1.853 | 1.851 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.5 | 720.5 | 666.6 | 674.6 |
| HPA replicas, mean | 3.968 | 4.124 | 4.305 | 4.473 |
| pods started | 0.1 | 0.3 | 0.9 | 0.7 |
| pod start wait, total (s) | 0.3 | 0.7 | 1.2 | 1.4 |
| pod start wait, mean (s) | 0.3 | 0.45 | 0.9 | 1.1 |
| host CPU busy, the real machine under kind (%) | 55.95 | 63.16 | 58.06 | 65.28 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 948.4 | 1089 | 982.4 | 1123 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 11.09 | 11.15 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 7.35 | 0.1125 | 14.08 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 33.8 | 0.8 | 129.6 |
| queue: job turnaround, submitted to done, mean (s) | 255.8 | 393.5 | 281.6 | 429 |
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
| worker nodes in service, mean | 12 | 11.5 | −4.1% | −1.4377 to +0.4439 | no |
| node-hours | 5.036 | 4.821 | −4.3% | −0.6131 to +0.1819 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.5 | 528.7 | +0.0% | −3.8549 to +4.1480 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.5 | 513.1 | −2.9% | −46.2141 to +15.3697 | no |
| response time (ms), mean | 1040 | 1123 | +8.0% | −9.7967 to +177.1642 | no |
| response time (ms), 95th percentile | 4564 | 5022 | +10.0% | −111.8103 to +1027.1943 | no |
| response time (ms), 99th percentile | 6186 | 6759 | +9.3% | −57.7931 to +1203.7685 | no |
| time over the response line (% of samples) | 32.76 | 34.39 | +5.0% | −0.6751 to +3.9203 | no |
| failed requests (%) | 0.1022 | 0.227 | +122.2% | −0.0575 to +0.3073 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18 | 18 | ±0.0% | −1.3060 to +1.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.6 | +29.600 (native is 0) | +27.0055 to +32.1945 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 64.34 | 50.18 | −22.0% | −67.7697 to +39.4297 | no |
| utilisation (used / allocatable) | 0.03709 | 0.04 | +7.8% | −0.0015 to +0.0073 | no |
| CPU used (cores), mean | 1.78 | 1.84 | +3.4% | −0.1301 to +0.2500 | no |
| Omni's own CPU (cores), mean | 0 | 0.01059 | +0.011 (native is 0) | +0.0093 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.78 | 1.851 | +4.0% | −0.1198 to +0.2609 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.5 | 674.6 | −6.4% | −122.4467 to +30.6031 | no |
| HPA replicas, mean | 4.124 | 4.473 | +8.5% | +0.0295 to +0.6692 | yes: power given |
| pods started | 0.3 | 0.7 | +133.3% | −0.5048 to +1.3048 | no |
| pod start wait, total (s) | 0.7 | 1.4 | +100.0% | −1.2676 to +2.6676 | no |
| pod start wait, mean (s) | 0.45 | 1.1 | +144.4% | −0.7611 to +2.0611 | no |
| host CPU busy, the real machine under kind (%) | 63.16 | 65.28 | +3.4% | +1.0099 to +3.2317 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1089 | 1123 | +3.1% | +12.6829 to +54.3171 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.15 | −7.1% | −2.3723 to +0.6711 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.35 | 14.08 | +91.6% | −2.4997 to +15.9663 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.8 | 129.6 | +283.4% | −12.7481 to +204.3481 | no |
| queue: job turnaround, submitted to done, mean (s) | 393.5 | 429 | +9.0% | +7.0352 to +63.9565 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.027 | 5.036 | +0.2% | −0.0056 to +0.0236 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 528.5 | +0.1% | −2.6752 to +3.8605 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 528.5 | +0.1% | −2.6752 to +3.8605 | no |
| response time (ms), mean | 832.5 | 1040 | +24.9% | +99.1116 to +315.0844 | yes: LOSS |
| response time (ms), 95th percentile | 3390 | 4564 | +34.6% | +437.0958 to +1911.2062 | yes: LOSS |
| response time (ms), 99th percentile | 4408 | 6186 | +40.3% | +1106.1429 to +2449.9257 | yes: LOSS |
| time over the response line (% of samples) | 29.61 | 32.76 | +10.6% | +1.1356 to +5.1620 | yes: LOSS |
| failed requests (%) | 0 | 0.1022 | +0.102 (native is 0) | −0.0404 to +0.2448 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.8 | 18 | +21.6% | +1.6996 to +4.7004 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.6 | 64.34 | +184.7% | −4.4852 to +87.9685 | no |
| utilisation (used / allocatable) | 0.03787 | 0.03709 | −2.1% | −0.0042 to +0.0027 | no |
| CPU used (cores), mean | 1.818 | 1.78 | −2.1% | −0.2028 to +0.1278 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.818 | 1.78 | −2.1% | −0.2028 to +0.1278 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.5 | 720.5 | +2.3% | −47.6361 to +79.5514 | no |
| HPA replicas, mean | 3.968 | 4.124 | +3.9% | +0.0567 to +0.2536 | yes: power given |
| pods started | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| pod start wait, total (s) | 0.3 | 0.7 | +133.3% | −1.0385 to +1.8385 | no |
| pod start wait, mean (s) | 0.3 | 0.45 | +50.0% | −0.8900 to +1.1900 | no |
| host CPU busy, the real machine under kind (%) | 55.95 | 63.16 | +12.9% | +5.8152 to +8.6145 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 948.4 | 1089 | +14.9% | +100.6073 to +181.1927 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 7.35 | +5780.0% | +0.3664 to +14.0836 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 33.8 | +3655.6% | −39.0100 to +104.8100 | no |
| queue: job turnaround, submitted to done, mean (s) | 255.8 | 393.5 | +53.9% | +99.1849 to +176.3401 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.41 | −4.9% | −1.8008 to +0.6210 | no |
| node-hours | 5.027 | 4.785 | −4.8% | −0.7484 to +0.2644 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 528.9 | +0.2% | −0.9364 to +2.9515 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 510.4 | −3.3% | −55.8041 to +20.6692 | no |
| response time (ms), mean | 832.5 | 866.1 | +4.0% | −16.7503 to +83.9570 | no |
| response time (ms), 95th percentile | 3390 | 3732 | +10.1% | +66.7644 to +616.8416 | yes: LOSS |
| response time (ms), 99th percentile | 4408 | 4926 | +11.8% | +75.4204 to +961.5486 | yes: LOSS |
| time over the response line (% of samples) | 29.61 | 30.5 | +3.0% | +0.0036 to +1.7727 | yes: LOSS |
| failed requests (%) | 0 | 0.007634 | +0.008 (native is 0) | −0.0096 to +0.0249 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.8 | 15.4 | +4.1% | +0.2306 to +0.9694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.800 (native is 0) | +20.1388 to +67.4612 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.6 | 21.48 | −5.0% | −9.7837 to +7.5337 | no |
| utilisation (used / allocatable) | 0.03787 | 0.04073 | +7.6% | −0.0018 to +0.0075 | no |
| CPU used (cores), mean | 1.818 | 1.84 | +1.2% | −0.0489 to +0.0940 | no |
| Omni's own CPU (cores), mean | 0 | 0.0126 | +0.013 (native is 0) | +0.0120 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.818 | 1.853 | +1.9% | −0.0363 to +0.1066 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.5 | 666.6 | −5.4% | −94.1616 to +18.2693 | no |
| HPA replicas, mean | 3.968 | 4.305 | +8.5% | −0.0330 to +0.7068 | no |
| pods started | 0.1 | 0.9 | +800.0% | +0.2358 to +1.3642 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.2 | +300.0% | −0.2410 to +2.0410 | no |
| pod start wait, mean (s) | 0.3 | 0.9 | +200.0% | −0.2396 to +1.4396 | no |
| host CPU busy, the real machine under kind (%) | 55.95 | 58.06 | +3.8% | +0.9462 to +3.2878 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 948.4 | 982.4 | +3.6% | +15.9103 to +52.0897 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.09 | −7.6% | −2.6994 to +0.8763 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 0.1125 | −10.0% | −0.0670 to +0.0420 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.8 | −11.1% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 255.8 | 281.6 | +10.1% | +9.9593 to +41.6574 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.41 | −4.9% | −1.8008 to +0.6210 | no |
| node-hours | 5.036 | 4.785 | −5.0% | −0.7569 to +0.2549 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 528.5 | 528.9 | +0.1% | −2.7765 to +3.6064 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 528.5 | 510.4 | −3.4% | −56.7433 to +20.4231 | no |
| response time (ms), mean | 1040 | 866.1 | −16.7% | −249.9151 to −97.0742 | yes: GAIN |
| response time (ms), 95th percentile | 4564 | 3732 | −18.2% | −1374.7783 to −289.9177 | yes: GAIN |
| response time (ms), 99th percentile | 6186 | 4926 | −20.4% | −1841.0557 to −678.0439 | yes: GAIN |
| time over the response line (% of samples) | 32.76 | 30.5 | −6.9% | −4.0551 to −0.4663 | yes: GAIN |
| failed requests (%) | 0.1022 | 0.007634 | −92.5% | −0.2213 to +0.0322 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18 | 15.4 | −14.4% | −4.2242 to −0.9758 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.8 | +43.800 (native is 0) | +20.1388 to +67.4612 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 64.34 | 21.48 | −66.6% | −85.2798 to −0.4535 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03709 | 0.04073 | +9.8% | −0.0015 to +0.0088 | no |
| CPU used (cores), mean | 1.78 | 1.84 | +3.4% | −0.0911 to +0.2112 | no |
| Omni's own CPU (cores), mean | 0 | 0.0126 | +0.013 (native is 0) | +0.0120 to +0.0132 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.78 | 1.853 | +4.1% | −0.0789 to +0.2241 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 720.5 | 666.6 | −7.5% | −127.6048 to +19.7973 | no |
| HPA replicas, mean | 4.124 | 4.305 | +4.4% | −0.1281 to +0.4916 | no |
| pods started | 0.3 | 0.9 | +200.0% | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0.7 | 1.2 | +71.4% | −0.7274 to +1.7274 | no |
| pod start wait, mean (s) | 0.45 | 0.9 | +100.0% | −0.1909 to +1.0909 | no |
| host CPU busy, the real machine under kind (%) | 63.16 | 58.06 | −8.1% | −5.4909 to −4.7048 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1089 | 982.4 | −9.8% | −132.7556 to −81.0444 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 11.09 | −7.6% | −2.6994 to +0.8763 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 7.35 | 0.1125 | −98.5% | −14.0987 to −0.3763 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 33.8 | 0.8 | −97.6% | −104.8843 to +38.8843 | no |
| queue: job turnaround, submitted to done, mean (s) | 393.5 | 281.6 | −28.4% | −138.8892 to −85.0191 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.5 | −4.1% | −1.4377 to +0.4439 | no |
| node-hours | 5.027 | 4.821 | −4.1% | −0.6046 to +0.1914 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.9 | 528.7 | +0.1% | −2.4329 to +3.9114 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.9 | 513.1 | −2.8% | −45.2357 to +15.5767 | no |
| response time (ms), mean | 832.5 | 1123 | +34.9% | +155.6098 to +425.9537 | yes: LOSS |
| response time (ms), 95th percentile | 3390 | 5022 | +48.1% | +950.0889 to +2313.5971 | yes: LOSS |
| response time (ms), 99th percentile | 4408 | 6759 | +53.3% | +1585.9596 to +3116.0844 | yes: LOSS |
| time over the response line (% of samples) | 29.61 | 34.39 | +16.1% | +2.4335 to +7.1092 | yes: LOSS |
| failed requests (%) | 0 | 0.227 | +0.227 (native is 0) | +0.0781 to +0.3760 | yes: LOSS |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.8 | 18 | +21.6% | +2.6358 to +3.7642 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.6 | +29.600 (native is 0) | +27.0055 to +32.1945 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.6 | 50.17 | +122.0% | +2.7635 to +52.3799 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03787 | 0.04 | +5.6% | −0.0016 to +0.0058 | no |
| CPU used (cores), mean | 1.818 | 1.84 | +1.2% | −0.1154 to +0.1604 | no |
| Omni's own CPU (cores), mean | 0 | 0.01059 | +0.011 (native is 0) | +0.0093 to +0.0119 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.818 | 1.851 | +1.8% | −0.1048 to +0.1709 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 704.5 | 674.6 | −4.3% | −90.9533 to +31.0250 | no |
| HPA replicas, mean | 3.968 | 4.473 | +12.7% | +0.1928 to +0.8162 | yes: power given |
| pods started | 0.1 | 0.7 | +600.0% | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0.3 | 1.4 | +366.7% | +0.1198 to +2.0802 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.1 | +266.7% | −0.2556 to +1.8556 | no |
| host CPU busy, the real machine under kind (%) | 55.95 | 65.28 | +16.7% | +7.0312 to +11.6401 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 948.4 | 1123 | +18.4% | +118.3405 to +230.4595 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 11.15 | −7.1% | −2.3723 to +0.6711 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.125 | 14.08 | +11166.7% | +4.8443 to +23.0724 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 129.6 | +14300.0% | +11.6666 to +245.7334 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 255.8 | 429 | +67.7% | +114.6162 to +231.9005 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*