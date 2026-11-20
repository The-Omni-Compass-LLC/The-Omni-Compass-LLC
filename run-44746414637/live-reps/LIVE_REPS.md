# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.995 |
| node-hours | 2.521 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 135.2 | 139.2 |
| response time (ms), 95th percentile | 237.3 | 249.9 |
| response time (ms), 99th percentile | 352.1 | 359.9 |
| time over the response line (% of samples) | 0.3099 | 0.2413 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1209 | 1213 |
| utilisation (used / allocatable) | 0.05996 | 0.05839 |
| CPU used (cores), mean | 1.439 | 1.4 |
| Omni's own CPU (cores), mean | 0 | 0.06584 |
| CPU used with Omni's own (cores), mean | 1.439 | 1.466 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.9 | 462.5 |
| HPA replicas, mean | 1.998 | 2.302 |
| pods started | 0 | 1.1 |
| pod start wait, total (s) | 0 | 2.6 |
| pod start wait, mean (s) | 0 | 0.9667 |
| host CPU busy, the real machine under kind (%) | 45.53 | 46.54 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1482 | 1443 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.905 |
| queue: job wait, submitted to its first pod running, mean (s) | 152.8 | 184.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 731.6 | 837.1 |
| queue: job turnaround, submitted to done, mean (s) | 873.6 | 858.2 |
| queue: jobs unfinished at the window's end | 11.9 | 11.5 |
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
| worker nodes in service, mean | 6 | 5.995 | −0.1% | −0.0147 to +0.0057 | no |
| node-hours | 2.521 | 2.515 | −0.2% | −0.0133 to +0.0025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.8 | −0.4% | −1.9328 to −0.3038 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 271.6 | −0.5% | −2.0824 to −0.4375 | yes: GAIN |
| response time (ms), mean | 135.2 | 139.2 | +3.0% | −1.7645 to +9.8068 | no |
| response time (ms), 95th percentile | 237.3 | 249.9 | +5.3% | −4.8306 to +29.9456 | no |
| response time (ms), 99th percentile | 352.1 | 359.9 | +2.2% | −17.6355 to +33.2359 | no |
| time over the response line (% of samples) | 0.3099 | 0.2413 | −22.1% | −0.2190 to +0.0819 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 27.2 | +27.200 (native is 0) | +14.3829 to +40.0171 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1209 | 1213 | +0.3% | −101.6179 to +107.6979 | no |
| utilisation (used / allocatable) | 0.05996 | 0.05839 | −2.6% | −0.0029 to −0.0002 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.439 | 1.4 | −2.7% | −0.0701 to −0.0073 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06584 | +0.066 (native is 0) | +0.0583 to +0.0734 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.439 | 1.466 | +1.9% | −0.0001 to +0.0543 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.9 | 462.5 | +2.4% | +0.6303 to +20.6700 | yes, up (shown, not judged) |
| HPA replicas, mean | 1.998 | 2.302 | +15.2% | +0.0543 to +0.5528 | yes: power given |
| pods started | 0 | 1.1 | +1.100 (native is 0) | +0.0634 to +2.1366 | yes: power given |
| pod start wait, total (s) | 0 | 2.6 | +2.600 (native is 0) | +0.1638 to +5.0362 | yes: LOSS |
| pod start wait, mean (s) | 0 | 0.9667 | +0.967 (native is 0) | +0.0504 to +1.8829 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.53 | 46.54 | +2.2% | +0.4253 to +1.5934 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1482 | 1443 | −2.6% | −107.8774 to +29.6774 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 6 | ±0.0% | ±0.0000 to ±0.0000 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 152.8 | 184.1 | +20.5% | −2.7930 to +65.3930 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 731.6 | 837.1 | +14.4% | −90.7925 to +301.7925 | no |
| queue: job turnaround, submitted to done, mean (s) | 873.6 | 858.2 | −1.8% | −86.7388 to +55.8304 | no |
| queue: jobs unfinished at the window's end | 11.9 | 11.5 | −3.4% | −2.3720 to +1.5720 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*