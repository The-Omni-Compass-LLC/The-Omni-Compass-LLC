# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.128 | 5.964 |
| node-hours | 2.514 | 2.522 | 2.153 | 2.499 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | 273.9 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.9 | 246.4 | 269.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 411.3 | 139.9 | 418.3 | 117 |
| response time (ms), 95th percentile | 1524 | 243.3 | 1818 | 263.1 |
| response time (ms), 99th percentile | 2187 | 351.7 | 2559 | 387.7 |
| time over the response line (% of samples) | 19.69 | 0.247 | 19.52 | 0.4613 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 0 | 10.6 | 0.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 116.3 | 112 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.55 | 1166 | 10.81 | 1257 |
| utilisation (used / allocatable) | 0.06131 | 0.05931 | 0.07347 | 0.05715 |
| CPU used (cores), mean | 1.472 | 1.423 | 1.49 | 1.364 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07324 | 0.07261 |
| CPU used with Omni's own (cores), mean | 1.472 | 1.423 | 1.563 | 1.437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 459 | 398.2 | 473.5 |
| HPA replicas, mean | 1.979 | 1.998 | 2.469 | 2.149 |
| pods started | 0 | 0.2 | 2.1 | 0.7 |
| pod start wait, total (s) | 0 | 0.5 | 4.5 | 1.4 |
| pod start wait, mean (s) | 0 | 0.25 | 1.783 | 0.8 |
| host CPU busy, the real machine under kind (%) | 42.12 | 44.9 | 45.6 | 46.27 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 796.4 | 1451 | 815.8 | 1454 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.594 | 5.283 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 155.1 | 0.05 | 219.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 701.4 | 0.3 | 847.7 |
| queue: job turnaround, submitted to done, mean (s) | 103 | 825.6 | 119.9 | 863.1 |
| queue: jobs unfinished at the window's end | 0 | 10.8 | 0 | 12.7 |
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
| worker nodes in service, mean | 6 | 5.964 | −0.6% | −0.1160 to +0.0449 | no |
| node-hours | 2.522 | 2.499 | −0.9% | −0.0572 to +0.0099 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 270.9 | −0.7% | −3.0042 to −0.9416 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 269.8 | −1.1% | −5.2549 to −0.9367 | yes: GAIN |
| response time (ms), mean | 139.9 | 117 | −16.4% | −27.6455 to −18.1228 | yes: GAIN |
| response time (ms), 95th percentile | 243.3 | 263.1 | +8.1% | +3.2609 to +36.3421 | yes: LOSS |
| response time (ms), 99th percentile | 351.7 | 387.7 | +10.2% | +7.1448 to +64.8042 | yes: LOSS |
| time over the response line (% of samples) | 0.247 | 0.4613 | +86.7% | +0.0751 to +0.3534 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112 | +112.000 (native is 0) | +100.1692 to +123.8308 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1166 | 1257 | +7.8% | +45.8518 to +135.5415 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05931 | 0.05715 | −3.6% | −0.0044 to +0.0001 | no |
| CPU used (cores), mean | 1.423 | 1.364 | −4.1% | −0.1047 to −0.0134 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07261 | +0.073 (native is 0) | +0.0636 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.423 | 1.437 | +1.0% | −0.0267 to +0.0539 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 473.5 | +3.2% | −2.5092 to +31.5626 | no |
| HPA replicas, mean | 1.998 | 2.149 | +7.6% | −0.0249 to +0.3280 | no |
| pods started | 0.2 | 0.7 | +250.0% | −0.4079 to +1.4079 | no |
| pod start wait, total (s) | 0.5 | 1.4 | +180.0% | −1.0792 to +2.8792 | no |
| pod start wait, mean (s) | 0.25 | 0.8 | +220.0% | −0.4955 to +1.5955 | no |
| host CPU busy, the real machine under kind (%) | 44.9 | 46.27 | +3.0% | +0.6398 to +2.0901 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1451 | 1454 | +0.2% | −13.6837 to +19.8837 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.283 | −12.0% | −9.8326 to +8.3978 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 155.1 | 219.9 | +41.8% | +16.8252 to +112.8665 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 701.4 | 847.7 | +20.9% | +10.5934 to +282.0066 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 825.6 | 863.1 | +4.5% | −1.8984 to +76.9817 | no |
| queue: jobs unfinished at the window's end | 10.8 | 12.7 | +17.6% | −1.0675 to +4.8675 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.522 | +0.3% | −0.0005 to +0.0175 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 272.9 | −0.0% | −2.4161 to +2.2787 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 272.9 | −0.0% | −2.4161 to +2.2787 | no |
| response time (ms), mean | 411.3 | 139.9 | −66.0% | −421.0764 to −121.7256 | yes: GAIN |
| response time (ms), 95th percentile | 1524 | 243.3 | −84.0% | −1979.7072 to −581.6468 | yes: GAIN |
| response time (ms), 99th percentile | 2187 | 351.7 | −83.9% | −2862.3150 to −807.6290 | yes: GAIN |
| time over the response line (% of samples) | 19.69 | 0.247 | −98.7% | −30.6016 to −8.2786 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 0 | −100.0% | −14.1978 to −5.6022 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.55 | 1166 | +10956.8% | +838.0534 to +1473.8399 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06131 | 0.05931 | −3.3% | −0.0082 to +0.0042 | no |
| CPU used (cores), mean | 1.472 | 1.423 | −3.3% | −0.1961 to +0.0997 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.472 | 1.423 | −3.3% | −0.1961 to +0.0997 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 459 | +0.1% | −46.1614 to +47.3752 | no |
| HPA replicas, mean | 1.979 | 1.998 | +1.0% | −0.0950 to +0.1331 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 42.12 | 44.9 | +6.6% | −0.6531 to +6.2225 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.4 | 1451 | +82.2% | +575.2435 to +733.5565 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 155.1 | +372030.0% | +100.1749 to +209.8501 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 701.4 | +175250.0% | +494.5229 to +907.4771 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 103 | 825.6 | +701.3% | +574.4031 to +870.7219 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.8 | +10.800 (native is 0) | +4.1340 to +17.4660 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.128 | −14.5% | −1.6981 to −0.0452 | yes: GAIN |
| node-hours | 2.514 | 2.153 | −14.4% | −0.7091 to −0.0130 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.9 | +0.3% | +0.2934 to +1.5398 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 246.4 | −9.7% | −52.8688 to −0.3312 | yes: GAIN |
| response time (ms), mean | 411.3 | 418.3 | +1.7% | −16.9328 to +30.8096 | no |
| response time (ms), 95th percentile | 1524 | 1818 | +19.3% | +113.3842 to +474.7218 | yes: LOSS |
| response time (ms), 99th percentile | 2187 | 2559 | +17.0% | +77.6933 to +666.0175 | yes: LOSS |
| time over the response line (% of samples) | 19.69 | 19.52 | −0.9% | −1.0398 to +0.6992 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10.6 | +7.1% | +0.2172 to +1.1828 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.3 | +116.300 (native is 0) | +41.4478 to +191.1522 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.55 | 10.81 | +2.4% | −1.4706 to +1.9873 | no |
| utilisation (used / allocatable) | 0.06131 | 0.07347 | +19.8% | +0.0017 to +0.0226 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.472 | 1.49 | +1.2% | −0.0091 to +0.0454 | no |
| Omni's own CPU (cores), mean | 0 | 0.07324 | +0.073 (native is 0) | +0.0649 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.472 | 1.563 | +6.2% | +0.0571 to +0.1257 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 398.2 | −13.1% | −114.1297 to −6.1354 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.469 | +24.8% | +0.1964 to +0.7842 | yes: power given |
| pods started | 0 | 2.1 | +2.100 (native is 0) | +1.0100 to +3.1900 | yes: power given |
| pod start wait, total (s) | 0 | 4.5 | +4.500 (native is 0) | +2.2068 to +6.7932 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.783 | +1.783 (native is 0) | +1.0526 to +2.5140 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.12 | 45.6 | +8.3% | +2.8104 to +4.1549 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.4 | 815.8 | +2.4% | +7.7376 to +31.0624 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.594 | −23.4% | −2.5571 to −0.2539 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 0.05 | +20.0% | −0.0439 to +0.0605 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.6278 to +0.4278 | no |
| queue: job turnaround, submitted to done, mean (s) | 103 | 119.9 | +16.4% | +6.0923 to +27.6327 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.128 | −14.5% | −1.6981 to −0.0452 | yes: GAIN |
| node-hours | 2.522 | 2.153 | −14.7% | −0.7167 to −0.0224 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 273.9 | +0.4% | −1.4089 to +3.3796 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 246.4 | −9.7% | −54.3006 to +1.2379 | no |
| response time (ms), mean | 139.9 | 418.3 | +198.9% | +110.3723 to +446.3066 | yes: LOSS |
| response time (ms), 95th percentile | 243.3 | 1818 | +647.3% | +708.9027 to +2440.5573 | yes: LOSS |
| response time (ms), 99th percentile | 351.7 | 2559 | +627.5% | +995.6894 to +3417.9654 | yes: LOSS |
| time over the response line (% of samples) | 0.247 | 19.52 | +7800.8% | +8.5978 to +29.9418 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.6 | +10.600 (native is 0) | +6.1880 to +15.0120 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 116.3 | +116.300 (native is 0) | +41.4478 to +191.1522 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1166 | 10.81 | −99.1% | −1472.5136 to −838.8630 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05931 | 0.07347 | +23.9% | +0.0066 to +0.0217 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.423 | 1.49 | +4.7% | −0.1036 to +0.2363 | no |
| Omni's own CPU (cores), mean | 0 | 0.07324 | +0.073 (native is 0) | +0.0649 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.423 | 1.563 | +9.8% | −0.0379 to +0.3171 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459 | 398.2 | −13.2% | −91.5190 to −29.9599 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.469 | +23.6% | +0.1588 to +0.7837 | yes: power given |
| pods started | 0.2 | 2.1 | +950.0% | +0.9198 to +2.8802 | yes: power given |
| pod start wait, total (s) | 0.5 | 4.5 | +800.0% | +2.1531 to +5.8469 | yes: LOSS |
| pod start wait, mean (s) | 0.25 | 1.783 | +613.3% | +0.7271 to +2.3396 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.9 | 45.6 | +1.6% | −3.3282 to +4.7240 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1451 | 815.8 | −43.8% | −712.6159 to −557.3841 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 155.1 | 0.05 | −100.0% | −209.8219 to −100.1864 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 701.4 | 0.3 | −100.0% | −907.5392 to −494.6608 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 825.6 | 119.9 | −85.5% | −845.5891 to −565.8109 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.8 | 0 | −100.0% | −17.4660 to −4.1340 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.964 | −0.6% | −0.1160 to +0.0449 | no |
| node-hours | 2.514 | 2.499 | −0.6% | −0.0483 to +0.0180 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 270.9 | −0.7% | −4.5125 to +0.4293 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 269.8 | −1.2% | −5.5813 to −0.7477 | yes: GAIN |
| response time (ms), mean | 411.3 | 117 | −71.5% | −443.3946 to −145.1757 | yes: GAIN |
| response time (ms), 95th percentile | 1524 | 263.1 | −82.7% | −1947.6613 to −574.0897 | yes: GAIN |
| response time (ms), 99th percentile | 2187 | 387.7 | −82.3% | −2809.8704 to −788.1246 | yes: GAIN |
| time over the response line (% of samples) | 19.69 | 0.4613 | −97.7% | −30.2676 to −8.1841 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 0.4 | −96.0% | −13.5779 to −5.4221 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 112 | +112.000 (native is 0) | +100.1692 to +123.8308 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.55 | 1257 | +11816.5% | +954.1211 to +1539.1656 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06131 | 0.05715 | −6.8% | −0.0118 to +0.0034 | no |
| CPU used (cores), mean | 1.472 | 1.364 | −7.3% | −0.2820 to +0.0676 | no |
| Omni's own CPU (cores), mean | 0 | 0.07261 | +0.073 (native is 0) | +0.0636 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.472 | 1.437 | −2.4% | −0.2006 to +0.1314 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 458.3 | 473.5 | +3.3% | −43.8635 to +74.1307 | no |
| HPA replicas, mean | 1.979 | 2.149 | +8.6% | +0.0205 to +0.3207 | yes: power given |
| pods started | 0 | 0.7 | +0.700 (native is 0) | +0.0214 to +1.3786 | yes: power given |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | +0.0428 to +2.7572 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.8 | +0.800 (native is 0) | +0.0612 to +1.5388 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.12 | 46.27 | +9.9% | +0.7362 to +7.5631 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.4 | 1454 | +82.6% | +584.8133 to +730.1867 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.283 | −12.0% | −9.8326 to +8.3978 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04167 | 219.9 | +527660.0% | +166.3532 to +273.3634 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 847.7 | +211825.0% | +702.4021 to +992.1979 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 103 | 863.1 | +737.8% | +617.4734 to +902.7349 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 12.7 | +12.700 (native is 0) | +7.0672 to +18.3328 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*