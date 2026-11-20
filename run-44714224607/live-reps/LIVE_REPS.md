# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.52 | 2.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 272.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 130.9 | 134.5 |
| response time (ms), 95th percentile | 225.9 | 244.4 |
| response time (ms), 99th percentile | 326.2 | 352.5 |
| time over the response line (% of samples) | 0.1148 | 0.2392 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1126 | 1189 |
| utilisation (used / allocatable) | 0.05991 | 0.05821 |
| CPU used (cores), mean | 1.438 | 1.397 |
| Omni's own CPU (cores), mean | 0 | 0.0669 |
| CPU used with Omni's own (cores), mean | 1.438 | 1.464 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 463.9 |
| HPA replicas, mean | 2.051 | 2.2 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 1.9 |
| pod start wait, mean (s) | 0 | 0.7583 |
| host CPU busy, the real machine under kind (%) | 45.37 | 46.57 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1485 | 1491 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 167.2 | 155.8 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 693 | 705.9 |
| queue: job turnaround, submitted to done, mean (s) | 844.8 | 861.9 |
| queue: jobs unfinished at the window's end | 9.9 | 10.8 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.52 | 2.52 | +0.0% | −0.0089 to +0.0103 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 272.2 | −0.2% | −1.6159 to +0.5270 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 272.2 | −0.2% | −1.6159 to +0.5270 | no |
| response time (ms), mean | 130.9 | 134.5 | +2.8% | +0.6498 to +6.5838 | yes: LOSS |
| response time (ms), 95th percentile | 225.9 | 244.4 | +8.2% | +6.6829 to +30.4201 | yes: LOSS |
| response time (ms), 99th percentile | 326.2 | 352.5 | +8.0% | +6.8811 to +45.5889 | yes: LOSS |
| time over the response line (% of samples) | 0.1148 | 0.2392 | +108.4% | −0.0264 to +0.2754 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.3 | +30.300 (native is 0) | +14.1318 to +46.4682 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1126 | 1189 | +5.7% | +0.4599 to +127.2567 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05991 | 0.05821 | −2.8% | −0.0024 to −0.0010 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.438 | 1.397 | −2.8% | −0.0565 to −0.0251 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0669 | +0.067 (native is 0) | +0.0608 to +0.0730 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.438 | 1.464 | +1.8% | +0.0145 to +0.0376 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.8 | 463.9 | +2.7% | +7.5352 to +16.6044 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.2 | +7.3% | −0.0311 to +0.3298 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | −0.2556 to +1.8556 | no |
| pod start wait, total (s) | 0 | 1.9 | +1.900 (native is 0) | −0.5187 to +4.3187 | no |
| pod start wait, mean (s) | 0 | 0.7583 | +0.758 (native is 0) | −0.1260 to +1.6427 | no |
| host CPU busy, the real machine under kind (%) | 45.37 | 46.57 | +2.6% | +0.9018 to +1.4905 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1485 | 1491 | +0.4% | −8.6098 to +19.4098 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 167.2 | 155.8 | −6.8% | −42.3689 to +19.5856 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 693 | 705.9 | +1.9% | −106.3982 to +132.1982 | no |
| queue: job turnaround, submitted to done, mean (s) | 844.8 | 861.9 | +2.0% | −34.7380 to +68.9296 | no |
| queue: jobs unfinished at the window's end | 9.9 | 10.8 | +9.1% | −1.0502 to +2.8502 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*