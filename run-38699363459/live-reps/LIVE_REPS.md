# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.334 | 4.335 |
| energy, parked workers still on at idle power (Wh, declared model) | 481.2 | 479.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.2 | 479.4 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 270.7 | 135.9 |
| response time (ms), 95th percentile | 689.7 | 249.1 |
| response time (ms), 99th percentile | 1307 | 721.8 |
| time over the response line (% of samples) | 12.57 | 2.708 |
| failed requests (%) | 1.248 | 1.004 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.4 | 7.5 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7683 | 0.8483 |
| utilisation (used / allocatable) | 0.07853 | 0.07548 |
| CPU used (cores), mean | 1.885 | 1.812 |
| Omni's own CPU (cores), mean | 0 | 0.0092 |
| CPU used with Omni's own (cores), mean | 1.885 | 1.821 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 383.1 | 397.4 |
| HPA replicas, mean | 9.737 | 10.75 |
| pods started | 5.3 | 12.8 |
| pod start wait, total (s) | 17.6 | 28.2 |
| pod start wait, mean (s) | 2.664 | 2.26 |
| host CPU busy, the real machine under kind (%) | 54.31 | 52.9 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.066e-16 to +1.162e-15 | EVEN, the same (under one part in a million) |
| node-hours | 4.334 | 4.335 | +0.0% | -0.005546 to +0.006879 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 481.2 | 479.4 | -0.4% | -2.506 to -1.104 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 481.2 | 479.4 | -0.4% | -2.506 to -1.104 | yes: GAIN |
| response time (ms), mean | 270.7 | 135.9 | -49.8% | -179 to -90.68 | yes: GAIN |
| response time (ms), 95th percentile | 689.7 | 249.1 | -63.9% | -580.3 to -300.7 | yes: GAIN |
| response time (ms), 99th percentile | 1307 | 721.8 | -44.8% | -822.4 to -348.1 | yes: GAIN |
| time over the response line (% of samples) | 12.57 | 2.708 | -78.5% | -14.77 to -4.95 | yes: GAIN |
| failed requests (%) | 1.248 | 1.004 | -19.5% | -0.421 to -0.06529 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 21.4 | 7.5 | -65.0% | -20.05 to -7.752 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 54.3 | +54.3 (native is 0) | +36.22 to +72.38 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7683 | 0.8483 | +10.4% | -0.4757 to +0.6357 | no |
| utilisation (used / allocatable) | 0.07853 | 0.07548 | -3.9% | -0.003702 to -0.002381 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.885 | 1.812 | -3.9% | -0.08886 to -0.05715 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.0092 | +0.0092 (native is 0) | +0.007592 to +0.01081 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.885 | 1.821 | -3.4% | -0.07865 to -0.04896 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 383.1 | 397.4 | +3.7% | +10.09 to +18.53 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.737 | 10.75 | +10.4% | -0.09918 to +2.129 | no |
| pods started | 5.3 | 12.8 | +141.5% | +3.976 to +11.02 | yes: power given |
| pod start wait, total (s) | 17.6 | 28.2 | +60.2% | -0.8161 to +22.02 | no |
| pod start wait, mean (s) | 2.664 | 2.26 | -15.2% | -1.426 to +0.6191 | no |
| host CPU busy, the real machine under kind (%) | 54.31 | 52.9 | -2.6% | -1.829 to -0.9944 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*