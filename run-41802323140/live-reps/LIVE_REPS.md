# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.135 |
| node-hours | 2.515 | 2.148 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 247.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 456.3 | 436.3 |
| response time (ms), 95th percentile | 2037 | 2274 |
| response time (ms), 99th percentile | 2956 | 3259 |
| time over the response line (% of samples) | 18.41 | 17.62 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.08 | 15.73 |
| utilisation (used / allocatable) | 0.06584 | 0.07964 |
| CPU used (cores), mean | 1.58 | 1.6 |
| Omni's own CPU (cores), mean | 0 | 0.07521 |
| CPU used with Omni's own (cores), mean | 1.58 | 1.675 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.3 | 369.7 |
| HPA replicas, mean | 1.957 | 2.452 |
| pods started | 0 | 1.8 |
| pod start wait, total (s) | 0 | 3.1 |
| pod start wait, mean (s) | 0 | 1.4 |
| host CPU busy, the real machine under kind (%) | 45.09 | 48.41 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 832.9 | 846.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.543 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.1333 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 |
| queue: job turnaround, submitted to done, mean (s) | 142.6 | 155.2 |
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
| worker nodes in service, mean | 6 | 5.135 | −14.4% | −1.7046 to −0.0254 | yes: GAIN |
| node-hours | 2.515 | 2.148 | −14.6% | −0.7168 to −0.0189 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.8 | 274.4 | −0.1% | −1.1276 to +0.4719 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.8 | 247.3 | −10.0% | −53.4471 to −1.4544 | yes: GAIN |
| response time (ms), mean | 456.3 | 436.3 | −4.4% | −45.6002 to +5.4898 | no |
| response time (ms), 95th percentile | 2037 | 2274 | +11.6% | +52.3464 to +421.5956 | yes: LOSS |
| response time (ms), 99th percentile | 2956 | 3259 | +10.3% | +89.1515 to +517.4671 | yes: LOSS |
| time over the response line (% of samples) | 18.41 | 17.62 | −4.3% | −2.4496 to +0.8758 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 11.9 | +1.7% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.8 | +81.800 (native is 0) | +27.4149 to +136.1851 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.08 | 15.73 | +11.7% | −1.1332 to +4.4332 | no |
| utilisation (used / allocatable) | 0.06584 | 0.07964 | +21.0% | +0.0008 to +0.0269 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.58 | 1.6 | +1.3% | +0.0024 to +0.0376 | yes, up (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07521 | +0.075 (native is 0) | +0.0665 to +0.0840 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.58 | 1.675 | +6.0% | +0.0728 to +0.1176 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 425.3 | 369.7 | −13.1% | −110.1554 to −0.9921 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.957 | 2.452 | +25.3% | +0.1964 to +0.7929 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.7997 to +2.8003 | yes: power given |
| pod start wait, total (s) | 0 | 3.1 | +3.100 (native is 0) | +1.1208 to +5.0792 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.4 | +1.400 (native is 0) | +0.6999 to +2.1001 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.09 | 48.41 | +7.4% | +2.6361 to +4.0001 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.9 | 846.1 | +1.6% | +4.5846 to +21.8154 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.543 | −24.3% | −2.6672 to −0.2472 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.1333 | +77.8% | −0.0432 to +0.1598 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.8 | +60.0% | −0.5294 to +1.1294 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.6 | 155.2 | +8.8% | +3.9297 to +21.2537 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*