# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.887 |
| node-hours | 2.513 | 2.046 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 239.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 491.4 | 451.8 |
| response time (ms), 95th percentile | 1921 | 1926 |
| response time (ms), 99th percentile | 2658 | 2745 |
| time over the response line (% of samples) | 20.72 | 20.37 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 15.87 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 16.09 |
| utilisation (used / allocatable) | 0.0652 | 0.08072 |
| CPU used (cores), mean | 1.565 | 1.553 |
| Omni's own CPU (cores), mean | 0 | 0.07592 |
| CPU used with Omni's own (cores), mean | 1.565 | 1.629 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.3 | 368.9 |
| HPA replicas, mean | 2.025 | 2.32 |
| pods started | 0.2 | 1.3 |
| pod start wait, total (s) | 0.4 | 3.3 |
| pod start wait, mean (s) | 0.4 | 1.2 |
| host CPU busy, the real machine under kind (%) | 44.95 | 47.99 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 830.2 | 834.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.092 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3167 | 0.225 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 135.4 | 139.7 |
| queue: jobs unfinished at the window's end | 0 | 0 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |

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
| worker nodes in service, mean | 6 | 4.887 | −18.5% | −1.9503 to −0.2750 | yes: GAIN |
| node-hours | 2.513 | 2.046 | −18.6% | −0.8207 to −0.1141 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274.1 | −0.0% | −1.0917 to +0.9635 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 239.1 | −12.8% | −61.6897 to −8.4010 | yes: GAIN |
| response time (ms), mean | 491.4 | 451.8 | −8.1% | −97.1444 to +18.0067 | no |
| response time (ms), 95th percentile | 1921 | 1926 | +0.3% | −202.7950 to +213.8260 | no |
| response time (ms), 99th percentile | 2658 | 2745 | +3.3% | −300.0161 to +473.9287 | no |
| time over the response line (% of samples) | 20.72 | 20.37 | −1.7% | −0.9294 to +0.2380 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.3 | −3.7% | −1.3048 to +0.5048 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.9 | +100.900 (native is 0) | +17.4813 to +184.3187 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 16.09 | +5.6% | −4.4758 to +6.1858 | no |
| utilisation (used / allocatable) | 0.0652 | 0.08072 | +23.8% | +0.0032 to +0.0278 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.565 | 1.553 | −0.7% | −0.0458 to +0.0228 | no |
| Omni's own CPU (cores), mean | 0 | 0.07592 | +0.076 (native is 0) | +0.0711 to +0.0808 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.565 | 1.629 | +4.1% | +0.0285 to +0.1002 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 430.3 | 368.9 | −14.3% | −111.8182 to −10.9376 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.32 | +14.5% | +0.1165 to +0.4722 | yes: power given |
| pods started | 0.2 | 1.3 | +550.0% | −0.2254 to +2.4254 | no |
| pod start wait, total (s) | 0.4 | 3.3 | +725.0% | −0.5790 to +6.3790 | no |
| pod start wait, mean (s) | 0.4 | 1.2 | +200.0% | −0.5297 to +2.1297 | no |
| host CPU busy, the real machine under kind (%) | 44.95 | 47.99 | +6.8% | +2.1600 to +3.9274 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 830.2 | 834.9 | +0.6% | −11.0116 to +20.4116 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.092 | −31.8% | −3.1375 to −0.6777 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3167 | 0.225 | −28.9% | −0.5830 to +0.3996 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 0.6 | −53.8% | −2.5790 to +1.1790 | no |
| queue: job turnaround, submitted to done, mean (s) | 135.4 | 139.7 | +3.2% | −12.0861 to +20.7361 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*