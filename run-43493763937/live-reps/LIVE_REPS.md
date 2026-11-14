# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.171 | 5.287 |
| node-hours | 2.512 | 2.517 | 2.169 | 2.215 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 275.1 | 275.3 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 275.1 | 249.2 | 252.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 475.8 | 406.6 | 481.5 | 406.8 |
| response time (ms), 95th percentile | 1805 | 1625 | 2010 | 1887 |
| response time (ms), 99th percentile | 2449 | 2522 | 2769 | 2808 |
| time over the response line (% of samples) | 21.77 | 16.26 | 22.95 | 16.69 |
| failed requests (%) | 0.02286 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 9.8 | 11.5 | 10.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 89.6 | 83.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 55 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 21.51 | 21.15 | 27.67 |
| utilisation (used / allocatable) | 0.06597 | 0.0666 | 0.07882 | 0.0769 |
| CPU used (cores), mean | 1.583 | 1.598 | 1.604 | 1.61 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07698 | 0.07923 |
| CPU used with Omni's own (cores), mean | 1.583 | 1.598 | 1.681 | 1.689 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.2 | 419.2 | 371.5 | 376.2 |
| HPA replicas, mean | 1.924 | 2.101 | 2.275 | 2.223 |
| pods started | 0.1 | 0.2 | 1.4 | 1 |
| pod start wait, total (s) | 0.2 | 0.6 | 3.4 | 2 |
| pod start wait, mean (s) | 0.2 | 0.6 | 1.425 | 1.425 |
| host CPU busy, the real machine under kind (%) | 45.32 | 46.56 | 48.96 | 49.92 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 829.9 | 848.5 | 851 | 861.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.695 | 4.79 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.9125 | 0.5417 | 1.137 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.1 | 3 | 3.2 |
| queue: job turnaround, submitted to done, mean (s) | 134.5 | 159.4 | 155 | 172.2 |
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
| worker nodes in service, mean | 6 | 5.287 | −11.9% | −1.4452 to +0.0187 | no |
| node-hours | 2.517 | 2.215 | −12.0% | −0.6098 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275 | −0.0% | −1.1805 to +1.0998 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 252.7 | −8.1% | −45.8838 to +1.0655 | no |
| response time (ms), mean | 406.6 | 406.8 | +0.0% | −38.7486 to +39.0703 | no |
| response time (ms), 95th percentile | 1625 | 1887 | +16.2% | −14.4109 to +539.7799 | no |
| response time (ms), 99th percentile | 2522 | 2808 | +11.3% | +43.6860 to +527.7946 | yes: LOSS |
| time over the response line (% of samples) | 16.26 | 16.69 | +2.6% | −1.7075 to +2.5662 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 10.7 | +9.2% | −0.1900 to +1.9900 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 83.1 | +83.100 (native is 0) | +16.4237 to +149.7763 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.51 | 27.67 | +28.6% | +4.0093 to +8.3040 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0666 | 0.0769 | +15.5% | +0.0004 to +0.0202 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.598 | 1.61 | +0.7% | −0.0168 to +0.0402 | no |
| Omni's own CPU (cores), mean | 0 | 0.07923 | +0.079 (native is 0) | +0.0729 to +0.0856 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.598 | 1.689 | +5.7% | +0.0573 to +0.1245 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 419.2 | 376.2 | −10.3% | −82.1056 to −3.9659 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.101 | 2.223 | +5.8% | −0.1707 to +0.4163 | no |
| pods started | 0.2 | 1 | +400.0% | −0.2003 to +1.8003 | no |
| pod start wait, total (s) | 0.6 | 2 | +233.3% | −0.4221 to +3.2221 | no |
| pod start wait, mean (s) | 0.6 | 1.425 | +137.5% | −0.6008 to +2.2508 | no |
| host CPU busy, the real machine under kind (%) | 46.56 | 49.92 | +7.2% | +2.7668 to +3.9396 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.5 | 861.5 | +1.5% | +4.8234 to +21.1766 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.79 | −20.2% | −2.3147 to −0.1045 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9125 | 1.137 | +24.7% | −0.0964 to +0.5464 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3.2 | +52.4% | −1.4999 to +3.6999 | no |
| queue: job turnaround, submitted to done, mean (s) | 159.4 | 172.2 | +8.0% | +4.8934 to +20.5649 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.516 | +0.2% | −0.0009 to +0.0105 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 275.1 | +0.3% | +0.0176 to +1.4616 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 275.1 | +0.3% | +0.0176 to +1.4616 | yes: power given |
| response time (ms), mean | 475.8 | 406.6 | −14.5% | −115.4767 to −22.8321 | yes: GAIN |
| response time (ms), 95th percentile | 1805 | 1625 | −10.0% | −383.8340 to +24.0730 | no |
| response time (ms), 99th percentile | 2449 | 2522 | +3.0% | −89.3869 to +236.6469 | no |
| time over the response line (% of samples) | 21.77 | 16.26 | −25.3% | −8.7276 to −2.3074 | yes: GAIN |
| failed requests (%) | 0.02286 | 0 | −100.0% | −0.0746 to +0.0288 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 9.8 | −13.3% | −3.2276 to +0.2276 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 21.51 | +52.5% | +3.0667 to +11.7433 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06597 | 0.0666 | +1.0% | −0.0001 to +0.0013 | no |
| CPU used (cores), mean | 1.583 | 1.598 | +1.0% | −0.0015 to +0.0319 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.583 | 1.598 | +1.0% | −0.0015 to +0.0319 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.2 | 419.2 | −0.9% | −8.6530 to +0.7026 | no |
| HPA replicas, mean | 1.924 | 2.101 | +9.2% | −0.0294 to +0.3827 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.5048 to +1.3048 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | −0.5048 to +1.3048 | no |
| host CPU busy, the real machine under kind (%) | 45.32 | 46.56 | +2.8% | +0.7157 to +1.7769 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 829.9 | 848.5 | +2.2% | +11.2031 to +25.9969 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.9125 | +584.4% | +0.4707 to +1.0876 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.1 | +133.3% | −1.0570 to +3.4570 | no |
| queue: job turnaround, submitted to done, mean (s) | 134.5 | 159.4 | +18.6% | +12.3548 to +37.5619 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.171 | −13.8% | −1.6553 to −0.0020 | yes: GAIN |
| node-hours | 2.512 | 2.169 | −13.6% | −0.6909 to +0.0055 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 275.3 | +0.3% | −0.1775 to +2.0524 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 249.2 | −9.2% | −51.5525 to +1.2940 | no |
| response time (ms), mean | 475.8 | 481.5 | +1.2% | −32.9560 to +44.3197 | no |
| response time (ms), 95th percentile | 1805 | 2010 | +11.4% | +36.2119 to +374.5721 | yes: LOSS |
| response time (ms), 99th percentile | 2449 | 2769 | +13.1% | +119.3558 to +521.2676 | yes: LOSS |
| time over the response line (% of samples) | 21.77 | 22.95 | +5.4% | −1.8354 to +4.1941 | no |
| failed requests (%) | 0.02286 | 0 | −100.0% | −0.0746 to +0.0288 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.5 | +1.8% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +20.7303 to +158.4697 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 21.15 | +49.9% | −3.6480 to +17.7246 | no |
| utilisation (used / allocatable) | 0.06597 | 0.07882 | +19.5% | +0.0010 to +0.0247 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.583 | 1.604 | +1.3% | −0.0223 to +0.0632 | no |
| Omni's own CPU (cores), mean | 0 | 0.07698 | +0.077 (native is 0) | +0.0701 to +0.0838 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.583 | 1.681 | +6.2% | +0.0522 to +0.1426 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.2 | 371.5 | −12.2% | −96.8673 to −6.5177 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.924 | 2.275 | +18.2% | +0.1480 to +0.5539 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.1791 to +2.4209 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.4 | +1600.0% | +0.4440 to +5.9560 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.425 | +612.5% | +0.0678 to +2.3822 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.32 | 48.96 | +8.0% | +2.5114 to +4.7824 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 829.9 | 851 | +2.5% | +2.4823 to +39.7177 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.695 | −21.8% | −2.5215 to −0.0892 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.5417 | +306.2% | −0.2983 to +1.1150 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 3 | +233.3% | −1.7068 to +5.9068 | no |
| queue: job turnaround, submitted to done, mean (s) | 134.5 | 155 | +15.3% | +4.4047 to +36.6703 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.171 | −13.8% | −1.6553 to −0.0020 | yes: GAIN |
| node-hours | 2.517 | 2.169 | −13.8% | −0.6955 to +0.0004 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.3 | +0.1% | −1.0224 to +1.4181 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 249.2 | −9.4% | −52.3129 to +0.5752 | no |
| response time (ms), mean | 406.6 | 481.5 | +18.4% | +25.1398 to +124.5327 | yes: LOSS |
| response time (ms), 95th percentile | 1625 | 2010 | +23.7% | +159.6927 to +610.8523 | yes: LOSS |
| response time (ms), 99th percentile | 2522 | 2769 | +9.8% | +97.6069 to +395.7565 | yes: LOSS |
| time over the response line (% of samples) | 16.26 | 22.95 | +41.2% | +3.2746 to +10.1191 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 11.5 | +17.3% | −0.1790 to +3.5790 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.6 | +89.600 (native is 0) | +20.7303 to +158.4697 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.51 | 21.15 | −1.7% | −9.8148 to +9.0815 | no |
| utilisation (used / allocatable) | 0.0666 | 0.07882 | +18.3% | +0.0003 to +0.0241 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.598 | 1.604 | +0.3% | −0.0334 to +0.0438 | no |
| Omni's own CPU (cores), mean | 0 | 0.07698 | +0.077 (native is 0) | +0.0701 to +0.0838 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.598 | 1.681 | +5.1% | +0.0415 to +0.1229 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 419.2 | 371.5 | −11.4% | −92.8865 to −2.5481 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.101 | 2.275 | +8.3% | −0.0635 to +0.4121 | no |
| pods started | 0.2 | 1.4 | +600.0% | −0.0064 to +2.4064 | no |
| pod start wait, total (s) | 0.6 | 3.4 | +466.7% | −0.3416 to +5.9416 | no |
| pod start wait, mean (s) | 0.6 | 1.425 | +137.5% | −0.8227 to +2.4727 | no |
| host CPU busy, the real machine under kind (%) | 46.56 | 48.96 | +5.2% | +1.4284 to +3.3727 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 848.5 | 851 | +0.3% | −16.2145 to +21.2145 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.695 | −21.8% | −2.5215 to −0.0892 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9125 | 0.5417 | −40.6% | −1.2291 to +0.4874 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3 | +42.9% | −4.2960 to +6.0960 | no |
| queue: job turnaround, submitted to done, mean (s) | 159.4 | 155 | −2.8% | −17.8469 to +9.0052 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.287 | −11.9% | −1.4452 to +0.0187 | no |
| node-hours | 2.512 | 2.215 | −11.8% | −0.6057 to +0.0132 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 275 | +0.3% | −0.3280 to +1.7265 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 252.7 | −7.9% | −45.1786 to +1.8396 | no |
| response time (ms), mean | 475.8 | 406.8 | −14.5% | −98.7938 to −39.1934 | yes: GAIN |
| response time (ms), 95th percentile | 1805 | 1887 | +4.6% | −70.8966 to +236.5046 | no |
| response time (ms), 99th percentile | 2449 | 2808 | +14.7% | +49.0266 to +669.7140 | yes: LOSS |
| time over the response line (% of samples) | 21.77 | 16.69 | −23.4% | −7.9166 to −2.2596 | yes: GAIN |
| failed requests (%) | 0.02286 | 0 | −100.0% | −0.0746 to +0.0288 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 10.7 | −5.3% | −2.0385 to +0.8385 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 83.1 | +83.100 (native is 0) | +16.4237 to +149.7763 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.11 | 27.67 | +96.1% | +7.5846 to +19.5387 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06597 | 0.0769 | +16.6% | +0.0011 to +0.0207 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.583 | 1.61 | +1.7% | −0.0086 to +0.0624 | no |
| Omni's own CPU (cores), mean | 0 | 0.07923 | +0.079 (native is 0) | +0.0729 to +0.0856 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.583 | 1.689 | +6.7% | +0.0660 to +0.1462 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 423.2 | 376.2 | −11.1% | −85.8783 to −8.1436 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.924 | 2.223 | +15.6% | +0.0432 to +0.5557 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | −0.0802 to +1.8802 | no |
| pod start wait, total (s) | 0.2 | 2 | +900.0% | +0.1899 to +3.4101 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.425 | +612.5% | −0.0266 to +2.4766 | no |
| host CPU busy, the real machine under kind (%) | 45.32 | 49.92 | +10.1% | +3.5863 to +5.6126 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 829.9 | 861.5 | +3.8% | +17.6838 to +45.5162 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.79 | −20.2% | −2.3147 to −0.1045 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 1.137 | +753.1% | +0.6997 to +1.3086 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 3.2 | +255.6% | +0.8674 to +3.7326 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 134.5 | 172.2 | +28.0% | +19.6626 to +55.7124 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*