# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.888 |
| node-hours | 2.509 | 2.052 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 239 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 375.5 | 357.3 |
| response time (ms), 95th percentile | 1565 | 1634 |
| response time (ms), 99th percentile | 2149 | 2295 |
| time over the response line (% of samples) | 12.92 | 13.07 |
| failed requests (%) | 0.01081 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 27.78 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.29 | 15.4 |
| utilisation (used / allocatable) | 0.06259 | 0.07667 |
| CPU used (cores), mean | 1.502 | 1.485 |
| Omni's own CPU (cores), mean | 0 | 0.06947 |
| CPU used with Omni's own (cores), mean | 1.502 | 1.554 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.6 | 388.4 |
| HPA replicas, mean | 2.12 | 2.178 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 1.4 |
| pod start wait, mean (s) | 0 | 1.1 |
| host CPU busy, the real machine under kind (%) | 42.99 | 45.66 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 810.9 | 817.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.226 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.6083 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.6 |
| queue: job turnaround, submitted to done, mean (s) | 117.7 | 122.9 |
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
| worker nodes in service, mean | 6 | 4.888 | −18.5% | −1.9451 to −0.2785 | yes: GAIN |
| node-hours | 2.509 | 2.052 | −18.2% | −0.8106 to −0.1030 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 274 | +0.4% | −0.0940 to +2.0671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 239 | −12.5% | −60.7718 to −7.2051 | yes: GAIN |
| response time (ms), mean | 375.5 | 357.3 | −4.8% | −34.9691 to −1.4257 | yes: GAIN |
| response time (ms), 95th percentile | 1565 | 1634 | +4.4% | −19.3763 to +157.9783 | no |
| response time (ms), 99th percentile | 2149 | 2295 | +6.8% | −20.2674 to +311.3944 | no |
| time over the response line (% of samples) | 12.92 | 13.07 | +1.2% | −0.6222 to +0.9292 | no |
| failed requests (%) | 0.01081 | 0 | −100.0% | −0.0353 to +0.0136 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.8 | 8.4 | +7.7% | −0.0911 to +1.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 64.2 | +64.200 (native is 0) | +34.4102 to +93.9898 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.29 | 15.4 | +15.8% | −0.5293 to +4.7426 | no |
| utilisation (used / allocatable) | 0.06259 | 0.07667 | +22.5% | +0.0030 to +0.0252 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.502 | 1.485 | −1.2% | −0.0405 to +0.0050 | no |
| Omni's own CPU (cores), mean | 0 | 0.06947 | +0.069 (native is 0) | +0.0615 to +0.0774 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.502 | 1.554 | +3.4% | +0.0228 to +0.0807 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.6 | 388.4 | −14.0% | −115.1873 to −11.3360 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.12 | 2.178 | +2.7% | −0.0770 to +0.1913 | no |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.2358 to +1.3642 | yes: power given |
| pod start wait, total (s) | 0 | 1.4 | +1.400 (native is 0) | +0.4344 to +2.3656 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.1 | +1.100 (native is 0) | +0.3311 to +1.8689 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.99 | 45.66 | +6.2% | +2.3466 to +3.0094 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 810.9 | 817.6 | +0.8% | +0.6675 to +12.7325 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.226 | −29.6% | −3.0045 to −0.5443 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2 | 0.6083 | +204.2% | −0.3278 to +1.1444 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.9 | 2.6 | +188.9% | −0.7093 to +4.1093 | no |
| queue: job turnaround, submitted to done, mean (s) | 117.7 | 122.9 | +4.5% | +0.1130 to +10.4620 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*