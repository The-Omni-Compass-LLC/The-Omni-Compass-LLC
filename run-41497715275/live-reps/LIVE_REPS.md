# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.136 |
| node-hours | 2.518 | 2.152 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 247.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 469.7 | 496.3 |
| response time (ms), 95th percentile | 1989 | 2306 |
| response time (ms), 99th percentile | 2679 | 3084 |
| time over the response line (% of samples) | 16.95 | 19.47 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 11.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.45 | 40.07 |
| utilisation (used / allocatable) | 0.06431 | 0.0765 |
| CPU used (cores), mean | 1.543 | 1.557 |
| Omni's own CPU (cores), mean | 0 | 0.08024 |
| CPU used with Omni's own (cores), mean | 1.543 | 1.637 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.6 | 382 |
| HPA replicas, mean | 2.026 | 2.264 |
| pods started | 0.2 | 1.2 |
| pod start wait, total (s) | 0.4 | 2.4 |
| pod start wait, mean (s) | 0.4 | 0.725 |
| host CPU busy, the real machine under kind (%) | 46.2 | 50.55 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 858.3 | 886.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.494 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.213 | 1.267 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 3.6 |
| queue: job turnaround, submitted to done, mean (s) | 158.7 | 182.7 |
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
| worker nodes in service, mean | 6 | 5.136 | −14.4% | −1.6514 to −0.0765 | yes: GAIN |
| node-hours | 2.518 | 2.152 | −14.5% | −0.6992 to −0.0313 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 274.3 | −0.1% | −2.0141 to +1.6223 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 247.2 | −9.9% | −52.8163 to −1.7380 | yes: GAIN |
| response time (ms), mean | 469.7 | 496.3 | +5.7% | −53.8098 to +107.1576 | no |
| response time (ms), 95th percentile | 1989 | 2306 | +15.9% | −167.0294 to +801.3144 | no |
| response time (ms), 99th percentile | 2679 | 3084 | +15.1% | −260.1972 to +1070.0424 | no |
| time over the response line (% of samples) | 16.95 | 19.47 | +14.9% | −1.4560 to +6.5044 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 11.2 | +6.7% | −0.4209 to +1.8209 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 89.9 | +89.900 (native is 0) | +38.1584 to +141.6416 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.45 | 40.07 | +19.8% | −1.2136 to +14.4469 | no |
| utilisation (used / allocatable) | 0.06431 | 0.0765 | +19.0% | +0.0017 to +0.0227 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.543 | 1.557 | +0.8% | −0.0605 to +0.0868 | no |
| Omni's own CPU (cores), mean | 0 | 0.08024 | +0.080 (native is 0) | +0.0718 to +0.0887 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.543 | 1.637 | +6.0% | +0.0169 to +0.1698 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 436.6 | 382 | −12.5% | −101.1921 to −8.0277 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.026 | 2.264 | +11.7% | +0.0003 to +0.4742 | yes: power given |
| pods started | 0.2 | 1.2 | +500.0% | −0.2158 to +2.2158 | no |
| pod start wait, total (s) | 0.4 | 2.4 | +500.0% | −0.5458 to +4.5458 | no |
| pod start wait, mean (s) | 0.4 | 0.725 | +81.3% | −0.5012 to +1.1512 | no |
| host CPU busy, the real machine under kind (%) | 46.2 | 50.55 | +9.4% | +2.2587 to +6.4432 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 858.3 | 886.4 | +3.3% | −7.6279 to +63.8279 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.494 | −25.1% | −2.6815 to −0.3296 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.213 | 1.267 | +4.5% | −0.2880 to +0.3963 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.3 | 3.6 | +9.1% | −0.9639 to +1.5639 | no |
| queue: job turnaround, submitted to done, mean (s) | 158.7 | 182.7 | +15.1% | −9.6254 to +57.6504 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*