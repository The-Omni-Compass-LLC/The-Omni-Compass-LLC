# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.517 | 4.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 509.2 | 508.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 509.2 | 508.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 243.8 | 145.9 |
| response time (ms), 95th percentile | 658 | 308.7 |
| response time (ms), 99th percentile | 1977 | 1518 |
| time over the response line (% of samples) | 13.95 | 8.729 |
| failed requests (%) | 6.1 | 6.26 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.7 | 16.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.485 | 0.7183 |
| utilisation (used / allocatable) | 0.08982 | 0.08919 |
| CPU used (cores), mean | 2.156 | 2.141 |
| Omni's own CPU (cores), mean | 0 | 0.04062 |
| CPU used with Omni's own (cores), mean | 2.156 | 2.181 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 345.9 | 350.9 |
| HPA replicas, mean | 9.483 | 12.33 |
| pods started | 5.7 | 9.9 |
| pod start wait, total (s) | 7.5 | 15.7 |
| pod start wait, mean (s) | 1.325 | 1.544 |
| host CPU busy, the real machine under kind (%) | 60.61 | 61.75 |
| host cores (the real machine under kind) | 4 | 4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 4.517 | 4.513 | −0.1% | −0.0104 to +0.0018 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 509.2 | 508.3 | −0.2% | −2.2777 to +0.4811 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 509.2 | 508.3 | −0.2% | −2.2777 to +0.4811 | no |
| response time (ms), mean | 243.8 | 145.9 | −40.2% | −127.0745 to −68.7532 | yes: GAIN |
| response time (ms), 95th percentile | 658 | 308.7 | −53.1% | −446.5417 to −252.0813 | yes: GAIN |
| response time (ms), 99th percentile | 1977 | 1518 | −23.2% | −916.4806 to −0.9826 | yes: GAIN |
| time over the response line (% of samples) | 13.95 | 8.729 | −37.4% | −7.7012 to −2.7487 | yes: GAIN |
| failed requests (%) | 6.1 | 6.26 | +2.6% | −0.3549 to +0.6757 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.7 | 16.1 | −29.1% | −9.7125 to −3.4875 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.8 | +50.800 (native is 0) | +38.4989 to +63.1011 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.485 | 0.7183 | +48.1% | −0.2872 to +0.7539 | no |
| utilisation (used / allocatable) | 0.08982 | 0.08919 | −0.7% | −0.0022 to +0.0009 | no |
| CPU used (cores), mean | 2.156 | 2.141 | −0.7% | −0.0520 to +0.0217 | no |
| Omni's own CPU (cores), mean | 0 | 0.04062 | +0.041 (native is 0) | +0.0334 to +0.0479 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.156 | 2.181 | +1.2% | −0.0159 to +0.0669 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 345.9 | 350.9 | +1.4% | −3.7276 to +13.7474 | no |
| HPA replicas, mean | 9.483 | 12.33 | +30.0% | +0.9253 to +4.7625 | yes: power given |
| pods started | 5.7 | 9.9 | +73.7% | +2.0461 to +6.3539 | yes: power given |
| pod start wait, total (s) | 7.5 | 15.7 | +109.3% | +3.7037 to +12.6963 | yes: LOSS |
| pod start wait, mean (s) | 1.325 | 1.544 | +16.6% | −0.0127 to +0.4520 | no |
| host CPU busy, the real machine under kind (%) | 60.61 | 61.75 | +1.9% | −0.0156 to +2.2907 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*