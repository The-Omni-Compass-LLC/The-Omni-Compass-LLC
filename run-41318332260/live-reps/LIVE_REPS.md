# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.968 |
| node-hours | 2.518 | 2.502 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 128.7 | 97.06 |
| response time (ms), 95th percentile | 223.6 | 213.2 |
| response time (ms), 99th percentile | 333.3 | 326 |
| time over the response line (% of samples) | 0.1987 | 0.1778 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1093 | 1092 |
| utilisation (used / allocatable) | 0.05875 | 0.05928 |
| CPU used (cores), mean | 1.41 | 1.415 |
| Omni's own CPU (cores), mean | 0 | 0.01195 |
| CPU used with Omni's own (cores), mean | 1.41 | 1.427 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.8 | 457.1 |
| HPA replicas, mean | 2.002 | 1.959 |
| pods started | 0.2 | 0 |
| pod start wait, total (s) | 0.4 | 0 |
| pod start wait, mean (s) | 0.4 | 0 |
| host CPU busy, the real machine under kind (%) | 44.09 | 44.32 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1430 | 1420 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 |
| queue: job wait, submitted to its first pod running, mean (s) | 149.7 | 142.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 617.9 | 679.8 |
| queue: job turnaround, submitted to done, mean (s) | 816 | 795 |
| queue: jobs unfinished at the window's end | 11 | 10.2 |
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
| worker nodes in service, mean | 6 | 5.968 | −0.5% | −0.0848 to +0.0206 | no |
| node-hours | 2.518 | 2.502 | −0.6% | −0.0379 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.8 | −0.0% | −1.3086 to +1.1057 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.8 | −0.4% | −3.1749 to +0.9471 | no |
| response time (ms), mean | 128.7 | 97.06 | −24.6% | −37.6158 to −25.7216 | yes: GAIN |
| response time (ms), 95th percentile | 223.6 | 213.2 | −4.7% | −20.9900 to +0.1120 | no |
| response time (ms), 99th percentile | 333.3 | 326 | −2.2% | −29.1957 to +14.6345 | no |
| time over the response line (% of samples) | 0.1987 | 0.1778 | −10.5% | −0.1157 to +0.0739 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 15.8 | +15.800 (native is 0) | +11.0576 to +20.5424 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1093 | 1092 | −0.1% | −49.9748 to +47.1381 | no |
| utilisation (used / allocatable) | 0.05875 | 0.05928 | +0.9% | −0.0008 to +0.0019 | no |
| CPU used (cores), mean | 1.41 | 1.415 | +0.4% | −0.0320 to +0.0430 | no |
| Omni's own CPU (cores), mean | 0 | 0.01195 | +0.012 (native is 0) | +0.0109 to +0.0130 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.41 | 1.427 | +1.2% | −0.0204 to +0.0552 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.8 | 457.1 | −0.6% | −12.1666 to +6.7472 | no |
| HPA replicas, mean | 2.002 | 1.959 | −2.1% | −0.1968 to +0.1114 | no |
| pods started | 0.2 | 0 | −100.0% | −0.5016 to +0.1016 | no |
| pod start wait, total (s) | 0.4 | 0 | −100.0% | −1.0032 to +0.2032 | no |
| pod start wait, mean (s) | 0.4 | 0 | −100.0% | −1.0032 to +0.2032 | no |
| host CPU busy, the real machine under kind (%) | 44.09 | 44.32 | +0.5% | −0.7113 to +1.1668 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1430 | 1420 | −0.7% | −28.8213 to +7.4213 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.5 | −8.3% | −1.5757 to +0.5757 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 149.7 | 142.8 | −4.6% | −44.5394 to +30.6644 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 617.9 | 679.8 | +10.0% | −107.0736 to +230.8736 | no |
| queue: job turnaround, submitted to done, mean (s) | 816 | 795 | −2.6% | −60.8725 to +18.6892 | no |
| queue: jobs unfinished at the window's end | 11 | 10.2 | −7.3% | −2.7015 to +1.1015 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*