# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.952 |
| node-hours | 2.513 | 2.078 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 274.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 241.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 355.5 | 333.8 |
| response time (ms), 95th percentile | 1455 | 1562 |
| response time (ms), 99th percentile | 2399 | 2539 |
| time over the response line (% of samples) | 14.63 | 14.14 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.25 | 18.74 |
| utilisation (used / allocatable) | 0.06397 | 0.07735 |
| CPU used (cores), mean | 1.535 | 1.515 |
| Omni's own CPU (cores), mean | 0 | 0.01802 |
| CPU used with Omni's own (cores), mean | 1.535 | 1.533 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.1 | 381.5 |
| HPA replicas, mean | 1.988 | 2.011 |
| pods started | 0.2 | 0.2 |
| pod start wait, total (s) | 0.4 | 0.5 |
| pod start wait, mean (s) | 0.4 | 0.5 |
| host CPU busy, the real machine under kind (%) | 44.59 | 45.61 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 833.5 | 836 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.257 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7667 | 0.8875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 2.3 |
| queue: job turnaround, submitted to done, mean (s) | 144 | 146.7 |
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
| worker nodes in service, mean | 6 | 4.952 | −17.5% | −1.8961 to −0.1992 | yes: GAIN |
| node-hours | 2.513 | 2.078 | −17.3% | −0.7867 to −0.0820 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.6 | 274.1 | +0.2% | −0.5131 to +1.5117 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.6 | 241.1 | −11.9% | −59.0034 to −6.0021 | yes: GAIN |
| response time (ms), mean | 355.5 | 333.8 | −6.1% | −54.3788 to +11.0430 | no |
| response time (ms), 95th percentile | 1455 | 1562 | +7.3% | −157.9578 to +370.4788 | no |
| response time (ms), 99th percentile | 2399 | 2539 | +5.8% | −130.6687 to +410.1945 | no |
| time over the response line (% of samples) | 14.63 | 14.14 | −3.4% | −2.0385 to +1.0527 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.5 | 8.8 | +3.5% | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.6 | +37.600 (native is 0) | +22.7166 to +52.4834 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 17.25 | 18.74 | +8.6% | −0.5548 to +3.5315 | no |
| utilisation (used / allocatable) | 0.06397 | 0.07735 | +20.9% | +0.0025 to +0.0242 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.535 | 1.515 | −1.3% | −0.0520 to +0.0122 | no |
| Omni's own CPU (cores), mean | 0 | 0.01802 | +0.018 (native is 0) | +0.0158 to +0.0202 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.535 | 1.533 | −0.1% | −0.0354 to +0.0317 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 438.1 | 381.5 | −12.9% | −103.8758 to −9.2333 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.988 | 2.011 | +1.2% | −0.0890 to +0.1349 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.4769 to +0.4769 | no |
| pod start wait, total (s) | 0.4 | 0.5 | +25.0% | −0.9900 to +1.1900 | no |
| pod start wait, mean (s) | 0.4 | 0.5 | +25.0% | −0.9900 to +1.1900 | no |
| host CPU busy, the real machine under kind (%) | 44.59 | 45.61 | +2.3% | +0.4415 to +1.5971 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 833.5 | 836 | +0.3% | −2.6388 to +7.6388 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.257 | −29.1% | −3.0290 to −0.4578 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7667 | 0.8875 | +15.8% | −0.0571 to +0.2988 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.4 | 2.3 | +64.3% | −1.1358 to +2.9358 | no |
| queue: job turnaround, submitted to done, mean (s) | 144 | 146.7 | +1.9% | −0.9584 to +6.3751 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*