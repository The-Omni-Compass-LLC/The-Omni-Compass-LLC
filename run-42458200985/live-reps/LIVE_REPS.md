# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.515 | 2.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 141.7 | 117.1 |
| response time (ms), 95th percentile | 243 | 263.3 |
| response time (ms), 99th percentile | 348.6 | 383 |
| time over the response line (% of samples) | 0.1237 | 0.3761 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3333 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 109.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1236 | 1283 |
| utilisation (used / allocatable) | 0.05959 | 0.05892 |
| CPU used (cores), mean | 1.43 | 1.414 |
| Omni's own CPU (cores), mean | 0 | 0.07102 |
| CPU used with Omni's own (cores), mean | 1.43 | 1.485 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454 | 458.5 |
| HPA replicas, mean | 2.101 | 2.206 |
| pods started | 0 | 0.8333 |
| pod start wait, total (s) | 0 | 2 |
| pod start wait, mean (s) | 0 | 0.7778 |
| host CPU busy, the real machine under kind (%) | 45.09 | 46.89 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1510 | 1507 |
| batch: worker machines in service after the queue finished, mean | nan | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 145.3 | 190.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 674.9 | 832.2 |
| queue: job turnaround, submitted to done, mean (s) | 927.2 | 928 |
| queue: jobs unfinished at the window's end | 13.88 | 14.5 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 4 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.511 | 2.512 | +0.0% | −0.0276 to +0.0293 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 271.4 | −0.0% | −3.7091 to +3.6018 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 271.4 | −0.0% | −3.7091 to +3.6018 | no |
| response time (ms), mean | 141.4 | 116.4 | −17.6% | −33.3773 to −16.5137 | yes: GAIN |
| response time (ms), 95th percentile | 244.8 | 263.7 | +7.7% | −4.4931 to +42.2356 | no |
| response time (ms), 99th percentile | 346.1 | 390.3 | +12.8% | −4.7338 to +93.2743 | no |
| time over the response line (% of samples) | 0.1332 | 0.3571 | +168.0% | −0.4221 to +0.8699 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.25 | +0.250 (native is 0) | −0.5455 to +1.0455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115 | +115.000 (native is 0) | +84.5901 to +145.4099 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1229 | 1259 | +2.5% | −128.2453 to +189.0287 | no |
| utilisation (used / allocatable) | 0.05958 | 0.05885 | −1.2% | −0.0032 to +0.0018 | no |
| CPU used (cores), mean | 1.43 | 1.412 | −1.2% | −0.0774 to +0.0426 | no |
| Omni's own CPU (cores), mean | 0 | 0.07055 | +0.071 (native is 0) | +0.0575 to +0.0836 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.43 | 1.483 | +3.7% | −0.0030 to +0.1093 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.2 | 459.1 | +1.1% | −13.1464 to +22.9161 | no |
| HPA replicas, mean | 2.087 | 2.15 | +3.0% | −0.2637 to +0.3906 | no |
| pods started | 0 | 0.5 | +0.500 (native is 0) | −1.0910 to +2.0910 | no |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | −2.1820 to +4.1820 | no |
| pod start wait, mean (s) | 0 | 0.5 | +0.500 (native is 0) | −1.0910 to +2.0910 | no |
| host CPU busy, the real machine under kind (%) | 44.86 | 46.74 | +4.2% | +0.8918 to +2.8579 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1508 | +0.0% | −13.5616 to +15.0616 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 151 | 195.2 | +29.3% | −34.2408 to +122.5949 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 647 | 856.8 | +32.4% | −45.5163 to +465.0163 | no |
| queue: job turnaround, submitted to done, mean (s) | 911.1 | 920.3 | +1.0% | −96.3884 to +114.7634 | no |
| queue: jobs unfinished at the window's end | 14.75 | 14.25 | −3.4% | −7.4350 to +6.4350 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*