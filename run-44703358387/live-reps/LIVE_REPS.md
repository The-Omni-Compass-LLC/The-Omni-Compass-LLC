# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.769 |
| node-hours | 2.516 | 1.998 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 234.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 402.4 | 371.8 |
| response time (ms), 95th percentile | 1693 | 1707 |
| response time (ms), 99th percentile | 2277 | 2359 |
| time over the response line (% of samples) | 13 | 13.09 |
| failed requests (%) | 0.01198 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.9 | 29.38 |
| utilisation (used / allocatable) | 0.06138 | 0.07806 |
| CPU used (cores), mean | 1.473 | 1.469 |
| Omni's own CPU (cores), mean | 0 | 0.07659 |
| CPU used with Omni's own (cores), mean | 1.473 | 1.546 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.9 | 383.3 |
| HPA replicas, mean | 2.055 | 2.145 |
| pods started | 0.3 | 0.6 |
| pod start wait, total (s) | 0.5 | 0.9 |
| pod start wait, mean (s) | 0.3 | 0.4833 |
| host CPU busy, the real machine under kind (%) | 44.63 | 47.79 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 828.5 | 837.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.84 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.062 | 1.104 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.4 | 2.7 |
| queue: job turnaround, submitted to done, mean (s) | 130.2 | 137.3 |
| queue: jobs unfinished at the window's end | 0 | 0 |
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
| worker nodes in service, mean | 6 | 4.769 | −20.5% | −1.9999 to −0.4620 | yes: GAIN |
| node-hours | 2.516 | 1.998 | −20.6% | −0.8404 to −0.1950 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.2 | 273.1 | −0.0% | −0.9913 to +0.8877 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.2 | 234.4 | −14.2% | −63.0957 to −14.3579 | yes: GAIN |
| response time (ms), mean | 402.4 | 371.8 | −7.6% | −49.9407 to −11.2783 | yes: GAIN |
| response time (ms), 95th percentile | 1693 | 1707 | +0.9% | −54.6867 to +83.7017 | no |
| response time (ms), 99th percentile | 2277 | 2359 | +3.6% | −9.9000 to +173.9046 | no |
| time over the response line (% of samples) | 13 | 13.09 | +0.6% | −1.2457 to +1.4119 | no |
| failed requests (%) | 0.01198 | 0 | −100.0% | −0.0391 to +0.0151 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 9.6 | +5.5% | −0.6802 to +1.6802 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.2 | +80.200 (native is 0) | +32.9888 to +127.4112 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 26.9 | 29.38 | +9.2% | −0.8812 to +5.8346 | no |
| utilisation (used / allocatable) | 0.06138 | 0.07806 | +27.2% | +0.0057 to +0.0277 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.473 | 1.469 | −0.3% | −0.0306 to +0.0229 | no |
| Omni's own CPU (cores), mean | 0 | 0.07659 | +0.077 (native is 0) | +0.0680 to +0.0852 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.473 | 1.546 | +4.9% | +0.0414 to +0.1041 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.9 | 383.3 | −15.6% | −115.9070 to −25.3166 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.055 | 2.145 | +4.4% | −0.0848 to +0.2657 | no |
| pods started | 0.3 | 0.6 | +100.0% | −0.6567 to +1.2567 | no |
| pod start wait, total (s) | 0.5 | 0.9 | +80.0% | −1.1155 to +1.9155 | no |
| pod start wait, mean (s) | 0.3 | 0.4833 | +61.1% | −0.5196 to +0.8863 | no |
| host CPU busy, the real machine under kind (%) | 44.63 | 47.79 | +7.1% | +2.6992 to +3.6102 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 828.5 | 837.3 | +1.1% | +1.9573 to +15.6427 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.84 | −36.0% | −3.2411 to −1.0798 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 1.062 | 1.104 | +3.9% | −0.0816 to +0.1650 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.4 | 2.7 | −20.6% | −1.7144 to +0.3144 | no |
| queue: job turnaround, submitted to done, mean (s) | 130.2 | 137.3 | +5.5% | +0.5836 to +13.6831 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*