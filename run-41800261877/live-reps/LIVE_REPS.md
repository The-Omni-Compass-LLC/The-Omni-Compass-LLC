# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.997 |
| node-hours | 2.519 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 138.9 | 115.6 |
| response time (ms), 95th percentile | 245.5 | 257.5 |
| response time (ms), 99th percentile | 358.3 | 377.5 |
| time over the response line (% of samples) | 0.2785 | 0.3855 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1172 | 1226 |
| utilisation (used / allocatable) | 0.06006 | 0.05841 |
| CPU used (cores), mean | 1.442 | 1.401 |
| Omni's own CPU (cores), mean | 0 | 0.07124 |
| CPU used with Omni's own (cores), mean | 1.442 | 1.472 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 462.7 |
| HPA replicas, mean | 2.004 | 2.31 |
| pods started | 0.1 | 1.7 |
| pod start wait, total (s) | 0.1 | 3.9 |
| pod start wait, mean (s) | 0.1 | 1.448 |
| host CPU busy, the real machine under kind (%) | 45.2 | 46.66 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1458 | 1474 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.893 |
| queue: job wait, submitted to its first pod running, mean (s) | 162.4 | 217.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 732.6 | 889.7 |
| queue: job turnaround, submitted to done, mean (s) | 843.7 | 877.8 |
| queue: jobs unfinished at the window's end | 9.8 | 11.7 |
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
| worker nodes in service, mean | 6 | 5.997 | −0.1% | −0.0104 to +0.0040 | no |
| node-hours | 2.519 | 2.515 | −0.1% | −0.0132 to +0.0059 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.8 | −0.3% | −1.9410 to +0.4757 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.7 | −0.3% | −2.1122 to +0.4468 | no |
| response time (ms), mean | 138.9 | 115.6 | −16.8% | −31.0090 to −15.5499 | yes: GAIN |
| response time (ms), 95th percentile | 245.5 | 257.5 | +4.9% | +0.8646 to +23.2474 | yes: LOSS |
| response time (ms), 99th percentile | 358.3 | 377.5 | +5.4% | −1.9936 to +40.3978 | no |
| time over the response line (% of samples) | 0.2785 | 0.3855 | +38.5% | −0.0437 to +0.2578 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0.2 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.2 | +111.200 (native is 0) | +92.9669 to +129.4331 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1172 | 1226 | +4.6% | −4.6383 to +113.1716 | no |
| utilisation (used / allocatable) | 0.06006 | 0.05841 | −2.8% | −0.0031 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.442 | 1.401 | −2.8% | −0.0747 to −0.0063 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07124 | +0.071 (native is 0) | +0.0622 to +0.0803 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.442 | 1.472 | +2.1% | +0.0011 to +0.0604 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.8 | 462.7 | +2.6% | +1.3657 to +22.4650 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.004 | 2.31 | +15.2% | +0.0664 to +0.5446 | yes: power given |
| pods started | 0.1 | 1.7 | +1600.0% | +0.3749 to +2.8251 | yes: power given |
| pod start wait, total (s) | 0.1 | 3.9 | +3800.0% | +0.8067 to +6.7933 | yes: LOSS |
| pod start wait, mean (s) | 0.1 | 1.448 | +1348.3% | +0.3413 to +2.3553 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.2 | 46.66 | +3.2% | +0.6986 to +2.2190 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1458 | 1474 | +1.1% | −14.2451 to +45.0451 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.893 | −1.8% | −1.4685 to +1.2542 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 162.4 | 217.1 | +33.7% | +6.4226 to +103.1108 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 732.6 | 889.7 | +21.4% | −17.3390 to +331.5390 | no |
| queue: job turnaround, submitted to done, mean (s) | 843.7 | 877.8 | +4.0% | −15.5542 to +83.7958 | no |
| queue: jobs unfinished at the window's end | 9.8 | 11.7 | +19.4% | −0.9101 to +4.7101 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*