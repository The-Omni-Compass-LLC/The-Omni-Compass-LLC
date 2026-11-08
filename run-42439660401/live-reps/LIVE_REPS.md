# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.588 |
| node-hours | 2.513 | 1.919 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 228.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 377.2 | 351.7 |
| response time (ms), 95th percentile | 1579 | 1717 |
| response time (ms), 99th percentile | 2235 | 2419 |
| time over the response line (% of samples) | 13.27 | 12.39 |
| failed requests (%) | 0.01136 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.77 | 14.72 |
| utilisation (used / allocatable) | 0.06231 | 0.0845 |
| CPU used (cores), mean | 1.495 | 1.496 |
| Omni's own CPU (cores), mean | 0 | 0.07476 |
| CPU used with Omni's own (cores), mean | 1.495 | 1.57 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.8 | 364.9 |
| HPA replicas, mean | 2.01 | 2.202 |
| pods started | 0.2 | 0.6 |
| pod start wait, total (s) | 0.4 | 1 |
| pod start wait, mean (s) | 0.4 | 0.5 |
| host CPU busy, the real machine under kind (%) | 43.07 | 46.39 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 807.3 | 818.7 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.878 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2333 | 0.3875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.7 |
| queue: job turnaround, submitted to done, mean (s) | 115.5 | 125.6 |
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
| worker nodes in service, mean | 6 | 4.588 | −23.5% | −2.4058 to −0.4186 | yes: GAIN |
| node-hours | 2.513 | 1.919 | −23.6% | −1.0071 to −0.1813 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.1 | 273.1 | −0.0% | −0.7715 to +0.7611 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.1 | 228.8 | −16.2% | −75.1554 to −13.5592 | yes: GAIN |
| response time (ms), mean | 377.2 | 351.7 | −6.8% | −46.9966 to −3.9541 | yes: GAIN |
| response time (ms), 95th percentile | 1579 | 1717 | +8.8% | +13.1750 to +264.1340 | yes: LOSS |
| response time (ms), 99th percentile | 2235 | 2419 | +8.2% | −32.4517 to +400.9273 | no |
| time over the response line (% of samples) | 13.27 | 12.39 | −6.7% | −2.4874 to +0.7200 | no |
| failed requests (%) | 0.01136 | 0 | −100.0% | −0.0371 to +0.0143 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8 | +5.3% | −0.2911 to +1.0911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 105.6 | +105.600 (native is 0) | +36.7311 to +174.4689 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.77 | 14.72 | +15.3% | −0.0934 to +4.0067 | no |
| utilisation (used / allocatable) | 0.06231 | 0.0845 | +35.6% | +0.0062 to +0.0382 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.495 | 1.496 | +0.0% | −0.0227 to +0.0231 | no |
| Omni's own CPU (cores), mean | 0 | 0.07476 | +0.075 (native is 0) | +0.0691 to +0.0805 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.495 | 1.57 | +5.0% | +0.0490 to +0.1009 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448.8 | 364.9 | −18.7% | −143.8307 to −23.9675 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.01 | 2.202 | +9.6% | −0.0764 to +0.4605 | no |
| pods started | 0.2 | 0.6 | +200.0% | −0.3689 to +1.1689 | no |
| pod start wait, total (s) | 0.4 | 1 | +150.0% | −0.9155 to +2.1155 | no |
| pod start wait, mean (s) | 0.4 | 0.5 | +25.0% | −0.7564 to +0.9564 | no |
| host CPU busy, the real machine under kind (%) | 43.07 | 46.39 | +7.7% | +2.9451 to +3.7038 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 807.3 | 818.7 | +1.4% | +3.6356 to +19.1644 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 3.878 | −35.4% | −3.4824 to −0.7614 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2333 | 0.3875 | +66.1% | −0.1889 to +0.4972 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.6 | 2.7 | +68.8% | −2.1944 to +4.3944 | no |
| queue: job turnaround, submitted to done, mean (s) | 115.5 | 125.6 | +8.7% | +2.7016 to +17.4068 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*