# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.516 | 2.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 271.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 271.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 148.3 | 123.7 |
| response time (ms), 95th percentile | 260.9 | 275.6 |
| response time (ms), 99th percentile | 380.8 | 408.4 |
| time over the response line (% of samples) | 0.2695 | 0.4841 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1356 | 1386 |
| utilisation (used / allocatable) | 0.06072 | 0.05887 |
| CPU used (cores), mean | 1.457 | 1.413 |
| Omni's own CPU (cores), mean | 0 | 0.07576 |
| CPU used with Omni's own (cores), mean | 1.457 | 1.489 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.6 | 459.3 |
| HPA replicas, mean | 2.026 | 2.248 |
| pods started | 0.2 | 1.2 |
| pod start wait, total (s) | 0.5 | 2.6 |
| pod start wait, mean (s) | 0.5 | 0.8167 |
| host CPU busy, the real machine under kind (%) | 45.9 | 47.84 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1507 | 1508 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 157.6 | 218.1 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696 | 869.6 |
| queue: job turnaround, submitted to done, mean (s) | 967.2 | 942.2 |
| queue: jobs unfinished at the window's end | 15.5 | 14.5 |
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
| node-hours | 2.516 | 2.513 | −0.1% | −0.0120 to +0.0050 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 271.7 | −0.4% | −2.1512 to +0.2072 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 271.7 | −0.4% | −2.1512 to +0.2072 | no |
| response time (ms), mean | 148.3 | 123.7 | −16.5% | −30.2091 to −18.8067 | yes: GAIN |
| response time (ms), 95th percentile | 260.9 | 275.6 | +5.6% | −3.0733 to +32.4633 | no |
| response time (ms), 99th percentile | 380.8 | 408.4 | +7.3% | −4.6198 to +59.8456 | no |
| time over the response line (% of samples) | 0.2695 | 0.4841 | +79.6% | −0.0257 to +0.4549 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.3 | +0.300 (native is 0) | −0.1828 to +0.7828 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 113.3 | +113.300 (native is 0) | +95.3426 to +131.2574 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1356 | 1386 | +2.3% | −35.2161 to +96.8028 | no |
| utilisation (used / allocatable) | 0.06072 | 0.05887 | −3.0% | −0.0042 to +0.0005 | no |
| CPU used (cores), mean | 1.457 | 1.413 | −3.0% | −0.1004 to +0.0118 | no |
| Omni's own CPU (cores), mean | 0 | 0.07576 | +0.076 (native is 0) | +0.0692 to +0.0823 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.457 | 1.489 | +2.2% | −0.0235 to +0.0863 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 446.6 | 459.3 | +2.8% | −3.4012 to +28.7681 | no |
| HPA replicas, mean | 2.026 | 2.248 | +11.0% | −0.0350 to +0.4792 | no |
| pods started | 0.2 | 1.2 | +500.0% | −0.1681 to +2.1681 | no |
| pod start wait, total (s) | 0.5 | 2.6 | +420.0% | −0.9432 to +5.1432 | no |
| pod start wait, mean (s) | 0.5 | 0.8167 | +63.3% | −0.8357 to +1.4690 | no |
| host CPU busy, the real machine under kind (%) | 45.9 | 47.84 | +4.2% | +0.9577 to +2.9248 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1507 | 1508 | +0.1% | −8.4383 to +11.0383 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 157.6 | 218.1 | +38.4% | +22.3565 to +98.6185 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 696 | 869.6 | +24.9% | +30.5746 to +316.6254 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 967.2 | 942.2 | −2.6% | −77.0157 to +27.0240 | no |
| queue: jobs unfinished at the window's end | 15.5 | 14.5 | −6.5% | −4.4388 to +2.4388 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*