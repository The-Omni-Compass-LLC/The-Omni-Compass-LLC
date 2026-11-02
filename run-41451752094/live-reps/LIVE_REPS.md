# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.083 |
| node-hours | 2.513 | 2.13 |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 245.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 490 | 466.7 |
| response time (ms), 95th percentile | 1869 | 1983 |
| response time (ms), 99th percentile | 2615 | 2773 |
| time over the response line (% of samples) | 21.24 | 20.92 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 18.75 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.63 | 16.72 |
| utilisation (used / allocatable) | 0.06466 | 0.07837 |
| CPU used (cores), mean | 1.552 | 1.566 |
| Omni's own CPU (cores), mean | 0 | 0.07743 |
| CPU used with Omni's own (cores), mean | 1.552 | 1.644 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.9 | 376 |
| HPA replicas, mean | 1.967 | 2.233 |
| pods started | 0.1 | 0.5 |
| pod start wait, total (s) | 0.3 | 1 |
| pod start wait, mean (s) | 0.3 | 0.75 |
| host CPU busy, the real machine under kind (%) | 45.26 | 48.55 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 835.6 | 845.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.541 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4833 | 1.021 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 5.5 |
| queue: job turnaround, submitted to done, mean (s) | 138.9 | 147.8 |
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
| worker nodes in service, mean | 6 | 5.083 | −15.3% | −1.7082 to −0.1254 | yes: GAIN |
| node-hours | 2.513 | 2.13 | −15.3% | −0.7144 to −0.0522 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274 | 274.3 | +0.1% | −0.6377 to +1.2671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274 | 245.5 | −10.4% | −53.5102 to −3.5063 | yes: GAIN |
| response time (ms), mean | 490 | 466.7 | −4.8% | −47.3187 to +0.5941 | no |
| response time (ms), 95th percentile | 1869 | 1983 | +6.1% | −24.2487 to +254.0547 | no |
| response time (ms), 99th percentile | 2615 | 2773 | +6.0% | −36.7977 to +352.8139 | no |
| time over the response line (% of samples) | 21.24 | 20.92 | −1.5% | −1.0167 to +0.3707 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 10.7 | −0.9% | −0.8113 to +0.6113 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.3 | +101.300 (native is 0) | +41.1697 to +161.4303 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.63 | 16.72 | +14.3% | −1.3057 to +5.4857 | no |
| utilisation (used / allocatable) | 0.06466 | 0.07837 | +21.2% | +0.0017 to +0.0257 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.552 | 1.566 | +0.9% | −0.0063 to +0.0356 | no |
| Omni's own CPU (cores), mean | 0 | 0.07743 | +0.077 (native is 0) | +0.0702 to +0.0847 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.552 | 1.644 | +5.9% | +0.0665 to +0.1177 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 432.9 | 376 | −13.1% | −106.2551 to −7.4052 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.967 | 2.233 | +13.5% | +0.0530 to +0.4793 | yes: power given |
| pods started | 0.1 | 0.5 | +400.0% | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0.3 | 1 | +233.3% | −0.6509 to +2.0509 | no |
| pod start wait, mean (s) | 0.3 | 0.75 | +150.0% | −0.5104 to +1.4104 | no |
| host CPU busy, the real machine under kind (%) | 45.26 | 48.55 | +7.3% | +2.8359 to +3.7479 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 835.6 | 845.3 | +1.2% | +0.1742 to +19.2258 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.541 | −24.3% | −2.5922 to −0.3253 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4833 | 1.021 | +111.2% | −0.3565 to +1.4315 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.7 | 5.5 | +103.7% | −2.7999 to +8.3999 | no |
| queue: job turnaround, submitted to done, mean (s) | 138.9 | 147.8 | +6.4% | −0.5751 to +18.3917 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*