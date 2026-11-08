# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.337 | 4.341 |
| energy, parked workers still on at idle power (Wh, declared model) | 480.7 | 480 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.7 | 480 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 268.5 | 134.1 |
| response time (ms), 95th percentile | 694.5 | 272.7 |
| response time (ms), 99th percentile | 1322 | 695.3 |
| time over the response line (% of samples) | 12.63 | 2.984 |
| failed requests (%) | 0.9937 | 0.9173 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.4 | 8.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 72.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 52.86 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.725 |
| utilisation (used / allocatable) | 0.07711 | 0.0754 |
| CPU used (cores), mean | 1.851 | 1.81 |
| Omni's own CPU (cores), mean | 0 | 0.04357 |
| CPU used with Omni's own (cores), mean | 1.851 | 1.853 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 396.1 | 402.4 |
| HPA replicas, mean | 9.652 | 12.12 |
| pods started | 6.2 | 16.5 |
| pod start wait, total (s) | 10.4 | 28.4 |
| pod start wait, mean (s) | 1.744 | 1.69 |
| host CPU busy, the real machine under kind (%) | 53.56 | 54.15 |
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
| node-hours | 4.337 | 4.341 | +0.1% | −0.0052 to +0.0122 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 480.7 | 480 | −0.1% | −1.8433 to +0.4675 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 480.7 | 480 | −0.1% | −1.8433 to +0.4675 | no |
| response time (ms), mean | 268.5 | 134.1 | −50.0% | −184.4695 to −84.2691 | yes: GAIN |
| response time (ms), 95th percentile | 694.5 | 272.7 | −60.7% | −556.9892 to −286.5018 | yes: GAIN |
| response time (ms), 99th percentile | 1322 | 695.3 | −47.4% | −906.7895 to −346.3909 | yes: GAIN |
| time over the response line (% of samples) | 12.63 | 2.984 | −76.4% | −14.6876 to −4.5973 | yes: GAIN |
| failed requests (%) | 0.9937 | 0.9173 | −7.7% | −0.1609 to +0.0080 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 22.4 | 8.5 | −62.1% | −19.7058 to −8.0942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 72.8 | +72.800 (native is 0) | +56.1956 to +89.4044 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3417 | 0.725 | +112.2% | −0.2232 to +0.9899 | no |
| utilisation (used / allocatable) | 0.07711 | 0.0754 | −2.2% | −0.0026 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.851 | 1.81 | −2.2% | −0.0625 to −0.0200 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04357 | +0.044 (native is 0) | +0.0357 to +0.0515 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.851 | 1.853 | +0.1% | −0.0141 to +0.0187 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 396.1 | 402.4 | +1.6% | +3.4724 to +9.2542 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.652 | 12.12 | +25.5% | +0.7690 to +4.1601 | yes: power given |
| pods started | 6.2 | 16.5 | +166.1% | +5.7006 to +14.8994 | yes: power given |
| pod start wait, total (s) | 10.4 | 28.4 | +173.1% | +9.1489 to +26.8511 | yes: LOSS |
| pod start wait, mean (s) | 1.744 | 1.69 | −3.1% | −0.2500 to +0.1416 | no |
| host CPU busy, the real machine under kind (%) | 53.56 | 54.15 | +1.1% | +0.1782 to +1.0031 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*