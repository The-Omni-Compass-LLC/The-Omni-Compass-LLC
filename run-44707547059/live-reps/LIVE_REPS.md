# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.596 |
| node-hours | 2.513 | 1.925 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 228.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 342.5 | 322.2 |
| response time (ms), 95th percentile | 1446 | 1492 |
| response time (ms), 99th percentile | 1983 | 2032 |
| time over the response line (% of samples) | 10.56 | 10.32 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 49.05 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.07 | 14.18 |
| utilisation (used / allocatable) | 0.06114 | 0.08159 |
| CPU used (cores), mean | 1.467 | 1.467 |
| Omni's own CPU (cores), mean | 0 | 0.07573 |
| CPU used with Omni's own (cores), mean | 1.467 | 1.543 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.1 | 372.8 |
| HPA replicas, mean | 2.021 | 2.29 |
| pods started | 0.3 | 1.6 |
| pod start wait, total (s) | 0.5 | 2.7 |
| pod start wait, mean (s) | 0.35 | 0.83 |
| host CPU busy, the real machine under kind (%) | 42.42 | 45.84 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 794.1 | 803.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.82 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.2708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 |
| queue: job turnaround, submitted to done, mean (s) | 100.7 | 108.7 |
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
| worker nodes in service, mean | 6 | 4.596 | −23.4% | −2.2790 to −0.5287 | yes: GAIN |
| node-hours | 2.513 | 1.925 | −23.4% | −0.9529 to −0.2240 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.8 | 273 | +0.1% | −0.4006 to +0.6906 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.8 | 228.9 | −16.1% | −71.2462 to −16.6513 | yes: GAIN |
| response time (ms), mean | 342.5 | 322.2 | −5.9% | −44.0750 to +3.5745 | no |
| response time (ms), 95th percentile | 1446 | 1492 | +3.2% | −94.3801 to +186.8991 | no |
| response time (ms), 99th percentile | 1983 | 2032 | +2.5% | −44.0211 to +142.3229 | no |
| time over the response line (% of samples) | 10.56 | 10.32 | −2.2% | −1.0762 to +0.6098 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 7.4 | +12.1% | +0.1427 to +1.4573 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 108.7 | +108.700 (native is 0) | +58.5706 to +158.8294 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.07 | 14.18 | +17.5% | −0.9717 to +5.1917 | no |
| utilisation (used / allocatable) | 0.06114 | 0.08159 | +33.4% | +0.0075 to +0.0334 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.467 | 1.467 | −0.0% | −0.0359 to +0.0356 | no |
| Omni's own CPU (cores), mean | 0 | 0.07573 | +0.076 (native is 0) | +0.0698 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.467 | 1.543 | +5.2% | +0.0372 to +0.1140 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 454.1 | 372.8 | −17.9% | −131.5563 to −31.0656 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.021 | 2.29 | +13.3% | −0.0467 to +0.5847 | no |
| pods started | 0.3 | 1.6 | +433.3% | −0.0924 to +2.6924 | no |
| pod start wait, total (s) | 0.5 | 2.7 | +440.0% | −0.2502 to +4.6502 | no |
| pod start wait, mean (s) | 0.35 | 0.83 | +137.1% | −0.3608 to +1.3208 | no |
| host CPU busy, the real machine under kind (%) | 42.42 | 45.84 | +8.1% | +2.8690 to +3.9753 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 794.1 | 803.7 | +1.2% | −0.7119 to +19.9119 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.82 | −36.3% | −3.4799 to −0.8801 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1083 | 0.2708 | +150.0% | −0.0278 to +0.3528 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 1.4 | +250.0% | −0.3488 to +2.3488 | no |
| queue: job turnaround, submitted to done, mean (s) | 100.7 | 108.7 | +7.9% | −0.4385 to +16.4468 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*