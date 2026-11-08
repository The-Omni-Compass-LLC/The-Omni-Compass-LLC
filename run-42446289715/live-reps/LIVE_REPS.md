# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 3.784 | 3.749 |
| node-hours | 2.515 | 2.516 | 1.589 | 1.573 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.5 | 270.9 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.5 | 201.1 | 200.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 227.9 | 215.6 | 213.3 | 188.7 |
| response time (ms), 95th percentile | 754.8 | 797.5 | 848.8 | 802.2 |
| response time (ms), 99th percentile | 1077 | 1120 | 1248 | 1151 |
| time over the response line (% of samples) | 7.223 | 5.481 | 7.232 | 4.965 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 3.2 | 4.6 | 3.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 185.8 | 168.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 16.67 | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.033 | 8.775 | 8.923 | 8.808 |
| utilisation (used / allocatable) | 0.055 | 0.05397 | 0.08699 | 0.08854 |
| CPU used (cores), mean | 1.32 | 1.295 | 1.29 | 1.291 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.06607 | 0.06546 |
| CPU used with Omni's own (cores), mean | 1.32 | 1.295 | 1.356 | 1.357 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.2 | 510.8 | 372.3 | 369.4 |
| HPA replicas, mean | 1.916 | 1.993 | 2.028 | 2.136 |
| pods started | 0.1 | 0 | 0.7 | 0.6 |
| pod start wait, total (s) | 0.2 | 0 | 1.5 | 1.1 |
| pod start wait, mean (s) | 0.2 | 0 | 0.625 | 0.55 |
| host CPU busy, the real machine under kind (%) | 36.99 | 36.96 | 39.99 | 39.91 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 755.1 | 755.8 | 757.6 | 758.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 2.738 | 2.919 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.02917 | 0.03333 | 0.025 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | 0.3 | 0.1 |
| queue: job turnaround, submitted to done, mean (s) | 59.86 | 62.11 | 62.91 | 65.18 |
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
| worker nodes in service, mean | 6 | 3.749 | −37.5% | −3.1169 to −1.3852 | yes: GAIN |
| node-hours | 2.516 | 1.573 | −37.5% | −1.3100 to −0.5765 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270.9 | +0.1% | −0.5187 to +1.2727 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 200.2 | −26.0% | −97.9645 to −42.7148 | yes: GAIN |
| response time (ms), mean | 215.6 | 188.7 | −12.5% | −39.7614 to −14.0267 | yes: GAIN |
| response time (ms), 95th percentile | 797.5 | 802.2 | +0.6% | −15.3646 to +24.6986 | no |
| response time (ms), 99th percentile | 1120 | 1151 | +2.8% | −78.3180 to +140.1958 | no |
| time over the response line (% of samples) | 5.481 | 4.965 | −9.4% | −1.3683 to +0.3363 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 3.3 | +3.1% | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 168.9 | +168.900 (native is 0) | +106.7433 to +231.0567 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.775 | 8.808 | +0.4% | −1.8276 to +1.8943 | no |
| utilisation (used / allocatable) | 0.05397 | 0.08854 | +64.1% | +0.0214 to +0.0478 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.295 | 1.291 | −0.3% | −0.0270 to +0.0193 | no |
| Omni's own CPU (cores), mean | 0 | 0.06546 | +0.065 (native is 0) | +0.0571 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.295 | 1.357 | +4.8% | +0.0365 to +0.0867 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.8 | 369.4 | −27.7% | −196.6469 to −86.2107 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.993 | 2.136 | +7.2% | −0.0739 to +0.3607 | no |
| pods started | 0 | 0.6 | +0.600 (native is 0) | −0.0911 to +1.2911 | no |
| pod start wait, total (s) | 0 | 1.1 | +1.100 (native is 0) | −0.2254 to +2.4254 | no |
| pod start wait, mean (s) | 0 | 0.55 | +0.550 (native is 0) | −0.1127 to +1.2127 | no |
| host CPU busy, the real machine under kind (%) | 36.96 | 39.91 | +8.0% | +2.5608 to +3.3438 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.8 | 758.5 | +0.4% | −0.7396 to +6.1396 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.919 | −51.4% | −4.2564 to −1.9061 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.025 | −14.3% | −0.0303 to +0.0219 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.11 | 65.18 | +5.0% | +0.0622 to +6.0878 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.515 | 2.516 | +0.0% | −0.0042 to +0.0065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.5 | −0.1% | −1.1046 to +0.7798 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 270.5 | −0.1% | −1.1046 to +0.7798 | no |
| response time (ms), mean | 227.9 | 215.6 | −5.4% | −19.4356 to −5.1468 | yes: GAIN |
| response time (ms), 95th percentile | 754.8 | 797.5 | +5.7% | −75.2668 to +160.7258 | no |
| response time (ms), 99th percentile | 1077 | 1120 | +4.0% | −124.2667 to +209.8523 | no |
| time over the response line (% of samples) | 7.223 | 5.481 | −24.1% | −3.9392 to +0.4550 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 3.2 | −20.0% | −1.9583 to +0.3583 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.033 | 8.775 | +9.2% | −0.8545 to +2.3378 | no |
| utilisation (used / allocatable) | 0.055 | 0.05397 | −1.9% | −0.0024 to +0.0004 | no |
| CPU used (cores), mean | 1.32 | 1.295 | −1.9% | −0.0584 to +0.0086 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.32 | 1.295 | −1.9% | −0.0584 to +0.0086 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.2 | 510.8 | +2.3% | −3.2037 to +26.3173 | no |
| HPA replicas, mean | 1.916 | 1.993 | +4.0% | −0.0635 to +0.2160 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| pod start wait, mean (s) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| host CPU busy, the real machine under kind (%) | 36.99 | 36.96 | −0.1% | −0.5580 to +0.4912 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.1 | 755.8 | +0.1% | −2.7064 to +4.1064 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.02917 | −12.5% | −0.0262 to +0.0178 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.86 | 62.11 | +3.8% | −2.4872 to +6.9788 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.784 | −36.9% | −2.9750 to −1.4565 | yes: GAIN |
| node-hours | 2.515 | 1.589 | −36.8% | −1.2459 to −0.6069 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 | +0.1% | −0.9170 to +1.2803 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 201.1 | −25.7% | −93.7254 to −45.3404 | yes: GAIN |
| response time (ms), mean | 227.9 | 213.3 | −6.4% | −21.6970 to −7.4516 | yes: GAIN |
| response time (ms), 95th percentile | 754.8 | 848.8 | +12.5% | +3.6450 to +184.3040 | yes: LOSS |
| response time (ms), 99th percentile | 1077 | 1248 | +15.9% | +0.5578 to +340.9426 | yes: LOSS |
| time over the response line (% of samples) | 7.223 | 7.232 | +0.1% | −0.7338 to +0.7524 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 4.6 | +15.0% | −0.5285 to +1.7285 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 185.8 | +185.800 (native is 0) | +120.5489 to +251.0511 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.033 | 8.923 | +11.1% | −0.6587 to +2.4387 | no |
| utilisation (used / allocatable) | 0.055 | 0.08699 | +58.2% | +0.0203 to +0.0437 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.32 | 1.29 | −2.3% | −0.0711 to +0.0115 | no |
| Omni's own CPU (cores), mean | 0 | 0.06607 | +0.066 (native is 0) | +0.0583 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.32 | 1.356 | +2.7% | −0.0086 to +0.0810 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.2 | 372.3 | −25.4% | −174.2006 to −79.7707 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.916 | 2.028 | +5.8% | −0.0385 to +0.2627 | no |
| pods started | 0.1 | 0.7 | +600.0% | −0.1689 to +1.3689 | no |
| pod start wait, total (s) | 0.2 | 1.5 | +650.0% | −0.4210 to +3.0210 | no |
| pod start wait, mean (s) | 0.2 | 0.625 | +212.5% | −0.1714 to +1.0214 | no |
| host CPU busy, the real machine under kind (%) | 36.99 | 39.99 | +8.1% | +2.2342 to +3.7730 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.1 | 757.6 | +0.3% | −0.3860 to +5.3860 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.738 | −54.4% | −4.1969 to −2.3261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.03333 | 0.0% | raw −0.0372 to +0.0372 | STEADY, the same (to nine decimal places) |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.86 | 62.91 | +5.1% | −0.7905 to +6.8822 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.784 | −36.9% | −2.9750 to −1.4565 | yes: GAIN |
| node-hours | 2.516 | 1.589 | −36.9% | −1.2479 to −0.6071 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270.9 | +0.1% | −0.3034 to +0.9916 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 201.1 | −25.6% | −93.4496 to −45.2914 | yes: GAIN |
| response time (ms), mean | 215.6 | 213.3 | −1.1% | −8.2717 to +3.7055 | no |
| response time (ms), 95th percentile | 797.5 | 848.8 | +6.4% | +10.4813 to +92.0087 | yes: LOSS |
| response time (ms), 99th percentile | 1120 | 1248 | +11.4% | −43.8631 to +299.7779 | no |
| time over the response line (% of samples) | 5.481 | 7.232 | +32.0% | +0.0852 to +3.4176 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.2 | 4.6 | +43.7% | −0.8163 to +3.6163 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 185.8 | +185.800 (native is 0) | +120.5489 to +251.0511 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.775 | 8.923 | +1.7% | −1.3506 to +1.6473 | no |
| utilisation (used / allocatable) | 0.05397 | 0.08699 | +61.2% | +0.0208 to +0.0452 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.295 | 1.29 | −0.4% | −0.0254 to +0.0155 | no |
| Omni's own CPU (cores), mean | 0 | 0.06607 | +0.066 (native is 0) | +0.0583 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.295 | 1.356 | +4.7% | +0.0386 to +0.0837 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 510.8 | 372.3 | −27.1% | −191.4125 to −85.6724 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.993 | 2.028 | +1.8% | −0.0770 to +0.1487 | no |
| pods started | 0 | 0.7 | +0.700 (native is 0) | −0.2567 to +1.6567 | no |
| pod start wait, total (s) | 0 | 1.5 | +1.500 (native is 0) | −0.6125 to +3.6125 | no |
| pod start wait, mean (s) | 0 | 0.625 | +0.625 (native is 0) | −0.0965 to +1.3465 | no |
| host CPU busy, the real machine under kind (%) | 36.96 | 39.99 | +8.2% | +2.5126 to +3.5614 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.8 | 757.6 | +0.2% | −1.1163 to +4.7163 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.738 | −54.4% | −4.1969 to −2.3261 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.03333 | +14.3% | −0.0342 to +0.0425 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.3 | +200.0% | −0.1016 to +0.5016 | no |
| queue: job turnaround, submitted to done, mean (s) | 62.11 | 62.91 | +1.3% | −1.6534 to +3.2534 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.749 | −37.5% | −3.1169 to −1.3852 | yes: GAIN |
| node-hours | 2.515 | 1.573 | −37.5% | −1.3079 to −0.5762 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.7 | 270.9 | +0.1% | −0.7917 to +1.2208 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.7 | 200.2 | −26.0% | −98.1825 to −42.8216 | yes: GAIN |
| response time (ms), mean | 227.9 | 188.7 | −17.2% | −58.7516 to −19.6189 | yes: GAIN |
| response time (ms), 95th percentile | 754.8 | 802.2 | +6.3% | −85.1908 to +179.9838 | no |
| response time (ms), 99th percentile | 1077 | 1151 | +6.8% | −68.6629 to +216.1263 | no |
| time over the response line (% of samples) | 7.223 | 4.965 | −31.3% | −5.2593 to +0.7431 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4 | 3.3 | −17.5% | −1.6567 to +0.2567 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 168.9 | +168.900 (native is 0) | +106.7433 to +231.0567 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 8.033 | 8.808 | +9.6% | −0.2696 to +1.8196 | no |
| utilisation (used / allocatable) | 0.055 | 0.08854 | +61.0% | +0.0208 to +0.0463 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.32 | 1.291 | −2.2% | −0.0657 to +0.0082 | no |
| Omni's own CPU (cores), mean | 0 | 0.06546 | +0.065 (native is 0) | +0.0571 to +0.0738 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.32 | 1.357 | +2.8% | −0.0047 to +0.0781 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 499.2 | 369.4 | −26.0% | −179.6096 to −80.1343 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.916 | 2.136 | +11.5% | +0.0288 to +0.4106 | yes: power given |
| pods started | 0.1 | 0.6 | +500.0% | −0.1079 to +1.1079 | no |
| pod start wait, total (s) | 0.2 | 1.1 | +450.0% | −0.3367 to +2.1367 | no |
| pod start wait, mean (s) | 0.2 | 0.55 | +175.0% | −0.3041 to +1.0041 | no |
| host CPU busy, the real machine under kind (%) | 36.99 | 39.91 | +7.9% | +2.3080 to +3.5298 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.1 | 758.5 | +0.5% | −1.2991 to +8.0991 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 2.919 | −51.4% | −4.2564 to −1.9061 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.03333 | 0.025 | −25.0% | −0.0391 to +0.0224 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job turnaround, submitted to done, mean (s) | 59.86 | 65.18 | +8.9% | −1.1035 to +11.7451 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*