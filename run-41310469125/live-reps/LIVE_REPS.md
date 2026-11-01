# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.893 |
| node-hours | 2.517 | 2.049 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 272.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 238.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 385.3 | 358 |
| response time (ms), 95th percentile | 1456 | 1519 |
| response time (ms), 99th percentile | 2120 | 2118 |
| time over the response line (% of samples) | 16.87 | 16.4 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.98 | 10.75 |
| utilisation (used / allocatable) | 0.06207 | 0.07632 |
| CPU used (cores), mean | 1.49 | 1.466 |
| Omni's own CPU (cores), mean | 0 | 0.01665 |
| CPU used with Omni's own (cores), mean | 1.49 | 1.483 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.9 | 389.9 |
| HPA replicas, mean | 2.051 | 2.139 |
| pods started | 0.4 | 0.6 |
| pod start wait, total (s) | 0.8 | 0.9 |
| pod start wait, mean (s) | 0.6 | 0.55 |
| host CPU busy, the real machine under kind (%) | 42.1 | 43.18 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 802.5 | 804.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.166 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.05833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 109.6 |
| queue: jobs unfinished at the window's end | 0 | 0 |
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
| worker nodes in service, mean | 6 | 4.893 | −18.5% | −1.9755 to −0.2391 | yes: GAIN |
| node-hours | 2.517 | 2.049 | −18.6% | −0.8269 to −0.1092 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.5 | 272.9 | −0.2% | −1.4164 to +0.2220 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.5 | 238.1 | −13.0% | −62.1317 to −8.7168 | yes: GAIN |
| response time (ms), mean | 385.3 | 358 | −7.1% | −38.3763 to −16.2560 | yes: GAIN |
| response time (ms), 95th percentile | 1456 | 1519 | +4.3% | +24.6115 to +100.3265 | yes: LOSS |
| response time (ms), 99th percentile | 2120 | 2118 | −0.1% | −129.9584 to +125.9506 | no |
| time over the response line (% of samples) | 16.87 | 16.4 | −2.8% | −1.2382 to +0.2853 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.9 | 8.4 | +6.3% | −0.1952 to +1.1952 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 43.7 | +43.700 (native is 0) | +22.7121 to +64.6879 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 10.98 | 10.75 | −2.1% | −1.0968 to +0.6368 | no |
| utilisation (used / allocatable) | 0.06207 | 0.07632 | +23.0% | +0.0024 to +0.0261 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.49 | 1.466 | −1.6% | −0.0411 to −0.0058 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01665 | +0.017 (native is 0) | +0.0151 to +0.0182 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.49 | 1.483 | −0.5% | −0.0252 to +0.0117 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 450.9 | 389.9 | −13.5% | −112.1866 to −9.7597 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.051 | 2.139 | +4.3% | −0.1749 to +0.3512 | no |
| pods started | 0.4 | 0.6 | +50.0% | −0.6121 to +1.0121 | no |
| pod start wait, total (s) | 0.8 | 0.9 | +12.5% | −1.3871 to +1.5871 | no |
| pod start wait, mean (s) | 0.6 | 0.55 | −8.3% | −0.8488 to +0.7488 | no |
| host CPU busy, the real machine under kind (%) | 42.1 | 43.18 | +2.6% | +0.6452 to +1.5149 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 802.5 | 804.2 | +0.2% | −2.3751 to +5.7751 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.166 | −30.6% | −3.1799 to −0.4884 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.075 | 0.05833 | −22.2% | −0.1057 to +0.0724 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.4 | 0.4 | ±0.0% | −0.5840 to +0.5840 | no |
| queue: job turnaround, submitted to done, mean (s) | 108.3 | 109.6 | +1.2% | −0.9031 to +3.5281 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*