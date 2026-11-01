# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.497 |
| node-hours | 2.517 | 1.884 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 270.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 223.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 325.4 | 300.6 |
| response time (ms), 95th percentile | 1309 | 1294 |
| response time (ms), 99th percentile | 1738 | 1703 |
| time over the response line (% of samples) | 8.98 | 9.059 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 5.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.8 | 27.52 |
| utilisation (used / allocatable) | 0.05721 | 0.07462 |
| CPU used (cores), mean | 1.373 | 1.33 |
| Omni's own CPU (cores), mean | 0 | 0.01739 |
| CPU used with Omni's own (cores), mean | 1.373 | 1.347 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.4 | 408.7 |
| HPA replicas, mean | 2.059 | 2.112 |
| pods started | 0.2 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.4 |
| pod start wait, mean (s) | 0.4 | 0.4 |
| host CPU busy, the real machine under kind (%) | 41.62 | 42.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 806.7 | 810.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.544 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9542 | 1.15 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 3.4 |
| queue: job turnaround, submitted to done, mean (s) | 107.2 | 109.6 |
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
| worker nodes in service, mean | 6 | 4.497 | −25.0% | −2.3538 to −0.6519 | yes: GAIN |
| node-hours | 2.517 | 1.883 | −25.2% | −0.9907 to −0.2763 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.7 | 270.9 | −0.3% | −1.5968 to −0.1123 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.7 | 223.7 | −17.7% | −75.1504 to −20.9587 | yes: GAIN |
| response time (ms), mean | 325.4 | 300.6 | −7.6% | −43.0559 to −6.6484 | yes: GAIN |
| response time (ms), 95th percentile | 1309 | 1294 | −1.1% | −44.9903 to +15.8423 | no |
| response time (ms), 99th percentile | 1738 | 1703 | −2.0% | −107.5886 to +38.4996 | no |
| time over the response line (% of samples) | 8.98 | 9.059 | +0.9% | −0.7752 to +0.9342 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5 | 5.2 | +4.0% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.9 | +38.900 (native is 0) | +25.0033 to +52.7967 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.8 | 27.52 | +11.0% | −2.1177 to +7.5577 | no |
| utilisation (used / allocatable) | 0.05721 | 0.07462 | +30.4% | +0.0070 to +0.0278 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.373 | 1.33 | −3.2% | −0.0913 to +0.0043 | no |
| Omni's own CPU (cores), mean | 0 | 0.01739 | +0.017 (native is 0) | +0.0152 to +0.0196 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.373 | 1.347 | −1.9% | −0.0751 to +0.0229 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 490.4 | 408.7 | −16.7% | −132.1020 to −31.2288 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.059 | 2.112 | +2.5% | −0.1149 to +0.2195 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.4278 to +0.6278 | no |
| pod start wait, total (s) | 0.4 | 0.4 | ±0.0% | −0.8921 to +0.8921 | no |
| pod start wait, mean (s) | 0.4 | 0.4 | ±0.0% | −0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 41.62 | 42.48 | +2.1% | +0.3903 to +1.3273 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 806.7 | 810.1 | +0.4% | −0.9077 to +7.7077 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.544 | −40.9% | −3.8009 to −1.1117 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9542 | 1.15 | +20.5% | −0.0759 to +0.4676 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.4 | 3.4 | +41.7% | −0.2617 to +2.2617 | no |
| queue: job turnaround, submitted to done, mean (s) | 107.2 | 109.6 | +2.2% | −1.6595 to +6.3261 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*