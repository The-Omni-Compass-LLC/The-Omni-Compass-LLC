# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.972 |
| node-hours | 2.511 | 2.503 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 270.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 128.9 | 98.35 |
| response time (ms), 95th percentile | 228.9 | 222.6 |
| response time (ms), 99th percentile | 328.2 | 336.3 |
| time over the response line (% of samples) | 0.1694 | 0.2015 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1134 | 1184 |
| utilisation (used / allocatable) | 0.05843 | 0.059 |
| CPU used (cores), mean | 1.402 | 1.41 |
| Omni's own CPU (cores), mean | 0 | 0.01271 |
| CPU used with Omni's own (cores), mean | 1.402 | 1.423 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 459.6 |
| HPA replicas, mean | 2.037 | 2.009 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.2 |
| pod start wait, mean (s) | 0.2 | 0.2 |
| host CPU busy, the real machine under kind (%) | 43.97 | 45.12 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1389 | 1436 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.692 |
| queue: job wait, submitted to its first pod running, mean (s) | 144.4 | 126.2 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 603.5 | 602.7 |
| queue: job turnaround, submitted to done, mean (s) | 810.2 | 846.2 |
| queue: jobs unfinished at the window's end | 11.2 | 11.2 |

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
| worker nodes in service, mean | 6 | 5.972 | −0.5% | −0.0836 to +0.0276 | no |
| node-hours | 2.511 | 2.503 | −0.3% | −0.0289 to +0.0124 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.2 | 271.8 | +0.2% | −0.3926 to +1.5861 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.2 | 270.9 | −0.1% | −1.6538 to +1.0806 | no |
| response time (ms), mean | 128.9 | 98.35 | −23.7% | −39.6884 to −21.5041 | yes: GAIN |
| response time (ms), 95th percentile | 228.9 | 222.6 | −2.8% | −16.9025 to +4.3115 | no |
| response time (ms), 99th percentile | 328.2 | 336.3 | +2.5% | −10.8881 to +27.0337 | no |
| time over the response line (% of samples) | 0.1694 | 0.2015 | +18.9% | −0.0923 to +0.1565 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.3 | +13.300 (native is 0) | +9.3814 to +17.2186 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1134 | 1184 | +4.4% | −24.3655 to +123.6321 | no |
| utilisation (used / allocatable) | 0.05843 | 0.059 | +1.0% | −0.0014 to +0.0026 | no |
| CPU used (cores), mean | 1.402 | 1.41 | +0.5% | −0.0368 to +0.0521 | no |
| Omni's own CPU (cores), mean | 0 | 0.01271 | +0.013 (native is 0) | +0.0113 to +0.0141 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.402 | 1.423 | +1.5% | −0.0240 to +0.0647 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 464 | 459.6 | −1.0% | −18.4679 to +9.6279 | no |
| HPA replicas, mean | 2.037 | 2.009 | −1.4% | −0.2010 to +0.1455 | no |
| pods started | 0.1 | 0.1 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0.2 | 0.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0.2 | 0.2 | ±0.0% | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 43.97 | 45.12 | +2.6% | +0.2378 to +2.0631 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1389 | 1436 | +3.4% | −12.8266 to +106.6266 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.692 | −5.1% | −1.1027 to +0.4862 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 144.4 | 126.2 | −12.6% | −52.6268 to +16.3434 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 603.5 | 602.7 | −0.1% | −139.3588 to +137.7588 | no |
| queue: job turnaround, submitted to done, mean (s) | 810.2 | 846.2 | +4.4% | −16.9275 to +88.9025 | no |
| queue: jobs unfinished at the window's end | 11.2 | 11.2 | ±0.0% | −2.0511 to +2.0511 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*