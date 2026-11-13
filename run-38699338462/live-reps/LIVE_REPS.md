# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.509 | 4.514 |
| energy, parked workers still on at idle power (Wh, declared model) | 507.5 | 507.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 507.5 | 507.2 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 235.9 | 124.4 |
| response time (ms), 95th percentile | 636.3 | 262.6 |
| response time (ms), 99th percentile | 2068 | 1108 |
| time over the response line (% of samples) | 12.43 | 7.084 |
| failed requests (%) | 5.91 | 5.315 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.9 | 14.2 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.6183 |
| utilisation (used / allocatable) | 0.08867 | 0.08716 |
| CPU used (cores), mean | 2.128 | 2.092 |
| Omni's own CPU (cores), mean | 0 | 0.00746 |
| CPU used with Omni's own (cores), mean | 2.128 | 2.099 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.3 | 351.6 |
| HPA replicas, mean | 9.342 | 9.543 |
| pods started | 5.3 | 8.2 |
| pod start wait, total (s) | 20.2 | 29.6 |
| pod start wait, mean (s) | 3.435 | 3.538 |
| host CPU busy, the real machine under kind (%) | 60.15 | 59.31 |
| host cores (the real machine under kind) | 4 | 4 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.041e-16 to +1.492e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.509 | 4.514 | +0.1% | -0.00249 to +0.01316 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 507.5 | 507.2 | -0.1% | -1.51 to +0.8659 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 507.5 | 507.2 | -0.1% | -1.51 to +0.8659 | no |
| response time (ms), mean | 235.9 | 124.4 | -47.3% | -150.3 to -72.69 | yes: GAIN |
| response time (ms), 95th percentile | 636.3 | 262.6 | -58.7% | -483.3 to -264.2 | yes: GAIN |
| response time (ms), 99th percentile | 2068 | 1108 | -46.4% | -1459 to -459.7 | yes: GAIN |
| time over the response line (% of samples) | 12.43 | 7.084 | -43.0% | -8.193 to -2.504 | yes: GAIN |
| failed requests (%) | 5.91 | 5.315 | -10.1% | -1.403 to +0.2128 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 20.9 | 14.2 | -32.1% | -9.356 to -4.044 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 37.1 | +37.1 (native is 0) | +24.69 to +49.51 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.48 | 0.6183 | +28.8% | -0.156 to +0.4327 | no |
| utilisation (used / allocatable) | 0.08867 | 0.08716 | -1.7% | -0.002967 to -5.611e-05 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.128 | 2.092 | -1.7% | -0.0712 to -0.001347 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00746 | +0.00746 (native is 0) | +0.006171 to +0.008749 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.128 | 2.099 | -1.4% | -0.06414 to +0.006504 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 344.3 | 351.6 | +2.1% | +1.98 to +12.51 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.342 | 9.543 | +2.2% | -0.5204 to +0.9227 | no |
| pods started | 5.3 | 8.2 | +54.7% | +0.5772 to +5.223 | yes: power given |
| pod start wait, total (s) | 20.2 | 29.6 | +46.5% | -1.739 to +20.54 | no |
| pod start wait, mean (s) | 3.435 | 3.538 | +3.0% | -0.905 to +1.112 | no |
| host CPU busy, the real machine under kind (%) | 60.15 | 59.31 | -1.4% | -1.712 to +0.01489 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; a rise is more work from the same machines, a GAIN.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 27.6 |  |  | 10 |
| compass | 36.0 | +30.4% | +4.3 to +12.5 | 10 |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*