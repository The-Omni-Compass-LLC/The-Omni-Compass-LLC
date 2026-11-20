# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.329 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 477.4 | 477.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.4 | 477.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 238.3 | 120.1 |
| response time (ms), 95th percentile | 619.9 | 251.9 |
| response time (ms), 99th percentile | 1137 | 547.8 |
| time over the response line (% of samples) | 9.889 | 2.58 |
| failed requests (%) | 0.8135 | 0.7829 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.5 | 7.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 32.94 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0.7033 |
| utilisation (used / allocatable) | 0.07349 | 0.07222 |
| CPU used (cores), mean | 1.764 | 1.733 |
| Omni's own CPU (cores), mean | 0 | 0.04215 |
| CPU used with Omni's own (cores), mean | 1.764 | 1.776 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.8 | 414.2 |
| HPA replicas, mean | 9.676 | 11.71 |
| pods started | 6.6 | 16.9 |
| pod start wait, total (s) | 10.2 | 26.6 |
| pod start wait, mean (s) | 1.56 | 1.537 |
| host CPU busy, the real machine under kind (%) | 51.2 | 51.9 |
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
| node-hours | 4.329 | 4.335 | +0.1% | +0.0004 to +0.0123 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 477.4 | 477.3 | −0.0% | −0.9749 to +0.7762 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 477.4 | 477.3 | −0.0% | −0.9749 to +0.7762 | no |
| response time (ms), mean | 238.3 | 120.1 | −49.6% | −158.9265 to −77.4434 | yes: GAIN |
| response time (ms), 95th percentile | 619.9 | 251.9 | −59.4% | −471.9762 to −264.0088 | yes: GAIN |
| response time (ms), 99th percentile | 1137 | 547.8 | −51.8% | −832.4858 to −345.6194 | yes: GAIN |
| time over the response line (% of samples) | 9.889 | 2.58 | −73.9% | −11.1602 to −3.4566 | yes: GAIN |
| failed requests (%) | 0.8135 | 0.7829 | −3.8% | −0.0754 to +0.0142 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 18.5 | 7.3 | −60.5% | −15.7340 to −6.6660 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 71.3 | +71.300 (native is 0) | +55.3906 to +87.2094 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5333 | 0.7033 | +31.9% | −0.3029 to +0.6429 | no |
| utilisation (used / allocatable) | 0.07349 | 0.07222 | −1.7% | −0.0020 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.764 | 1.733 | −1.7% | −0.0469 to −0.0140 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04215 | +0.042 (native is 0) | +0.0347 to +0.0496 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.764 | 1.776 | +0.7% | −0.0057 to +0.0291 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 407.8 | 414.2 | +1.6% | +2.4025 to +10.3586 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.676 | 11.71 | +21.0% | +0.5398 to +3.5271 | yes: power given |
| pods started | 6.6 | 16.9 | +156.1% | +5.9418 to +14.6582 | yes: power given |
| pod start wait, total (s) | 10.2 | 26.6 | +160.8% | +8.0160 to +24.7840 | yes: LOSS |
| pod start wait, mean (s) | 1.56 | 1.537 | −1.5% | −0.2617 to +0.2158 | no |
| host CPU busy, the real machine under kind (%) | 51.2 | 51.9 | +1.4% | +0.0610 to +1.3382 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*