# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.119 |
| node-hours | 2.522 | 2.142 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 244.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 319.9 | 309.6 |
| response time (ms), 95th percentile | 1080 | 1187 |
| response time (ms), 99th percentile | 1495 | 1641 |
| time over the response line (% of samples) | 11.77 | 12.4 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 16.38 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.388 | 10.78 |
| utilisation (used / allocatable) | 0.06007 | 0.07149 |
| CPU used (cores), mean | 1.442 | 1.456 |
| Omni's own CPU (cores), mean | 0 | 0.07706 |
| CPU used with Omni's own (cores), mean | 1.442 | 1.533 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.9 | 405.3 |
| HPA replicas, mean | 1.979 | 2.384 |
| pods started | 0 | 1.5 |
| pod start wait, total (s) | 0 | 3.5 |
| pod start wait, mean (s) | 0 | 2.15 |
| host CPU busy, the real machine under kind (%) | 41.97 | 45.44 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 774.7 | 783.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.388 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.2958 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 79.76 | 86.92 |
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
| worker nodes in service, mean | 6 | 5.119 | −14.7% | −1.3675 to −0.3954 | yes: GAIN |
| node-hours | 2.522 | 2.142 | −15.0% | −0.5885 to −0.1699 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 272.4 | −0.3% | −1.7859 to +0.1481 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 244.8 | −10.4% | −44.3800 to −12.4661 | yes: GAIN |
| response time (ms), mean | 319.9 | 309.6 | −3.2% | −28.4289 to +7.8435 | no |
| response time (ms), 95th percentile | 1080 | 1187 | +9.9% | −0.0492 to +214.0122 | no |
| response time (ms), 99th percentile | 1495 | 1641 | +9.8% | +2.2556 to +289.6012 | yes: LOSS |
| time over the response line (% of samples) | 11.77 | 12.4 | +5.4% | +0.0232 to +1.2431 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 9.8 | +18.1% | +0.4204 to +2.5796 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103.9 | +103.900 (native is 0) | +58.5364 to +149.2636 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.388 | 10.78 | +14.8% | −1.3255 to +4.1022 | no |
| utilisation (used / allocatable) | 0.06007 | 0.07149 | +19.0% | +0.0056 to +0.0172 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.442 | 1.456 | +1.0% | −0.0021 to +0.0303 | no |
| Omni's own CPU (cores), mean | 0 | 0.07706 | +0.077 (native is 0) | +0.0718 to +0.0823 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.442 | 1.533 | +6.3% | +0.0716 to +0.1107 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 456.9 | 405.3 | −11.3% | −77.5242 to −25.7495 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.979 | 2.384 | +20.5% | +0.2350 to +0.5761 | yes: power given |
| pods started | 0 | 1.5 | +1.500 (native is 0) | +0.6570 to +2.3430 | yes: power given |
| pod start wait, total (s) | 0 | 3.5 | +3.500 (native is 0) | +1.4980 to +5.5020 | yes: LOSS |
| pod start wait, mean (s) | 0 | 2.15 | +2.150 (native is 0) | +1.4337 to +2.8663 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.97 | 45.44 | +8.3% | +2.9765 to +3.9643 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.7 | 783.4 | +1.1% | +0.3578 to +17.0422 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.388 | −26.9% | −2.4352 to −0.7893 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1542 | 0.2958 | +91.9% | −0.1846 to +0.4679 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.6 | +77.8% | −1.1790 to +2.5790 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.76 | 86.92 | +9.0% | +0.2017 to +14.1150 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*