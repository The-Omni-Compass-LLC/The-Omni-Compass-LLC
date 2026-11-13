# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.856 |
| node-hours | 2.508 | 2.034 |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 236.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 513.1 | 447.7 |
| response time (ms), 95th percentile | 3095 | 3015 |
| response time (ms), 99th percentile | 4604 | 4641 |
| time over the response line (% of samples) | 15.6 | 15.15 |
| failed requests (%) | 0 | 0 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 185.3 | 187.1 |
| utilisation (used / allocatable) | 0.06167 | 0.07493 |
| CPU used (cores), mean | 1.48 | 1.452 |
| Omni's own CPU (cores), mean | 0 | 0.02393 |
| CPU used with Omni's own (cores), mean | 1.48 | 1.476 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 391.6 |
| HPA replicas, mean | 1.976 | 2.171 |
| pods started | 0.1 | 0.2 |
| pod start wait, total (s) | 4.7 | 8.4 |
| pod start wait, mean (s) | 4.7 | 8.4 |
| host CPU busy, the real machine under kind (%) | 42.39 | 42.88 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 573.8 | 577.1 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.176 |

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
| worker nodes in service, mean | 6 | 4.856 | -19.1% | -1.583 to -0.7049 | yes: GAIN |
| node-hours | 2.508 | 2.034 | -18.9% | -0.6597 to -0.2885 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 272.2 | 272.6 | +0.1% | -0.3213 to +1.098 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 272.2 | 236.7 | -13.1% | -49.18 to -21.88 | yes: GAIN |
| response time (ms), mean | 513.1 | 447.7 | -12.7% | -78.03 to -52.71 | yes: GAIN |
| response time (ms), 95th percentile | 3095 | 3015 | -2.6% | -248.1 to +87.9 | no |
| response time (ms), 99th percentile | 4604 | 4641 | +0.8% | -143.5 to +217.9 | no |
| time over the response line (% of samples) | 15.6 | 15.15 | -2.9% | -0.8642 to -0.04018 | yes: GAIN |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 9.9 | 10 | +1.0% | -0.1262 to +0.3262 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.5 | +12.5 (native is 0) | +11.1 to +13.9 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 185.3 | 187.1 | +1.0% | -4.167 to +7.863 | no |
| utilisation (used / allocatable) | 0.06167 | 0.07493 | +21.5% | +0.007492 to +0.01901 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.48 | 1.452 | -1.9% | -0.0591 to +0.00298 | no |
| Omni's own CPU (cores), mean | 0 | 0.02393 | +0.0239 (native is 0) | +0.02017 to +0.02769 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.48 | 1.476 | -0.3% | -0.03442 to +0.02616 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 447.3 | 391.6 | -12.4% | -86.62 to -24.74 | yes, down (shown, not judged) |
| HPA replicas, mean | 1.976 | 2.171 | +9.9% | -0.04183 to +0.4335 | no |
| pods started | 0.1 | 0.2 | +100.0% | -0.306 to +0.506 | no |
| pod start wait, total (s) | 4.7 | 8.4 | +78.7% | -14.19 to +21.59 | no |
| pod start wait, mean (s) | 4.7 | 8.4 | +78.7% | -14.19 to +21.59 | no |
| host CPU busy, the real machine under kind (%) | 42.39 | 42.88 | +1.2% | +0.1004 to +0.8906 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 573.8 | 577.1 | +0.6% | -1.084 to +7.684 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.176 | -30.4% | -2.454 to -1.194 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*