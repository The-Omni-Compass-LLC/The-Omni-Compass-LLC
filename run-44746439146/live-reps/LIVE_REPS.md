# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.948 |
| node-hours | 2.516 | 2.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 270.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 268.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 122.7 | 125 |
| response time (ms), 95th percentile | 208.5 | 219 |
| response time (ms), 99th percentile | 305.1 | 317.2 |
| time over the response line (% of samples) | 0.08432 | 0.1291 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 916.6 | 1035 |
| utilisation (used / allocatable) | 0.05891 | 0.05693 |
| CPU used (cores), mean | 1.414 | 1.356 |
| Omni's own CPU (cores), mean | 0 | 0.06272 |
| CPU used with Omni's own (cores), mean | 1.414 | 1.419 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.5 | 475.3 |
| HPA replicas, mean | 1.957 | 2.046 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 1 |
| pod start wait, mean (s) | 0 | 0.25 |
| host CPU busy, the real machine under kind (%) | 44.03 | 45.13 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1449 | 1463 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.154 |
| queue: job wait, submitted to its first pod running, mean (s) | 129.3 | 152.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 553.1 | 634 |
| queue: job turnaround, submitted to done, mean (s) | 732.8 | 789 |
| queue: jobs unfinished at the window's end | 4.9 | 8.9 |
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
| worker nodes in service, mean | 6 | 5.948 | −0.9% | −0.1700 to +0.0658 | no |
| node-hours | 2.516 | 2.489 | −1.1% | −0.0756 to +0.0204 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 270.3 | −0.6% | −3.1804 to +0.0679 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 268.7 | −1.2% | −7.0519 to +0.6770 | no |
| response time (ms), mean | 122.7 | 125 | +1.8% | −1.8017 to +6.2695 | no |
| response time (ms), 95th percentile | 208.5 | 219 | +5.1% | +2.6946 to +18.4394 | yes: LOSS |
| response time (ms), 99th percentile | 305.1 | 317.2 | +4.0% | −5.6203 to +29.9461 | no |
| time over the response line (% of samples) | 0.08432 | 0.1291 | +53.2% | −0.0182 to +0.1078 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 40.7 | +40.700 (native is 0) | +5.1994 to +76.2006 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 916.6 | 1035 | +12.9% | +56.0187 to +180.1813 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05891 | 0.05693 | −3.4% | −0.0035 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.414 | 1.356 | −4.1% | −0.0890 to −0.0266 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06272 | +0.063 (native is 0) | +0.0581 to +0.0674 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.414 | 1.419 | +0.3% | −0.0271 to +0.0368 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 460.5 | 475.3 | +3.2% | +4.7142 to +24.8389 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.046 | +4.5% | −0.1230 to +0.3008 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.5048 to +1.3048 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −1.2620 to +3.2620 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 44.03 | 45.13 | +2.5% | +0.2166 to +1.9762 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1449 | 1463 | +0.9% | −23.1042 to +50.5042 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.154 | −30.8% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 129.3 | 152.6 | +18.1% | −2.7175 to +49.4091 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 553.1 | 634 | +14.6% | −30.9426 to +192.7426 | no |
| queue: job turnaround, submitted to done, mean (s) | 732.8 | 789 | +7.7% | −7.2541 to +119.7958 | no |
| queue: jobs unfinished at the window's end | 4.9 | 8.9 | +81.6% | +0.8010 to +7.1990 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*