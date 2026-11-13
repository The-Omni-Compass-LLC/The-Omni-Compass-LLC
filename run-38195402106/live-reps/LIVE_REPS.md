# Repeated live runs on kind (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 6 | 5.969 |
| node-hours | 1.518 | 1.499 |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.4 |
| response time (ms), mean | 145.1 | 87.18 |
| response time (ms), 95th percentile | 293.1 | 136.2 |
| response time (ms), 99th percentile | 440 | 164.1 |
| time over the response line (% of samples) | 0.652 | 0 |
| failed requests (%) | 0 | 0 |
| pods with no machine to take them (unschedulable) | 0 | 0 |
| time pods had no machine to take them, pod-minutes | 0 | 0 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.2967 |
| utilisation (used / allocatable) | 0.03769 | 0.05026 |
| CPU used (cores), mean | 0.9045 | 1.201 |
| Omni's own CPU (cores), mean | 0 | 0.01025 |
| CPU used with Omni's own (cores), mean | 0.9045 | 1.211 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.6 | 536.8 |
| HPA replicas, mean | 8.868 | 9.254 |
| pods started | 5 | 4.8 |
| pod start wait, total (s) | 15.6 | 14.7 |
| pod start wait, mean (s) | 3.085 | 2.813 |
| host CPU busy, the real machine under kind (%) | 26.63 | 35.55 |
| host cores (the real machine under kind) | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.969 | -0.5% | -0.06626 to +0.005107 | no |
| node-hours | 1.518 | 1.499 | -1.2% | -0.02138 to -0.0154 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 159.2 | 160.9 | +1.1% | +1.019 to +2.407 | yes, worse |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 159.2 | 160.4 | +0.7% | +0.513 to +1.754 | yes, worse |
| response time (ms), mean | 145.1 | 87.18 | -39.9% | -66.91 to -48.97 | yes, better |
| response time (ms), 95th percentile | 293.1 | 136.2 | -53.5% | -170.8 to -143 | yes, better |
| response time (ms), 99th percentile | 440 | 164.1 | -62.7% | -306 to -245.9 | yes, better |
| time over the response line (% of samples) | 0.652 | 0 | -100.0% | -0.8924 to -0.4117 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pods with no machine to take them (unschedulable) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| time pods had no machine to take them, pod-minutes | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 0.2983 | 0.2967 | -0.6% | -0.4034 to +0.4001 | no |
| utilisation (used / allocatable) | 0.03769 | 0.05026 | +33.4% | +0.01028 to +0.01486 | yes, more |
| CPU used (cores), mean | 0.9045 | 1.201 | +32.8% | +0.238 to +0.3545 | yes, more |
| Omni's own CPU (cores), mean | 0 | 0.01025 | +0.0103 (native is 0) | +0.009098 to +0.0114 | yes, more |
| CPU used with Omni's own (cores), mean | 0.9045 | 1.211 | +33.9% | +0.2476 to +0.3654 | yes, more |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 697.6 | 536.8 | -23.0% | -185.3 to -136.3 | yes, less |
| HPA replicas, mean | 8.868 | 9.254 | +4.4% | +0.2345 to +0.537 | yes, worse |
| pods started | 5 | 4.8 | -4.0% | -1.142 to +0.7417 | no |
| pod start wait, total (s) | 15.6 | 14.7 | -5.8% | -9.644 to +7.844 | no |
| pod start wait, mean (s) | 3.085 | 2.813 | -8.8% | -1.513 to +0.9692 | no |
| host CPU busy, the real machine under kind (%) | 26.63 | 35.55 | +33.5% | +7.221 to +10.63 | yes, more |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*