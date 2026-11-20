# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.142 |
| node-hours | 2.515 | 2.155 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 246.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 382.8 | 383 |
| response time (ms), 95th percentile | 1352 | 1594 |
| response time (ms), 99th percentile | 1920 | 2161 |
| time over the response line (% of samples) | 16.9 | 16.89 |
| failed requests (%) | 0.01143 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 21.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.97 | 13.79 |
| utilisation (used / allocatable) | 0.06232 | 0.07334 |
| CPU used (cores), mean | 1.496 | 1.505 |
| Omni's own CPU (cores), mean | 0 | 0.07852 |
| CPU used with Omni's own (cores), mean | 1.496 | 1.583 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.4 | 394.5 |
| HPA replicas, mean | 1.918 | 2.341 |
| pods started | 0 | 1.9 |
| pod start wait, total (s) | 0 | 4.4 |
| pod start wait, mean (s) | 0 | 1.84 |
| host CPU busy, the real machine under kind (%) | 43.1 | 46.56 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 795.4 | 804.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.511 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.0875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.3 |
| queue: job turnaround, submitted to done, mean (s) | 98.8 | 109.2 |
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
| worker nodes in service, mean | 6 | 5.142 | −14.3% | −1.4123 to −0.3042 | yes: GAIN |
| node-hours | 2.515 | 2.155 | −14.3% | −0.5902 to −0.1298 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.6 | +0.1% | −0.3323 to +1.1187 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 246.6 | −9.7% | −43.8402 to −9.3985 | yes: GAIN |
| response time (ms), mean | 382.8 | 383 | +0.0% | −22.0405 to +22.3534 | no |
| response time (ms), 95th percentile | 1352 | 1594 | +17.8% | +55.7862 to +427.0068 | yes: LOSS |
| response time (ms), 99th percentile | 1920 | 2161 | +12.5% | +61.9957 to +418.3909 | yes: LOSS |
| time over the response line (% of samples) | 16.9 | 16.89 | −0.1% | −0.7680 to +0.7402 | no |
| failed requests (%) | 0.01143 | 0 | −100.0% | −0.0373 to +0.0144 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.6 | 10.1 | +5.2% | −0.7729 to +1.7729 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 93.8 | +93.800 (native is 0) | +22.0393 to +165.5607 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.97 | 13.79 | +25.7% | +0.2512 to +5.3888 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06232 | 0.07334 | +17.7% | +0.0041 to +0.0180 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.496 | 1.505 | +0.6% | −0.0125 to +0.0307 | no |
| Omni's own CPU (cores), mean | 0 | 0.07852 | +0.079 (native is 0) | +0.0736 to +0.0834 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.496 | 1.583 | +5.9% | +0.0649 to +0.1103 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.4 | 394.5 | −11.2% | −79.8811 to −19.9324 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.918 | 2.341 | +22.0% | +0.1720 to +0.6725 | yes: power given |
| pods started | 0 | 1.9 | +1.900 (native is 0) | +0.7590 to +3.0410 | yes: power given |
| pod start wait, total (s) | 0 | 4.4 | +4.400 (native is 0) | +1.6564 to +7.1436 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.84 | +1.840 (native is 0) | +1.1067 to +2.5733 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 43.1 | 46.56 | +8.0% | +2.9900 to +3.9316 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 795.4 | 804.6 | +1.2% | +0.7984 to +17.6016 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.511 | −24.8% | −2.3354 to −0.6430 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1375 | 0.0875 | −36.4% | −0.1141 to +0.0141 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 0.3 | −66.7% | −1.1001 to −0.0999 | yes: GAIN |
| queue: job turnaround, submitted to done, mean (s) | 98.8 | 109.2 | +10.6% | +2.3877 to +18.4956 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*