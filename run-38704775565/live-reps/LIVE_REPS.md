# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.02 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1438 | 1434 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1438 | 1434 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 590.8 | 394.2 |
| response time (ms), 95th percentile | 2035 | 1583 |
| response time (ms), 99th percentile | 6577 | 6316 |
| time over the response line (% of samples) | 45.14 | 31.8 |
| failed requests (%) | 26.87 | 23.91 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 118.3 | 101.7 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 6.667 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.578 | 1.756 |
| utilisation (used / allocatable) | 0.1357 | 0.1344 |
| CPU used (cores), mean | 3.258 | 3.224 |
| Omni's own CPU (cores), mean | 0 | 0.01063 |
| CPU used with Omni's own (cores), mean | 3.258 | 3.235 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 220.3 | 222.2 |
| HPA replicas, mean | 9.963 | 15.12 |
| pods started | 3.333 | 7 |
| pod start wait, total (s) | 9.333 | 13 |
| pod start wait, mean (s) | 2.389 | 1.825 |
| host CPU busy, the real machine under kind (%) | 91.17 | 91.1 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.207e-15 to +2.207e-15 | no |
| node-hours | 12.02 | 12.01 | -0.1% | -0.0341 to +0.01299 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1438 | 1434 | -0.3% | -9.752 to +2.349 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1438 | 1434 | -0.3% | -9.752 to +2.349 | no |
| response time (ms), mean | 590.8 | 394.2 | -33.3% | -223.9 to -169.2 | yes: GAIN |
| response time (ms), 95th percentile | 2035 | 1583 | -22.2% | -948.3 to +44.58 | no |
| response time (ms), 99th percentile | 6577 | 6316 | -4.0% | -477.7 to -42.42 | yes: GAIN |
| time over the response line (% of samples) | 45.14 | 31.8 | -29.6% | -18.81 to -7.875 | yes: GAIN |
| failed requests (%) | 26.87 | 23.91 | -11.0% | -6.56 to +0.6336 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 118.3 | 101.7 | -14.1% | -22.4 to -10.93 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 100.7 | +101 (native is 0) | +64.98 to +136.4 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 2.578 | 1.756 | -31.9% | -2.576 to +0.9317 | no |
| utilisation (used / allocatable) | 0.1357 | 0.1344 | -1.0% | -0.004163 to +0.001371 | no |
| CPU used (cores), mean | 3.258 | 3.224 | -1.0% | -0.09992 to +0.03291 | no |
| Omni's own CPU (cores), mean | 0 | 0.01063 | +0.0106 (native is 0) | +0.01049 to +0.01078 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 3.258 | 3.235 | -0.7% | -0.08926 to +0.04352 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 220.3 | 222.2 | +0.9% | -2.065 to +5.914 | no |
| HPA replicas, mean | 9.963 | 15.12 | +51.7% | +5.145 to +5.159 | yes: power given |
| pods started | 3.333 | 7 | +110.0% | -1.505 to +8.838 | no |
| pod start wait, total (s) | 9.333 | 13 | +39.3% | -18.74 to +26.07 | no |
| pod start wait, mean (s) | 2.389 | 1.825 | -23.6% | -3.533 to +2.406 | no |
| host CPU busy, the real machine under kind (%) | 91.17 | 91.1 | -0.1% | -2.237 to +2.098 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.031 | 117 | 97.5% | 0 | 1.03 | yes |
| omni | 2 | long |  |  |  | 0 | 1.023 | 117 | 97.5% | 0 | 1.10 | yes |
| omni | 3 | long |  |  |  | 0 | 1.010 | 117 | 97.5% | 0 | 1.07 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*