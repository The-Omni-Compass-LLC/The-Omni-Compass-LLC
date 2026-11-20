# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.518 | 2.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.3 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 130.6 | 133.6 |
| response time (ms), 95th percentile | 228.1 | 238 |
| response time (ms), 99th percentile | 326.1 | 352.8 |
| time over the response line (% of samples) | 0.1544 | 0.1773 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1089 | 1157 |
| utilisation (used / allocatable) | 0.0605 | 0.0586 |
| CPU used (cores), mean | 1.452 | 1.406 |
| Omni's own CPU (cores), mean | 0 | 0.06478 |
| CPU used with Omni's own (cores), mean | 1.452 | 1.471 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.7 | 461.1 |
| HPA replicas, mean | 1.997 | 2.105 |
| pods started | 0.1 | 0.4 |
| pod start wait, total (s) | 0.2 | 0.9 |
| pod start wait, mean (s) | 0.2 | 0.225 |
| host CPU busy, the real machine under kind (%) | 45.12 | 46.58 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1457 | 1492 |
| batch: worker machines in service after the queue finished, mean | 6 | 6 |
| queue: job wait, submitted to its first pod running, mean (s) | 140.7 | 192.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 683.4 | 828.1 |
| queue: job turnaround, submitted to done, mean (s) | 803.6 | 846.5 |
| queue: jobs unfinished at the window's end | 8 | 10.4 |
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
| node-hours | 2.518 | 2.521 | +0.1% | −0.0012 to +0.0082 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.3 | −0.1% | −0.9621 to +0.2560 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 272.3 | −0.1% | −0.9621 to +0.2560 | no |
| response time (ms), mean | 130.6 | 133.6 | +2.3% | −1.2992 to +7.3395 | no |
| response time (ms), 95th percentile | 228.1 | 238 | +4.3% | −0.5008 to +20.2918 | no |
| response time (ms), 99th percentile | 326.1 | 352.8 | +8.2% | +10.7270 to +42.6864 | yes: LOSS |
| time over the response line (% of samples) | 0.1544 | 0.1773 | +14.8% | −0.0672 to +0.1129 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 | −100.0% | −0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 29.3 | +29.300 (native is 0) | +14.1408 to +44.4592 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1089 | 1157 | +6.3% | −15.9199 to +152.8065 | no |
| utilisation (used / allocatable) | 0.0605 | 0.0586 | −3.2% | −0.0033 to −0.0005 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.452 | 1.406 | −3.2% | −0.0786 to −0.0130 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06478 | +0.065 (native is 0) | +0.0574 to +0.0721 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.452 | 1.471 | +1.3% | −0.0157 to +0.0537 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.7 | 461.1 | +3.0% | +3.7415 to +23.0793 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.997 | 2.105 | +5.4% | −0.1418 to +0.3586 | no |
| pods started | 0.1 | 0.4 | +300.0% | −0.6567 to +1.2567 | no |
| pod start wait, total (s) | 0.2 | 0.9 | +350.0% | −1.4340 to +2.8340 | no |
| pod start wait, mean (s) | 0.2 | 0.225 | +12.5% | −0.6925 to +0.7425 | no |
| host CPU busy, the real machine under kind (%) | 45.12 | 46.58 | +3.2% | +0.7410 to +2.1784 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1457 | 1492 | +2.4% | −24.9635 to +93.7635 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±nan to ±nan | no |
| queue: job wait, submitted to its first pod running, mean (s) | 140.7 | 192.4 | +36.7% | +14.8218 to +88.5782 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 683.4 | 828.1 | +21.2% | +19.3345 to +270.0655 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 803.6 | 846.6 | +5.3% | −30.3737 to +116.3237 | no |
| queue: jobs unfinished at the window's end | 8 | 10.4 | +30.0% | −0.4252 to +5.2252 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*