# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.513 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 141.2 | 117.4 |
| response time (ms), 95th percentile | 244.1 | 261.1 |
| response time (ms), 99th percentile | 360.4 | 384.2 |
| time over the response line (% of samples) | 0.1782 | 0.2944 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1196 | 1349 |
| utilisation (used / allocatable) | 0.06011 | 0.05853 |
| CPU used (cores), mean | 1.443 | 1.405 |
| Omni's own CPU (cores), mean | 0 | 0.072 |
| CPU used with Omni's own (cores), mean | 1.443 | 1.477 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.6 | 461.9 |
| HPA replicas, mean | 1.982 | 2.226 |
| pods started | 0 | 0.9 |
| pod start wait, total (s) | 0 | 2 |
| pod start wait, mean (s) | 0 | 1.067 |
| host CPU busy, the real machine under kind (%) | 45.18 | 47.07 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1460 | 1509 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 171.4 | 208.6 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 741.1 | 868.9 |
| queue: job turnaround, submitted to done, mean (s) | 863.4 | 946.6 |
| queue: jobs unfinished at the window's end | 12.2 | 14.7 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 2.513 | 2.513 | −0.0% | −0.0111 to +0.0108 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.5 | −0.2% | −1.9477 to +0.6330 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.5 | −0.2% | −1.9477 to +0.6330 | no |
| response time (ms), mean | 141.2 | 117.4 | −16.9% | −30.2581 to −17.4142 | yes: GAIN |
| response time (ms), 95th percentile | 244.1 | 261.1 | +7.0% | +11.3516 to +22.6754 | yes: LOSS |
| response time (ms), 99th percentile | 360.4 | 384.2 | +6.6% | +10.7195 to +36.8691 | yes: LOSS |
| time over the response line (% of samples) | 0.1782 | 0.2944 | +65.2% | +0.0179 to +0.2145 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.1 | +117.100 (native is 0) | +97.5063 to +136.6937 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1196 | 1349 | +12.9% | +88.9373 to +218.6494 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06011 | 0.05853 | −2.6% | −0.0029 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.443 | 1.405 | −2.6% | −0.0699 to −0.0058 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.072 | +0.072 (native is 0) | +0.0638 to +0.0802 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.443 | 1.477 | +2.4% | +0.0070 to +0.0613 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.6 | 461.9 | +2.5% | +1.2122 to +21.3519 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.982 | 2.226 | +12.3% | +0.1064 to +0.3812 | yes: power given |
| pods started | 0 | 0.9 | +0.900 (native is 0) | +0.0436 to +1.7564 | yes: power given |
| pod start wait, total (s) | 0 | 2 | +2.000 (native is 0) | −0.0232 to +4.0232 | no |
| pod start wait, mean (s) | 0 | 1.067 | +1.067 (native is 0) | +0.2499 to +1.8834 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.18 | 47.07 | +4.2% | +1.1606 to +2.6039 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1460 | 1509 | +3.4% | −25.4474 to +123.8474 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 171.4 | 208.6 | +21.7% | −3.9046 to +78.2296 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 741.1 | 868.9 | +17.2% | −58.9382 to +314.5382 | no |
| queue: job turnaround, submitted to done, mean (s) | 863.4 | 946.6 | +9.6% | +33.6612 to +132.8472 | yes: LOSS |
| queue: jobs unfinished at the window's end | 12.2 | 14.7 | +20.5% | +0.4698 to +4.5302 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*