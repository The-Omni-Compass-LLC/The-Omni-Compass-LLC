# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native against omni: Omni-Compass on top of native)

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.


## All columns, mean over repetitions

| Gauge | native | omni |
|---|---:|---:|
| worker nodes in service, mean | 1.922 | 1.922 |
| node-hours | 0.9663 | 0.9682 |
| energy, parked workers still on at idle power (Wh, declared model) | 186.1 | 184.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 181.9 |
| response time (ms), mean | 477.1 | 427.6 |
| response time (ms), 95th percentile | 1270 | 897.8 |
| response time (ms), 99th percentile | 4747 | 4719 |
| time over the response line (% of samples) | 33.78 | 33.81 |
| failed requests (%) | 18.03 | 21.82 |
| pods with no machine to take them (unschedulable) | 2.25 | 2.5 |
| time pods had no machine to take them, pod-minutes | 3.3 | 3.058 |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.383 | 5.55 |
| utilisation (used / allocatable) | 0.5895 | 0.5916 |
| CPU used (cores), mean | 2.152 | 2.161 |
| Omni's own CPU (cores), mean | 0 | 0.0124 |
| CPU used with Omni's own (cores), mean | 2.152 | 2.174 |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 169.2 | 167.2 |
| HPA replicas, mean | 9.684 | 9.765 |
| pods started | 5.25 | 5 |
| pod start wait, total (s) | 238 | 220 |
| pod start wait, mean (s) | 44.83 | 44 |
| machines billed, machine-hours | 1.129 | 1.07 |
| compute bill at list price ($) | 0.1084 | 0.1027 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## omni (compass law): Omni-Compass on top of native, push and pull on the HPA target and the node pool vs native, 4 paired repetitions

| Gauge | native | omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 1.922 | 1.922 | +0.0% | -0.08132 to +0.08298 | no |
| node-hours | 0.9663 | 0.9682 | +0.2% | -0.04339 to +0.04714 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 186.1 | 184.8 | -0.7% | -10.4 to +7.762 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 181.9 | -0.7% | -13.43 to +10.85 | no |
| response time (ms), mean | 477.1 | 427.6 | -10.4% | -162.4 to +63.36 | no |
| response time (ms), 95th percentile | 1270 | 897.8 | -29.3% | -816 to +71.88 | no |
| response time (ms), 99th percentile | 4747 | 4719 | -0.6% | -2462 to +2405 | no |
| time over the response line (% of samples) | 33.78 | 33.81 | +0.1% | -2.321 to +2.383 | no |
| failed requests (%) | 18.03 | 21.82 | +21.0% | -11.31 to +18.88 | no |
| pods with no machine to take them (unschedulable) | 2.25 | 2.5 | +11.1% | -3.03 to +3.53 | no |
| time pods had no machine to take them, pod-minutes | 3.3 | 3.058 | -7.3% | -3.663 to +3.18 | no |
| pending pods in a 15 s snapshot, pod-minutes (a pod being started counts too: shown, not judged) | 5.383 | 5.55 | +3.1% | -5.123 to +5.457 | no |
| utilisation (used / allocatable) | 0.5895 | 0.5916 | +0.4% | -0.02391 to +0.02814 | no |
| CPU used (cores), mean | 2.152 | 2.161 | +0.4% | -0.1505 to +0.1686 | no |
| Omni's own CPU (cores), mean | 0 | 0.0124 | +0.0124 (native is 0) | +0.01186 to +0.01294 | yes, more |
| CPU used with Omni's own (cores), mean | 2.152 | 2.174 | +1.0% | -0.1376 to +0.1805 | no |
| energy per core-hour (Wh, the 25 W standby model; a ratio over CPU used: shown, not judged) | 169.2 | 167.2 | -1.2% | -7.835 to +3.653 | no |
| HPA replicas, mean | 9.684 | 9.765 | +0.8% | +0.02047 to +0.1419 | yes, worse |
| pods started | 5.25 | 5 | -4.8% | -1.046 to +0.5455 | no |
| pod start wait, total (s) | 238 | 220 | -7.6% | -262.5 to +226.5 | no |
| pod start wait, mean (s) | 44.83 | 44 | -1.9% | -49.76 to +48.1 | no |
| machines billed, machine-hours | 1.129 | 1.07 | -5.3% | -0.1588 to +0.04016 | no |
| compute bill at list price ($) | 0.1084 | 0.1027 | -5.3% | -0.01524 to +0.003855 | no |


---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Patents, copyrights and trademarks filed. See `LICENSE`, `NOTICE` and `DISCLOSURES.md`.*