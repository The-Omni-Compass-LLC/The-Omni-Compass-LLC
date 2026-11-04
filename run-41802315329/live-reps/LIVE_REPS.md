# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.676 |
| node-hours | 2.515 | 2.38 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 264.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 495 | 485.1 |
| response time (ms), 95th percentile | 1895 | 2055 |
| response time (ms), 99th percentile | 2618 | 2914 |
| time over the response line (% of samples) | 21 | 21.09 |
| failed requests (%) | 0.01111 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.17 | 17.54 |
| utilisation (used / allocatable) | 0.06614 | 0.07069 |
| CPU used (cores), mean | 1.587 | 1.605 |
| Omni's own CPU (cores), mean | 0 | 0.07794 |
| CPU used with Omni's own (cores), mean | 1.587 | 1.683 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.1 | 400.1 |
| HPA replicas, mean | 1.973 | 2.354 |
| pods started | 0.1 | 1 |
| pod start wait, total (s) | 0.2 | 2 |
| pod start wait, mean (s) | 0.2 | 1.25 |
| host CPU busy, the real machine under kind (%) | 45.54 | 48.85 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 832.7 | 842.8 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.32 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.9375 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.8 |
| queue: job turnaround, submitted to done, mean (s) | 134.9 | 146.4 |
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
| worker nodes in service, mean | 6 | 5.676 | −5.4% | −0.6282 to −0.0191 | yes: GAIN |
| node-hours | 2.515 | 2.38 | −5.3% | −0.2658 to −0.0029 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275.1 | +0.2% | −0.4400 to +1.3430 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 264.9 | −3.5% | −19.6446 to +0.2434 | no |
| response time (ms), mean | 495 | 485.1 | −2.0% | −28.1334 to +8.2943 | no |
| response time (ms), 95th percentile | 1895 | 2055 | +8.4% | +7.8432 to +312.3988 | yes: LOSS |
| response time (ms), 99th percentile | 2618 | 2914 | +11.3% | +6.2483 to +585.2045 | yes: LOSS |
| time over the response line (% of samples) | 21 | 21.09 | +0.4% | −0.4092 to +0.5941 | no |
| failed requests (%) | 0.01111 | 0 | −100.0% | −0.0362 to +0.0140 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.3 | 11.7 | +3.5% | −0.6228 to +1.4228 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 91.2 | +91.200 (native is 0) | +31.8196 to +150.5804 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.17 | 17.54 | +33.1% | −0.3565 to +9.0898 | no |
| utilisation (used / allocatable) | 0.06614 | 0.07069 | +6.9% | +0.0009 to +0.0081 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.587 | 1.605 | +1.1% | −0.0009 to +0.0370 | no |
| Omni's own CPU (cores), mean | 0 | 0.07794 | +0.078 (native is 0) | +0.0726 to +0.0833 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.587 | 1.683 | +6.0% | +0.0762 to +0.1158 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 421.1 | 400.1 | −5.0% | −38.4937 to −3.4620 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.973 | 2.354 | +19.3% | +0.1998 to +0.5619 | yes: power given |
| pods started | 0.1 | 1 | +900.0% | +0.2737 to +1.5263 | yes: power given |
| pod start wait, total (s) | 0.2 | 2 | +900.0% | +0.5474 to +3.0526 | yes: LOSS |
| pod start wait, mean (s) | 0.2 | 1.25 | +525.0% | +0.2336 to +1.8664 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.54 | 48.85 | +7.2% | +2.9058 to +3.6948 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 832.7 | 842.8 | +1.2% | +0.4886 to +19.7114 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 5.32 | −11.3% | −1.2921 to −0.0674 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1333 | 0.9375 | +603.1% | −0.6847 to +2.2931 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.7 | 2.8 | +300.0% | −1.2796 to +5.4796 | no |
| queue: job turnaround, submitted to done, mean (s) | 134.9 | 146.4 | +8.5% | +3.4809 to +19.4024 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*