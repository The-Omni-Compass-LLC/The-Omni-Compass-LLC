# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.788 |
| node-hours | 2.514 | 2.006 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 235.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 472.3 | 445.5 |
| response time (ms), 95th percentile | 2597 | 2667 |
| response time (ms), 99th percentile | 3559 | 3637 |
| time over the response line (% of samples) | 17.58 | 17.19 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 10.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 188.6 | 193.6 |
| utilisation (used / allocatable) | 0.06192 | 0.07794 |
| CPU used (cores), mean | 1.486 | 1.487 |
| Omni's own CPU (cores), mean | 0 | 0.0746 |
| CPU used with Omni's own (cores), mean | 1.486 | 1.562 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.7 | 381.8 |
| HPA replicas, mean | 2.175 | 1.994 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 0.5 | 0 |
| pod start wait, mean (s) | 0.5 | 0 |
| host CPU busy, the real machine under kind (%) | 43.17 | 45.59 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 585 | 601.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.12 |
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
| worker nodes in service, mean | 6 | 4.788 | −20.2% | −1.9043 to −0.5198 | yes: GAIN |
| node-hours | 2.514 | 2.006 | −20.2% | −0.7998 to −0.2162 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.3 | 273.4 | +0.1% | −0.7444 to +1.0864 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.3 | 235.3 | −13.9% | −60.0024 to −15.8847 | yes: GAIN |
| response time (ms), mean | 472.3 | 445.5 | −5.7% | −48.4644 to −5.1101 | yes: GAIN |
| response time (ms), 95th percentile | 2597 | 2667 | +2.7% | −58.6180 to +199.8330 | no |
| response time (ms), 99th percentile | 3559 | 3637 | +2.2% | −94.5549 to +249.8223 | no |
| time over the response line (% of samples) | 17.58 | 17.19 | −2.2% | −1.0217 to +0.2585 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.1 | 10.3 | +2.0% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 8.8 | +8.800 (native is 0) | +7.5474 to +10.0526 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 188.6 | 193.6 | +2.6% | +0.9597 to +8.9503 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06192 | 0.07794 | +25.9% | +0.0073 to +0.0247 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 1.487 | +0.1% | −0.0412 to +0.0428 | no |
| Omni's own CPU (cores), mean | 0 | 0.0746 | +0.075 (native is 0) | +0.0645 to +0.0847 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.486 | 1.562 | +5.1% | +0.0282 to +0.1226 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.7 | 381.8 | −15.3% | −107.8351 to −29.9619 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.175 | 1.994 | −8.3% | −0.5475 to +0.1869 | no |
| pods started | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| pod start wait, total (s) | 0.5 | 0 | −100.0% | −1.6310 to +0.6310 | no |
| pod start wait, mean (s) | 0.5 | 0 | −100.0% | −1.6310 to +0.6310 | no |
| host CPU busy, the real machine under kind (%) | 43.17 | 45.59 | +5.6% | +1.7189 to +3.1167 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 585 | 601.1 | +2.8% | +5.8254 to +26.3746 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.12 | −31.3% | −2.9166 to −0.8430 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*