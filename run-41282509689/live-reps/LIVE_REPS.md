# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.513 | 4.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.5 | 511.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.5 | 511.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 256.5 | 138.1 |
| response time (ms), 95th percentile | 690 | 290.6 |
| response time (ms), 99th percentile | 2148 | 1167 |
| time over the response line (% of samples) | 16.53 | 9.913 |
| failed requests (%) | 8.821 | 7.831 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.2 | 18.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.625 |
| utilisation (used / allocatable) | 0.09552 | 0.09358 |
| CPU used (cores), mean | 2.293 | 2.246 |
| Omni's own CPU (cores), mean | 0 | 0.00902 |
| CPU used with Omni's own (cores), mean | 2.293 | 2.255 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.8 | 338.4 |
| HPA replicas, mean | 9.506 | 9.894 |
| pods started | 5.8 | 7.1 |
| pod start wait, total (s) | 7.6 | 10.8 |
| pod start wait, mean (s) | 1.335 | 1.532 |
| host CPU busy, the real machine under kind (%) | 64.61 | 63.65 |
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
| node-hours | 4.513 | 4.517 | +0.1% | −0.0018 to +0.0114 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.5 | 511.9 | −0.1% | −1.4454 to +0.1329 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.5 | 511.9 | −0.1% | −1.4454 to +0.1329 | no |
| response time (ms), mean | 256.5 | 138.1 | −46.2% | −157.7844 to −79.0054 | yes: GAIN |
| response time (ms), 95th percentile | 690 | 290.6 | −57.9% | −515.9039 to −283.0261 | yes: GAIN |
| response time (ms), 99th percentile | 2148 | 1167 | −45.7% | −1808.3132 to −154.2592 | yes: GAIN |
| time over the response line (% of samples) | 16.53 | 9.913 | −40.0% | −9.4366 to −3.8066 | yes: GAIN |
| failed requests (%) | 8.821 | 7.831 | −11.2% | −1.7987 to −0.1815 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 25.2 | 18.4 | −27.0% | −9.1796 to −4.4204 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.5 | +37.500 (native is 0) | +27.0727 to +47.9273 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2633 | 0.625 | +137.3% | −0.0138 to +0.7372 | no |
| utilisation (used / allocatable) | 0.09552 | 0.09358 | −2.0% | −0.0026 to −0.0013 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.293 | 2.246 | −2.0% | −0.0618 to −0.0313 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00902 | +0.009 (native is 0) | +0.0075 to +0.0106 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.293 | 2.255 | −1.6% | −0.0538 to −0.0212 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 328.8 | 338.4 | +2.9% | +1.8046 to +17.3203 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.506 | 9.894 | +4.1% | −0.5550 to +1.3320 | no |
| pods started | 5.8 | 7.1 | +22.4% | −0.4210 to +3.0210 | no |
| pod start wait, total (s) | 7.6 | 10.8 | +42.1% | −0.6712 to +7.0712 | no |
| pod start wait, mean (s) | 1.335 | 1.532 | +14.7% | −0.1398 to +0.5327 | no |
| host CPU busy, the real machine under kind (%) | 64.61 | 63.65 | −1.5% | −1.4473 to −0.4831 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*