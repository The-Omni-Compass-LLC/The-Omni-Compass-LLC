# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.511 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 170 | 170.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170 | 170.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 402.2 | 419.6 |
| response time (ms), 95th percentile | 1639 | 1904 |
| response time (ms), 99th percentile | 4040 | 4299 |
| time over the response line (% of samples) | 18.24 | 19.21 |
| failed requests (%) | 1.89 | 0.9454 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 427 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.503 | 1.453 |
| utilisation (used / allocatable) | 0.08812 | 0.0882 |
| CPU used (cores), mean | 2.115 | 2.117 |
| Omni's own CPU (cores), mean | 0 | 0.07644 |
| CPU used with Omni's own (cores), mean | 2.115 | 2.193 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 330.4 | 329.3 |
| HPA replicas, mean | 14.82 | 15.43 |
| pods started | 5.6 | 6 |
| pod start wait, total (s) | 9.5 | 10.3 |
| pod start wait, mean (s) | 1.652 | 1.696 |
| host CPU busy, the real machine under kind (%) | 61.21 | 63.94 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 330.9 | 360.8 |
| second app: response time (ms), 99th percentile | 1992 | 2971 |
| second app: time over the response line (% of samples) | 11.64 | 12.22 |
| second app: failed requests (%) | 9.118 | 9.198 |

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
| node-hours | 1.511 | 1.516 | +0.3% | +0.0000 to +0.0096 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 170 | 170.5 | +0.3% | −0.2114 to +1.1447 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170 | 170.5 | +0.3% | −0.2114 to +1.1447 | no |
| response time (ms), mean | 402.2 | 419.6 | +4.3% | −20.0456 to +54.7662 | no |
| response time (ms), 95th percentile | 1639 | 1904 | +16.2% | −83.4152 to +613.9362 | no |
| response time (ms), 99th percentile | 4040 | 4299 | +6.4% | −438.5126 to +955.8850 | no |
| time over the response line (% of samples) | 18.24 | 19.21 | +5.3% | +0.0654 to +1.8753 | yes: LOSS |
| failed requests (%) | 1.89 | 0.9454 | −50.0% | −1.9984 to +0.1088 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7 | 7.1 | +1.4% | −0.8802 to +1.0802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 427 | +427.000 (native is 0) | +375.6615 to +478.3385 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.503 | 1.453 | −3.3% | −0.9751 to +0.8751 | no |
| utilisation (used / allocatable) | 0.08812 | 0.0882 | +0.1% | −0.0014 to +0.0016 | no |
| CPU used (cores), mean | 2.115 | 2.117 | +0.1% | −0.0336 to +0.0376 | no |
| Omni's own CPU (cores), mean | 0 | 0.07644 | +0.076 (native is 0) | +0.0640 to +0.0889 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.115 | 2.193 | +3.7% | +0.0445 to +0.1124 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 330.4 | 329.3 | −0.4% | −7.4517 to +5.1112 | no |
| HPA replicas, mean | 14.82 | 15.43 | +4.1% | −0.1427 to +1.3676 | no |
| pods started | 5.6 | 6 | +7.1% | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 9.5 | 10.3 | +8.4% | −0.4526 to +2.0526 | no |
| pod start wait, mean (s) | 1.652 | 1.696 | +2.7% | −0.1058 to +0.1938 | no |
| host CPU busy, the real machine under kind (%) | 61.21 | 63.94 | +4.5% | +1.7579 to +3.6965 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 330.9 | 360.8 | +9.1% | −73.2325 to +133.1485 | no |
| second app: response time (ms), 99th percentile | 1992 | 2971 | +49.2% | −779.2635 to +2738.4437 | no |
| second app: time over the response line (% of samples) | 11.64 | 12.22 | +5.0% | −0.5892 to +1.7469 | no |
| second app: failed requests (%) | 9.118 | 9.198 | +0.9% | −0.1973 to +0.3580 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*