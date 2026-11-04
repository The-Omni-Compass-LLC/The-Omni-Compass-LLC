# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 160.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 160.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 200.5 | 103.3 |
| response time (ms), 95th percentile | 473.9 | 249 |
| response time (ms), 99th percentile | 643.4 | 508.2 |
| time over the response line (% of samples) | 4.569 | 1.248 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.05333 |
| utilisation (used / allocatable) | 0.03017 | 0.04451 |
| CPU used (cores), mean | 0.7241 | 1.068 |
| Omni's own CPU (cores), mean | 0 | 0.05896 |
| CPU used with Omni's own (cores), mean | 0.7241 | 1.127 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.6 | 599.7 |
| HPA replicas, mean | 2.909 | 2.586 |
| pods started | 2.9 | 2.5 |
| pod start wait, total (s) | 4.1 | 4 |
| pod start wait, mean (s) | 1.383 | 1.667 |
| host CPU busy, the real machine under kind (%) | 23.75 | 35.02 |
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
| node-hours | 1.514 | 1.514 | −0.0% | −0.0115 to +0.0105 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.4 | 160.6 | +2.0% | +1.8372 to +4.6129 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.4 | 160.6 | +2.0% | +1.8372 to +4.6129 | yes: power given |
| response time (ms), mean | 200.5 | 103.3 | −48.5% | −113.6673 to −80.7572 | yes: GAIN |
| response time (ms), 95th percentile | 473.9 | 249 | −47.5% | −266.4030 to −183.3440 | yes: GAIN |
| response time (ms), 99th percentile | 643.4 | 508.2 | −21.0% | −213.4994 to −56.9556 | yes: GAIN |
| time over the response line (% of samples) | 4.569 | 1.248 | −72.7% | −5.4699 to −1.1722 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 4.6 | 2 | −56.5% | −4.4531 to −0.7469 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 82.3 | +82.300 (native is 0) | +68.0295 to +96.5705 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.16 | 0.05333 | −66.7% | −0.2675 to +0.0542 | no |
| utilisation (used / allocatable) | 0.03017 | 0.04451 | +47.5% | +0.0126 to +0.0161 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.7241 | 1.068 | +47.5% | +0.3022 to +0.3859 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05896 | +0.059 (native is 0) | +0.0509 to +0.0671 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7241 | 1.127 | +55.7% | +0.3547 to +0.4514 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 863.6 | 599.7 | −30.6% | −281.6552 to −246.1684 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.909 | 2.586 | −11.1% | −0.5705 to −0.0759 | yes: GAIN |
| pods started | 2.9 | 2.5 | −13.8% | −0.9001 to +0.1001 | no |
| pod start wait, total (s) | 4.1 | 4 | −2.4% | −1.4254 to +1.2254 | no |
| pod start wait, mean (s) | 1.383 | 1.667 | +20.5% | −0.2163 to +0.7830 | no |
| host CPU busy, the real machine under kind (%) | 23.75 | 35.02 | +47.5% | +9.9471 to +12.6020 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*