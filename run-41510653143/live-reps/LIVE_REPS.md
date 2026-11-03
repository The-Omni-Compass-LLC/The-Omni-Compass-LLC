# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 2.515 | 2.518 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 136.2 | 116.8 |
| response time (ms), 95th percentile | 232.3 | 251.4 |
| response time (ms), 99th percentile | 338.8 | 365.5 |
| time over the response line (% of samples) | 0.201 | 0.2414 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1177 | 1323 |
| utilisation (used / allocatable) | 0.06086 | 0.0582 |
| CPU used (cores), mean | 1.461 | 1.397 |
| Omni's own CPU (cores), mean | 0 | 0.07041 |
| CPU used with Omni's own (cores), mean | 1.461 | 1.467 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 464 |
| HPA replicas, mean | 2.023 | 2.141 |
| pods started | 0.2 | 0.3 |
| pod start wait, total (s) | 0.4 | 0.6 |
| pod start wait, mean (s) | 0.2 | 0.4 |
| host CPU busy, the real machine under kind (%) | 45.56 | 46.86 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1454 | 1510 |
| batch: worker machines in service after the queue finished, mean | 6 | nan |
| queue: job wait, submitted to its first pod running, mean (s) | 159.2 | 215.4 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 720.2 | 929.2 |
| queue: job turnaround, submitted to done, mean (s) | 846.5 | 914.7 |
| queue: jobs unfinished at the window's end | 10.5 | 12.5 |
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
| node-hours | 2.515 | 2.518 | +0.1% | −0.0062 to +0.0132 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 271.9 | −0.3% | −1.7010 to +0.3339 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 271.9 | −0.3% | −1.7010 to +0.3339 | no |
| response time (ms), mean | 136.2 | 116.8 | −14.3% | −28.4942 to −10.3201 | yes: GAIN |
| response time (ms), 95th percentile | 232.3 | 251.4 | +8.2% | +5.1615 to +32.8935 | yes: LOSS |
| response time (ms), 99th percentile | 338.8 | 365.5 | +7.9% | −1.4437 to +54.9525 | no |
| time over the response line (% of samples) | 0.201 | 0.2414 | +20.1% | −0.1055 to +0.1863 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.2 | +100.0% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 111.2 | +111.200 (native is 0) | +88.8205 to +133.5795 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1177 | 1323 | +12.4% | +74.1608 to +217.6159 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06086 | 0.0582 | −4.4% | −0.0046 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.461 | 1.397 | −4.4% | −0.1103 to −0.0174 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.07041 | +0.070 (native is 0) | +0.0621 to +0.0787 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.461 | 1.467 | +0.4% | −0.0373 to +0.0504 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 445.6 | 464 | +4.1% | +5.0169 to +31.7728 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.023 | 2.141 | +5.8% | −0.0777 to +0.3136 | no |
| pods started | 0.2 | 0.3 | +50.0% | −0.6113 to +0.8113 | no |
| pod start wait, total (s) | 0.4 | 0.6 | +50.0% | −1.2226 to +1.6226 | no |
| pod start wait, mean (s) | 0.2 | 0.4 | +100.0% | −0.6121 to +1.0121 | no |
| host CPU busy, the real machine under kind (%) | 45.56 | 46.86 | +2.9% | +0.6640 to +1.9343 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1454 | 1510 | +3.9% | −23.0170 to +136.0170 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 159.2 | 215.4 | +35.3% | +2.1906 to +110.2510 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 720.2 | 929.2 | +29.0% | +55.8158 to +362.1842 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 846.5 | 914.7 | +8.1% | +21.6348 to +114.8235 | yes: LOSS |
| queue: jobs unfinished at the window's end | 10.5 | 12.5 | +19.0% | +0.2157 to +3.7843 | yes: LOSS |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*