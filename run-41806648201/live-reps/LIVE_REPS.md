# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.955 |
| node-hours | 2.51 | 2.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.5 | 270.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.5 | 269.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 127.2 | 97.06 |
| response time (ms), 95th percentile | 225.2 | 212.8 |
| response time (ms), 99th percentile | 329.1 | 318.3 |
| time over the response line (% of samples) | 0.1606 | 0.1506 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1052 | 1054 |
| utilisation (used / allocatable) | 0.05905 | 0.05734 |
| CPU used (cores), mean | 1.417 | 1.367 |
| Omni's own CPU (cores), mean | 0 | 0.06867 |
| CPU used with Omni's own (cores), mean | 1.417 | 1.435 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.7 | 471.8 |
| HPA replicas, mean | 2.053 | 2.056 |
| pods started | 0.2 | 0.75 |
| pod start wait, total (s) | 0.3 | 1.75 |
| pod start wait, mean (s) | 0.3 | 0.5833 |
| host CPU busy, the real machine under kind (%) | 44.33 | 45.26 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1418 | 1433 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.25 |
| queue: job wait, submitted to its first pod running, mean (s) | 148.8 | 165.3 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 670.8 | 674.9 |
| queue: job turnaround, submitted to done, mean (s) | 779.9 | 752.3 |
| queue: jobs unfinished at the window's end | 8.5 | 7.625 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 8 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.955 | −0.8% | −0.1519 to +0.0616 | no |
| node-hours | 2.512 | 2.491 | −0.8% | −0.0616 to +0.0204 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 271.4 | 270.7 | −0.3% | −1.9579 to +0.3934 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.4 | 269.2 | −0.8% | −4.7122 to +0.3040 | no |
| response time (ms), mean | 118.8 | 97.06 | −18.3% | −27.7068 to −15.7229 | yes: GAIN |
| response time (ms), 95th percentile | 210.6 | 212.8 | +1.0% | −11.6351 to +16.0514 | no |
| response time (ms), 99th percentile | 308 | 318.3 | +3.3% | −10.8138 to +31.4363 | no |
| time over the response line (% of samples) | 0.1138 | 0.1506 | +32.3% | −0.1138 to +0.1874 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 115 | +115.000 (native is 0) | +101.5619 to +128.4381 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 964.5 | 1054 | +9.3% | +28.0038 to +151.7795 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.05861 | 0.05734 | −2.2% | −0.0035 to +0.0009 | no |
| CPU used (cores), mean | 1.407 | 1.367 | −2.8% | −0.0719 to −0.0082 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.06867 | +0.069 (native is 0) | +0.0614 to +0.0760 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.407 | 1.435 | +2.0% | −0.0017 to +0.0589 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 463.2 | 471.8 | +1.9% | −8.2101 to +25.3672 | no |
| HPA replicas, mean | 2.046 | 2.056 | +0.5% | −0.3228 to +0.3424 | no |
| pods started | 0.125 | 0.75 | +500.0% | −0.6342 to +1.8842 | no |
| pod start wait, total (s) | 0.125 | 1.75 | +1300.0% | −1.1639 to +4.4139 | no |
| pod start wait, mean (s) | 0.125 | 0.5833 | +366.7% | −0.5514 to +1.4681 | no |
| host CPU busy, the real machine under kind (%) | 43.65 | 45.26 | +3.7% | +0.3697 to +2.8503 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1397 | 1433 | +2.6% | −31.6014 to +104.3514 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.25 | −12.5% | −10.2795 to +8.7795 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 122.6 | 165.3 | +34.9% | −7.6996 to +93.1579 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 617.5 | 674.9 | +9.3% | −135.2377 to +249.9877 | no |
| queue: job turnaround, submitted to done, mean (s) | 729.9 | 752.3 | +3.1% | −19.2884 to +64.0697 | no |
| queue: jobs unfinished at the window's end | 6.5 | 7.625 | +17.3% | −1.0388 to +3.2888 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*