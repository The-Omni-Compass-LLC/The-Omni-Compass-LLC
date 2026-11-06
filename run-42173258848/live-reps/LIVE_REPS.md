# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.973 |
| node-hours | 2.511 | 2.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 124.2 | 106.1 |
| response time (ms), 95th percentile | 209.9 | 226.6 |
| response time (ms), 99th percentile | 302.8 | 339.3 |
| time over the response line (% of samples) | 0.092 | 0.1204 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 990.3 | 1110 |
| utilisation (used / allocatable) | 0.06023 | 0.0584 |
| CPU used (cores), mean | 1.446 | 1.396 |
| Omni's own CPU (cores), mean | 0 | 0.06494 |
| CPU used with Omni's own (cores), mean | 1.446 | 1.461 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.2 | 462.9 |
| HPA replicas, mean | 1.988 | 2.087 |
| pods started | 0 | 0.3 |
| pod start wait, total (s) | 0 | 0.8 |
| pod start wait, mean (s) | 0 | 0.45 |
| host CPU busy, the real machine under kind (%) | 44.59 | 45.8 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1442 | 1475 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.342 |
| queue: job wait, submitted to its first pod running, mean (s) | 118 | 171.7 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 569.3 | 734.6 |
| queue: job turnaround, submitted to done, mean (s) | 766.7 | 805.1 |
| queue: jobs unfinished at the window's end | 6.8 | 8.1 |
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
| worker nodes in service, mean | 6 | 5.973 | −0.5% | −0.0882 to +0.0341 | no |
| node-hours | 2.511 | 2.503 | −0.3% | −0.0319 to +0.0168 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 271.4 | −0.2% | −1.6103 to +0.6301 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 270.5 | −0.5% | −3.2548 to +0.5663 | no |
| response time (ms), mean | 124.2 | 106.1 | −14.6% | −26.5745 to −9.6113 | yes: GAIN |
| response time (ms), 95th percentile | 209.9 | 226.6 | +8.0% | +7.9268 to +25.4642 | yes: LOSS |
| response time (ms), 99th percentile | 302.8 | 339.3 | +12.0% | +11.9908 to +60.9694 | yes: LOSS |
| time over the response line (% of samples) | 0.092 | 0.1204 | +30.8% | −0.0551 to +0.1118 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 104 | +104.000 (native is 0) | +89.0944 to +118.9056 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 990.3 | 1110 | +12.0% | +77.7700 to +160.7566 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06023 | 0.0584 | −3.0% | −0.0035 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.446 | 1.396 | −3.5% | −0.0853 to −0.0148 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06494 | +0.065 (native is 0) | +0.0577 to +0.0721 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.461 | +1.0% | −0.0210 to +0.0509 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.2 | 462.9 | +2.8% | +1.5671 to +23.8573 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.988 | 2.087 | +5.0% | −0.0812 to +0.2807 | no |
| pods started | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| pod start wait, total (s) | 0 | 0.8 | +0.800 (native is 0) | −0.7744 to +2.3744 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.3488 to +1.2488 | no |
| host CPU busy, the real machine under kind (%) | 44.59 | 45.8 | +2.7% | +0.4916 to +1.9311 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1442 | 1475 | +2.2% | −21.9458 to +86.7458 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.342 | −11.0% | −9.0171 to +7.7013 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 118 | 171.7 | +45.4% | +17.6186 to +89.6314 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 569.3 | 734.6 | +29.0% | −16.0927 to +346.6927 | no |
| queue: job turnaround, submitted to done, mean (s) | 766.7 | 805.2 | +5.0% | +3.7732 to +73.0685 | yes: LOSS |
| queue: jobs unfinished at the window's end | 6.8 | 8.1 | +19.1% | −0.5174 to +3.1174 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*