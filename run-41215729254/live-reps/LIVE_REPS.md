# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.485 |
| node-hours | 2.513 | 2.298 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 275 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 258.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 511.4 | 501.1 |
| response time (ms), 95th percentile | 2260 | 2436 |
| response time (ms), 99th percentile | 2974 | 3375 |
| time over the response line (% of samples) | 18.12 | 18.85 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 28.34 | 31.84 |
| utilisation (used / allocatable) | 0.0655 | 0.07374 |
| CPU used (cores), mean | 1.572 | 1.612 |
| Omni's own CPU (cores), mean | 0 | 0.01822 |
| CPU used with Omni's own (cores), mean | 1.572 | 1.63 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426 | 385.1 |
| HPA replicas, mean | 2.008 | 2.17 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.2 | 0.6 |
| pod start wait, mean (s) | 0.2 | 0.3333 |
| host CPU busy, the real machine under kind (%) | 47.98 | 49.6 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 870.5 | 885.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.083 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.325 | 1.208 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.8 | 3.1 |
| queue: job turnaround, submitted to done, mean (s) | 169.8 | 182.2 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.485 | −8.6% | −1.1206 to +0.0913 | no |
| node-hours | 2.513 | 2.298 | −8.5% | −0.4699 to +0.0404 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.3 | 275 | +0.3% | −0.0502 to +1.4955 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.3 | 258.9 | −5.6% | −34.7043 to +3.8163 | no |
| response time (ms), mean | 511.4 | 501.1 | −2.0% | −72.5918 to +52.1487 | no |
| response time (ms), 95th percentile | 2260 | 2436 | +7.8% | −117.6080 to +469.4200 | no |
| response time (ms), 99th percentile | 2974 | 3375 | +13.5% | −18.8344 to +820.9150 | no |
| time over the response line (% of samples) | 18.12 | 18.85 | +4.1% | −3.1782 to +4.6485 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.7 | 12.2 | +4.3% | −0.9005 to +1.9005 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.1 | +21.100 (native is 0) | +12.4869 to +29.7131 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 28.34 | 31.84 | +12.4% | +0.8827 to +6.1340 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.0655 | 0.07374 | +12.6% | +0.0003 to +0.0162 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.572 | 1.612 | +2.6% | −0.0114 to +0.0920 | no |
| Omni's own CPU (cores), mean | 0 | 0.01822 | +0.018 (native is 0) | +0.0172 to +0.0192 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.572 | 1.63 | +3.7% | +0.0073 to +0.1097 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 426 | 385.1 | −9.6% | −79.4923 to −2.2650 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.008 | 2.17 | +8.0% | −0.0166 to +0.3388 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.4578 to +1.0578 | no |
| pod start wait, total (s) | 0.2 | 0.6 | +200.0% | −0.7285 to +1.5285 | no |
| pod start wait, mean (s) | 0.2 | 0.3333 | +66.7% | −0.6054 to +0.8721 | no |
| host CPU busy, the real machine under kind (%) | 47.98 | 49.6 | +3.4% | +0.2309 to +3.0100 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 870.5 | 885.6 | +1.7% | −5.6794 to +35.8794 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.083 | −15.3% | −1.9503 to +0.1168 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.325 | 1.208 | −8.8% | −0.3250 to +0.0916 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 4.8 | 3.1 | −35.4% | −3.8866 to +0.4866 | no |
| queue: job turnaround, submitted to done, mean (s) | 169.8 | 182.2 | +7.3% | −7.2513 to +32.1013 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*