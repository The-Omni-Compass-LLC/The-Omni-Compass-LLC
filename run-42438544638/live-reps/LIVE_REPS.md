# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.586 |
| node-hours | 2.519 | 1.923 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 226.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 259.5 | 246.1 |
| response time (ms), 95th percentile | 950.7 | 1038 |
| response time (ms), 99th percentile | 1384 | 1519 |
| time over the response line (% of samples) | 7.189 | 7.791 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 6.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 122.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.65 | 19.97 |
| utilisation (used / allocatable) | 0.0554 | 0.07299 |
| CPU used (cores), mean | 1.33 | 1.323 |
| Omni's own CPU (cores), mean | 0 | 0.07382 |
| CPU used with Omni's own (cores), mean | 1.33 | 1.397 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.1 | 413.8 |
| HPA replicas, mean | 2.017 | 2.075 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 1.3 |
| pod start wait, mean (s) | 0 | 1.033 |
| host CPU busy, the real machine under kind (%) | 40.31 | 43.45 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 773.7 | 784.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.704 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8542 | 0.9125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 79.49 | 88.21 |
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
| worker nodes in service, mean | 6 | 4.586 | −23.6% | −2.2214 to −0.6067 | yes: GAIN |
| node-hours | 2.519 | 1.923 | −23.7% | −0.9343 to −0.2579 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 271 | −0.2% | −1.4742 to +0.5508 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 226.6 | −16.5% | −70.6567 to −19.1833 | yes: GAIN |
| response time (ms), mean | 259.5 | 246.1 | −5.1% | −26.8730 to +0.1855 | no |
| response time (ms), 95th percentile | 950.7 | 1038 | +9.2% | −21.8499 to +197.0559 | no |
| response time (ms), 99th percentile | 1384 | 1519 | +9.7% | −12.5337 to +281.5439 | no |
| time over the response line (% of samples) | 7.189 | 7.791 | +8.4% | −0.6598 to +1.8652 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 5.7 | 6.9 | +21.1% | −0.3004 to +2.7004 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 122.9 | +122.900 (native is 0) | +69.1144 to +176.6856 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 16.65 | 19.97 | +20.0% | −3.5184 to +10.1617 | no |
| utilisation (used / allocatable) | 0.0554 | 0.07299 | +31.7% | +0.0081 to +0.0270 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.33 | 1.323 | −0.5% | −0.0436 to +0.0299 | no |
| Omni's own CPU (cores), mean | 0 | 0.07382 | +0.074 (native is 0) | +0.0655 to +0.0821 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.33 | 1.397 | +5.0% | +0.0272 to +0.1067 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 503.1 | 413.8 | −17.7% | −141.1505 to −37.3740 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.017 | 2.075 | +2.9% | −0.1701 to +0.2863 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.1427 to +1.4573 | yes: power given |
| pod start wait, total (s) | 0 | 1.3 | +1.300 (native is 0) | +0.3433 to +2.2567 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.033 | +1.033 (native is 0) | +0.3547 to +1.7119 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.31 | 43.45 | +7.8% | +2.3806 to +3.8896 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 773.7 | 784.3 | +1.4% | −2.4910 to +23.6910 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.704 | −38.3% | −3.4805 to −1.1121 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8542 | 0.9125 | +6.8% | −0.1144 to +0.2311 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.3 | 2.5 | +8.7% | −1.1821 to +1.5821 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.49 | 88.21 | +11.0% | −1.4085 to +18.8418 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*