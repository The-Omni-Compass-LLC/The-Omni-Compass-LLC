# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.466 |
| node-hours | 2.51 | 2.288 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.4 | 274.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.4 | 257.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 502.9 | 462 |
| response time (ms), 95th percentile | 1947 | 1967 |
| response time (ms), 99th percentile | 2725 | 2786 |
| time over the response line (% of samples) | 23.71 | 23.11 |
| failed requests (%) | 0.01143 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 10.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.03 | 12.73 |
| utilisation (used / allocatable) | 0.06686 | 0.07391 |
| CPU used (cores), mean | 1.605 | 1.593 |
| Omni's own CPU (cores), mean | 0 | 0.01573 |
| CPU used with Omni's own (cores), mean | 1.605 | 1.609 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.9 | 389.2 |
| HPA replicas, mean | 1.987 | 2.207 |
| pods started | 0.1 | 0.7 |
| pod start wait, total (s) | 0.3 | 1.1 |
| pod start wait, mean (s) | 0.3 | 0.95 |
| host CPU busy, the real machine under kind (%) | 45.55 | 46.38 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 836.6 | 838.9 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.119 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.06667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 142.8 | 143.8 |
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
| worker nodes in service, mean | 6 | 5.466 | −8.9% | −1.2781 to +0.2096 | no |
| node-hours | 2.51 | 2.288 | −8.8% | −0.5327 to +0.0891 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 274.4 | 274.6 | +0.1% | −0.7930 to +1.2255 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.4 | 257.8 | −6.0% | −39.8594 to +6.7212 | no |
| response time (ms), mean | 502.9 | 462 | −8.1% | −59.7512 to −22.1226 | yes: GAIN |
| response time (ms), 95th percentile | 1947 | 1967 | +1.1% | −95.1063 to +136.2303 | no |
| response time (ms), 99th percentile | 2725 | 2786 | +2.2% | −115.2471 to +237.1271 | no |
| time over the response line (% of samples) | 23.71 | 23.11 | −2.5% | −1.2754 to +0.0706 | no |
| failed requests (%) | 0.01143 | 0 | −100.0% | −0.0373 to +0.0144 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.2 | 10.9 | −2.7% | −0.9786 to +0.3786 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 25.1 | +25.100 (native is 0) | +11.5639 to +38.6361 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.03 | 12.73 | −2.3% | −2.5842 to +1.9909 | no |
| utilisation (used / allocatable) | 0.06686 | 0.07391 | +10.5% | −0.0031 to +0.0171 | no |
| CPU used (cores), mean | 1.605 | 1.593 | −0.7% | −0.0388 to +0.0161 | no |
| Omni's own CPU (cores), mean | 0 | 0.01573 | +0.016 (native is 0) | +0.0145 to +0.0170 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.605 | 1.609 | +0.3% | −0.0240 to +0.0328 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 416.9 | 389.2 | −6.6% | −70.4573 to +15.1403 | no |
| HPA replicas, mean | 1.987 | 2.207 | +11.1% | +0.0635 to +0.3769 | yes: power given |
| pods started | 0.1 | 0.7 | +600.0% | −0.0032 to +1.2032 | no |
| pod start wait, total (s) | 0.3 | 1.1 | +266.7% | −0.4064 to +2.0064 | no |
| pod start wait, mean (s) | 0.3 | 0.95 | +216.7% | −0.4433 to +1.7433 | no |
| host CPU busy, the real machine under kind (%) | 45.55 | 46.38 | +1.8% | +0.4968 to +1.1523 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 836.6 | 838.9 | +0.3% | −2.6218 to +7.2218 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.119 | −14.7% | −2.0582 to +0.2967 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1208 | 0.06667 | −44.8% | −0.1431 to +0.0347 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.4 | −42.9% | −0.7828 to +0.1828 | no |
| queue: job turnaround, submitted to done, mean (s) | 142.8 | 143.8 | +0.7% | −4.4736 to +6.4986 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*