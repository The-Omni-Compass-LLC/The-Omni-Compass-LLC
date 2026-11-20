# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.047 |
| node-hours | 2.514 | 2.115 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 243.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 366.5 | 348.6 |
| response time (ms), 95th percentile | 1317 | 1431 |
| response time (ms), 99th percentile | 1886 | 1991 |
| time over the response line (% of samples) | 14.56 | 14.76 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 33.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.9 | 13.52 |
| utilisation (used / allocatable) | 0.06202 | 0.07405 |
| CPU used (cores), mean | 1.488 | 1.478 |
| Omni's own CPU (cores), mean | 0 | 0.07309 |
| CPU used with Omni's own (cores), mean | 1.488 | 1.551 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.3 | 395 |
| HPA replicas, mean | 2.075 | 2.351 |
| pods started | 0 | 1.1 |
| pod start wait, total (s) | 0 | 2.8 |
| pod start wait, mean (s) | 0 | 1.35 |
| host CPU busy, the real machine under kind (%) | 42.57 | 45.59 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 790.8 | 798.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.34 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 94.63 | 102.7 |
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
| worker nodes in service, mean | 6 | 5.047 | −15.9% | −1.6524 to −0.2538 | yes: GAIN |
| node-hours | 2.514 | 2.115 | −15.9% | −0.6902 to −0.1081 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.1 | −0.0% | −0.7066 to +0.6089 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 243.2 | −11.0% | −51.9196 to −8.0282 | yes: GAIN |
| response time (ms), mean | 366.5 | 348.6 | −4.9% | −26.9599 to −8.9030 | yes: GAIN |
| response time (ms), 95th percentile | 1317 | 1431 | +8.7% | +11.5083 to +217.4177 | yes: LOSS |
| response time (ms), 99th percentile | 1886 | 1991 | +5.6% | −40.3213 to +249.7629 | no |
| time over the response line (% of samples) | 14.56 | 14.76 | +1.4% | −0.6855 to +1.0958 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.4 | +5.6% | −0.6802 to +1.6802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.1 | +117.100 (native is 0) | +38.0468 to +196.1532 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.9 | 13.52 | +24.1% | −0.5127 to +5.7560 | no |
| utilisation (used / allocatable) | 0.06202 | 0.07405 | +19.4% | +0.0020 to +0.0220 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.488 | 1.478 | −0.7% | −0.0353 to +0.0148 | no |
| Omni's own CPU (cores), mean | 0 | 0.07309 | +0.073 (native is 0) | +0.0686 to +0.0776 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.488 | 1.551 | +4.2% | +0.0343 to +0.0914 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.3 | 395 | −11.5% | −90.0666 to −12.5356 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.075 | 2.351 | +13.3% | +0.0159 to +0.5347 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.1198 to +2.0802 | yes: power given |
| pod start wait, total (s) | 0 | 2.8 | +2.800 (native is 0) | +0.5180 to +5.0820 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.35 | +1.350 (native is 0) | +0.3100 to +2.3900 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.57 | 45.59 | +7.1% | +2.6693 to +3.3718 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 790.8 | 798.8 | +1.0% | +1.5226 to +14.4774 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.34 | −27.7% | −2.7639 to −0.5552 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.04583 | 0.1333 | +190.9% | −0.0040 to +0.1790 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.8 | +100.0% | −0.2032 to +1.0032 | no |
| queue: job turnaround, submitted to done, mean (s) | 94.63 | 102.7 | +8.6% | +1.0601 to +15.1316 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*