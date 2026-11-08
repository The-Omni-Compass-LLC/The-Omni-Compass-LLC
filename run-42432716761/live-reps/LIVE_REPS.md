# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.658 |
| node-hours | 2.513 | 1.953 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 231.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 418.6 | 404.6 |
| response time (ms), 95th percentile | 1575 | 1669 |
| response time (ms), 99th percentile | 2270 | 2386 |
| time over the response line (% of samples) | 17.66 | 17.55 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 28.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.25 | 13.95 |
| utilisation (used / allocatable) | 0.06143 | 0.08082 |
| CPU used (cores), mean | 1.474 | 1.484 |
| Omni's own CPU (cores), mean | 0 | 0.07635 |
| CPU used with Omni's own (cores), mean | 1.474 | 1.56 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.6 | 373.8 |
| HPA replicas, mean | 2.071 | 2.294 |
| pods started | 0.1 | 0.9 |
| pod start wait, total (s) | 0.3 | 2 |
| pod start wait, mean (s) | 0.3 | 1.15 |
| host CPU busy, the real machine under kind (%) | 42.81 | 46.19 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 812.4 | 819.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.802 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 0.5583 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.8 |
| queue: job turnaround, submitted to done, mean (s) | 117 | 124.4 |
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
| worker nodes in service, mean | 6 | 4.658 | −22.4% | −2.1686 to −0.5149 | yes: GAIN |
| node-hours | 2.513 | 1.953 | −22.3% | −0.9055 to −0.2136 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 273.3 | +0.2% | −0.4029 to +1.5912 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 231.1 | −15.3% | −67.5298 to −15.7360 | yes: GAIN |
| response time (ms), mean | 418.6 | 404.6 | −3.3% | −28.1410 to +0.1034 | no |
| response time (ms), 95th percentile | 1575 | 1669 | +6.0% | −18.1249 to +205.9369 | no |
| response time (ms), 99th percentile | 2270 | 2386 | +5.1% | −56.5073 to +288.8785 | no |
| time over the response line (% of samples) | 17.66 | 17.55 | −0.6% | −0.6520 to +0.4395 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.3 | +4.5% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 118.5 | +118.500 (native is 0) | +45.6016 to +191.3984 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.25 | 13.95 | +13.9% | −0.4872 to +3.8839 | no |
| utilisation (used / allocatable) | 0.06143 | 0.08082 | +31.6% | +0.0071 to +0.0317 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.474 | 1.484 | +0.7% | −0.0286 to +0.0477 | no |
| Omni's own CPU (cores), mean | 0 | 0.07635 | +0.076 (native is 0) | +0.0690 to +0.0837 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.474 | 1.56 | +5.8% | +0.0453 to +0.1265 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.6 | 373.8 | −18.7% | −146.6633 to −25.0388 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.071 | 2.294 | +10.8% | +0.0193 to +0.4271 | yes: power given |
| pods started | 0.1 | 0.9 | +800.0% | +0.0612 to +1.5388 | yes: power given |
| pod start wait, total (s) | 0.3 | 2 | +566.7% | +0.1901 to +3.2099 | yes: LOSS |
| pod start wait, mean (s) | 0.3 | 1.15 | +283.3% | −0.0429 to +1.7429 | no |
| host CPU busy, the real machine under kind (%) | 42.81 | 46.19 | +7.9% | +2.9155 to +3.8416 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.4 | 819.6 | +0.9% | +0.8664 to +13.5336 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.802 | −36.6% | −3.2970 to −1.0992 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.35 | 0.5583 | +59.5% | −0.0047 to +0.4214 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 1.8 | +20.0% | −0.8209 to +1.4209 | no |
| queue: job turnaround, submitted to done, mean (s) | 117 | 124.4 | +6.3% | +1.0634 to +13.6949 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*