# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1417 | 1414 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1417 | 1414 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 543.1 | 349.4 |
| response time (ms), 95th percentile | 1918 | 1202 |
| response time (ms), 99th percentile | 5718 | 5029 |
| time over the response line (% of samples) | 37.28 | 25.02 |
| failed requests (%) | 19.61 | 17.82 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 105.7 | 84.67 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 139.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 45.69 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.039 | 3.678 |
| utilisation (used / allocatable) | 0.1246 | 0.1228 |
| CPU used (cores), mean | 2.99 | 2.947 |
| Omni's own CPU (cores), mean | 0 | 0.05123 |
| CPU used with Omni's own (cores), mean | 2.99 | 2.998 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 240.7 | 244.1 |
| HPA replicas, mean | 9.945 | 15.79 |
| pods started | 4.333 | 14 |
| pod start wait, total (s) | 7.333 | 26.67 |
| pod start wait, mean (s) | 1.567 | 1.915 |
| host CPU busy, the real machine under kind (%) | 83.58 | 84.38 |
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
| node-hours | 12.01 | 12.02 | +0.1% | −0.0161 to +0.0317 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1417 | 1414 | −0.2% | −8.2327 to +3.6133 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1417 | 1414 | −0.2% | −8.2327 to +3.6133 | no |
| response time (ms), mean | 543.1 | 349.4 | −35.7% | −311.0180 to −76.3613 | yes: GAIN |
| response time (ms), 95th percentile | 1918 | 1202 | −37.3% | −1220.7285 to −210.8949 | yes: GAIN |
| response time (ms), 99th percentile | 5718 | 5029 | −12.1% | −2200.2777 to +821.9884 | no |
| time over the response line (% of samples) | 37.28 | 25.02 | −32.9% | −17.9756 to −6.5382 | yes: GAIN |
| failed requests (%) | 19.61 | 17.82 | −9.1% | −4.7023 to +1.1300 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 105.7 | 84.67 | −19.9% | −43.0813 to +1.0813 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 139.3 | +139.333 (native is 0) | +88.3388 to +190.3279 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.039 | 3.678 | +80.4% | +0.6553 to +2.6225 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1246 | 0.1228 | −1.4% | −0.0032 to −0.0004 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.99 | 2.947 | −1.4% | −0.0778 to −0.0087 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05123 | +0.051 (native is 0) | +0.0299 to +0.0725 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.99 | 2.998 | +0.3% | −0.0472 to +0.0632 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 240.7 | 244.1 | +1.4% | −2.4905 to +9.2204 | no |
| HPA replicas, mean | 9.945 | 15.79 | +58.8% | +5.5367 to +6.1552 | yes: power given |
| pods started | 4.333 | 14 | +223.1% | −15.2181 to +34.5514 | no |
| pod start wait, total (s) | 7.333 | 26.67 | +263.6% | −31.6612 to +70.3279 | no |
| pod start wait, mean (s) | 1.567 | 1.915 | +22.3% | −1.3216 to +2.0190 | no |
| host CPU busy, the real machine under kind (%) | 83.58 | 84.38 | +1.0% | −1.0944 to +2.6882 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.057 | 720 | 100.0% | 0 | 1.06 | yes |
| omni | 2 | long |  |  |  | 0 | 1.059 | 720 | 100.0% | 0 | 1.03 | yes |
| omni | 3 | long |  |  |  | 0 | 1.074 | 720 | 100.0% | 0 | 1.07 | yes |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*