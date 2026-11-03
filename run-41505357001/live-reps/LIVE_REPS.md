# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.991 |
| node-hours | 2.514 | 2.092 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 241 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 406.3 | 384.8 |
| response time (ms), 95th percentile | 1474 | 1592 |
| response time (ms), 99th percentile | 2063 | 2249 |
| time over the response line (% of samples) | 17.77 | 17.56 |
| failed requests (%) | 0 | 0.01111 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.8 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.75 | 17.26 |
| utilisation (used / allocatable) | 0.06057 | 0.07254 |
| CPU used (cores), mean | 1.454 | 1.444 |
| Omni's own CPU (cores), mean | 0 | 0.06844 |
| CPU used with Omni's own (cores), mean | 1.454 | 1.513 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.4 | 409.7 |
| HPA replicas, mean | 2.036 | 2.625 |
| pods started | 0 | 2.3 |
| pod start wait, total (s) | 0 | 5.6 |
| pod start wait, mean (s) | 0 | 1.7 |
| host CPU busy, the real machine under kind (%) | 41.32 | 44.25 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 812.3 | 822.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.515 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2917 | 0.3708 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 2.1 |
| queue: job turnaround, submitted to done, mean (s) | 118.8 | 127 |
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
| worker nodes in service, mean | 6 | 4.991 | −16.8% | −1.9765 to −0.0411 | yes: GAIN |
| node-hours | 2.514 | 2.092 | −16.8% | −0.8281 to −0.0157 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.8 | +0.1% | −0.8424 to +1.2231 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 241 | −11.6% | −62.5809 to −0.5760 | yes: GAIN |
| response time (ms), mean | 406.3 | 384.8 | −5.3% | −42.3370 to −0.6222 | yes: GAIN |
| response time (ms), 95th percentile | 1474 | 1592 | +8.0% | −35.7626 to +272.3576 | no |
| response time (ms), 99th percentile | 2063 | 2249 | +9.0% | −75.4970 to +447.4274 | no |
| time over the response line (% of samples) | 17.77 | 17.56 | −1.2% | −0.7129 to +0.2992 | no |
| failed requests (%) | 0 | 0.01111 | +0.011 (native is 0) | −0.0140 to +0.0362 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.9 | 9.5 | +6.7% | −0.7572 to +1.9572 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 114.8 | +114.800 (native is 0) | +54.6539 to +174.9461 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 14.75 | 17.26 | +17.0% | −0.3419 to +5.3619 | no |
| utilisation (used / allocatable) | 0.06057 | 0.07254 | +19.8% | +0.0018 to +0.0222 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.454 | 1.444 | −0.6% | −0.0585 to +0.0397 | no |
| Omni's own CPU (cores), mean | 0 | 0.06844 | +0.068 (native is 0) | +0.0607 to +0.0762 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.454 | 1.513 | +4.1% | +0.0035 to +0.1145 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 473.4 | 409.7 | −13.4% | −120.2748 to −7.0543 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.036 | 2.625 | +28.9% | +0.2902 to +0.8867 | yes: power given |
| pods started | 0 | 2.3 | +2.300 (native is 0) | +1.0819 to +3.5181 | yes: power given |
| pod start wait, total (s) | 0 | 5.6 | +5.600 (native is 0) | +2.5428 to +8.6572 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.7 | +1.700 (native is 0) | +0.8176 to +2.5824 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 41.32 | 44.25 | +7.1% | +2.4510 to +3.4119 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 812.3 | 822.3 | +1.2% | +1.7956 to +18.2044 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.515 | −24.7% | −2.7913 to −0.1780 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.2917 | 0.3708 | +27.1% | −0.1502 to +0.3085 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 2.1 | 2.1 | ±0.0% | −0.8921 to +0.8921 | no |
| queue: job turnaround, submitted to done, mean (s) | 118.8 | 127 | +6.9% | −0.5387 to +16.8887 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*