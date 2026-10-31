# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.7 |
| node-hours | 2.518 | 1.968 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 231 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 314.9 | 270.7 |
| response time (ms), 95th percentile | 1354 | 1291 |
| response time (ms), 99th percentile | 1875 | 1836 |
| time over the response line (% of samples) | 10.08 | 9.585 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.6 | 10.78 |
| utilisation (used / allocatable) | 0.05796 | 0.07436 |
| CPU used (cores), mean | 1.391 | 1.391 |
| Omni's own CPU (cores), mean | 0 | 0.01643 |
| CPU used with Omni's own (cores), mean | 1.391 | 1.407 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 401.3 |
| HPA replicas, mean | 1.946 | 2.013 |
| pods started | 0.2 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.5 |
| pod start wait, mean (s) | 0.4 | 0.3 |
| host CPU busy, the real machine under kind (%) | 40.09 | 40.97 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 786.9 | 790.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.768 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1125 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 93.54 | 97.08 |
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
| worker nodes in service, mean | 6 | 4.7 | −21.7% | −2.0866 to −0.5140 | yes: GAIN |
| node-hours | 2.518 | 1.968 | −21.8% | −0.8817 to −0.2172 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.1 | 271.7 | −0.1% | −1.3961 to +0.6376 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.1 | 231 | −15.1% | −66.2887 to −16.0364 | yes: GAIN |
| response time (ms), mean | 314.9 | 270.7 | −14.0% | −64.8826 to −23.4053 | yes: GAIN |
| response time (ms), 95th percentile | 1354 | 1291 | −4.6% | −185.8991 to +60.3751 | no |
| response time (ms), 99th percentile | 1875 | 1836 | −2.1% | −179.7750 to +101.8828 | no |
| time over the response line (% of samples) | 10.08 | 9.585 | −4.9% | −1.6589 to +0.6704 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 38.5 | +38.500 (native is 0) | +26.1876 to +50.8124 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.6 | 10.78 | +1.7% | −2.4076 to +2.7643 | no |
| utilisation (used / allocatable) | 0.05796 | 0.07436 | +28.3% | +0.0068 to +0.0260 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.391 | 1.391 | −0.0% | −0.0299 to +0.0294 | no |
| Omni's own CPU (cores), mean | 0 | 0.01643 | +0.016 (native is 0) | +0.0151 to +0.0178 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.391 | 1.407 | +1.2% | −0.0141 to +0.0465 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 482.4 | 401.3 | −16.8% | −127.9006 to −34.2335 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.946 | 2.013 | +3.5% | −0.0688 to +0.2036 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.5263 to +0.7263 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −1.0898 to +1.2898 | no |
| pod start wait, mean (s) | 0.4 | 0.3 | −25.0% | −0.9564 to +0.7564 | no |
| host CPU busy, the real machine under kind (%) | 40.09 | 40.97 | +2.2% | +0.5702 to +1.2012 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 786.9 | 790.2 | +0.4% | −2.3025 to +8.9025 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.768 | −37.2% | −3.4931 to −0.9701 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.05417 | 0.1125 | +107.7% | −0.0262 to +0.1429 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.3 | 0.4 | +33.3% | −0.3060 to +0.5060 | no |
| queue: job turnaround, submitted to done, mean (s) | 93.54 | 97.08 | +3.8% | −1.5577 to +8.6327 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*