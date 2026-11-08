# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.615 |
| node-hours | 2.514 | 1.933 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 228.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 330.1 | 320.2 |
| response time (ms), 95th percentile | 1160 | 1285 |
| response time (ms), 99th percentile | 1629 | 1756 |
| time over the response line (% of samples) | 14.33 | 15.26 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.452 | 11.9 |
| utilisation (used / allocatable) | 0.05979 | 0.07867 |
| CPU used (cores), mean | 1.435 | 1.414 |
| Omni's own CPU (cores), mean | 0 | 0.07341 |
| CPU used with Omni's own (cores), mean | 1.435 | 1.488 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 387 |
| HPA replicas, mean | 1.985 | 2.268 |
| pods started | 0.1 | 1.4 |
| pod start wait, total (s) | 0.1 | 3.2 |
| pod start wait, mean (s) | 0.1 | 1.5 |
| host CPU busy, the real machine under kind (%) | 40.97 | 44.31 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 776.1 | 786.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.871 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.225 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.7 |
| queue: job turnaround, submitted to done, mean (s) | 81.89 | 90.47 |
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
| worker nodes in service, mean | 6 | 4.615 | −23.1% | −2.2994 to −0.4704 | yes: GAIN |
| node-hours | 2.514 | 1.933 | −23.1% | −0.9605 to −0.2013 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 272.1 | −0.1% | −1.2753 to +0.9356 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 228.6 | −16.1% | −72.5801 to −14.8763 | yes: GAIN |
| response time (ms), mean | 330.1 | 320.2 | −3.0% | −29.5992 to +9.7227 | no |
| response time (ms), 95th percentile | 1160 | 1285 | +10.8% | +6.1099 to +243.6881 | yes: LOSS |
| response time (ms), 99th percentile | 1629 | 1756 | +7.8% | −128.5921 to +383.0877 | no |
| time over the response line (% of samples) | 14.33 | 15.26 | +6.5% | +0.0306 to +1.8428 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.7 | 8.7 | +13.0% | +0.1740 to +1.8260 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 134.6 | +134.600 (native is 0) | +52.8759 to +216.3241 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.452 | 11.9 | +25.9% | −1.1164 to +6.0164 | no |
| utilisation (used / allocatable) | 0.05979 | 0.07867 | +31.6% | +0.0067 to +0.0310 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.435 | 1.414 | −1.4% | −0.0685 to +0.0274 | no |
| Omni's own CPU (cores), mean | 0 | 0.07341 | +0.073 (native is 0) | +0.0677 to +0.0791 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.435 | 1.488 | +3.7% | +0.0015 to +0.1042 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.1 | 387 | −16.3% | −120.9764 to −29.3509 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.985 | 2.268 | +14.2% | +0.0854 to +0.4803 | yes: power given |
| pods started | 0.1 | 1.4 | +1300.0% | +0.4706 to +2.1294 | yes: power given |
| pod start wait, total (s) | 0.1 | 3.2 | +3100.0% | +0.8773 to +5.3227 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.5 | +1400.0% | +0.5604 to +2.2396 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.97 | 44.31 | +8.2% | +2.5688 to +4.1238 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.1 | 786.4 | +1.3% | −0.4431 to +21.0431 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.871 | −35.5% | −3.4291 to −0.8279 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.07083 | 0.225 | +217.6% | −0.1874 to +0.4957 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.2 | 1.7 | +750.0% | −1.6677 to +4.6677 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.89 | 90.47 | +10.5% | +0.6260 to +16.5323 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*