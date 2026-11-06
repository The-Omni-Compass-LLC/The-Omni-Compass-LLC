# The bill on a real cloud: Azure Kubernetes Service, Azure's own cluster autoscaler underneath, 4 paired repetitions

> © 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `aks-metered`, run 37187059424, commit `5b2832f`, 2026-10-04, job `aggregate` (job
111467353670). Artifact `live-reps-aks` (zip SHA-256 `75a545d88505e764a5a5ace0255f4ff977b4a5fa3cbd232d1efca557b15bdad8`).
eastus, `Standard_D2s_v4` workers (2 vCPU, 8 GiB, USD 0.096 an hour; the subscription does not allow the preregistered
`Standard_D2s_v5` in eastus, same size and price), one system machine and a work pool of 1 to 4 under Azure's
autoscaler, a fresh cluster per arm, deleted after it. Arms native / compass / omni, order rotated, 900 measured seconds.
Repetition 2 lost an arm and is excluded, as preregistered; four paired repetitions remain. Three earlier attempts
(runs 37171672509, 37178992436, 37183307625) stopped before any measurement at the load generator's placement (kind's
control-plane selector kept beside the AKS one) and are not results. Evidence class **L**, the bill **metered** (Azure's
own count of machines every 15 s, priced at list).

**Result. No difference in the bill, either way, and no LOSS clear of the noise.** Native 0.615 machine-hours
(USD 0.059 a 15-minute window); with the allocation law −0.6%, with the compass law +0.8%, intervals across zero. Azure's own
autoscaler already ran this workload on about 1.86 workers out of 4: on a real cloud with a node autoscaler underneath,
this light workload leaves Omni-Compass no machine to give back. The machine savings measured on kind (where the native
arm has no node autoscaler and all six workers stay on) do not carry to this setting, and that is now the reading of
record. Four repetitions with wide intervals: no saving shown, none excluded at the size of the kind results either.

## B: the allocation law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.857 | 1.752 | -5.7% | -0.2367 to +0.02554 | no |
| node-hours | 0.4696 | 0.4438 | -5.5% | -0.06027 to +0.008606 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.91 | 86.55 | +0.8% | -0.9189 to +2.215 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.21 | 81.84 | -1.6% | -4.434 to +1.689 | no |
| response time (ms), mean | 507.5 | 536.9 | +5.8% | -164.5 to +223.4 | no |
| response time (ms), 95th percentile | 1423 | 1180 | -17.1% | -970.5 to +483.9 | no |
| response time (ms), 99th percentile | 4486 | 6171 | +37.6% | -3333 to +6703 | no |
| time over the response line (% of samples) | 26.79 | 31.97 | +19.3% | -3.457 to +13.81 | no |
| failed requests (%) | 4.426 | 7.102 | +60.5% | -1.726 to +7.079 | no |
| pending pods, pod-minutes | 4.867 | 5.733 | +17.8% | -4.707 to +6.44 | no |
| utilisation (used / allocatable) | 0.476 | 0.5193 | +9.1% | -0.02881 to +0.1154 | no |
| CPU used (cores), mean | 1.673 | 1.727 | +3.2% | -0.0967 to +0.2042 | no |
| Omni's own CPU (cores), mean | 0 | 0.01315 | +0.0132 (native is 0) | +0.01226 to +0.01404 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.673 | 1.74 | +4.0% | -0.0838 to +0.2176 | no |
| energy per core-hour (Wh, the 25 W standby model) | 197.5 | 187.1 | -5.3% | -34.39 to +13.55 | no |
| HPA replicas, mean | 9.474 | 9.125 | -3.7% | -0.6744 to -0.02221 | yes: GAIN |
| pods started | 6 | 6.5 | +8.3% | -4.093 to +5.093 | no |
| pod start wait, total (s) | 211.8 | 282 | +33.2% | -161.3 to +301.8 | no |
| pod start wait, mean (s) | 36.28 | 45.63 | +25.8% | -41.2 to +59.89 | no |
| machines billed, machine-hours | 0.615 | 0.6116 | -0.6% | -0.1364 to +0.1296 | no |
| compute bill at list price ($) | 0.05904 | 0.05871 | -0.6% | -0.01309 to +0.01244 | no |

## B with the compass law vs native

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.857 | 1.852 | -0.3% | -0.2451 to +0.235 | no |
| node-hours | 0.4696 | 0.4697 | +0.0% | -0.06305 to +0.06319 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 85.91 | 85.8 | -0.1% | -4.315 to +4.1 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.21 | 82.99 | -0.3% | -5.891 to +5.457 | no |
| response time (ms), mean | 507.5 | 481.3 | -5.2% | -222.9 to +170.5 | no |
| response time (ms), 95th percentile | 1423 | 1135 | -20.2% | -1218 to +641.4 | no |
| response time (ms), 99th percentile | 4486 | 4169 | -7.1% | -5434 to +4799 | no |
| time over the response line (% of samples) | 26.79 | 27.61 | +3.1% | -7.188 to +8.831 | no |
| failed requests (%) | 4.426 | 3.868 | -12.6% | -9.343 to +8.229 | no |
| pending pods, pod-minutes | 4.867 | 5.171 | +6.3% | -7.794 to +8.402 | no |
| utilisation (used / allocatable) | 0.476 | 0.4853 | +1.9% | -0.1359 to +0.1544 | no |
| CPU used (cores), mean | 1.673 | 1.701 | +1.6% | -0.2966 to +0.3517 | no |
| Omni's own CPU (cores), mean | 0 | 0.01367 | +0.0137 (native is 0) | +0.01187 to +0.01548 | yes: power given |
| CPU used with Omni's own (cores), mean | 1.673 | 1.715 | +2.5% | -0.2826 to +0.3651 | no |
| energy per core-hour (Wh, the 25 W standby model) | 197.5 | 193.2 | -2.2% | -48.03 to +39.4 | no |
| HPA replicas, mean | 9.474 | 9.465 | -0.1% | -0.4911 to +0.4746 | no |
| pods started | 6 | 5 | -16.7% | -4.182 to +2.182 | no |
| pod start wait, total (s) | 211.8 | 235.2 | +11.1% | -346.1 to +393.1 | no |
| pod start wait, mean (s) | 36.28 | 47.05 | +29.7% | -68.86 to +90.39 | no |
| machines billed, machine-hours | 0.615 | 0.6201 | +0.8% | -0.1966 to +0.2068 | no |
| compute bill at list price ($) | 0.05904 | 0.05953 | +0.8% | -0.01888 to +0.01985 | no |

The energy rows remain the declared model; the bill rows are metered.

---

*© 2026 The Omni-Compass LLC / Dubra Software. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC / Dubra Software. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
