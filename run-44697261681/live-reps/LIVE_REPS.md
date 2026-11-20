# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.411 |
| node-hours | 2.518 | 1.847 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 221.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 250.9 | 239.1 |
| response time (ms), 95th percentile | 907.3 | 976.9 |
| response time (ms), 99th percentile | 1455 | 1511 |
| time over the response line (% of samples) | 7.856 | 8.288 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 4.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.65 | 17.51 |
| utilisation (used / allocatable) | 0.05892 | 0.08013 |
| CPU used (cores), mean | 1.414 | 1.381 |
| Omni's own CPU (cores), mean | 0 | 0.07222 |
| CPU used with Omni's own (cores), mean | 1.414 | 1.453 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.5 | 384.9 |
| HPA replicas, mean | 2.021 | 2.01 |
| pods started | 0.2 | 0.4 |
| pod start wait, total (s) | 0.4 | 0.9 |
| pod start wait, mean (s) | 0.4 | 0.6 |
| host CPU busy, the real machine under kind (%) | 40.89 | 43.83 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 782.7 | 787.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.549 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.75 | 0.8625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2.3 |
| queue: job turnaround, submitted to done, mean (s) | 92.45 | 96.05 |
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
| worker nodes in service, mean | 6 | 4.411 | −26.5% | −2.4765 to −0.7020 | yes: GAIN |
| node-hours | 2.518 | 1.847 | −26.6% | −1.0405 to −0.3015 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.3 | 271.5 | −0.3% | −1.7473 to +0.0503 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.3 | 221.5 | −18.7% | −78.8264 to −22.8206 | yes: GAIN |
| response time (ms), mean | 250.9 | 239.1 | −4.7% | −35.9461 to +12.3192 | no |
| response time (ms), 95th percentile | 907.3 | 976.9 | +7.7% | −81.2476 to +220.4386 | no |
| response time (ms), 99th percentile | 1455 | 1511 | +3.9% | −61.8468 to +174.0258 | no |
| time over the response line (% of samples) | 7.856 | 8.288 | +5.5% | −0.4377 to +1.3022 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.7 | 4.9 | +4.3% | −0.5388 to +0.9388 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 121.7 | +121.700 (native is 0) | +54.5127 to +188.8873 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.65 | 17.51 | +11.9% | −0.8362 to +4.5562 | no |
| utilisation (used / allocatable) | 0.05892 | 0.08013 | +36.0% | +0.0090 to +0.0334 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.381 | −2.4% | −0.0870 to +0.0198 | no |
| Omni's own CPU (cores), mean | 0 | 0.07222 | +0.072 (native is 0) | +0.0647 to +0.0798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.453 | +2.7% | −0.0178 to +0.0951 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.5 | 384.9 | −18.2% | −134.8451 to −36.3766 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.021 | 2.01 | −0.5% | −0.1234 to +0.1023 | no |
| pods started | 0.2 | 0.4 | +100.0% | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0.4 | 0.9 | +125.0% | −0.9405 to +1.9405 | no |
| pod start wait, mean (s) | 0.4 | 0.6 | +50.0% | −0.8003 to +1.2003 | no |
| host CPU busy, the real machine under kind (%) | 40.89 | 43.83 | +7.2% | +2.4419 to +3.4354 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 782.7 | 787.8 | +0.7% | −0.9268 to +11.1268 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.549 | −40.8% | −3.6332 to −1.2685 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.75 | 0.8625 | +15.0% | −0.0906 to +0.3156 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.3 | 2.3 | +76.9% | −0.7843 to +2.7843 | no |
| queue: job turnaround, submitted to done, mean (s) | 92.45 | 96.05 | +3.9% | −2.1147 to +9.3064 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*