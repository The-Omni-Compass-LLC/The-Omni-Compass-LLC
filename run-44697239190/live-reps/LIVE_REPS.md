# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.51 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.9 | 173.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.9 | 173.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 386.6 | 248.9 |
| response time (ms), 95th percentile | 1030 | 678.9 |
| response time (ms), 99th percentile | 3940 | 3498 |
| time over the response line (% of samples) | 24.66 | 16.12 |
| failed requests (%) | 11.04 | 10.17 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 97.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2533 | 0.7917 |
| utilisation (used / allocatable) | 0.1062 | 0.1038 |
| CPU used (cores), mean | 2.548 | 2.491 |
| Omni's own CPU (cores), mean | 0 | 0.05102 |
| CPU used with Omni's own (cores), mean | 2.548 | 2.542 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 285.6 | 289.4 |
| HPA replicas, mean | 9.409 | 11.51 |
| pods started | 5.4 | 13.3 |
| pod start wait, total (s) | 7.4 | 23.9 |
| pod start wait, mean (s) | 1.392 | 1.853 |
| host CPU busy, the real machine under kind (%) | 72.74 | 73.55 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| robust: failed requests in the 300 s after the kill (%) | 44.43 | 47.58 |
| robust: time over the line in the 300 s after the kill (% of samples) | 65.94 | 68.29 |

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
| node-hours | 1.51 | 1.511 | +0.1% | −0.0046 to +0.0076 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.9 | 173.6 | −0.2% | −1.4274 to +0.6650 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.9 | 173.6 | −0.2% | −1.4274 to +0.6650 | no |
| response time (ms), mean | 386.6 | 248.9 | −35.6% | −186.5827 to −88.9052 | yes: GAIN |
| response time (ms), 95th percentile | 1030 | 678.9 | −34.1% | −562.8109 to −140.1051 | yes: GAIN |
| response time (ms), 99th percentile | 3940 | 3498 | −11.2% | −1320.1788 to +435.5480 | no |
| time over the response line (% of samples) | 24.66 | 16.12 | −34.7% | −12.0308 to −5.0673 | yes: GAIN |
| failed requests (%) | 11.04 | 10.17 | −7.8% | −1.5105 to −0.2204 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10.5 | 8.2 | −21.9% | −3.2567 to −1.3433 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 85.9 | +85.900 (native is 0) | +75.0495 to +96.7505 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2533 | 0.7917 | +212.5% | −0.0714 to +1.1481 | no |
| utilisation (used / allocatable) | 0.1062 | 0.1038 | −2.2% | −0.0039 to −0.0008 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.548 | 2.491 | −2.2% | −0.0941 to −0.0190 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05102 | +0.051 (native is 0) | +0.0462 to +0.0558 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.548 | 2.542 | −0.2% | −0.0400 to +0.0290 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 285.6 | 289.4 | +1.3% | −0.0299 to +7.5251 | no |
| HPA replicas, mean | 9.409 | 11.51 | +22.3% | +1.9125 to +2.2859 | yes: power given |
| pods started | 5.4 | 13.3 | +146.3% | +4.7108 to +11.0892 | yes: power given |
| pod start wait, total (s) | 7.4 | 23.9 | +223.0% | +10.5702 to +22.4298 | yes: LOSS |
| pod start wait, mean (s) | 1.392 | 1.853 | +33.1% | +0.0918 to +0.8297 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 72.74 | 73.55 | +1.1% | +0.1116 to +1.5133 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 44.43 | 47.58 | +7.1% | +0.1468 to +6.1451 | yes: LOSS |
| robust: time over the line in the 300 s after the kill (% of samples) | 65.94 | 68.29 | +3.6% | −1.9607 to +6.6586 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 2 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 3 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 4 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 5 | kill | 11 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 6 | kill | 8 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 9 | kill | 12 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 10 | kill | 18 | yes | yes | 1 |  | 82 |  |  |  |  |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*