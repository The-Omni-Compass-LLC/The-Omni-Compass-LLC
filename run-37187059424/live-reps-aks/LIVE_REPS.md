# Repeated live runs on Azure Kubernetes Service (AKS), billed machines (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 1.857 | 1.761 | 1.849 |
| node-hours | 0.4696 | 0.4464 | 0.4692 |
| energy, parked workers still on at idle power (Wh, declared model) | 85.91 | 86.35 | 85.77 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 83.21 | 81.81 | 82.89 |
| response time (ms), mean | 507.5 | 528.4 | 476.5 |
| response time (ms), 95th percentile | 1423 | 1192 | 1092 |
| response time (ms), 99th percentile | 4486 | 5870 | 4030 |
| time over the response line (% of samples) | 26.79 | 31.71 | 27.15 |
| failed requests (%) | 4.426 | 6.748 | 3.911 |
| pending pods, pod-minutes | 4.867 | 5.647 | 5.533 |
| utilisation (used / allocatable) | 0.476 | 0.5125 | 0.4854 |
| CPU used (cores), mean | 1.673 | 1.713 | 1.7 |
| Omni's own CPU (cores), mean | 0 | 0.01216 | 0.01262 |
| CPU used with Omni's own (cores), mean | 1.673 | 1.726 | 1.712 |
| energy per core-hour (Wh, the 25 W standby model) | 197.5 | 188.4 | 192.8 |
| HPA replicas, mean | 9.474 | 9.176 | 9.462 |
| pods started | 6 | 6.2 | 5 |
| pod start wait, total (s) | 211.8 | 269.6 | 241.6 |
| pod start wait, mean (s) | 36.28 | 45.3 | 48.32 |
| machines billed, machine-hours | 0.615 | 0.6081 | 0.6108 |
| compute bill at list price ($) | 0.05904 | 0.05838 | 0.05864 |

**The bill is Azure's own count of machines.** Every worker machine that exists is billed, in service or idle;
Azure's cluster autoscaler deletes a machine once it is empty. Machine-hours are integrated every 15 s over the
measured window and priced at the list price per machine-hour. The energy rows remain the declared model.

## B: Omni-Compass on top vs native, 4 paired repetitions

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
| Omni's own CPU (cores), mean | 0 | 0.01315 | +0.0132 (native is 0) | +0.01226 to +0.01404 | yes, more |
| CPU used with Omni's own (cores), mean | 1.673 | 1.74 | +4.0% | -0.0838 to +0.2176 | no |
| energy per core-hour (Wh, the 25 W standby model) | 197.5 | 187.1 | -5.3% | -34.39 to +13.55 | no |
| HPA replicas, mean | 9.474 | 9.125 | -3.7% | -0.6744 to -0.02221 | yes, better |
| pods started | 6 | 6.5 | +8.3% | -4.093 to +5.093 | no |
| pod start wait, total (s) | 211.8 | 282 | +33.2% | -161.3 to +301.8 | no |
| pod start wait, mean (s) | 36.28 | 45.63 | +25.8% | -41.2 to +59.89 | no |
| machines billed, machine-hours | 0.615 | 0.6116 | -0.6% | -0.1364 to +0.1296 | no |
| compute bill at list price ($) | 0.05904 | 0.05871 | -0.6% | -0.01309 to +0.01244 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 4 paired repetitions

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
| Omni's own CPU (cores), mean | 0 | 0.01367 | +0.0137 (native is 0) | +0.01187 to +0.01548 | yes, more |
| CPU used with Omni's own (cores), mean | 1.673 | 1.715 | +2.5% | -0.2826 to +0.3651 | no |
| energy per core-hour (Wh, the 25 W standby model) | 197.5 | 193.2 | -2.2% | -48.03 to +39.4 | no |
| HPA replicas, mean | 9.474 | 9.465 | -0.1% | -0.4911 to +0.4746 | no |
| pods started | 6 | 5 | -16.7% | -4.182 to +2.182 | no |
| pod start wait, total (s) | 211.8 | 235.2 | +11.1% | -346.1 to +393.1 | no |
| pod start wait, mean (s) | 36.28 | 47.05 | +29.7% | -68.86 to +90.39 | no |
| machines billed, machine-hours | 0.615 | 0.6201 | +0.8% | -0.1966 to +0.2068 | no |
| compute bill at list price ($) | 0.05904 | 0.05953 | +0.8% | -0.01888 to +0.01985 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 0.0 |  |  | 1 |
