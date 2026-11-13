# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 12.01 | 12.01 |
| energy, parked workers still on at idle power (Wh, declared model) | 1352 | 1352 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1352 | 1352 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 298.2 | 207.5 |
| response time (ms), 95th percentile | 912.8 | 647.4 |
| response time (ms), 99th percentile | 2969 | 3301 |
| time over the response line (% of samples) | 17.62 | 11.35 |
| failed requests (%) | 9.109 | 7.888 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 56.67 | 39.67 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 166.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 53.33 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.944 | 3.011 |
| utilisation (used / allocatable) | 0.08911 | 0.08857 |
| CPU used (cores), mean | 2.139 | 2.126 |
| Omni's own CPU (cores), mean | 0 | 0.009567 |
| CPU used with Omni's own (cores), mean | 2.139 | 2.135 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 354.1 | 357.4 |
| HPA replicas, mean | 9.89 | 13.08 |
| pods started | 7 | 18.33 |
| pod start wait, total (s) | 29.33 | 52.33 |
| pod start wait, mean (s) | 4.189 | 3.193 |
| host CPU busy, the real machine under kind (%) | 60.6 | 60.83 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.844e-15 to +2.252e-15 | EVEN, the same (under one part in a million) |
| node-hours | 12.01 | 12.01 | +0.0% | -0.03156 to +0.04267 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 1352 | 1352 | -0.0% | -7.316 to +7.02 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1352 | 1352 | -0.0% | -7.316 to +7.02 | no |
| response time (ms), mean | 298.2 | 207.5 | -30.4% | -260 to +78.77 | no |
| response time (ms), 95th percentile | 912.8 | 647.4 | -29.1% | -401.6 to -129.3 | yes: GAIN |
| response time (ms), 99th percentile | 2969 | 3301 | +11.2% | -1383 to +2046 | no |
| time over the response line (% of samples) | 17.62 | 11.35 | -35.6% | -24.18 to +11.63 | no |
| failed requests (%) | 9.109 | 7.888 | -13.4% | -6.456 to +4.013 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 56.67 | 39.67 | -30.0% | -30.15 to -3.854 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 166.3 | +166 (native is 0) | -95.58 to +428.2 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.944 | 3.011 | +54.9% | -2.967 to +5.1 | no |
| utilisation (used / allocatable) | 0.08911 | 0.08857 | -0.6% | -0.007014 to +0.005924 | no |
| CPU used (cores), mean | 2.139 | 2.126 | -0.6% | -0.1683 to +0.1422 | no |
| Omni's own CPU (cores), mean | 0 | 0.009567 | +0.00957 (native is 0) | +0.002969 to +0.01616 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.139 | 2.135 | -0.2% | -0.1626 to +0.1556 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 354.1 | 357.4 | +0.9% | -32.15 to +38.77 | no |
| HPA replicas, mean | 9.89 | 13.08 | +32.3% | -5.768 to +12.16 | no |
| pods started | 7 | 18.33 | +161.9% | -16.03 to +38.7 | no |
| pod start wait, total (s) | 29.33 | 52.33 | +78.4% | -14.1 to +60.1 | no |
| pod start wait, mean (s) | 4.189 | 3.193 | -23.8% | -4.256 to +2.265 | no |
| host CPU busy, the real machine under kind (%) | 60.6 | 60.83 | +0.4% | -3.894 to +4.356 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The robustness test: the governor killed outright, the lease, and the long run

In the kill scenario the governor receives SIGKILL at 40% of the window and the watchdog beside it must hand every setting back from the lease it left; the harness asks the cluster every 2 s until the HPA target, the replica range, every CPU limit, every worker and the records are at the operator's. Preregistered: within 60 s, or the repetition is marked. A second governor starts at 50% and governs to the end. The governor's resident memory is sampled from the process table; the mean of the last ten minutes over the first ten above 1.25 is marked a leak. The 120 s after the kill mark are compared between the arms in the paired table above (`docs/ROBUSTNESS_PREREGISTRATION.md`). In the long run the governor's own audit gives its decisions against the count its 60 s interval predicts for the window (under 95% reads INVALID), its failed decisions, and its decision time (the gap between decisions less the interval it sleeps), mean of the last hour over the first (over 1.5 is marked); the reset check at the end says whether every setting was handed back.

| Arm | Repetition | Mode | Seconds from the kill to every setting back | Within the allowance | Second governor | Watchdog hand-backs | Governor memory, last ten minutes / first ten | Decisions | Decisions of expected | Failed decisions | Decision time, last hour / first hour | Handed back at the end |
|---|---:|---|---:|---|---|---:|---:|---:|---:|---:|---:|---|
| omni | 1 | long |  |  |  | 0 | 1.013 | 117 | 97.5% | 0 | 0.73 | yes |
| omni | 2 | long |  |  |  | 0 | 1.051 | 120 | 100.0% | 0 | 1.13 | yes |
| omni | 3 | long |  |  |  | 0 | 1.051 | 119 | 99.2% | 0 | 0.95 | yes |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*