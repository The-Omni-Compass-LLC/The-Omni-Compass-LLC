# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.987 |
| node-hours | 2.513 | 2.508 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 137.2 | 102.5 |
| response time (ms), 95th percentile | 238.5 | 228.2 |
| response time (ms), 99th percentile | 339.6 | 336.4 |
| time over the response line (% of samples) | 0.1544 | 0.2093 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1149 | 1121 |
| utilisation (used / allocatable) | 0.05967 | 0.05935 |
| CPU used (cores), mean | 1.432 | 1.421 |
| Omni's own CPU (cores), mean | 0 | 0.01175 |
| CPU used with Omni's own (cores), mean | 1.432 | 1.433 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.4 | 455.8 |
| HPA replicas, mean | 2.067 | 1.99 |
| pods started | 0 | 0.2 |
| pod start wait, total (s) | 0 | 0.5 |
| pod start wait, mean (s) | 0 | 0.25 |
| host CPU busy, the real machine under kind (%) | 45.09 | 44.83 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1455 | 1471 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.667 |
| queue: job wait, submitted to its first pod running, mean (s) | 137.5 | 176.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 645.1 | 739.7 |
| queue: job turnaround, submitted to done, mean (s) | 848.6 | 831.6 |
| queue: jobs unfinished at the window's end | 11.1 | 10.2 |
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
| worker nodes in service, mean | 6 | 5.987 | −0.2% | −0.0420 to +0.0163 | no |
| node-hours | 2.513 | 2.508 | −0.2% | −0.0194 to +0.0086 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.5 | −0.1% | −0.9552 to +0.4660 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 271.1 | −0.2% | −2.0289 to +0.7272 | no |
| response time (ms), mean | 137.2 | 102.5 | −25.3% | −41.1601 to −28.3346 | yes: GAIN |
| response time (ms), 95th percentile | 238.5 | 228.2 | −4.3% | −21.6399 to +0.9509 | no |
| response time (ms), 99th percentile | 339.6 | 336.4 | −0.9% | −30.3103 to +23.9363 | no |
| time over the response line (% of samples) | 0.1544 | 0.2093 | +35.5% | −0.0868 to +0.1965 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.7 | +14.700 (native is 0) | +10.9900 to +18.4100 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1149 | 1121 | −2.5% | −80.7776 to +24.3209 | no |
| utilisation (used / allocatable) | 0.05967 | 0.05935 | −0.5% | −0.0015 to +0.0009 | no |
| CPU used (cores), mean | 1.432 | 1.421 | −0.7% | −0.0413 to +0.0200 | no |
| Omni's own CPU (cores), mean | 0 | 0.01175 | +0.012 (native is 0) | +0.0105 to +0.0130 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.432 | 1.433 | +0.1% | −0.0298 to +0.0320 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 453.4 | 455.8 | +0.5% | −6.0092 to +10.8999 | no |
| HPA replicas, mean | 2.067 | 1.99 | −3.7% | −0.1963 to +0.0425 | no |
| pods started | 0 | 0.2 | +0.200 (native is 0) | −0.2524 to +0.6524 | no |
| pod start wait, total (s) | 0 | 0.5 | +0.500 (native is 0) | −0.6310 to +1.6310 | no |
| pod start wait, mean (s) | 0 | 0.25 | +0.250 (native is 0) | −0.3155 to +0.8155 | no |
| host CPU busy, the real machine under kind (%) | 45.09 | 44.83 | −0.6% | −0.8314 to +0.3187 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1455 | 1471 | +1.1% | −12.5052 to +44.7052 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.667 | −5.6% | −4.5687 to +3.9020 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 137.5 | 176.2 | +28.1% | −3.2024 to +80.5274 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 645.1 | 739.7 | +14.7% | −65.6842 to +254.8842 | no |
| queue: job turnaround, submitted to done, mean (s) | 848.6 | 831.6 | −2.0% | −67.1821 to +33.2154 | no |
| queue: jobs unfinished at the window's end | 11.1 | 10.2 | −8.1% | −2.6986 to +0.8986 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*