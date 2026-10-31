# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.996 |
| node-hours | 2.511 | 2.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 272.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 142.9 | 106.4 |
| response time (ms), 95th percentile | 247.5 | 237.3 |
| response time (ms), 99th percentile | 364 | 355.3 |
| time over the response line (% of samples) | 0.2621 | 0.2982 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.3333 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.89 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1234 | 1236 |
| utilisation (used / allocatable) | 0.06022 | 0.05965 |
| CPU used (cores), mean | 1.445 | 1.431 |
| Omni's own CPU (cores), mean | 0 | 0.01237 |
| CPU used with Omni's own (cores), mean | 1.445 | 1.443 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.7 | 453.5 |
| HPA replicas, mean | 2.049 | 1.99 |
| pods started | 0.2 | 0 |
| pod start wait, total (s) | 0.3 | 0 |
| pod start wait, mean (s) | 0.15 | 0 |
| host CPU busy, the real machine under kind (%) | 45.65 | 45.52 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1488 | 1485 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.786 |
| queue: job wait, submitted to its first pod running, mean (s) | 177 | 186.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 761.8 | 816.2 |
| queue: job turnaround, submitted to done, mean (s) | 885.3 | 888.5 |
| queue: jobs unfinished at the window's end | 11.8 | 13 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

**The babysitting tax.** Omni-Compass runs on autopilot: no person touched a setting in either arm. An alert
minute is a whole minute whose 95th percentile, failed requests counted over, was over the line: a minute an
on-call page would be open. The commands are the settings the governor wrote on its own, each in its audit with
its reason; the share decided inside the line counts its additions (a machine more, or a lower HPA target) made
before the line was crossed. The alert minutes are judged; the commands and the share are shown, not judged.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 9 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.996 | −0.1% | −0.0120 to +0.0047 | no |
| node-hours | 2.512 | 2.516 | +0.2% | −0.0077 to +0.0162 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.9 | 272.3 | +0.1% | −0.8714 to +1.6423 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.9 | 272.2 | +0.1% | −0.9770 to +1.5211 | no |
| response time (ms), mean | 140.9 | 106.4 | −24.5% | −39.1049 to −29.8780 | yes: GAIN |
| response time (ms), 95th percentile | 243.9 | 237.3 | −2.7% | −16.0438 to +2.9627 | no |
| response time (ms), 99th percentile | 357.8 | 355.3 | −0.7% | −22.7866 to +17.9817 | no |
| time over the response line (% of samples) | 0.2569 | 0.2982 | +16.1% | −0.0364 to +0.1190 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1111 | 0.3333 | +200.0% | −0.4183 to +0.8628 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.89 | +12.889 (native is 0) | +10.1864 to +15.5914 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1189 | 1236 | +3.9% | −19.6721 to +113.4166 | no |
| utilisation (used / allocatable) | 0.06032 | 0.05965 | −1.1% | −0.0018 to +0.0004 | no |
| CPU used (cores), mean | 1.448 | 1.431 | −1.2% | −0.0428 to +0.0089 | no |
| Omni's own CPU (cores), mean | 0 | 0.01237 | +0.012 (native is 0) | +0.0110 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.448 | 1.443 | −0.3% | −0.0310 to +0.0219 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449 | 453.5 | +1.0% | −3.0054 to +12.0822 | no |
| HPA replicas, mean | 2.059 | 1.99 | −3.3% | −0.1487 to +0.0116 | no |
| pods started | 0.2222 | 0 | −100.0% | −0.7347 to +0.2902 | no |
| pod start wait, total (s) | 0.3333 | 0 | −100.0% | −1.1020 to +0.4353 | no |
| pod start wait, mean (s) | 0.1667 | 0 | −100.0% | −0.5510 to +0.2177 | no |
| host CPU busy, the real machine under kind (%) | 45.55 | 45.52 | −0.1% | −0.5881 to +0.5310 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1486 | 1485 | −0.1% | −11.2337 to +9.2337 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.786 | −3.6% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 178.2 | 186.9 | +4.9% | −24.0367 to +41.5552 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 770.4 | 816.2 | +5.9% | −149.9361 to +241.4917 | no |
| queue: job turnaround, submitted to done, mean (s) | 862.2 | 888.5 | +3.1% | −35.0501 to +87.6612 | no |
| queue: jobs unfinished at the window's end | 10.78 | 13 | +20.6% | −0.0115 to +4.4559 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*