# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.355 |
| node-hours | 2.514 | 1.822 |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 218.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 179.5 | 156.3 |
| response time (ms), 95th percentile | 473.4 | 536.4 |
| response time (ms), 99th percentile | 729.5 | 808.8 |
| time over the response line (% of samples) | 2.679 | 2.948 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 2.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90.48 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.93 | 13.11 |
| utilisation (used / allocatable) | 0.05533 | 0.07723 |
| CPU used (cores), mean | 1.328 | 1.319 |
| Omni's own CPU (cores), mean | 0 | 0.07281 |
| CPU used with Omni's own (cores), mean | 1.328 | 1.391 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.8 | 397.3 |
| HPA replicas, mean | 2.015 | 2.119 |
| pods started | 0 | 0.5 |
| pod start wait, total (s) | 0 | 1 |
| pod start wait, mean (s) | 0 | 0.7333 |
| host CPU busy, the real machine under kind (%) | 39.01 | 42.16 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 745.7 | 750.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.153 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6833 | 0.7167 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 51.27 | 57.43 |
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
| worker nodes in service, mean | 6 | 4.355 | −27.4% | −2.3257 to −0.9640 | yes: GAIN |
| node-hours | 2.514 | 1.822 | −27.5% | −0.9761 to −0.4070 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 270.5 | 270.3 | −0.1% | −1.4824 to +0.9744 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 270.5 | 218.7 | −19.2% | −73.2766 to −30.4147 | yes: GAIN |
| response time (ms), mean | 179.5 | 156.3 | −12.9% | −31.8071 to −14.6682 | yes: GAIN |
| response time (ms), 95th percentile | 473.4 | 536.4 | +13.3% | −38.8599 to +164.7289 | no |
| response time (ms), 99th percentile | 729.5 | 808.8 | +10.9% | −36.0484 to +194.6136 | no |
| time over the response line (% of samples) | 2.679 | 2.948 | +10.1% | −0.4271 to +0.9660 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 2 | 2.5 | +25.0% | −0.6310 to +1.6310 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150.6 | +150.600 (native is 0) | +97.8176 to +203.3824 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.93 | 13.11 | +9.9% | −1.9340 to +4.2873 | no |
| utilisation (used / allocatable) | 0.05533 | 0.07723 | +39.6% | +0.0125 to +0.0313 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.328 | 1.319 | −0.7% | −0.0383 to +0.0193 | no |
| Omni's own CPU (cores), mean | 0 | 0.07281 | +0.073 (native is 0) | +0.0685 to +0.0771 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.328 | 1.391 | +4.8% | +0.0330 to +0.0937 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 492.8 | 397.3 | −19.4% | −138.4344 to −52.6083 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.015 | 2.119 | +5.2% | −0.0925 to +0.3005 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −0.1952 to +1.1952 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −0.1681 to +2.1681 | no |
| pod start wait, mean (s) | 0 | 0.7333 | +0.733 (native is 0) | −0.1715 to +1.6381 | no |
| host CPU busy, the real machine under kind (%) | 39.01 | 42.16 | +8.1% | +2.4610 to +3.8449 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 745.7 | 750.3 | +0.6% | +1.0602 to +8.1398 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.153 | −47.5% | −3.8423 to −1.8517 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.6833 | 0.7167 | +4.9% | −0.0542 to +0.1209 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.1 | 1.4 | +27.3% | −0.0455 to +0.6455 | no |
| queue: job turnaround, submitted to done, mean (s) | 51.27 | 57.43 | +12.0% | +1.5716 to +10.7534 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*