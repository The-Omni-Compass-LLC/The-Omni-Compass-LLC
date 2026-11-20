# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.512 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.6 | 142.9 |
| response time (ms), 95th percentile | 235.4 | 251.5 |
| response time (ms), 99th percentile | 335.2 | 357.4 |
| time over the response line (% of samples) | 0.1217 | 0.1531 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1041 | 1155 |
| utilisation (used / allocatable) | 0.06013 | 0.05825 |
| CPU used (cores), mean | 1.443 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0.06398 |
| CPU used with Omni's own (cores), mean | 1.443 | 1.462 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.4 | 463.5 |
| HPA replicas, mean | 2.03 | 2.062 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 1 |
| pod start wait, mean (s) | 0 | 0.4 |
| host CPU busy, the real machine under kind (%) | 45.12 | 46.19 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1505 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 151 | 185.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 790.6 | 767.7 |
| queue: job turnaround, submitted to done, mean (s) | 826.1 | 856.6 |
| queue: jobs unfinished at the window's end | 8 | 11.2 |
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
| node-hours | 2.512 | 2.516 | +0.2% | −0.0044 to +0.0124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 271.7 | −0.1% | −1.4808 to +0.8441 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 271.7 | −0.1% | −1.4808 to +0.8441 | no |
| response time (ms), mean | 138.6 | 142.9 | +3.1% | +0.9418 to +7.6171 | yes: LOSS |
| response time (ms), 95th percentile | 235.4 | 251.5 | +6.9% | +5.1366 to +27.1244 | yes: LOSS |
| response time (ms), 99th percentile | 335.2 | 357.4 | +6.6% | −1.0971 to +45.4679 | no |
| time over the response line (% of samples) | 0.1217 | 0.1531 | +25.8% | −0.0472 to +0.1099 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.1 | +29.100 (native is 0) | +22.3102 to +35.8898 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1041 | 1155 | +10.9% | +58.0926 to +169.5007 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06013 | 0.05825 | −3.1% | −0.0032 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.398 | −3.1% | −0.0774 to −0.0129 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06398 | +0.064 (native is 0) | +0.0600 to +0.0679 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.462 | +1.3% | −0.0129 to +0.0505 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.4 | 463.5 | +2.9% | +3.7374 to +22.3891 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.03 | 2.062 | +1.6% | −0.2438 to +0.3078 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −1.0232 to +3.0232 | no |
| pod start wait, mean (s) | 0 | 0.4 | +0.400 (native is 0) | −0.2911 to +1.0911 | no |
| host CPU busy, the real machine under kind (%) | 45.12 | 46.19 | +2.4% | +0.3136 to +1.8243 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1505 | 1510 | +0.3% | −1.4229 to +10.2229 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 151 | 185.5 | +22.8% | +2.8185 to +66.1482 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 790.6 | 767.7 | −2.9% | −188.7472 to +142.9472 | no |
| queue: job turnaround, submitted to done, mean (s) | 826.1 | 856.6 | +3.7% | −18.3982 to +79.4732 | no |
| queue: jobs unfinished at the window's end | 8 | 11.2 | +40.0% | −0.3654 to +6.7654 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*