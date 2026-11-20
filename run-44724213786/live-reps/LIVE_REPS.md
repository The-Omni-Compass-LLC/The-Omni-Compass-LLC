# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | the organism alone (no orchestrator) | native | omni on the organism alone | omni |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 6 |
| node-hours | 1.513 | 1.515 | 1.515 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.6 | 158.8 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.6 | 158.8 | 159.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan | nan | nan |
| response time (ms), mean | 114 | 116.7 | 115.1 | 119.9 |
| response time (ms), 95th percentile | 232.4 | 238.8 | 237.4 | 246 |
| response time (ms), 99th percentile | 338.7 | 338.4 | 335.7 | 346.1 |
| time over the response line (% of samples) | 0.1151 | 0.206 | 0.1406 | 0.3337 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | 5.1 | 5.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan | 100 | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.105 | 0.3167 | 0.1917 |
| utilisation (used / allocatable) | 0.03663 | 0.04061 | 0.03691 | 0.04121 |
| CPU used (cores), mean | 0.8791 | 0.9746 | 0.8859 | 0.989 |
| Omni's own CPU (cores), mean | 0 | 0 | 0.02813 | 0.04428 |
| CPU used with Omni's own (cores), mean | 0.8791 | 0.9746 | 0.914 | 1.033 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.5 | 650.3 | 713.2 | 643.3 |
| HPA replicas, mean | 8.846 | 8.836 | 9.631 | 9.577 |
| pods started | 4.8 | 4.8 | 6.3 | 6.9 |
| pod start wait, total (s) | 7.1 | 7.8 | 8.4 | 9.7 |
| pod start wait, mean (s) | 1.487 | 1.58 | 1.336 | 1.402 |
| host CPU busy, the real machine under kind (%) | 26.72 | 30.02 | 27.7 | 32.11 |
| host cores (the real machine under kind) | 4 | 4 | 4 | 4 |
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
| node-hours | 1.515 | 1.512 | −0.2% | −0.0126 to +0.0056 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 159.4 | −0.2% | −1.0703 to +0.5806 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 159.4 | −0.2% | −1.0703 to +0.5806 | no |
| response time (ms), mean | 116.7 | 119.9 | +2.8% | −0.1236 to +6.5566 | no |
| response time (ms), 95th percentile | 238.8 | 246 | +3.0% | −7.8372 to +22.3092 | no |
| response time (ms), 99th percentile | 338.4 | 346.1 | +2.3% | −10.9037 to +26.4445 | no |
| time over the response line (% of samples) | 0.206 | 0.3337 | +62.0% | +0.0134 to +0.2419 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.500 (native is 0) | +3.8395 to +7.1605 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.1917 | +82.5% | −0.1754 to +0.3487 | no |
| utilisation (used / allocatable) | 0.04061 | 0.04121 | +1.5% | −0.0004 to +0.0016 | no |
| CPU used (cores), mean | 0.9746 | 0.989 | +1.5% | −0.0089 to +0.0378 | no |
| Omni's own CPU (cores), mean | 0 | 0.04428 | +0.044 (native is 0) | +0.0374 to +0.0511 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9746 | 1.033 | +6.0% | +0.0296 to +0.0879 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 650.3 | 643.3 | −1.1% | −20.7996 to +6.8932 | no |
| HPA replicas, mean | 8.836 | 9.577 | +8.4% | −0.0458 to +1.5272 | no |
| pods started | 4.8 | 6.9 | +43.8% | +0.0642 to +4.1358 | yes: power given |
| pod start wait, total (s) | 7.8 | 9.7 | +24.4% | −1.5790 to +5.3790 | no |
| pod start wait, mean (s) | 1.58 | 1.402 | −11.2% | −0.5497 to +0.1946 | no |
| host CPU busy, the real machine under kind (%) | 30.02 | 32.11 | +6.9% | +1.2782 to +2.8839 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## the orchestrator as shipped vs the organism alone (what the orchestrator does on its own), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | native | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.1% | −0.0081 to +0.0125 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.6 | +0.7% | +0.0404 to +2.2175 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.6 | +0.7% | +0.0404 to +2.2175 | yes: power given |
| response time (ms), mean | 114 | 116.7 | +2.3% | −0.6809 to +5.9724 | no |
| response time (ms), 95th percentile | 232.4 | 238.8 | +2.7% | −5.1805 to +17.9495 | no |
| response time (ms), 99th percentile | 338.7 | 338.4 | −0.1% | −28.9210 to +28.2444 | no |
| time over the response line (% of samples) | 0.1151 | 0.206 | +79.1% | −0.0473 to +0.2293 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.105 | −33.7% | −0.2676 to +0.1609 | no |
| utilisation (used / allocatable) | 0.03663 | 0.04061 | +10.9% | +0.0035 to +0.0045 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8791 | 0.9746 | +10.9% | +0.0833 to +0.1077 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| CPU used with Omni's own (cores), mean | 0.8791 | 0.9746 | +10.9% | +0.0833 to +0.1077 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.5 | 650.3 | −9.2% | −73.0780 to −59.4288 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.846 | 8.836 | −0.1% | −0.2230 to +0.2030 | no |
| pods started | 4.8 | 4.8 | ±0.0% | −1.2158 to +1.2158 | no |
| pod start wait, total (s) | 7.1 | 7.8 | +9.9% | −2.2406 to +3.6406 | no |
| pod start wait, mean (s) | 1.487 | 1.58 | +6.3% | −0.1885 to +0.3752 | no |
| host CPU busy, the real machine under kind (%) | 26.72 | 30.02 | +12.4% | +2.8827 to +3.7357 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the organism alone (Omni-Compass without the orchestrator), 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.515 | +0.2% | −0.0056 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 158.8 | +0.2% | −0.4027 to +1.0383 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 158.8 | +0.2% | −0.4027 to +1.0383 | no |
| response time (ms), mean | 114 | 115.1 | +1.0% | −2.7425 to +4.9167 | no |
| response time (ms), 95th percentile | 232.4 | 237.4 | +2.1% | −7.4042 to +17.3862 | no |
| response time (ms), 99th percentile | 338.7 | 335.7 | −0.9% | −25.8833 to +19.9511 | no |
| time over the response line (% of samples) | 0.1151 | 0.1406 | +22.2% | −0.1161 to +0.1672 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.1 | +5.100 (native is 0) | +3.6516 to +6.5484 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.3167 | +100.0% | −0.1689 to +0.4856 | no |
| utilisation (used / allocatable) | 0.03663 | 0.03691 | +0.8% | −0.0007 to +0.0012 | no |
| CPU used (cores), mean | 0.8791 | 0.8859 | +0.8% | −0.0160 to +0.0296 | no |
| Omni's own CPU (cores), mean | 0 | 0.02813 | +0.028 (native is 0) | +0.0238 to +0.0325 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8791 | 0.914 | +4.0% | +0.0088 to +0.0611 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.5 | 713.2 | −0.5% | −19.9059 to +13.2516 | no |
| HPA replicas, mean | 8.846 | 9.631 | +8.9% | −0.1700 to +1.7399 | no |
| pods started | 4.8 | 6.3 | +31.2% | −0.1605 to +3.1605 | no |
| pod start wait, total (s) | 7.1 | 8.4 | +18.3% | −1.1093 to +3.7093 | no |
| pod start wait, mean (s) | 1.487 | 1.336 | −10.1% | −0.4447 to +0.1442 | no |
| host CPU busy, the real machine under kind (%) | 26.72 | 27.7 | +3.7% | +0.3900 to +1.5875 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on the organism alone vs the orchestrator as shipped, 10 paired repetitions

| Gauge | native | omni on the organism alone | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.515 | +0.0% | −0.0103 to +0.0106 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 159.6 | 158.8 | −0.5% | −1.8594 to +0.2371 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.6 | 158.8 | −0.5% | −1.8594 to +0.2371 | no |
| response time (ms), mean | 116.7 | 115.1 | −1.3% | −4.8478 to +1.7304 | no |
| response time (ms), 95th percentile | 238.8 | 237.4 | −0.6% | −15.3952 to +12.6082 | no |
| response time (ms), 99th percentile | 338.4 | 335.7 | −0.8% | −33.9313 to +28.6757 | no |
| time over the response line (% of samples) | 0.206 | 0.1406 | −31.7% | −0.2039 to +0.0730 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.1 | +5.100 (native is 0) | +3.6516 to +6.5484 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.105 | 0.3167 | +201.6% | −0.0216 to +0.4450 | no |
| utilisation (used / allocatable) | 0.04061 | 0.03691 | −9.1% | −0.0045 to −0.0029 | yes, down (shown, not judged) |
| CPU used (cores), mean | 0.9746 | 0.8859 | −9.1% | −0.1076 to −0.0697 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02813 | +0.028 (native is 0) | +0.0238 to +0.0325 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.9746 | 0.914 | −6.2% | −0.0821 to −0.0390 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 650.3 | 713.2 | +9.7% | +46.6489 to +79.2036 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.836 | 9.631 | +9.0% | −0.1070 to +1.6968 | no |
| pods started | 4.8 | 6.3 | +31.2% | −0.8664 to +3.8664 | no |
| pod start wait, total (s) | 7.8 | 8.4 | +7.7% | −3.3926 to +4.5926 | no |
| pod start wait, mean (s) | 1.58 | 1.336 | −15.4% | −0.6064 to +0.1192 | no |
| host CPU busy, the real machine under kind (%) | 30.02 | 27.7 | −7.7% | −2.6706 to −1.9702 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## omni on top of the orchestrator vs the organism alone, 10 paired repetitions

| Gauge | the organism alone (no orchestrator) | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw +0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.513 | 1.512 | −0.1% | −0.0085 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 159.4 | +0.6% | +0.1110 to +1.6572 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 159.4 | +0.6% | +0.1110 to +1.6572 | yes: power given |
| response time (ms), mean | 114 | 119.9 | +5.1% | +2.0554 to +9.6691 | yes: LOSS |
| response time (ms), 95th percentile | 232.4 | 246 | +5.9% | +0.1749 to +27.0661 | yes: LOSS |
| response time (ms), 99th percentile | 338.7 | 346.1 | +2.2% | −19.8801 to +34.7443 | no |
| time over the response line (% of samples) | 0.1151 | 0.3337 | +190.0% | −0.0005 to +0.4378 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 5.5 | +5.500 (native is 0) | +3.8395 to +7.1605 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1583 | 0.1917 | +21.1% | −0.3142 to +0.3809 | no |
| utilisation (used / allocatable) | 0.03663 | 0.04121 | +12.5% | +0.0033 to +0.0059 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8791 | 0.989 | +12.5% | +0.0794 to +0.1406 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04428 | +0.044 (native is 0) | +0.0374 to +0.0511 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8791 | 1.033 | +17.5% | +0.1177 to +0.1908 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 716.5 | 643.3 | −10.2% | −88.3046 to −58.1085 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.846 | 9.577 | +8.3% | −0.0338 to +1.4951 | no |
| pods started | 4.8 | 6.9 | +43.8% | +0.1208 to +4.0792 | yes: power given |
| pod start wait, total (s) | 7.1 | 9.7 | +36.6% | −0.4572 to +5.6572 | no |
| pod start wait, mean (s) | 1.487 | 1.402 | −5.7% | −0.3145 to +0.1460 | no |
| host CPU busy, the real machine under kind (%) | 26.72 | 32.11 | +20.2% | +4.2910 to +6.4894 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*