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
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1370 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1370 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 390.9 | 241.2 |
| response time (ms), 95th percentile | 1354 | 770.4 |
| response time (ms), 99th percentile | 4036 | 3213 |
| time over the response line (% of samples) | 23.6 | 14.39 |
| failed requests (%) | 11.72 | 9.946 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 70.67 | 53.33 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 52.54 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.222 | 2.756 |
| utilisation (used / allocatable) | 0.1011 | 0.09857 |
| CPU used (cores), mean | 2.427 | 2.366 |
| Omni's own CPU (cores), mean | 0 | 0.04463 |
| CPU used with Omni's own (cores), mean | 2.427 | 2.41 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.6 | 318.3 |
| HPA replicas, mean | 9.9 | 14.04 |
| pods started | 8.333 | 31.33 |
| pod start wait, total (s) | 11.67 | 50 |
| pod start wait, mean (s) | 1.4 | 1.645 |
| host CPU busy, the real machine under kind (%) | 68.46 | 68.79 |
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
| node-hours | 12.01 | 12.01 | −0.0% | −0.0420 to +0.0409 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1375 | 1370 | −0.3% | −8.1028 to −0.7850 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1375 | 1370 | −0.3% | −8.1028 to −0.7850 | yes: GAIN |
| response time (ms), mean | 390.9 | 241.2 | −38.3% | −367.7869 to +68.2624 | no |
| response time (ms), 95th percentile | 1354 | 770.4 | −43.1% | −1419.8337 to +252.3637 | no |
| response time (ms), 99th percentile | 4036 | 3213 | −20.4% | −2613.3183 to +967.9963 | no |
| time over the response line (% of samples) | 23.6 | 14.39 | −39.0% | −26.4762 to +8.0538 | no |
| failed requests (%) | 11.72 | 9.946 | −15.1% | −8.5141 to +4.9624 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 70.67 | 53.33 | −24.5% | −34.2439 to −0.4228 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 164.7 | +164.667 (native is 0) | +41.3140 to +288.0193 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.222 | 2.756 | +24.0% | −2.8738 to +3.9404 | no |
| utilisation (used / allocatable) | 0.1011 | 0.09857 | −2.5% | −0.0057 to +0.0006 | no |
| CPU used (cores), mean | 2.427 | 2.366 | −2.5% | −0.1369 to +0.0138 | no |
| Omni's own CPU (cores), mean | 0 | 0.04463 | +0.045 (native is 0) | +0.0172 to +0.0720 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.427 | 2.41 | −0.7% | −0.0649 to +0.0311 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 311.6 | 318.3 | +2.2% | +1.4418 to +12.0800 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.9 | 14.04 | +41.8% | −3.1126 to +11.3984 | no |
| pods started | 8.333 | 31.33 | +276.0% | −33.1592 to +79.1592 | no |
| pod start wait, total (s) | 11.67 | 50 | +328.6% | −46.0733 to +122.7399 | no |
| pod start wait, mean (s) | 1.4 | 1.645 | +17.5% | −0.7012 to +1.1903 | no |
| host CPU busy, the real machine under kind (%) | 68.46 | 68.79 | +0.5% | −0.0483 to +0.7076 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.056 | 720 | 100.0% | 0 | 1.04 | yes |
| omni | 2 | long |  |  |  | 0 | 1.087 | 720 | 100.0% | 0 | 1.01 | yes |
| omni | 3 | long |  |  |  | 0 | 1.081 | 720 | 100.0% | 0 | 1.15 | yes |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*