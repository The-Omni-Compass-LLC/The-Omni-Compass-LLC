# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **STEADY**: native and Omni-Compass within 0.5% of each other (the mean of the three runs' changes under the 0.5% floor, or no change at all), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A change of 0.5% or more, the mean of the three runs' changes, reads GAIN, LOSS or power given: **in all three of our runs** where A, B and C moved the same way with every interval clear of zero, otherwise **by the mean of our three runs**, with the count of runs beyond the noise beside it; **the runs disagree** names runs that moved 0.5% or more in opposite directions, a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1360 | 1356 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1360 | 1356 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 346.6 | 221.3 |
| response time (ms), 95th percentile | 1183 | 808.5 |
| response time (ms), 99th percentile | 3572 | 3544 |
| time over the response line (% of samples) | 20.04 | 10.59 |
| failed requests (%) | 9.666 | 6.467 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 61 | 43.67 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 194 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 55.81 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.622 | 4.344 |
| utilisation (used / allocatable) | 0.09296 | 0.09078 |
| CPU used (cores), mean | 2.231 | 2.179 |
| Omni's own CPU (cores), mean | 0 | 0.0457 |
| CPU used with Omni's own (cores), mean | 2.231 | 2.224 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 341.2 | 342.5 |
| HPA replicas, mean | 9.88 | 13.66 |
| pods started | 10 | 36.67 |
| pod start wait, total (s) | 14.67 | 63.67 |
| pod start wait, mean (s) | 1.409 | 2.013 |
| host CPU busy, the real machine under kind (%) | 63.84 | 63.95 |
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
| worker nodes in service, mean | 6 | 6 | ±0.0% | −0.0000 to +0.0000 | no |
| node-hours | 12.01 | 12.01 | +0.0% | −0.0156 to +0.0178 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1360 | 1356 | −0.3% | −25.4410 to +17.5391 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1360 | 1356 | −0.3% | −25.4410 to +17.5391 | no |
| response time (ms), mean | 346.6 | 221.3 | −36.2% | −353.1705 to +102.5221 | no |
| response time (ms), 95th percentile | 1183 | 808.5 | −31.6% | −845.2743 to +96.9143 | no |
| response time (ms), 99th percentile | 3572 | 3544 | −0.8% | −2625.4716 to +2568.6576 | no |
| time over the response line (% of samples) | 20.04 | 10.59 | −47.2% | −39.0551 to +20.1533 | no |
| failed requests (%) | 9.666 | 6.467 | −33.1% | −17.6368 to +11.2386 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 61 | 43.67 | −28.4% | −42.8306 to +8.1639 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 194 | +194.000 (native is 0) | +4.6028 to +383.3972 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | ±0.000 (native is 0) | ±0.0000 to ±0.0000 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.622 | 4.344 | +65.7% | −1.5163 to +4.9607 | no |
| utilisation (used / allocatable) | 0.09296 | 0.09078 | −2.3% | −0.0132 to +0.0088 | no |
| CPU used (cores), mean | 2.231 | 2.179 | −2.3% | −0.3166 to +0.2123 | no |
| Omni's own CPU (cores), mean | 0 | 0.0457 | +0.046 (native is 0) | +0.0147 to +0.0767 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.231 | 2.224 | −0.3% | −0.2479 to +0.2349 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 341.2 | 342.5 | +0.4% | −19.6922 to +22.3704 | no |
| HPA replicas, mean | 9.88 | 13.66 | +38.2% | −3.7660 to +11.3162 | no |
| pods started | 10 | 36.67 | +266.7% | −33.3872 to +86.7205 | no |
| pod start wait, total (s) | 14.67 | 63.67 | +334.1% | −44.3860 to +142.3860 | no |
| pod start wait, mean (s) | 1.409 | 2.013 | +42.9% | −1.2536 to +2.4611 | no |
| host CPU busy, the real machine under kind (%) | 63.84 | 63.95 | +0.2% | −6.9203 to +7.1392 | no |
| host cores (the real machine under kind) | 4 | 4 | ±0.0% | ±0.0000 to ±0.0000 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 300 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.072 | 720 | 100.0% | 0 | 1.06 | yes |
| omni | 2 | long |  |  |  | 0 | 1.082 | 720 | 100.0% | 0 | 1.12 | yes |
| omni | 3 | long |  |  |  | 0 | 1.053 | 720 | 100.0% | 0 | 1.03 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*