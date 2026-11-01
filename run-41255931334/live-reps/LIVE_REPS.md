# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.295 |
| node-hours | 2.514 | 2.22 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 251.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 455.3 | 426.5 |
| response time (ms), 95th percentile | 1716 | 1795 |
| response time (ms), 99th percentile | 2443 | 2455 |
| time over the response line (% of samples) | 21.73 | 21.22 |
| failed requests (%) | 0.01149 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.14 | 12.71 |
| utilisation (used / allocatable) | 0.06353 | 0.07286 |
| CPU used (cores), mean | 1.525 | 1.529 |
| Omni's own CPU (cores), mean | 0 | 0.01751 |
| CPU used with Omni's own (cores), mean | 1.525 | 1.546 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.5 | 397.1 |
| HPA replicas, mean | 1.955 | 2.114 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 0.2 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.2 |
| host CPU busy, the real machine under kind (%) | 44.27 | 45.2 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 820.8 | 827.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.85 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5292 | 0.6625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 3.5 |
| queue: job turnaround, submitted to done, mean (s) | 127.9 | 131.7 |
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
| worker nodes in service, mean | 6 | 5.295 | −11.7% | −1.4911 to +0.0817 | no |
| node-hours | 2.514 | 2.22 | −11.7% | −0.6270 to +0.0379 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 273.7 | 273.9 | +0.1% | −0.4841 to +1.0160 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.7 | 251.8 | −8.0% | −46.7138 to +2.9873 | no |
| response time (ms), mean | 455.3 | 426.5 | −6.3% | −36.8436 to −20.6666 | yes: GAIN |
| response time (ms), 95th percentile | 1716 | 1795 | +4.6% | −8.0277 to +166.5667 | no |
| response time (ms), 99th percentile | 2443 | 2455 | +0.5% | −118.2956 to +142.8662 | no |
| time over the response line (% of samples) | 21.73 | 21.22 | −2.3% | −1.0396 to +0.0318 | no |
| failed requests (%) | 0.01149 | 0 | −100.0% | −0.0375 to +0.0145 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.7 | 10.7 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.7 | +37.700 (native is 0) | +11.2841 to +64.1159 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 11.14 | 12.71 | +14.1% | −0.4385 to +3.5752 | no |
| utilisation (used / allocatable) | 0.06353 | 0.07286 | +14.7% | −0.0012 to +0.0199 | no |
| CPU used (cores), mean | 1.525 | 1.529 | +0.3% | −0.0146 to +0.0222 | no |
| Omni's own CPU (cores), mean | 0 | 0.01751 | +0.018 (native is 0) | +0.0162 to +0.0188 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.525 | 1.546 | +1.4% | +0.0023 to +0.0403 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.5 | 397.1 | −10.9% | −106.4677 to +9.5375 | no |
| HPA replicas, mean | 1.955 | 2.114 | +8.1% | −0.0820 to +0.3991 | no |
| pods started | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| host CPU busy, the real machine under kind (%) | 44.27 | 45.2 | +2.1% | +0.5351 to +1.3338 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 820.8 | 827.2 | +0.8% | +0.8675 to +11.9325 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.85 | −19.2% | −2.3335 to +0.0337 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.5292 | 0.6625 | +25.2% | −0.0139 to +0.2806 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 3.5 | +29.6% | −1.2732 to +2.8732 | no |
| queue: job turnaround, submitted to done, mean (s) | 127.9 | 131.7 | +2.9% | +0.1712 to +7.3038 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*