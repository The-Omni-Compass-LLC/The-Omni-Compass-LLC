# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, the power drawn and its peaks and swings, machines, memory, processor time, a bill, wear) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss; work bought with each unit of a resource (work per energy) that fell is power given too. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.509 | 1.512 |
| energy, parked workers still on at idle power (Wh, declared model) | 169.6 | 169.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.6 | 169.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 282 | 153.3 |
| response time (ms), 95th percentile | 933.3 | 330.7 |
| response time (ms), 99th percentile | 2877 | 1901 |
| time over the response line (% of samples) | 16.71 | 11.29 |
| failed requests (%) | 9.35 | 9.044 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5933 | 0.6383 |
| utilisation (used / allocatable) | 0.08736 | 0.08566 |
| CPU used (cores), mean | 2.097 | 2.056 |
| Omni's own CPU (cores), mean | 0 | 0.01008 |
| CPU used with Omni's own (cores), mean | 2.097 | 2.066 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 364.6 | 371 |
| HPA replicas, mean | 9.243 | 9.51 |
| pods started | 5.5 | 5.5 |
| pod start wait, total (s) | 25.6 | 25.8 |
| pod start wait, mean (s) | 4.103 | 3.774 |
| host CPU busy, the real machine under kind (%) | 60.53 | 60.42 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 28.35 | 35.96 |
| robust: time over the line in the 120 s after the kill (% of samples) | 39.79 | 41.46 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.509 | 1.512 | +0.2% | -0.0003736 to +0.00504 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 169.6 | 169.6 | -0.1% | -0.4875 to +0.302 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 169.6 | 169.6 | -0.1% | -0.4875 to +0.302 | no |
| response time (ms), mean | 282 | 153.3 | -45.6% | -235.1 to -22.36 | yes: GAIN |
| response time (ms), 95th percentile | 933.3 | 330.7 | -64.6% | -1177 to -28 | yes: GAIN |
| response time (ms), 99th percentile | 2877 | 1901 | -33.9% | -3189 to +1237 | no |
| time over the response line (% of samples) | 16.71 | 11.29 | -32.5% | -9.342 to -1.508 | yes: GAIN |
| failed requests (%) | 9.35 | 9.044 | -3.3% | -1.049 to +0.4377 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.6 | 5.1 | -22.7% | -2.108 to -0.8921 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 41 | +41 (native is 0) | +35.8 to +46.2 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5933 | 0.6383 | +7.6% | -0.7381 to +0.8281 | no |
| utilisation (used / allocatable) | 0.08736 | 0.08566 | -1.9% | -0.002604 to -0.000792 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.097 | 2.056 | -1.9% | -0.0625 to -0.01901 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01008 | +0.0101 (native is 0) | +0.00853 to +0.01163 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.097 | 2.066 | -1.5% | -0.05168 to -0.009667 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 364.6 | 371 | +1.7% | +1.632 to +11.07 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.243 | 9.51 | +2.9% | -0.06853 to +0.6023 | no |
| pods started | 5.5 | 5.5 | +0.0% | -2.023 to +2.023 | no |
| pod start wait, total (s) | 25.6 | 25.8 | +0.8% | -8.784 to +9.184 | no |
| pod start wait, mean (s) | 4.103 | 3.774 | -8.0% | -1.552 to +0.8943 | no |
| host CPU busy, the real machine under kind (%) | 60.53 | 60.42 | -0.2% | -0.989 to +0.7839 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 28.35 | 35.96 | +26.8% | -0.2108 to +15.43 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 39.79 | 41.46 | +4.2% | -2.266 to +5.612 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 8 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*