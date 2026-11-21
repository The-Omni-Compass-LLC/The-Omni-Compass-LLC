# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

<!-- how to read this receipt (tools/readings.py) -->
**How to read this receipt.** Every judged row reads one of three words, decided by what its gauge is for and never by the plus or minus sign of its number. **GAIN**: the gauge moved toward its declared aim against native (more work done, a shorter wait, fewer misses or failures, or a resource cut). **EVEN**: native and Omni-Compass could not be told apart (the 95% interval includes zero: no difference beyond the noise), or the knob is at its limit on native. **LOSS**: the gauge moved away from its aim (less work done, a longer wait, more misses or failures). A resource spent or held (energy, machines, memory, processor time, a bill) that fell is a cut, a GAIN; one that rose is **power given**, what Omni-Compass put in to buy the work and the speed shown beside it, always shown and never called a loss. So a minus can read GAIN (a response time cut) and a plus can read LOSS (failed requests up). A reading counts when it holds the same way in all three of our runs, A, B and C, with every interval clear of zero; **the runs disagree** names a test unstable there; **shown, not judged** is a gauge declared shown only. The output follows the input: every reading is the result of the tune, the wiring and the load it names, and where a reading elsewhere differs the first presumption is the wiring (`DISCLOSURES.md`, section 4). The full key, letter by letter: `docs/HOW_TO_READ_THE_RESULTS.md`. Run and scored by The Omni-Compass LLC's own code. No outside party has reviewed or approved these results. Preregistered means the rules were written down in our own repository before the runs; nothing was filed with any outside body.
<!-- end: how to read this receipt -->

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1296 | 1292 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1296 | 1292 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 102.1 | 57.64 |
| response time (ms), 95th percentile | 286.7 | 92.56 |
| response time (ms), 99th percentile | 513.4 | 175.6 |
| time over the response line (% of samples) | 1.133 | 0.08366 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.67 | 0 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.894 | 3.622 |
| utilisation (used / allocatable) | 0.05771 | 0.0554 |
| CPU used (cores), mean | 1.385 | 1.33 |
| Omni's own CPU (cores), mean | 0 | 0.006567 |
| CPU used with Omni's own (cores), mean | 1.385 | 1.336 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.8 | 485.9 |
| HPA replicas, mean | 9.818 | 8.938 |
| pods started | 10.33 | 16.67 |
| pod start wait, total (s) | 34.67 | 59.33 |
| pod start wait, mean (s) | 3.442 | 3.542 |
| host CPU busy, the real machine under kind (%) | 39.96 | 38.9 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.956e-15 to +3.14e-15 | EVEN, the same (under one part in a million) |
| node-hours | 12.01 | 12.01 | -0.0% | -0.01843 to +0.01065 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1296 | 1292 | -0.4% | -10.38 to +0.9651 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1296 | 1292 | -0.4% | -10.38 to +0.9651 | no |
| response time (ms), mean | 102.1 | 57.64 | -43.5% | -52.92 to -35.96 | yes: GAIN |
| response time (ms), 95th percentile | 286.7 | 92.56 | -67.7% | -220.8 to -167.4 | yes: GAIN |
| response time (ms), 99th percentile | 513.4 | 175.6 | -65.8% | -465.4 to -210.4 | yes: GAIN |
| time over the response line (% of samples) | 1.133 | 0.08366 | -92.6% | -1.247 to -0.851 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 11.67 | 0 | -100.0% | -17.92 to -5.415 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 117.7 | +118 (native is 0) | +62.26 to +173.1 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.894 | 3.622 | +91.2% | -3.78 to +7.236 | no |
| utilisation (used / allocatable) | 0.05771 | 0.0554 | -4.0% | -0.005137 to +0.0005144 | no |
| CPU used (cores), mean | 1.385 | 1.33 | -4.0% | -0.1233 to +0.01234 | no |
| Omni's own CPU (cores), mean | 0 | 0.006567 | +0.00657 (native is 0) | +0.005393 to +0.007741 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.385 | 1.336 | -3.5% | -0.1179 to +0.02004 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 467.8 | 485.9 | +3.9% | -4.879 to +41.14 | no |
| HPA replicas, mean | 9.818 | 8.938 | -9.0% | -1.62 to -0.1401 | yes: GAIN |
| pods started | 10.33 | 16.67 | +61.3% | -4.01 to +16.68 | no |
| pod start wait, total (s) | 34.67 | 59.33 | +71.2% | -6.594 to +55.93 | no |
| pod start wait, mean (s) | 3.442 | 3.542 | +2.9% | -1.161 to +1.362 | no |
| host CPU busy, the real machine under kind (%) | 39.96 | 38.9 | -2.7% | -2.64 to +0.5046 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.052 | 120 | 100.0% | 0 | 1.15 | yes |
| omni | 2 | long |  |  |  | 0 | 1.044 | 120 | 100.0% | 0 | 1.14 | yes |
| omni | 3 | long |  |  |  | 0 | 1.051 | 120 | 100.0% | 0 | 1.11 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*