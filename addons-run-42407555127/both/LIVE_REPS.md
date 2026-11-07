# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 161 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 161 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 157 | 112.1 |
| response time (ms), 95th percentile | 313.1 | 208.6 |
| response time (ms), 99th percentile | 472.7 | 346.6 |
| time over the response line (% of samples) | 0.8437 | 0.1511 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 465.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1617 | 0.08167 |
| utilisation (used / allocatable) | 0.03738 | 0.04913 |
| CPU used (cores), mean | 0.8972 | 1.179 |
| Omni's own CPU (cores), mean | 0 | 0.1302 |
| CPU used with Omni's own (cores), mean | 0.8972 | 1.309 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 702.3 | 543.4 |
| HPA replicas, mean | 8.886 | 11.62 |
| pods started | 5 | 8.7 |
| pod start wait, total (s) | 6.5 | 13.8 |
| pod start wait, mean (s) | 1.347 | 1.565 |
| host CPU busy, the real machine under kind (%) | 28.58 | 40.95 |
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
| node-hours | 1.512 | 1.51 | −0.1% | −0.0050 to +0.0023 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 158.5 | 161 | +1.6% | +2.0324 to +2.9890 | yes: power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 158.5 | 161 | +1.6% | +2.0324 to +2.9890 | yes: power given |
| response time (ms), mean | 157 | 112.1 | −28.6% | −51.2263 to −38.5382 | yes: GAIN |
| response time (ms), 95th percentile | 313.1 | 208.6 | −33.4% | −116.9621 to −92.0459 | yes: GAIN |
| response time (ms), 99th percentile | 472.7 | 346.6 | −26.7% | −162.6507 to −89.5625 | yes: GAIN |
| time over the response line (% of samples) | 0.8437 | 0.1511 | −82.1% | −1.0698 to −0.3154 | yes: GAIN |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.5 | 0.1 | −80.0% | −0.7694 to −0.0306 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 465.3 | +465.300 (native is 0) | +344.4062 to +586.1938 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1617 | 0.08167 | −49.5% | −0.2846 to +0.1246 | no |
| utilisation (used / allocatable) | 0.03738 | 0.04913 | +31.4% | +0.0110 to +0.0125 | yes, up (shown, not judged) |
| CPU used (cores), mean | 0.8972 | 1.179 | +31.4% | +0.2644 to +0.2993 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.1302 | +0.130 (native is 0) | +0.1028 to +0.1576 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.8972 | 1.309 | +45.9% | +0.3757 to +0.4483 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 702.3 | 543.4 | −22.6% | −167.9176 to −149.8522 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.886 | 11.62 | +30.7% | +1.9868 to +3.4715 | yes: power given |
| pods started | 5 | 8.7 | +74.0% | +1.7615 to +5.6385 | yes: power given |
| pod start wait, total (s) | 6.5 | 13.8 | +112.3% | +4.2270 to +10.3730 | yes: LOSS |
| pod start wait, mean (s) | 1.347 | 1.565 | +16.2% | −0.0161 to +0.4534 | no |
| host CPU busy, the real machine under kind (%) | 28.58 | 40.95 | +43.2% | +11.0531 to +13.6719 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*