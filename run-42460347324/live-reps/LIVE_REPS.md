# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.521 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 134 | 112.1 |
| response time (ms), 95th percentile | 235.4 | 245.5 |
| response time (ms), 99th percentile | 354.2 | 358.5 |
| time over the response line (% of samples) | 0.2635 | 0.2924 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1111 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1109 | 1217 |
| utilisation (used / allocatable) | 0.05975 | 0.0588 |
| CPU used (cores), mean | 1.434 | 1.411 |
| Omni's own CPU (cores), mean | 0 | 0.06997 |
| CPU used with Omni's own (cores), mean | 1.434 | 1.481 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.9 | 459.4 |
| HPA replicas, mean | 1.969 | 2.166 |
| pods started | 0.1111 | 1 |
| pod start wait, total (s) | 0.2222 | 2.333 |
| pod start wait, mean (s) | 0.2222 | 1.611 |
| host CPU busy, the real machine under kind (%) | 45.07 | 46.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1472 | 1487 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 142.2 | 178.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 661.8 | 803.1 |
| queue: job turnaround, submitted to done, mean (s) | 822.6 | 875.2 |
| queue: jobs unfinished at the window's end | 8.333 | 12.22 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 8 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.521 | 2.515 | −0.3% | −0.0156 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 271.6 | −0.4% | −2.2474 to −0.0014 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 271.6 | −0.4% | −2.2474 to −0.0014 | yes: GAIN |
| response time (ms), mean | 133.6 | 109.5 | −18.1% | −30.7558 to −17.5298 | yes: GAIN |
| response time (ms), 95th percentile | 237.4 | 247.4 | +4.2% | −13.7949 to +33.9187 | no |
| response time (ms), 99th percentile | 359.4 | 364.6 | +1.5% | −29.0449 to +39.4676 | no |
| time over the response line (% of samples) | 0.2775 | 0.3196 | +15.2% | −0.1195 to +0.2037 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.125 | +0.125 (native is 0) | −0.1706 to +0.4206 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.9 | +101.875 (native is 0) | +73.9368 to +129.8132 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1108 | 1234 | +11.3% | +74.7465 to +176.1410 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0598 | 0.05876 | −1.7% | −0.0027 to +0.0006 | no |
| CPU used (cores), mean | 1.435 | 1.41 | −1.7% | −0.0639 to +0.0138 | no |
| Omni's own CPU (cores), mean | 0 | 0.07078 | +0.071 (native is 0) | +0.0627 to +0.0788 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.435 | 1.481 | +3.2% | +0.0094 to +0.0821 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 452.6 | 459.7 | +1.6% | −4.3749 to +18.5959 | no |
| HPA replicas, mean | 1.947 | 2.197 | +12.8% | +0.0111 to +0.4888 | yes: power given |
| pods started | 0.125 | 1.125 | +800.0% | +0.0006 to +1.9994 | yes: power given |
| pod start wait, total (s) | 0.25 | 2.625 | +950.0% | +0.1431 to +4.6069 | yes: LOSS |
| pod start wait, mean (s) | 0.25 | 1.812 | +625.0% | −0.0088 to +3.1338 | no |
| host CPU busy, the real machine under kind (%) | 45.15 | 46.46 | +2.9% | +0.4269 to +2.1939 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1467 | 1483 | +1.1% | −7.1333 to +39.1333 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 144.6 | 189.1 | +30.8% | +0.7779 to +88.1909 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 678.1 | 843.8 | +24.4% | +67.4369 to +263.8131 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 807.2 | 882.8 | +9.4% | +16.2684 to +134.9816 | yes: LOSS |
| queue: jobs unfinished at the window's end | 7.875 | 12.88 | +63.5% | +1.2874 to +8.7126 | yes: LOSS |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*