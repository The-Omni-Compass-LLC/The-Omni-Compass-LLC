# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.731 |
| node-hours | 2.517 | 2.398 |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 275.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 266.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 515.6 | 466.3 |
| response time (ms), 95th percentile | 2386 | 2374 |
| response time (ms), 99th percentile | 3472 | 3425 |
| time over the response line (% of samples) | 20.42 | 19.96 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 13.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.87 | 16.48 |
| utilisation (used / allocatable) | 0.06893 | 0.0725 |
| CPU used (cores), mean | 1.654 | 1.657 |
| Omni's own CPU (cores), mean | 0 | 0.01607 |
| CPU used with Omni's own (cores), mean | 1.654 | 1.673 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.5 | 386.7 |
| HPA replicas, mean | 2.061 | 2.265 |
| pods started | 0 | 0.8 |
| pod start wait, total (s) | 0 | 1 |
| pod start wait, mean (s) | 0 | 1 |
| host CPU busy, the real machine under kind (%) | 47.28 | 48.16 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 856.8 | 859.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.53 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.2458 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 |
| queue: job turnaround, submitted to done, mean (s) | 166.5 | 166.4 |
| queue: jobs unfinished at the window's end | 0 | 0 |

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
| worker nodes in service, mean | 6 | 5.731 | −4.5% | −0.7856 to +0.2466 | no |
| node-hours | 2.517 | 2.398 | −4.7% | −0.3365 to +0.0986 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 275.4 | −0.2% | −1.3825 to +0.1013 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 266.9 | −3.3% | −25.5700 to +7.3430 | no |
| response time (ms), mean | 515.6 | 466.3 | −9.6% | −74.0190 to −24.5737 | yes: GAIN |
| response time (ms), 95th percentile | 2386 | 2374 | −0.5% | −220.8224 to +195.9864 | no |
| response time (ms), 99th percentile | 3472 | 3425 | −1.3% | −247.6810 to +153.9552 | no |
| time over the response line (% of samples) | 20.42 | 19.96 | −2.2% | −2.0531 to +1.1483 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 13 | 13.1 | +0.8% | −0.3060 to +0.5060 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 20.3 | +20.300 (native is 0) | +12.7672 to +27.8328 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.87 | 16.48 | +10.8% | −0.1302 to +3.3536 | no |
| utilisation (used / allocatable) | 0.06893 | 0.0725 | +5.2% | −0.0031 to +0.0102 | no |
| CPU used (cores), mean | 1.654 | 1.657 | +0.1% | −0.0175 to +0.0222 | no |
| Omni's own CPU (cores), mean | 0 | 0.01607 | +0.016 (native is 0) | +0.0152 to +0.0169 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.654 | 1.673 | +1.1% | −0.0012 to +0.0380 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 403.5 | 386.7 | −4.2% | −47.4740 to +13.8716 | no |
| HPA replicas, mean | 2.061 | 2.265 | +9.9% | +0.0207 to +0.3873 | yes: power given |
| pods started | 0 | 0.8 | +0.800 (native is 0) | +0.4984 to +1.1016 | yes: power given |
| pod start wait, total (s) | 0 | 1 | +1.000 (native is 0) | +0.5231 to +1.4769 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1 | +1.000 (native is 0) | +0.5231 to +1.4769 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 47.28 | 48.16 | +1.9% | +0.4765 to +1.2939 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 856.8 | 859.4 | +0.3% | −1.9765 to +7.1765 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.53 | −7.8% | −1.3505 to +0.4100 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1625 | 0.2458 | +51.3% | −0.2039 to +0.3706 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 0.9 | +28.6% | −0.5388 to +0.9388 | no |
| queue: job turnaround, submitted to done, mean (s) | 166.5 | 166.4 | −0.1% | −5.9503 to +5.7419 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*