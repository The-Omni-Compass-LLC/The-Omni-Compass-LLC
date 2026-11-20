# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.26 | 6.679 |
| node-hours | 5.023 | 5.033 | 4.301 | 2.806 |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 505.1 | 525.7 | 506.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 505.1 | 471.1 | 338.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 562 | 117.3 | 663.7 | 70.27 |
| response time (ms), 95th percentile | 2186 | 160.9 | 2758 | 95.55 |
| response time (ms), 99th percentile | 2979 | 183.7 | 3608 | 125.8 |
| time over the response line (% of samples) | 20.04 | 0 | 25.2 | 0.00726 |
| failed requests (%) | 0 | 0 | 0.007463 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 0 | 13.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 161 | 33.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 44.44 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.83 | 0 | 32.7 | 0.05167 |
| utilisation (used / allocatable) | 0.03441 | 0.005991 | 0.04019 | 0.009063 |
| CPU used (cores), mean | 1.651 | 0.2876 | 1.625 | 0.2416 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05473 | 0.02994 |
| CPU used with Omni's own (cores), mean | 1.651 | 0.2876 | 1.68 | 0.2715 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.8 | 4288 | 694.3 | 3466 |
| HPA replicas, mean | 4.11 | 4.309 | 4.574 | 4.734 |
| pods started | 0.4 | 1.1 | 2.5 | 2.5 |
| pod start wait, total (s) | 1.1 | 2 | 6.4 | 4.1 |
| pod start wait, mean (s) | 0.8 | 0.9167 | 1.626 | 1.317 |
| host CPU busy, the real machine under kind (%) | 50.7 | 15.1 | 56.85 | 17.4 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 859.3 | 1508 | 911.3 | 1509 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.939 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1161 | 0.1292 | 1163 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1477 | 0.7 | 1479 |
| queue: job turnaround, submitted to done, mean (s) | 166.5 | 1161 | 218.5 | 1163 |
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
| worker nodes in service, mean | 12 | 6.679 | −44.3% | −6.2386 to −4.4027 | yes: GAIN |
| node-hours | 5.033 | 2.806 | −44.2% | −2.6132 to −1.8396 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 505.1 | 506.1 | +0.2% | −0.0107 to +2.0257 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.1 | 338.5 | −33.0% | −195.7319 to −137.5698 | yes: GAIN |
| response time (ms), mean | 117.3 | 70.27 | −40.1% | −57.9508 to −36.1509 | yes: GAIN |
| response time (ms), 95th percentile | 160.9 | 95.55 | −40.6% | −80.5903 to −50.0297 | yes: GAIN |
| response time (ms), 99th percentile | 183.7 | 125.8 | −31.6% | −67.9921 to −47.9381 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0.00726 | +0.007 (native is 0) | −0.0092 to +0.0237 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.300 (native is 0) | +29.4398 to +37.1602 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.05167 | +0.052 (native is 0) | −0.0263 to +0.1296 | no |
| utilisation (used / allocatable) | 0.005991 | 0.009063 | +51.3% | +0.0024 to +0.0038 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2876 | 0.2416 | −16.0% | −0.0625 to −0.0294 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02994 | +0.030 (native is 0) | +0.0255 to +0.0344 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2876 | 0.2715 | −5.6% | −0.0347 to +0.0026 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4288 | 3466 | −19.2% | −956.6510 to −687.5442 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.309 | 4.734 | +9.9% | +0.0610 to +0.7885 | yes: power given |
| pods started | 1.1 | 2.5 | +127.3% | −0.5429 to +3.3429 | no |
| pod start wait, total (s) | 2 | 4.1 | +105.0% | −1.8244 to +6.0244 | no |
| pod start wait, mean (s) | 0.9167 | 1.317 | +43.6% | −0.3523 to +1.1523 | no |
| host CPU busy, the real machine under kind (%) | 15.1 | 17.4 | +15.3% | +1.3230 to +3.2859 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 1509 | +0.1% | −1.3357 to +4.7357 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1161 | 1163 | +0.1% | −1.4389 to +4.4389 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1477 | 1479 | +0.1% | −1.5395 to +4.5395 | no |
| queue: job turnaround, submitted to done, mean (s) | 1161 | 1163 | +0.1% | −1.4389 to +4.4389 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.023 | 5.033 | +0.2% | −0.0067 to +0.0260 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 505.1 | −3.8% | −23.3882 to −16.3793 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 505.1 | −3.8% | −23.3882 to −16.3793 | yes: GAIN |
| response time (ms), mean | 562 | 117.3 | −79.1% | −765.4718 to −123.8087 | yes: GAIN |
| response time (ms), 95th percentile | 2186 | 160.9 | −92.6% | −3521.7065 to −527.7775 | yes: GAIN |
| response time (ms), 99th percentile | 2979 | 183.7 | −93.8% | −4817.3308 to −773.3362 | yes: GAIN |
| time over the response line (% of samples) | 20.04 | 0 | −100.0% | −31.5143 to −8.5639 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 0 | −100.0% | −16.3695 to −6.4305 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.83 | 0 | −100.0% | −26.8394 to −6.8173 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03441 | 0.005991 | −82.6% | −0.0319 to −0.0249 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.651 | 0.2876 | −82.6% | −1.5329 to −1.1950 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.651 | 0.2876 | −82.6% | −1.5329 to −1.1950 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.8 | 4288 | +451.3% | +3085.5466 to +3934.2301 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.11 | 4.309 | +4.8% | −0.0802 to +0.4781 | no |
| pods started | 0.4 | 1.1 | +175.0% | −0.5181 to +1.9181 | no |
| pod start wait, total (s) | 1.1 | 2 | +81.8% | −1.7433 to +3.5433 | no |
| pod start wait, mean (s) | 0.8 | 0.9167 | +14.6% | −1.2086 to +1.4419 | no |
| host CPU busy, the real machine under kind (%) | 50.7 | 15.1 | −70.2% | −40.7816 to −30.4131 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 859.3 | 1508 | +75.5% | +540.2205 to +756.5795 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1161 | +1466631.6% | +1158.6721 to +1163.4946 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1477 | +295360.0% | +1474.4204 to +1479.1796 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 166.5 | 1161 | +597.5% | +888.6222 to +1100.7528 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.26 | −14.5% | −3.2551 to −0.2249 | yes: GAIN |
| node-hours | 5.023 | 4.301 | −14.4% | −1.3603 to −0.0832 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 525.7 | +0.1% | −1.1892 to +2.4820 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 471.1 | −10.3% | −101.9622 to −5.8575 | yes: GAIN |
| response time (ms), mean | 562 | 663.7 | +18.1% | +29.7414 to +173.7385 | yes: LOSS |
| response time (ms), 95th percentile | 2186 | 2758 | +26.2% | +214.6017 to +930.7073 | yes: LOSS |
| response time (ms), 99th percentile | 2979 | 3608 | +21.1% | +241.7368 to +1015.4790 | yes: LOSS |
| time over the response line (% of samples) | 20.04 | 25.2 | +25.8% | +2.2674 to +8.0639 | yes: LOSS |
| failed requests (%) | 0 | 0.007463 | +0.007 (native is 0) | −0.0094 to +0.0243 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 13.1 | +14.9% | +0.1529 to +3.2471 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161 | +161.000 (native is 0) | +60.8950 to +261.1050 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.83 | 32.7 | +94.3% | −0.5936 to +32.3436 | no |
| utilisation (used / allocatable) | 0.03441 | 0.04019 | +16.8% | −0.0002 to +0.0118 | no |
| CPU used (cores), mean | 1.651 | 1.625 | −1.6% | −0.1254 to +0.0733 | no |
| Omni's own CPU (cores), mean | 0 | 0.05473 | +0.055 (native is 0) | +0.0484 to +0.0611 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.651 | 1.68 | +1.7% | −0.0685 to +0.1259 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.8 | 694.3 | −10.7% | −169.5622 to +2.5416 | no |
| HPA replicas, mean | 4.11 | 4.574 | +11.3% | −0.0448 to +0.9732 | no |
| pods started | 0.4 | 2.5 | +525.0% | +0.3333 to +3.8667 | yes: power given |
| pod start wait, total (s) | 1.1 | 6.4 | +481.8% | +0.6028 to +9.9972 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 1.626 | +103.3% | −0.2805 to +1.9329 | no |
| host CPU busy, the real machine under kind (%) | 50.7 | 56.85 | +12.1% | +4.8406 to +7.4708 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 859.3 | 911.3 | +6.1% | +23.1996 to +80.8004 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.939 | −25.5% | −5.4932 to −0.6291 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 0.1292 | +63.2% | −0.0375 to +0.1375 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 166.5 | 218.5 | +31.2% | +25.0397 to +78.9603 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.26 | −14.5% | −3.2551 to −0.2249 | yes: GAIN |
| node-hours | 5.033 | 4.301 | −14.5% | −1.3769 to −0.0860 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 505.1 | 525.7 | +4.1% | +16.7640 to +24.2961 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 505.1 | 471.1 | −6.7% | −84.9151 to +16.8627 | no |
| response time (ms), mean | 117.3 | 663.7 | +465.7% | +167.8451 to +924.9152 | yes: LOSS |
| response time (ms), 95th percentile | 160.9 | 2758 | +1614.7% | +843.2453 to +4351.5477 | yes: LOSS |
| response time (ms), 99th percentile | 183.7 | 3608 | +1863.6% | +1229.9090 to +5617.9738 | yes: LOSS |
| time over the response line (% of samples) | 0 | 25.2 | +25.205 (native is 0) | +13.5954 to +36.8140 | yes: LOSS |
| failed requests (%) | 0 | 0.007463 | +0.007 (native is 0) | −0.0094 to +0.0243 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 13.1 | +13.100 (native is 0) | +8.2433 to +17.9567 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 161 | +161.000 (native is 0) | +60.8950 to +261.1050 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 32.7 | +32.703 (native is 0) | +9.1289 to +56.2777 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005991 | 0.04019 | +570.9% | +0.0306 to +0.0378 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2876 | 1.625 | +465.3% | +1.1704 to +1.5054 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05473 | +0.055 (native is 0) | +0.0484 to +0.0611 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2876 | 1.68 | +484.3% | +1.2203 to +1.5649 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4288 | 694.3 | −83.8% | −4097.6421 to −3089.1554 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.309 | 4.574 | +6.2% | −0.0884 to +0.6189 | no |
| pods started | 1.1 | 2.5 | +127.3% | −0.5429 to +3.3429 | no |
| pod start wait, total (s) | 2 | 6.4 | +220.0% | −1.1735 to +9.9735 | no |
| pod start wait, mean (s) | 0.9167 | 1.626 | +77.4% | −0.5635 to +1.9825 | no |
| host CPU busy, the real machine under kind (%) | 15.1 | 56.85 | +276.5% | +35.6084 to +47.8977 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 911.3 | −39.6% | −729.6172 to −463.1828 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1161 | 0.1292 | −100.0% | −1163.4520 to −1158.6147 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1477 | 0.7 | −100.0% | −1479.0825 to −1474.1175 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1161 | 218.5 | −81.2% | −1071.0384 to −814.3366 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.679 | −44.3% | −6.2386 to −4.4027 | yes: GAIN |
| node-hours | 5.023 | 2.806 | −44.1% | −2.6047 to −1.8288 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525 | 506.1 | −3.6% | −21.9299 to −15.8225 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525 | 338.5 | −35.5% | −214.3784 to −158.6906 | yes: GAIN |
| response time (ms), mean | 562 | 70.27 | −87.5% | −821.1106 to −162.2716 | yes: GAIN |
| response time (ms), 95th percentile | 2186 | 95.55 | −95.6% | −3593.3847 to −586.7193 | yes: GAIN |
| response time (ms), 99th percentile | 2979 | 125.8 | −95.8% | −4879.1128 to −827.4844 | yes: GAIN |
| time over the response line (% of samples) | 20.04 | 0.00726 | −100.0% | −31.5011 to −8.5626 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.4 | 0 | −100.0% | −16.3695 to −6.4305 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.300 (native is 0) | +29.4398 to +37.1602 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.83 | 0.05167 | −99.7% | −26.8175 to −6.7358 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03441 | 0.009063 | −73.7% | −0.0287 to −0.0220 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.651 | 0.2416 | −85.4% | −1.5709 to −1.2489 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02994 | +0.030 (native is 0) | +0.0255 to +0.0344 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.651 | 0.2715 | −83.6% | −1.5367 to −1.2233 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 777.8 | 3466 | +345.6% | +2264.3122 to +3111.2694 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.11 | 4.734 | +15.2% | +0.1615 to +1.0859 | yes: power given |
| pods started | 0.4 | 2.5 | +525.0% | +0.9102 to +3.2898 | yes: power given |
| pod start wait, total (s) | 1.1 | 4.1 | +272.7% | +0.6156 to +5.3844 | yes: LOSS |
| pod start wait, mean (s) | 0.8 | 1.317 | +64.6% | −0.4909 to +1.5243 | no |
| host CPU busy, the real machine under kind (%) | 50.7 | 17.4 | −65.7% | −37.5967 to −28.9891 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 859.3 | 1509 | +75.7% | +542.1250 to +758.0750 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07917 | 1163 | +1468526.3% | +1160.2625 to +1164.9041 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 1479 | +295660.0% | +1475.8907 to +1480.7093 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 166.5 | 1163 | +598.4% | +890.3069 to +1102.0681 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*