# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.515 | 1.519 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 173.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 173.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 534.6 | 436.6 |
| response time (ms), 95th percentile | 2246 | 1976 |
| response time (ms), 99th percentile | 5529 | 5074 |
| time over the response line (% of samples) | 24.63 | 21.59 |
| failed requests (%) | 4.047 | 3.835 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.7 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.12 | 1.097 |
| utilisation (used / allocatable) | 0.09842 | 0.09779 |
| CPU used (cores), mean | 2.362 | 2.347 |
| Omni's own CPU (cores), mean | 0 | 0.01082 |
| CPU used with Omni's own (cores), mean | 2.362 | 2.358 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.7 | 300.9 |
| HPA replicas, mean | 15.08 | 15.4 |
| pods started | 4.7 | 3.2 |
| pod start wait, total (s) | 9.7 | 8 |
| pod start wait, mean (s) | 1.941 | 1.966 |
| host CPU busy, the real machine under kind (%) | 68.47 | 68.23 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 258.3 | 298 |
| second app: response time (ms), 99th percentile | 898.6 | 1509 |
| second app: time over the response line (% of samples) | 14.63 | 14.49 |
| second app: failed requests (%) | 13.4 | 13.21 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.037e-15 to +1.037e-15 | no |
| node-hours | 1.515 | 1.519 | +0.2% | -0.001948 to +0.009281 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.8 | 173.1 | +0.2% | -0.4448 to +0.9705 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.8 | 173.1 | +0.2% | -0.4448 to +0.9705 | no |
| response time (ms), mean | 534.6 | 436.6 | -18.3% | -157.5 to -38.34 | yes: GAIN |
| response time (ms), 95th percentile | 2246 | 1976 | -12.0% | -648.1 to +108.9 | no |
| response time (ms), 99th percentile | 5529 | 5074 | -8.2% | -1248 to +336.6 | no |
| time over the response line (% of samples) | 24.63 | 21.59 | -12.3% | -5.239 to -0.8427 | yes: GAIN |
| failed requests (%) | 4.047 | 3.835 | -5.2% | -1.476 to +1.052 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 8.7 | 8.2 | -5.7% | -1.273 to +0.2726 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 32.7 | +32.7 (native is 0) | +30.49 to +34.91 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 1.12 | 1.097 | -2.1% | -0.9192 to +0.8725 | no |
| utilisation (used / allocatable) | 0.09842 | 0.09779 | -0.6% | -0.00148 to +0.0002189 | no |
| CPU used (cores), mean | 2.362 | 2.347 | -0.6% | -0.03552 to +0.005253 | no |
| Omni's own CPU (cores), mean | 0 | 0.01082 | +0.0108 (native is 0) | +0.009501 to +0.01214 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.362 | 2.358 | -0.2% | -0.02519 to +0.01656 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 298.7 | 300.9 | +0.7% | -1.651 to +6.082 | no |
| HPA replicas, mean | 15.08 | 15.4 | +2.1% | +0.04704 to +0.5819 | yes: power given |
| pods started | 4.7 | 3.2 | -31.9% | -2.58 to -0.4204 | yes: GAIN |
| pod start wait, total (s) | 9.7 | 8 | -17.5% | -4.562 to +1.162 | no |
| pod start wait, mean (s) | 1.941 | 1.966 | +1.3% | -0.3812 to +0.4327 | no |
| host CPU busy, the real machine under kind (%) | 68.47 | 68.23 | -0.3% | -0.9022 to +0.4243 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 258.3 | 298 | +15.3% | -51.44 to +130.7 | no |
| second app: response time (ms), 99th percentile | 898.6 | 1509 | +68.0% | -186.7 to +1408 | no |
| second app: time over the response line (% of samples) | 14.63 | 14.49 | -0.9% | -0.5956 to +0.3215 | no |
| second app: failed requests (%) | 13.4 | 13.21 | -1.4% | -0.8653 to +0.4922 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*