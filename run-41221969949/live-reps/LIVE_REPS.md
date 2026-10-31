# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.802 |
| node-hours | 2.513 | 2.015 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 235.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 401.2 | 371.3 |
| response time (ms), 95th percentile | 1549 | 1551 |
| response time (ms), 99th percentile | 2131 | 2198 |
| time over the response line (% of samples) | 16.81 | 16.5 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.81 | 12.91 |
| utilisation (used / allocatable) | 0.06112 | 0.07495 |
| CPU used (cores), mean | 1.467 | 1.429 |
| Omni's own CPU (cores), mean | 0 | 0.01597 |
| CPU used with Omni's own (cores), mean | 1.467 | 1.445 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 398.7 |
| HPA replicas, mean | 1.941 | 2.012 |
| pods started | 0.2 | 0.2 |
| pod start wait, total (s) | 0.6 | 0.3 |
| pod start wait, mean (s) | 0.3 | 0.3 |
| host CPU busy, the real machine under kind (%) | 41.71 | 42.46 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 808.6 | 810.4 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.074 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.2875 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 2.5 |
| queue: job turnaround, submitted to done, mean (s) | 114 | 115.9 |
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
| worker nodes in service, mean | 6 | 4.802 | −20.0% | −2.1202 to −0.2761 | yes: GAIN |
| node-hours | 2.513 | 2.015 | −19.8% | −0.8877 to −0.1075 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.6 | 272.7 | +0.0% | −0.8099 to +1.0700 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.6 | 235.1 | −13.8% | −67.0529 to −7.9328 | yes: GAIN |
| response time (ms), mean | 401.2 | 371.3 | −7.4% | −49.9456 to −9.8028 | yes: GAIN |
| response time (ms), 95th percentile | 1549 | 1551 | +0.1% | −101.7939 to +104.7339 | no |
| response time (ms), 99th percentile | 2131 | 2198 | +3.1% | −60.6204 to +193.3982 | no |
| time over the response line (% of samples) | 16.81 | 16.5 | −1.8% | −0.7746 to +0.1721 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 8.1 | +6.6% | −0.4079 to +1.4079 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 35.9 | +35.900 (native is 0) | +18.8008 to +52.9992 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 12.81 | 12.9 | +0.8% | −1.2502 to +1.4435 | no |
| utilisation (used / allocatable) | 0.06112 | 0.07495 | +22.6% | +0.0027 to +0.0250 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.467 | 1.429 | −2.6% | −0.0723 to −0.0034 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01597 | +0.016 (native is 0) | +0.0142 to +0.0177 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.467 | 1.445 | −1.5% | −0.0574 to +0.0136 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 465 | 398.7 | −14.3% | −119.8938 to −12.7666 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.941 | 2.012 | +3.7% | −0.0731 to +0.2155 | no |
| pods started | 0.2 | 0.2 | ±0.0% | −0.5840 to +0.5840 | no |
| pod start wait, total (s) | 0.6 | 0.3 | −50.0% | −1.8099 to +1.2099 | no |
| pod start wait, mean (s) | 0.3 | 0.3 | ±0.0% | −0.8921 to +0.8921 | no |
| host CPU busy, the real machine under kind (%) | 41.71 | 42.46 | +1.8% | +0.4473 to +1.0434 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 808.6 | 810.4 | +0.2% | −2.7089 to +6.3089 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.074 | −32.1% | −3.3860 to −0.4650 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.1833 | 0.2875 | +56.8% | −0.0748 to +0.2831 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 0.8 | 2.5 | +212.5% | −1.3730 to +4.7730 | no |
| queue: job turnaround, submitted to done, mean (s) | 114 | 115.9 | +1.7% | −3.6866 to +7.4866 | no |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*