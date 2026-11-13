# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.885 |
| node-hours | 2.51 | 2.045 |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 236.5 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 465 | 413.4 |
| response time (ms), 95th percentile | 2888 | 2831 |
| response time (ms), 99th percentile | 4441 | 4205 |
| time over the response line (% of samples) | 14.81 | 14.5 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174.7 | 177.5 |
| utilisation (used / allocatable) | 0.05942 | 0.07094 |
| CPU used (cores), mean | 1.426 | 1.382 |
| Omni's own CPU (cores), mean | 0 | 0.02277 |
| CPU used with Omni's own (cores), mean | 1.426 | 1.405 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.8 | 410.4 |
| HPA replicas, mean | 2.054 | 2.154 |
| pods started | 0.2 | 0.1 |
| pod start wait, total (s) | 10.2 | 5 |
| pod start wait, mean (s) | 5.1 | 5 |
| host CPU busy, the real machine under kind (%) | 40.63 | 41.32 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 549.6 | 550.5 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.296 |

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
| worker nodes in service, mean | 6 | 4.885 | -18.6% | -1.613 to -0.6171 | yes: GAIN |
| node-hours | 2.51 | 2.045 | -18.5% | -0.6739 to -0.2569 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 271.8 | 271.4 | -0.1% | -1.144 to +0.4334 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 271.8 | 236.5 | -13.0% | -51.1 to -19.57 | yes: GAIN |
| response time (ms), mean | 465 | 413.4 | -11.1% | -64.34 to -38.81 | yes: GAIN |
| response time (ms), 95th percentile | 2888 | 2831 | -2.0% | -179.4 to +66.2 | no |
| response time (ms), 99th percentile | 4441 | 4205 | -5.3% | -392.1 to -79.25 | yes: GAIN |
| time over the response line (% of samples) | 14.81 | 14.5 | -2.1% | -0.9038 to +0.2839 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.5 | 9.4 | -1.1% | -0.3262 to +0.1262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 14.1 | +14.1 (native is 0) | +12.5 to +15.7 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 174.7 | 177.5 | +1.6% | -1.901 to +7.498 | no |
| utilisation (used / allocatable) | 0.05942 | 0.07094 | +19.4% | +0.005409 to +0.01762 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.426 | 1.382 | -3.1% | -0.07385 to -0.01361 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02277 | +0.0228 (native is 0) | +0.01905 to +0.02649 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.426 | 1.405 | -1.5% | -0.05166 to +0.009736 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 461.8 | 410.4 | -11.1% | -83.43 to -19.35 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.054 | 2.154 | +4.9% | -0.1376 to +0.3374 | no |
| pods started | 0.2 | 0.1 | -50.0% | -0.6278 to +0.4278 | no |
| pod start wait, total (s) | 10.2 | 5 | -51.0% | -32 to +21.6 | no |
| pod start wait, mean (s) | 5.1 | 5 | -2.0% | -17.13 to +16.93 | no |
| host CPU busy, the real machine under kind (%) | 40.63 | 41.32 | +1.7% | +0.3017 to +1.089 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 549.6 | 550.5 | +0.2% | -6.185 to +7.985 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.296 | -28.4% | -2.396 to -1.012 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*