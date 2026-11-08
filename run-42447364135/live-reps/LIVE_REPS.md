# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.486 | 5.968 |
| node-hours | 2.514 | 2.518 | 1.881 | 2.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 287.6 | 271.2 | 287.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 287.6 | 223.7 | 286.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 308.9 | 590 | 289.2 | 605.3 |
| response time (ms), 95th percentile | 1066 | 1230 | 1194 | 1261 |
| response time (ms), 99th percentile | 1445 | 1661 | 1614 | 1720 |
| time over the response line (% of samples) | 11.66 | 51.69 | 12.08 | 52.98 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 24 | 7.2 | 24 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 124 | 33.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 28.12 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.427 | 2.255 | 10.72 | 2.247 |
| utilisation (used / allocatable) | 0.05736 | 0.09965 | 0.0757 | 0.09913 |
| CPU used (cores), mean | 1.377 | 2.392 | 1.348 | 2.368 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06882 | 0.03944 |
| CPU used with Omni's own (cores), mean | 1.377 | 2.392 | 1.416 | 2.407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.4 | 287.5 | 405.1 | 288.9 |
| HPA replicas, mean | 1.964 | 2.027 | 2.124 | 2.508 |
| pods started | 0.1 | 0 | 1 | 1.6 |
| pod start wait, total (s) | 0.2 | 0 | 2.2 | 4.3 |
| pod start wait, mean (s) | 0.2 | 0 | 1.283 | 2.04 |
| host CPU busy, the real machine under kind (%) | 39.29 | 74.65 | 42.15 | 75.99 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.5 | 1455 | 779.8 | 1462 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.59 | 5.53 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 510.1 | 0.2167 | 540.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 998.2 | 0.5 | 1057 |
| queue: job turnaround, submitted to done, mean (s) | 79.67 | 896.2 | 85 | 901.9 |
| queue: jobs unfinished at the window's end | 0 | 11.5 | 0 | 12.3 |
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
| worker nodes in service, mean | 6 | 5.968 | −0.5% | −0.1028 to +0.0398 | no |
| node-hours | 2.518 | 2.507 | −0.4% | −0.0382 to +0.0170 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 287.6 | 287.6 | −0.0% | −0.7218 to +0.6902 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.6 | 286.6 | −0.4% | −2.9848 to +0.9657 | no |
| response time (ms), mean | 590 | 605.3 | +2.6% | −27.7043 to +58.1465 | no |
| response time (ms), 95th percentile | 1230 | 1261 | +2.5% | −80.4518 to +142.1798 | no |
| response time (ms), 99th percentile | 1661 | 1720 | +3.6% | −56.0781 to +174.4963 | no |
| time over the response line (% of samples) | 51.69 | 52.98 | +2.5% | −3.3885 to +5.9606 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +29.0456 to +38.5544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.255 | 2.247 | −0.4% | −0.4772 to +0.4606 | no |
| utilisation (used / allocatable) | 0.09965 | 0.09913 | −0.5% | −0.0019 to +0.0009 | no |
| CPU used (cores), mean | 2.392 | 2.368 | −1.0% | −0.0384 to −0.0093 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03944 | +0.039 (native is 0) | +0.0336 to +0.0453 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.392 | 2.407 | +0.7% | +0.0010 to +0.0302 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.5 | 288.9 | +0.5% | −2.2855 to +4.9394 | no |
| HPA replicas, mean | 2.027 | 2.508 | +23.7% | +0.2582 to +0.7037 | yes: power given |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4222 to +2.7778 | yes: power given |
| pod start wait, total (s) | 0 | 4.3 | +4.300 (native is 0) | +1.4180 to +7.1820 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.04 | +2.040 (native is 0) | +0.8792 to +3.2008 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 74.65 | 75.99 | +1.8% | +1.0734 to +1.6104 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 1462 | +0.5% | −0.1115 to +13.5115 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.53 | −7.8% | −2.4908 to +1.5514 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 510.1 | 540.5 | +6.0% | −7.6393 to +68.4274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 998.2 | 1057 | +5.9% | −4.3749 to +121.4411 | no |
| queue: job turnaround, submitted to done, mean (s) | 896.2 | 901.9 | +0.6% | −18.2216 to +29.5799 | no |
| queue: jobs unfinished at the window's end | 11.5 | 12.3 | +7.0% | −0.2556 to +1.8556 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.518 | +0.2% | −0.0036 to +0.0122 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 287.6 | +6.0% | +12.0505 to +20.4936 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 287.6 | +6.0% | +12.0505 to +20.4936 | yes: power given |
| response time (ms), mean | 308.9 | 590 | +91.0% | +181.3217 to +380.9922 | yes: LOSS |
| response time (ms), 95th percentile | 1066 | 1230 | +15.4% | −470.7339 to +799.5499 | no |
| response time (ms), 99th percentile | 1445 | 1661 | +14.9% | −628.0369 to +1060.0475 | no |
| time over the response line (% of samples) | 11.66 | 51.69 | +343.2% | +31.0595 to +48.9960 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 24 | +252.9% | +13.0046 to +21.3954 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.427 | 2.255 | −76.1% | −10.8353 to −3.5080 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05736 | 0.09965 | +73.7% | +0.0320 to +0.0526 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.377 | 2.392 | +73.7% | +0.7684 to +1.2616 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.377 | 2.392 | +73.7% | +0.7684 to +1.2616 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.4 | 287.5 | −41.1% | −273.9952 to −127.7271 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.027 | +3.2% | −0.0539 to +0.1801 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 39.29 | 74.65 | +90.0% | +30.6158 to +40.1056 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.5 | 1455 | +88.1% | +598.1290 to +765.2710 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 510.1 | +1020056.0% | +226.9366 to +793.1194 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 998.2 | +499019.1% | +581.5448 to +1414.5318 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.67 | 896.2 | +1024.9% | +683.1474 to +949.9859 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.5 | +11.500 (native is 0) | +5.0117 to +17.9883 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.486 | −25.2% | −2.3654 to −0.6622 | yes: GAIN |
| node-hours | 2.514 | 1.881 | −25.2% | −0.9907 to −0.2751 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 271.2 | −0.1% | −1.3435 to +1.0671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 223.7 | −17.6% | −75.0976 to −20.1830 | yes: GAIN |
| response time (ms), mean | 308.9 | 289.2 | −6.4% | −37.9697 to −1.3725 | yes: GAIN |
| response time (ms), 95th percentile | 1066 | 1194 | +12.0% | +17.3501 to +238.7439 | yes: LOSS |
| response time (ms), 99th percentile | 1445 | 1614 | +11.6% | −58.8502 to +395.3314 | no |
| time over the response line (% of samples) | 11.66 | 12.08 | +3.6% | −1.1167 to +1.9537 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.2 | +5.9% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124 | +124.000 (native is 0) | +63.7139 to +184.2861 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.427 | 10.72 | +13.7% | −1.2196 to +3.7996 | no |
| utilisation (used / allocatable) | 0.05736 | 0.0757 | +32.0% | +0.0085 to +0.0282 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.377 | 1.348 | −2.1% | −0.0817 to +0.0235 | no |
| Omni's own CPU (cores), mean | 0 | 0.06882 | +0.069 (native is 0) | +0.0609 to +0.0767 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.377 | 1.416 | +2.9% | −0.0194 to +0.0989 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.4 | 405.1 | −17.0% | −130.4357 to −36.0965 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.124 | +8.2% | −0.0723 to +0.3937 | no |
| pods started | 0.1 | 1 | +900.0% | +0.1887 to +1.6113 | yes: power given |
| pod start wait, total (s) | 0.2 | 2.2 | +1000.0% | +0.3140 to +3.6860 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.283 | +541.7% | +0.2588 to +1.9079 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.29 | 42.15 | +7.3% | +1.9482 to +3.7634 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.5 | 779.8 | +0.8% | −1.3601 to +13.9601 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.59 | −40.2% | −3.5917 to −1.2291 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.2167 | +333.3% | −0.1122 to +0.4456 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.5 | +150.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.67 | 85 | +6.7% | −1.9327 to +12.5827 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.486 | −25.2% | −2.3654 to −0.6622 | yes: GAIN |
| node-hours | 2.518 | 1.881 | −25.3% | −0.9952 to −0.2792 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 287.6 | 271.2 | −5.7% | −21.0169 to −11.8037 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.6 | 223.7 | −22.2% | −94.1431 to −33.6816 | yes: GAIN |
| response time (ms), mean | 590 | 289.2 | −51.0% | −395.2123 to −206.4438 | yes: GAIN |
| response time (ms), 95th percentile | 1230 | 1194 | −3.0% | −756.1796 to +683.4576 | no |
| response time (ms), 99th percentile | 1661 | 1614 | −2.9% | −1035.0157 to +939.4863 | no |
| time over the response line (% of samples) | 51.69 | 12.08 | −76.6% | −47.8514 to −31.3671 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 24 | 7.2 | −70.0% | −20.7583 to −12.8417 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124 | +124.000 (native is 0) | +63.7139 to +184.2861 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.255 | 10.72 | +375.2% | +3.7952 to +13.1282 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09965 | 0.0757 | −24.0% | −0.0343 to −0.0136 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.392 | 1.348 | −43.7% | −1.3266 to −0.7616 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06882 | +0.069 (native is 0) | +0.0609 to +0.0767 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.392 | 1.416 | −40.8% | −1.2647 to −0.6859 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 287.5 | 405.1 | +40.9% | +73.4999 to +161.6903 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.027 | 2.124 | +4.8% | −0.1658 to +0.3609 | no |
| pods started | 0 | 1 | +1.000 (native is 0) | +0.2460 to +1.7540 | yes: power given |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | +0.4544 to +3.9456 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.283 | +1.283 (native is 0) | +0.4845 to +2.0822 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 74.65 | 42.15 | −43.5% | −38.0254 to −26.9845 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 779.8 | −46.4% | −760.6968 to −590.1032 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 510.1 | 0.2167 | −100.0% | −792.8328 to −226.8898 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 998.2 | 0.5 | −99.9% | −1414.2341 to −581.2425 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 896.2 | 85 | −90.5% | −942.3751 to −680.1082 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.5 | 0 | −100.0% | −17.9883 to −5.0117 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.968 | −0.5% | −0.1028 to +0.0398 | no |
| node-hours | 2.514 | 2.507 | −0.2% | −0.0387 to +0.0262 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.3 | 287.6 | +6.0% | +11.9159 to +20.5967 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.3 | 286.6 | +5.6% | +9.9557 to +20.5694 | yes: power given |
| response time (ms), mean | 308.9 | 605.3 | +96.0% | +212.0362 to +380.7199 | yes: LOSS |
| response time (ms), 95th percentile | 1066 | 1261 | +18.3% | −399.5370 to +790.0810 | no |
| response time (ms), 99th percentile | 1445 | 1720 | +19.0% | −558.9408 to +1109.3696 | no |
| time over the response line (% of samples) | 11.66 | 52.98 | +354.2% | +31.9373 to +50.6904 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 24 | +252.9% | +13.0046 to +21.3954 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.8 | +33.800 (native is 0) | +29.0456 to +38.5544 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.427 | 2.247 | −76.2% | −10.8060 to −3.5540 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05736 | 0.09913 | +72.8% | +0.0317 to +0.0519 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.377 | 2.368 | +72.0% | +0.7443 to +1.2381 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03944 | +0.039 (native is 0) | +0.0336 to +0.0453 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.377 | 2.407 | +74.9% | +0.7884 to +1.2729 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 488.4 | 288.9 | −40.9% | −272.8628 to −126.2056 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.964 | 2.508 | +27.7% | +0.3667 to +0.7215 | yes: power given |
| pods started | 0.1 | 1.6 | +1500.0% | +0.2726 to +2.7274 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.3 | +2050.0% | +1.2101 to +6.9899 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.04 | +920.0% | +0.9025 to +2.7775 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 39.29 | 75.99 | +93.4% | +32.0196 to +41.3857 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.5 | 1462 | +89.0% | +607.8799 to +768.9201 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.53 | −7.8% | −2.4908 to +1.5514 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 540.5 | +1080844.1% | +262.9537 to +817.8904 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1057 | +528285.7% | +680.1730 to +1432.9699 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.67 | 901.9 | +1032.1% | +687.9893 to +956.5024 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.3 | +12.300 (native is 0) | +5.7005 to +18.8995 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*