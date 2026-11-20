# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 120.9 | 66.71 |
| response time (ms), 95th percentile | 275 | 92.4 |
| response time (ms), 99th percentile | 400.4 | 116.5 |
| time over the response line (% of samples) | 1.173 | 0.0122 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 90 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.08 |
| utilisation (used / allocatable) | 0.03273 | 0.03197 |
| CPU used (cores), mean | 0.7854 | 0.7673 |
| Omni's own CPU (cores), mean | 0 | 0.03122 |
| CPU used with Omni's own (cores), mean | 0.7854 | 0.7985 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 872.6 | 879.5 |
| HPA replicas, mean | 7.913 | 8.134 |
| pods started | 5 | 4.9 |
| pod start wait, total (s) | 6.6 | 6.5 |
| pod start wait, mean (s) | 1.378 | 1.31 |
| host CPU busy, the real machine under kind (%) | 24.15 | 24.83 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.513 | 1.514 | +0.1% | −0.0002 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 157.7 | 157.6 | −0.0% | −0.3230 to +0.2159 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 157.7 | 157.6 | −0.0% | −0.3230 to +0.2159 | no |
| response time (ms), mean | 120.9 | 66.71 | −44.8% | −79.0303 to −29.3486 | yes: GAIN |
| response time (ms), 95th percentile | 275 | 92.4 | −66.4% | −256.5834 to −108.6686 | yes: GAIN |
| response time (ms), 99th percentile | 400.4 | 116.5 | −70.9% | −390.6118 to −177.2182 | yes: GAIN |
| time over the response line (% of samples) | 1.173 | 0.0122 | −99.0% | −2.4852 to +0.1637 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 1.3 | 0 | −100.0% | −2.9537 to +0.3537 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 19.3 | +19.300 (native is 0) | +17.4210 to +21.1790 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1867 | 0.08 | −57.1% | −0.3479 to +0.1346 | no |
| utilisation (used / allocatable) | 0.03273 | 0.03197 | −2.3% | −0.0017 to +0.0002 | no |
| CPU used (cores), mean | 0.7854 | 0.7673 | −2.3% | −0.0402 to +0.0038 | no |
| Omni's own CPU (cores), mean | 0 | 0.03122 | +0.031 (native is 0) | +0.0259 to +0.0365 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 0.7854 | 0.7985 | +1.7% | −0.0049 to +0.0310 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 872.6 | 879.5 | +0.8% | −14.4513 to +28.3688 | no |
| HPA replicas, mean | 7.913 | 8.134 | +2.8% | −0.1813 to +0.6215 | no |
| pods started | 5 | 4.9 | −2.0% | −1.0802 to +0.8802 | no |
| pod start wait, total (s) | 6.6 | 6.5 | −1.5% | −2.3227 to +2.1227 | no |
| pod start wait, mean (s) | 1.378 | 1.31 | −5.0% | −0.4610 to +0.3244 | no |
| host CPU busy, the real machine under kind (%) | 24.15 | 24.83 | +2.8% | +0.1565 to +1.1885 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*