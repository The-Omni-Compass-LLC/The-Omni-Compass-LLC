# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.999 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1436 | 1434 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1436 | 1434 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 588.8 | 394.7 |
| response time (ms), 95th percentile | 1970 | 1411 |
| response time (ms), 99th percentile | 6840 | 6644 |
| time over the response line (% of samples) | 45.29 | 31.21 |
| failed requests (%) | 27.22 | 23.68 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 119 | 101 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 31.67 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.333 | 2.339 |
| utilisation (used / allocatable) | 0.1358 | 0.1343 |
| CPU used (cores), mean | 3.258 | 3.222 |
| Omni's own CPU (cores), mean | 0 | 0.0107 |
| CPU used with Omni's own (cores), mean | 3.258 | 3.233 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 220.3 | 222.3 |
| HPA replicas, mean | 9.968 | 15.09 |
| pods started | 2.667 | 8 |
| pod start wait, total (s) | 7.333 | 15 |
| pod start wait, mean (s) | 1.933 | 1.898 |
| host CPU busy, the real machine under kind (%) | 91.35 | 91.07 |
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
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.005149 to +0.003207 | no |
| node-hours | 12.01 | 12.01 | +0.1% | -0.01063 to +0.02785 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1436 | 1434 | -0.1% | -3.911 to +0.9739 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1436 | 1434 | -0.1% | -4.658 to +1.429 | no |
| response time (ms), mean | 588.8 | 394.7 | -33.0% | -219.7 to -168.4 | yes: GAIN |
| response time (ms), 95th percentile | 1970 | 1411 | -28.4% | -1186 to +68.49 | no |
| response time (ms), 99th percentile | 6840 | 6644 | -2.9% | -1407 to +1016 | no |
| time over the response line (% of samples) | 45.29 | 31.21 | -31.1% | -17.27 to -10.88 | yes: GAIN |
| failed requests (%) | 27.22 | 23.68 | -13.0% | -4.184 to -2.91 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 119 | 101 | -15.1% | -20.48 to -15.52 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 101.3 | +101 (native is 0) | +81.1 to +121.6 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.333 | 2.339 | +0.2% | -1.982 to +1.994 | no |
| utilisation (used / allocatable) | 0.1358 | 0.1343 | -1.1% | -0.003177 to +0.000205 | no |
| CPU used (cores), mean | 3.258 | 3.222 | -1.1% | -0.07848 to +0.006086 | no |
| Omni's own CPU (cores), mean | 0 | 0.0107 | +0.0107 (native is 0) | +0.009839 to +0.01156 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 3.258 | 3.233 | -0.8% | -0.06843 to +0.01744 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 220.3 | 222.3 | +0.9% | -0.1484 to +4.187 | no |
| HPA replicas, mean | 9.968 | 15.09 | +51.4% | +5.023 to +5.23 | yes: power given |
| pods started | 2.667 | 8 | +200.0% | -0.9188 to +11.59 | no |
| pod start wait, total (s) | 7.333 | 15 | +104.5% | -10.98 to +26.31 | no |
| pod start wait, mean (s) | 1.933 | 1.898 | -1.8% | -3.367 to +3.296 | no |
| host CPU busy, the real machine under kind (%) | 91.35 | 91.07 | -0.3% | -1.206 to +0.6387 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.035 | 117 | 97.5% | 0 | 0.91 | yes |
| omni | 2 | long |  |  |  | 0 | 1.027 | 117 | 97.5% | 0 | 0.87 | yes |
| omni | 3 | long |  |  |  | 0 | 1.027 | 117 | 97.5% | 0 | 1.04 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*