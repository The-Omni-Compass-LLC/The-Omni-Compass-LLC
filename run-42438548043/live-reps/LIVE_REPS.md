# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.722 |
| node-hours | 2.516 | 1.978 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 232.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 315.8 | 291.1 |
| response time (ms), 95th percentile | 1225 | 1266 |
| response time (ms), 99th percentile | 1715 | 1860 |
| time over the response line (% of samples) | 11.37 | 11.75 |
| failed requests (%) | 0 | 0.01156 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 10.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.02 | 20.49 |
| utilisation (used / allocatable) | 0.05987 | 0.07732 |
| CPU used (cores), mean | 1.437 | 1.433 |
| Omni's own CPU (cores), mean | 0 | 0.07485 |
| CPU used with Omni's own (cores), mean | 1.437 | 1.508 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.8 | 387.7 |
| HPA replicas, mean | 1.963 | 1.994 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 42.87 | 45.71 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 791.7 | 795.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 3.732 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.9292 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 2.6 |
| queue: job turnaround, submitted to done, mean (s) | 96.72 | 101.6 |
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
| worker nodes in service, mean | 6 | 4.722 | −21.3% | −1.9713 to −0.5850 | yes: GAIN |
| node-hours | 2.516 | 1.978 | −21.4% | −0.8268 to −0.2488 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.7 | 272.6 | −0.0% | −0.8920 to +0.7295 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.7 | 232.4 | −14.8% | −61.9880 to −18.5662 | yes: GAIN |
| response time (ms), mean | 315.8 | 291.1 | −7.8% | −41.0734 to −8.4816 | yes: GAIN |
| response time (ms), 95th percentile | 1225 | 1266 | +3.3% | −71.2394 to +152.2674 | no |
| response time (ms), 99th percentile | 1715 | 1860 | +8.4% | −39.2312 to +327.5178 | no |
| time over the response line (% of samples) | 11.37 | 11.75 | +3.4% | −1.4311 to +2.1996 | no |
| failed requests (%) | 0 | 0.01156 | +0.012 (native is 0) | −0.0146 to +0.0377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.8 | 10.2 | +15.9% | −0.2588 to +3.0588 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 95.4 | +95.400 (native is 0) | +44.6191 to +146.1809 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 20.02 | 20.49 | +2.3% | −2.2705 to +3.2038 | no |
| utilisation (used / allocatable) | 0.05987 | 0.07732 | +29.2% | +0.0066 to +0.0283 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.437 | 1.433 | −0.3% | −0.0389 to +0.0314 | no |
| Omni's own CPU (cores), mean | 0 | 0.07485 | +0.075 (native is 0) | +0.0682 to +0.0815 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.437 | 1.508 | +4.9% | +0.0346 to +0.1076 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 459.8 | 387.7 | −15.7% | −116.0772 to −28.1907 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.963 | 1.994 | +1.6% | −0.0991 to +0.1606 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 42.87 | 45.71 | +6.6% | +2.3476 to +3.3481 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 791.7 | 795.4 | +0.5% | −1.5461 to +8.9461 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 3.732 | −37.8% | −3.2373 to −1.2992 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.7792 | 0.9292 | +19.3% | −0.0613 to +0.3613 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.5 | 2.6 | +73.3% | −1.0179 to +3.2179 | no |
| queue: job turnaround, submitted to done, mean (s) | 96.72 | 101.6 | +5.0% | −0.2077 to +9.8744 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*