# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.652 |
| node-hours | 2.515 | 1.951 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 229.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 221.5 | 195.5 |
| response time (ms), 95th percentile | 830.9 | 824 |
| response time (ms), 99th percentile | 1184 | 1180 |
| time over the response line (% of samples) | 5.862 | 6.231 |
| failed requests (%) | 0.01053 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 4.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.332 | 9.815 |
| utilisation (used / allocatable) | 0.05685 | 0.07339 |
| CPU used (cores), mean | 1.364 | 1.336 |
| Omni's own CPU (cores), mean | 0 | 0.01562 |
| CPU used with Omni's own (cores), mean | 1.364 | 1.352 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.2 | 409.8 |
| HPA replicas, mean | 2.005 | 2.135 |
| pods started | 0.2 | 0.2 |
| pod start wait, total (s) | 0.3 | 0.4 |
| pod start wait, mean (s) | 0.3 | 0.4 |
| host CPU busy, the real machine under kind (%) | 39.01 | 39.68 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 755.4 | 758.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.769 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.05417 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 63.21 | 66.13 |
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
| worker nodes in service, mean | 6 | 4.652 | −22.5% | −2.1338 to −0.5615 | yes: GAIN |
| node-hours | 2.515 | 1.951 | −22.4% | −0.8915 to −0.2360 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.5 | +0.0% | −0.6110 to +0.7278 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 229.2 | −15.6% | −67.1142 to −17.4565 | yes: GAIN |
| response time (ms), mean | 221.5 | 195.5 | −11.7% | −37.6356 to −14.3476 | yes: GAIN |
| response time (ms), 95th percentile | 830.9 | 824 | −0.8% | −43.4307 to +29.5947 | no |
| response time (ms), 99th percentile | 1184 | 1180 | −0.3% | −110.0960 to +102.9326 | no |
| time over the response line (% of samples) | 5.862 | 6.231 | +6.3% | −0.2045 to +0.9417 | no |
| failed requests (%) | 0.01053 | 0 | −100.0% | −0.0343 to +0.0133 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.3 | 4.8 | +11.6% | −0.4685 to +1.4685 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 42.3 | +42.300 (native is 0) | +30.2877 to +54.3123 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.332 | 9.815 | +5.2% | −0.8776 to +1.8442 | no |
| utilisation (used / allocatable) | 0.05685 | 0.07339 | +29.1% | +0.0062 to +0.0268 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.364 | 1.336 | −2.1% | −0.0648 to +0.0086 | no |
| Omni's own CPU (cores), mean | 0 | 0.01562 | +0.016 (native is 0) | +0.0140 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.364 | 1.352 | −0.9% | −0.0495 to +0.0246 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.2 | 409.8 | −15.0% | −115.0725 to −29.7391 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.005 | 2.135 | +6.5% | −0.0498 to +0.3092 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.3 | 0.4 | +33.3% | −0.6113 to +0.8113 | no |
| pod start wait, mean (s) | 0.3 | 0.4 | +33.3% | −0.6113 to +0.8113 | no |
| host CPU busy, the real machine under kind (%) | 39.01 | 39.68 | +1.7% | +0.3335 to +1.0093 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 755.4 | 758.2 | +0.4% | −2.3999 to +7.9999 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.769 | −37.2% | −3.4817 to −0.9795 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.02917 | 0.05417 | +85.7% | −0.0100 to +0.0600 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.1 | 0.4 | +300.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 63.21 | 66.13 | +4.6% | −1.3665 to +7.2081 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*