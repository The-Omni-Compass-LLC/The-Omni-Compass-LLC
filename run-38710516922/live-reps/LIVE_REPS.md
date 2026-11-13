# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 6 |
| node-hours | 1.514 | 1.517 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.1 | 171.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.1 | 171.1 |
| energy, the machine's own meter over the window (Wh; the processor's RAPL counters, class P) | nan | nan |
| energy Kepler attributes to the service's pods (Wh; its split of the meter by each pod's CPU time: shown, not judged) | nan | nan |
| energy, Kepler's reading of the same counters (Wh; Kepler 0.11.4: shown, not judged) | nan | nan |
| response time (ms), mean | 464.8 | 382.7 |
| response time (ms), 95th percentile | 1935 | 1711 |
| response time (ms), 99th percentile | 4615 | 4378 |
| time over the response line (% of samples) | 19.97 | 18.33 |
| failed requests (%) | 1.768 | 1.95 |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.1 |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 |
| governor's additions decided while the service was still inside its line (% of its additions) | nan | nan |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9217 | 0.9283 |
| utilisation (used / allocatable) | 0.09181 | 0.09001 |
| CPU used (cores), mean | 2.203 | 2.16 |
| Omni's own CPU (cores), mean | 0 | 0.01013 |
| CPU used with Omni's own (cores), mean | 2.203 | 2.17 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 317.8 | 324.8 |
| HPA replicas, mean | 14.84 | 14.93 |
| pods started | 5.5 | 4.2 |
| pod start wait, total (s) | 12.5 | 12.4 |
| pod start wait, mean (s) | 2.149 | 2.581 |
| host CPU busy, the real machine under kind (%) | 63.25 | 62.95 |
| host cores (the real machine under kind) | 4 | 4 |
| second app: response time (ms), 95th percentile | 302.6 | 278.9 |
| second app: response time (ms), 99th percentile | 2029 | 1960 |
| second app: time over the response line (% of samples) | 12.6 | 12.48 |
| second app: failed requests (%) | 10.28 | 10.34 |

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
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.338e-16 to +4.785e-16 | EVEN, the same (under one part in a million) |
| node-hours | 1.514 | 1.517 | +0.2% | +0.001517 to +0.005483 | yes: power given |
| energy, parked workers still on at idle power (Wh, declared model) | 171.1 | 171.1 | -0.0% | -0.4813 to +0.399 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.1 | 171.1 | -0.0% | -0.4813 to +0.399 | no |
| response time (ms), mean | 464.8 | 382.7 | -17.7% | -133.1 to -31.21 | yes: GAIN |
| response time (ms), 95th percentile | 1935 | 1711 | -11.6% | -605.2 to +157.4 | no |
| response time (ms), 99th percentile | 4615 | 4378 | -5.1% | -912.2 to +437.3 | no |
| time over the response line (% of samples) | 19.97 | 18.33 | -8.2% | -3.726 to +0.4378 | no |
| failed requests (%) | 1.768 | 1.95 | +10.3% | -0.07547 to +0.4393 | no |
| alert minutes (whole minutes whose 95th percentile, failed requests counted over, was over the line) | 7.6 | 7.1 | -6.6% | -1.006 to +0.005799 | no |
| settings commands the governor wrote on its own (no person touched either arm) | 0 | 34.2 | +34.2 (native is 0) | +32.63 to +35.77 | yes, up (shown, not judged) |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.9217 | 0.9283 | +0.7% | -0.5698 to +0.5832 | no |
| utilisation (used / allocatable) | 0.09181 | 0.09001 | -2.0% | -0.002664 to -0.0009325 | yes, down (shown, not judged) |
| CPU used (cores), mean | 2.203 | 2.16 | -2.0% | -0.06393 to -0.02238 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01013 | +0.0101 (native is 0) | +0.008929 to +0.01133 | yes, up (shown, not judged) |
| CPU used with Omni's own (cores), mean | 2.203 | 2.17 | -1.5% | -0.05443 to -0.01163 | yes, down (shown, not judged) |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 317.8 | 324.8 | +2.2% | +2.44 to +11.51 | yes, up (shown, not judged) |
| HPA replicas, mean | 14.84 | 14.93 | +0.6% | -0.2633 to +0.4425 | no |
| pods started | 5.5 | 4.2 | -23.6% | -2.421 to -0.1791 | yes: GAIN |
| pod start wait, total (s) | 12.5 | 12.4 | -0.8% | -5.916 to +5.716 | no |
| pod start wait, mean (s) | 2.149 | 2.581 | +20.1% | -0.3173 to +1.181 | no |
| host CPU busy, the real machine under kind (%) | 63.25 | 62.95 | -0.5% | -0.9677 to +0.3722 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 302.6 | 278.9 | -7.8% | -96.25 to +48.86 | no |
| second app: response time (ms), 99th percentile | 2029 | 1960 | -3.4% | -1891 to +1752 | no |
| second app: time over the response line (% of samples) | 12.6 | 12.48 | -1.0% | -1.117 to +0.8773 | no |
| second app: failed requests (%) | 10.28 | 10.34 | +0.6% | -0.5267 to +0.6544 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*