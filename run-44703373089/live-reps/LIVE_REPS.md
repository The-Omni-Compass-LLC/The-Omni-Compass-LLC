# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.938 |
| node-hours | 2.515 | 2.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 269 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 127.2 | 128.7 |
| response time (ms), 95th percentile | 222.6 | 232.7 |
| response time (ms), 99th percentile | 320.8 | 339.7 |
| time over the response line (% of samples) | 0.1923 | 0.2091 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1030 | 1119 |
| utilisation (used / allocatable) | 0.05885 | 0.05691 |
| CPU used (cores), mean | 1.412 | 1.353 |
| Omni's own CPU (cores), mean | 0 | 0.06631 |
| CPU used with Omni's own (cores), mean | 1.412 | 1.419 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 475.7 |
| HPA replicas, mean | 1.976 | 2.08 |
| pods started | 0.2 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.6 |
| pod start wait, mean (s) | 0.4 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43.75 | 45.35 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1401 | 1440 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.194 |
| queue: job wait, submitted to its first pod running, mean (s) | 114.7 | 161.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 579.5 | 677.9 |
| queue: job turnaround, submitted to done, mean (s) | 750 | 787.1 |
| queue: jobs unfinished at the window's end | 9.2 | 10 |
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
| worker nodes in service, mean | 6 | 5.938 | −1.0% | −0.1830 to +0.0581 | no |
| node-hours | 2.515 | 2.49 | −1.0% | −0.0774 to +0.0284 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271 | −0.3% | −1.8454 to −0.0072 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 269 | −1.1% | −6.7377 to +0.9602 | no |
| response time (ms), mean | 127.2 | 128.7 | +1.2% | −1.3507 to +4.3398 | no |
| response time (ms), 95th percentile | 222.6 | 232.7 | +4.5% | −0.3240 to +20.4780 | no |
| response time (ms), 99th percentile | 320.8 | 339.7 | +5.9% | −1.8528 to +39.7050 | no |
| time over the response line (% of samples) | 0.1923 | 0.2091 | +8.7% | −0.1230 to +0.1566 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 58.6 | +58.600 (native is 0) | +15.9111 to +101.2889 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1030 | 1119 | +8.7% | +36.3080 to +143.6287 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05885 | 0.05691 | −3.3% | −0.0040 to +0.0001 | no |
| CPU used (cores), mean | 1.412 | 1.353 | −4.2% | −0.0958 to −0.0230 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06631 | +0.066 (native is 0) | +0.0599 to +0.0728 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.412 | 1.419 | +0.5% | −0.0283 to +0.0422 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 462.2 | 475.7 | +2.9% | −1.1432 to +28.1028 | no |
| HPA replicas, mean | 1.976 | 2.08 | +5.3% | −0.1473 to +0.3551 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.6872 to +0.8872 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −1.3744 to +1.7744 | no |
| pod start wait, mean (s) | 0.4 | 0.2 | −50.0% | −1.0121 to +0.6121 | no |
| host CPU busy, the real machine under kind (%) | 43.75 | 45.35 | +3.7% | +0.8604 to +2.3358 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1401 | 1440 | +2.8% | −8.6307 to +87.4307 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.194 | −13.4% | −3.2194 to +1.6074 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 114.7 | 161.4 | +40.6% | −4.8308 to +98.0558 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 579.5 | 677.9 | +17.0% | −124.6271 to +321.4271 | no |
| queue: job turnaround, submitted to done, mean (s) | 750 | 787.1 | +4.9% | −9.5704 to +83.7870 | no |
| queue: jobs unfinished at the window's end | 9.2 | 10 | +8.7% | −1.9144 to +3.5144 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*