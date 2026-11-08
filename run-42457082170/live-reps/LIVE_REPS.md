# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.94 |
| node-hours | 2.511 | 2.486 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 270.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 268.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 123.8 | 98.22 |
| response time (ms), 95th percentile | 208 | 214.9 |
| response time (ms), 99th percentile | 302.4 | 323.1 |
| time over the response line (% of samples) | 0.1463 | 0.1811 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 972.4 | 1098 |
| utilisation (used / allocatable) | 0.0584 | 0.05736 |
| CPU used (cores), mean | 1.402 | 1.365 |
| Omni's own CPU (cores), mean | 0 | 0.06647 |
| CPU used with Omni's own (cores), mean | 1.402 | 1.431 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.4 | 472.7 |
| HPA replicas, mean | 2.025 | 2.123 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.1667 |
| host CPU busy, the real machine under kind (%) | 43.44 | 45.07 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1375 | 1417 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.37 |
| queue: job wait, submitted to its first pod running, mean (s) | 138.8 | 154.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 583.3 | 758.4 |
| queue: job turnaround, submitted to done, mean (s) | 745.6 | 783.6 |
| queue: jobs unfinished at the window's end | 8.6 | 9.7 |
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
| worker nodes in service, mean | 6 | 5.94 | −1.0% | −0.1680 to +0.0490 | no |
| node-hours | 2.511 | 2.486 | −1.0% | −0.0705 to +0.0208 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 270.7 | −0.2% | −1.7929 to +0.8451 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 268.8 | −0.9% | −5.9145 to +1.2376 | no |
| response time (ms), mean | 123.8 | 98.22 | −20.7% | −30.9092 to −20.3148 | yes: GAIN |
| response time (ms), 95th percentile | 208 | 214.9 | +3.3% | −5.1757 to +18.9097 | no |
| response time (ms), 99th percentile | 302.4 | 323.1 | +6.9% | +1.2375 to +40.2033 | yes: LOSS |
| time over the response line (% of samples) | 0.1463 | 0.1811 | +23.8% | −0.0487 to +0.1183 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107 | +107.000 (native is 0) | +91.7401 to +122.2599 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 972.4 | 1098 | +12.9% | +64.6064 to +186.7803 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0584 | 0.05736 | −1.8% | −0.0028 to +0.0008 | no |
| CPU used (cores), mean | 1.402 | 1.365 | −2.6% | −0.0801 to +0.0063 | no |
| Omni's own CPU (cores), mean | 0 | 0.06647 | +0.066 (native is 0) | +0.0577 to +0.0752 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.402 | 1.431 | +2.1% | −0.0093 to +0.0685 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464.4 | 472.7 | +1.8% | −4.3710 to +21.1263 | no |
| HPA replicas, mean | 2.025 | 2.123 | +4.9% | −0.0990 to +0.2956 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.3786 to +0.9786 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.1667 | +0.167 (native is 0) | −0.2103 to +0.5437 | no |
| host CPU busy, the real machine under kind (%) | 43.44 | 45.07 | +3.8% | +0.9839 to +2.2821 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1375 | 1417 | +3.0% | −27.5639 to +110.9639 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.37 | −10.5% | −2.0066 to +0.7461 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 138.8 | 154.5 | +11.3% | −13.5975 to +45.0975 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 583.3 | 758.4 | +30.0% | +65.1543 to +285.0457 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 745.6 | 783.6 | +5.1% | −10.2100 to +86.2350 | no |
| queue: jobs unfinished at the window's end | 8.6 | 9.7 | +12.8% | −0.5329 to +2.7329 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*