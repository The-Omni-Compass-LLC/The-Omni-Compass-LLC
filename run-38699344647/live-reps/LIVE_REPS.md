# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.513 | 1.516 |
| energy, parked workers still on at idle power (Wh, declared model) | 170.8 | 170.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.8 | 170.8 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 418.8 | 373.8 |
| response time (ms), 95th percentile | 1780 | 1705 |
| response time (ms), 99th percentile | 4210 | 4374 |
| time over the response line (% of samples) | 19.41 | 18.02 |
| failed requests (%) | 3.11 | 2.924 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.093 | 1.26 |
| utilisation (used / allocatable) | 0.09071 | 0.08942 |
| CPU used (cores), mean | 2.177 | 2.146 |
| Omni's own CPU (cores), mean | 0 | 0.01006 |
| CPU used with Omni's own (cores), mean | 2.177 | 2.156 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 324.6 | 329.3 |
| HPA replicas, mean | 14.97 | 14.74 |
| pods started | 4.4 | 4.7 |
| pod start wait, total (s) | 12.8 | 17 |
| pod start wait, mean (s) | 2.544 | 2.938 |
| host CPU busy, the real machine under kind (%) | 62.53 | 62.69 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 332.3 | 307.7 |
| second app: response time (ms), 99th percentile | 1495 | 1401 |
| second app: time over the response line (% of samples) | 12.79 | 12.35 |
| second app: failed requests (%) | 10.36 | 10.53 |

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
| node-hours | 1.513 | 1.516 | +0.2% | +7.903e-05 to +0.005254 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 170.8 | 170.8 | +0.0% | -0.2994 to +0.3519 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 170.8 | 170.8 | +0.0% | -0.2994 to +0.3519 | no |
| response time (ms), mean | 418.8 | 373.8 | -10.8% | -91.27 to +1.187 | no |
| response time (ms), 95th percentile | 1780 | 1705 | -4.2% | -279.5 to +130.5 | no |
| response time (ms), 99th percentile | 4210 | 4374 | +3.9% | -1028 to +1355 | no |
| time over the response line (% of samples) | 19.41 | 18.02 | -7.2% | -2.76 to -0.01679 | yes: GAIN |
| failed requests (%) | 3.11 | 2.924 | -6.0% | -0.6806 to +0.3091 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 6.9 | 6.8 | -1.4% | -0.6278 to +0.4278 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 33.3 | +33.3 (native is 0) | +31.3 to +35.3 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.093 | 1.26 | +15.2% | -0.5598 to +0.8932 | no |
| utilisation (used / allocatable) | 0.09071 | 0.08942 | -1.4% | -0.002447 to -0.0001352 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.177 | 2.146 | -1.4% | -0.05872 to -0.003244 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01006 | +0.0101 (native is 0) | +0.008587 to +0.01153 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.177 | 2.156 | -1.0% | -0.04871 to +0.006864 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 324.6 | 329.3 | +1.4% | -1.392 to +10.73 | no |
| HPA replicas, mean | 14.97 | 14.74 | -1.5% | -0.5087 to +0.05796 | no |
| pods started | 4.4 | 4.7 | +6.8% | -0.4578 to +1.058 | no |
| pod start wait, total (s) | 12.8 | 17 | +32.8% | -0.3089 to +8.709 | no |
| pod start wait, mean (s) | 2.544 | 2.938 | +15.5% | -0.2624 to +1.051 | no |
| host CPU busy, the real machine under kind (%) | 62.53 | 62.69 | +0.2% | -0.44 to +0.7503 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 332.3 | 307.7 | -7.4% | -73.24 to +24.05 | no |
| second app: response time (ms), 99th percentile | 1495 | 1401 | -6.3% | -988.4 to +801.3 | no |
| second app: time over the response line (% of samples) | 12.79 | 12.35 | -3.4% | -1.067 to +0.1897 | no |
| second app: failed requests (%) | 10.36 | 10.53 | +1.6% | -0.1958 to +0.53 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*