# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.717 | 6.551 |
| node-hours | 5.026 | 5.027 | 4.069 | 2.744 |
| energy, parked workers still on at idle power (Wh, declared model) | 523.7 | 504.4 | 524.2 | 504.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.7 | 504.4 | 452.3 | 333.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 460.7 | 108.9 | 511.6 | 65.96 |
| response time (ms), 95th percentile | 1742 | 150 | 2077 | 88.11 |
| response time (ms), 99th percentile | 2333 | 168.8 | 2765 | 115.2 |
| time over the response line (% of samples) | 15.78 | 0.003802 | 19.08 | 0.003656 |
| failed requests (%) | 0 | 0 | 0.01581 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | 10.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 172.9 | 32.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 34.25 | 97.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 0 | 15.38 | 0.195 |
| utilisation (used / allocatable) | 0.03205 | 0.005655 | 0.03996 | 0.008715 |
| CPU used (cores), mean | 1.538 | 0.2714 | 1.539 | 0.2293 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05143 | 0.0287 |
| CPU used with Omni's own (cores), mean | 1.538 | 0.2714 | 1.59 | 0.258 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853.7 | 4544 | 714.2 | 3586 |
| HPA replicas, mean | 3.867 | 4.199 | 4.65 | 4.513 |
| pods started | 0.1 | 0.7 | 2.2 | 2.3 |
| pod start wait, total (s) | 0.2 | 1.1 | 5.8 | 3.9 |
| pod start wait, mean (s) | 0.2 | 0.575 | 1.285 | 1.469 |
| host CPU busy, the real machine under kind (%) | 47.27 | 14 | 52.6 | 16.44 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 827.6 | 1505 | 858.7 | 1506 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 8.354 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1159 | 0.0625 | 1159 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1475 | 0.5 | 1476 |
| queue: job turnaround, submitted to done, mean (s) | 135.6 | 1159 | 164.1 | 1159 |
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
| worker nodes in service, mean | 12 | 6.551 | −45.4% | −6.0910 to −4.8076 | yes: GAIN |
| node-hours | 5.027 | 2.744 | −45.4% | −2.5566 to −2.0080 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 504.5 | +0.0% | −1.0724 to +1.3958 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 333.4 | −33.9% | −191.8480 to −150.1203 | yes: GAIN |
| response time (ms), mean | 108.9 | 65.96 | −39.4% | −54.2480 to −31.6531 | yes: GAIN |
| response time (ms), 95th percentile | 150 | 88.11 | −41.3% | −79.3474 to −44.4766 | yes: GAIN |
| response time (ms), 99th percentile | 168.8 | 115.2 | −31.8% | −70.8652 to −36.3538 | yes: GAIN |
| time over the response line (% of samples) | 0.003802 | 0.003656 | −3.8% | −0.0005 to +0.0002 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.100 (native is 0) | +27.6848 to +36.5152 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.195 | +0.195 (native is 0) | −0.1346 to +0.5246 | no |
| utilisation (used / allocatable) | 0.005655 | 0.008715 | +54.1% | +0.0026 to +0.0035 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2714 | 0.2293 | −15.5% | −0.0563 to −0.0279 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0287 | +0.029 (native is 0) | +0.0247 to +0.0327 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2714 | 0.258 | −4.9% | −0.0292 to +0.0024 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4544 | 3586 | −21.1% | −1078.9253 to −838.5233 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.199 | 4.513 | +7.5% | −0.0604 to +0.6888 | no |
| pods started | 0.7 | 2.3 | +228.6% | −0.1260 to +3.3260 | no |
| pod start wait, total (s) | 1.1 | 3.9 | +254.5% | −0.3954 to +5.9954 | no |
| pod start wait, mean (s) | 0.575 | 1.469 | +155.5% | +0.2725 to +1.5156 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 14 | 16.44 | +17.5% | +1.7885 to +3.0994 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1506 | +0.1% | −2.8161 to +4.6161 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1159 | +0.1% | −2.9791 to +4.5624 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1476 | +0.1% | −2.9820 to +4.5820 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1159 | +0.1% | −2.9791 to +4.5624 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.026 | 5.027 | +0.0% | −0.0098 to +0.0111 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 523.7 | 504.4 | −3.7% | −23.5861 to −15.1460 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.7 | 504.4 | −3.7% | −23.5861 to −15.1460 | yes: GAIN |
| response time (ms), mean | 460.7 | 108.9 | −76.4% | −663.5333 to −39.9564 | yes: GAIN |
| response time (ms), 95th percentile | 1742 | 150 | −91.4% | −3050.7631 to −133.6939 | yes: GAIN |
| response time (ms), 99th percentile | 2333 | 168.8 | −92.8% | −4068.9855 to −260.0035 | yes: GAIN |
| time over the response line (% of samples) | 15.78 | 0.003802 | −100.0% | −27.1925 to −4.3537 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | −100.0% | −14.8310 to −3.7690 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 0 | −100.0% | −19.4076 to −5.1690 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03205 | 0.005655 | −82.4% | −0.0311 to −0.0217 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.538 | 0.2714 | −82.4% | −1.4938 to −1.0397 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.538 | 0.2714 | −82.4% | −1.4938 to −1.0397 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853.7 | 4544 | +432.3% | +3292.1586 to +4089.2279 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.867 | 4.199 | +8.6% | +0.1298 to +0.5342 | yes: power given |
| pods started | 0.1 | 0.7 | +600.0% | −0.3048 to +1.5048 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.6617 to +2.4617 | no |
| pod start wait, mean (s) | 0.2 | 0.575 | +187.5% | −0.0809 to +0.8309 | no |
| host CPU busy, the real machine under kind (%) | 47.27 | 14 | −70.4% | −39.4497 to −27.0866 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 827.6 | 1505 | +81.9% | +571.5049 to +783.2951 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1159 | +1986064.3% | +1155.3448 to +1161.7302 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1475 | +368575.0% | +1471.1903 to +1477.4097 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 135.6 | 1159 | +754.4% | +918.0753 to +1127.9247 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.717 | −19.0% | −4.0130 to −0.5537 | yes: GAIN |
| node-hours | 5.026 | 4.069 | −19.0% | −1.6750 to −0.2398 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.7 | 524.2 | +0.1% | −1.2174 to +2.0863 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.7 | 452.3 | −13.6% | −124.9976 to −17.8918 | yes: GAIN |
| response time (ms), mean | 460.7 | 511.6 | +11.1% | −9.6208 to +111.5716 | no |
| response time (ms), 95th percentile | 1742 | 2077 | +19.2% | +81.0222 to +588.7478 | yes: LOSS |
| response time (ms), 99th percentile | 2333 | 2765 | +18.5% | +84.3839 to +779.9533 | yes: LOSS |
| time over the response line (% of samples) | 15.78 | 19.08 | +20.9% | +1.5324 to +5.0773 | yes: LOSS |
| failed requests (%) | 0 | 0.01581 | +0.016 (native is 0) | −0.0200 to +0.0516 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 10.3 | +10.8% | −0.0663 to +2.0663 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 172.9 | +172.900 (native is 0) | +90.2784 to +255.5216 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 15.38 | +25.1% | −3.6647 to +9.8414 | no |
| utilisation (used / allocatable) | 0.03205 | 0.03996 | +24.7% | +0.0020 to +0.0139 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.538 | 1.539 | +0.0% | −0.0396 to +0.0405 | no |
| Omni's own CPU (cores), mean | 0 | 0.05143 | +0.051 (native is 0) | +0.0454 to +0.0574 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.538 | 1.59 | +3.4% | +0.0104 to +0.0934 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853.7 | 714.2 | −16.3% | −249.7322 to −29.4103 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.867 | 4.65 | +20.2% | +0.3618 to +1.2036 | yes: power given |
| pods started | 0.1 | 2.2 | +2100.0% | +0.3333 to +3.8667 | yes: power given |
| pod start wait, total (s) | 0.2 | 5.8 | +2800.0% | +0.4839 to +10.7161 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.285 | +542.5% | −0.1726 to +2.3426 | no |
| host CPU busy, the real machine under kind (%) | 47.27 | 52.6 | +11.3% | +4.2068 to +6.4516 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 827.6 | 858.7 | +3.8% | +4.9623 to +57.2377 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 8.354 | −30.4% | −6.1766 to −1.1146 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 0.0625 | +7.1% | −0.0367 to +0.0450 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 135.6 | 164.1 | +21.0% | +6.9070 to +50.1764 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.717 | −19.0% | −4.0130 to −0.5537 | yes: GAIN |
| node-hours | 5.027 | 4.069 | −19.1% | −1.6814 to −0.2347 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 524.2 | +3.9% | +16.5712 to +23.0299 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 452.3 | −10.3% | −109.3155 to +5.1583 | no |
| response time (ms), mean | 108.9 | 511.6 | +369.8% | +32.1479 to +773.2926 | yes: LOSS |
| response time (ms), 95th percentile | 150 | 2077 | +1284.5% | +230.7517 to +3623.4753 | yes: LOSS |
| response time (ms), 99th percentile | 168.8 | 2765 | +1538.3% | +353.8612 to +4839.4650 | yes: LOSS |
| time over the response line (% of samples) | 0.003802 | 19.08 | +501749.4% | +6.7014 to +31.4544 | yes: LOSS |
| failed requests (%) | 0 | 0.01581 | +0.016 (native is 0) | −0.0200 to +0.0516 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.3 | +10.300 (native is 0) | +4.6773 to +15.9227 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 172.9 | +172.900 (native is 0) | +90.2784 to +255.5216 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 15.38 | +15.377 (native is 0) | +4.0579 to +26.6954 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.005655 | 0.03996 | +606.7% | +0.0310 to +0.0376 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2714 | 1.539 | +466.9% | +1.0280 to +1.5064 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05143 | +0.051 (native is 0) | +0.0454 to +0.0574 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2714 | 1.59 | +485.8% | +1.0742 to +1.5631 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4544 | 714.2 | −84.3% | −4322.4961 to −3338.0330 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.199 | 4.65 | +10.7% | +0.0301 to +0.8714 | yes: power given |
| pods started | 0.7 | 2.2 | +214.3% | −0.2276 to +3.2276 | no |
| pod start wait, total (s) | 1.1 | 5.8 | +427.3% | −0.4587 to +9.8587 | no |
| pod start wait, mean (s) | 0.575 | 1.285 | +123.5% | −0.5032 to +1.9232 | no |
| host CPU busy, the real machine under kind (%) | 14 | 52.6 | +275.7% | +31.4972 to +45.6975 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 858.7 | −42.9% | −777.3391 to −515.2609 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.0625 | −100.0% | −1161.7409 to −1155.3257 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.5 | −100.0% | −1477.5347 to −1470.8653 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 164.1 | −85.8% | −1119.4274 to −869.4892 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.551 | −45.4% | −6.0910 to −4.8076 | yes: GAIN |
| node-hours | 5.026 | 2.744 | −45.4% | −2.5525 to −2.0107 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 523.7 | 504.5 | −3.7% | −22.5362 to −15.8726 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 523.7 | 333.4 | −36.3% | −209.4663 to −171.2341 | yes: GAIN |
| response time (ms), mean | 460.7 | 65.96 | −85.7% | −714.7014 to −74.6894 | yes: GAIN |
| response time (ms), 95th percentile | 1742 | 88.11 | −94.9% | −3119.7903 to −188.4907 | yes: GAIN |
| response time (ms), 99th percentile | 2333 | 115.2 | −95.1% | −4124.0419 to −312.1661 | yes: GAIN |
| time over the response line (% of samples) | 15.78 | 0.003656 | −100.0% | −27.1928 to −4.3536 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 0 | −100.0% | −14.8310 to −3.7690 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.1 | +32.100 (native is 0) | +27.6848 to +36.5152 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.29 | 0.195 | −98.4% | −19.0210 to −5.1657 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03205 | 0.008715 | −72.8% | −0.0278 to −0.0188 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.538 | 0.2293 | −85.1% | −1.5341 to −1.0836 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0287 | +0.029 (native is 0) | +0.0247 to +0.0327 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.538 | 0.258 | −83.2% | −1.5017 to −1.0585 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 853.7 | 3586 | +320.0% | +2412.3985 to +3051.5395 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.867 | 4.513 | +16.7% | +0.2831 to +1.0093 | yes: power given |
| pods started | 0.1 | 2.3 | +2200.0% | +0.8179 to +3.5821 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.9 | +1850.0% | +1.0438 to +6.3562 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.469 | +634.5% | +0.6440 to +1.8941 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.27 | 16.44 | −65.2% | −36.5447 to −25.1036 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 827.6 | 1506 | +82.0% | +573.4121 to +783.1879 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05833 | 1159 | +1987421.4% | +1156.6066 to +1162.0518 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1476 | +368775.0% | +1472.5665 to +1477.6335 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 135.6 | 1159 | +755.0% | +920.0889 to +1127.4945 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*