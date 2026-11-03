# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.515 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 140 | 114.9 |
| response time (ms), 95th percentile | 242.6 | 249.5 |
| response time (ms), 99th percentile | 342.8 | 363.6 |
| time over the response line (% of samples) | 0.2 | 0.2928 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1186 | 1262 |
| utilisation (used / allocatable) | 0.06107 | 0.05953 |
| CPU used (cores), mean | 1.466 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0.0716 |
| CPU used with Omni's own (cores), mean | 1.466 | 1.5 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.1 | 454.6 |
| HPA replicas, mean | 2.057 | 2.197 |
| pods started | 0.2 | 0.8 |
| pod start wait, total (s) | 0.2 | 2.1 |
| pod start wait, mean (s) | 0.2 | 0.775 |
| host CPU busy, the real machine under kind (%) | 45.89 | 47.43 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1488 | 1493 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 150.3 | 192.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 712 | 812.9 |
| queue: job turnaround, submitted to done, mean (s) | 877 | 905.8 |
| queue: jobs unfinished at the window's end | 11.9 | 13.3 |
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
| node-hours | 2.515 | 2.514 | −0.0% | −0.0109 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.1 | −0.2% | −1.7014 to +0.5222 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 272.1 | −0.2% | −1.7014 to +0.5222 | no |
| response time (ms), mean | 140 | 114.9 | −18.0% | −30.2861 to −20.0378 | yes: GAIN |
| response time (ms), 95th percentile | 242.6 | 249.5 | +2.8% | −2.7940 to +16.4720 | no |
| response time (ms), 99th percentile | 342.8 | 363.6 | +6.1% | −6.5801 to +48.0679 | no |
| time over the response line (% of samples) | 0.2 | 0.2928 | +46.4% | −0.0960 to +0.2815 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | −0.4278 to +0.6278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 107.2 | +107.200 (native is 0) | +89.2434 to +125.1566 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1186 | 1262 | +6.4% | +11.0911 to +141.3489 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06107 | 0.05953 | −2.5% | −0.0028 to −0.0003 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.466 | 1.429 | −2.5% | −0.0660 to −0.0079 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0716 | +0.072 (native is 0) | +0.0645 to +0.0787 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.466 | 1.5 | +2.4% | +0.0057 to +0.0636 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 444.1 | 454.6 | +2.3% | +2.5421 to +18.3254 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.057 | 2.197 | +6.8% | −0.1059 to +0.3858 | no |
| pods started | 0.2 | 0.8 | +300.0% | −0.3048 to +1.5048 | no |
| pod start wait, total (s) | 0.2 | 2.1 | +950.0% | −0.6558 to +4.4558 | no |
| pod start wait, mean (s) | 0.2 | 0.775 | +287.5% | −0.2931 to +1.4431 | no |
| host CPU busy, the real machine under kind (%) | 45.89 | 47.43 | +3.4% | +0.9047 to +2.1889 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1488 | 1493 | +0.4% | −9.8681 to +20.6681 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 150.3 | 192.3 | +28.0% | −11.2979 to +95.3979 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 712 | 812.9 | +14.2% | −194.1136 to +395.9136 | no |
| queue: job turnaround, submitted to done, mean (s) | 877 | 905.8 | +3.3% | −16.2109 to +73.7693 | no |
| queue: jobs unfinished at the window's end | 11.9 | 13.3 | +11.8% | −0.6841 to +3.4841 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*