# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.305 |
| node-hours | 2.517 | 2.226 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 252.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 472.2 | 460.6 |
| response time (ms), 95th percentile | 1774 | 1923 |
| response time (ms), 99th percentile | 2498 | 2718 |
| time over the response line (% of samples) | 21.08 | 21 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 11.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 3.704 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.71 | 16.47 |
| utilisation (used / allocatable) | 0.06565 | 0.07453 |
| CPU used (cores), mean | 1.576 | 1.573 |
| Omni's own CPU (cores), mean | 0 | 0.07631 |
| CPU used with Omni's own (cores), mean | 1.576 | 1.649 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425 | 387.1 |
| HPA replicas, mean | 2.051 | 2.347 |
| pods started | 0.2 | 0.9 |
| pod start wait, total (s) | 0.4 | 1.9 |
| pod start wait, mean (s) | 0.4 | 1.183 |
| host CPU busy, the real machine under kind (%) | 45 | 48.08 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 827.1 | 838.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.737 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 132.2 | 141.3 |
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
| worker nodes in service, mean | 6 | 5.305 | −11.6% | −1.3045 to −0.0856 | yes: GAIN |
| node-hours | 2.517 | 2.226 | −11.6% | −0.5451 to −0.0374 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.7 | 274.8 | +0.0% | −0.6600 to +0.7821 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.7 | 252.9 | −7.9% | −41.0512 to −2.6142 | yes: GAIN |
| response time (ms), mean | 472.2 | 460.6 | −2.5% | −24.9086 to +1.7248 | no |
| response time (ms), 95th percentile | 1774 | 1923 | +8.4% | +27.3593 to +270.2597 | yes: LOSS |
| response time (ms), 99th percentile | 2498 | 2718 | +8.8% | −6.9399 to +446.4387 | no |
| time over the response line (% of samples) | 21.08 | 21 | −0.4% | −0.7893 to +0.6241 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.4 | 11.5 | +10.6% | +0.1198 to +2.0802 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 96.6 | +96.600 (native is 0) | +36.7235 to +156.4765 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.71 | 16.47 | +20.1% | −0.9711 to +6.4811 | no |
| utilisation (used / allocatable) | 0.06565 | 0.07453 | +13.5% | +0.0009 to +0.0169 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.576 | 1.573 | −0.2% | −0.0238 to +0.0184 | no |
| Omni's own CPU (cores), mean | 0 | 0.07631 | +0.076 (native is 0) | +0.0699 to +0.0828 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.576 | 1.649 | +4.7% | +0.0474 to +0.0998 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425 | 387.1 | −8.9% | −70.0034 to −5.7837 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.347 | +14.4% | +0.1217 to +0.4700 | yes: power given |
| pods started | 0.2 | 0.9 | +350.0% | −0.1294 to +1.5294 | no |
| pod start wait, total (s) | 0.4 | 1.9 | +375.0% | −0.5020 to +3.5020 | no |
| pod start wait, mean (s) | 0.4 | 1.183 | +195.8% | −0.3983 to +1.9649 | no |
| host CPU busy, the real machine under kind (%) | 45 | 48.08 | +6.8% | +2.5156 to +3.6465 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 827.1 | 838.5 | +1.4% | +4.7562 to +18.0438 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.737 | −21.0% | −2.2102 to −0.3149 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1125 | 0.375 | +233.3% | −0.0244 to +0.5494 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 2.1 | +320.0% | −0.8825 to +4.0825 | no |
| queue: job turnaround, submitted to done, mean (s) | 132.2 | 141.3 | +6.9% | +2.8061 to +15.4606 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*