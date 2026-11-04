# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.518 | 2.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 150.3 | 123.8 |
| response time (ms), 95th percentile | 259.4 | 277.3 |
| response time (ms), 99th percentile | 385.4 | 405.6 |
| time over the response line (% of samples) | 0.317 | 0.3769 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1326 | 1440 |
| utilisation (used / allocatable) | 0.05966 | 0.05823 |
| CPU used (cores), mean | 1.432 | 1.398 |
| Omni's own CPU (cores), mean | 0 | 0.07499 |
| CPU used with Omni's own (cores), mean | 1.432 | 1.473 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.6 | 464 |
| HPA replicas, mean | 2.047 | 2.435 |
| pods started | 0.1 | 1.8 |
| pod start wait, total (s) | 0.2 | 3.6 |
| pod start wait, mean (s) | 0.2 | 1.353 |
| host CPU busy, the real machine under kind (%) | 45.74 | 47.45 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1490 | 1512 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 172.1 | 210.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 818.2 | 848.1 |
| queue: job turnaround, submitted to done, mean (s) | 933 | 983.9 |
| queue: jobs unfinished at the window's end | 15 | 16.4 |
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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 2.518 | 2.519 | +0.0% | −0.0103 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.1 | −0.1% | −1.6062 to +0.8209 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 | −0.1% | −1.6062 to +0.8209 | no |
| response time (ms), mean | 150.3 | 123.8 | −17.7% | −31.9717 to −21.1009 | yes: GAIN |
| response time (ms), 95th percentile | 259.4 | 277.3 | +6.9% | +5.6799 to +30.1431 | yes: LOSS |
| response time (ms), 99th percentile | 385.4 | 405.6 | +5.2% | −8.2042 to +48.5542 | no |
| time over the response line (% of samples) | 0.317 | 0.3769 | +18.9% | −0.0993 to +0.2190 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.2 | +0.200 (native is 0) | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 125 | +125.000 (native is 0) | +106.0118 to +143.9882 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1326 | 1440 | +8.6% | +47.5299 to +181.0167 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05966 | 0.05823 | −2.4% | −0.0031 to +0.0002 | no |
| CPU used (cores), mean | 1.432 | 1.398 | −2.4% | −0.0744 to +0.0060 | no |
| Omni's own CPU (cores), mean | 0 | 0.07499 | +0.075 (native is 0) | +0.0676 to +0.0824 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.473 | +2.8% | +0.0040 to +0.0775 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.6 | 464 | +2.3% | −1.8796 to +22.6836 | no |
| HPA replicas, mean | 2.047 | 2.435 | +19.0% | +0.1235 to +0.6533 | yes: power given |
| pods started | 0.1 | 1.8 | +1700.0% | +0.4361 to +2.9639 | yes: power given |
| pod start wait, total (s) | 0.2 | 3.6 | +1700.0% | +0.6564 to +6.1436 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.353 | +576.7% | +0.1564 to +2.1503 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.74 | 47.45 | +3.7% | +0.9426 to +2.4784 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1490 | 1512 | +1.5% | −28.6378 to +72.2378 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 172.1 | 210.5 | +22.3% | +6.7896 to +69.9854 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 818.2 | 848.1 | +3.7% | −109.3879 to +169.1879 | no |
| queue: job turnaround, submitted to done, mean (s) | 933 | 983.9 | +5.5% | +1.5482 to +100.2685 | yes: LOSS |
| queue: jobs unfinished at the window's end | 15 | 16.4 | +9.3% | −0.4835 to +3.2835 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*