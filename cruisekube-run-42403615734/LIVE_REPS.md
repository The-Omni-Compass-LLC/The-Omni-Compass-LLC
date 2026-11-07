# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.972 |
| node-hours | 1.515 | 1.507 |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 162 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 161.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 79.44 | 80.85 |
| response time (ms), 95th percentile | 117.8 | 119.8 |
| response time (ms), 99th percentile | 131.2 | 141.1 |
| time over the response line (% of samples) | 0 | 0 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.11 |
| utilisation (used / allocatable) | 0.04808 | 0.04866 |
| CPU used (cores), mean | 1.154 | 1.162 |
| Omni's own CPU (cores), mean | 0 | 0.04909 |
| CPU used with Omni's own (cores), mean | 1.154 | 1.211 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 560.9 | 557.2 |
| HPA replicas, mean | 2.887 | 2.803 |
| pods started | 1.3 | 1.3 |
| pod start wait, total (s) | 1.7 | 1.9 |
| pod start wait, mean (s) | 1.1 | 1.45 |
| host CPU busy, the real machine under kind (%) | 36.38 | 38.1 |
| host cores (the real machine under kind) | 4 | 4 |
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
| worker nodes in service, mean | 6 | 5.972 | −0.5% | −0.0709 to +0.0144 | no |
| node-hours | 1.515 | 1.507 | −0.6% | −0.0248 to +0.0079 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 161.5 | 162 | +0.3% | −0.3416 to +1.3426 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 161.5 | 161.4 | −0.0% | −0.8868 to +0.8211 | no |
| response time (ms), mean | 79.44 | 80.85 | +1.8% | −0.1098 to +2.9337 | no |
| response time (ms), 95th percentile | 117.8 | 119.8 | +1.7% | +0.3075 to +3.7655 | yes: LOSS |
| response time (ms), 99th percentile | 131.2 | 141.1 | +7.6% | −0.4556 to +20.3202 | no |
| time over the response line (% of samples) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 4 | +4.000 (native is 0) | +4.0000 to +4.0000 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1333 | 0.11 | −17.5% | −0.2542 to +0.2075 | no |
| utilisation (used / allocatable) | 0.04808 | 0.04866 | +1.2% | −0.0000 to +0.0012 | no |
| CPU used (cores), mean | 1.154 | 1.162 | +0.7% | −0.0088 to +0.0242 | no |
| Omni's own CPU (cores), mean | 0 | 0.04909 | +0.049 (native is 0) | +0.0433 to +0.0548 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.154 | 1.211 | +4.9% | +0.0396 to +0.0740 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 560.9 | 557.2 | −0.7% | −10.4525 to +3.0473 | no |
| HPA replicas, mean | 2.887 | 2.803 | −2.9% | −0.3660 to +0.1986 | no |
| pods started | 1.3 | 1.3 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 1.7 | 1.9 | +11.8% | −0.6121 to +1.0121 | no |
| pod start wait, mean (s) | 1.1 | 1.45 | +31.8% | −0.2105 to +0.9105 | no |
| host CPU busy, the real machine under kind (%) | 36.38 | 38.1 | +4.7% | +1.2084 to +2.2289 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*