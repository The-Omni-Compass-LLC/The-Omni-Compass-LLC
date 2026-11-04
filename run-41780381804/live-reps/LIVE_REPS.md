# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.521 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.2 | 173.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.2 | 173.9 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 543.7 | 548.8 |
| response time (ms), 95th percentile | 2428 | 2590 |
| response time (ms), 99th percentile | 5188 | 5631 |
| time over the response line (% of samples) | 24.94 | 25.7 |
| failed requests (%) | 3.352 | 2.529 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 131.4 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.657 | 1.727 |
| utilisation (used / allocatable) | 0.1003 | 0.1003 |
| CPU used (cores), mean | 2.407 | 2.406 |
| Omni's own CPU (cores), mean | 0 | 0.0564 |
| CPU used with Omni's own (cores), mean | 2.407 | 2.462 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.9 | 290.5 |
| HPA replicas, mean | 15.08 | 15.99 |
| pods started | 5.4 | 5.7 |
| pod start wait, total (s) | 8.3 | 10.9 |
| pod start wait, mean (s) | 1.521 | 1.912 |
| host CPU busy, the real machine under kind (%) | 69.46 | 70.96 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| second app: response time (ms), 95th percentile | 246.2 | 255 |
| second app: response time (ms), 99th percentile | 2301 | 1516 |
| second app: time over the response line (% of samples) | 15.08 | 15.21 |
| second app: failed requests (%) | 13.47 | 13.61 |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.515 | 1.521 | +0.4% | +0.0006 to +0.0114 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 173.2 | 173.9 | +0.4% | −0.1809 to +1.4905 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.2 | 173.9 | +0.4% | −0.1809 to +1.4905 | no |
| response time (ms), mean | 543.7 | 548.8 | +0.9% | −29.1184 to +39.3760 | no |
| response time (ms), 95th percentile | 2428 | 2590 | +6.6% | −56.0658 to +378.7238 | no |
| response time (ms), 99th percentile | 5188 | 5631 | +8.5% | +2.9588 to +883.7456 | yes: LOSS |
| time over the response line (% of samples) | 24.94 | 25.7 | +3.0% | −1.2391 to +2.7525 | no |
| failed requests (%) | 3.352 | 2.529 | −24.5% | −1.6738 to +0.0286 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.1 | 8.7 | −4.4% | −1.0911 to +0.2911 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 131.4 | +131.400 (native is 0) | +102.8072 to +159.9928 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.657 | 1.727 | +4.2% | −0.6676 to +0.8076 | no |
| utilisation (used / allocatable) | 0.1003 | 0.1003 | −0.0% | −0.0021 to +0.0020 | no |
| CPU used (cores), mean | 2.407 | 2.406 | −0.0% | −0.0513 to +0.0489 | no |
| Omni's own CPU (cores), mean | 0 | 0.0564 | +0.056 (native is 0) | +0.0499 to +0.0629 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.407 | 2.462 | +2.3% | +0.0086 to +0.1019 | yes, up (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 290.9 | 290.5 | −0.1% | −5.8861 to +5.2144 | no |
| HPA replicas, mean | 15.08 | 15.99 | +6.0% | +0.4117 to +1.4078 | yes: power given |
| pods started | 5.4 | 5.7 | +5.6% | −0.8209 to +1.4209 | no |
| pod start wait, total (s) | 8.3 | 10.9 | +31.3% | −0.7415 to +5.9415 | no |
| pod start wait, mean (s) | 1.521 | 1.912 | +25.7% | +0.0361 to +0.7449 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 69.46 | 70.96 | +2.2% | +0.4598 to +2.5440 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| second app: response time (ms), 95th percentile | 246.2 | 255 | +3.6% | −7.1721 to +24.8001 | no |
| second app: response time (ms), 99th percentile | 2301 | 1516 | −34.1% | −1809.6459 to +239.8823 | no |
| second app: time over the response line (% of samples) | 15.08 | 15.21 | +0.9% | −0.4331 to +0.6937 | no |
| second app: failed requests (%) | 13.47 | 13.61 | +1.0% | −0.5362 to +0.8119 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*