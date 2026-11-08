# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.03 | 5.095 |
| node-hours | 2.51 | 2.511 | 2.107 | 2.134 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.3 | 274.6 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 274.3 | 244.1 | 245.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 505.6 | 509.8 | 526.9 | 530.7 |
| response time (ms), 95th percentile | 1996 | 2130 | 2065 | 2224 |
| response time (ms), 99th percentile | 2833 | 2963 | 2957 | 3159 |
| time over the response line (% of samples) | 21.67 | 20.46 | 22.58 | 21.43 |
| failed requests (%) | 0 | 0.01149 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.4 | 12.3 | 11.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 15.1 | 13.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 71.43 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.39 | 24.42 | 21.71 | 27.82 |
| utilisation (used / allocatable) | 0.06744 | 0.0671 | 0.08028 | 0.0773 |
| CPU used (cores), mean | 1.619 | 1.61 | 1.59 | 1.577 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06193 | 0.06807 |
| CPU used with Omni's own (cores), mean | 1.619 | 1.61 | 1.652 | 1.646 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.1 | 417.2 | 368 | 376.9 |
| HPA replicas, mean | 2.069 | 2.097 | 2.388 | 2.189 |
| pods started | 0 | 0 | 1.1 | 0.7 |
| pod start wait, total (s) | 0 | 0 | 2.3 | 1.1 |
| pod start wait, mean (s) | 0 | 0 | 1.533 | 0.6 |
| host CPU busy, the real machine under kind (%) | 46.33 | 47.04 | 48.24 | 49.4 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 847.5 | 854.7 | 852.8 | 861.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.35 | 4.31 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5917 | 0.4875 | 0.5292 | 0.3333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.9 | 3.3 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 151.9 | 161.7 | 158.3 | 168.5 |
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
| worker nodes in service, mean | 6 | 5.095 | −15.1% | −1.6179 to −0.1925 | yes: GAIN |
| node-hours | 2.511 | 2.134 | −15.0% | −0.6714 to −0.0811 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.4 | +0.0% | −0.8112 to +1.0027 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 245.9 | −10.3% | −50.8850 to −5.8569 | yes: GAIN |
| response time (ms), mean | 509.8 | 530.7 | +4.1% | −3.5492 to +45.3815 | no |
| response time (ms), 95th percentile | 2130 | 2224 | +4.4% | −2.4881 to +191.1401 | no |
| response time (ms), 99th percentile | 2963 | 3159 | +6.6% | +64.6821 to +327.0935 | yes: LOSS |
| time over the response line (% of samples) | 20.46 | 21.43 | +4.7% | −0.1642 to +2.1072 | no |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 11.8 | +3.5% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.8 | +13.800 (native is 0) | +9.4190 to +18.1810 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.42 | 27.82 | +13.9% | +1.4066 to +5.3801 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0671 | 0.0773 | +15.2% | +0.0029 to +0.0175 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.577 | −2.0% | −0.0864 to +0.0207 | no |
| Omni's own CPU (cores), mean | 0 | 0.06807 | +0.068 (native is 0) | +0.0594 to +0.0768 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.646 | +2.2% | −0.0254 to +0.0958 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.2 | 376.9 | −9.7% | −71.1020 to −9.5216 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.097 | 2.189 | +4.4% | −0.0326 to +0.2174 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.0410 to +2.2410 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | +0.0208 to +1.1792 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.04 | 49.4 | +5.0% | +1.6796 to +3.0393 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 854.7 | 861.3 | +0.8% | +0.3169 to +12.8831 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.31 | −28.2% | −2.8504 to −0.5305 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4875 | 0.3333 | −31.6% | −0.4623 to +0.1540 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 0.9 | −52.6% | −3.3117 to +1.3117 | no |
| queue: job turnaround, submitted to done, mean (s) | 161.7 | 168.5 | +4.2% | +2.4021 to +11.2646 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.511 | +0.0% | −0.0058 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.3 | −0.0% | −1.0549 to +0.9122 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 274.3 | −0.0% | −1.0549 to +0.9122 | no |
| response time (ms), mean | 505.6 | 509.8 | +0.8% | −12.0139 to +20.2597 | no |
| response time (ms), 95th percentile | 1996 | 2130 | +6.7% | −13.7503 to +282.0953 | no |
| response time (ms), 99th percentile | 2833 | 2963 | +4.6% | −67.4867 to +326.0615 | no |
| time over the response line (% of samples) | 21.67 | 20.46 | −5.6% | −3.1346 to +0.7032 | no |
| failed requests (%) | 0 | 0.01149 | +0.011 (native is 0) | −0.0145 to +0.0375 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.4 | −2.6% | −0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.39 | 24.42 | +40.4% | +2.3090 to +11.7510 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06744 | 0.0671 | −0.5% | −0.0016 to +0.0009 | no |
| CPU used (cores), mean | 1.619 | 1.61 | −0.5% | −0.0386 to +0.0218 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.619 | 1.61 | −0.5% | −0.0386 to +0.0218 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.1 | 417.2 | +0.7% | −7.6099 to +13.7922 | no |
| HPA replicas, mean | 2.069 | 2.097 | +1.3% | −0.1513 to +0.2066 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 46.33 | 47.04 | +1.5% | +0.3058 to +1.1153 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.5 | 854.7 | +0.8% | −2.5134 to +16.9134 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5917 | 0.4875 | −17.6% | −0.8303 to +0.6220 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.9 | +35.7% | −2.3860 to +3.3860 | no |
| queue: job turnaround, submitted to done, mean (s) | 151.9 | 161.7 | +6.4% | +2.0734 to +17.4433 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.03 | −16.2% | −1.7912 to −0.1498 | yes: GAIN |
| node-hours | 2.51 | 2.107 | −16.1% | −0.7487 to −0.0577 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 | +0.1% | −0.3602 to +0.9510 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 244.1 | −11.0% | −56.4292 to −4.0091 | yes: GAIN |
| response time (ms), mean | 505.6 | 526.9 | +4.2% | −3.0475 to +45.5822 | no |
| response time (ms), 95th percentile | 1996 | 2065 | +3.5% | −88.6019 to +228.1849 | no |
| response time (ms), 99th percentile | 2833 | 2957 | +4.3% | −142.9870 to +389.2894 | no |
| time over the response line (% of samples) | 21.67 | 22.58 | +4.2% | −0.2948 to +2.1197 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.3 | +5.1% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.1 | +15.100 (native is 0) | +9.6269 to +20.5731 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.39 | 21.71 | +24.8% | +1.3216 to +7.3117 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06744 | 0.08028 | +19.0% | +0.0015 to +0.0242 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.619 | 1.59 | −1.8% | −0.0622 to +0.0048 | no |
| Omni's own CPU (cores), mean | 0 | 0.06193 | +0.062 (native is 0) | +0.0542 to +0.0697 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.619 | 1.652 | +2.1% | −0.0068 to +0.0733 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.1 | 368 | −11.1% | −87.4180 to −4.7460 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.069 | 2.388 | +15.4% | +0.1150 to +0.5235 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3887 to +1.8113 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | +0.7166 to +3.8834 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.533 | +1.533 (native is 0) | +0.5668 to +2.4999 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.33 | 48.24 | +4.1% | +1.4423 to +2.3884 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.5 | 852.8 | +0.6% | +0.6149 to +9.9851 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.35 | −27.5% | −2.7947 to −0.5050 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5917 | 0.5292 | −10.6% | −0.5740 to +0.4490 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 3.3 | +135.7% | −1.0866 to +4.8866 | no |
| queue: job turnaround, submitted to done, mean (s) | 151.9 | 158.3 | +4.2% | +2.0949 to +10.7634 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.03 | −16.2% | −1.7912 to −0.1498 | yes: GAIN |
| node-hours | 2.511 | 2.107 | −16.1% | −0.7453 to −0.0627 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.6 | +0.1% | −0.5996 to +1.3332 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 244.1 | −11.0% | −55.7900 to −4.5056 | yes: GAIN |
| response time (ms), mean | 509.8 | 526.9 | +3.4% | −7.9186 to +42.2075 | no |
| response time (ms), 95th percentile | 2130 | 2065 | −3.0% | −202.4084 to +73.6464 | no |
| response time (ms), 99th percentile | 2963 | 2957 | −0.2% | −151.1360 to +138.8636 | no |
| time over the response line (% of samples) | 20.46 | 22.58 | +10.4% | +0.3832 to +3.8732 | yes: LOSS |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 12.3 | +7.9% | −0.0204 to +1.8204 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.1 | +15.100 (native is 0) | +9.6269 to +20.5731 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.42 | 21.71 | −11.1% | −6.0434 to +0.6167 | no |
| utilisation (used / allocatable) | 0.0671 | 0.08028 | +19.6% | +0.0016 to +0.0248 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.61 | 1.59 | −1.3% | −0.0580 to +0.0174 | no |
| Omni's own CPU (cores), mean | 0 | 0.06193 | +0.062 (native is 0) | +0.0542 to +0.0697 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.61 | 1.652 | +2.6% | −0.0010 to +0.0843 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.2 | 368 | −11.8% | −93.0251 to −5.3212 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.097 | 2.388 | +13.9% | +0.1348 to +0.4483 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.3887 to +1.8113 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | +0.7166 to +3.8834 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.533 | +1.533 (native is 0) | +0.5668 to +2.4999 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.04 | 48.24 | +2.6% | +0.5036 to +1.9060 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 854.7 | 852.8 | −0.2% | −11.3021 to +7.5021 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.35 | −27.5% | −2.7947 to −0.5050 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4875 | 0.5292 | +8.5% | −0.2322 to +0.3156 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.9 | 3.3 | +73.7% | −0.2927 to +3.0927 | no |
| queue: job turnaround, submitted to done, mean (s) | 161.7 | 158.3 | −2.1% | −10.9064 to +4.2481 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.095 | −15.1% | −1.6179 to −0.1925 | yes: GAIN |
| node-hours | 2.51 | 2.134 | −15.0% | −0.6751 to −0.0757 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 274.4 | +0.0% | −1.0923 to +1.1410 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 245.9 | −10.4% | −51.5837 to −5.3009 | yes: GAIN |
| response time (ms), mean | 505.6 | 530.7 | +5.0% | +4.3411 to +45.7370 | yes: LOSS |
| response time (ms), 95th percentile | 1996 | 2224 | +11.4% | +58.5102 to +398.4868 | yes: LOSS |
| response time (ms), 99th percentile | 2833 | 3159 | +11.5% | +24.2425 to +626.1079 | yes: LOSS |
| time over the response line (% of samples) | 21.67 | 21.43 | −1.1% | −1.4227 to +0.9343 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.8 | +0.9% | −0.5263 to +0.7263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.8 | +13.800 (native is 0) | +9.4190 to +18.1810 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.39 | 27.82 | +59.9% | +4.0600 to +16.7867 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06744 | 0.0773 | +14.6% | +0.0029 to +0.0168 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.619 | 1.577 | −2.5% | −0.0951 to +0.0127 | no |
| Omni's own CPU (cores), mean | 0 | 0.06807 | +0.068 (native is 0) | +0.0594 to +0.0768 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.619 | 1.646 | +1.7% | −0.0351 to +0.0888 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 414.1 | 376.9 | −9.0% | −64.8045 to −9.6367 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.069 | 2.189 | +5.8% | −0.0748 to +0.3149 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: power given |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.0410 to +2.2410 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | +0.0208 to +1.1792 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.33 | 49.4 | +6.6% | +2.5913 to +3.5487 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.5 | 861.3 | +1.6% | +6.4680 to +21.1320 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.31 | −28.2% | −2.8504 to −0.5305 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5917 | 0.3333 | −43.7% | −0.8271 to +0.3104 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 0.9 | −35.7% | −2.1259 to +1.1259 | no |
| queue: job turnaround, submitted to done, mean (s) | 151.9 | 168.5 | +10.9% | +6.9327 to +26.2506 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*