# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.311 | 5.234 |
| node-hours | 2.512 | 2.517 | 2.226 | 2.196 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.4 | 275.8 | 276 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.4 | 254.1 | 251.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 563.4 | 570.4 | 557.1 | 576.4 |
| response time (ms), 95th percentile | 2182 | 2249 | 2472 | 2534 |
| response time (ms), 99th percentile | 3046 | 3135 | 3450 | 3556 |
| time over the response line (% of samples) | 27.31 | 27.03 | 26.5 | 27.08 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.2 | 12.4 | 12.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 86 | 85.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.44 | 16.54 | 18.42 | 20.32 |
| utilisation (used / allocatable) | 0.06919 | 0.06718 | 0.07928 | 0.08027 |
| CPU used (cores), mean | 1.661 | 1.612 | 1.65 | 1.649 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07524 | 0.07896 |
| CPU used with Omni's own (cores), mean | 1.661 | 1.612 | 1.726 | 1.728 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 404.1 | 420 | 367.6 | 364.2 |
| HPA replicas, mean | 2.026 | 1.99 | 2.374 | 2.205 |
| pods started | 0 | 0 | 1.1 | 1.1 |
| pod start wait, total (s) | 0 | 0 | 2.4 | 2.9 |
| pod start wait, mean (s) | 0 | 0 | 1.317 | 1.033 |
| host CPU busy, the real machine under kind (%) | 46.93 | 47.24 | 49.84 | 50.76 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 857.9 | 866.5 | 872.4 | 883.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.917 | 4.728 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.6708 | 0.2917 | 1.554 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 3.3 | 1.6 | 11.2 |
| queue: job turnaround, submitted to done, mean (s) | 164.1 | 169.7 | 176.1 | 186.1 |
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
| worker nodes in service, mean | 6 | 5.234 | −12.8% | −1.5922 to +0.0606 | no |
| node-hours | 2.517 | 2.196 | −12.8% | −0.6668 to +0.0244 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.4 | 276 | +0.2% | −0.5510 to +1.6985 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.4 | 251.9 | −8.5% | −49.1472 to +2.1698 | no |
| response time (ms), mean | 570.4 | 576.4 | +1.1% | −16.6919 to +28.7681 | no |
| response time (ms), 95th percentile | 2249 | 2534 | +12.7% | +72.3090 to +497.6820 | yes: LOSS |
| response time (ms), 99th percentile | 3135 | 3556 | +13.4% | +222.0521 to +621.1219 | yes: LOSS |
| time over the response line (% of samples) | 27.03 | 27.08 | +0.2% | −0.5250 to +0.6280 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.2 | 12.5 | +2.5% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.4 | +85.400 (native is 0) | +13.0261 to +157.7739 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.54 | 20.32 | +22.8% | +0.0596 to +7.4937 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06718 | 0.08027 | +19.5% | −0.0003 to +0.0265 | no |
| CPU used (cores), mean | 1.612 | 1.649 | +2.3% | +0.0167 to +0.0578 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07896 | +0.079 (native is 0) | +0.0712 to +0.0868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.612 | 1.728 | +7.2% | +0.0986 to +0.1337 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420 | 364.2 | −13.3% | −116.5408 to +4.9002 | no |
| HPA replicas, mean | 1.99 | 2.205 | +10.8% | +0.0153 to +0.4140 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.0100 to +2.1900 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.900 (native is 0) | −0.1245 to +5.9245 | no |
| pod start wait, mean (s) | 0 | 1.033 | +1.033 (native is 0) | +0.0570 to +2.0097 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.24 | 50.76 | +7.4% | +3.2109 to +3.8242 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 866.5 | 883.2 | +1.9% | +8.0107 to +25.3893 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.728 | −21.2% | −2.3937 to −0.1498 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6708 | 1.554 | +131.7% | +0.1270 to +1.6397 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 11.2 | +239.4% | +0.0827 to +15.7173 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 169.7 | 186.1 | +9.7% | +8.2714 to +24.5786 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.512 | 2.517 | +0.2% | −0.0054 to +0.0151 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.4 | −0.1% | −1.3024 to +1.0223 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 275.4 | −0.1% | −1.3024 to +1.0223 | no |
| response time (ms), mean | 563.4 | 570.4 | +1.2% | −9.6929 to +23.6854 | no |
| response time (ms), 95th percentile | 2182 | 2249 | +3.1% | −59.3494 to +192.6064 | no |
| response time (ms), 99th percentile | 3046 | 3135 | +2.9% | −101.6797 to +279.0121 | no |
| time over the response line (% of samples) | 27.31 | 27.03 | −1.0% | −0.8038 to +0.2558 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.2 | +1.7% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.44 | 16.54 | +0.6% | −1.2046 to +1.4179 | no |
| utilisation (used / allocatable) | 0.06919 | 0.06718 | −2.9% | −0.0034 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.661 | 1.612 | −2.9% | −0.0818 to −0.0149 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.661 | 1.612 | −2.9% | −0.0818 to −0.0149 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 404.1 | 420 | +4.0% | +0.0270 to +31.9298 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.026 | 1.99 | −1.8% | −0.2092 to +0.1374 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 46.93 | 47.24 | +0.7% | −0.2258 to +0.8430 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 857.9 | 866.5 | +1.0% | +3.0367 to +14.1633 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.6708 | +250.0% | −0.0056 to +0.9639 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 3.3 | +120.0% | −1.3416 to +4.9416 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.1 | 169.7 | +3.4% | +0.3344 to +10.8989 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.311 | −11.5% | −1.5505 to +0.1730 | no |
| node-hours | 2.512 | 2.226 | −11.4% | −0.6459 to +0.0738 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 275.8 | +0.1% | −0.7962 to +1.3244 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 254.1 | −7.8% | −48.5081 to +5.7322 | no |
| response time (ms), mean | 563.4 | 557.1 | −1.1% | −25.4345 to +12.8878 | no |
| response time (ms), 95th percentile | 2182 | 2472 | +13.3% | +135.9815 to +443.6625 | yes: LOSS |
| response time (ms), 99th percentile | 3046 | 3450 | +13.3% | +129.2678 to +679.5420 | yes: LOSS |
| time over the response line (% of samples) | 27.31 | 26.5 | −3.0% | −1.3556 to −0.2642 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.4 | +3.3% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 86 | +86.000 (native is 0) | +13.3150 to +158.6850 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.44 | 18.42 | +12.1% | −1.3973 to +5.3640 | no |
| utilisation (used / allocatable) | 0.06919 | 0.07928 | +14.6% | −0.0021 to +0.0223 | no |
| CPU used (cores), mean | 1.661 | 1.65 | −0.6% | −0.0403 to +0.0199 | no |
| Omni's own CPU (cores), mean | 0 | 0.07524 | +0.075 (native is 0) | +0.0682 to +0.0823 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.661 | 1.726 | +3.9% | +0.0284 to +0.1017 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 404.1 | 367.6 | −9.0% | −81.4798 to +8.6381 | no |
| HPA replicas, mean | 2.026 | 2.374 | +17.1% | +0.1724 to +0.5226 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.2436 to +1.9564 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.400 (native is 0) | +0.3434 to +4.4566 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.317 | +1.317 (native is 0) | +0.4344 to +2.1989 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.93 | 49.84 | +6.2% | +2.0928 to +3.7214 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 857.9 | 872.4 | +1.7% | +5.5579 to +23.4421 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.917 | −18.1% | −2.3481 to +0.1813 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 0.2917 | +52.2% | −0.1196 to +0.3196 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.6 | +6.7% | −1.5673 to +1.7673 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.1 | 176.1 | +7.4% | +2.7498 to +21.4336 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.311 | −11.5% | −1.5505 to +0.1730 | no |
| node-hours | 2.517 | 2.226 | −11.6% | −0.6501 to +0.0684 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.4 | 275.8 | +0.1% | −0.3390 to +1.1474 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.4 | 254.1 | −7.7% | −47.8134 to +5.3177 | no |
| response time (ms), mean | 570.4 | 557.1 | −2.3% | −36.0779 to +9.5388 | no |
| response time (ms), 95th percentile | 2249 | 2472 | +9.9% | +27.9024 to +418.4846 | yes: LOSS |
| response time (ms), 99th percentile | 3135 | 3450 | +10.1% | +155.3913 to +476.0861 | yes: LOSS |
| time over the response line (% of samples) | 27.03 | 26.5 | −2.0% | −1.2737 to +0.2019 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.2 | 12.4 | +1.6% | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 86 | +86.000 (native is 0) | +13.3150 to +158.6850 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.54 | 18.42 | +11.3% | −1.9307 to +5.6840 | no |
| utilisation (used / allocatable) | 0.06718 | 0.07928 | +18.0% | −0.0012 to +0.0255 | no |
| CPU used (cores), mean | 1.612 | 1.65 | +2.4% | +0.0228 to +0.0535 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07524 | +0.075 (native is 0) | +0.0682 to +0.0823 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.612 | 1.726 | +7.0% | +0.0984 to +0.1285 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 420 | 367.6 | −12.5% | −112.4997 to +7.7012 | no |
| HPA replicas, mean | 1.99 | 2.374 | +19.3% | +0.1425 to +0.6243 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.2436 to +1.9564 | yes: power given |
| pod start wait, total (s) | 0 | 2.4 | +2.400 (native is 0) | +0.3434 to +4.4566 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.317 | +1.317 (native is 0) | +0.4344 to +2.1989 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.24 | 49.84 | +5.5% | +2.1486 to +3.0484 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 866.5 | 872.4 | +0.7% | −0.7970 to +12.5970 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.917 | −18.1% | −2.3481 to +0.1813 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6708 | 0.2917 | −56.5% | −0.8459 to +0.0875 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 1.6 | −51.5% | −5.8167 to +2.4167 | no |
| queue: job turnaround, submitted to done, mean (s) | 169.7 | 176.1 | +3.8% | −0.1874 to +13.1374 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.234 | −12.8% | −1.5922 to +0.0606 | no |
| node-hours | 2.512 | 2.196 | −12.6% | −0.6622 to +0.0296 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.5 | 276 | +0.2% | −0.3290 to +1.1964 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 251.9 | −8.6% | −49.8452 to +2.5876 | no |
| response time (ms), mean | 563.4 | 576.4 | +2.3% | −11.2701 to +37.3386 | no |
| response time (ms), 95th percentile | 2182 | 2534 | +16.1% | +161.4447 to +541.8033 | yes: LOSS |
| response time (ms), 99th percentile | 3046 | 3556 | +16.8% | +243.5811 to +776.9253 | yes: LOSS |
| time over the response line (% of samples) | 27.31 | 27.08 | −0.8% | −0.6291 to +0.1840 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.5 | +4.2% | +0.1230 to +0.8770 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.4 | +85.400 (native is 0) | +13.0261 to +157.7739 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.44 | 20.32 | +23.6% | +0.1781 to +7.5885 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06919 | 0.08027 | +16.0% | −0.0011 to +0.0232 | no |
| CPU used (cores), mean | 1.661 | 1.649 | −0.7% | −0.0410 to +0.0188 | no |
| Omni's own CPU (cores), mean | 0 | 0.07896 | +0.079 (native is 0) | +0.0712 to +0.0868 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.661 | 1.728 | +4.1% | +0.0326 to +0.1031 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 404.1 | 364.2 | −9.9% | −85.1126 to +5.4288 | no |
| HPA replicas, mean | 2.026 | 2.205 | +8.8% | −0.0880 to +0.4455 | no |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.0100 to +2.1900 | yes: power given |
| pod start wait, total (s) | 0 | 2.9 | +2.900 (native is 0) | −0.1245 to +5.9245 | no |
| pod start wait, mean (s) | 0 | 1.033 | +1.033 (native is 0) | +0.0570 to +2.0097 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.93 | 50.76 | +8.2% | +3.0806 to +4.5716 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 857.9 | 883.2 | +2.9% | +12.6739 to +37.9261 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.728 | −21.2% | −2.3937 to −0.1498 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1917 | 1.554 | +710.9% | +0.1621 to +2.5629 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 11.2 | +646.7% | −0.7806 to +20.1806 | no |
| queue: job turnaround, submitted to done, mean (s) | 164.1 | 186.1 | +13.4% | +10.7003 to +33.3831 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*