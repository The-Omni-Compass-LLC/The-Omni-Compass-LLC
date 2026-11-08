# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.513 | 2.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 147.2 | 121 |
| response time (ms), 95th percentile | 260 | 270.6 |
| response time (ms), 99th percentile | 374.7 | 392.3 |
| time over the response line (% of samples) | 0.2765 | 0.2849 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1263 | 1356 |
| utilisation (used / allocatable) | 0.06073 | 0.05796 |
| CPU used (cores), mean | 1.458 | 1.391 |
| Omni's own CPU (cores), mean | 0 | 0.07234 |
| CPU used with Omni's own (cores), mean | 1.458 | 1.463 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.2 | 465.9 |
| HPA replicas, mean | 2.003 | 2.2 |
| pods started | 0.1 | 1 |
| pod start wait, total (s) | 0.2 | 2 |
| pod start wait, mean (s) | 0.2 | 0.775 |
| host CPU busy, the real machine under kind (%) | 45.62 | 47.22 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1508 | 1512 |
| batch: worker machines in service after the queue finished, mean | nan | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 162.6 | 205.5 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 720.8 | 856.4 |
| queue: job turnaround, submitted to done, mean (s) | 920.4 | 958.9 |
| queue: jobs unfinished at the window's end | 14.2 | 15.6 |
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
| node-hours | 2.513 | 2.518 | +0.2% | −0.0037 to +0.0147 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 271.9 | −0.1% | −1.3643 to +0.7627 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 271.9 | −0.1% | −1.3643 to +0.7627 | no |
| response time (ms), mean | 147.2 | 121 | −17.8% | −29.8188 to −22.5814 | yes: GAIN |
| response time (ms), 95th percentile | 260 | 270.6 | +4.1% | +0.8183 to +20.3607 | yes: LOSS |
| response time (ms), 99th percentile | 374.7 | 392.3 | +4.7% | +1.8014 to +33.2334 | yes: LOSS |
| time over the response line (% of samples) | 0.2765 | 0.2849 | +3.1% | −0.0866 to +0.1036 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.2 | 0 | −100.0% | −0.6524 to +0.2524 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 103 | +103.000 (native is 0) | +88.6462 to +117.3538 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1263 | 1356 | +7.4% | +32.9954 to +153.1979 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06073 | 0.05796 | −4.6% | −0.0044 to −0.0012 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.458 | 1.391 | −4.6% | −0.1053 to −0.0279 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07234 | +0.072 (native is 0) | +0.0668 to +0.0779 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.458 | 1.463 | +0.4% | −0.0335 to +0.0450 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.2 | 465.9 | +4.4% | +8.5907 to +30.7484 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.003 | 2.2 | +9.8% | −0.0676 to +0.4609 | no |
| pods started | 0.1 | 1 | +900.0% | −0.1900 to +1.9900 | no |
| pod start wait, total (s) | 0.2 | 2 | +900.0% | −0.5068 to +4.1068 | no |
| pod start wait, mean (s) | 0.2 | 0.775 | +287.5% | −0.0997 to +1.2497 | no |
| host CPU busy, the real machine under kind (%) | 45.62 | 47.22 | +3.5% | +0.5920 to +2.6091 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1508 | 1512 | +0.2% | −1.8586 to +8.6586 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 162.6 | 205.5 | +26.4% | −15.6159 to +101.4242 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 720.8 | 856.4 | +18.8% | −43.5864 to +314.7864 | no |
| queue: job turnaround, submitted to done, mean (s) | 920.4 | 958.9 | +4.2% | −9.1857 to +86.1190 | no |
| queue: jobs unfinished at the window's end | 14.2 | 15.6 | +9.9% | −1.4850 to +4.2850 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*