# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.987 |
| node-hours | 2.513 | 2.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.8 | 104.8 |
| response time (ms), 95th percentile | 245.9 | 234.5 |
| response time (ms), 99th percentile | 347.2 | 362.4 |
| time over the response line (% of samples) | 0.1919 | 0.2675 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1200 | 1216 |
| utilisation (used / allocatable) | 0.05949 | 0.05948 |
| CPU used (cores), mean | 1.428 | 1.425 |
| Omni's own CPU (cores), mean | 0 | 0.01274 |
| CPU used with Omni's own (cores), mean | 1.428 | 1.437 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.5 | 455.4 |
| HPA replicas, mean | 1.98 | 2.002 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 45.26 | 45.48 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1473 | 1477 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.4 |
| queue: job wait, submitted to its first pod running, mean (s) | 150.1 | 174.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 677.3 | 712.3 |
| queue: job turnaround, submitted to done, mean (s) | 865.7 | 877.2 |
| queue: jobs unfinished at the window's end | 12.5 | 12.4 |

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
| worker nodes in service, mean | 6 | 5.987 | −0.2% | −0.0431 to +0.0167 | no |
| node-hours | 2.513 | 2.51 | −0.1% | −0.0168 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.1 | +0.1% | −0.6525 to +1.1399 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.6 | −0.1% | −1.2667 to +0.9208 | no |
| response time (ms), mean | 138.8 | 104.8 | −24.5% | −39.4876 to −28.5513 | yes: GAIN |
| response time (ms), 95th percentile | 245.9 | 234.5 | −4.6% | −21.0272 to −1.7748 | yes: GAIN |
| response time (ms), 99th percentile | 347.2 | 362.4 | +4.4% | −8.4765 to +38.8209 | no |
| time over the response line (% of samples) | 0.1919 | 0.2675 | +39.4% | −0.0601 to +0.2113 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.8 | +12.800 (native is 0) | +10.8985 to +14.7015 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1200 | 1216 | +1.3% | −49.1683 to +79.7749 | no |
| utilisation (used / allocatable) | 0.05949 | 0.05948 | −0.0% | −0.0017 to +0.0017 | no |
| CPU used (cores), mean | 1.428 | 1.425 | −0.2% | −0.0414 to +0.0348 | no |
| Omni's own CPU (cores), mean | 0 | 0.01274 | +0.013 (native is 0) | +0.0119 to +0.0136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.428 | 1.437 | +0.7% | −0.0287 to +0.0476 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.5 | 455.4 | −0.0% | −12.0831 to +11.8213 | no |
| HPA replicas, mean | 1.98 | 2.002 | +1.1% | −0.0890 to +0.1320 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 45.26 | 45.48 | +0.5% | −0.5604 to +1.0073 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1473 | 1477 | +0.3% | −2.0983 to +10.6983 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.4 | −10.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 150.1 | 174.8 | +16.4% | −12.0873 to +61.4373 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 677.3 | 712.3 | +5.2% | −106.1411 to +176.1411 | no |
| queue: job turnaround, submitted to done, mean (s) | 865.7 | 877.2 | +1.3% | −59.4594 to +82.4510 | no |
| queue: jobs unfinished at the window's end | 12.5 | 12.4 | −0.8% | −3.3422 to +3.1422 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*