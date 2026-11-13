# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 4.331 | 4.332 |
| energy, parked workers still on at idle power (Wh, declared model) | 485.9 | 483.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.9 | 483.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 307.5 | 149.6 |
| response time (ms), 95th percentile | 792.9 | 294.8 |
| response time (ms), 99th percentile | 1604 | 679.7 |
| time over the response line (% of samples) | 14.92 | 3.091 |
| failed requests (%) | 1.452 | 1.256 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.1 | 9.4 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 12.5 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7883 | 1.105 |
| utilisation (used / allocatable) | 0.08619 | 0.08271 |
| CPU used (cores), mean | 2.069 | 1.985 |
| Omni's own CPU (cores), mean | 0 | 0.00997 |
| CPU used with Omni's own (cores), mean | 2.069 | 1.995 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 333.3 | 345.6 |
| HPA replicas, mean | 9.873 | 11.16 |
| pods started | 4.7 | 13.5 |
| pod start wait, total (s) | 15.1 | 28.7 |
| pod start wait, mean (s) | 2.971 | 2.163 |
| host CPU busy, the real machine under kind (%) | 59.47 | 57.75 |
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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.471e-16 to +8.471e-16 | no |
| node-hours | 4.331 | 4.332 | +0.0% | -0.009251 to +0.01025 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 485.9 | 483.7 | -0.4% | -3.321 to -1.022 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 485.9 | 483.7 | -0.4% | -3.321 to -1.022 | yes: GAIN |
| response time (ms), mean | 307.5 | 149.6 | -51.4% | -187.4 to -128.6 | yes: GAIN |
| response time (ms), 95th percentile | 792.9 | 294.8 | -62.8% | -579.8 to -416.4 | yes: GAIN |
| response time (ms), 99th percentile | 1604 | 679.7 | -57.6% | -1081 to -768.3 | yes: GAIN |
| time over the response line (% of samples) | 14.92 | 3.091 | -79.3% | -15.55 to -8.104 | yes: GAIN |
| failed requests (%) | 1.452 | 1.256 | -13.5% | -0.3228 to -0.06911 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 26.1 | 9.4 | -64.0% | -20 to -13.4 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 61.1 | +61.1 (native is 0) | +48.17 to +74.03 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.7883 | 1.105 | +40.2% | -0.04997 to +0.6833 | no |
| utilisation (used / allocatable) | 0.08619 | 0.08271 | -4.0% | -0.00418 to -0.002796 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.069 | 1.985 | -4.0% | -0.1003 to -0.0671 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00997 | +0.00997 (native is 0) | +0.008726 to +0.01121 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.069 | 1.995 | -3.6% | -0.08983 to -0.05766 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 333.3 | 345.6 | +3.7% | +10.31 to +14.45 | yes, up (shown, not judged) |
| HPA replicas, mean | 9.873 | 11.16 | +13.0% | +0.3563 to +2.212 | yes: power given |
| pods started | 4.7 | 13.5 | +187.2% | +5.788 to +11.81 | yes: power given |
| pod start wait, total (s) | 15.1 | 28.7 | +90.1% | +7.719 to +19.48 | yes: LOSS |
| pod start wait, mean (s) | 2.971 | 2.163 | -27.2% | -1.649 to +0.03385 | no |
| host CPU busy, the real machine under kind (%) | 59.47 | 57.75 | -2.9% | -2.151 to -1.284 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*