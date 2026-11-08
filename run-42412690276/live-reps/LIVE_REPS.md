# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.761 |
| node-hours | 2.512 | 1.99 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 232.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 331.7 | 326.1 |
| response time (ms), 95th percentile | 1153 | 1308 |
| response time (ms), 99th percentile | 1611 | 1856 |
| time over the response line (% of samples) | 13.42 | 14.04 |
| failed requests (%) | 0 | 0.0113 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 9.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 122.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.02 | 13.94 |
| utilisation (used / allocatable) | 0.05994 | 0.07606 |
| CPU used (cores), mean | 1.438 | 1.424 |
| Omni's own CPU (cores), mean | 0 | 0.07519 |
| CPU used with Omni's own (cores), mean | 1.438 | 1.5 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.7 | 394.6 |
| HPA replicas, mean | 1.938 | 2.391 |
| pods started | 0 | 2.1 |
| pod start wait, total (s) | 0 | 4.8 |
| pod start wait, mean (s) | 0 | 1.85 |
| host CPU busy, the real machine under kind (%) | 41.66 | 45.12 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 781.1 | 791.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.842 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1417 | 0.7292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 4.5 |
| queue: job turnaround, submitted to done, mean (s) | 84.98 | 95.59 |
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
| worker nodes in service, mean | 6 | 4.761 | −20.7% | −1.9669 to −0.5112 | yes: GAIN |
| node-hours | 2.512 | 1.99 | −20.8% | −0.8251 to −0.2183 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.8 | −0.1% | −0.7948 to +0.1970 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 232.9 | −14.4% | −62.0325 to −16.2903 | yes: GAIN |
| response time (ms), mean | 331.7 | 326.1 | −1.7% | −22.1750 to +11.0292 | no |
| response time (ms), 95th percentile | 1153 | 1308 | +13.5% | +31.5285 to +279.7585 | yes: LOSS |
| response time (ms), 99th percentile | 1611 | 1856 | +15.2% | +49.0100 to +441.1484 | yes: LOSS |
| time over the response line (% of samples) | 13.42 | 14.04 | +4.7% | −0.0253 to +1.2744 | no |
| failed requests (%) | 0 | 0.0113 | +0.011 (native is 0) | −0.0143 to +0.0369 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 9.6 | +21.5% | +0.2283 to +3.1717 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 122.2 | +122.200 (native is 0) | +55.7874 to +188.6126 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.02 | 13.94 | +39.2% | +0.1714 to +7.6786 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05994 | 0.07606 | +26.9% | +0.0062 to +0.0260 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.438 | 1.424 | −1.0% | −0.0392 to +0.0111 | no |
| Omni's own CPU (cores), mean | 0 | 0.07519 | +0.075 (native is 0) | +0.0689 to +0.0815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.438 | 1.5 | +4.2% | +0.0317 to +0.0906 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.7 | 394.6 | −14.5% | −110.1909 to −24.0831 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.938 | 2.391 | +23.4% | +0.2666 to +0.6400 | yes: power given |
| pods started | 0 | 2.1 | +2.100 (native is 0) | +1.0634 to +3.1366 | yes: power given |
| pod start wait, total (s) | 0 | 4.8 | +4.800 (native is 0) | +1.5869 to +8.0131 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.85 | +1.850 (native is 0) | +1.1935 to +2.5065 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.66 | 45.12 | +8.3% | +3.0093 to +3.9121 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 781.1 | 791.4 | +1.3% | −0.1752 to +20.7752 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.842 | −36.0% | −3.1881 to −1.1279 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1417 | 0.7292 | +414.7% | +0.0007 to +1.1743 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 4.5 | +462.5% | −0.4988 to +7.8988 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.98 | 95.59 | +12.5% | +1.1900 to +20.0350 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*