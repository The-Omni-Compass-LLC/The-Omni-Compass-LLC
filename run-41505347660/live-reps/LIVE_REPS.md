# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.298 |
| node-hours | 2.514 | 2.221 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 253.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 467 | 454.2 |
| response time (ms), 95th percentile | 2104 | 2272 |
| response time (ms), 99th percentile | 3007 | 3246 |
| time over the response line (% of samples) | 17.64 | 17 |
| failed requests (%) | 0 | 0.0107 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 72.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.4 | 17.94 |
| utilisation (used / allocatable) | 0.06743 | 0.07732 |
| CPU used (cores), mean | 1.618 | 1.624 |
| Omni's own CPU (cores), mean | 0 | 0.07769 |
| CPU used with Omni's own (cores), mean | 1.618 | 1.701 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.7 | 373.5 |
| HPA replicas, mean | 2.039 | 2.374 |
| pods started | 0 | 1.1 |
| pod start wait, total (s) | 0 | 2.3 |
| pod start wait, mean (s) | 0 | 1.05 |
| host CPU busy, the real machine under kind (%) | 46.28 | 49.63 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 840.4 | 855.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.692 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.325 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.6 |
| queue: job turnaround, submitted to done, mean (s) | 149.4 | 163.2 |
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
| worker nodes in service, mean | 6 | 5.298 | −11.7% | −1.3577 to −0.0453 | yes: GAIN |
| node-hours | 2.514 | 2.221 | −11.6% | −0.5683 to −0.0162 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 275.1 | 275.5 | +0.2% | −0.5830 to +1.4472 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.1 | 253.4 | −7.9% | −42.6311 to −0.7130 | yes: GAIN |
| response time (ms), mean | 467 | 454.2 | −2.8% | −34.8625 to +9.1297 | no |
| response time (ms), 95th percentile | 2104 | 2272 | +8.0% | +50.2959 to +286.4211 | yes: LOSS |
| response time (ms), 99th percentile | 3007 | 3246 | +7.9% | +48.7251 to +427.5453 | yes: LOSS |
| time over the response line (% of samples) | 17.64 | 17 | −3.6% | −1.8404 to +0.5528 | no |
| failed requests (%) | 0 | 0.0107 | +0.011 (native is 0) | −0.0135 to +0.0349 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.1 | 10.9 | −1.8% | −1.0121 to +0.6121 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 72.2 | +72.200 (native is 0) | +28.4462 to +115.9538 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.4 | 17.94 | +24.6% | +1.6141 to +5.4825 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06743 | 0.07732 | +14.7% | +0.0011 to +0.0186 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.618 | 1.624 | +0.3% | −0.0187 to +0.0295 | no |
| Omni's own CPU (cores), mean | 0 | 0.07769 | +0.078 (native is 0) | +0.0723 to +0.0831 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.618 | 1.701 | +5.1% | +0.0565 to +0.1097 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 411.7 | 373.5 | −9.3% | −71.0315 to −5.4109 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.039 | 2.374 | +16.4% | +0.1195 to +0.5506 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.1796 to +2.0204 | yes: power given |
| pod start wait, total (s) | 0 | 2.3 | +2.300 (native is 0) | +0.3615 to +4.2385 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.05 | +1.050 (native is 0) | +0.2433 to +1.8567 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 46.28 | 49.63 | +7.2% | +2.9806 to +3.7196 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 840.4 | 855.5 | +1.8% | +7.0181 to +23.1819 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.692 | −21.8% | −2.3982 to −0.2181 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.325 | +188.9% | +0.0196 to +0.4054 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.6 | +77.8% | −0.6924 to +2.0924 | no |
| queue: job turnaround, submitted to done, mean (s) | 149.4 | 163.2 | +9.2% | +5.5903 to +21.9930 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*