# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1370 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1372 | 1370 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 366.9 | 234.2 |
| response time (ms), 95th percentile | 1116 | 788.3 |
| response time (ms), 99th percentile | 4093 | 2870 |
| time over the response line (% of samples) | 21.47 | 13.9 |
| failed requests (%) | 10.32 | 9.414 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 70 | 51.67 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 48.73 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.633 | 3.422 |
| utilisation (used / allocatable) | 0.09964 | 0.09842 |
| CPU used (cores), mean | 2.391 | 2.362 |
| Omni's own CPU (cores), mean | 0 | 0.04383 |
| CPU used with Omni's own (cores), mean | 2.391 | 2.406 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.4 | 316.3 |
| HPA replicas, mean | 9.9 | 13.85 |
| pods started | 9 | 28.67 |
| pod start wait, total (s) | 12.67 | 48 |
| pod start wait, mean (s) | 1.562 | 1.619 |
| host CPU busy, the real machine under kind (%) | 67.43 | 68.44 |
| host cores (the real machine under kind) | 4 | 4 |
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

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 3 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to +0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 12.01 | 12.01 | −0.0% | −0.0201 to +0.0190 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1372 | 1370 | −0.1% | −6.7607 to +3.0226 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1372 | 1370 | −0.1% | −6.7607 to +3.0226 | no |
| response time (ms), mean | 366.9 | 234.2 | −36.2% | −307.3964 to +41.9839 | no |
| response time (ms), 95th percentile | 1116 | 788.3 | −29.3% | −793.8805 to +139.2572 | no |
| response time (ms), 99th percentile | 4093 | 2870 | −29.9% | −3092.6819 to +646.0259 | no |
| time over the response line (% of samples) | 21.47 | 13.9 | −35.3% | −20.4347 to +5.2975 | no |
| failed requests (%) | 10.32 | 9.414 | −8.8% | −4.5183 to +2.7081 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 70 | 51.67 | −26.2% | −43.4649 to +6.7982 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 150 | +150.000 (native is 0) | +69.3833 to +230.6167 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.633 | 3.422 | +109.5% | +0.7710 to +2.8068 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.09964 | 0.09842 | −1.2% | −0.0044 to +0.0020 | no |
| CPU used (cores), mean | 2.391 | 2.362 | −1.2% | −0.1065 to +0.0484 | no |
| Omni's own CPU (cores), mean | 0 | 0.04383 | +0.044 (native is 0) | +0.0181 to +0.0696 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.391 | 2.406 | +0.6% | −0.0408 to +0.0703 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 314.4 | 316.3 | +0.6% | −5.4077 to +9.2572 | no |
| HPA replicas, mean | 9.9 | 13.85 | +39.9% | −4.2176 to +12.1192 | no |
| pods started | 9 | 28.67 | +218.5% | −23.9569 to +63.2902 | no |
| pod start wait, total (s) | 12.67 | 48 | +278.9% | −50.3793 to +121.0460 | no |
| pod start wait, mean (s) | 1.562 | 1.619 | +3.6% | −1.4181 to +1.5307 | no |
| host CPU busy, the real machine under kind (%) | 67.43 | 68.44 | +1.5% | −0.7336 to +2.7568 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.053 | 720 | 100.0% | 0 | 1.06 | yes |
| omni | 2 | long |  |  |  | 0 | 1.093 | 720 | 100.0% | 0 | 1.23 | yes |
| omni | 3 | long |  |  |  | 0 | 1.070 | 720 | 100.0% | 0 | 1.08 | yes |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*