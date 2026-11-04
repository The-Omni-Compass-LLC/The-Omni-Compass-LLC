# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.512 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 175.2 | 174.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.2 | 174.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 404.5 | 233.8 |
| response time (ms), 95th percentile | 1171 | 627 |
| response time (ms), 99th percentile | 3785 | 3076 |
| time over the response line (% of samples) | 26.14 | 17.48 |
| failed requests (%) | 12.74 | 12.3 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 8.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1417 | 0.5567 |
| utilisation (used / allocatable) | 0.1106 | 0.1086 |
| CPU used (cores), mean | 2.654 | 2.605 |
| Omni's own CPU (cores), mean | 0 | 0.04977 |
| CPU used with Omni's own (cores), mean | 2.654 | 2.655 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.8 | 276.8 |
| HPA replicas, mean | 9.415 | 11.45 |
| pods started | 5.4 | 12.7 |
| pod start wait, total (s) | 8.1 | 21.4 |
| pod start wait, mean (s) | 1.489 | 1.727 |
| host CPU busy, the real machine under kind (%) | 75.53 | 76.26 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| robust: failed requests in the 300 s after the kill (%) | 49.16 | 56.58 |
| robust: time over the line in the 300 s after the kill (% of samples) | 71.25 | 73.72 |

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
| node-hours | 1.512 | 1.511 | −0.0% | −0.0091 to +0.0077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 175.2 | 174.6 | −0.3% | −1.7037 to +0.5799 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.2 | 174.6 | −0.3% | −1.7037 to +0.5799 | no |
| response time (ms), mean | 404.5 | 233.8 | −42.2% | −233.2426 to −108.1902 | yes: GAIN |
| response time (ms), 95th percentile | 1171 | 627 | −46.4% | −806.2541 to −281.0809 | yes: GAIN |
| response time (ms), 99th percentile | 3785 | 3076 | −18.7% | −1949.4371 to +531.5417 | no |
| time over the response line (% of samples) | 26.14 | 17.48 | −33.1% | −11.5031 to −5.8125 | yes: GAIN |
| failed requests (%) | 12.74 | 12.3 | −3.5% | −1.0640 to +0.1846 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11 | 8.8 | −20.0% | −3.0121 to −1.3879 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 80.2 | +80.200 (native is 0) | +71.7714 to +88.6286 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.1417 | 0.5567 | +292.9% | +0.1951 to +0.6349 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1106 | 0.1086 | −1.8% | −0.0034 to −0.0006 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.654 | 2.605 | −1.8% | −0.0821 to −0.0146 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04977 | +0.050 (native is 0) | +0.0457 to +0.0539 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.654 | 2.655 | +0.1% | −0.0292 to +0.0320 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 273.8 | 276.8 | +1.1% | +0.1038 to +5.9964 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.415 | 11.45 | +21.6% | +1.8179 to +2.2546 | yes: power given |
| pods started | 5.4 | 12.7 | +135.2% | +4.6438 to +9.9562 | yes: power given |
| pod start wait, total (s) | 8.1 | 21.4 | +164.2% | +7.6470 to +18.9530 | yes: LOSS |
| pod start wait, mean (s) | 1.489 | 1.727 | +16.0% | −0.0272 to +0.5030 | no |
| host CPU busy, the real machine under kind (%) | 75.53 | 76.26 | +1.0% | +0.0917 to +1.3695 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 49.16 | 56.58 | +15.1% | +0.8344 to +14.0147 | yes: LOSS |
| robust: time over the line in the 300 s after the kill (% of samples) | 71.25 | 73.72 | +3.5% | −0.4497 to +5.4039 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 2 | kill | 11 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 3 | kill | 8 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 5 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 6 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 7 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 8 | kill | 9 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 9 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*