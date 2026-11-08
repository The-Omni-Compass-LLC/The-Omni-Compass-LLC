# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.54 | 11.2 |
| node-hours | 5.028 | 5.027 | 4.411 | 4.696 |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526.7 | 526.3 | 528.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 526.7 | 480.4 | 503.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 638.2 | 807 | 732.8 | 999.1 |
| response time (ms), 95th percentile | 2543 | 3652 | 3136 | 4678 |
| response time (ms), 99th percentile | 3443 | 5132 | 4253 | 6209 |
| time over the response line (% of samples) | 24.56 | 26.56 | 27.36 | 33.09 |
| failed requests (%) | 0 | 0.05493 | 0 | 0.2344 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 16.3 | 14.1 | 18.11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 96.5 | 37.56 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 21.39 | 10.37 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.58 | 24.57 | 24.02 | 44.36 |
| utilisation (used / allocatable) | 0.03555 | 0.03615 | 0.0411 | 0.04023 |
| CPU used (cores), mean | 1.706 | 1.735 | 1.727 | 1.801 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0589 | 0.04818 |
| CPU used with Omni's own (cores), mean | 1.706 | 1.735 | 1.786 | 1.849 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.3 | 737.9 | 669.4 | 670.3 |
| HPA replicas, mean | 4.114 | 4.041 | 4.729 | 5.579 |
| pods started | 0.2 | 0.2 | 3.4 | 5.333 |
| pod start wait, total (s) | 0.4 | 0.3 | 8.9 | 16.89 |
| pod start wait, mean (s) | 0.2 | 0.3 | 2.208 | 2.843 |
| host CPU busy, the real machine under kind (%) | 52.41 | 58.73 | 58.77 | 66.4 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 881.3 | 985.5 | 929.6 | 1076 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 9.091 | 10.31 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1.896 | 0.1125 | 14.06 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.5 | 0.8 | 72.67 |
| queue: job turnaround, submitted to done, mean (s) | 189.9 | 294.6 | 233.9 | 381.7 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.2 | −6.6% | −1.9513 to +0.3611 | no |
| node-hours | 5.03 | 4.696 | −6.6% | −0.8192 to +0.1514 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 527.4 | 528.2 | +0.1% | −1.4018 to +2.8983 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 527.4 | 503.2 | −4.6% | −60.9595 to +12.3680 | no |
| response time (ms), mean | 878.4 | 999.1 | +13.7% | +41.4880 to +199.8960 | yes: LOSS |
| response time (ms), 95th percentile | 4005 | 4678 | +16.8% | +147.6856 to +1197.8833 | yes: LOSS |
| response time (ms), 99th percentile | 5613 | 6209 | +10.6% | +130.2984 to +1061.1658 | yes: LOSS |
| time over the response line (% of samples) | 29 | 33.09 | +14.1% | +2.0232 to +6.1514 | yes: LOSS |
| failed requests (%) | 0.06103 | 0.2344 | +284.1% | −0.1056 to +0.4524 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 17 | 18.11 | +6.5% | +0.6492 to +1.5730 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.56 | +37.556 (native is 0) | +33.5043 to +41.6068 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.47 | 44.36 | +67.6% | +5.0945 to +30.6870 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03688 | 0.04023 | +9.1% | −0.0004 to +0.0071 | no |
| CPU used (cores), mean | 1.77 | 1.801 | +1.8% | −0.0507 to +0.1130 | no |
| Omni's own CPU (cores), mean | 0 | 0.04818 | +0.048 (native is 0) | +0.0426 to +0.0537 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.77 | 1.849 | +4.5% | −0.0031 to +0.1617 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 722.3 | 670.3 | −7.2% | −107.2525 to +3.2343 | no |
| HPA replicas, mean | 4.082 | 5.579 | +36.7% | +0.6284 to +2.3659 | yes: power given |
| pods started | 0.2222 | 5.333 | +2300.0% | +2.6669 to +7.5553 | yes: power given |
| pod start wait, total (s) | 0.3333 | 16.89 | +4966.7% | +8.6220 to +24.4891 | yes: LOSS |
| pod start wait, mean (s) | 0.3333 | 2.843 | +753.0% | +1.6249 to +3.3948 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 60.06 | 66.4 | +10.6% | +5.0326 to +7.6599 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1010 | 1076 | +6.5% | +36.4990 to +94.3899 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.31 | −14.1% | −4.0117 to +0.6392 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 2.069 | 14.06 | +579.6% | −0.9282 to +24.9190 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.556 | 72.67 | +4571.4% | −36.0479 to +178.2701 | no |
| queue: job turnaround, submitted to done, mean (s) | 319.6 | 381.7 | +19.4% | +27.3225 to +96.9553 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.028 | 5.027 | −0.0% | −0.0163 to +0.0143 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526.7 | +0.1% | −1.2700 to +1.8426 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 526.7 | +0.1% | −1.2700 to +1.8426 | no |
| response time (ms), mean | 638.2 | 807 | +26.5% | +63.0500 to +274.6178 | yes: LOSS |
| response time (ms), 95th percentile | 2543 | 3652 | +43.6% | +516.2024 to +1701.9856 | yes: LOSS |
| response time (ms), 99th percentile | 3443 | 5132 | +49.1% | +967.7217 to +2410.4205 | yes: LOSS |
| time over the response line (% of samples) | 24.56 | 26.56 | +8.1% | −1.3303 to +5.3314 | no |
| failed requests (%) | 0 | 0.05493 | +0.055 (native is 0) | −0.0187 to +0.1286 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 16.3 | +37.0% | +2.2095 to +6.5905 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.58 | 24.57 | +57.8% | −0.2047 to +18.1980 | no |
| utilisation (used / allocatable) | 0.03555 | 0.03615 | +1.7% | −0.0005 to +0.0017 | no |
| CPU used (cores), mean | 1.706 | 1.735 | +1.7% | −0.0228 to +0.0804 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.706 | 1.735 | +1.7% | −0.0228 to +0.0804 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.3 | 737.9 | −1.8% | −33.3838 to +6.6429 | no |
| HPA replicas, mean | 4.114 | 4.041 | −1.8% | −0.3512 to +0.2050 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.4 | 0.3 | −25.0% | −1.1900 to +0.9900 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 52.41 | 58.73 | +12.1% | +4.8691 to +7.7639 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 881.3 | 985.5 | +11.8% | +57.2896 to +151.1104 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 1.896 | +2066.7% | −1.2695 to +4.8862 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1.5 | +114.3% | +0.4984 to +1.1016 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 189.9 | 294.6 | +55.1% | +57.8047 to +151.6036 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.54 | −12.2% | −2.7216 to −0.1993 | yes: GAIN |
| node-hours | 5.028 | 4.411 | −12.3% | −1.1493 to −0.0852 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.4 | 526.3 | −0.0% | −1.8971 to +1.5480 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.4 | 480.4 | −8.7% | −86.3457 to −5.6910 | yes: GAIN |
| response time (ms), mean | 638.2 | 732.8 | +14.8% | +31.9991 to +157.2362 | yes: LOSS |
| response time (ms), 95th percentile | 2543 | 3136 | +23.3% | +284.3923 to +901.2067 | yes: LOSS |
| response time (ms), 99th percentile | 3443 | 4253 | +23.5% | +395.3037 to +1224.1801 | yes: LOSS |
| time over the response line (% of samples) | 24.56 | 27.36 | +11.4% | +0.8506 to +4.7559 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.9 | 14.1 | +18.5% | +0.6996 to +3.7004 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.5 | +96.500 (native is 0) | +34.3371 to +158.6629 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.58 | 24.02 | +54.2% | −2.7944 to +19.6744 | no |
| utilisation (used / allocatable) | 0.03555 | 0.0411 | +15.6% | +0.0011 to +0.0100 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.706 | 1.727 | +1.2% | −0.0514 to +0.0926 | no |
| Omni's own CPU (cores), mean | 0 | 0.0589 | +0.059 (native is 0) | +0.0565 to +0.0613 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.706 | 1.786 | +4.7% | +0.0073 to +0.1517 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 751.3 | 669.4 | −10.9% | −149.3918 to −14.3423 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.114 | 4.729 | +15.0% | +0.2929 to +0.9381 | yes: power given |
| pods started | 0.2 | 3.4 | +1600.0% | +1.5550 to +4.8450 | yes: power given |
| pod start wait, total (s) | 0.4 | 8.9 | +2125.0% | +3.4168 to +13.5832 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.208 | +1004.2% | +1.1661 to +2.8506 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.41 | 58.77 | +12.1% | +5.4022 to +7.3061 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 881.3 | 929.6 | +5.5% | +22.3553 to +74.2447 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.091 | −24.2% | −5.0953 to −0.7219 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0875 | 0.1125 | +28.6% | −0.0038 to +0.0538 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.8 | +14.3% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 189.9 | 233.9 | +23.2% | +21.8115 to +66.2302 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.54 | −12.2% | −2.7216 to −0.1993 | yes: GAIN |
| node-hours | 5.027 | 4.411 | −12.3% | −1.1426 to −0.0899 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 526.7 | 526.3 | −0.1% | −1.6377 to +0.7159 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.7 | 480.4 | −8.8% | −86.2054 to −6.4040 | yes: GAIN |
| response time (ms), mean | 807 | 732.8 | −9.2% | −122.6305 to −25.8019 | yes: GAIN |
| response time (ms), 95th percentile | 3652 | 3136 | −14.1% | −854.9743 to −177.6147 | yes: GAIN |
| response time (ms), 99th percentile | 5132 | 4253 | −17.1% | −1331.1209 to −427.5375 | yes: GAIN |
| time over the response line (% of samples) | 26.56 | 27.36 | +3.0% | −1.4927 to +3.0981 | no |
| failed requests (%) | 0.05493 | 0 | −100.0% | −0.1286 to +0.0187 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 16.3 | 14.1 | −13.5% | −3.7004 to −0.6996 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.5 | +96.500 (native is 0) | +34.3371 to +158.6629 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.57 | 24.02 | −2.3% | −7.2328 to +6.1195 | no |
| utilisation (used / allocatable) | 0.03615 | 0.0411 | +13.7% | +0.0008 to +0.0091 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.735 | 1.727 | −0.5% | −0.0618 to +0.0453 | no |
| Omni's own CPU (cores), mean | 0 | 0.0589 | +0.059 (native is 0) | +0.0565 to +0.0613 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.735 | 1.786 | +2.9% | −0.0042 to +0.1055 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 737.9 | 669.4 | −9.3% | −126.8947 to −10.0984 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.041 | 4.729 | +17.0% | +0.4169 to +0.9603 | yes: power given |
| pods started | 0.2 | 3.4 | +1600.0% | +1.7379 to +4.6621 | yes: power given |
| pod start wait, total (s) | 0.3 | 8.9 | +2866.7% | +3.9252 to +13.2748 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.208 | +636.1% | +1.1646 to +2.6520 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 58.73 | 58.77 | +0.1% | −0.6469 to +0.7222 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 985.5 | 929.6 | −5.7% | −78.4507 to −33.3493 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 9.091 | −24.2% | −5.0953 to −0.7219 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.896 | 0.1125 | −94.1% | −4.8469 to +1.2802 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.8 | −46.7% | −1.0455 to −0.3545 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 294.6 | 233.9 | −20.6% | −87.6227 to −33.7440 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 9 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 11.2 | −6.6% | −1.9513 to +0.3611 | no |
| node-hours | 5.026 | 4.696 | −6.6% | −0.8113 to +0.1509 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 526.8 | 528.2 | +0.3% | −0.2295 to +3.0136 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 526.8 | 503.2 | −4.5% | −59.9434 to +12.6395 | no |
| response time (ms), mean | 696.6 | 999.1 | +43.4% | +148.0507 to +457.0188 | yes: LOSS |
| response time (ms), 95th percentile | 2802 | 4678 | +66.9% | +1122.0735 to +2629.5176 | yes: LOSS |
| response time (ms), 99th percentile | 3784 | 6209 | +64.1% | +1563.9655 to +3284.3369 | yes: LOSS |
| time over the response line (% of samples) | 27.28 | 33.09 | +21.3% | +1.4677 to +10.1527 | yes: LOSS |
| failed requests (%) | 0 | 0.2344 | +0.234 (native is 0) | −0.0706 to +0.5395 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.22 | 18.11 | +37.0% | +2.8755 to +6.9023 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.56 | +37.556 (native is 0) | +33.5043 to +41.6068 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.52 | 44.36 | +168.5% | +10.4196 to +45.2582 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0364 | 0.04023 | +10.5% | +0.0004 to +0.0073 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.747 | 1.801 | +3.1% | −0.0095 to +0.1176 | no |
| Omni's own CPU (cores), mean | 0 | 0.04818 | +0.048 (native is 0) | +0.0426 to +0.0537 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.747 | 1.849 | +5.9% | +0.0378 to +0.1667 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 731.5 | 670.3 | −8.4% | −114.5956 to −7.8215 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.188 | 5.579 | +33.2% | +0.3871 to +2.3956 | yes: power given |
| pods started | 0.2222 | 5.333 | +2300.0% | +2.5489 to +7.6733 | yes: power given |
| pod start wait, total (s) | 0.4444 | 16.89 | +3700.0% | +8.3177 to +24.5712 | yes: LOSS |
| pod start wait, mean (s) | 0.2222 | 2.843 | +1179.4% | +1.6741 to +3.5678 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 53.7 | 66.4 | +23.7% | +10.3204 to +15.0868 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 898.2 | 1076 | +19.8% | +108.0852 to +246.8037 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 10.31 | −14.1% | −4.0117 to +0.6392 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.09722 | 14.06 | +14366.7% | −1.4528 to +29.3880 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7778 | 72.67 | +9242.9% | −35.3666 to +179.1444 | no |
| queue: job turnaround, submitted to done, mean (s) | 207.3 | 381.7 | +84.1% | +105.8034 to +242.9188 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*