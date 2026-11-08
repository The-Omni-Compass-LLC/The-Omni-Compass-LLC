# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 160.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 160.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 175.9 | 89.29 |
| response time (ms), 95th percentile | 427.9 | 216.5 |
| response time (ms), 99th percentile | 586.6 | 454.5 |
| time over the response line (% of samples) | 3.308 | 0.9956 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.07833 |
| utilisation (used / allocatable) | 0.02925 | 0.04198 |
| CPU used (cores), mean | 0.702 | 1.007 |
| Omni's own CPU (cores), mean | 0 | 0.05135 |
| CPU used with Omni's own (cores), mean | 0.702 | 1.059 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 889 | 635.4 |
| HPA replicas, mean | 2.869 | 2.465 |
| pods started | 3.1 | 2.4 |
| pod start wait, total (s) | 4.1 | 3 |
| pod start wait, mean (s) | 1.308 | 1.183 |
| host CPU busy, the real machine under kind (%) | 22.83 | 33.03 |
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
| node-hours | 1.516 | 1.515 | −0.1% | −0.0092 to +0.0075 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 160.2 | +1.8% | +1.7253 to +3.8616 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 160.2 | +1.8% | +1.7253 to +3.8616 | yes: power given |
| response time (ms), mean | 175.9 | 89.29 | −49.2% | −106.2732 to −67.0104 | yes: GAIN |
| response time (ms), 95th percentile | 427.9 | 216.5 | −49.4% | −256.1562 to −166.7898 | yes: GAIN |
| response time (ms), 99th percentile | 586.6 | 454.5 | −22.5% | −181.6831 to −82.3547 | yes: GAIN |
| time over the response line (% of samples) | 3.308 | 0.9956 | −69.9% | −3.6795 to −0.9458 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 3.5 | 1 | −71.4% | −3.7729 to −1.2271 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.4 | +71.400 (native is 0) | +49.1010 to +93.6990 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.07833 | 0.07833 | 0.0% | raw −0.1509 to +0.1509 | STEADY, the same (to nine decimal places) |
| utilisation (used / allocatable) | 0.02925 | 0.04198 | +43.5% | +0.0106 to +0.0149 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.702 | 1.007 | +43.5% | +0.2543 to +0.3565 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05135 | +0.051 (native is 0) | +0.0437 to +0.0590 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.702 | 1.059 | +50.8% | +0.2994 to +0.4141 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 889 | 635.4 | −28.5% | −274.7208 to −232.3934 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.869 | 2.465 | −14.1% | −0.7146 to −0.0933 | yes: GAIN |
| pods started | 3.1 | 2.4 | −22.6% | −1.2889 to −0.1111 | yes: GAIN |
| pod start wait, total (s) | 4.1 | 3 | −26.8% | −2.2898 to +0.0898 | no |
| pod start wait, mean (s) | 1.308 | 1.183 | −9.6% | −0.5075 to +0.2575 | no |
| host CPU busy, the real machine under kind (%) | 22.83 | 33.03 | +44.7% | +8.6006 to +11.7904 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*