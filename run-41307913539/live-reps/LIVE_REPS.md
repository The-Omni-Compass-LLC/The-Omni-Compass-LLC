# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.485 |
| node-hours | 2.518 | 2.299 |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 259.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 630.2 | 609.8 |
| response time (ms), 95th percentile | 2918 | 3022 |
| response time (ms), 99th percentile | 3841 | 4043 |
| time over the response line (% of samples) | 22.54 | 22.64 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 13.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.24 | 39.67 |
| utilisation (used / allocatable) | 0.06791 | 0.07432 |
| CPU used (cores), mean | 1.63 | 1.636 |
| Omni's own CPU (cores), mean | 0 | 0.01804 |
| CPU used with Omni's own (cores), mean | 1.63 | 1.654 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.8 | 384.5 |
| HPA replicas, mean | 2.009 | 2.145 |
| pods started | 0 | 0.4 |
| pod start wait, total (s) | 0 | 0.4 |
| pod start wait, mean (s) | 0 | 0.3 |
| host CPU busy, the real machine under kind (%) | 49.52 | 50.84 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 914.8 | 925.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.151 |
| queue: job wait, submitted to its first pod running, mean (s) | 1.463 | 1.758 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.1 | 8.2 |
| queue: job turnaround, submitted to done, mean (s) | 209.5 | 219.1 |
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
| worker nodes in service, mean | 6 | 5.485 | −8.6% | −1.2400 to +0.2093 | no |
| node-hours | 2.518 | 2.299 | −8.7% | −0.5226 to +0.0855 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 275.7 | 275.7 | −0.0% | −1.0342 to +1.0294 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.7 | 259.4 | −5.9% | −39.2602 to +6.7471 | no |
| response time (ms), mean | 630.2 | 609.8 | −3.2% | −51.5356 to +10.7968 | no |
| response time (ms), 95th percentile | 2918 | 3022 | +3.6% | −72.0779 to +280.2499 | no |
| response time (ms), 99th percentile | 3841 | 4043 | +5.2% | −34.2774 to +436.8882 | no |
| time over the response line (% of samples) | 22.54 | 22.64 | +0.4% | −1.5884 to +1.7892 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 12.7 | 13.1 | +3.1% | +0.0306 to +0.7694 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 21.5 | +21.500 (native is 0) | +11.0237 to +31.9763 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 33.24 | 39.67 | +19.3% | +1.5810 to +11.2657 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06791 | 0.07432 | +9.4% | −0.0012 to +0.0140 | no |
| CPU used (cores), mean | 1.63 | 1.636 | +0.4% | −0.0217 to +0.0346 | no |
| Omni's own CPU (cores), mean | 0 | 0.01804 | +0.018 (native is 0) | +0.0172 to +0.0189 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.63 | 1.654 | +1.5% | −0.0041 to +0.0530 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 418.8 | 384.5 | −8.2% | −78.2170 to +9.6991 | no |
| HPA replicas, mean | 2.009 | 2.145 | +6.8% | −0.0316 to +0.3042 | no |
| pods started | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, total (s) | 0 | 0.4 | +0.400 (native is 0) | −0.1001 to +0.9001 | no |
| pod start wait, mean (s) | 0 | 0.3 | +0.300 (native is 0) | −0.0455 to +0.6455 | no |
| host CPU busy, the real machine under kind (%) | 49.52 | 50.84 | +2.7% | +0.9588 to +1.6844 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 914.8 | 925.8 | +1.2% | +3.2518 to +18.7482 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.151 | −14.2% | −1.9772 to +0.2787 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 1.463 | 1.758 | +20.2% | −0.1443 to +0.7360 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 6.1 | 8.2 | +34.4% | −2.1579 to +6.3579 | no |
| queue: job turnaround, submitted to done, mean (s) | 209.5 | 219.1 | +4.6% | +3.5296 to +15.6537 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*