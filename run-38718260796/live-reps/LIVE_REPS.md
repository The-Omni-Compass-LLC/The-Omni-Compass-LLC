# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.02 |
| energy, parked workers still on at idle power (Wh, declared model) | 1349 | 1348 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1349 | 1348 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 258 | 144.4 |
| response time (ms), 95th percentile | 739.3 | 312.8 |
| response time (ms), 99th percentile | 2055 | 1562 |
| time over the response line (% of samples) | 11.11 | 4.272 |
| failed requests (%) | 2.019 | 1.742 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 57 | 32 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 198.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 40 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.394 | 4.25 |
| utilisation (used / allocatable) | 0.08705 | 0.08578 |
| CPU used (cores), mean | 2.089 | 2.059 |
| Omni's own CPU (cores), mean | 0 | 0.008833 |
| CPU used with Omni's own (cores), mean | 2.089 | 2.068 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 337.4 | 343.8 |
| HPA replicas, mean | 9.901 | 12.7 |
| pods started | 6 | 23 |
| pod start wait, total (s) | 22 | 55.67 |
| pod start wait, mean (s) | 3.6 | 2.373 |
| host CPU busy, the real machine under kind (%) | 58.8 | 58.58 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.57e-15 to +9.779e-16 | EVEN, the same (under one part in a million) |
| node-hours | 12.01 | 12.02 | +0.1% | +0.0007118 to +0.02262 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 1349 | 1348 | -0.1% | -6.021 to +4.36 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1349 | 1348 | -0.1% | -6.021 to +4.36 | no |
| response time (ms), mean | 258 | 144.4 | -44.0% | -238.8 to +11.54 | no |
| response time (ms), 95th percentile | 739.3 | 312.8 | -57.7% | -827.4 to -25.49 | yes: GAIN |
| response time (ms), 99th percentile | 2055 | 1562 | -24.0% | -778.3 to -207.3 | yes: GAIN |
| time over the response line (% of samples) | 11.11 | 4.272 | -61.5% | -18.32 to +4.649 | no |
| failed requests (%) | 2.019 | 1.742 | -13.7% | -1.037 to +0.4833 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 57 | 32 | -43.9% | -38.83 to -11.17 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 198.3 | +198 (native is 0) | +22.27 to +374.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.394 | 4.25 | +77.5% | -0.4155 to +4.127 | no |
| utilisation (used / allocatable) | 0.08705 | 0.08578 | -1.5% | -0.004078 to +0.001547 | no |
| CPU used (cores), mean | 2.089 | 2.059 | -1.5% | -0.09787 to +0.03713 | no |
| Omni's own CPU (cores), mean | 0 | 0.008833 | +0.00883 (native is 0) | +0.005213 to +0.01245 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.089 | 2.068 | -1.0% | -0.09223 to +0.04916 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 337.4 | 343.8 | +1.9% | -13 to +25.73 | no |
| HPA replicas, mean | 9.901 | 12.7 | +28.2% | -6.352 to +11.94 | no |
| pods started | 6 | 23 | +283.3% | +1.485 to +32.51 | yes: power given |
| pod start wait, total (s) | 22 | 55.67 | +153.0% | -33.79 to +101.1 | no |
| pod start wait, mean (s) | 3.6 | 2.373 | -34.1% | -2.923 to +0.4699 | no |
| host CPU busy, the real machine under kind (%) | 58.8 | 58.58 | -0.4% | -1.718 to +1.266 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.032 | 119 | 99.2% | 0 | 0.83 | yes |
| omni | 2 | long |  |  |  | 0 | 1.054 | 120 | 100.0% | 0 | 0.98 | yes |
| omni | 3 | long |  |  |  | 0 | 1.032 | 119 | 99.2% | 0 | 0.77 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*