# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.282 |
| node-hours | 2.512 | 1.794 |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 218.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 333.8 | 330.8 |
| response time (ms), 95th percentile | 1223 | 1406 |
| response time (ms), 99th percentile | 1753 | 1900 |
| time over the response line (% of samples) | 13.66 | 13.39 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 6.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 167.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 50 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.45 | 12.8 |
| utilisation (used / allocatable) | 0.05944 | 0.08503 |
| CPU used (cores), mean | 1.427 | 1.41 |
| Omni's own CPU (cores), mean | 0 | 0.06614 |
| CPU used with Omni's own (cores), mean | 1.427 | 1.476 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 369.9 |
| HPA replicas, mean | 1.9 | 2.284 |
| pods started | 0 | 1.8 |
| pod start wait, total (s) | 0 | 4 |
| pod start wait, mean (s) | 0 | 1.573 |
| host CPU busy, the real machine under kind (%) | 40.07 | 42.98 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 792.1 | 799.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.65 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 0.2083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.3 |
| queue: job turnaround, submitted to done, mean (s) | 97.71 | 105.6 |
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
| worker nodes in service, mean | 6 | 4.282 | −28.6% | −2.7778 to −0.6584 | yes: GAIN |
| node-hours | 2.512 | 1.794 | −28.6% | −1.1609 to −0.2759 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272 | 272.3 | +0.1% | −0.5639 to +1.0853 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272 | 218.2 | −19.8% | −87.1684 to −20.3935 | yes: GAIN |
| response time (ms), mean | 333.8 | 330.8 | −0.9% | −14.8785 to +8.9315 | no |
| response time (ms), 95th percentile | 1223 | 1406 | +15.0% | +56.3199 to +311.2501 | yes: LOSS |
| response time (ms), 99th percentile | 1753 | 1900 | +8.4% | +10.6902 to +282.7354 | yes: LOSS |
| time over the response line (% of samples) | 13.66 | 13.39 | −1.9% | −0.9015 to +0.3693 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.2 | 6.3 | +1.6% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 167.6 | +167.600 (native is 0) | +75.8272 to +259.3728 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.45 | 12.8 | +11.8% | −0.9934 to +3.7034 | no |
| utilisation (used / allocatable) | 0.05944 | 0.08503 | +43.0% | +0.0105 to +0.0406 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.427 | 1.41 | −1.2% | −0.0551 to +0.0211 | no |
| Omni's own CPU (cores), mean | 0 | 0.06614 | +0.066 (native is 0) | +0.0580 to +0.0742 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.427 | 1.476 | +3.4% | +0.0040 to +0.0942 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 470.7 | 369.9 | −21.4% | −159.8037 to −41.7834 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.9 | 2.284 | +20.2% | +0.1311 to +0.6373 | yes: power given |
| pods started | 0 | 1.8 | +1.800 (native is 0) | +0.5936 to +3.0064 | yes: power given |
| pod start wait, total (s) | 0 | 4 | +4.000 (native is 0) | +1.3024 to +6.6976 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.573 | +1.573 (native is 0) | +0.6538 to +2.4929 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 40.07 | 42.98 | +7.3% | +2.3410 to +3.4905 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 792.1 | 799.1 | +0.9% | +0.5314 to +13.4686 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.65 | −39.2% | −3.8008 to −0.8992 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1667 | 0.2083 | +25.0% | −0.0286 to +0.1119 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 1.3 | +44.4% | −0.3689 to +1.1689 | no |
| queue: job turnaround, submitted to done, mean (s) | 97.71 | 105.6 | +8.1% | +0.8414 to +15.0002 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*