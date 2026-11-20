# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.639 |
| node-hours | 2.512 | 1.947 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 229.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 313 | 294.3 |
| response time (ms), 95th percentile | 1072 | 1199 |
| response time (ms), 99th percentile | 1560 | 1689 |
| time over the response line (% of samples) | 11.14 | 11.07 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 153.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 22 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.27 | 10.44 |
| utilisation (used / allocatable) | 0.05893 | 0.07612 |
| CPU used (cores), mean | 1.414 | 1.395 |
| Omni's own CPU (cores), mean | 0 | 0.07758 |
| CPU used with Omni's own (cores), mean | 1.414 | 1.472 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 393.8 |
| HPA replicas, mean | 1.969 | 2.167 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 1.7 |
| pod start wait, mean (s) | 0 | 0.8667 |
| host CPU busy, the real machine under kind (%) | 41.28 | 44.37 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 777.6 | 782.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.674 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.7 |
| queue: job turnaround, submitted to done, mean (s) | 81.28 | 86.94 |
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
| worker nodes in service, mean | 6 | 4.639 | −22.7% | −2.1164 to −0.6063 | yes: GAIN |
| node-hours | 2.512 | 1.947 | −22.5% | −0.8831 to −0.2463 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 272.4 | +0.3% | +0.2658 to +1.1820 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 229.5 | −15.5% | −66.1323 to −18.1282 | yes: GAIN |
| response time (ms), mean | 313 | 294.3 | −6.0% | −26.0515 to −11.4459 | yes: GAIN |
| response time (ms), 95th percentile | 1072 | 1199 | +11.9% | +25.8349 to +228.3211 | yes: LOSS |
| response time (ms), 99th percentile | 1560 | 1689 | +8.2% | +25.7150 to +231.3868 | yes: LOSS |
| time over the response line (% of samples) | 11.14 | 11.07 | −0.7% | −0.9840 to +0.8264 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 8 | +29.0% | +0.0872 to +3.5128 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 153.5 | +153.500 (native is 0) | +71.6167 to +235.3833 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.27 | 10.44 | +12.6% | −1.5339 to +3.8773 | no |
| utilisation (used / allocatable) | 0.05893 | 0.07612 | +29.2% | +0.0070 to +0.0274 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.395 | −1.4% | −0.0427 to +0.0031 | no |
| Omni's own CPU (cores), mean | 0 | 0.07758 | +0.078 (native is 0) | +0.0710 to +0.0841 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.472 | +4.1% | +0.0335 to +0.0821 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 469 | 393.8 | −16.0% | −117.0543 to −33.2883 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.969 | 2.167 | +10.1% | +0.0334 to +0.3641 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.0121 to +1.6121 | no |
| pod start wait, total (s) | 0 | 1.7 | +1.700 (native is 0) | −0.2090 to +3.6090 | no |
| pod start wait, mean (s) | 0 | 0.8667 | +0.867 (native is 0) | −0.0126 to +1.7460 | no |
| host CPU busy, the real machine under kind (%) | 41.28 | 44.37 | +7.5% | +2.6753 to +3.5046 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 777.6 | 782.3 | +0.6% | −1.6806 to +11.0806 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.674 | −38.8% | −3.5492 to −1.1022 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1042 | 0.2708 | +160.0% | −0.0726 to +0.4059 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.7 | +16.7% | −0.1262 to +0.3262 | no |
| queue: job turnaround, submitted to done, mean (s) | 81.28 | 86.94 | +7.0% | −0.5524 to +11.8690 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*