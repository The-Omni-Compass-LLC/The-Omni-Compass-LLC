# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.043 | 4.87 |
| node-hours | 2.518 | 2.522 | 2.111 | 2.04 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.9 | 273.3 | 273.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 273.9 | 243.1 | 237.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 371.8 | 390.6 | 353.3 | 367.2 |
| response time (ms), 95th percentile | 1348 | 1419 | 1419 | 1487 |
| response time (ms), 99th percentile | 1852 | 1913 | 1987 | 2042 |
| time over the response line (% of samples) | 14.51 | 15.02 | 15.12 | 14.76 |
| failed requests (%) | 0 | 0.0113 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.4 | 9.9 | 9.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 93.2 | 89.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 25 | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.79 | 12.16 | 13.84 | 14.54 |
| utilisation (used / allocatable) | 0.06184 | 0.06203 | 0.07529 | 0.0767 |
| CPU used (cores), mean | 1.484 | 1.489 | 1.489 | 1.484 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.07376 | 0.07445 |
| CPU used with Omni's own (cores), mean | 1.484 | 1.489 | 1.563 | 1.558 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 447.6 | 394.1 | 385.3 |
| HPA replicas, mean | 2.011 | 1.97 | 2.436 | 2.332 |
| pods started | 0 | 0.2 | 2 | 1.2 |
| pod start wait, total (s) | 0 | 0.6 | 4 | 2.3 |
| pod start wait, mean (s) | 0 | 0.6 | 1.433 | 1.05 |
| host CPU busy, the real machine under kind (%) | 42.58 | 43.17 | 45.79 | 46.57 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
| batch: queue finished (s) | 796.8 | 804.4 | 802 | 809 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | 4.347 | 3.954 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2417 | 0.6875 | 0.175 | 1.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 4.9 | 0.8 | 8.2 |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 107.6 | 107.3 | 112.4 |
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
| worker nodes in service, mean | 6 | 4.87 | −18.8% | −1.8407 to −0.4183 | yes: GAIN |
| node-hours | 2.522 | 2.04 | −19.1% | −0.7788 to −0.1840 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.2 | −0.3% | −1.6906 to +0.1751 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 237.7 | −13.2% | −58.8323 to −13.5874 | yes: GAIN |
| response time (ms), mean | 390.6 | 367.2 | −6.0% | −34.0901 to −12.7801 | yes: GAIN |
| response time (ms), 95th percentile | 1419 | 1487 | +4.8% | +22.5823 to +112.6597 | yes: LOSS |
| response time (ms), 99th percentile | 1913 | 2042 | +6.8% | +1.5915 to +256.6929 | yes: LOSS |
| time over the response line (% of samples) | 15.02 | 14.76 | −1.7% | −0.9930 to +0.4781 | no |
| failed requests (%) | 0.0113 | 0 | −100.0% | −0.0369 to +0.0143 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.5 | +13.1% | +0.2436 to +1.9564 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.5 | +89.500 (native is 0) | +32.7621 to +146.2379 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.16 | 14.54 | +19.6% | −0.1774 to +4.9374 | no |
| utilisation (used / allocatable) | 0.06203 | 0.0767 | +23.6% | +0.0056 to +0.0238 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.489 | 1.484 | −0.3% | −0.0376 to +0.0273 | no |
| Omni's own CPU (cores), mean | 0 | 0.07445 | +0.074 (native is 0) | +0.0681 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.489 | 1.558 | +4.7% | +0.0332 to +0.1054 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.6 | 385.3 | −13.9% | −99.6304 to −24.8891 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.97 | 2.332 | +18.4% | +0.1330 to +0.5909 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | −0.0116 to +2.0116 | no |
| pod start wait, total (s) | 0.6 | 2.3 | +283.3% | −0.6855 to +4.0855 | no |
| pod start wait, mean (s) | 0.6 | 1.05 | +75.0% | −0.8657 to +1.7657 | no |
| host CPU busy, the real machine under kind (%) | 43.17 | 46.57 | +7.9% | +3.0340 to +3.7506 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.4 | 809 | +0.6% | −0.7550 to +9.9550 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.954 | −34.1% | −3.2066 to −0.8864 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6875 | 1.1 | +60.0% | −0.4617 to +1.2867 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.9 | 8.2 | +67.3% | −2.6183 to +9.2183 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.6 | 112.4 | +4.5% | +0.6147 to +8.9853 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.522 | +0.1% | −0.0039 to +0.0102 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.9 | +0.2% | −0.3251 to +1.1587 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 273.9 | +0.2% | −0.3251 to +1.1587 | no |
| response time (ms), mean | 371.8 | 390.6 | +5.1% | −3.7048 to +41.2940 | no |
| response time (ms), 95th percentile | 1348 | 1419 | +5.3% | −2.7189 to +145.3309 | no |
| response time (ms), 99th percentile | 1852 | 1913 | +3.3% | −86.5118 to +207.3866 | no |
| time over the response line (% of samples) | 14.51 | 15.02 | +3.5% | +0.2336 to +0.7845 | yes: LOSS |
| failed requests (%) | 0 | 0.0113 | +0.011 (native is 0) | −0.0143 to +0.0369 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 8.4 | +3.7% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.79 | 12.16 | −5.0% | −4.1866 to +2.9133 | no |
| utilisation (used / allocatable) | 0.06184 | 0.06203 | +0.3% | −0.0007 to +0.0011 | no |
| CPU used (cores), mean | 1.484 | 1.489 | +0.3% | −0.0173 to +0.0266 | no |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 1.484 | 1.489 | +0.3% | −0.0173 to +0.0266 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 447.6 | −0.5% | −8.5622 to +3.8532 | no |
| HPA replicas, mean | 2.011 | 1.97 | −2.0% | −0.1827 to +0.1016 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| pod start wait, mean (s) | 0 | 0.6 | +0.600 (native is 0) | −0.3048 to +1.5048 | no |
| host CPU busy, the real machine under kind (%) | 42.58 | 43.17 | +1.4% | +0.1202 to +1.0624 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.8 | 804.4 | +1.0% | −0.9784 to +16.1784 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2417 | 0.6875 | +184.5% | +0.0362 to +0.8555 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 4.9 | +226.7% | −1.5810 to +8.3810 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 107.6 | +6.2% | −1.1583 to +13.7083 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.043 | −16.0% | −1.7078 to −0.2068 | yes: GAIN |
| node-hours | 2.518 | 2.111 | −16.2% | −0.7175 to −0.0964 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.3 | −0.1% | −1.0968 to +0.7000 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 243.1 | −11.1% | −53.5557 to −7.1786 | yes: GAIN |
| response time (ms), mean | 371.8 | 353.3 | −5.0% | −38.5546 to +1.5815 | no |
| response time (ms), 95th percentile | 1348 | 1419 | +5.3% | +2.8629 to +139.3681 | yes: LOSS |
| response time (ms), 99th percentile | 1852 | 1987 | +7.2% | −50.5255 to +318.8685 | no |
| time over the response line (% of samples) | 14.51 | 15.12 | +4.2% | +0.0449 to +1.1749 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 9.9 | +22.2% | +0.1550 to +3.4450 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93.2 | +93.200 (native is 0) | +29.7619 to +156.6381 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.79 | 13.84 | +8.2% | −1.9160 to +4.0127 | no |
| utilisation (used / allocatable) | 0.06184 | 0.07529 | +21.7% | +0.0029 to +0.0240 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.489 | +0.3% | −0.0147 to +0.0246 | no |
| Omni's own CPU (cores), mean | 0 | 0.07376 | +0.074 (native is 0) | +0.0654 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.563 | +5.3% | +0.0601 to +0.0974 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 394.1 | −12.4% | −97.7324 to −14.0261 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.436 | +21.2% | +0.1229 to +0.7283 | yes: power given |
| pods started | 0 | 2 | +2.000 (native is 0) | +0.9337 to +3.0663 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +1.8409 to +6.1591 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.433 | +1.433 (native is 0) | +0.6685 to +2.1981 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.58 | 45.79 | +7.5% | +2.6458 to +3.7585 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.8 | 802 | +0.7% | −2.7496 to +13.1496 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.347 | −27.6% | −2.8252 to −0.4811 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2417 | 0.175 | −27.6% | −0.4355 to +0.3022 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 0.8 | −46.7% | −2.8604 to +1.4604 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 107.3 | +6.0% | −1.7924 to +13.8507 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.043 | −16.0% | −1.7078 to −0.2068 | yes: GAIN |
| node-hours | 2.522 | 2.111 | −16.3% | −0.7217 to −0.0985 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 273.3 | −0.2% | −1.4979 to +0.2675 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 243.1 | −11.2% | −54.1083 to −7.4596 | yes: GAIN |
| response time (ms), mean | 390.6 | 353.3 | −9.5% | −54.5598 to −20.0024 | yes: GAIN |
| response time (ms), 95th percentile | 1419 | 1419 | −0.0% | −36.6592 to +36.2782 | no |
| response time (ms), 99th percentile | 1913 | 1987 | +3.9% | +7.6322 to +139.8360 | yes: LOSS |
| time over the response line (% of samples) | 15.02 | 15.12 | +0.7% | −0.4896 to +0.6914 | no |
| failed requests (%) | 0.0113 | 0 | −100.0% | −0.0369 to +0.0143 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.4 | 9.9 | +17.9% | −0.1605 to +3.1605 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93.2 | +93.200 (native is 0) | +29.7619 to +156.6381 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.16 | 13.84 | +13.9% | −0.3402 to +3.7102 | no |
| utilisation (used / allocatable) | 0.06203 | 0.07529 | +21.4% | +0.0028 to +0.0237 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.489 | 1.489 | +0.0% | −0.0324 to +0.0331 | no |
| Omni's own CPU (cores), mean | 0 | 0.07376 | +0.074 (native is 0) | +0.0654 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.489 | 1.563 | +5.0% | +0.0428 to +0.1053 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.6 | 394.1 | −12.0% | −94.6394 to −12.4100 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.97 | 2.436 | +23.7% | +0.2260 to +0.7063 | yes: power given |
| pods started | 0.2 | 2 | +900.0% | +0.7444 to +2.8556 | yes: power given |
| pod start wait, total (s) | 0.6 | 4 | +566.7% | +1.0590 to +5.7410 | yes: LOSS |
| pod start wait, mean (s) | 0.6 | 1.433 | +138.9% | −0.2822 to +1.9489 | no |
| host CPU busy, the real machine under kind (%) | 43.17 | 45.79 | +6.0% | +2.2488 to +2.9730 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 804.4 | 802 | −0.3% | −5.2850 to +0.4850 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.347 | −27.6% | −2.8252 to −0.4811 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6875 | 0.175 | −74.5% | −1.1772 to +0.1522 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.9 | 0.8 | −83.7% | −11.1122 to +2.9122 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.6 | 107.3 | −0.2% | −3.3623 to +2.8706 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.87 | −18.8% | −1.8407 to −0.4183 | yes: GAIN |
| node-hours | 2.518 | 2.04 | −19.0% | −0.7773 to −0.1791 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 273.2 | −0.1% | −1.2549 to +0.5731 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 237.7 | −13.1% | −58.4671 to −13.1189 | yes: GAIN |
| response time (ms), mean | 371.8 | 367.2 | −1.2% | −25.2800 to +15.9990 | no |
| response time (ms), 95th percentile | 1348 | 1487 | +10.3% | +22.2054 to +255.6486 | yes: LOSS |
| response time (ms), 99th percentile | 1852 | 2042 | +10.2% | +7.1525 to +372.0067 | yes: LOSS |
| time over the response line (% of samples) | 14.51 | 14.76 | +1.7% | −0.3199 to +0.8230 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.1 | 9.5 | +17.3% | +0.4952 to +2.3048 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.5 | +89.500 (native is 0) | +32.7621 to +146.2379 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.79 | 14.54 | +13.6% | −1.8354 to +5.3220 | no |
| utilisation (used / allocatable) | 0.06184 | 0.0767 | +24.0% | +0.0054 to +0.0243 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.484 | 1.484 | −0.0% | −0.0258 to +0.0249 | no |
| Omni's own CPU (cores), mean | 0 | 0.07445 | +0.074 (native is 0) | +0.0681 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.484 | 1.558 | +5.0% | +0.0443 to +0.1037 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 385.3 | −14.4% | −104.5757 to −24.6528 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.011 | 2.332 | +16.0% | +0.0899 to +0.5530 | yes: power given |
| pods started | 0 | 1.2 | +1.200 (native is 0) | +0.3207 to +2.0793 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | +0.3910 to +4.2090 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.05 | +1.050 (native is 0) | +0.3171 to +1.7829 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.58 | 46.57 | +9.4% | +3.4572 to +4.5101 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 796.8 | 809 | +1.5% | +1.5646 to +22.8354 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.954 | −34.1% | −3.2066 to −0.8864 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2417 | 1.1 | +355.2% | −0.3490 to +2.0657 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 8.2 | +446.7% | −3.3032 to +16.7032 | no |
| queue: job turnaround, submitted to done, mean (s) | 101.3 | 112.4 | +10.9% | +1.1553 to +20.9947 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*