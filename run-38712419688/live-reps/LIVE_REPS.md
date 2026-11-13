# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 5.914 | 5.913 |
| node-hours | 1.498 | 1.489 |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 165.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.5 | 164.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 201 | 144.8 |
| response time (ms), 95th percentile | 378 | 148.8 |
| response time (ms), 99th percentile | 1217 | 998.6 |
| time over the response line (% of samples) | 8.493 | 6.012 |
| failed requests (%) | 5.911 | 4.917 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 5.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.1 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | 100 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.79 |
| utilisation (used / allocatable) | 0.07507 | 0.07292 |
| CPU used (cores), mean | 1.776 | 1.725 |
| Omni's own CPU (cores), mean | 0 | 0.01027 |
| CPU used with Omni's own (cores), mean | 1.776 | 1.735 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 374.3 | 382.7 |
| HPA replicas, mean | 8.888 | 10.84 |
| pods started | 4.3 | 4.6 |
| pod start wait, total (s) | 12.1 | 13.7 |
| pod start wait, mean (s) | 2.475 | 2.586 |
| host CPU busy, the real machine under kind (%) | 50.54 | 49.42 |
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
| worker nodes in service, mean | 5.914 | 5.913 | -0.0% | -0.0019 to -0.000194 | yes: GAIN |
| node-hours | 1.498 | 1.489 | -0.6% | -0.0194 to +0.001791 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 165.7 | -0.8% | -2.615 to -0.2095 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.5 | 164.1 | -0.9% | -2.625 to -0.2208 | yes: GAIN |
| response time (ms), mean | 201 | 144.8 | -28.0% | -84.4 to -27.98 | yes: GAIN |
| response time (ms), 95th percentile | 378 | 148.8 | -60.6% | -282.2 to -176.1 | yes: GAIN |
| response time (ms), 99th percentile | 1217 | 998.6 | -18.0% | -580.3 to +142.6 | no |
| time over the response line (% of samples) | 8.493 | 6.012 | -29.2% | -3.514 to -1.447 | yes: GAIN |
| failed requests (%) | 5.911 | 4.917 | -16.8% | -1.606 to -0.3814 | yes: GAIN |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.4 | 5.8 | -21.6% | -2.566 to -0.6344 | yes: GAIN |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 30.1 | +30.1 (native is 0) | +25.25 to +34.95 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.3017 | 0.79 | +161.9% | +0.09505 to +0.8816 | yes, up (shown, not judged) |
| utilisation (used / allocatable) | 0.07507 | 0.07292 | -2.9% | -0.003533 to -0.0007602 | yes, down (shown, not judged) |
| CPU used (cores), mean | 1.776 | 1.725 | -2.9% | -0.0838 to -0.01837 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01027 | +0.0103 (native is 0) | +0.009181 to +0.01136 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.776 | 1.735 | -2.3% | -0.07309 to -0.008547 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 374.3 | 382.7 | +2.2% | +2.075 to +14.7 | yes, up (shown, not judged) |
| HPA replicas, mean | 8.888 | 10.84 | +21.9% | +0.8422 to +3.058 | yes: power given |
| pods started | 4.3 | 4.6 | +7.0% | -1.247 to +1.847 | no |
| pod start wait, total (s) | 12.1 | 13.7 | +13.2% | -4.992 to +8.192 | no |
| pod start wait, mean (s) | 2.475 | 2.586 | +4.5% | -0.6444 to +0.8663 | no |
| host CPU busy, the real machine under kind (%) | 50.54 | 49.42 | -2.2% | -2.022 to -0.2079 | yes, down (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; a fall is a shorter time in both, a GAIN, and a rise a LOSS.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 69 | 14.2 |  |
| machine down | omni | 42 | 9.8 | -28 s (-40%) |
| spike | native | 278 | 73.2 |  |
| spike | omni | 277 | 68.0 | -1 s (-0%) |
| runaway pod started | native | 128 | 13.7 |  |
| runaway pod started | omni | 99 | 8.1 | -29 s (-23%) |
| probe blind | native | 67 | 0.6 |  |
| probe blind | omni | 54 | 0.1 | -13 s (-19%) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*