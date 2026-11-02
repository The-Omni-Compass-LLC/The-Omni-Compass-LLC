# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.891 |
| node-hours | 2.513 | 2.053 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 275.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 240.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 562.5 | 520.3 |
| response time (ms), 95th percentile | 3096 | 3151 |
| response time (ms), 99th percentile | 4184 | 4179 |
| time over the response line (% of samples) | 18.04 | 17.8 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 202.4 | 208.9 |
| utilisation (used / allocatable) | 0.06601 | 0.08108 |
| CPU used (cores), mean | 1.584 | 1.577 |
| Omni's own CPU (cores), mean | 0 | 0.0824 |
| CPU used with Omni's own (cores), mean | 1.584 | 1.66 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.8 | 364.5 |
| HPA replicas, mean | 2.224 | 2.203 |
| pods started | 0 | 0 |
| pod start wait, total (s) | 0 | 0 |
| pod start wait, mean (s) | 0 | 0 |
| host CPU busy, the real machine under kind (%) | 45.96 | 48.69 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 625.8 | 646.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.086 |
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
| worker nodes in service, mean | 6 | 4.891 | −18.5% | −1.5370 to −0.6814 | yes: GAIN |
| node-hours | 2.513 | 2.053 | −18.3% | −0.6392 to −0.2806 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.5 | 275.3 | +0.3% | −0.2614 to +1.8180 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.5 | 240.4 | −12.4% | −47.6758 to −20.6551 | yes: GAIN |
| response time (ms), mean | 562.5 | 520.3 | −7.5% | −58.2390 to −26.0500 | yes: GAIN |
| response time (ms), 95th percentile | 3096 | 3151 | +1.8% | −48.6159 to +160.3289 | no |
| response time (ms), 99th percentile | 4184 | 4179 | −0.1% | −145.8213 to +134.9153 | no |
| time over the response line (% of samples) | 18.04 | 17.8 | −1.3% | −0.7374 to +0.2710 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.8 | 11 | +1.9% | −0.1016 to +0.5016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 9.9 | +9.900 (native is 0) | +8.7102 to +11.0898 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 202.4 | 208.9 | +3.2% | +1.1973 to +11.7794 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06601 | 0.08108 | +22.8% | +0.0091 to +0.0210 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.584 | 1.577 | −0.4% | −0.0406 to +0.0264 | no |
| Omni's own CPU (cores), mean | 0 | 0.0824 | +0.082 (native is 0) | +0.0748 to +0.0900 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.584 | 1.66 | +4.8% | +0.0444 to +0.1062 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 417.8 | 364.5 | −12.8% | −76.5605 to −30.0377 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.224 | 2.203 | −1.0% | −0.2712 to +0.2278 | no |
| pods started | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, total (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pod start wait, mean (s) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| host CPU busy, the real machine under kind (%) | 45.96 | 48.69 | +5.9% | +2.2086 to +3.2433 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 625.8 | 646.3 | +3.3% | +12.0414 to +28.9586 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.086 | −31.9% | −2.5872 to −1.2410 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*