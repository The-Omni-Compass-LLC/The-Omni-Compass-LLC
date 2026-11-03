# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.618 | 5.908 |
| node-hours | 2.51 | 2.513 | 1.939 | 2.479 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 284.7 | 273.8 | 285.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 284.7 | 230.3 | 282.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 399.4 | 632 | 388.8 | 626.4 |
| response time (ms), 95th percentile | 1487 | 1353 | 1620 | 1328 |
| response time (ms), 99th percentile | 2081 | 1775 | 2277 | 1820 |
| time over the response line (% of samples) | 17.32 | 54.59 | 17.61 | 54.5 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 23.2 | 8.8 | 23.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 131.1 | 34.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.26 | 2.068 | 15.51 | 2.292 |
| utilisation (used / allocatable) | 0.06273 | 0.09324 | 0.08367 | 0.09457 |
| CPU used (cores), mean | 1.506 | 2.238 | 1.495 | 2.236 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07052 | 0.04145 |
| CPU used with Omni's own (cores), mean | 1.506 | 2.238 | 1.566 | 2.278 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 304.6 | 366.6 | 301.3 |
| HPA replicas, mean | 1.911 | 1.99 | 2.415 | 2.594 |
| pods started | 0 | 0.1 | 1.9 | 1.2 |
| pod start wait, total (s) | 0 | 0.2 | 4.1 | 3.8 |
| pod start wait, mean (s) | 0 | 0.2 | 1.458 | 0.8833 |
| host CPU busy, the real machine under kind (%) | 42.79 | 72.21 | 45.87 | 73.58 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 810.1 | 1396 | 818.2 | 1405 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.968 | 4.911 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 554.7 | 0.2458 | 551.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 903.2 | 1.3 | 936.2 |
| queue: job turnaround, submitted to done, mean (s) | 115.1 | 859.6 | 122.9 | 872.5 |
| queue: jobs unfinished at the window's end | 0 | 11.5 | 0 | 11.9 |
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
| worker nodes in service, mean | 6 | 5.908 | −1.5% | −0.2257 to +0.0407 | no |
| node-hours | 2.513 | 2.479 | −1.3% | −0.0903 to +0.0228 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 285.2 | +0.2% | −0.4676 to +1.5261 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 282.3 | −0.8% | −6.8322 to +2.0824 | no |
| response time (ms), mean | 632 | 626.4 | −0.9% | −44.7010 to +33.4382 | no |
| response time (ms), 95th percentile | 1353 | 1328 | −1.8% | −122.9678 to +73.9168 | no |
| response time (ms), 99th percentile | 1775 | 1820 | +2.5% | −74.0688 to +163.7910 | no |
| time over the response line (% of samples) | 54.59 | 54.5 | −0.2% | −3.4963 to +3.3217 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.2 | 23.1 | −0.4% | −0.5060 to +0.3060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.8 | +34.800 (native is 0) | +29.2204 to +40.3796 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.068 | 2.292 | +10.8% | −0.2042 to +0.6509 | no |
| utilisation (used / allocatable) | 0.09324 | 0.09457 | +1.4% | −0.0008 to +0.0035 | no |
| CPU used (cores), mean | 2.238 | 2.236 | −0.1% | −0.0408 to +0.0376 | no |
| Omni's own CPU (cores), mean | 0 | 0.04145 | +0.041 (native is 0) | +0.0357 to +0.0472 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.238 | 2.278 | +1.8% | +0.0011 to +0.0786 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.6 | 301.3 | −1.1% | −9.1718 to +2.5771 | no |
| HPA replicas, mean | 1.99 | 2.594 | +30.3% | +0.2818 to +0.9260 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | −0.4977 to +2.6977 | no |
| pod start wait, total (s) | 0.2 | 3.8 | +1800.0% | −1.6586 to +8.8586 | no |
| pod start wait, mean (s) | 0.2 | 0.8833 | +341.7% | −0.5485 to +1.9152 | no |
| host CPU busy, the real machine under kind (%) | 72.21 | 73.58 | +1.9% | +0.2604 to +2.4689 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1396 | 1405 | +0.6% | −11.1446 to +29.1446 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.911 | −18.1% | −2.7389 to +0.5615 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 554.7 | 551.7 | −0.5% | −18.2625 to +12.4495 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 903.2 | 936.2 | +3.6% | −6.7489 to +72.6122 | no |
| queue: job turnaround, submitted to done, mean (s) | 859.6 | 872.5 | +1.5% | −22.6254 to +48.4421 | no |
| queue: jobs unfinished at the window's end | 11.5 | 11.9 | +3.5% | −0.2911 to +1.0911 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.51 | 2.513 | +0.1% | −0.0053 to +0.0107 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 284.7 | +4.3% | +9.1574 to +14.1707 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 284.7 | +4.3% | +9.1574 to +14.1707 | yes: power given |
| response time (ms), mean | 399.4 | 632 | +58.2% | +157.5631 to +307.6165 | yes: LOSS |
| response time (ms), 95th percentile | 1487 | 1353 | −9.0% | −775.2439 to +506.4769 | no |
| response time (ms), 99th percentile | 2081 | 1775 | −14.7% | −1245.9060 to +634.5214 | no |
| time over the response line (% of samples) | 17.32 | 54.59 | +215.1% | +27.8208 to +46.7041 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 23.2 | +179.5% | +10.9756 to +18.8244 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.26 | 2.068 | −84.4% | −18.1190 to −4.2677 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06273 | 0.09324 | +48.6% | +0.0245 to +0.0365 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 2.238 | +48.6% | +0.5878 to +0.8766 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.506 | 2.238 | +48.6% | +0.5878 to +0.8766 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 304.6 | −31.7% | −186.8062 to −95.4890 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.911 | 1.99 | +4.2% | −0.0568 to +0.2157 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 42.79 | 72.21 | +68.8% | +26.5394 to +32.3074 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.1 | 1396 | +72.4% | +514.1504 to +658.4496 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 554.7 | +277227.5% | +234.0563 to +874.8538 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 903.2 | +64416.4% | +426.5669 to +1377.0919 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 115.1 | 859.6 | +647.1% | +587.0632 to +902.0201 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.5 | +11.500 (native is 0) | +4.2738 to +18.7262 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.618 | −23.0% | −2.3968 to −0.3670 | yes: GAIN |
| node-hours | 2.51 | 1.939 | −22.8% | −0.9990 to −0.1447 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.8 | +0.3% | −0.6108 to +2.1045 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 230.3 | −15.6% | −75.1849 to −10.1964 | yes: GAIN |
| response time (ms), mean | 399.4 | 388.8 | −2.7% | −26.5705 to +5.2159 | no |
| response time (ms), 95th percentile | 1487 | 1620 | +9.0% | +19.7385 to +247.1105 | yes: LOSS |
| response time (ms), 99th percentile | 2081 | 2277 | +9.4% | +32.5209 to +358.7985 | yes: LOSS |
| time over the response line (% of samples) | 17.32 | 17.61 | +1.7% | −0.5742 to +1.1516 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.8 | +6.0% | −0.4079 to +1.4079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 131.1 | +131.100 (native is 0) | +49.8963 to +212.3037 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.26 | 15.51 | +17.0% | −0.2191 to +4.7225 | no |
| utilisation (used / allocatable) | 0.06273 | 0.08367 | +33.4% | +0.0059 to +0.0360 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 1.495 | −0.7% | −0.0454 to +0.0247 | no |
| Omni's own CPU (cores), mean | 0 | 0.07052 | +0.071 (native is 0) | +0.0626 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 1.566 | +4.0% | +0.0190 to +0.1014 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 366.6 | −17.8% | −134.9393 to −23.4132 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.911 | 2.415 | +26.4% | +0.2043 to +0.8048 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.8634 to +2.9366 | yes: power given |
| pod start wait, total (s) | 0 | 4.1 | +4.100 (native is 0) | +1.3307 to +6.8693 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.458 | +1.458 (native is 0) | +0.6729 to +2.2438 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.79 | 45.87 | +7.2% | +2.5551 to +3.6050 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.1 | 818.2 | +1.0% | −0.2176 to +16.4176 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.968 | −33.9% | −3.4203 to −0.6436 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.2458 | +22.9% | −0.0520 to +0.1436 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 1.3 | −7.1% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.1 | 122.9 | +6.8% | +1.5463 to +14.1704 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.618 | −23.0% | −2.3968 to −0.3670 | yes: GAIN |
| node-hours | 2.513 | 1.938 | −22.9% | −1.0027 to −0.1463 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 273.8 | −3.8% | −13.5791 to −8.2553 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 230.3 | −19.1% | −88.6394 to −20.0700 | yes: GAIN |
| response time (ms), mean | 632 | 388.8 | −38.5% | −316.1344 to −170.3998 | yes: GAIN |
| response time (ms), 95th percentile | 1353 | 1620 | +19.8% | −419.4645 to +955.0805 | no |
| response time (ms), 99th percentile | 1775 | 2277 | +28.2% | −530.1787 to +1532.8827 | no |
| time over the response line (% of samples) | 54.59 | 17.61 | −67.7% | −46.1641 to −27.7833 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.2 | 8.8 | −62.1% | −18.1579 to −10.6421 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 131.1 | +131.100 (native is 0) | +49.8963 to +212.3037 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.068 | 15.51 | +650.0% | +5.1306 to +21.7594 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09324 | 0.08367 | −10.3% | −0.0205 to +0.0014 | no |
| CPU used (cores), mean | 2.238 | 1.495 | −33.2% | −0.9006 to −0.5845 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07052 | +0.071 (native is 0) | +0.0626 to +0.0784 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.238 | 1.566 | −30.0% | −0.8366 to −0.5073 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 304.6 | 366.6 | +20.3% | +44.7771 to +79.1656 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.99 | 2.415 | +21.4% | +0.1793 to +0.6708 | yes: power given |
| pods started | 0.1 | 1.9 | +1800.0% | +0.6417 to +2.9583 | yes: power given |
| pod start wait, total (s) | 0.2 | 4.1 | +1950.0% | +0.9325 to +6.8675 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.458 | +629.2% | +0.1845 to +2.3322 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.21 | 45.87 | −36.5% | −29.0103 to −23.6764 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1396 | 818.2 | −41.4% | −648.3453 to −508.0547 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2 | −66.7% | −4.0000 to −4.0000 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 554.7 | 0.2458 | −100.0% | −874.7562 to −234.0623 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 903.2 | 1.3 | −99.9% | −1377.0810 to −426.7778 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 859.6 | 122.9 | −85.7% | −889.8369 to −583.5298 | yes: GAIN |
| queue: jobs unfinished at the window's end | 11.5 | 0 | −100.0% | −18.7262 to −4.2738 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.908 | −1.5% | −0.2257 to +0.0407 | no |
| node-hours | 2.51 | 2.479 | −1.2% | −0.0917 to +0.0296 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 285.2 | +4.5% | +9.9909 to +14.3957 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 282.3 | +3.4% | +4.4408 to +14.1375 | yes: power given |
| response time (ms), mean | 399.4 | 626.4 | +56.8% | +145.3460 to +308.5708 | yes: LOSS |
| response time (ms), 95th percentile | 1487 | 1328 | −10.7% | −835.8893 to +518.0713 | no |
| response time (ms), 99th percentile | 2081 | 1820 | −12.5% | −1239.3520 to +717.6896 | no |
| time over the response line (% of samples) | 17.32 | 54.5 | +214.6% | +26.9852 to +47.3652 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 23.1 | +178.3% | +10.9731 to +18.6269 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.8 | +34.800 (native is 0) | +29.2204 to +40.3796 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.26 | 2.292 | −82.7% | −18.0121 to −3.9279 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.06273 | 0.09457 | +50.8% | +0.0249 to +0.0387 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.506 | 2.236 | +48.5% | +0.5815 to +0.8796 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04145 | +0.041 (native is 0) | +0.0357 to +0.0472 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.506 | 2.278 | +51.3% | +0.6272 to +0.9168 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.8 | 301.3 | −32.4% | −193.0889 to −95.8010 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.911 | 2.594 | +35.8% | +0.3157 to +1.0510 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | −0.3379 to +2.7379 | no |
| pod start wait, total (s) | 0 | 3.8 | +3.800 (native is 0) | −1.3559 to +8.9559 | no |
| pod start wait, mean (s) | 0 | 0.8833 | +0.883 (native is 0) | −0.1711 to +1.9378 | no |
| host CPU busy, the real machine under kind (%) | 42.79 | 73.58 | +72.0% | +27.7914 to +33.7847 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.1 | 1405 | +73.5% | +523.2190 to +667.3810 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.911 | −18.1% | −2.7389 to +0.5615 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 551.7 | +275774.3% | +238.5029 to +864.5944 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 936.2 | +66768.6% | +466.9429 to +1402.5793 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 115.1 | 872.5 | +658.3% | +603.8303 to +911.0697 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.9 | +11.900 (native is 0) | +4.4476 to +19.3524 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*