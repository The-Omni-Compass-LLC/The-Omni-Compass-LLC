# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 12 | 12 | 9.162 | 6.129 |
| node-hours | 5.027 | 5.027 | 3.836 | 2.567 |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 504.4 | 524.1 | 504.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 504.4 | 434.9 | 320 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 489.6 | 102.5 | 549.7 | 61.03 |
| response time (ms), 95th percentile | 1848 | 139.5 | 2242 | 80.4 |
| response time (ms), 99th percentile | 2501 | 163.4 | 2916 | 107.4 |
| time over the response line (% of samples) | 15.75 | 0.00381 | 18.07 | 0 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 0 | 10.4 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 162.3 | 32.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 36.39 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.28 | 0 | 29.39 | 0.07667 |
| utilisation (used / allocatable) | 0.03219 | 0.005566 | 0.04197 | 0.008818 |
| CPU used (cores), mean | 1.545 | 0.2672 | 1.525 | 0.2164 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.05298 | 0.02879 |
| CPU used with Omni's own (cores), mean | 1.545 | 0.2672 | 1.578 | 0.2452 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 848.6 | 4670 | 691 | 3680 |
| HPA replicas, mean | 3.956 | 4.13 | 4.382 | 4.372 |
| pods started | 0.1 | 0.7 | 2 | 1.8 |
| pod start wait, total (s) | 0.2 | 0.9 | 5.5 | 3.1 |
| pod start wait, mean (s) | 0.2 | 0.75 | 1.397 | 1.342 |
| host CPU busy, the real machine under kind (%) | 47.93 | 14.28 | 53.26 | 16.79 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 847.3 | 1506 | 879.7 | 1506 |
| batch: worker machines in service after the queue finished, mean | 12 | nan | 7.293 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1160 | 0.07917 | 1160 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1476 | 0.5 | 1476 |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 1160 | 184.5 | 1160 |
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
| worker nodes in service, mean | 12 | 6.129 | −48.9% | −5.9026 to −5.8399 | yes: GAIN |
| node-hours | 5.027 | 2.567 | −48.9% | −2.4813 to −2.4388 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 504.4 | −0.0% | −1.7379 to +1.6638 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 320 | −36.6% | −186.4151 to −182.5174 | yes: GAIN |
| response time (ms), mean | 102.5 | 61.03 | −40.5% | −54.5358 to −28.4588 | yes: GAIN |
| response time (ms), 95th percentile | 139.5 | 80.4 | −42.4% | −76.2907 to −41.8753 | yes: GAIN |
| response time (ms), 99th percentile | 163.4 | 107.4 | −34.3% | −69.8508 to −42.2354 | yes: GAIN |
| time over the response line (% of samples) | 0.00381 | 0 | −100.0% | −0.0124 to +0.0048 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 | +32.200 (native is 0) | +30.6996 to +33.7004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 0.07667 | +0.077 (native is 0) | −0.0455 to +0.1988 | no |
| utilisation (used / allocatable) | 0.005566 | 0.008818 | +58.4% | +0.0027 to +0.0038 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2672 | 0.2164 | −19.0% | −0.0575 to −0.0441 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02879 | +0.029 (native is 0) | +0.0244 to +0.0332 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2672 | 0.2452 | −8.2% | −0.0268 to −0.0172 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4670 | 3680 | −21.2% | −1109.1565 to −871.8496 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.13 | 4.372 | +5.9% | +0.0133 to +0.4703 | yes: power given |
| pods started | 0.7 | 1.8 | +157.1% | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0.9 | 3.1 | +244.4% | +0.7774 to +3.6226 | yes: LOSS |
| pod start wait, mean (s) | 0.75 | 1.342 | +78.9% | −0.0047 to +1.1881 | no |
| host CPU busy, the real machine under kind (%) | 14.28 | 16.79 | +17.5% | +2.0877 to +2.9185 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 1506 | +0.0% | −4.4087 to +4.8087 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 1160 | +0.0% | −4.3767 to +4.9351 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 1476 | +0.0% | −4.1997 to +5.1997 | no |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 1160 | +0.0% | −4.3767 to +4.9351 | no |
| queue: jobs unfinished at the window's end | 24 | 24 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 12 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 5.027 | 5.027 | −0.0% | −0.0181 to +0.0175 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 504.4 | −3.7% | −23.8568 to −15.2881 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 504.4 | −3.7% | −23.8568 to −15.2881 | yes: GAIN |
| response time (ms), mean | 489.6 | 102.5 | −79.1% | −710.0180 to −64.0744 | yes: GAIN |
| response time (ms), 95th percentile | 1848 | 139.5 | −92.5% | −3171.4664 to −245.3596 | yes: GAIN |
| response time (ms), 99th percentile | 2501 | 163.4 | −93.5% | −4249.1612 to −426.9252 | yes: GAIN |
| time over the response line (% of samples) | 15.75 | 0.00381 | −100.0% | −29.7355 to −1.7616 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 0 | −100.0% | −13.6056 to −1.5944 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.28 | 0 | −100.0% | −18.7029 to −5.8538 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03219 | 0.005566 | −82.7% | −0.0312 to −0.0221 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.545 | 0.2672 | −82.7% | −1.4962 to −1.0597 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.545 | 0.2672 | −82.7% | −1.4962 to −1.0597 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 848.6 | 4670 | +450.3% | +3305.5177 to +4337.6034 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.13 | +4.4% | −0.0745 to +0.4219 | no |
| pods started | 0.1 | 0.7 | +600.0% | +0.0999 to +1.1001 | yes: power given |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −0.1294 to +1.5294 | no |
| pod start wait, mean (s) | 0.2 | 0.75 | +275.0% | −0.0909 to +1.1909 | no |
| host CPU busy, the real machine under kind (%) | 47.93 | 14.28 | −70.2% | −39.8770 to −27.4207 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.3 | 1506 | +77.8% | +543.5294 to +774.2706 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1160 | +1855453.3% | +1155.1381 to +1164.1786 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1476 | +368825.0% | +1470.8006 to +1479.7994 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 1160 | +642.6% | +886.8328 to +1120.2505 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.162 | −23.7% | −4.5939 to −1.0830 | yes: GAIN |
| node-hours | 5.027 | 3.836 | −23.7% | −1.9254 to −0.4567 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 524.1 | +0.0% | −2.9322 to +3.0397 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 434.9 | −17.0% | −144.0561 to −34.1947 | yes: GAIN |
| response time (ms), mean | 489.6 | 549.7 | +12.3% | −7.1253 to +127.4509 | no |
| response time (ms), 95th percentile | 1848 | 2242 | +21.3% | +81.9376 to +706.1264 | yes: LOSS |
| response time (ms), 99th percentile | 2501 | 2916 | +16.6% | +6.3349 to +822.9519 | yes: LOSS |
| time over the response line (% of samples) | 15.75 | 18.07 | +14.7% | +0.9925 to +3.6394 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 10.4 | +36.8% | +0.8108 to +4.7892 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 162.3 | +162.300 (native is 0) | +79.1498 to +245.4502 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.28 | 29.39 | +139.4% | −10.1472 to +44.3672 | no |
| utilisation (used / allocatable) | 0.03219 | 0.04197 | +30.4% | +0.0033 to +0.0163 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.545 | 1.525 | −1.3% | −0.1149 to +0.0739 | no |
| Omni's own CPU (cores), mean | 0 | 0.05298 | +0.053 (native is 0) | +0.0476 to +0.0584 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.545 | 1.578 | +2.1% | −0.0630 to +0.1280 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 848.6 | 691 | −18.6% | −274.9630 to −40.2475 | yes, down (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.382 | +10.8% | +0.0554 to +0.7965 | yes: power given |
| pods started | 0.1 | 2 | +1900.0% | +0.0701 to +3.7299 | yes: power given |
| pod start wait, total (s) | 0.2 | 5.5 | +2650.0% | +0.2527 to +10.3473 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.397 | +598.3% | −0.1051 to +2.4984 | no |
| host CPU busy, the real machine under kind (%) | 47.93 | 53.26 | +11.1% | +4.0063 to +6.6450 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.3 | 879.7 | +3.8% | +4.7061 to +60.0939 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 12 | 7.293 | −39.2% | −7.4110 to −2.0039 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 0.07917 | +26.7% | −0.0344 to +0.0677 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.5 | +25.0% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 184.5 | +18.1% | +7.9574 to +48.6343 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 9.162 | −23.7% | −4.5939 to −1.0830 | yes: GAIN |
| node-hours | 5.027 | 3.836 | −23.7% | −1.9272 to −0.4542 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 504.4 | 524.1 | +3.9% | +15.6032 to +23.6491 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 504.4 | 434.9 | −13.8% | −127.9244 to −11.1816 | yes: GAIN |
| response time (ms), mean | 102.5 | 549.7 | +436.2% | +67.3400 to +827.0779 | yes: LOSS |
| response time (ms), 95th percentile | 139.5 | 2242 | +1507.3% | +378.8014 to +3826.0886 | yes: LOSS |
| response time (ms), 99th percentile | 163.4 | 2916 | +1684.4% | +581.0969 to +4924.2763 | yes: LOSS |
| time over the response line (% of samples) | 0.00381 | 18.07 | +474193.3% | +3.8889 to +32.2401 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 10.4 | +10.400 (native is 0) | +4.7154 to +16.0846 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 162.3 | +162.300 (native is 0) | +79.1498 to +245.4502 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0 | 29.39 | +29.388 (native is 0) | −2.1637 to +60.9403 | no |
| utilisation (used / allocatable) | 0.005566 | 0.04197 | +654.0% | +0.0334 to +0.0394 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.2672 | 1.525 | +470.6% | +1.0175 to +1.4973 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05298 | +0.053 (native is 0) | +0.0476 to +0.0584 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.2672 | 1.578 | +490.5% | +1.0659 to +1.5548 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 4670 | 691 | −85.2% | −4595.2539 to −3363.0777 | yes, down (shown, not judged) |
| HPA replicas, mean | 4.13 | 4.382 | +6.1% | −0.1414 to +0.6459 | no |
| pods started | 0.7 | 2 | +185.7% | −0.0924 to +2.6924 | no |
| pod start wait, total (s) | 0.9 | 5.5 | +511.1% | +0.3188 to +8.8812 | yes: LOSS |
| pod start wait, mean (s) | 0.75 | 1.397 | +86.2% | −0.1331 to +1.4265 | no |
| host CPU busy, the real machine under kind (%) | 14.28 | 53.26 | +272.9% | +31.5903 to +46.3587 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1506 | 879.7 | −41.6% | −768.0466 to −484.9534 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1160 | 0.07917 | −100.0% | −1164.1692 to −1155.1142 | yes: GAIN |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1476 | 0.5 | −100.0% | −1479.9063 to −1470.4937 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 1160 | 184.5 | −84.1% | −1110.5203 to −839.9714 | yes: GAIN |
| queue: jobs unfinished at the window's end | 24 | 0 | −100.0% | −24.0000 to −24.0000 | yes: GAIN |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 12 | 6.129 | −48.9% | −5.9026 to −5.8399 | yes: GAIN |
| node-hours | 5.027 | 2.567 | −48.9% | −2.4803 to −2.4405 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 524 | 504.4 | −3.7% | −22.6061 to −16.6129 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 524 | 320 | −38.9% | −206.7037 to −201.3737 | yes: GAIN |
| response time (ms), mean | 489.6 | 61.03 | −87.5% | −764.2854 to −92.8016 | yes: GAIN |
| response time (ms), 95th percentile | 1848 | 80.4 | −95.6% | −3246.8310 to −288.1610 | yes: GAIN |
| response time (ms), 99th percentile | 2501 | 107.4 | −95.7% | −4311.2254 to −476.9472 | yes: GAIN |
| time over the response line (% of samples) | 15.75 | 0 | −100.0% | −29.7427 to −1.7621 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 0 | −100.0% | −13.6056 to −1.5944 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.2 | +32.200 (native is 0) | +30.6996 to +33.7004 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.28 | 0.07667 | −99.4% | −18.6081 to −5.7952 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.03219 | 0.008818 | −72.6% | −0.0274 to −0.0194 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.545 | 0.2164 | −86.0% | −1.5504 to −1.1070 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02879 | +0.029 (native is 0) | +0.0244 to +0.0332 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.545 | 0.2452 | −84.1% | −1.5175 to −1.0823 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 848.6 | 3680 | +333.6% | +2416.5785 to +3245.5366 | yes, up (shown, not judged) |
| HPA replicas, mean | 3.956 | 4.372 | +10.5% | +0.2221 to +0.6089 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.8047 to +2.5953 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.1 | +1450.0% | +1.2671 to +4.5329 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.342 | +570.8% | +0.5196 to +1.7637 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.93 | 16.79 | −65.0% | −37.0569 to −25.2346 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.3 | 1506 | +77.8% | +546.0702 to +772.1298 | yes: LOSS |
| queue: job wait, submitted to its first pod running, mean (s) | 0.0625 | 1160 | +1855900.0% | +1157.0625 to +1162.8125 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1476 | +368950.0% | +1473.0440 to +1478.5560 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 156.2 | 1160 | +642.7% | +889.4167 to +1118.2250 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 24 | +24.000 (native is 0) | +24.0000 to +24.0000 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*