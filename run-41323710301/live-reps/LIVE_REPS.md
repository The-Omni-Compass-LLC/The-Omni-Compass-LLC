# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.721 | 5.993 |
| node-hours | 2.515 | 2.513 | 1.975 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.7 | 271.3 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.7 | 231.2 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 315.1 | 123.5 | 296.6 | 99.74 |
| response time (ms), 95th percentile | 1153 | 220.8 | 1235 | 209.8 |
| response time (ms), 99th percentile | 1604 | 333.4 | 1739 | 313.8 |
| time over the response line (% of samples) | 13.16 | 0.3091 | 13.43 | 0.189 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 0 | 7.3 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 43 | 16.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.71 | 1104 | 9.685 | 1070 |
| utilisation (used / allocatable) | 0.0584 | 0.05903 | 0.07404 | 0.0596 |
| CPU used (cores), mean | 1.402 | 1.417 | 1.378 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.0168 | 0.01205 |
| CPU used with Omni's own (cores), mean | 1.402 | 1.417 | 1.395 | 1.441 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 458 | 404.2 | 454.1 |
| HPA replicas, mean | 1.896 | 1.939 | 2.023 | 2.045 |
| pods started | 0.2 | 0 | 0.4 | 0 |
| pod start wait, total (s) | 0.6 | 0 | 0.8 | 0 |
| pod start wait, mean (s) | 0.3 | 0 | 0.6 | 0 |
| host CPU busy, the real machine under kind (%) | 39.72 | 44.09 | 40.94 | 44.53 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.9 | 1412 | 780.2 | 1412 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.966 | 5.903 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 139.9 | 0.04167 | 151.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 612.3 | 0.4 | 689.5 |
| queue: job turnaround, submitted to done, mean (s) | 79.05 | 783.2 | 85.22 | 789.6 |
| queue: jobs unfinished at the window's end | 0 | 9 | 0 | 8.5 |
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
| worker nodes in service, mean | 6 | 5.993 | −0.1% | −0.0164 to +0.0033 | no |
| node-hours | 2.513 | 2.51 | −0.1% | −0.0148 to +0.0090 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.8 | +0.0% | −1.2084 to +1.4574 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 271.6 | −0.0% | −1.5183 to +1.3590 | no |
| response time (ms), mean | 123.5 | 99.74 | −19.2% | −31.6097 to −15.8371 | yes: GAIN |
| response time (ms), 95th percentile | 220.8 | 209.8 | −5.0% | −19.6374 to −2.3826 | yes: GAIN |
| response time (ms), 99th percentile | 333.4 | 313.8 | −5.9% | −40.2637 to +1.0687 | no |
| time over the response line (% of samples) | 0.3091 | 0.189 | −38.8% | −0.2537 to +0.0136 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.4 | +16.400 (native is 0) | +12.5672 to +20.2328 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1104 | 1070 | −3.1% | −106.6429 to +37.3262 | no |
| utilisation (used / allocatable) | 0.05903 | 0.0596 | +1.0% | −0.0003 to +0.0014 | no |
| CPU used (cores), mean | 1.417 | 1.429 | +0.9% | −0.0085 to +0.0326 | no |
| Omni's own CPU (cores), mean | 0 | 0.01205 | +0.012 (native is 0) | +0.0104 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.417 | 1.441 | +1.7% | +0.0033 to +0.0449 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458 | 454.1 | −0.9% | −9.5238 to +1.6618 | no |
| HPA replicas, mean | 1.939 | 2.045 | +5.5% | +0.0010 to +0.2116 | yes: power given |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 44.09 | 44.53 | +1.0% | −0.1352 to +1.0154 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1412 | 1412 | −0.0% | −15.1060 to +14.1060 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.903 | −1.6% | −0.2750 to +0.0813 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 139.9 | 151.4 | +8.2% | −19.8581 to +42.8581 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 612.3 | 689.5 | +12.6% | −37.9473 to +192.3473 | no |
| queue: job turnaround, submitted to done, mean (s) | 783.2 | 789.6 | +0.8% | −41.9222 to +54.7972 | no |
| queue: jobs unfinished at the window's end | 9 | 8.5 | −5.6% | −2.9374 to +1.9374 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.513 | −0.1% | −0.0116 to +0.0083 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.7 | −0.1% | −3.0574 to +2.7508 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.7 | −0.1% | −3.0574 to +2.7508 | no |
| response time (ms), mean | 315.1 | 123.5 | −60.8% | −341.7263 to −41.4891 | yes: GAIN |
| response time (ms), 95th percentile | 1153 | 220.8 | −80.8% | −1663.8584 to −199.5656 | yes: GAIN |
| response time (ms), 99th percentile | 1604 | 333.4 | −79.2% | −2257.3859 to −283.5841 | yes: GAIN |
| time over the response line (% of samples) | 13.16 | 0.3091 | −97.7% | −23.7916 to −1.9199 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 0 | −100.0% | −11.6256 to −1.9744 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.71 | 1104 | +12580.1% | +808.5400 to +1382.9133 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0584 | 0.05903 | +1.1% | −0.0064 to +0.0076 | no |
| CPU used (cores), mean | 1.402 | 1.417 | +1.1% | −0.1526 to +0.1830 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.402 | 1.417 | +1.1% | −0.1526 to +0.1830 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 458 | −3.4% | −65.8561 to +33.6218 | no |
| HPA replicas, mean | 1.896 | 1.939 | +2.3% | −0.0575 to +0.1429 | no |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.6 | 0 | −100.0% | −1.9572 to +0.7572 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 39.72 | 44.09 | +11.0% | +0.7542 to +7.9849 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.9 | 1412 | +82.5% | +569.6716 to +707.1284 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 139.9 | +305127.3% | +82.8620 to +196.8380 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 612.3 | +306050.0% | +384.0895 to +840.1105 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.05 | 783.2 | +890.7% | +588.2499 to +819.9584 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9 | +9.000 (native is 0) | +2.2476 to +15.7524 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.721 | −21.3% | −2.1376 to −0.4207 | yes: GAIN |
| node-hours | 2.515 | 1.975 | −21.4% | −0.8963 to −0.1820 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.3 | −0.2% | −1.4412 to +0.4699 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 231.2 | −15.0% | −67.9525 to −13.3688 | yes: GAIN |
| response time (ms), mean | 315.1 | 296.6 | −5.9% | −37.2289 to +0.3603 | no |
| response time (ms), 95th percentile | 1153 | 1235 | +7.2% | −18.2396 to +183.5716 | no |
| response time (ms), 99th percentile | 1604 | 1739 | +8.4% | +4.1390 to +266.3668 | yes: LOSS |
| time over the response line (% of samples) | 13.16 | 13.43 | +2.0% | −0.0738 to +0.6007 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 7.3 | +7.4% | −0.0058 to +1.0058 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43 | +43.000 (native is 0) | +21.5196 to +64.4804 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.71 | 9.685 | +11.2% | +0.1752 to +1.7748 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0584 | 0.07404 | +26.8% | +0.0057 to +0.0256 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.402 | 1.378 | −1.7% | −0.0682 to +0.0215 | no |
| Omni's own CPU (cores), mean | 0 | 0.0168 | +0.017 (native is 0) | +0.0149 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.402 | 1.395 | −0.5% | −0.0524 to +0.0393 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 404.2 | −14.7% | −112.4008 to −27.3360 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.896 | 2.023 | +6.7% | −0.0723 to +0.3260 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.5388 to +0.9388 | no |
| pod start wait, total (s) | 0.6 | 0.8 | +33.3% | −1.6714 to +2.0714 | no |
| pod start wait, mean (s) | 0.3 | 0.6 | +100.0% | −0.8209 to +1.4209 | no |
| host CPU busy, the real machine under kind (%) | 39.72 | 40.94 | +3.1% | +0.5942 to +1.8329 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.9 | 780.2 | +0.8% | −0.0179 to +12.6179 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.966 | −33.9% | −3.3564 to −0.7115 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.04167 | −9.1% | −0.0303 to +0.0219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 0.4 | +100.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.05 | 85.22 | +7.8% | −0.2423 to +12.5757 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.721 | −21.3% | −2.1376 to −0.4207 | yes: GAIN |
| node-hours | 2.513 | 1.975 | −21.4% | −0.8975 to −0.1775 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 271.3 | −0.1% | −3.3653 to +2.7006 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 231.2 | −14.9% | −70.1592 to −10.8555 | yes: GAIN |
| response time (ms), mean | 123.5 | 296.6 | +140.3% | +19.2297 to +327.1171 | yes: LOSS |
| response time (ms), 95th percentile | 220.8 | 1235 | +459.3% | +234.4849 to +1794.2711 | yes: LOSS |
| response time (ms), 99th percentile | 333.4 | 1739 | +421.6% | +336.3138 to +2475.1620 | yes: LOSS |
| time over the response line (% of samples) | 0.3091 | 13.43 | +4244.6% | +2.0314 to +24.2069 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 7.3 | +7.300 (native is 0) | +2.4480 to +12.1520 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43 | +43.000 (native is 0) | +21.5196 to +64.4804 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1104 | 9.685 | −99.1% | −1381.8544 to −807.6490 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05903 | 0.07404 | +25.4% | +0.0092 to +0.0208 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.417 | 1.378 | −2.7% | −0.2460 to +0.1689 | no |
| Omni's own CPU (cores), mean | 0 | 0.0168 | +0.017 (native is 0) | +0.0149 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.417 | 1.395 | −1.5% | −0.2296 to +0.1861 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458 | 404.2 | −11.7% | −76.8393 to −30.6632 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.939 | 2.023 | +4.3% | −0.1445 to +0.3129 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.2556 to +1.8556 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| host CPU busy, the real machine under kind (%) | 44.09 | 40.94 | −7.2% | −6.9644 to +0.6524 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1412 | 780.2 | −44.8% | −700.1511 to −564.0489 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.02 | −66.3% | −4.0445 to −3.9147 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 139.9 | 0.04167 | −100.0% | −196.8386 to −82.8698 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 612.3 | 0.4 | −99.9% | −839.7494 to −384.0506 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 783.2 | 85.22 | −89.1% | −809.8934 to −585.9816 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9 | 0 | −100.0% | −15.7524 to −2.2476 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.993 | −0.1% | −0.0164 to +0.0033 | no |
| node-hours | 2.515 | 2.51 | −0.2% | −0.0105 to +0.0014 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.8 | −0.0% | −2.7142 to +2.6567 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.6 | −0.1% | −2.8136 to +2.3477 | no |
| response time (ms), mean | 315.1 | 99.74 | −68.3% | −365.9336 to −64.7287 | yes: GAIN |
| response time (ms), 95th percentile | 1153 | 209.8 | −81.8% | −1676.3372 to −209.1068 | yes: GAIN |
| response time (ms), 99th percentile | 1604 | 313.8 | −80.4% | −2284.8591 to −295.3059 | yes: GAIN |
| time over the response line (% of samples) | 13.16 | 0.189 | −98.6% | −24.0235 to −1.9281 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.8 | 0.1 | −98.5% | −11.4454 to −1.9546 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.4 | +16.400 (native is 0) | +12.5672 to +20.2328 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.71 | 1070 | +12182.2% | +777.2406 to +1344.8961 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0584 | 0.0596 | +2.1% | −0.0059 to +0.0083 | no |
| CPU used (cores), mean | 1.402 | 1.429 | +1.9% | −0.1422 to +0.1968 | no |
| Omni's own CPU (cores), mean | 0 | 0.01205 | +0.012 (native is 0) | +0.0104 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.402 | 1.441 | +2.8% | −0.1287 to +0.2073 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 474.1 | 454.1 | −4.2% | −70.7009 to +30.6047 | no |
| HPA replicas, mean | 1.896 | 2.045 | +7.9% | +0.0229 to +0.2752 | yes: power given |
| pods started | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.6 | 0 | −100.0% | −1.9572 to +0.7572 | no |
| pod start wait, mean (s) | 0.3 | 0 | −100.0% | −0.9786 to +0.3786 | no |
| host CPU busy, the real machine under kind (%) | 39.72 | 44.53 | +12.1% | +1.3883 to +8.2310 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.9 | 1412 | +82.4% | +569.8848 to +705.9152 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.903 | −1.6% | −0.2750 to +0.0813 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 151.4 | +330218.2% | +102.0956 to +200.6044 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 689.5 | +344650.0% | +532.6189 to +845.9811 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.05 | 789.6 | +898.8% | +595.1522 to +825.9311 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.5 | +8.500 (native is 0) | +1.8047 to +15.1953 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*