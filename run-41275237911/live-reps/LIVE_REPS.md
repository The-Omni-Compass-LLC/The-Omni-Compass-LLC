# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1395 | 1393 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1395 | 1393 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 438.6 | 256.8 |
| response time (ms), 95th percentile | 1363 | 757.8 |
| response time (ms), 99th percentile | 4359 | 3613 |
| time over the response line (% of samples) | 27.57 | 14.78 |
| failed requests (%) | 11.49 | 9.577 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 92 | 65 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 18.06 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.106 | 1.7 |
| utilisation (used / allocatable) | 0.1129 | 0.1107 |
| CPU used (cores), mean | 2.711 | 2.657 |
| Omni's own CPU (cores), mean | 0 | 0.0106 |
| CPU used with Omni's own (cores), mean | 2.711 | 2.667 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 261.6 | 266.5 |
| HPA replicas, mean | 9.935 | 15.17 |
| pods started | 5 | 16.67 |
| pod start wait, total (s) | 5 | 31.67 |
| pod start wait, mean (s) | 0.9444 | 1.903 |
| host CPU busy, the real machine under kind (%) | 75.46 | 75.01 |
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
| node-hours | 12.01 | 12.02 | +0.1% | −0.0107 to +0.0307 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1395 | 1393 | −0.2% | −5.4133 to +0.4697 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1395 | 1393 | −0.2% | −5.4133 to +0.4697 | no |
| response time (ms), mean | 438.6 | 256.8 | −41.5% | −323.9865 to −39.6284 | yes: GAIN |
| response time (ms), 95th percentile | 1363 | 757.8 | −44.4% | −828.2159 to −381.7708 | yes: GAIN |
| response time (ms), 99th percentile | 4359 | 3613 | −17.1% | −1177.5623 to −314.9777 | yes: GAIN |
| time over the response line (% of samples) | 27.57 | 14.78 | −46.4% | −23.2697 to −2.3105 | yes: GAIN |
| failed requests (%) | 11.49 | 9.577 | −16.7% | −7.2675 to +3.4346 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 92 | 65 | −29.3% | −42.5147 to −11.4853 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 124 | +124.000 (native is 0) | +98.0627 to +149.9373 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.106 | 1.7 | −19.3% | −0.8855 to +0.0743 | no |
| utilisation (used / allocatable) | 0.1129 | 0.1107 | −2.0% | −0.0028 to −0.0017 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.711 | 2.657 | −2.0% | −0.0679 to −0.0399 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0106 | +0.011 (native is 0) | +0.0067 to +0.0145 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.711 | 2.667 | −1.6% | −0.0601 to −0.0265 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 261.6 | 266.5 | +1.9% | +0.4011 to +9.3560 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.935 | 15.17 | +52.7% | +5.0698 to +5.4078 | yes: power given |
| pods started | 5 | 16.67 | +233.3% | −7.1444 to +30.4778 | no |
| pod start wait, total (s) | 5 | 31.67 | +533.3% | −10.7087 to +64.0420 | no |
| pod start wait, mean (s) | 0.9444 | 1.903 | +101.5% | +0.5975 to +1.3199 | yes: LOSS |
| host CPU busy, the real machine under kind (%) | 75.46 | 75.01 | −0.6% | −1.7694 to +0.8744 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.027 | 120 | 100.0% | 0 | 1.08 | yes |
| omni | 2 | long |  |  |  | 0 | 1.010 | 120 | 100.0% | 0 | 1.03 | yes |
| omni | 3 | long |  |  |  | 0 | 1.031 | 120 | 100.0% | 0 | 1.18 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*