# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.985 |
| node-hours | 2.518 | 2.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 135.5 | 106.9 |
| response time (ms), 95th percentile | 236.1 | 235.4 |
| response time (ms), 99th percentile | 348 | 349.9 |
| time over the response line (% of samples) | 0.2006 | 0.2694 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.6 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1206 | 1210 |
| utilisation (used / allocatable) | 0.06024 | 0.05912 |
| CPU used (cores), mean | 1.446 | 1.416 |
| Omni's own CPU (cores), mean | 0 | 0.01254 |
| CPU used with Omni's own (cores), mean | 1.446 | 1.428 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.9 | 458.1 |
| HPA replicas, mean | 1.976 | 2.004 |
| pods started | 0.1 | 0.1 |
| pod start wait, total (s) | 0.2 | 0.1 |
| pod start wait, mean (s) | 0.2 | 0.1 |
| host CPU busy, the real machine under kind (%) | 45.05 | 45.08 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1453 | 1455 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.625 |
| queue: job wait, submitted to its first pod running, mean (s) | 144.9 | 144.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 622.1 | 708.9 |
| queue: job turnaround, submitted to done, mean (s) | 874.7 | 877.4 |
| queue: jobs unfinished at the window's end | 12.3 | 12.1 |
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
| worker nodes in service, mean | 6 | 5.985 | −0.3% | −0.0425 to +0.0121 | no |
| node-hours | 2.518 | 2.515 | −0.1% | −0.0163 to +0.0110 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.5 | 272.5 | +0.0% | −1.0615 to +1.1616 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.5 | 272.1 | −0.2% | −2.0137 to +1.1596 | no |
| response time (ms), mean | 135.5 | 106.9 | −21.1% | −39.7614 to −17.3407 | yes: GAIN |
| response time (ms), 95th percentile | 236.1 | 235.4 | −0.3% | −13.4470 to +12.1380 | no |
| response time (ms), 99th percentile | 348 | 349.9 | +0.6% | −9.0167 to +12.9085 | no |
| time over the response line (% of samples) | 0.2006 | 0.2694 | +34.3% | +0.0143 to +0.1233 | yes: LOSS |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0.1 | +0.100 (native is 0) | −0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 13.6 | +13.600 (native is 0) | +9.8572 to +17.3428 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1206 | 1210 | +0.3% | −57.4799 to +65.5599 | no |
| utilisation (used / allocatable) | 0.06024 | 0.05912 | −1.9% | −0.0029 to +0.0006 | no |
| CPU used (cores), mean | 1.446 | 1.416 | −2.1% | −0.0739 to +0.0137 | no |
| Omni's own CPU (cores), mean | 0 | 0.01254 | +0.013 (native is 0) | +0.0114 to +0.0137 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.446 | 1.428 | −1.2% | −0.0611 to +0.0260 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 449.9 | 458.1 | +1.8% | −4.1951 to +20.6818 | no |
| HPA replicas, mean | 1.976 | 2.004 | +1.4% | −0.0741 to +0.1299 | no |
| pods started | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| pod start wait, total (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| pod start wait, mean (s) | 0.2 | 0.1 | −50.0% | −0.6278 to +0.4278 | no |
| host CPU busy, the real machine under kind (%) | 45.05 | 45.08 | +0.1% | −0.6384 to +0.6927 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1453 | 1455 | +0.1% | −7.2536 to +10.6536 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.625 | −6.2% | −2.5985 to +1.8485 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 144.9 | 144.3 | −0.4% | −28.1474 to +26.8807 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 622.1 | 708.9 | +14.0% | −65.1761 to +238.7761 | no |
| queue: job turnaround, submitted to done, mean (s) | 874.7 | 877.4 | +0.3% | −42.5304 to +47.7721 | no |
| queue: jobs unfinished at the window's end | 12.3 | 12.1 | −1.6% | −2.0407 to +1.6407 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*