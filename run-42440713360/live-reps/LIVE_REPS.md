# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.231 |
| node-hours | 2.518 | 2.195 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 249.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 299.7 | 290.3 |
| response time (ms), 95th percentile | 1149 | 1276 |
| response time (ms), 99th percentile | 1678 | 1844 |
| time over the response line (% of samples) | 9.63 | 10.38 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 90.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.872 | 11.91 |
| utilisation (used / allocatable) | 0.06114 | 0.07132 |
| CPU used (cores), mean | 1.467 | 1.482 |
| Omni's own CPU (cores), mean | 0 | 0.07281 |
| CPU used with Omni's own (cores), mean | 1.467 | 1.555 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.6 | 403.5 |
| HPA replicas, mean | 2.077 | 2.316 |
| pods started | 0.1 | 1.2 |
| pod start wait, total (s) | 0.1 | 2.6 |
| pod start wait, mean (s) | 0.1 | 1.583 |
| host CPU busy, the real machine under kind (%) | 42.17 | 45.27 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 776.6 | 786.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.55 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1625 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 |
| queue: job turnaround, submitted to done, mean (s) | 84.68 | 94.56 |
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
| worker nodes in service, mean | 6 | 5.231 | −12.8% | −1.2903 to −0.2480 | yes: GAIN |
| node-hours | 2.518 | 2.195 | −12.8% | −0.5386 to −0.1077 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.6 | +0.1% | −0.5600 to +0.9274 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 249.4 | −8.8% | −40.2900 to −7.8385 | yes: GAIN |
| response time (ms), mean | 299.7 | 290.3 | −3.1% | −41.3618 to +22.5165 | no |
| response time (ms), 95th percentile | 1149 | 1276 | +11.0% | −29.7446 to +283.2026 | no |
| response time (ms), 99th percentile | 1678 | 1844 | +9.9% | −20.7177 to +352.1165 | no |
| time over the response line (% of samples) | 9.63 | 10.38 | +7.8% | −0.8169 to +2.3182 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.3 | 7.7 | +5.5% | −0.1001 to +0.9001 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 90.2 | +90.200 (native is 0) | +51.2585 to +129.1415 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 9.872 | 11.91 | +20.6% | +0.2386 to +3.8380 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06114 | 0.07132 | +16.6% | +0.0038 to +0.0166 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.467 | 1.482 | +1.0% | −0.0069 to +0.0368 | no |
| Omni's own CPU (cores), mean | 0 | 0.07281 | +0.073 (native is 0) | +0.0682 to +0.0774 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.467 | 1.555 | +6.0% | +0.0634 to +0.1121 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.6 | 403.5 | −10.3% | −73.0848 to −19.2689 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.077 | 2.316 | +11.5% | −0.0138 to +0.4910 | no |
| pods started | 0.1 | 1.2 | +1100.0% | +0.3128 to +1.8872 | yes: power given |
| pod start wait, total (s) | 0.1 | 2.6 | +2500.0% | +0.9094 to +4.0906 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.583 | +1483.3% | +0.7037 to +2.2630 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 42.17 | 45.27 | +7.4% | +2.6641 to +3.5476 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 776.6 | 786.3 | +1.2% | +1.6491 to +17.7509 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.55 | −24.2% | −2.3811 to −0.5199 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.06667 | 0.1625 | +143.7% | −0.0841 to +0.2758 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.5 | 0.6 | +20.0% | −0.4278 to +0.6278 | no |
| queue: job turnaround, submitted to done, mean (s) | 84.68 | 94.56 | +11.7% | +2.3776 to +17.3807 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*