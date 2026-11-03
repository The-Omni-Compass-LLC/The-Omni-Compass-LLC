# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.689 |
| node-hours | 2.514 | 1.962 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 231.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 383.7 | 377.8 |
| response time (ms), 95th percentile | 1575 | 1766 |
| response time (ms), 99th percentile | 2196 | 2398 |
| time over the response line (% of samples) | 12.76 | 12.66 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.6 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.34 | 31.1 |
| utilisation (used / allocatable) | 0.06017 | 0.07822 |
| CPU used (cores), mean | 1.444 | 1.449 |
| Omni's own CPU (cores), mean | 0 | 0.07633 |
| CPU used with Omni's own (cores), mean | 1.444 | 1.525 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466 | 385.5 |
| HPA replicas, mean | 2.003 | 2.246 |
| pods started | 0.1 | 0.6 |
| pod start wait, total (s) | 0.2 | 1 |
| pod start wait, mean (s) | 0.2 | 0.6 |
| host CPU busy, the real machine under kind (%) | 43.38 | 46.89 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 822 | 836.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.781 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8833 | 1.158 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3.5 |
| queue: job turnaround, submitted to done, mean (s) | 124.2 | 135.6 |
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
| worker nodes in service, mean | 6 | 4.689 | −21.9% | −2.1298 to −0.4931 | yes: GAIN |
| node-hours | 2.514 | 1.962 | −21.9% | −0.8929 to −0.2100 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.4 | −0.1% | −1.0473 to +0.6406 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 231.2 | −15.2% | −67.1473 to −15.6052 | yes: GAIN |
| response time (ms), mean | 383.7 | 377.8 | −1.5% | −25.2647 to +13.5641 | no |
| response time (ms), 95th percentile | 1575 | 1766 | +12.1% | −7.6378 to +389.3168 | no |
| response time (ms), 99th percentile | 2196 | 2398 | +9.2% | +22.8715 to +380.7819 | yes: LOSS |
| time over the response line (% of samples) | 12.76 | 12.66 | −0.8% | −0.8970 to +0.6850 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.3 | 8.6 | +3.6% | −0.0455 to +0.6455 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.1 | +105.100 (native is 0) | +52.3475 to +157.8525 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 24.34 | 31.1 | +27.8% | −2.0054 to +15.5154 | no |
| utilisation (used / allocatable) | 0.06017 | 0.07822 | +30.0% | +0.0070 to +0.0291 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.444 | 1.449 | +0.3% | −0.0201 to +0.0288 | no |
| Omni's own CPU (cores), mean | 0 | 0.07633 | +0.076 (native is 0) | +0.0662 to +0.0864 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.444 | 1.525 | +5.6% | +0.0472 to +0.1142 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 466 | 385.5 | −17.3% | −131.9366 to −29.0662 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.246 | +12.1% | −0.0268 to +0.5132 | no |
| pods started | 0.1 | 0.6 | +500.0% | −0.1952 to +1.1952 | no |
| pod start wait, total (s) | 0.2 | 1 | +400.0% | −0.5403 to +2.1403 | no |
| pod start wait, mean (s) | 0.2 | 0.6 | +200.0% | −0.4396 to +1.2396 | no |
| host CPU busy, the real machine under kind (%) | 43.38 | 46.89 | +8.1% | +2.7973 to +4.2262 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 822 | 836.1 | +1.7% | +1.3289 to +26.8711 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.781 | −37.0% | −3.2826 to −1.1555 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.8833 | 1.158 | +31.1% | −0.0064 to +0.5564 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 3.5 | +66.7% | +0.0854 to +2.7146 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 124.2 | 135.6 | +9.2% | +1.5776 to +21.2391 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*