# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.333 |
| energy, parked workers still on at idle power (Wh, declared model) | 472.8 | 471.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 472.8 | 471.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 204 | 105 |
| response time (ms), 95th percentile | 528.3 | 192.7 |
| response time (ms), 99th percentile | 996.5 | 462 |
| time over the response line (% of samples) | 7.382 | 1.665 |
| failed requests (%) | 0.5994 | 0.5251 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.1 | 4.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 46.25 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.525 | 0.825 |
| utilisation (used / allocatable) | 0.06556 | 0.06418 |
| CPU used (cores), mean | 1.573 | 1.54 |
| Omni's own CPU (cores), mean | 0 | 0.03949 |
| CPU used with Omni's own (cores), mean | 1.573 | 1.58 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 464.6 |
| HPA replicas, mean | 9.485 | 10.84 |
| pods started | 7.6 | 17.2 |
| pod start wait, total (s) | 10.4 | 27.8 |
| pod start wait, mean (s) | 1.409 | 1.63 |
| host CPU busy, the real machine under kind (%) | 46.12 | 46.61 |
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
| node-hours | 4.334 | 4.333 | −0.0% | −0.0106 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 472.8 | 471.9 | −0.2% | −2.1491 to +0.2048 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 472.8 | 471.9 | −0.2% | −2.1491 to +0.2048 | no |
| response time (ms), mean | 204 | 105 | −48.5% | −142.6639 to −55.3111 | yes: GAIN |
| response time (ms), 95th percentile | 528.3 | 192.7 | −63.5% | −465.5656 to −205.7044 | yes: GAIN |
| response time (ms), 99th percentile | 996.5 | 462 | −53.6% | −772.2828 to −296.6362 | yes: GAIN |
| time over the response line (% of samples) | 7.382 | 1.665 | −77.4% | −9.8715 to −1.5624 | yes: GAIN |
| failed requests (%) | 0.5994 | 0.5251 | −12.4% | −0.1775 to +0.0289 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 15.1 | 4.9 | −67.5% | −16.2771 to −4.1229 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 68.1 | +68.100 (native is 0) | +47.0488 to +89.1512 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.525 | 0.825 | +57.1% | −0.2162 to +0.8162 | no |
| utilisation (used / allocatable) | 0.06556 | 0.06418 | −2.1% | −0.0025 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.573 | 1.54 | −2.1% | −0.0607 to −0.0055 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.03949 | +0.039 (native is 0) | +0.0324 to +0.0465 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.573 | 1.58 | +0.4% | −0.0180 to +0.0308 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.5 | 464.6 | +1.1% | −1.3426 to +11.4844 | no |
| HPA replicas, mean | 9.485 | 10.84 | +14.3% | −0.1856 to +2.8982 | no |
| pods started | 7.6 | 17.2 | +126.3% | +4.2770 to +14.9230 | yes: power given |
| pod start wait, total (s) | 10.4 | 27.8 | +167.3% | +9.1321 to +25.6679 | yes: LOSS |
| pod start wait, mean (s) | 1.409 | 1.63 | +15.7% | −0.0645 to +0.5070 | no |
| host CPU busy, the real machine under kind (%) | 46.12 | 46.61 | +1.1% | −0.1440 to +1.1253 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*