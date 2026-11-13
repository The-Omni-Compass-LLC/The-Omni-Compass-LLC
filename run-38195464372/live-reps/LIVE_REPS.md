# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.517 | 1.515 |
| energy, parked workers still on at idle power (Wh, declared model) | 176 | 175.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176 | 175.3 |
| response time (ms), mean | 428.4 | 262.2 |
| response time (ms), 95th percentile | 1233 | 754.1 |
| response time (ms), 99th percentile | 4598 | 4243 |
| time over the response line (% of samples) | 31.75 | 20.18 |
| failed requests (%) | 17.16 | 15.13 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7867 | 0.2667 |
| utilisation (used / allocatable) | 0.1117 | 0.1094 |
| CPU used (cores), mean | 2.681 | 2.625 |
| Omni's own CPU (cores), mean | 0 | 0.01445 |
| CPU used with Omni's own (cores), mean | 2.681 | 2.64 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 283.2 | 289.9 |
| HPA replicas, mean | 9.473 | 9.538 |
| pods started | 4.8 | 3.7 |
| pod start wait, total (s) | 17.1 | 10.7 |
| pod start wait, mean (s) | 3.158 | 2.093 |
| host CPU busy, the real machine under kind (%) | 76.99 | 76.11 |
| host cores (the real machine under kind) | 4 | 4 |
| robust: failed requests in the 120 s after the kill (%) | 59.35 | 60.57 |
| robust: time over the line in the 120 s after the kill (% of samples) | 74.47 | 72.92 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.953e-16 to +1.624e-16 | same (under one part in a million) |
| node-hours | 1.517 | 1.515 | -0.1% | -0.009615 to +0.006281 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 176 | 175.3 | -0.4% | -1.698 to +0.2933 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 176 | 175.3 | -0.4% | -1.698 to +0.2933 | no |
| response time (ms), mean | 428.4 | 262.2 | -38.8% | -224.9 to -107.5 | yes, better |
| response time (ms), 95th percentile | 1233 | 754.1 | -38.9% | -704.3 to -254.3 | yes, better |
| response time (ms), 99th percentile | 4598 | 4243 | -7.7% | -1901 to +1191 | no |
| time over the response line (% of samples) | 31.75 | 20.18 | -36.5% | -15.86 to -7.292 | yes, better |
| failed requests (%) | 17.16 | 15.13 | -11.9% | -3.121 to -0.9508 | yes, better |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7867 | 0.2667 | -66.1% | -1.189 to +0.1489 | no |
| utilisation (used / allocatable) | 0.1117 | 0.1094 | -2.1% | -0.002863 to -0.001819 | yes, less |
| CPU used (cores), mean | 2.681 | 2.625 | -2.1% | -0.06872 to -0.04365 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01445 | +0.0144 (native is 0) | +0.01281 to +0.01609 | yes, more |
| CPU used with Omni's own (cores), mean | 2.681 | 2.64 | -1.6% | -0.05436 to -0.02912 | yes, less |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 283.2 | 289.9 | +2.4% | +2.036 to +11.29 | yes, more |
| HPA replicas, mean | 9.473 | 9.538 | +0.7% | -0.04079 to +0.1716 | no |
| pods started | 4.8 | 3.7 | -22.9% | -2.241 to +0.04101 | no |
| pod start wait, total (s) | 17.1 | 10.7 | -37.4% | -12.97 to +0.1663 | no |
| pod start wait, mean (s) | 3.158 | 2.093 | -33.7% | -2.143 to +0.01233 | no |
| host CPU busy, the real machine under kind (%) | 76.99 | 76.11 | -1.1% | -1.41 to -0.3448 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| robust: failed requests in the 120 s after the kill (%) | 59.35 | 60.57 | +2.1% | -5.284 to +7.722 | no |
| robust: time over the line in the 120 s after the kill (% of samples) | 74.47 | 72.92 | -2.1% | -4.997 to +1.901 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition reads WORSE. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 reads WORSE (a leak). The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 reads WORSE); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 2 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 3 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 4 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 5 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 6 | kill | 7 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 7 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 8 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 9 | kill | 11 | yes | yes | 1 |  | 14 |  |  |  |  |
| omni | 10 | kill | 10 | yes | yes | 1 |  | 14 |  |  |  |  |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*