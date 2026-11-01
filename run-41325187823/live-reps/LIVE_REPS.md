# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.843 | 6 |
| node-hours | 2.515 | 2.511 | 2.029 | 2.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 | 271.9 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.8 | 235.5 | 272.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 324.2 | 128.3 | 291.2 | 101 |
| response time (ms), 95th percentile | 1145 | 226.2 | 1179 | 227.5 |
| response time (ms), 99th percentile | 1631 | 325.1 | 1684 | 351.3 |
| time over the response line (% of samples) | 13.76 | 0.2075 | 13.48 | 0.3739 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 0 | 8.3 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 40.3 | 15.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 1106 | 9.518 | 1168 |
| utilisation (used / allocatable) | 0.05865 | 0.0603 | 0.07368 | 0.06024 |
| CPU used (cores), mean | 1.408 | 1.447 | 1.399 | 1.446 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.01692 | 0.01202 |
| CPU used with Omni's own (cores), mean | 1.408 | 1.447 | 1.416 | 1.458 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.8 | 449.1 | 402.5 | 449.4 |
| HPA replicas, mean | 2.045 | 1.999 | 2.041 | 2.027 |
| pods started | 0 | 0.1 | 0.2 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 | 0.3 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 | 0.3 | 0.2 |
| host CPU busy, the real machine under kind (%) | 40.41 | 44.97 | 41.31 | 45.21 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 773.2 | 1453 | 774.6 | 1479 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.041 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 151.1 | 0.05 | 154.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 696.2 | 0.3 | 651 |
| queue: job turnaround, submitted to done, mean (s) | 79.41 | 798.3 | 79.42 | 862.4 |
| queue: jobs unfinished at the window's end | 0 | 9.9 | 0 | 10 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.517 | +0.2% | +0.0012 to +0.0101 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.4 | +0.2% | −0.2606 to +1.5091 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 272.4 | +0.2% | −0.2606 to +1.5091 | no |
| response time (ms), mean | 128.3 | 101 | −21.3% | −36.1051 to −18.5855 | yes: GAIN |
| response time (ms), 95th percentile | 226.2 | 227.5 | +0.6% | −10.8518 to +13.3538 | no |
| response time (ms), 99th percentile | 325.1 | 351.3 | +8.1% | −1.6327 to +54.0713 | no |
| time over the response line (% of samples) | 0.2075 | 0.3739 | +80.2% | −0.0510 to +0.3839 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.4 | +15.400 (native is 0) | +9.7254 to +21.0746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1106 | 1168 | +5.6% | −12.8952 to +137.7252 | no |
| utilisation (used / allocatable) | 0.0603 | 0.06024 | −0.1% | −0.0017 to +0.0016 | no |
| CPU used (cores), mean | 1.447 | 1.446 | −0.1% | −0.0420 to +0.0391 | no |
| Omni's own CPU (cores), mean | 0 | 0.01202 | +0.012 (native is 0) | +0.0104 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.447 | 1.458 | +0.7% | −0.0295 to +0.0508 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.1 | 449.4 | +0.1% | −11.0671 to +11.7593 | no |
| HPA replicas, mean | 1.999 | 2.027 | +1.4% | −0.1575 to +0.2135 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.6744 to +0.6744 | no |
| host CPU busy, the real machine under kind (%) | 44.97 | 45.21 | +0.5% | −0.5617 to +1.0349 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1453 | 1479 | +1.7% | −29.3886 to +80.1886 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 151.1 | 154.6 | +2.3% | −25.5374 to +32.5041 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696.2 | 651 | −6.5% | −270.0965 to +179.6965 | no |
| queue: job turnaround, submitted to done, mean (s) | 798.3 | 862.4 | +8.0% | +2.0274 to +126.3309 | yes: LOSS |
| queue: jobs unfinished at the window's end | 9.9 | 10 | +1.0% | −1.3871 to +1.5871 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.511 | −0.1% | −0.0134 to +0.0060 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.8 | −0.1% | −2.5298 to +2.1365 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.8 | −0.1% | −2.5298 to +2.1365 | no |
| response time (ms), mean | 324.2 | 128.3 | −60.4% | −342.6760 to −49.1146 | yes: GAIN |
| response time (ms), 95th percentile | 1145 | 226.2 | −80.2% | −1609.7057 to −228.5003 | yes: GAIN |
| response time (ms), 99th percentile | 1631 | 325.1 | −80.1% | −2293.3688 to −319.3974 | yes: GAIN |
| time over the response line (% of samples) | 13.76 | 0.2075 | −98.5% | −24.5251 to −2.5817 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 0 | −100.0% | −12.4297 to −3.3703 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 1106 | +10638.5% | +843.1357 to +1347.6876 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05865 | 0.0603 | +2.8% | −0.0050 to +0.0083 | no |
| CPU used (cores), mean | 1.408 | 1.447 | +2.8% | −0.1190 to +0.1982 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.408 | 1.447 | +2.8% | −0.1190 to +0.1982 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.8 | 449.1 | −4.8% | −70.4104 to +24.9052 | no |
| HPA replicas, mean | 2.045 | 1.999 | −2.3% | −0.1871 to +0.0947 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.41 | 44.97 | +11.3% | +1.0971 to +8.0327 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.2 | 1453 | +87.9% | +609.9048 to +750.0952 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 151.1 | +241706.7% | +111.1952 to +190.9381 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 696.2 | +173950.0% | +530.9094 to +860.6906 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.41 | 798.3 | +905.3% | +592.9320 to +844.7680 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 9.9 | +9.900 (native is 0) | +3.9875 to +15.8125 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.843 | −19.3% | −2.0033 to −0.3114 | yes: GAIN |
| node-hours | 2.515 | 2.029 | −19.3% | −0.8408 to −0.1296 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.9 | −0.0% | −1.2030 to +1.0978 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 235.5 | −13.4% | −63.2882 to −9.5962 | yes: GAIN |
| response time (ms), mean | 324.2 | 291.2 | −10.2% | −48.6810 to −17.2459 | yes: GAIN |
| response time (ms), 95th percentile | 1145 | 1179 | +3.0% | −51.9561 to +120.0781 | no |
| response time (ms), 99th percentile | 1631 | 1684 | +3.2% | −65.7313 to +170.6829 | no |
| time over the response line (% of samples) | 13.76 | 13.48 | −2.0% | −0.9235 to +0.3676 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.3 | +5.1% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.3 | +40.300 (native is 0) | +17.2689 to +63.3311 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 9.518 | −7.6% | −2.6801 to +1.1234 | no |
| utilisation (used / allocatable) | 0.05865 | 0.07368 | +25.6% | +0.0040 to +0.0261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.408 | 1.399 | −0.6% | −0.0298 to +0.0133 | no |
| Omni's own CPU (cores), mean | 0 | 0.01692 | +0.017 (native is 0) | +0.0152 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.408 | 1.416 | +0.6% | −0.0132 to +0.0305 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.8 | 402.5 | −14.7% | −120.1443 to −18.5079 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.045 | 2.041 | −0.2% | −0.2318 to +0.2233 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 40.41 | 41.31 | +2.2% | +0.5287 to +1.2790 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.2 | 774.6 | +0.2% | −1.6385 to +4.4385 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.041 | −32.7% | −3.3247 to −0.5937 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.05 | −20.0% | −0.0670 to +0.0420 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.41 | 79.42 | +0.0% | −2.0754 to +2.1087 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.843 | −19.3% | −2.0033 to −0.3114 | yes: GAIN |
| node-hours | 2.511 | 2.029 | −19.2% | −0.8357 to −0.1274 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.9 | +0.1% | −2.3976 to +2.6856 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 235.5 | −13.3% | −64.8095 to −7.6817 | yes: GAIN |
| response time (ms), mean | 128.3 | 291.2 | +127.0% | +23.7791 to +302.0845 | yes: LOSS |
| response time (ms), 95th percentile | 226.2 | 1179 | +421.3% | +246.9624 to +1659.3656 | yes: LOSS |
| response time (ms), 99th percentile | 325.1 | 1684 | +418.0% | +353.2269 to +2364.4909 | yes: LOSS |
| time over the response line (% of samples) | 0.2075 | 13.48 | +6399.1% | +2.7969 to +23.7541 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 8.3 | +8.300 (native is 0) | +4.0608 to +12.5392 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.3 | +40.300 (native is 0) | +17.2689 to +63.3311 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1106 | 9.518 | −99.1% | −1349.3365 to −843.0435 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.0603 | 0.07368 | +22.2% | +0.0067 to +0.0200 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.447 | 1.399 | −3.3% | −0.2132 to +0.1175 | no |
| Omni's own CPU (cores), mean | 0 | 0.01692 | +0.017 (native is 0) | +0.0152 to +0.0187 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.447 | 1.416 | −2.1% | −0.1969 to +0.1351 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.1 | 402.5 | −10.4% | −69.9391 to −23.2080 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.999 | 2.041 | +2.1% | −0.1405 to +0.2245 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| pod start wait, mean (s) | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 44.97 | 41.31 | −8.1% | −6.9875 to −0.3347 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1453 | 774.6 | −46.7% | −749.0110 to −608.1890 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.007 | −66.6% | −4.0225 to −3.9639 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 151.1 | 0.05 | −100.0% | −190.9616 to −111.1967 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696.2 | 0.3 | −100.0% | −860.8815 to −530.9185 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 798.3 | 79.43 | −90.1% | −844.9191 to −592.7475 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.9 | 0 | −100.0% | −15.8125 to −3.9875 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.517 | +0.1% | −0.0058 to +0.0098 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.4 | +0.2% | −1.8404 to +2.6957 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272.4 | +0.2% | −1.8404 to +2.6957 | no |
| response time (ms), mean | 324.2 | 101 | −68.9% | −374.0966 to −72.3846 | yes: GAIN |
| response time (ms), 95th percentile | 1145 | 227.5 | −80.1% | −1610.9999 to −224.7041 | yes: GAIN |
| response time (ms), 99th percentile | 1631 | 351.3 | −78.5% | −2262.9978 to −297.3298 | yes: GAIN |
| time over the response line (% of samples) | 13.76 | 0.3739 | −97.3% | −24.2475 to −2.5265 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 0.1 | −98.7% | −12.2582 to −3.3418 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.4 | +15.400 (native is 0) | +9.7254 to +21.0746 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.3 | 1168 | +11244.7% | +934.8120 to +1380.8413 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05865 | 0.06024 | +2.7% | −0.0053 to +0.0084 | no |
| CPU used (cores), mean | 1.408 | 1.446 | +2.7% | −0.1262 to +0.2025 | no |
| Omni's own CPU (cores), mean | 0 | 0.01202 | +0.012 (native is 0) | +0.0104 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.408 | 1.458 | +3.6% | −0.1127 to +0.2131 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.8 | 449.4 | −4.7% | −71.6577 to +26.8448 | no |
| HPA replicas, mean | 2.045 | 2.027 | −0.9% | −0.2183 to +0.1818 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 40.41 | 45.21 | +11.9% | +1.0679 to +8.5351 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.2 | 1479 | +91.2% | +653.5029 to +757.2971 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 154.6 | +247280.0% | +101.9348 to +207.1652 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 651 | +162650.0% | +475.8674 to +825.3326 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 79.41 | 862.4 | +986.1% | +698.6257 to +867.4327 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10 | +10.000 (native is 0) | +4.1595 to +15.8405 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*