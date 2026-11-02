# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.516 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 178.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 178.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 512.6 | 317.1 |
| response time (ms), 95th percentile | 1448 | 825.4 |
| response time (ms), 99th percentile | 5398 | 4688 |
| time over the response line (% of samples) | 40.31 | 27.37 |
| failed requests (%) | 23.4 | 21.75 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.6 | 12.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2283 | 0.8233 |
| utilisation (used / allocatable) | 0.1288 | 0.1259 |
| CPU used (cores), mean | 3.09 | 3.022 |
| Omni's own CPU (cores), mean | 0 | 0.05666 |
| CPU used with Omni's own (cores), mean | 3.09 | 3.079 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 230.2 | 234.6 |
| HPA replicas, mean | 9.521 | 11.48 |
| pods started | 4.9 | 8.2 |
| pod start wait, total (s) | 8.4 | 17.4 |
| pod start wait, mean (s) | 1.72 | 2.149 |
| host CPU busy, the real machine under kind (%) | 88.58 | 89.02 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| robust: failed requests in the 300 s after the kill (%) | 86.27 | 95.09 |
| robust: time over the line in the 300 s after the kill (% of samples) | 99.06 | 100 |

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
| worker nodes in service, mean | 6 | 6 | 0.0% | raw −0.0000 to −0.0000 | STEADY, the same (to nine decimal places) |
| node-hours | 1.516 | 1.51 | −0.4% | −0.0130 to +0.0013 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 178.4 | −0.7% | −2.3233 to −0.3671 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 178.4 | −0.7% | −2.3233 to −0.3671 | yes: GAIN |
| response time (ms), mean | 512.6 | 317.1 | −38.1% | −262.2655 to −128.8634 | yes: GAIN |
| response time (ms), 95th percentile | 1448 | 825.4 | −43.0% | −976.9067 to −267.8893 | yes: GAIN |
| response time (ms), 99th percentile | 5398 | 4688 | −13.1% | −3105.6790 to +1686.1630 | no |
| time over the response line (% of samples) | 40.31 | 27.37 | −32.1% | −14.5539 to −11.3089 | yes: GAIN |
| failed requests (%) | 23.4 | 21.75 | −7.0% | −2.3409 to −0.9507 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 14.6 | 12.1 | −17.1% | −3.0058 to −1.9942 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 74.7 | +74.700 (native is 0) | +72.4876 to +76.9124 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2283 | 0.8233 | +260.6% | +0.0937 to +1.0963 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1288 | 0.1259 | −2.2% | −0.0035 to −0.0022 | yes, down (shown, not judged) |
| CPU used (cores), mean | 3.09 | 3.022 | −2.2% | −0.0837 to −0.0523 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.05666 | +0.057 (native is 0) | +0.0549 to +0.0585 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 3.09 | 3.079 | −0.4% | −0.0264 to +0.0037 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 230.2 | 234.6 | +1.9% | +3.3390 to +5.3117 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.521 | 11.48 | +20.6% | +1.8407 to +2.0840 | yes: power given |
| pods started | 4.9 | 8.2 | +67.3% | +2.1295 to +4.4705 | yes: power given |
| pod start wait, total (s) | 8.4 | 17.4 | +107.1% | +5.1553 to +12.8447 | yes: LOSS |
| pod start wait, mean (s) | 1.72 | 2.149 | +25.0% | −0.0417 to +0.9005 | no |
| host CPU busy, the real machine under kind (%) | 88.58 | 89.02 | +0.5% | +0.1659 to +0.7239 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 86.27 | 95.09 | +10.2% | +0.9161 to +16.7046 | yes: LOSS |
| robust: time over the line in the 300 s after the kill (% of samples) | 99.06 | 100 | +0.9% | −0.5712 to +2.4462 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 2 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 3 | kill | 12 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 4 | kill | 15 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 5 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 6 | kill | 17 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 7 | kill | 16 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 8 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 9 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 10 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*