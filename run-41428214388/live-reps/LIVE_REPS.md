# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 174.5 | 174.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.5 | 174.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 401.9 | 245.3 |
| response time (ms), 95th percentile | 1263 | 732.9 |
| response time (ms), 99th percentile | 4344 | 3421 |
| time over the response line (% of samples) | 25.11 | 17.81 |
| failed requests (%) | 13.77 | 12.78 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.9 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 80 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.4967 |
| utilisation (used / allocatable) | 0.1063 | 0.1045 |
| CPU used (cores), mean | 2.55 | 2.508 |
| Omni's own CPU (cores), mean | 0 | 0.05062 |
| CPU used with Omni's own (cores), mean | 2.55 | 2.559 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.2 | 298.2 |
| HPA replicas, mean | 9.353 | 11.44 |
| pods started | 5.4 | 11.4 |
| pod start wait, total (s) | 7.8 | 19.8 |
| pod start wait, mean (s) | 1.43 | 1.777 |
| host CPU busy, the real machine under kind (%) | 73.14 | 73.88 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| robust: failed requests in the 300 s after the kill (%) | 56.12 | 58.96 |
| robust: time over the line in the 300 s after the kill (% of samples) | 67.69 | 67.22 |

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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 1.515 | 1.518 | +0.2% | −0.0064 to +0.0114 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 174.5 | 174.4 | −0.1% | −1.3057 to +1.0848 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 174.5 | 174.4 | −0.1% | −1.3057 to +1.0848 | no |
| response time (ms), mean | 401.9 | 245.3 | −39.0% | −241.2116 to −72.1116 | yes: GAIN |
| response time (ms), 95th percentile | 1263 | 732.9 | −42.0% | −1033.4040 to −27.3110 | yes: GAIN |
| response time (ms), 99th percentile | 4344 | 3421 | −21.2% | −2388.4648 to +542.5862 | no |
| time over the response line (% of samples) | 25.11 | 17.81 | −29.1% | −10.9842 to −3.6278 | yes: GAIN |
| failed requests (%) | 13.77 | 12.78 | −7.2% | −2.2554 to +0.2826 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.7 | 8.2 | −15.5% | −2.3430 to −0.6570 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.9 | +81.900 (native is 0) | +74.0464 to +89.7536 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.085 | 0.4967 | +484.3% | +0.1074 to +0.7159 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1063 | 0.1045 | −1.7% | −0.0034 to −0.0001 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.55 | 2.508 | −1.7% | −0.0826 to −0.0020 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05062 | +0.051 (native is 0) | +0.0448 to +0.0564 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.55 | 2.559 | +0.3% | −0.0281 to +0.0448 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 296.2 | 298.2 | +0.7% | −3.2919 to +7.2939 | no |
| HPA replicas, mean | 9.353 | 11.44 | +22.3% | +1.8781 to +2.2947 | yes: power given |
| pods started | 5.4 | 11.4 | +111.1% | +3.2194 to +8.7806 | yes: power given |
| pod start wait, total (s) | 7.8 | 19.8 | +153.8% | +7.1486 to +16.8514 | yes: LOSS |
| pod start wait, mean (s) | 1.43 | 1.777 | +24.2% | −0.0373 to +0.7304 | no |
| host CPU busy, the real machine under kind (%) | 73.14 | 73.88 | +1.0% | +0.0248 to +1.4588 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 56.12 | 58.96 | +5.1% | −0.0046 to +5.6872 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 67.69 | 67.22 | −0.7% | −2.0947 to +1.1527 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 2 | kill | 12 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 3 | kill | 9 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 4 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 6 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 8 | kill | 12 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 9 | kill | 8 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 10 | kill | 12 | yes | yes | 1 |  | 82 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*