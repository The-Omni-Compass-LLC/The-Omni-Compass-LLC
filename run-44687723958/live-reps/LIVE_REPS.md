# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.697 |
| node-hours | 2.517 | 1.97 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 231.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 265.5 | 243.6 |
| response time (ms), 95th percentile | 920.5 | 1030 |
| response time (ms), 99th percentile | 1496 | 1613 |
| time over the response line (% of samples) | 7.63 | 7.375 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 4.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 86.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 16.74 |
| utilisation (used / allocatable) | 0.06055 | 0.0768 |
| CPU used (cores), mean | 1.453 | 1.432 |
| Omni's own CPU (cores), mean | 0 | 0.07503 |
| CPU used with Omni's own (cores), mean | 1.453 | 1.507 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.8 | 387.8 |
| HPA replicas, mean | 2.103 | 2.077 |
| pods started | 0.8 | 0.5 |
| pod start wait, total (s) | 1.7 | 0.8 |
| pod start wait, mean (s) | 0.8667 | 0.275 |
| host CPU busy, the real machine under kind (%) | 42.32 | 45.38 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 783.4 | 790.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.661 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8167 | 0.7292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.5 |
| queue: job turnaround, submitted to done, mean (s) | 91.63 | 98.31 |
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
| worker nodes in service, mean | 6 | 4.697 | −21.7% | −1.9538 to −0.6513 | yes: GAIN |
| node-hours | 2.517 | 1.97 | −21.7% | −0.8234 to −0.2698 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.6 | −0.0% | −0.9344 to +0.7089 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 231.7 | −15.1% | −62.0901 to −20.0771 | yes: GAIN |
| response time (ms), mean | 265.5 | 243.6 | −8.2% | −35.3847 to −8.3836 | yes: GAIN |
| response time (ms), 95th percentile | 920.5 | 1030 | +11.9% | −43.6920 to +262.0290 | no |
| response time (ms), 99th percentile | 1496 | 1613 | +7.9% | −78.5596 to +313.6856 | no |
| time over the response line (% of samples) | 7.63 | 7.375 | −3.3% | −0.5723 to +0.0613 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.1 | 4.7 | −7.8% | −1.0032 to +0.2032 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 86.8 | +86.800 (native is 0) | +42.9164 to +130.6836 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 15.24 | 16.74 | +9.8% | −0.0370 to +3.0370 | no |
| utilisation (used / allocatable) | 0.06055 | 0.0768 | +26.8% | +0.0073 to +0.0252 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.453 | 1.432 | −1.5% | −0.0526 to +0.0093 | no |
| Omni's own CPU (cores), mean | 0 | 0.07503 | +0.075 (native is 0) | +0.0689 to +0.0811 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.453 | 1.507 | +3.7% | +0.0210 to +0.0857 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.8 | 387.8 | −14.9% | −103.5426 to −32.2777 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.103 | 2.077 | −1.2% | −0.1923 to +0.1399 | no |
| pods started | 0.8 | 0.5 | −37.5% | −1.3144 to +0.7144 | no |
| pod start wait, total (s) | 1.7 | 0.8 | −52.9% | −2.6011 to +0.8011 | no |
| pod start wait, mean (s) | 0.8667 | 0.275 | −68.3% | −1.3857 to +0.2023 | no |
| host CPU busy, the real machine under kind (%) | 42.32 | 45.38 | +7.2% | +2.3781 to +3.7519 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 783.4 | 790.7 | +0.9% | −0.3526 to +14.9526 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.661 | −39.0% | −3.3678 to −1.3094 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8167 | 0.7292 | −10.7% | −0.2398 to +0.0648 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.5 | ±0.0% | −0.4769 to +0.4769 | no |
| queue: job turnaround, submitted to done, mean (s) | 91.63 | 98.31 | +7.3% | +0.3651 to +12.9932 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*