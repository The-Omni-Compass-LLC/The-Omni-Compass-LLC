# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.096 |
| node-hours | 2.518 | 2.137 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 244.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 317.2 | 289.1 |
| response time (ms), 95th percentile | 1071 | 1186 |
| response time (ms), 99th percentile | 1525 | 1620 |
| time over the response line (% of samples) | 12.73 | 12.88 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.06 | 9.895 |
| utilisation (used / allocatable) | 0.05961 | 0.07129 |
| CPU used (cores), mean | 1.431 | 1.43 |
| Omni's own CPU (cores), mean | 0 | 0.01589 |
| CPU used with Omni's own (cores), mean | 1.431 | 1.446 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.3 | 409.9 |
| HPA replicas, mean | 2.041 | 2.077 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.9 |
| pod start wait, mean (s) | 0 | 0.9 |
| host CPU busy, the real machine under kind (%) | 40.86 | 41.83 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 774.4 | 776.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.452 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 |
| queue: job turnaround, submitted to done, mean (s) | 79.79 | 82.57 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.096 | −15.1% | −1.6378 to −0.1706 | yes: GAIN |
| node-hours | 2.518 | 2.137 | −15.1% | −0.6850 to −0.0773 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.6 | −0.0% | −0.9363 to +0.8182 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 244.1 | −10.5% | −51.1684 to −5.8247 | yes: GAIN |
| response time (ms), mean | 317.2 | 289.1 | −8.8% | −40.9617 to −15.0963 | yes: GAIN |
| response time (ms), 95th percentile | 1071 | 1186 | +10.8% | −26.0486 to +257.8546 | no |
| response time (ms), 99th percentile | 1525 | 1620 | +6.2% | −31.4857 to +221.8509 | no |
| time over the response line (% of samples) | 12.73 | 12.88 | +1.2% | −0.7251 to +1.0261 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8.1 | +6.6% | −1.0174 to +2.0174 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 46.9 | +46.900 (native is 0) | +25.7249 to +68.0751 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.06 | 9.895 | −1.6% | −1.7920 to +1.4653 | no |
| utilisation (used / allocatable) | 0.05961 | 0.07129 | +19.6% | +0.0018 to +0.0215 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.431 | 1.43 | −0.1% | −0.0242 to +0.0220 | no |
| Omni's own CPU (cores), mean | 0 | 0.01589 | +0.016 (native is 0) | +0.0146 to +0.0172 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.431 | 1.446 | +1.0% | −0.0084 to +0.0380 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.3 | 409.9 | −11.5% | −98.4674 to −8.3366 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.041 | 2.077 | +1.8% | −0.1100 to +0.1827 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | +0.0306 to +0.7694 | yes: power given |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.86 | 41.83 | +2.4% | +0.6563 to +1.2790 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 774.4 | 776.9 | +0.3% | −3.4585 to +8.4585 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.452 | −25.8% | −2.7026 to −0.3933 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05 | 0.0375 | −25.0% | −0.0524 to +0.0274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.3 | −25.0% | −0.5060 to +0.3060 | no |
| queue: job turnaround, submitted to done, mean (s) | 79.79 | 82.57 | +3.5% | −4.1471 to +9.7221 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*