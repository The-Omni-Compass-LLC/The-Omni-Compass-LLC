# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.031 |
| node-hours | 2.516 | 2.112 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 242.7 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 517.8 | 444.6 |
| response time (ms), 95th percentile | 3162 | 2991 |
| response time (ms), 99th percentile | 4698 | 4621 |
| time over the response line (% of samples) | 15.61 | 15 |
| failed requests (%) | 0 | 0.02938 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.8 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.7 | 190.3 |
| utilisation (used / allocatable) | 0.06193 | 0.07165 |
| CPU used (cores), mean | 1.486 | 1.436 |
| Omni's own CPU (cores), mean | 0 | 0.02377 |
| CPU used with Omni's own (cores), mean | 1.486 | 1.46 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443 | 406 |
| HPA replicas, mean | 2.062 | 2.126 |
| pods started | 0.1 | 0 |
| pod start wait, total (s) | 4.1 | 0 |
| pod start wait, mean (s) | 4.1 | 0 |
| host CPU busy, the real machine under kind (%) | 42.4 | 42.92 |
| host cores (the real machine under kind) | 4 | 4 |
| batch: queue finished (s) | 577.2 | 578.2 |
| batch: worker machines in service after the queue finished, mean | 6 | 4.433 |

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
| worker nodes in service, mean | 6 | 5.031 | -16.1% | -1.369 to -0.5683 | yes: GAIN |
| node-hours | 2.516 | 2.111 | -16.1% | -0.5724 to -0.2363 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 273.4 | 273.2 | -0.1% | -1.019 to +0.687 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.4 | 242.7 | -11.2% | -43.45 to -17.83 | yes: GAIN |
| response time (ms), mean | 517.8 | 444.6 | -14.2% | -86.99 to -59.56 | yes: GAIN |
| response time (ms), 95th percentile | 3162 | 2991 | -5.4% | -317.3 to -25.01 | yes: GAIN |
| response time (ms), 99th percentile | 4698 | 4621 | -1.6% | -262.8 to +108.7 | no |
| time over the response line (% of samples) | 15.61 | 15 | -3.9% | -1.276 to +0.05514 | no |
| failed requests (%) | 0 | 0.02938 | +0.0294 (native is 0) | -0.00458 to +0.06334 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 10 | 9.8 | -2.0% | -0.5016 to +0.1016 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 12.3 | +12.3 (native is 0) | +10.51 to +14.09 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 189.7 | 190.3 | +0.3% | -3.123 to +4.223 | no |
| utilisation (used / allocatable) | 0.06193 | 0.07165 | +15.7% | +0.005144 to +0.01429 | yes, up (shown, not judged) |
| CPU used (cores), mean | 1.486 | 1.436 | -3.4% | -0.07052 to -0.02987 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.02377 | +0.0238 (native is 0) | +0.01956 to +0.02798 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 1.486 | 1.46 | -1.8% | -0.04906 to -0.003787 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 443 | 406 | -8.4% | -59.03 to -14.99 | yes, down (shown, not judged) |
| HPA replicas, mean | 2.062 | 2.126 | +3.1% | -0.2692 to +0.3974 | no |
| pods started | 0.1 | 0 | -100.0% | -0.3262 to +0.1262 | no |
| pod start wait, total (s) | 4.1 | 0 | -100.0% | -13.37 to +5.174 | no |
| pod start wait, mean (s) | 4.1 | 0 | -100.0% | -13.37 to +5.174 | no |
| host CPU busy, the real machine under kind (%) | 42.4 | 42.92 | +1.2% | +0.2511 to +0.7818 | yes, up (shown, not judged) |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| batch: queue finished (s) | 577.2 | 578.2 | +0.2% | -2.455 to +4.455 | no |
| batch: worker machines in service after the queue finished, mean | 6 | 4.433 | -26.1% | -2.161 to -0.9729 | yes: GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*