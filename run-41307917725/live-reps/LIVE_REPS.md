# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.519 | 2.52 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.2 | 105.2 |
| response time (ms), 95th percentile | 244.5 | 240.3 |
| response time (ms), 99th percentile | 367.7 | 359.1 |
| time over the response line (% of samples) | 0.2381 | 0.2457 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1213 | 1253 |
| utilisation (used / allocatable) | 0.06021 | 0.05971 |
| CPU used (cores), mean | 1.445 | 1.433 |
| Omni's own CPU (cores), mean | 0 | 0.01262 |
| CPU used with Omni's own (cores), mean | 1.445 | 1.446 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 453.2 |
| HPA replicas, mean | 2.082 | 2.006 |
| pods started | 0.3 | 0.1 |
| pod start wait, total (s) | 0.6 | 0.2 |
| pod start wait, mean (s) | 0.6 | 0.2 |
| host CPU busy, the real machine under kind (%) | 45.64 | 45.51 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1462 | 1486 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 164.5 | 190.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 776 | 841.6 |
| queue: job turnaround, submitted to done, mean (s) | 882.3 | 902.3 |
| queue: jobs unfinished at the window's end | 11.9 | 12.9 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.519 | 2.52 | +0.0% | −0.0048 to +0.0062 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 272.6 | −0.1% | −1.0151 to +0.5154 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 272.6 | −0.1% | −1.0151 to +0.5154 | no |
| response time (ms), mean | 138.2 | 105.2 | −23.9% | −39.8676 to −26.1046 | yes: GAIN |
| response time (ms), 95th percentile | 244.5 | 240.3 | −1.7% | −13.7712 to +5.2952 | no |
| response time (ms), 99th percentile | 367.7 | 359.1 | −2.3% | −36.8829 to +19.6611 | no |
| time over the response line (% of samples) | 0.2381 | 0.2457 | +3.2% | −0.1015 to +0.1168 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 16.3 | +16.300 (native is 0) | +11.7130 to +20.8870 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1213 | 1253 | +3.3% | −2.5875 to +83.2509 | no |
| utilisation (used / allocatable) | 0.06021 | 0.05971 | −0.8% | −0.0018 to +0.0009 | no |
| CPU used (cores), mean | 1.445 | 1.433 | −0.8% | −0.0444 to +0.0207 | no |
| Omni's own CPU (cores), mean | 0 | 0.01262 | +0.013 (native is 0) | +0.0113 to +0.0139 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.445 | 1.446 | +0.1% | −0.0321 to +0.0336 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450 | 453.2 | +0.7% | −5.7295 to +12.1594 | no |
| HPA replicas, mean | 2.082 | 2.006 | −3.6% | −0.2682 to +0.1175 | no |
| pods started | 0.3 | 0.1 | −66.7% | −0.6524 to +0.2524 | no |
| pod start wait, total (s) | 0.6 | 0.2 | −66.7% | −1.3656 to +0.5656 | no |
| pod start wait, mean (s) | 0.6 | 0.2 | −66.7% | −1.3656 to +0.5656 | no |
| host CPU busy, the real machine under kind (%) | 45.64 | 45.51 | −0.3% | −0.9088 to +0.6483 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1462 | 1486 | +1.7% | −20.9760 to +69.9760 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 164.5 | 190.5 | +15.8% | −0.9784 to +53.0950 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 776 | 841.6 | +8.5% | −134.0840 to +265.2840 | no |
| queue: job turnaround, submitted to done, mean (s) | 882.3 | 902.3 | +2.3% | −29.3343 to +69.2426 | no |
| queue: jobs unfinished at the window's end | 11.9 | 12.9 | +8.4% | −0.4306 to +2.4306 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*