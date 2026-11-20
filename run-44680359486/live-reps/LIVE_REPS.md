# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.995 |
| node-hours | 4.516 | 4.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 512.1 | 511.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.1 | 510.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 264.4 | 162.6 |
| response time (ms), 95th percentile | 713.2 | 359.5 |
| response time (ms), 99th percentile | 2353 | 2059 |
| time over the response line (% of samples) | 16.08 | 11.08 |
| failed requests (%) | 8.449 | 8.267 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 18.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 85 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.6667 |
| utilisation (used / allocatable) | 0.09433 | 0.09326 |
| CPU used (cores), mean | 2.264 | 2.238 |
| Omni's own CPU (cores), mean | 0 | 0.0444 |
| CPU used with Omni's own (cores), mean | 2.264 | 2.282 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 332.8 | 335.8 |
| HPA replicas, mean | 9.484 | 11.28 |
| pods started | 5.7 | 8.7 |
| pod start wait, total (s) | 9.1 | 15.4 |
| pod start wait, mean (s) | 1.615 | 1.751 |
| host CPU busy, the real machine under kind (%) | 63.98 | 65.18 |
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
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0159 to +0.0061 | no |
| node-hours | 4.516 | 4.51 | −0.1% | −0.0145 to +0.0028 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 512.1 | 511.2 | −0.2% | −2.1631 to +0.3303 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 512.1 | 510.9 | −0.2% | −2.8774 to +0.4947 | no |
| response time (ms), mean | 264.4 | 162.6 | −38.5% | −134.6697 to −68.9234 | yes: GAIN |
| response time (ms), 95th percentile | 713.2 | 359.5 | −49.6% | −520.4028 to −187.0962 | yes: GAIN |
| response time (ms), 99th percentile | 2353 | 2059 | −12.5% | −836.7030 to +249.6154 | no |
| time over the response line (% of samples) | 16.08 | 11.08 | −31.1% | −7.2467 to −2.7382 | yes: GAIN |
| failed requests (%) | 8.449 | 8.267 | −2.2% | −1.2831 to +0.9183 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 23.6 | 18.3 | −22.5% | −8.1222 to −2.4778 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 50.9 | +50.900 (native is 0) | +41.1244 to +60.6756 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.295 | 0.6667 | +126.0% | +0.0829 to +0.6604 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09433 | 0.09326 | −1.1% | −0.0032 to +0.0011 | no |
| CPU used (cores), mean | 2.264 | 2.238 | −1.2% | −0.0787 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0.0444 | +0.044 (native is 0) | +0.0365 to +0.0523 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.264 | 2.282 | +0.8% | −0.0343 to +0.0707 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 332.8 | 335.8 | +0.9% | −5.6153 to +11.6159 | no |
| HPA replicas, mean | 9.484 | 11.28 | +19.0% | +0.2794 to +3.3195 | yes: power given |
| pods started | 5.7 | 8.7 | +52.6% | +1.0338 to +4.9662 | yes: power given |
| pod start wait, total (s) | 9.1 | 15.4 | +69.2% | +2.3814 to +10.2186 | yes: LOSS |
| pod start wait, mean (s) | 1.615 | 1.751 | +8.4% | −0.1670 to +0.4398 | no |
| host CPU busy, the real machine under kind (%) | 63.98 | 65.18 | +1.9% | −0.1729 to +2.5762 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*