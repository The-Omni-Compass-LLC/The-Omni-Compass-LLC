# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 161 | 159.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161 | 159.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 70.15 | 56.58 |
| response time (ms), 95th percentile | 101.7 | 81.61 |
| response time (ms), 99th percentile | 112.1 | 95.53 |
| time over the response line (% of samples) | 0.01711 | 0 |
| failed requests (%) | 0.01711 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1881 | 0 |
| utilisation (used / allocatable) | 0.04557 | 0.04028 |
| CPU used (cores), mean | 1.094 | 0.9668 |
| Omni's own CPU (cores), mean | 0 | 0.03975 |
| CPU used with Omni's own (cores), mean | 1.094 | 1.007 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 590.3 | 661.4 |
| HPA replicas, mean | 2.789 | 2.587 |
| pods started | 2 | 1.333 |
| pod start wait, total (s) | 2.429 | 2.167 |
| pod start wait, mean (s) | 1.381 | 1.5 |
| host CPU busy, the real machine under kind (%) | 34.3 | 31.94 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.511 | 1.514 | +0.2% | −0.0366 to +0.0433 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 160.1 | 160.3 | +0.2% | −4.1237 to +4.6139 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.1 | 160.3 | +0.2% | −4.1237 to +4.6139 | no |
| response time (ms), mean | 63.08 | 64.63 | +2.5% | −5.9305 to +9.0272 | no |
| response time (ms), 95th percentile | 90.98 | 90.98 | −0.0% | −9.9102 to +9.9068 | no |
| response time (ms), 99th percentile | 100.7 | 104.8 | +4.1% | −21.6322 to +29.8455 | no |
| time over the response line (% of samples) | 0.03992 | 0 | −100.0% | −0.2117 to +0.1319 | no |
| failed requests (%) | 0.03992 | 0 | −100.0% | −0.2117 to +0.1319 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4.000 (native is 0) | +4.0000 to +4.0000 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2611 | 0 | −100.0% | −0.2850 to −0.2372 | yes, down (shown, not judged) |
| utilisation (used / allocatable) | 0.04344 | 0.04311 | −0.8% | −0.0041 to +0.0035 | no |
| CPU used (cores), mean | 1.043 | 1.035 | −0.8% | −0.0993 to +0.0836 | no |
| Omni's own CPU (cores), mean | 0 | 0.04353 | +0.044 (native is 0) | +0.0178 to +0.0693 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.043 | 1.078 | +3.4% | −0.0657 to +0.1371 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 617.8 | 621.3 | +0.6% | −39.7711 to +46.7913 | no |
| HPA replicas, mean | 2.73 | 2.599 | −4.8% | −0.4586 to +0.1967 | no |
| pods started | 2 | 1.333 | −33.3% | −3.5353 to +2.2020 | no |
| pod start wait, total (s) | 2.333 | 2 | −14.3% | −3.2020 to +2.5353 | no |
| pod start wait, mean (s) | 1.333 | 1.5 | +12.5% | −2.4191 to +2.7524 | no |
| host CPU busy, the real machine under kind (%) | 32.86 | 34.16 | +3.9% | +0.3528 to +2.2427 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*