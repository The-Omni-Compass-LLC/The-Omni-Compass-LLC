# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 173.6 | 173.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.6 | 173.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 381.4 | 229.3 |
| response time (ms), 95th percentile | 1253 | 655.5 |
| response time (ms), 99th percentile | 4479 | 2801 |
| time over the response line (% of samples) | 21.84 | 15.14 |
| failed requests (%) | 9.821 | 9.708 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 7.9 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 97.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2767 | 0.5433 |
| utilisation (used / allocatable) | 0.1034 | 0.1016 |
| CPU used (cores), mean | 2.481 | 2.439 |
| Omni's own CPU (cores), mean | 0 | 0.04848 |
| CPU used with Omni's own (cores), mean | 2.481 | 2.487 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.2 | 301.4 |
| HPA replicas, mean | 9.404 | 11.35 |
| pods started | 5.1 | 13.2 |
| pod start wait, total (s) | 7.9 | 22.2 |
| pod start wait, mean (s) | 1.581 | 1.698 |
| host CPU busy, the real machine under kind (%) | 70.61 | 71.39 |
| host cores (the real machine under kind) | 4 | 4 |
| work inside the response line (requests a second; the capacity test's own gauge) | nan | nan |
| work per dollar of the bill (answers inside the line for each $; the cloud's judged number) | nan | nan |
| robust: failed requests in the 300 s after the kill (%) | 43.09 | 46.98 |
| robust: time over the line in the 300 s after the kill (% of samples) | 62.41 | 63.38 |

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
| node-hours | 1.513 | 1.512 | −0.0% | −0.0071 to +0.0064 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 173.6 | 173.2 | −0.2% | −1.3474 to +0.5298 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 173.6 | 173.2 | −0.2% | −1.3474 to +0.5298 | no |
| response time (ms), mean | 381.4 | 229.3 | −39.9% | −210.0130 to −94.2590 | yes: GAIN |
| response time (ms), 95th percentile | 1253 | 655.5 | −47.7% | −1006.4700 to −189.4180 | yes: GAIN |
| response time (ms), 99th percentile | 4479 | 2801 | −37.5% | −2847.6570 to −508.3044 | yes: GAIN |
| time over the response line (% of samples) | 21.84 | 15.14 | −30.7% | −9.3989 to −4.0024 | yes: GAIN |
| failed requests (%) | 9.821 | 9.708 | −1.1% | −0.9313 to +0.7057 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.8 | 7.9 | −19.4% | −2.3060 to −1.4940 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 81.3 | +81.300 (native is 0) | +71.2797 to +91.3203 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2767 | 0.5433 | +96.4% | +0.0304 to +0.5030 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.1034 | 0.1016 | −1.7% | −0.0029 to −0.0007 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.481 | 2.439 | −1.7% | −0.0687 to −0.0162 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.04848 | +0.048 (native is 0) | +0.0433 to +0.0537 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.481 | 2.487 | +0.2% | −0.0204 to +0.0325 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 295.2 | 301.4 | +2.1% | +0.1988 to +12.1198 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.404 | 11.35 | +20.7% | +1.7614 to +2.1388 | yes: power given |
| pods started | 5.1 | 13.2 | +158.8% | +5.7772 to +10.4228 | yes: power given |
| pod start wait, total (s) | 7.9 | 22.2 | +181.0% | +9.4951 to +19.1049 | yes: LOSS |
| pod start wait, mean (s) | 1.581 | 1.698 | +7.4% | −0.2326 to +0.4666 | no |
| host CPU busy, the real machine under kind (%) | 70.61 | 71.39 | +1.1% | −0.0907 to +1.6325 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |
| robust: failed requests in the 300 s after the kill (%) | 43.09 | 46.98 | +9.0% | −1.5110 to +9.2864 | no |
| robust: time over the line in the 300 s after the kill (% of samples) | 62.41 | 63.38 | +1.6% | −3.9876 to +5.9280 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 17 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 2 | kill | 11 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 3 | kill | 14 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 4 | kill | 13 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 6 | kill | 9 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 8 | kill | 8 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 82 |  |  |  |  |

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*