# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.616 | 5.926 |
| node-hours | 2.516 | 2.513 | 1.935 | 2.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.1 | 271.2 | 271.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.1 | 227.7 | 268.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 269.8 | 122.2 | 265.5 | 97.14 |
| response time (ms), 95th percentile | 918.9 | 212.6 | 1097 | 219.5 |
| response time (ms), 99th percentile | 1399 | 312.8 | 1572 | 324.1 |
| time over the response line (% of samples) | 10.28 | 0.1779 | 10.47 | 0.2648 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 0.1 | 6.9 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 156.8 | 102.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 44.44 | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.95 | 964.6 | 7.878 | 1055 |
| utilisation (used / allocatable) | 0.05572 | 0.05745 | 0.0737 | 0.05708 |
| CPU used (cores), mean | 1.337 | 1.379 | 1.33 | 1.355 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06646 | 0.06467 |
| CPU used with Omni's own (cores), mean | 1.337 | 1.379 | 1.397 | 1.419 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.6 | 471.6 | 410.6 | 475.3 |
| HPA replicas, mean | 1.947 | 1.973 | 2.197 | 2.019 |
| pods started | 0 | 0 | 0.9 | 0.3 |
| pod start wait, total (s) | 0 | 0 | 2.2 | 0.6 |
| pod start wait, mean (s) | 0 | 0 | 0.9083 | 0.35 |
| host CPU busy, the real machine under kind (%) | 37.83 | 42.95 | 40.9 | 44.29 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 758.1 | 1371 | 767.2 | 1397 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.856 | 5.148 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 130.9 | 0.02083 | 155.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 561.4 | 0.1 | 659.6 |
| queue: job turnaround, submitted to done, mean (s) | 64.44 | 720.3 | 72.62 | 766.1 |
| queue: jobs unfinished at the window's end | 0 | 7.5 | 0 | 8.6 |
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
| worker nodes in service, mean | 6 | 5.926 | −1.2% | −0.1800 to +0.0310 | no |
| node-hours | 2.513 | 2.488 | −1.0% | −0.0695 to +0.0182 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.1% | −1.4520 to +1.7729 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 268.9 | −0.8% | −5.9061 to +1.5312 | no |
| response time (ms), mean | 122.2 | 97.14 | −20.5% | −30.8061 to −19.2647 | yes: GAIN |
| response time (ms), 95th percentile | 212.6 | 219.5 | +3.3% | −7.5557 to +21.3837 | no |
| response time (ms), 99th percentile | 312.8 | 324.1 | +3.6% | −14.5583 to +37.3075 | no |
| time over the response line (% of samples) | 0.1779 | 0.2648 | +48.8% | −0.1150 to +0.2886 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3 | +200.0% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.1 | +102.100 (native is 0) | +90.9650 to +113.2350 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 964.6 | 1055 | +9.4% | +14.1919 to +167.4181 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05745 | 0.05708 | −0.6% | −0.0028 to +0.0021 | no |
| CPU used (cores), mean | 1.379 | 1.355 | −1.7% | −0.0833 to +0.0351 | no |
| Omni's own CPU (cores), mean | 0 | 0.06467 | +0.065 (native is 0) | +0.0556 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.419 | +2.9% | −0.0177 to +0.0988 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.6 | 475.3 | +0.8% | −13.8822 to +21.4335 | no |
| HPA replicas, mean | 1.973 | 2.019 | +2.4% | −0.0839 to +0.1767 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.5285 to +1.7285 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.350 (native is 0) | −0.2353 to +0.9353 | no |
| host CPU busy, the real machine under kind (%) | 42.95 | 44.29 | +3.1% | +0.1859 to +2.4891 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1371 | 1397 | +1.9% | +2.0630 to +50.3370 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.148 | −14.2% | −2.0280 to +0.3236 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 130.9 | 155.3 | +18.6% | +3.4864 to +45.2302 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 561.4 | 659.6 | +17.5% | −46.2735 to +242.6735 | no |
| queue: job turnaround, submitted to done, mean (s) | 720.3 | 766.1 | +6.4% | −7.4652 to +99.1402 | no |
| queue: jobs unfinished at the window's end | 7.5 | 8.6 | +14.7% | −1.7101 to +3.9101 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.516 | 2.513 | −0.1% | −0.0131 to +0.0074 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.1 | +0.0% | −2.4919 to +2.6651 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 271.1 | +0.0% | −2.4919 to +2.6651 | no |
| response time (ms), mean | 269.8 | 122.2 | −54.7% | −284.0775 to −11.2437 | yes: GAIN |
| response time (ms), 95th percentile | 918.9 | 212.6 | −76.9% | −1345.4027 to −67.0503 | yes: GAIN |
| response time (ms), 99th percentile | 1399 | 312.8 | −77.6% | −2107.4413 to −65.4535 | yes: GAIN |
| time over the response line (% of samples) | 10.28 | 0.1779 | −98.3% | −20.3649 to +0.1522 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 0.1 | −98.4% | −10.5537 to −1.6463 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.95 | 964.6 | +10677.7% | +654.8968 to +1256.4132 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05572 | 0.05745 | +3.1% | −0.0041 to +0.0075 | no |
| CPU used (cores), mean | 1.337 | 1.379 | +3.1% | −0.0976 to +0.1807 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.337 | 1.379 | +3.1% | −0.0976 to +0.1807 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.6 | 471.6 | −5.0% | −69.0159 to +18.8571 | no |
| HPA replicas, mean | 1.947 | 1.973 | +1.3% | −0.0953 to +0.1462 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 37.83 | 42.95 | +13.6% | +1.9168 to +8.3397 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.1 | 1371 | +80.8% | +510.0434 to +715.5566 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 131 | +261800.0% | +83.7270 to +178.0730 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 561.4 | +140250.0% | +385.0167 to +736.9833 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 64.44 | 720.3 | +1017.8% | +504.2535 to +807.4632 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 7.5 | +7.500 (native is 0) | +1.0380 to +13.9620 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.616 | −23.1% | −2.2669 to −0.5009 | yes: GAIN |
| node-hours | 2.516 | 1.935 | −23.1% | −0.9499 to −0.2120 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.2 | +0.1% | −0.5520 to +0.9973 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 227.7 | −16.0% | −71.1748 to −15.4424 | yes: GAIN |
| response time (ms), mean | 269.8 | 265.5 | −1.6% | −24.0674 to +15.3333 | no |
| response time (ms), 95th percentile | 918.9 | 1097 | +19.3% | −5.5820 to +361.0730 | no |
| response time (ms), 99th percentile | 1399 | 1572 | +12.4% | −31.2450 to +377.1428 | no |
| time over the response line (% of samples) | 10.28 | 10.47 | +1.8% | −0.5191 to +0.8985 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 6.9 | +11.3% | −0.4209 to +1.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 156.8 | +156.800 (native is 0) | +94.9418 to +218.6582 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.95 | 7.878 | −12.0% | −1.9326 to −0.2107 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05572 | 0.0737 | +32.3% | +0.0065 to +0.0295 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.337 | 1.33 | −0.5% | −0.0504 to +0.0366 | no |
| Omni's own CPU (cores), mean | 0 | 0.06646 | +0.066 (native is 0) | +0.0576 to +0.0753 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.337 | 1.397 | +4.5% | +0.0087 to +0.1105 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.6 | 410.6 | −17.3% | −140.7092 to −31.4204 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.947 | 2.197 | +12.8% | −0.0036 to +0.5037 | no |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.1366 to +1.9366 | no |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | −0.5144 to +4.9144 | no |
| pod start wait, mean (s) | 0 | 0.9083 | +0.908 (native is 0) | +0.0567 to +1.7599 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 37.83 | 40.9 | +8.1% | +2.2118 to +3.9416 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.1 | 767.2 | +1.2% | −1.0633 to +19.2633 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.856 | −35.7% | −3.3560 to −0.9324 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.02083 | −58.3% | −0.0637 to +0.0054 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.1 | −75.0% | −0.6455 to +0.0455 | no |
| queue: job turnaround, submitted to done, mean (s) | 64.44 | 72.62 | +12.7% | −0.7495 to +17.1161 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.616 | −23.1% | −2.2669 to −0.5009 | yes: GAIN |
| node-hours | 2.513 | 1.935 | −23.0% | −0.9503 to −0.2059 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.1 | 271.2 | +0.1% | −2.3284 to +2.6004 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.1 | 227.7 | −16.0% | −73.0604 to −13.7301 | yes: GAIN |
| response time (ms), mean | 122.2 | 265.5 | +117.3% | −9.4481 to +296.0354 | no |
| response time (ms), 95th percentile | 212.6 | 1097 | +415.7% | +72.5946 to +1695.3494 | yes: LOSS |
| response time (ms), 99th percentile | 312.8 | 1572 | +402.7% | +90.1081 to +2428.6845 | yes: LOSS |
| time over the response line (% of samples) | 0.1779 | 10.47 | +5786.0% | +0.2936 to +20.2985 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 6.9 | +6800.0% | +2.4320 to +11.1680 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 156.8 | +156.800 (native is 0) | +94.9418 to +218.6582 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 964.6 | 7.878 | −99.2% | −1257.7663 to −655.6871 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05745 | 0.0737 | +28.3% | +0.0075 to +0.0250 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.379 | 1.33 | −3.5% | −0.2172 to +0.1203 | no |
| Omni's own CPU (cores), mean | 0 | 0.06646 | +0.066 (native is 0) | +0.0576 to +0.0753 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.379 | 1.397 | +1.3% | −0.1585 to +0.1945 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.6 | 410.6 | −12.9% | −94.0308 to −27.9399 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.197 | +11.4% | +0.0358 to +0.4135 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | −0.1366 to +1.9366 | no |
| pod start wait, total (s) | 0 | 2.2 | +2.200 (native is 0) | −0.5144 to +4.9144 | no |
| pod start wait, mean (s) | 0 | 0.9083 | +0.908 (native is 0) | +0.0567 to +1.7599 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.95 | 40.9 | −4.8% | −5.7326 to +1.6295 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1371 | 767.2 | −44.0% | −704.6206 to −502.7794 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.365 | −60.6% | −4.3767 to −2.8937 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 130.9 | 0.02083 | −100.0% | −178.1140 to −83.7444 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 561.4 | 0.1 | −100.0% | −737.4083 to −385.1917 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 720.3 | 72.62 | −89.9% | −793.5483 to −501.8017 | yes: GAIN |
| queue: jobs unfinished at the window's end | 7.5 | 0 | −100.0% | −13.9620 to −1.0380 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.926 | −1.2% | −0.1800 to +0.0310 | no |
| node-hours | 2.516 | 2.488 | −1.1% | −0.0740 to +0.0170 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271 | 271.2 | +0.1% | −2.0216 to +2.5158 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271 | 268.9 | −0.8% | −5.6978 to +1.4961 | no |
| response time (ms), mean | 269.8 | 97.14 | −64.0% | −310.2804 to −35.1116 | yes: GAIN |
| response time (ms), 95th percentile | 918.9 | 219.5 | −76.1% | −1326.5171 to −72.1079 | yes: GAIN |
| response time (ms), 99th percentile | 1399 | 324.1 | −76.8% | −2078.7519 to −71.3937 | yes: GAIN |
| time over the response line (% of samples) | 10.28 | 0.2648 | −97.4% | −20.1880 to +0.1489 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 0.3 | −95.2% | −10.1579 to −1.6421 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.1 | +102.100 (native is 0) | +90.9650 to +113.2350 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.95 | 1055 | +11692.3% | +725.4570 to +1367.4630 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05572 | 0.05708 | +2.5% | −0.0053 to +0.0080 | no |
| CPU used (cores), mean | 1.337 | 1.355 | +1.3% | −0.1343 to +0.1692 | no |
| Omni's own CPU (cores), mean | 0 | 0.06467 | +0.065 (native is 0) | +0.0556 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.337 | 1.419 | +6.1% | −0.0613 to +0.2256 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 496.6 | 475.3 | −4.3% | −70.1398 to +27.5323 | no |
| HPA replicas, mean | 1.947 | 2.019 | +3.7% | −0.1215 to +0.2651 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.5285 to +1.7285 | no |
| pod start wait, mean (s) | 0 | 0.35 | +0.350 (native is 0) | −0.2353 to +0.9353 | no |
| host CPU busy, the real machine under kind (%) | 37.83 | 44.29 | +17.1% | +3.2755 to +9.6560 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 758.1 | 1397 | +84.3% | +542.5198 to +735.4802 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.148 | −14.2% | −2.0280 to +0.3236 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 155.3 | +310516.7% | +101.8018 to +208.7148 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 659.6 | +164800.0% | +446.0529 to +872.3471 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 64.44 | 766.1 | +1088.9% | +537.5937 to +865.7979 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 8.6 | +8.600 (native is 0) | +2.5005 to +14.6995 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*