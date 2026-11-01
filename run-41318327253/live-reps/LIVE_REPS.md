# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.996 |
| node-hours | 2.515 | 2.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 129.4 | 97.65 |
| response time (ms), 95th percentile | 228.2 | 216.6 |
| response time (ms), 99th percentile | 332.8 | 331.7 |
| time over the response line (% of samples) | 0.2233 | 0.2914 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1113 | 1074 |
| utilisation (used / allocatable) | 0.05944 | 0.05933 |
| CPU used (cores), mean | 1.427 | 1.423 |
| Omni's own CPU (cores), mean | 0 | 0.01222 |
| CPU used with Omni's own (cores), mean | 1.427 | 1.435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 456 |
| HPA replicas, mean | 1.989 | 1.998 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.6 |
| pod start wait, mean (s) | 0 | 0.45 |
| host CPU busy, the real machine under kind (%) | 44.62 | 44.88 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1418 | 1413 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.938 |
| queue: job wait, submitted to its first pod running, mean (s) | 127.3 | 162.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 633.5 | 715.1 |
| queue: job turnaround, submitted to done, mean (s) | 830.2 | 797.7 |
| queue: jobs unfinished at the window's end | 9.7 | 9.4 |
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
| worker nodes in service, mean | 6 | 5.996 | −0.1% | −0.0141 to +0.0054 | no |
| node-hours | 2.515 | 2.512 | −0.1% | −0.0114 to +0.0042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | −0.1% | −1.1685 to +0.4995 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 271.6 | −0.2% | −1.2885 to +0.3486 | no |
| response time (ms), mean | 129.4 | 97.65 | −24.5% | −37.6591 to −25.7459 | yes: GAIN |
| response time (ms), 95th percentile | 228.2 | 216.6 | −5.1% | −25.4233 to +2.0913 | no |
| response time (ms), 99th percentile | 332.8 | 331.7 | −0.4% | −23.6715 to +21.2865 | no |
| time over the response line (% of samples) | 0.2233 | 0.2914 | +30.5% | −0.0994 to +0.2354 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.9 | +15.900 (native is 0) | +10.1335 to +21.6665 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1113 | 1074 | −3.5% | −84.3730 to +6.1363 | no |
| utilisation (used / allocatable) | 0.05944 | 0.05933 | −0.2% | −0.0012 to +0.0010 | no |
| CPU used (cores), mean | 1.427 | 1.423 | −0.3% | −0.0297 to +0.0222 | no |
| Omni's own CPU (cores), mean | 0 | 0.01222 | +0.012 (native is 0) | +0.0107 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.427 | 1.435 | +0.6% | −0.0175 to +0.0344 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 455.3 | 456 | +0.2% | −7.2560 to +8.6698 | no |
| HPA replicas, mean | 1.989 | 1.998 | +0.5% | −0.0831 to +0.1019 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.6 | +0.600 (native is 0) | −0.1689 to +1.3689 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.0950 to +0.9950 | no |
| host CPU busy, the real machine under kind (%) | 44.62 | 44.88 | +0.6% | −0.5208 to +1.0543 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1418 | 1413 | −0.3% | −15.3603 to +5.7603 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.938 | −1.0% | −0.2614 to +0.1364 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 127.3 | 162.3 | +27.4% | −12.7061 to +82.5561 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 633.5 | 715.1 | +12.9% | −121.7294 to +284.9294 | no |
| queue: job turnaround, submitted to done, mean (s) | 830.2 | 797.7 | −3.9% | −62.0913 to −2.9004 | yes: GAIN |
| queue: jobs unfinished at the window's end | 9.7 | 9.4 | −3.1% | −1.6924 to +1.0924 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*