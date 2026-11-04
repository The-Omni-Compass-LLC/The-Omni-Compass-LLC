# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.917 |
| node-hours | 2.518 | 2.06 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 240.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 403.6 | 409.4 |
| response time (ms), 95th percentile | 1674 | 1920 |
| response time (ms), 99th percentile | 2648 | 2786 |
| time over the response line (% of samples) | 15.76 | 16.22 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.46 | 25.43 |
| utilisation (used / allocatable) | 0.06557 | 0.08045 |
| CPU used (cores), mean | 1.574 | 1.558 |
| Omni's own CPU (cores), mean | 0 | 0.08088 |
| CPU used with Omni's own (cores), mean | 1.574 | 1.639 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.4 | 369.9 |
| HPA replicas, mean | 2.051 | 2.151 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.9 |
| pod start wait, mean (s) | 0 | 0.45 |
| host CPU busy, the real machine under kind (%) | 45.88 | 49.17 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 845.6 | 856.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.198 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9583 | 1.046 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.6 | 3.5 |
| queue: job turnaround, submitted to done, mean (s) | 157 | 166.6 |
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
| worker nodes in service, mean | 6 | 4.917 | −18.1% | −1.9615 to −0.2053 | yes: GAIN |
| node-hours | 2.518 | 2.06 | −18.2% | −0.8249 to −0.0911 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.3 | −0.2% | −1.3174 to +0.3651 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 240.2 | −12.6% | −62.2595 to −6.8178 | yes: GAIN |
| response time (ms), mean | 403.6 | 409.4 | +1.4% | −34.9567 to +46.5807 | no |
| response time (ms), 95th percentile | 1674 | 1920 | +14.6% | −39.0597 to +529.5047 | no |
| response time (ms), 99th percentile | 2648 | 2786 | +5.2% | +7.8132 to +268.3156 | yes: LOSS |
| time over the response line (% of samples) | 15.76 | 16.22 | +2.9% | −1.4427 to +2.3623 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.3 | 9.2 | −1.1% | −0.7263 to +0.5263 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.7 | +105.700 (native is 0) | +39.6511 to +171.7489 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 21.46 | 25.43 | +18.5% | −0.0560 to +8.0060 | no |
| utilisation (used / allocatable) | 0.06557 | 0.08045 | +22.7% | +0.0028 to +0.0270 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.574 | 1.558 | −1.0% | −0.0424 to +0.0120 | no |
| Omni's own CPU (cores), mean | 0 | 0.08088 | +0.081 (native is 0) | +0.0738 to +0.0879 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.574 | 1.639 | +4.2% | +0.0332 to +0.0982 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 428.4 | 369.9 | −13.6% | −106.6513 to −10.2998 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.151 | +4.9% | −0.1358 to +0.3362 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.2032 to +1.0032 | no |
| pod start wait, total (s) | 0 | 0.9 | +0.900 (native is 0) | −0.4676 to +2.2676 | no |
| pod start wait, mean (s) | 0 | 0.45 | +0.450 (native is 0) | −0.2338 to +1.1338 | no |
| host CPU busy, the real machine under kind (%) | 45.88 | 49.17 | +7.2% | +2.7362 to +3.8479 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 845.6 | 856.5 | +1.3% | +3.5166 to +18.2834 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.198 | −30.0% | −3.1010 to −0.5032 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.9583 | 1.046 | +9.1% | −0.1211 to +0.2961 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.6 | 3.5 | +34.6% | −0.6977 to +2.4977 | no |
| queue: job turnaround, submitted to done, mean (s) | 157 | 166.6 | +6.1% | +2.8421 to +16.4163 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*