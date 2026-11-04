# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.954 |
| node-hours | 2.51 | 2.073 |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 240.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 451.6 | 450.2 |
| response time (ms), 95th percentile | 1720 | 1931 |
| response time (ms), 99th percentile | 2411 | 2615 |
| time over the response line (% of samples) | 19.64 | 20.16 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 11 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 12.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.31 | 15.81 |
| utilisation (used / allocatable) | 0.06278 | 0.07715 |
| CPU used (cores), mean | 1.507 | 1.524 |
| Omni's own CPU (cores), mean | 0 | 0.0779 |
| CPU used with Omni's own (cores), mean | 1.507 | 1.602 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.3 | 381.3 |
| HPA replicas, mean | 1.93 | 2.281 |
| pods started | 0.1 | 1.5 |
| pod start wait, total (s) | 0.3 | 3.2 |
| pod start wait, mean (s) | 0.3 | 1.093 |
| host CPU busy, the real machine under kind (%) | 44.17 | 47.53 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 818.4 | 830.6 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.084 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4417 | 0.9833 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.4 | 7.4 |
| queue: job turnaround, submitted to done, mean (s) | 122.4 | 134.1 |
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
| worker nodes in service, mean | 6 | 4.954 | −17.4% | −1.7104 to −0.3814 | yes: GAIN |
| node-hours | 2.51 | 2.073 | −17.4% | −0.7162 to −0.1584 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.2 | +0.1% | −0.5444 to +1.0612 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 240.5 | −11.9% | −53.6230 to −11.4268 | yes: GAIN |
| response time (ms), mean | 451.6 | 450.2 | −0.3% | −15.2203 to +12.3996 | no |
| response time (ms), 95th percentile | 1720 | 1931 | +12.3% | +87.1777 to +335.1613 | yes: LOSS |
| response time (ms), 99th percentile | 2411 | 2615 | +8.4% | −31.2963 to +438.0809 | no |
| time over the response line (% of samples) | 19.64 | 20.16 | +2.6% | −0.7712 to +1.8107 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.2 | 11 | +7.8% | +0.0612 to +1.5388 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110.3 | +110.300 (native is 0) | +36.9795 to +183.6205 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.31 | 15.81 | +28.4% | +0.8491 to +6.1509 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06278 | 0.07715 | +22.9% | +0.0055 to +0.0232 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.507 | 1.524 | +1.1% | −0.0509 to +0.0852 | no |
| Omni's own CPU (cores), mean | 0 | 0.0779 | +0.078 (native is 0) | +0.0702 to +0.0856 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.507 | 1.602 | +6.3% | +0.0251 to +0.1649 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 451.3 | 381.3 | −15.5% | −126.4856 to −13.5239 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.93 | 2.281 | +18.2% | +0.0743 to +0.6276 | yes: power given |
| pods started | 0.1 | 1.5 | +1400.0% | +0.0428 to +2.7572 | yes: power given |
| pod start wait, total (s) | 0.3 | 3.2 | +966.7% | −0.0290 to +5.8290 | no |
| pod start wait, mean (s) | 0.3 | 1.093 | +264.4% | −0.4618 to +2.0485 | no |
| host CPU busy, the real machine under kind (%) | 44.17 | 47.53 | +7.6% | +2.8370 to +3.8873 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 818.4 | 830.6 | +1.5% | +3.8052 to +20.5948 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.084 | −31.9% | −2.8993 to −0.9322 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.4417 | 0.9833 | +122.6% | −0.0118 to +1.0952 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 3.4 | 7.4 | +117.6% | −1.0242 to +9.0242 | no |
| queue: job turnaround, submitted to done, mean (s) | 122.4 | 134.1 | +9.6% | +4.0758 to +19.3409 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*