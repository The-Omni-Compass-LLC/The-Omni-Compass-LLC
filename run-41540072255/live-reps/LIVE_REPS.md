# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.06 | 6.296 |
| node-hours | 5.027 | 5.027 | 4.216 | 2.64 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.6 | 526.9 | 505.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 504.6 | 465.9 | 325.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 669.7 | 120.4 | 788.5 | 71.38 |
| response time (ms), 95th percentile | 2593 | 164.7 | 3302 | 96.09 |
| response time (ms), 99th percentile | 3489 | 196.4 | 4447 | 123.3 |
| time over the response line (% of samples) | 22.76 | 0.00381 | 24.71 | 0.003636 |
| failed requests (%) | 0 | 0 | 0.03089 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 0 | 11.6 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 144.9 | 35.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 32.74 | 97.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.06 | 0 | 30.27 | 0.1567 |
| utilisation (used / allocatable) | 0.035 | 0.005985 | 0.0427 | 0.009491 |
| CPU used (cores), mean | 1.68 | 0.2873 | 1.705 | 0.2402 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05712 | 0.0312 |
| CPU used with Omni's own (cores), mean | 1.68 | 0.2873 | 1.763 | 0.2714 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.1 | 4311 | 663.6 | 3390 |
| HPA replicas, mean | 4.015 | 4.182 | 4.72 | 4.608 |
| pods started | 0 | 0.5 | 3.1 | 2.6 |
| pod start wait, total (s) | 0 | 0.5 | 8.5 | 3.5 |
| pod start wait, mean (s) | 0 | 0.3 | 1.91 | 0.9524 |
| host CPU busy, the real machine under kind (%) | 51.74 | 14.66 | 58.12 | 17.3 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 904.8 | 1506 | 958.5 | 1508 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.976 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1160 | 0.1208 | 1162 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1476 | 0.6 | 1478 |
| queue: job turnaround, submitted to done, mean (s) | 214.2 | 1160 | 259.9 | 1162 |
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
| worker nodes in service, mean | 12 | 6.296 | −47.5% | −5.8982 to −5.5106 | yes: GAIN |
| node-hours | 5.027 | 2.64 | −47.5% | −2.4728 to −2.3014 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 505.3 | +0.1% | −0.0315 to +1.4654 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 325.9 | −35.4% | −185.2880 to −172.0906 | yes: GAIN |
| response time (ms), mean | 120.4 | 71.38 | −40.7% | −60.9856 to −37.0184 | yes: GAIN |
| response time (ms), 95th percentile | 164.7 | 96.09 | −41.7% | −82.5405 to −54.7335 | yes: GAIN |
| response time (ms), 99th percentile | 196.4 | 123.3 | −37.2% | −91.3448 to −54.7952 | yes: GAIN |
| time over the response line (% of samples) | 0.00381 | 0.003636 | −4.5% | −0.0127 to +0.0124 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.5 | +35.500 (native is 0) | +29.9979 to +41.0021 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1567 | +0.157 (native is 0) | −0.0238 to +0.3371 | no |
| utilisation (used / allocatable) | 0.005985 | 0.009491 | +58.6% | +0.0029 to +0.0041 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2873 | 0.2402 | −16.4% | −0.0541 to −0.0402 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0312 | +0.031 (native is 0) | +0.0268 to +0.0356 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2873 | 0.2714 | −5.5% | −0.0259 to −0.0059 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4311 | 3390 | −21.3% | −993.5921 to −847.1461 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.182 | 4.608 | +10.2% | −0.0586 to +0.9095 | no |
| pods started | 0.5 | 2.6 | +420.0% | +0.0365 to +4.1635 | yes: power given |
| pod start wait, total (s) | 0.5 | 3.5 | +600.0% | −0.0905 to +6.0905 | no |
| pod start wait, mean (s) | 0.3 | 0.9524 | +217.5% | −0.1374 to +1.4421 | no |
| host CPU busy, the real machine under kind (%) | 14.66 | 17.3 | +18.0% | +1.9214 to +3.3654 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1508 | +0.1% | −0.1485 to +3.5485 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1162 | +0.2% | −0.1348 to +3.6514 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1478 | +0.1% | −0.1015 to +3.7015 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1162 | +0.2% | −0.1348 to +3.6514 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.027 | 5.027 | +0.0% | −0.0146 to +0.0153 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.6 | −4.0% | −25.6479 to −16.9078 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 504.6 | −4.0% | −25.6479 to −16.9078 | yes: GAIN |
| response time (ms), mean | 669.7 | 120.4 | −82.0% | −866.2474 to −232.4596 | yes: GAIN |
| response time (ms), 95th percentile | 2593 | 164.7 | −93.6% | −3858.3855 to −998.9395 | yes: GAIN |
| response time (ms), 99th percentile | 3489 | 196.4 | −94.4% | −5196.1790 to −1389.6522 | yes: GAIN |
| time over the response line (% of samples) | 22.76 | 0.00381 | −100.0% | −36.6983 to −8.8201 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 0 | −100.0% | −16.8086 to −3.9914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.06 | 0 | −100.0% | −34.0980 to −10.0153 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.035 | 0.005985 | −82.9% | −0.0331 to −0.0249 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.68 | 0.2873 | −82.9% | −1.5905 to −1.1949 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.68 | 0.2873 | −82.9% | −1.5905 to −1.1949 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.1 | 4311 | +457.6% | +3065.8759 to +4009.6276 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.015 | 4.182 | +4.2% | −0.0564 to +0.3900 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.1079 to +1.1079 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| host CPU busy, the real machine under kind (%) | 51.74 | 14.66 | −71.7% | −43.4300 to −30.7406 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 904.8 | 1506 | +66.5% | +487.8603 to +715.3397 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1160 | +1159675.0% | +1157.4807 to +1161.8693 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1476 | +210742.9% | +1472.7966 to +1477.6034 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 214.2 | 1160 | +441.5% | +829.9557 to +1061.2027 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.06 | −16.2% | −3.7792 to −0.1012 | yes: GAIN |
| node-hours | 5.027 | 4.216 | −16.1% | −1.5762 to −0.0447 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 526.9 | +0.2% | −0.7585 to +2.9336 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 465.9 | −11.4% | −118.0388 to −1.9528 | yes: GAIN |
| response time (ms), mean | 669.7 | 788.5 | +17.7% | +31.2909 to +206.2028 | yes: LOSS |
| response time (ms), 95th percentile | 2593 | 3302 | +27.3% | +238.0180 to +1179.1920 | yes: LOSS |
| response time (ms), 99th percentile | 3489 | 4447 | +27.4% | +338.4595 to +1577.1139 | yes: LOSS |
| time over the response line (% of samples) | 22.76 | 24.71 | +8.5% | +0.9003 to +2.9921 | yes: LOSS |
| failed requests (%) | 0 | 0.03089 | +0.031 (native is 0) | −0.0085 to +0.0703 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 11.6 | +11.5% | +0.5427 to +1.8573 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 144.9 | +144.900 (native is 0) | +63.9565 to +225.8435 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.06 | 30.27 | +37.2% | −5.1629 to +21.5929 | no |
| utilisation (used / allocatable) | 0.035 | 0.0427 | +22.0% | +0.0019 to +0.0135 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.68 | 1.705 | +1.5% | −0.0642 to +0.1151 | no |
| Omni's own CPU (cores), mean | 0 | 0.05712 | +0.057 (native is 0) | +0.0532 to +0.0611 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.68 | 1.763 | +4.9% | −0.0105 to +0.1756 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.1 | 663.6 | −14.2% | −186.6672 to −32.4473 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.015 | 4.72 | +17.6% | +0.2036 to +1.2063 | yes: power given |
| pods started | 0 | 3.1 | +3.100 (native is 0) | +1.2701 to +4.9299 | yes: power given |
| pod start wait, total (s) | 0 | 8.5 | +8.500 (native is 0) | +3.3612 to +13.6388 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.91 | +1.910 (native is 0) | +0.8960 to +2.9235 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.74 | 58.12 | +12.3% | +4.9487 to +7.8006 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 904.8 | 958.5 | +5.9% | +21.3868 to +86.0132 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.976 | −25.2% | −5.7758 to −0.2720 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.1208 | +20.8% | −0.0170 to +0.0587 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.6 | −14.3% | −0.3262 to +0.1262 | no |
| queue: job turnaround, submitted to done, mean (s) | 214.2 | 259.9 | +21.3% | +17.7630 to +73.5704 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.06 | −16.2% | −3.7792 to −0.1012 | yes: GAIN |
| node-hours | 5.027 | 4.216 | −16.1% | −1.5860 to −0.0356 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.6 | 526.9 | +4.4% | +17.9623 to +26.7685 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.6 | 465.9 | −7.7% | −100.6776 to +23.2417 | no |
| response time (ms), mean | 120.4 | 788.5 | +555.0% | +266.7376 to +1069.4631 | yes: LOSS |
| response time (ms), 95th percentile | 164.7 | 3302 | +1904.5% | +1286.5163 to +4988.0187 | yes: LOSS |
| response time (ms), 99th percentile | 196.4 | 4447 | +2164.5% | +1815.5944 to +6685.8102 | yes: LOSS |
| time over the response line (% of samples) | 0.00381 | 24.71 | +648518.2% | +9.8764 to +39.5345 | yes: LOSS |
| failed requests (%) | 0 | 0.03089 | +0.031 (native is 0) | −0.0085 to +0.0703 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 11.6 | +11.600 (native is 0) | +5.0424 to +18.1576 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 144.9 | +144.900 (native is 0) | +63.9565 to +225.8435 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 30.27 | +30.272 (native is 0) | +8.8723 to +51.6711 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005985 | 0.0427 | +613.3% | +0.0335 to +0.0399 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2873 | 1.705 | +493.6% | +1.1461 to +1.6901 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05712 | +0.057 (native is 0) | +0.0532 to +0.0611 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2873 | 1.763 | +513.5% | +1.1996 to +1.7509 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4311 | 663.6 | −84.6% | −4191.4646 to −3103.1533 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.182 | 4.72 | +12.9% | +0.0557 to +1.0206 | yes: power given |
| pods started | 0.5 | 3.1 | +520.0% | +0.5159 to +4.6841 | yes: power given |
| pod start wait, total (s) | 0.5 | 8.5 | +1600.0% | +2.6048 to +13.3952 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.91 | +536.6% | +0.4629 to +2.7566 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14.66 | 58.12 | +296.5% | +35.7586 to +51.1614 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 958.5 | −36.4% | −693.5819 to −402.2181 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.1208 | −100.0% | −1161.8465 to −1157.4618 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.6 | −100.0% | −1477.6374 to −1472.9626 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 259.9 | −77.6% | −1042.8886 to −756.9364 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.296 | −47.5% | −5.8982 to −5.5106 | yes: GAIN |
| node-hours | 5.027 | 2.64 | −47.5% | −2.4653 to −2.3082 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 505.3 | −3.9% | −24.2827 to −16.8391 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 325.9 | −38.0% | −204.3701 to −195.5643 | yes: GAIN |
| response time (ms), mean | 669.7 | 71.38 | −89.3% | −926.0705 to −270.6406 | yes: GAIN |
| response time (ms), 95th percentile | 2593 | 96.09 | −96.3% | −3937.2129 to −1057.3861 | yes: GAIN |
| response time (ms), 99th percentile | 3489 | 123.3 | −96.5% | −5276.3315 to −1455.6397 | yes: GAIN |
| time over the response line (% of samples) | 22.76 | 0.003636 | −100.0% | −36.6980 to −8.8208 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 0 | −100.0% | −16.8086 to −3.9914 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.5 | +35.500 (native is 0) | +29.9979 to +41.0021 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 22.06 | 0.1567 | −99.3% | −33.8579 to −9.9421 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.035 | 0.009491 | −72.9% | −0.0291 to −0.0219 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.68 | 0.2402 | −85.7% | −1.6335 to −1.2461 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0312 | +0.031 (native is 0) | +0.0268 to +0.0356 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.68 | 0.2714 | −83.8% | −1.5982 to −1.2190 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 773.1 | 3390 | +338.6% | +2155.4453 to +3079.3201 | yes, up (shown, not judged) |
| HPA replicas, mean | 4.015 | 4.608 | +14.7% | +0.2535 to +0.9310 | yes: power given |
| pods started | 0 | 2.6 | +2.600 (native is 0) | +0.9412 to +4.2588 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +0.7554 to +6.2446 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9524 | +0.952 (native is 0) | +0.4109 to +1.4938 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 51.74 | 17.3 | −66.6% | −40.1115 to −28.7724 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 904.8 | 1508 | +66.7% | +490.3760 to +716.2240 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 1162 | +1161433.3% | +1159.6571 to +1163.2095 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1478 | +211000.0% | +1475.1226 to +1478.8774 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 214.2 | 1162 | +442.3% | +832.7296 to +1061.9454 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*