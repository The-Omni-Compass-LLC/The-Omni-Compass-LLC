# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.995 |
| node-hours | 2.517 | 2.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 128.7 | 130.4 |
| response time (ms), 95th percentile | 225 | 227.8 |
| response time (ms), 99th percentile | 326.8 | 329.1 |
| time over the response line (% of samples) | 0.1389 | 0.1774 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1040 | 1124 |
| utilisation (used / allocatable) | 0.05917 | 0.05824 |
| CPU used (cores), mean | 1.42 | 1.397 |
| Omni's own CPU (cores), mean | 0 | 0.06463 |
| CPU used with Omni's own (cores), mean | 1.42 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.2 | 463.9 |
| HPA replicas, mean | 2.008 | 2.138 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.2 | 1.6 |
| pod start wait, mean (s) | 0.2 | 0.5 |
| host CPU busy, the real machine under kind (%) | 44.21 | 46.05 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1445 | 1487 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.688 |
| queue: job wait, submitted to its first pod running, mean (s) | 135.3 | 177 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 664.7 | 713.3 |
| queue: job turnaround, submitted to done, mean (s) | 784.9 | 827.3 |
| queue: jobs unfinished at the window's end | 8.5 | 9.2 |
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
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0172 to +0.0067 | no |
| node-hours | 2.517 | 2.519 | +0.1% | −0.0068 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.1 | +0.0% | −0.5884 to +0.8118 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 272 | −0.0% | −0.7924 to +0.6824 | no |
| response time (ms), mean | 128.7 | 130.4 | +1.3% | −1.6911 to +5.1369 | no |
| response time (ms), 95th percentile | 225 | 227.8 | +1.2% | −9.8619 to +15.4089 | no |
| response time (ms), 99th percentile | 326.8 | 329.1 | +0.7% | −24.3143 to +28.8503 | no |
| time over the response line (% of samples) | 0.1389 | 0.1774 | +27.7% | −0.0522 to +0.1292 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41.9 | +41.900 (native is 0) | +12.4603 to +71.3397 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1040 | 1124 | +8.0% | +18.2182 to +149.1251 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05917 | 0.05824 | −1.6% | −0.0020 to +0.0001 | no |
| CPU used (cores), mean | 1.42 | 1.397 | −1.6% | −0.0483 to +0.0016 | no |
| Omni's own CPU (cores), mean | 0 | 0.06463 | +0.065 (native is 0) | +0.0582 to +0.0710 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.42 | 1.461 | +2.9% | +0.0158 to +0.0668 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 457.2 | 463.9 | +1.5% | −0.6585 to +14.0359 | no |
| HPA replicas, mean | 2.008 | 2.138 | +6.4% | −0.0755 to +0.3342 | no |
| pods started | 0.1 | 0.6 | +500.0% | −0.5256 to +1.5256 | no |
| pod start wait, total (s) | 0.2 | 1.6 | +700.0% | −1.4652 to +4.2652 | no |
| pod start wait, mean (s) | 0.2 | 0.5 | +150.0% | −0.6567 to +1.2567 | no |
| host CPU busy, the real machine under kind (%) | 44.21 | 46.05 | +4.2% | +1.3590 to +2.3195 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1445 | 1487 | +2.9% | −12.9201 to +96.3201 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.688 | −5.2% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 135.3 | 177 | +30.8% | +11.4625 to +71.8292 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 664.7 | 713.3 | +7.3% | −100.4207 to +197.6207 | no |
| queue: job turnaround, submitted to done, mean (s) | 784.9 | 827.3 | +5.4% | −11.2899 to +96.0983 | no |
| queue: jobs unfinished at the window's end | 8.5 | 9.2 | +8.2% | −0.9189 to +2.3189 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*