# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.423 |
| node-hours | 2.516 | 2.27 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 255.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 440 | 420 |
| response time (ms), 95th percentile | 1592 | 1731 |
| response time (ms), 99th percentile | 2263 | 2418 |
| time over the response line (% of samples) | 19.88 | 20.1 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 11.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.83 | 16.52 |
| utilisation (used / allocatable) | 0.06477 | 0.07255 |
| CPU used (cores), mean | 1.554 | 1.564 |
| Omni's own CPU (cores), mean | 0 | 0.07479 |
| CPU used with Omni's own (cores), mean | 1.554 | 1.639 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.5 | 396.1 |
| HPA replicas, mean | 2.025 | 2.362 |
| pods started | 0 | 1.3 |
| pod start wait, total (s) | 0 | 3.2 |
| pod start wait, mean (s) | 0 | 1.25 |
| host CPU busy, the real machine under kind (%) | 44.54 | 47.71 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 816.8 | 825.3 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.854 |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3042 | 0.3667 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2.4 |
| queue: job turnaround, submitted to done, mean (s) | 122.1 | 130.5 |
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
| worker nodes in service, mean | 6 | 5.423 | −9.6% | −1.0883 to −0.0652 | yes: GAIN |
| node-hours | 2.516 | 2.27 | −9.8% | −0.4595 to −0.0327 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 274.2 | 274 | −0.1% | −0.7006 to +0.3546 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.2 | 255.9 | −6.7% | −34.2511 to −2.3365 | yes: GAIN |
| response time (ms), mean | 440 | 420 | −4.5% | −28.6061 to −11.3057 | yes: GAIN |
| response time (ms), 95th percentile | 1592 | 1731 | +8.8% | +24.6616 to +254.0614 | yes: LOSS |
| response time (ms), 99th percentile | 2263 | 2418 | +6.8% | +45.7081 to +264.1765 | yes: LOSS |
| time over the response line (% of samples) | 19.88 | 20.1 | +1.1% | −0.4593 to +0.8930 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.6 | 11.7 | +10.4% | +0.1198 to +2.0802 | yes: LOSS |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 102.7 | +102.700 (native is 0) | +38.9702 to +166.4298 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 13.83 | 16.52 | +19.5% | −0.1681 to +5.5581 | no |
| utilisation (used / allocatable) | 0.06477 | 0.07255 | +12.0% | +0.0012 to +0.0143 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.554 | 1.564 | +0.6% | −0.0058 to +0.0252 | no |
| Omni's own CPU (cores), mean | 0 | 0.07479 | +0.075 (native is 0) | +0.0701 to +0.0795 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.554 | 1.639 | +5.4% | +0.0679 to +0.1011 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 429.5 | 396.1 | −7.8% | −59.0333 to −7.8001 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.025 | 2.362 | +16.6% | +0.0203 to +0.6537 | yes: power given |
| pods started | 0 | 1.3 | +1.300 (native is 0) | +0.2856 to +2.3144 | yes: power given |
| pod start wait, total (s) | 0 | 3.2 | +3.200 (native is 0) | +0.1317 to +6.2683 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.25 | +1.250 (native is 0) | +0.3382 to +2.1618 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 44.54 | 47.71 | +7.1% | +2.8634 to +3.4745 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 816.8 | 825.3 | +1.0% | +2.1355 to +14.8645 | yes: LOSS |
| batch: worker machines in service after the queue finished, mean | 6 | 4.854 | −19.1% | −2.1839 to −0.1083 | yes: GAIN |
| queue: job wait, submitted to its first pod running, mean (s) | 0.3042 | 0.3667 | +20.5% | −0.0160 to +0.1410 | no |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 1.2 | 2.4 | +100.0% | +0.0417 to +2.3583 | yes: LOSS |
| queue: job turnaround, submitted to done, mean (s) | 122.1 | 130.5 | +6.9% | +1.3417 to +15.4833 | yes: LOSS |
| queue: jobs unfinished at the window's end | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*