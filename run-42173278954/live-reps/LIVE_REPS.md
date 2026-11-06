# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.998 |
| node-hours | 2.52 | 2.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 271.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 139.8 | 116.3 |
| response time (ms), 95th percentile | 248.4 | 259.4 |
| response time (ms), 99th percentile | 360.2 | 383.9 |
| time over the response line (% of samples) | 0.27 | 0.4154 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1211 | 1323 |
| utilisation (used / allocatable) | 0.06048 | 0.0582 |
| CPU used (cores), mean | 1.451 | 1.396 |
| Omni's own CPU (cores), mean | 0 | 0.0726 |
| CPU used with Omni's own (cores), mean | 1.451 | 1.469 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448 | 464.1 |
| HPA replicas, mean | 2.042 | 2.292 |
| pods started | 0 | 1.6 |
| pod start wait, total (s) | 0 | 3.4 |
| pod start wait, mean (s) | 0 | 1.183 |
| host CPU busy, the real machine under kind (%) | 45.63 | 46.77 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 1452 | 1466 |
| batch: worker machines in service after the queue finished, mean | 6 | 5.929 |
| queue: job wait, submitted to its first pod running, mean (s) | 161.8 | 204.9 |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 779.2 | 805 |
| queue: job turnaround, submitted to done, mean (s) | 852.1 | 909.7 |
| queue: jobs unfinished at the window's end | 12.8 | 14.2 |
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
| worker nodes in service, mean | 6 | 5.998 | −0.0% | −0.0073 to +0.0028 | no |
| node-hours | 2.52 | 2.514 | −0.2% | −0.0142 to +0.0027 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 272.9 | 271.6 | −0.5% | −2.0858 to −0.5196 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.9 | 271.6 | −0.5% | −2.0797 to −0.6673 | yes: GAIN |
| response time (ms), mean | 139.8 | 116.3 | −16.8% | −29.1806 to −17.7441 | yes: GAIN |
| response time (ms), 95th percentile | 248.4 | 259.4 | +4.4% | −2.7344 to +24.6024 | no |
| response time (ms), 99th percentile | 360.2 | 383.9 | +6.6% | +3.4494 to +44.0108 | yes: LOSS |
| time over the response line (% of samples) | 0.27 | 0.4154 | +53.9% | −0.0069 to +0.2979 | no |
| failed requests (%) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 0.1 | 0.1 | ±0.0% | −0.3372 to +0.3372 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 110 | +110.000 (native is 0) | +93.4223 to +126.5777 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1211 | 1323 | +9.2% | +57.0525 to +165.7209 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.06048 | 0.0582 | −3.8% | −0.0037 to −0.0009 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.451 | 1.396 | −3.8% | −0.0887 to −0.0215 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0726 | +0.073 (native is 0) | +0.0636 to +0.0816 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.451 | 1.469 | +1.2% | −0.0175 to +0.0525 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 448 | 464.1 | +3.6% | +6.0787 to +26.1484 | yes, up (shown, not judged) |
| HPA replicas, mean | 2.042 | 2.292 | +12.2% | −0.0112 to +0.5113 | no |
| pods started | 0 | 1.6 | +1.600 (native is 0) | +0.4715 to +2.7285 | yes: power given |
| pod start wait, total (s) | 0 | 3.4 | +3.400 (native is 0) | +0.7406 to +6.0594 | yes: LOSS |
| pod start wait, mean (s) | 0 | 1.183 | +1.183 (native is 0) | +0.3680 to +1.9986 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 45.63 | 46.77 | +2.5% | +0.3084 to +1.9797 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| batch: queue finished (s) | 1452 | 1466 | +0.9% | −15.8571 to +42.6571 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 5.929 | −1.2% | −0.9790 to +0.8361 | no |
| queue: job wait, submitted to its first pod running, mean (s) | 161.8 | 204.9 | +26.6% | +14.3924 to +71.7909 | yes: LOSS |
| queue: job wait, submitted to its first pod running, 95th percentile (s) | 779.2 | 805 | +3.3% | −45.3297 to +96.9297 | no |
| queue: job turnaround, submitted to done, mean (s) | 852.1 | 909.7 | +6.8% | +10.4703 to +104.6297 | yes: LOSS |
| queue: jobs unfinished at the window's end | 12.8 | 14.2 | +10.9% | −0.6006 to +3.4006 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*