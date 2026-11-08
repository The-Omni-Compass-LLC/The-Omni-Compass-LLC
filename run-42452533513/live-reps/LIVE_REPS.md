# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.862 | 10.46 |
| node-hours | 5.031 | 5.03 | 4.138 | 4.379 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 525.6 | 525.8 | 526.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 525.6 | 458.6 | 478.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 482.7 | 703.3 | 538.9 | 809.9 |
| response time (ms), 95th percentile | 1828 | 2521 | 2234 | 3121 |
| response time (ms), 99th percentile | 2479 | 3317 | 2966 | 4248 |
| time over the response line (% of samples) | 18.65 | 27.06 | 22.09 | 34.18 |
| failed requests (%) | 0 | 0.01711 | 0 | 0.09411 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 13.2 | 11.9 | 15.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 124.9 | 68.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 35.68 | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 18.38 | 16.32 | 22.74 |
| utilisation (used / allocatable) | 0.03342 | 0.03427 | 0.04133 | 0.0416 |
| CPU used (cores), mean | 1.604 | 1.645 | 1.612 | 1.74 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05447 | 0.05391 |
| CPU used with Omni's own (cores), mean | 1.604 | 1.645 | 1.666 | 1.794 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.7 | 780.8 | 683.9 | 661.7 |
| HPA replicas, mean | 4.075 | 3.93 | 4.483 | 4.668 |
| pods started | 0.3 | 0.2 | 1.7 | 2.1 |
| pod start wait, total (s) | 0.5 | 0.5 | 3.7 | 6.3 |
| pod start wait, mean (s) | 0.3 | 0.5 | 1.367 | 2.323 |
| host CPU busy, the real machine under kind (%) | 49.1 | 54.65 | 54.29 | 61.41 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 835.7 | 919.6 | 865.8 | 1015 |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | 8.31 | 8.416 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 4.979 | 0.0875 | 22.02 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 38.3 | 0.6 | 138.3 |
| queue: job turnaround, submitted to done, mean (s) | 144.7 | 210.6 | 169.8 | 265.6 |
| queue: jobs unfinished at the window's end | 0 | 0 | 0 | 0.2 |
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
| worker nodes in service, mean | 12 | 10.46 | −12.9% | −2.6461 to −0.4427 | yes: GAIN |
| node-hours | 5.03 | 4.379 | −12.9% | −1.1102 to −0.1916 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 526.8 | +0.2% | −0.6468 to +3.1879 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 478.3 | −9.0% | −81.6689 to −12.8733 | yes: GAIN |
| response time (ms), mean | 703.3 | 809.9 | +15.2% | +20.0436 to +193.1128 | yes: LOSS |
| response time (ms), 95th percentile | 2521 | 3121 | +23.8% | +150.2995 to +1048.3665 | yes: LOSS |
| response time (ms), 99th percentile | 3317 | 4248 | +28.1% | +310.8855 to +1552.1119 | yes: LOSS |
| time over the response line (% of samples) | 27.06 | 34.18 | +26.3% | +1.7312 to +12.5047 | yes: LOSS |
| failed requests (%) | 0.01711 | 0.09411 | +450.0% | −0.0542 to +0.2082 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 15.4 | +16.7% | −0.5560 to +4.9560 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.6 | +68.600 (native is 0) | +18.8232 to +118.3768 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.38 | 22.74 | +23.7% | +2.3717 to +6.3517 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03427 | 0.0416 | +21.4% | +0.0032 to +0.0115 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.645 | 1.74 | +5.8% | −0.0011 to +0.1904 | no |
| Omni's own CPU (cores), mean | 0 | 0.05391 | +0.054 (native is 0) | +0.0491 to +0.0587 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.794 | +9.0% | +0.0543 to +0.2428 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.8 | 661.7 | −15.3% | −188.7151 to −49.5155 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.93 | 4.668 | +18.8% | +0.2497 to +1.2269 | yes: power given |
| pods started | 0.2 | 2.1 | +950.0% | +0.7102 to +3.0898 | yes: power given |
| pod start wait, total (s) | 0.5 | 6.3 | +1160.0% | +1.3674 to +10.2326 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 2.323 | +364.7% | +0.3089 to +3.3378 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 54.65 | 61.41 | +12.4% | +5.0963 to +8.4124 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 919.6 | 1015 | +10.4% | +41.7118 to +148.8882 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.416 | −29.9% | −5.3795 to −1.7884 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.979 | 22.02 | +342.3% | −4.1267 to +38.2100 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 38.3 | 138.3 | +261.1% | −71.6678 to +271.6678 | no |
| queue: job turnaround, submitted to done, mean (s) | 210.6 | 265.6 | +26.1% | +22.9093 to +87.0240 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.031 | 5.03 | −0.0% | −0.0187 to +0.0174 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 525.6 | +0.1% | −1.3436 to +2.1220 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 525.6 | +0.1% | −1.3436 to +2.1220 | no |
| response time (ms), mean | 482.7 | 703.3 | +45.7% | +42.4298 to +398.7080 | yes: LOSS |
| response time (ms), 95th percentile | 1828 | 2521 | +37.9% | +245.9325 to +1140.3635 | yes: LOSS |
| response time (ms), 99th percentile | 2479 | 3317 | +33.8% | +337.1441 to +1338.4477 | yes: LOSS |
| time over the response line (% of samples) | 18.65 | 27.06 | +45.1% | +4.5980 to +12.2275 | yes: LOSS |
| failed requests (%) | 0 | 0.01711 | +0.017 (native is 0) | −0.0089 to +0.0431 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 13.2 | +25.7% | +1.1901 to +4.2099 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 18.38 | +29.8% | +0.1061 to +8.3373 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03342 | 0.03427 | +2.5% | +0.0001 to +0.0016 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.604 | 1.645 | +2.5% | +0.0039 to +0.0777 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.604 | 1.645 | +2.5% | +0.0039 to +0.0777 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.7 | 780.8 | −2.0% | −32.8270 to +1.2118 | no |
| HPA replicas, mean | 4.075 | 3.93 | −3.5% | −0.4328 to +0.1435 | no |
| pods started | 0.3 | 0.2 | −33.3% | −0.7263 to +0.5263 | no |
| pod start wait, total (s) | 0.5 | 0.5 | ±0.0% | −1.3903 to +1.3903 | no |
| pod start wait, mean (s) | 0.3 | 0.5 | +66.7% | −0.9081 to +1.3081 | no |
| host CPU busy, the real machine under kind (%) | 49.1 | 54.65 | +11.3% | +3.4889 to +7.6211 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.7 | 919.6 | +10.0% | +28.4049 to +139.3951 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 12 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 4.979 | +4879.2% | −5.4596 to +15.2179 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 38.3 | +5371.4% | −45.9466 to +121.1466 | no |
| queue: job turnaround, submitted to done, mean (s) | 144.7 | 210.6 | +45.5% | +17.8455 to +113.8629 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.862 | −17.8% | −3.6532 to −0.6227 | yes: GAIN |
| node-hours | 5.031 | 4.138 | −17.8% | −1.5296 to −0.2573 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 525.8 | +0.1% | −1.0682 to +2.2714 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 458.6 | −12.7% | −114.7960 to −18.3675 | yes: GAIN |
| response time (ms), mean | 482.7 | 538.9 | +11.6% | −9.0232 to +121.4332 | no |
| response time (ms), 95th percentile | 1828 | 2234 | +22.2% | +110.3368 to +701.1722 | yes: LOSS |
| response time (ms), 99th percentile | 2479 | 2966 | +19.6% | +77.4826 to +895.9986 | yes: LOSS |
| time over the response line (% of samples) | 18.65 | 22.09 | +18.5% | +1.1772 to +5.7032 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 11.9 | +13.3% | +0.2715 to +2.5285 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.9 | +124.900 (native is 0) | +62.0267 to +187.7733 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 16.32 | +15.3% | −0.0987 to +4.4220 | no |
| utilisation (used / allocatable) | 0.03342 | 0.04133 | +23.7% | +0.0027 to +0.0131 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.604 | 1.612 | +0.5% | −0.0470 to +0.0618 | no |
| Omni's own CPU (cores), mean | 0 | 0.05447 | +0.054 (native is 0) | +0.0499 to +0.0591 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.604 | 1.666 | +3.9% | +0.0045 to +0.1192 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.7 | 683.9 | −14.1% | −180.8137 to −44.5940 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.075 | 4.483 | +10.0% | +0.0619 to +0.7541 | yes: power given |
| pods started | 0.3 | 1.7 | +466.7% | +0.2715 to +2.5285 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.7 | +640.0% | +0.8444 to +5.5556 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.367 | +355.6% | +0.0244 to +2.1089 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.1 | 54.29 | +10.6% | +3.8942 to +6.4874 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.7 | 865.8 | +3.6% | +5.5574 to +54.6426 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.31 | −30.7% | −5.9239 to −1.4553 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.0875 | −12.5% | −0.0326 to +0.0076 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 144.7 | 169.8 | +17.3% | +5.4815 to +44.6435 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.862 | −17.8% | −3.6532 to −0.6227 | yes: GAIN |
| node-hours | 5.03 | 4.138 | −17.7% | −1.5321 to −0.2534 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.6 | 525.8 | +0.0% | −1.3599 to +1.7846 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.6 | 458.6 | −12.7% | −114.9570 to −18.9849 | yes: GAIN |
| response time (ms), mean | 703.3 | 538.9 | −23.4% | −304.7958 to −23.9320 | yes: GAIN |
| response time (ms), 95th percentile | 2521 | 2234 | −11.4% | −624.2059 to +49.4189 | no |
| response time (ms), 99th percentile | 3317 | 2966 | −10.6% | −705.4802 to +3.3696 | no |
| time over the response line (% of samples) | 27.06 | 22.09 | −18.4% | −7.7772 to −2.1680 | yes: GAIN |
| failed requests (%) | 0.01711 | 0 | −100.0% | −0.0431 to +0.0089 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.2 | 11.9 | −9.8% | −2.1294 to −0.4706 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124.9 | +124.900 (native is 0) | +62.0267 to +187.7733 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 18.38 | 16.32 | −11.2% | −5.3979 to +1.2779 | no |
| utilisation (used / allocatable) | 0.03427 | 0.04133 | +20.6% | +0.0013 to +0.0128 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.645 | 1.612 | −2.0% | −0.0788 to +0.0120 | no |
| Omni's own CPU (cores), mean | 0 | 0.05447 | +0.054 (native is 0) | +0.0499 to +0.0591 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.645 | 1.666 | +1.3% | −0.0273 to +0.0695 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 780.8 | 683.9 | −12.4% | −177.2843 to −16.5082 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.93 | 4.483 | +14.1% | +0.2444 to +0.8609 | yes: power given |
| pods started | 0.2 | 1.7 | +750.0% | +0.4744 to +2.5256 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.7 | +640.0% | +1.0461 to +5.3539 | yes: LOSS |
| pod start wait, mean (s) | 0.5 | 1.367 | +173.3% | −0.2679 to +2.0012 | no |
| host CPU busy, the real machine under kind (%) | 54.65 | 54.29 | −0.7% | −1.6018 to +0.8732 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 919.6 | 865.8 | −5.9% | −88.4377 to −19.1623 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 12 | 8.31 | −30.7% | −5.9239 to −1.4553 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 4.979 | 0.0875 | −98.2% | −15.2379 to +5.4545 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 38.3 | 0.6 | −98.4% | −121.2213 to +45.8213 | no |
| queue: job turnaround, submitted to done, mean (s) | 210.6 | 169.8 | −19.4% | −74.6496 to −6.9338 | yes: GAIN |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.46 | −12.9% | −2.6461 to −0.4427 | yes: GAIN |
| node-hours | 5.031 | 4.379 | −13.0% | −1.1099 to −0.1932 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.2 | 526.8 | +0.3% | −0.5703 to +3.8898 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.2 | 478.3 | −8.9% | −81.6521 to −12.1118 | yes: GAIN |
| response time (ms), mean | 482.7 | 809.9 | +67.8% | +193.1863 to +461.1080 | yes: LOSS |
| response time (ms), 95th percentile | 1828 | 3121 | +70.7% | +891.5740 to +1693.3880 | yes: LOSS |
| response time (ms), 99th percentile | 2479 | 4248 | +71.4% | +1202.6971 to +2335.8921 | yes: LOSS |
| time over the response line (% of samples) | 18.65 | 34.18 | +83.3% | +9.8562 to +21.2053 | yes: LOSS |
| failed requests (%) | 0 | 0.09411 | +0.094 (native is 0) | −0.0560 to +0.2442 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 15.4 | +46.7% | +2.1929 to +7.6071 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.6 | +68.600 (native is 0) | +18.8232 to +118.3768 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.16 | 22.74 | +60.6% | +3.7558 to +13.4108 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03342 | 0.0416 | +24.5% | +0.0045 to +0.0118 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.604 | 1.74 | +8.4% | +0.0429 to +0.2280 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05391 | +0.054 (native is 0) | +0.0491 to +0.0587 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.604 | 1.794 | +11.8% | +0.0977 to +0.2810 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 796.7 | 661.7 | −16.9% | −195.8650 to −73.9808 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.075 | 4.668 | +14.6% | +0.0274 to +1.1599 | yes: power given |
| pods started | 0.3 | 2.1 | +600.0% | +0.6417 to +2.9583 | yes: power given |
| pod start wait, total (s) | 0.5 | 6.3 | +1160.0% | +1.8131 to +9.7869 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 2.323 | +674.4% | +0.9937 to +3.0530 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 49.1 | 61.41 | +25.1% | +10.3160 to +14.3027 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.7 | 1015 | +21.4% | +84.1345 to +274.2655 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.416 | −29.9% | −5.3795 to −1.7884 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 22.02 | +21920.8% | −3.0344 to +46.8760 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 138.3 | +19657.1% | −36.1230 to +311.3230 | no |
| queue: job turnaround, submitted to done, mean (s) | 144.7 | 265.6 | +83.5% | +81.1435 to +160.4982 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*