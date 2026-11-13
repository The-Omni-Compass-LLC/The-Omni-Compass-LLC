# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native |
|---|---:|
| worker nodes in service, mean | 6 |
| node-hours | 1.513 |
| energy, parked workers still on at idle power (Wh, declared model) | 175.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 175.6 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan |
| response time (ms), mean | 433.7 |
| response time (ms), 95th percentile | 1506 |
| response time (ms), 99th percentile | 4696 |
| time over the response line (% of samples) | 28.25 |
| failed requests (%) | 16.07 |
| pods with no machine to take them (unschedulable) | 0 |
| time pods had no machine to take them, pod-minutes | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.5867 |
| utilisation (used / allocatable) | 0.1119 |
| CPU used (cores), mean | 2.687 |
| Omni's own CPU (cores), mean | 0 |
| CPU used with Omni's own (cores), mean | 2.687 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 277.4 |
| HPA replicas, mean | 9.467 |
| pods started | 4.9 |
| pod start wait, total (s) | 17.4 |
| pod start wait, mean (s) | 3.261 |
| host CPU busy, the real machine under kind (%) | 76.84 |
| host cores (the real machine under kind) | 4 |
| robust: failed requests in the 120 s after the kill (%) | 54.45 |
| robust: time over the line in the 120 s after the kill (% of samples) | 73.34 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 7 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 2 | kill | 11 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 3 | kill | 10 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 4 | kill | 9 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 5 | kill | 10 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 6 | kill | 9 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 7 | kill | 11 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 8 | kill | 11 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 9 | kill | 10 | yes | yes | 1 |  | 7 |  |  |  |  |
| omni | 10 | kill | 11 | yes | yes | 1 |  | 7 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*