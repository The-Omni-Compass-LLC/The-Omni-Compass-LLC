# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 4.38 | 5.95 |
| node-hours | 2.514 | 2.513 | 1.832 | 2.488 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 284.9 | 271.9 | 284.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 284.9 | 221 | 283 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 332.1 | 569.8 | 323.2 | 572 |
| response time (ms), 95th percentile | 1233 | 1217 | 1333 | 1246 |
| response time (ms), 99th percentile | 1688 | 1638 | 1937 | 1660 |
| time over the response line (% of samples) | 13.65 | 48.63 | 13.75 | 48.85 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 22.5 | 7.3 | 23 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 138.8 | 35.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 14.29 | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.2 | 2.138 | 11.45 | 2.315 |
| utilisation (used / allocatable) | 0.05919 | 0.09362 | 0.08284 | 0.09488 |
| CPU used (cores), mean | 1.42 | 2.247 | 1.412 | 2.26 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06876 | 0.03959 |
| CPU used with Omni's own (cores), mean | 1.42 | 2.247 | 1.481 | 2.299 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.9 | 305.1 | 374.7 | 300.7 |
| HPA replicas, mean | 1.937 | 2.036 | 2.083 | 2.481 |
| pods started | 0.1 | 0.1 | 0.4 | 1.2 |
| pod start wait, total (s) | 0.1 | 0.2 | 0.8 | 3.4 |
| pod start wait, mean (s) | 0.1 | 0.2 | 0.4 | 2.35 |
| host CPU busy, the real machine under kind (%) | 40.22 | 70.59 | 43.18 | 72.89 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 786.7 | 1364 | 795.4 | 1388 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 3.575 | 5.546 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 457.9 | 0.1 | 512.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 870.3 | 0.7 | 888 |
| queue: job turnaround, submitted to done, mean (s) | 92.78 | 793.9 | 99.66 | 837.4 |
| queue: jobs unfinished at the window's end | 0 | 10.2 | 0 | 11.5 |
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
| worker nodes in service, mean | 6 | 5.95 | −0.8% | −0.1646 to +0.0637 | no |
| node-hours | 2.513 | 2.488 | −1.0% | −0.0754 to +0.0256 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 284.9 | 284.6 | −0.1% | −1.8265 to +1.3527 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.9 | 283 | −0.6% | −5.8630 to +2.2309 | no |
| response time (ms), mean | 569.8 | 572 | +0.4% | −41.3979 to +45.6322 | no |
| response time (ms), 95th percentile | 1217 | 1246 | +2.4% | −86.8635 to +144.7135 | no |
| response time (ms), 99th percentile | 1638 | 1660 | +1.4% | −161.7826 to +206.4000 | no |
| time over the response line (% of samples) | 48.63 | 48.85 | +0.5% | −4.3644 to +4.8046 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.5 | 23 | +2.2% | −0.1952 to +1.1952 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.6 | +35.600 (native is 0) | +27.8210 to +43.3790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.138 | 2.315 | +8.3% | −0.3845 to +0.7379 | no |
| utilisation (used / allocatable) | 0.09362 | 0.09488 | +1.3% | −0.0016 to +0.0041 | no |
| CPU used (cores), mean | 2.247 | 2.26 | +0.6% | −0.0414 to +0.0666 | no |
| Omni's own CPU (cores), mean | 0 | 0.03959 | +0.040 (native is 0) | +0.0336 to +0.0456 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.247 | 2.299 | +2.3% | +0.0018 to +0.1025 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.1 | 300.7 | −1.4% | −13.0545 to +4.2145 | no |
| HPA replicas, mean | 2.036 | 2.481 | +21.8% | +0.1993 to +0.6904 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.4737 to +1.7263 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.4 | +1600.0% | +1.4221 to +4.9779 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 2.35 | +1075.0% | +1.0964 to +3.2036 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 70.59 | 72.89 | +3.3% | +0.9017 to +3.7089 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1364 | 1388 | +1.8% | −8.0145 to +56.2145 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.546 | −7.6% | −1.8974 to +0.9900 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 457.9 | 512.6 | +11.9% | −0.9289 to +110.3543 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 870.3 | 888 | +2.0% | −35.9962 to +71.3941 | no |
| queue: job turnaround, submitted to done, mean (s) | 793.9 | 837.4 | +5.5% | +14.9694 to +71.8889 | yes: LOSS |
| queue: jobs unfinished at the window's end | 10.2 | 11.5 | +12.7% | −0.2099 to +2.8099 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.514 | 2.513 | −0.0% | −0.0088 to +0.0072 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 284.9 | +4.7% | +10.2573 to +15.3385 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 284.9 | +4.7% | +10.2573 to +15.3385 | yes: power given |
| response time (ms), mean | 332.1 | 569.8 | +71.6% | +174.7743 to +300.6715 | yes: LOSS |
| response time (ms), 95th percentile | 1233 | 1217 | −1.3% | −638.6015 to +606.5425 | no |
| response time (ms), 99th percentile | 1688 | 1638 | −3.0% | −949.8133 to +849.5521 | no |
| time over the response line (% of samples) | 13.65 | 48.63 | +256.4% | +24.8876 to +45.0757 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 22.5 | +240.9% | +11.9756 to +19.8244 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.2 | 2.138 | −80.9% | −13.1202 to −4.9998 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05919 | 0.09362 | +58.2% | +0.0263 to +0.0426 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.42 | 2.247 | +58.2% | +0.6301 to +1.0230 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.42 | 2.247 | +58.2% | +0.6301 to +1.0230 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.9 | 305.1 | −35.3% | −220.3590 to −113.2496 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.937 | 2.036 | +5.1% | −0.0638 to +0.2630 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| pod start wait, mean (s) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| host CPU busy, the real machine under kind (%) | 40.22 | 70.59 | +75.5% | +25.5145 to +35.2209 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.7 | 1364 | +73.4% | +468.3031 to +686.4969 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 457.9 | +646367.0% | +177.6204 to +738.0662 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 870.3 | +173953.8% | +397.4566 to +1342.0812 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 92.78 | 793.9 | +755.8% | +525.2724 to +877.0609 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 10.2 | +10.200 (native is 0) | +3.4830 to +16.9170 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.38 | −27.0% | −2.5888 to −0.6510 | yes: GAIN |
| node-hours | 2.514 | 1.832 | −27.1% | −1.0833 to −0.2799 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.9 | −0.0% | −1.0836 to +0.8397 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 221 | −18.8% | −81.0968 to −20.9388 | yes: GAIN |
| response time (ms), mean | 332.1 | 323.2 | −2.7% | −17.6776 to −0.1810 | yes: GAIN |
| response time (ms), 95th percentile | 1233 | 1333 | +8.1% | +23.6566 to +175.2054 | yes: LOSS |
| response time (ms), 99th percentile | 1688 | 1937 | +14.7% | +43.8758 to +453.4348 | yes: LOSS |
| time over the response line (% of samples) | 13.65 | 13.75 | +0.8% | −0.3562 to +0.5664 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.3 | +10.6% | −0.2567 to +1.6567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.8 | +138.800 (native is 0) | +57.1694 to +220.4306 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.2 | 11.45 | +2.2% | −1.9297 to +2.4297 | no |
| utilisation (used / allocatable) | 0.05919 | 0.08284 | +40.0% | +0.0096 to +0.0377 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.42 | 1.412 | −0.6% | −0.0324 to +0.0165 | no |
| Omni's own CPU (cores), mean | 0 | 0.06876 | +0.069 (native is 0) | +0.0607 to +0.0768 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.42 | 1.481 | +4.3% | +0.0301 to +0.0915 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.9 | 374.7 | −20.6% | −154.3776 to −39.9755 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.937 | 2.083 | +7.6% | −0.0707 to +0.3634 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.1 | 0.8 | +700.0% | −0.3690 to +1.7690 | no |
| pod start wait, mean (s) | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| host CPU busy, the real machine under kind (%) | 40.22 | 43.18 | +7.4% | +2.3074 to +3.6161 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.7 | 795.4 | +1.1% | +1.4990 to +15.9010 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.575 | −40.4% | −3.7819 to −1.0684 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.1 | +41.2% | −0.0175 to +0.0759 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.7 | +40.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.78 | 99.66 | +7.4% | +0.4513 to +13.3154 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.38 | −27.0% | −2.5888 to −0.6510 | yes: GAIN |
| node-hours | 2.513 | 1.832 | −27.1% | −1.0784 to −0.2831 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 284.9 | 271.9 | −4.5% | −15.8575 to −9.9821 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.9 | 221 | −22.4% | −95.2680 to −32.3633 | yes: GAIN |
| response time (ms), mean | 569.8 | 323.2 | −43.3% | −315.2113 to −178.0930 | yes: GAIN |
| response time (ms), 95th percentile | 1217 | 1333 | +9.5% | −564.5373 to +795.4583 | no |
| response time (ms), 99th percentile | 1638 | 1937 | +18.2% | −773.8767 to +1371.4485 | no |
| time over the response line (% of samples) | 48.63 | 13.75 | −71.7% | −45.1062 to −24.6469 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.5 | 7.3 | −67.6% | −18.8753 to −11.5247 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 138.8 | +138.800 (native is 0) | +57.1694 to +220.4306 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.138 | 11.45 | +435.4% | +3.9817 to +14.6383 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09362 | 0.08284 | −11.5% | −0.0230 to +0.0014 | no |
| CPU used (cores), mean | 2.247 | 1.412 | −37.1% | −1.0405 to −0.6285 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06876 | +0.069 (native is 0) | +0.0607 to +0.0768 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.247 | 1.481 | −34.1% | −0.9748 to −0.5566 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 305.1 | 374.7 | +22.8% | +43.0677 to +96.1877 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.036 | 2.083 | +2.3% | −0.1805 to +0.2741 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0.2 | 0.8 | +300.0% | −0.3656 to +1.5656 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 70.59 | 43.18 | −38.8% | −32.2106 to −22.6013 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1364 | 795.4 | −41.7% | −675.3461 to −462.0539 | yes: GAIN |
| batch: worker machines in service after the queue finished, mean | 6 | 2.057 | −65.7% | −4.1250 to −3.7604 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 457.9 | 0.1 | −100.0% | −738.0250 to −177.6033 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 870.3 | 0.7 | −99.9% | −1341.9067 to −397.2311 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 793.9 | 99.66 | −87.4% | −866.3620 to −522.2047 | yes: GAIN |
| queue: jobs unfinished at the window's end | 10.2 | 0 | −100.0% | −16.9170 to −3.4830 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.95 | −0.8% | −0.1646 to +0.0637 | no |
| node-hours | 2.514 | 2.488 | −1.0% | −0.0742 to +0.0228 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 284.6 | +4.6% | +9.3989 to +15.7231 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 283 | +4.0% | +5.8477 to +16.1160 | yes: power given |
| response time (ms), mean | 332.1 | 572 | +72.2% | +166.8255 to +312.8546 | yes: LOSS |
| response time (ms), 95th percentile | 1233 | 1246 | +1.0% | −630.4876 to +656.2786 | no |
| response time (ms), 99th percentile | 1688 | 1660 | −1.6% | −989.8685 to +934.2247 | no |
| time over the response line (% of samples) | 13.65 | 48.85 | +258.0% | +25.5041 to +44.8994 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 23 | +248.5% | +12.2537 to +20.5463 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.6 | +35.600 (native is 0) | +27.8210 to +43.3790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.2 | 2.315 | −79.3% | −12.9201 to −4.8466 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.05919 | 0.09488 | +60.3% | +0.0273 to +0.0441 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.42 | 2.26 | +59.1% | +0.6365 to +1.0418 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03959 | +0.040 (native is 0) | +0.0336 to +0.0456 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.42 | 2.299 | +61.9% | +0.6799 to +1.0775 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 471.9 | 300.7 | −36.3% | −228.1290 to −114.3196 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.937 | 2.481 | +28.1% | +0.3627 to +0.7261 | yes: power given |
| pods started | 0.1 | 1.2 | +1100.0% | +0.4737 to +1.7263 | yes: power given |
| pod start wait, total (s) | 0.1 | 3.4 | +3300.0% | +1.5790 to +5.0210 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 2.35 | +2250.0% | +1.2349 to +3.2651 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.22 | 72.89 | +81.2% | +28.2330 to +37.1129 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.7 | 1388 | +76.5% | +510.5442 to +692.4558 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.546 | −7.6% | −1.8974 to +0.9900 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 512.6 | +723608.5% | +203.0287 to +822.0834 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 888 | +177493.6% | +434.7001 to +1340.2356 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 92.78 | 837.4 | +802.6% | +573.3397 to +915.8520 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 11.5 | +11.500 (native is 0) | +4.1800 to +18.8200 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*