# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.997 |
| node-hours | 2.516 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 136.3 | 102.3 |
| response time (ms), 95th percentile | 239 | 226.3 |
| response time (ms), 99th percentile | 348.8 | 341.9 |
| time over the response line (% of samples) | 0.2088 | 0.2698 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1152 | 1179 |
| utilisation (used / allocatable) | 0.06059 | 0.0596 |
| CPU used (cores), mean | 1.454 | 1.43 |
| Omni's own CPU (cores), mean | 0 | 0.01208 |
| CPU used with Omni's own (cores), mean | 1.454 | 1.442 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 454 |
| HPA replicas, mean | 1.964 | 2 |
| pods started | 0 | 0.1 |
| pod start wait, total (s) | 0 | 0.2 |
| pod start wait, mean (s) | 0 | 0.2 |
| host CPU busy, the real machine under kind (%) | 45.51 | 45.32 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1475 | 1461 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.912 |
| queue: job wait, submitted to its first pod running, mean (s) | 139.6 | 143.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 652 | 710.6 |
| queue: job turnaround, submitted to done, mean (s) | 862.2 | 856.7 |
| queue: jobs unfinished at the window's end | 10.7 | 10.9 |
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
| node-hours | 2.516 | 2.514 | −0.1% | −0.0140 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.2 | −0.1% | −1.4066 to +0.8588 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 | −0.1% | −1.5992 to +0.8515 | no |
| response time (ms), mean | 136.3 | 102.3 | −25.0% | −40.1273 to −27.9121 | yes: GAIN |
| response time (ms), 95th percentile | 239 | 226.3 | −5.3% | −19.1678 to −6.1592 | yes: GAIN |
| response time (ms), 99th percentile | 348.8 | 341.9 | −2.0% | −40.7780 to +26.8740 | no |
| time over the response line (% of samples) | 0.2088 | 0.2698 | +29.2% | −0.1042 to +0.2262 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 11.2 | +11.200 (native is 0) | +9.6256 to +12.7744 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1152 | 1179 | +2.4% | −55.1635 to +109.6802 | no |
| utilisation (used / allocatable) | 0.06059 | 0.0596 | −1.6% | −0.0027 to +0.0007 | no |
| CPU used (cores), mean | 1.454 | 1.43 | −1.7% | −0.0638 to +0.0151 | no |
| Omni's own CPU (cores), mean | 0 | 0.01208 | +0.012 (native is 0) | +0.0109 to +0.0133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.454 | 1.442 | −0.8% | −0.0517 to +0.0271 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 454 | +1.5% | −4.6525 to +18.1709 | no |
| HPA replicas, mean | 1.964 | 2 | +1.8% | −0.1220 to +0.1946 | no |
| pods started | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| pod start wait, total (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, mean (s) | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| host CPU busy, the real machine under kind (%) | 45.51 | 45.32 | −0.4% | −1.1203 to +0.7350 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1475 | 1461 | −0.9% | −61.6856 to +34.0856 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.824 | −2.9% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 139.6 | 143.2 | +2.5% | −26.8785 to +33.9285 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 652 | 710.6 | +9.0% | −49.4139 to +166.6139 | no |
| queue: job turnaround, submitted to done, mean (s) | 862.2 | 856.7 | −0.6% | −70.3085 to +59.3252 | no |
| queue: jobs unfinished at the window's end | 10.7 | 10.9 | +1.9% | −2.9052 to +3.3052 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*