# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 10.68 | 6.213 |
| node-hours | 5.028 | 5.026 | 4.474 | 2.607 |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.4 | 526.6 | 505.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 504.4 | 485.1 | 323.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 599.8 | 124.8 | 699.6 | 74.22 |
| response time (ms), 95th percentile | 2294 | 172.6 | 2818 | 97.29 |
| response time (ms), 99th percentile | 3049 | 191.4 | 3714 | 124.4 |
| time over the response line (% of samples) | 24.7 | 0 | 28.41 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.9 | 0 | 14.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 80.3 | 33.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 6.923 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.17 | 0 | 29.07 | 0.1333 |
| utilisation (used / allocatable) | 0.03505 | 0.006095 | 0.04031 | 0.00994 |
| CPU used (cores), mean | 1.682 | 0.2926 | 1.713 | 0.2472 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05488 | 0.03133 |
| CPU used with Omni's own (cores), mean | 1.682 | 0.2926 | 1.768 | 0.2786 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.1 | 4162 | 682.2 | 3166 |
| HPA replicas, mean | 3.984 | 4.116 | 4.713 | 4.56 |
| pods started | 0.2 | 0.5 | 2.5 | 1.6 |
| pod start wait, total (s) | 0.4 | 0.6 | 5.8 | 2.6 |
| pod start wait, mean (s) | 0.2 | 0.6 | 1.583 | 0.9083 |
| host CPU busy, the real machine under kind (%) | 52.16 | 15.21 | 57.82 | 18.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 871.3 | 1506 | 921.2 | 1508 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 9.429 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 1159 | 0.1542 | 1161 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1475 | 0.9 | 1477 |
| queue: job turnaround, submitted to done, mean (s) | 181.8 | 1159 | 227 | 1161 |
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
| worker nodes in service, mean | 12 | 6.213 | −48.2% | −5.9740 to −5.6002 | yes: GAIN |
| node-hours | 5.026 | 2.607 | −48.1% | −2.4976 to −2.3400 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 505.6 | +0.2% | +0.6057 to +1.7262 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 323.5 | −35.9% | −186.9207 to −174.9724 | yes: GAIN |
| response time (ms), mean | 124.8 | 74.22 | −40.5% | −57.6524 to −43.4072 | yes: GAIN |
| response time (ms), 95th percentile | 172.6 | 97.29 | −43.6% | −87.4815 to −63.1335 | yes: GAIN |
| response time (ms), 99th percentile | 191.4 | 124.4 | −35.0% | −74.7111 to −59.2209 | yes: GAIN |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.4 | +33.400 (native is 0) | +31.8845 to +34.9155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.1333 | +0.133 (native is 0) | −0.0727 to +0.3394 | no |
| utilisation (used / allocatable) | 0.006095 | 0.00994 | +63.1% | +0.0034 to +0.0042 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2926 | 0.2472 | −15.5% | −0.0512 to −0.0395 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03133 | +0.031 (native is 0) | +0.0280 to +0.0347 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2926 | 0.2786 | −4.8% | −0.0210 to −0.0070 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4162 | 3166 | −23.9% | −1082.0971 to −910.2736 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.116 | 4.56 | +10.8% | +0.2214 to +0.6668 | yes: power given |
| pods started | 0.5 | 1.6 | +220.0% | −0.2676 to +2.4676 | no |
| pod start wait, total (s) | 0.6 | 2.6 | +333.3% | −0.4779 to +4.4779 | no |
| pod start wait, mean (s) | 0.6 | 0.9083 | +51.4% | −0.5882 to +1.2049 | no |
| host CPU busy, the real machine under kind (%) | 15.21 | 18.11 | +19.1% | +2.2879 to +3.5183 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1508 | +0.1% | +0.0463 to +3.3537 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 1161 | +0.1% | −0.0537 to +3.4704 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 1477 | +0.1% | −0.0859 to +3.4859 | no |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 1161 | +0.1% | −0.0537 to +3.4704 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.028 | 5.026 | −0.1% | −0.0179 to +0.0125 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 504.4 | −4.1% | −24.0041 to −19.0198 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 504.4 | −4.1% | −24.0041 to −19.0198 | yes: GAIN |
| response time (ms), mean | 599.8 | 124.8 | −79.2% | −768.3169 to −181.8098 | yes: GAIN |
| response time (ms), 95th percentile | 2294 | 172.6 | −92.5% | −3465.0379 to −777.2631 | yes: GAIN |
| response time (ms), 99th percentile | 3049 | 191.4 | −93.7% | −4656.5227 to −1059.0441 | yes: GAIN |
| time over the response line (% of samples) | 24.7 | 0 | −100.0% | −33.5891 to −15.8176 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.9 | 0 | −100.0% | −16.4558 to −11.3442 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.17 | 0 | −100.0% | −28.9328 to −5.4006 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.006095 | −82.6% | −0.0321 to −0.0258 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.682 | 0.2926 | −82.6% | −1.5398 to −1.2395 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.682 | 0.2926 | −82.6% | −1.5398 to −1.2395 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.1 | 4162 | +449.1% | +3120.0481 to +3688.4324 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.984 | 4.116 | +3.3% | −0.0392 to +0.3035 | no |
| pods started | 0.2 | 0.5 | +150.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −0.7417 to +1.1417 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | −0.2032 to +1.0032 | no |
| host CPU busy, the real machine under kind (%) | 52.16 | 15.21 | −70.8% | −41.6781 to −32.2295 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 871.3 | 1506 | +72.8% | +532.2368 to +736.9632 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 1159 | +1030337.0% | +1157.7093 to +1160.5490 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1475 | +210671.4% | +1473.3491 to +1476.0509 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 181.8 | 1159 | +537.6% | +877.6203 to +1077.2380 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.68 | −11.0% | −2.4337 to −0.2093 | yes: GAIN |
| node-hours | 5.028 | 4.474 | −11.0% | −1.0199 to −0.0897 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 526.6 | +0.1% | −1.1333 to +2.5746 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 485.1 | −7.8% | −76.0605 to −5.5691 | yes: GAIN |
| response time (ms), mean | 599.8 | 699.6 | +16.6% | −11.9176 to +211.5504 | no |
| response time (ms), 95th percentile | 2294 | 2818 | +22.9% | +95.1458 to +954.1462 | yes: LOSS |
| response time (ms), 99th percentile | 3049 | 3714 | +21.8% | +191.6458 to +1138.7508 | yes: LOSS |
| time over the response line (% of samples) | 24.7 | 28.41 | +15.0% | +1.5448 to +5.8678 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.9 | 14.4 | +3.6% | −0.8168 to +1.8168 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.3 | +80.300 (native is 0) | +44.8122 to +115.7878 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.17 | 29.07 | +69.3% | +0.8774 to +22.9326 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.04031 | +15.0% | +0.0014 to +0.0091 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.682 | 1.713 | +1.8% | −0.0347 to +0.0966 | no |
| Omni's own CPU (cores), mean | 0 | 0.05488 | +0.055 (native is 0) | +0.0494 to +0.0603 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.682 | 1.768 | +5.1% | +0.0187 to +0.1530 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.1 | 682.2 | −10.0% | −125.5892 to −26.2261 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.984 | 4.713 | +18.3% | +0.4058 to +1.0518 | yes: power given |
| pods started | 0.2 | 2.5 | +1150.0% | +0.5462 to +4.0538 | yes: power given |
| pod start wait, total (s) | 0.4 | 5.8 | +1350.0% | +1.1857 to +9.6143 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.583 | +691.7% | +0.2681 to +2.4986 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 52.16 | 57.82 | +10.8% | +3.9501 to +7.3588 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 871.3 | 921.2 | +5.7% | +13.5005 to +86.2995 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 9.429 | −21.4% | −4.4001 to −0.7418 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.1542 | +37.0% | −0.0340 to +0.1173 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.2524 to +0.6524 | no |
| queue: job turnaround, submitted to done, mean (s) | 181.8 | 227 | +24.8% | +11.0183 to +79.3400 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 10.68 | −11.0% | −2.4337 to −0.2093 | yes: GAIN |
| node-hours | 5.026 | 4.474 | −11.0% | −1.0133 to −0.0910 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 526.6 | +4.4% | +19.6343 to +24.8308 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 485.1 | −3.8% | −55.7978 to +17.1921 | no |
| response time (ms), mean | 124.8 | 699.6 | +460.8% | +179.2408 to +970.5186 | yes: LOSS |
| response time (ms), 95th percentile | 172.6 | 2818 | +1532.9% | +899.7967 to +4391.7963 | yes: LOSS |
| response time (ms), 99th percentile | 191.4 | 3714 | +1840.9% | +1301.4588 to +5744.5046 | yes: LOSS |
| time over the response line (% of samples) | 0 | 28.41 | +28.410 (native is 0) | +18.6130 to +38.2062 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 14.4 | +14.400 (native is 0) | +10.5672 to +18.2328 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.3 | +80.300 (native is 0) | +44.8122 to +115.7878 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 29.07 | +29.072 (native is 0) | +7.5944 to +50.5489 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.006095 | 0.04031 | +561.4% | +0.0310 to +0.0374 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2926 | 1.713 | +485.6% | +1.2414 to +1.5998 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05488 | +0.055 (native is 0) | +0.0494 to +0.0603 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2926 | 1.768 | +504.3% | +1.2917 to +1.6593 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4162 | 682.2 | −83.6% | −3810.3310 to −3149.9647 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.116 | 4.713 | +14.5% | +0.3066 to +0.8867 | yes: power given |
| pods started | 0.5 | 2.5 | +400.0% | +0.4920 to +3.5080 | yes: power given |
| pod start wait, total (s) | 0.6 | 5.8 | +866.7% | +1.3880 to +9.0120 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.583 | +163.9% | +0.0647 to +1.9020 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 15.21 | 57.82 | +280.1% | +36.2501 to +48.9665 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 921.2 | −38.8% | −722.1060 to −447.2940 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1159 | 0.1542 | −100.0% | −1160.5314 to −1157.6436 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1475 | 0.9 | −99.9% | −1475.9795 to −1473.0205 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1159 | 227 | −80.4% | −1064.7324 to −799.7676 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.213 | −48.2% | −5.9740 to −5.6002 | yes: GAIN |
| node-hours | 5.028 | 2.607 | −48.2% | −2.4959 to −2.3471 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 525.9 | 505.6 | −3.9% | −22.6853 to −18.0067 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 525.9 | 323.5 | −38.5% | −206.8979 to −198.0191 | yes: GAIN |
| response time (ms), mean | 599.8 | 74.22 | −87.6% | −823.8035 to −227.3827 | yes: GAIN |
| response time (ms), 95th percentile | 2294 | 97.29 | −95.8% | −3541.0708 to −851.8452 | yes: GAIN |
| response time (ms), 99th percentile | 3049 | 124.4 | −95.9% | −4721.4692 to −1128.0296 | yes: GAIN |
| time over the response line (% of samples) | 24.7 | 0 | −100.0% | −33.5891 to −15.8176 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13.9 | 0 | −100.0% | −16.4558 to −11.3442 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.4 | +33.400 (native is 0) | +31.8845 to +34.9155 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.17 | 0.1333 | −99.2% | −28.7821 to −5.2846 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03505 | 0.00994 | −71.6% | −0.0280 to −0.0222 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.682 | 0.2472 | −85.3% | −1.5847 to −1.2853 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03133 | +0.031 (native is 0) | +0.0280 to +0.0347 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.682 | 0.2786 | −83.4% | −1.5503 to −1.2570 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 758.1 | 3166 | +317.6% | +2154.2748 to +2661.8350 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.984 | 4.56 | +14.5% | +0.3482 to +0.8042 | yes: power given |
| pods started | 0.2 | 1.6 | +700.0% | +0.0015 to +2.7985 | yes: power given |
| pod start wait, total (s) | 0.4 | 2.6 | +550.0% | −0.4293 to +4.8293 | no |
| pod start wait, mean (s) | 0.2 | 0.9083 | +354.2% | −0.1861 to +1.6028 | no |
| host CPU busy, the real machine under kind (%) | 52.16 | 18.11 | −65.3% | −38.2600 to −29.8414 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 871.3 | 1508 | +73.0% | +534.8456 to +737.7544 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 1161 | +1031855.6% | +1159.4900 to +1162.1850 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 1477 | +210914.3% | +1474.9615 to +1477.8385 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 181.8 | 1161 | +538.5% | +880.2445 to +1078.0305 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*