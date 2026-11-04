# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.482 |
| node-hours | 2.514 | 2.296 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 275.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 259.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 498.7 | 486.5 |
| response time (ms), 95th percentile | 2299 | 2500 |
| response time (ms), 99th percentile | 3344 | 3551 |
| time over the response line (% of samples) | 19.44 | 19.14 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.9 | 16.17 |
| utilisation (used / allocatable) | 0.06776 | 0.07707 |
| CPU used (cores), mean | 1.626 | 1.661 |
| Omni's own CPU (cores), mean | 0 | 0.07661 |
| CPU used with Omni's own (cores), mean | 1.626 | 1.737 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.9 | 372.5 |
| HPA replicas, mean | 2.071 | 2.332 |
| pods started | 0.3 | 1.4 |
| pod start wait, total (s) | 0.8 | 2.6 |
| pod start wait, mean (s) | 0.6 | 1.133 |
| host CPU busy, the real machine under kind (%) | 46.72 | 50.3 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 847.4 | 867.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.129 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.1375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 155.7 | 174.3 |
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
| worker nodes in service, mean | 6 | 5.482 | −8.6% | −1.2403 to +0.2043 | no |
| node-hours | 2.514 | 2.296 | −8.7% | −0.5199 to +0.0845 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 275.8 | +0.2% | −0.6182 to +1.4707 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 259.5 | −5.7% | −38.4054 to +6.7537 | no |
| response time (ms), mean | 498.7 | 486.5 | −2.4% | −37.4529 to +13.1338 | no |
| response time (ms), 95th percentile | 2299 | 2500 | +8.7% | +74.2378 to +327.9222 | yes: LOSS |
| response time (ms), 99th percentile | 3344 | 3551 | +6.2% | +55.6272 to +356.8812 | yes: LOSS |
| time over the response line (% of samples) | 19.44 | 19.14 | −1.5% | −2.0312 to +1.4316 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12 | 12.2 | +1.7% | −0.3642 to +0.7642 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 57.6 | +57.600 (native is 0) | +23.5059 to +91.6941 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.9 | 16.16 | +16.3% | −1.3366 to +5.8633 | no |
| utilisation (used / allocatable) | 0.06776 | 0.07707 | +13.7% | −0.0021 to +0.0207 | no |
| CPU used (cores), mean | 1.626 | 1.661 | +2.1% | +0.0195 to +0.0497 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07661 | +0.077 (native is 0) | +0.0706 to +0.0826 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.626 | 1.737 | +6.8% | +0.0938 to +0.1286 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 409.9 | 372.5 | −9.1% | −80.9363 to +6.1415 | no |
| HPA replicas, mean | 2.071 | 2.332 | +12.6% | +0.0100 to +0.5125 | yes: power given |
| pods started | 0.3 | 1.4 | +366.7% | −0.1818 to +2.3818 | no |
| pod start wait, total (s) | 0.8 | 2.6 | +225.0% | −0.6502 to +4.2502 | no |
| pod start wait, mean (s) | 0.6 | 1.133 | +88.9% | −0.6030 to +1.6696 | no |
| host CPU busy, the real machine under kind (%) | 46.72 | 50.3 | +7.7% | +3.0860 to +4.0745 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 847.4 | 867.6 | +2.4% | +11.0906 to +29.3094 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.129 | −14.5% | −1.9824 to +0.2401 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1 | 0.1375 | +37.5% | −0.0387 to +0.1137 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.6 | 0.9 | +50.0% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 155.7 | 174.3 | +12.0% | +8.8308 to +28.4525 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*