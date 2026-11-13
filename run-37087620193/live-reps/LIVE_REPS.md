# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 4.222 | 5.715 |
| node-hours | 1.518 | 1.068 | 1.442 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.8 | 159.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 126.1 | 154 |
| response time (ms), mean | 169.4 | 96.46 | 87.65 |
| response time (ms), 95th percentile | 381.9 | 160.4 | 132.4 |
| response time (ms), 99th percentile | 593.3 | 242 | 186 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.295 | 0.08 | 0 |
| utilisation (used / allocatable) | 0.04178 | 0.05533 | 0.04207 |
| CPU used (cores), mean | 1.003 | 0.9232 | 0.9626 |
| Omni's own CPU (cores), mean | 0 | 0.06784 | 0.0627 |
| CPU used with Omni's own (cores), mean | 1.003 | 0.9911 | 1.025 |
| energy per core-hour (Wh, the 25 W standby model) | 653.1 | 550.8 | 650.4 |
| HPA replicas, mean | 8.852 | 6.471 | 8.367 |
| pods started | 4.9 | 2.8 | 3.3 |
| pod start wait, total (s) | 16.7 | 6.3 | 8.9 |
| pod start wait, mean (s) | 3.15 | 1.787 | 2.241 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.222 | -29.6% | -2.254 to -1.302 | yes, better |
| node-hours | 1.518 | 1.068 | -29.6% | -0.57 to -0.33 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.8 | -0.3% | -1.033 to +0.1884 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 126.1 | -21.3% | -42.97 to -25.38 | yes, better |
| response time (ms), mean | 169.4 | 96.46 | -43.1% | -88.92 to -56.99 | yes, better |
| response time (ms), 95th percentile | 381.9 | 160.4 | -58.0% | -259.9 to -183 | yes, better |
| response time (ms), 99th percentile | 593.3 | 242 | -59.2% | -427.3 to -275.2 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.295 | 0.08 | -72.9% | -0.4664 to +0.03636 | no |
| utilisation (used / allocatable) | 0.04178 | 0.05533 | +32.4% | +0.007892 to +0.01922 | yes, more |
| CPU used (cores), mean | 1.003 | 0.9232 | -7.9% | -0.1021 to -0.05685 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.06784 | +0.0678 (native is 0) | +0.06099 to +0.07469 | yes, more |
| CPU used with Omni's own (cores), mean | 1.003 | 0.9911 | -1.2% | -0.02833 to +0.005093 | no |
| energy per core-hour (Wh, the 25 W standby model) | 653.1 | 550.8 | -15.7% | -162.2 to -42.53 | yes, better |
| HPA replicas, mean | 8.852 | 6.471 | -26.9% | -3.427 to -1.334 | yes, better |
| pods started | 4.9 | 2.8 | -42.9% | -3.834 to -0.3658 | yes, better |
| pod start wait, total (s) | 16.7 | 6.3 | -62.3% | -18.82 to -1.975 | yes, better |
| pod start wait, mean (s) | 3.15 | 1.787 | -43.3% | -2.658 to -0.06823 | yes, better |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.715 | -4.7% | -0.3913 to -0.1779 | yes, better |
| node-hours | 1.518 | 1.442 | -5.0% | -0.1029 to -0.04985 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160.2 | 159.4 | -0.5% | -1.686 to +0.02712 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.2 | 154 | -3.9% | -8.233 to -4.185 | yes, better |
| response time (ms), mean | 169.4 | 87.65 | -48.3% | -100 to -63.51 | yes, better |
| response time (ms), 95th percentile | 381.9 | 132.4 | -65.3% | -297.3 to -201.6 | yes, better |
| response time (ms), 99th percentile | 593.3 | 186 | -68.6% | -486.5 to -327.9 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.295 | 0 | -100.0% | -0.5233 to -0.06671 | yes, better |
| utilisation (used / allocatable) | 0.04178 | 0.04207 | +0.7% | -0.0009075 to +0.001495 | no |
| CPU used (cores), mean | 1.003 | 0.9626 | -4.0% | -0.06377 to -0.01653 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0627 | +0.0627 (native is 0) | +0.05672 to +0.06868 | yes, more |
| CPU used with Omni's own (cores), mean | 1.003 | 1.025 | +2.2% | +0.00319 to +0.04191 | yes, more |
| energy per core-hour (Wh, the 25 W standby model) | 653.1 | 650.4 | -0.4% | -22.27 to +16.84 | no |
| HPA replicas, mean | 8.852 | 8.367 | -5.5% | -1.241 to +0.2722 | no |
| pods started | 4.9 | 3.3 | -32.7% | -2.957 to -0.2428 | yes, better |
| pod start wait, total (s) | 16.7 | 8.9 | -46.7% | -13.89 to -1.714 | yes, better |
| pod start wait, mean (s) | 3.15 | 2.241 | -28.9% | -1.846 to +0.02798 | no |
