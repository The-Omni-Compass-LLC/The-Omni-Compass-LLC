# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 3.85 | 4.97 |
| node-hours | 1.519 | 0.9763 | 1.256 |
| energy, parked workers still on at idle power (Wh, declared model) | 160.5 | 160.3 | 159.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.5 | 119.4 | 140.3 |
| response time (ms), mean | 180.7 | 105 | 92.52 |
| response time (ms), 95th percentile | 414.3 | 184.7 | 146 |
| response time (ms), 99th percentile | 699.4 | 289.2 | 214.3 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.2617 | 0.1067 | 0.1867 |
| utilisation (used / allocatable) | 0.04291 | 0.06103 | 0.04883 |
| CPU used (cores), mean | 1.03 | 0.9424 | 0.9663 |
| Omni's own CPU (cores), mean | 0 | 0.07228 | 0.07441 |
| CPU used with Omni's own (cores), mean | 1.03 | 1.015 | 1.041 |
| energy per core-hour (Wh, the 25 W standby model) | 642.3 | 515.1 | 586.9 |
| HPA replicas, mean | 8.845 | 7.487 | 8.538 |
| pods started | 4 | 3.7 | 1.9 |
| pod start wait, total (s) | 13 | 7.4 | 2.9 |
| pod start wait, mean (s) | 2.93 | 2.01 | 1.383 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.85 | -35.8% | -2.365 to -1.934 | yes, better |
| node-hours | 1.519 | 0.9763 | -35.7% | -0.5972 to -0.4883 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160.5 | 160.3 | -0.1% | -0.9025 to +0.4403 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.5 | 119.4 | -25.6% | -45.15 to -37.08 | yes, better |
| response time (ms), mean | 180.7 | 105 | -41.9% | -89.98 to -61.37 | yes, better |
| response time (ms), 95th percentile | 414.3 | 184.7 | -55.4% | -267.7 to -191.6 | yes, better |
| response time (ms), 99th percentile | 699.4 | 289.2 | -58.6% | -491.7 to -328.6 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2617 | 0.1067 | -59.2% | -0.4085 to +0.09846 | no |
| utilisation (used / allocatable) | 0.04291 | 0.06103 | +42.2% | +0.0156 to +0.02064 | yes, more |
| CPU used (cores), mean | 1.03 | 0.9424 | -8.5% | -0.1096 to -0.0655 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.07228 | +0.0723 (native is 0) | +0.06594 to +0.07862 | yes, more |
| CPU used with Omni's own (cores), mean | 1.03 | 1.015 | -1.5% | -0.03376 to +0.003268 | no |
| energy per core-hour (Wh, the 25 W standby model) | 642.3 | 515.1 | -19.8% | -179.5 to -74.95 | yes, better |
| HPA replicas, mean | 8.845 | 7.487 | -15.4% | -1.916 to -0.8012 | yes, better |
| pods started | 4 | 3.7 | -7.5% | -1.257 to +0.6567 | no |
| pod start wait, total (s) | 13 | 7.4 | -43.1% | -14.3 to +3.097 | no |
| pod start wait, mean (s) | 2.93 | 2.01 | -31.4% | -2.329 to +0.4885 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.97 | -17.2% | -1.584 to -0.4764 | yes, better |
| node-hours | 1.519 | 1.256 | -17.3% | -0.401 to -0.1258 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160.5 | 159.8 | -0.4% | -1.452 to +0.07024 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160.5 | 140.3 | -12.6% | -30.32 to -10.12 | yes, better |
| response time (ms), mean | 180.7 | 92.52 | -48.8% | -106 to -70.33 | yes, better |
| response time (ms), 95th percentile | 414.3 | 146 | -64.8% | -318.9 to -217.8 | yes, better |
| response time (ms), 99th percentile | 699.4 | 214.3 | -69.4% | -590.9 to -379.3 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2617 | 0.1867 | -28.7% | -0.3409 to +0.1909 | no |
| utilisation (used / allocatable) | 0.04291 | 0.04883 | +13.8% | +0.0008535 to +0.01098 | yes, more |
| CPU used (cores), mean | 1.03 | 0.9663 | -6.2% | -0.08302 to -0.04428 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.07441 | +0.0744 (native is 0) | +0.06791 to +0.08091 | yes, more |
| CPU used with Omni's own (cores), mean | 1.03 | 1.041 | +1.0% | -0.006798 to +0.02832 | no |
| energy per core-hour (Wh, the 25 W standby model) | 642.3 | 586.9 | -8.6% | -128.5 to +17.62 | no |
| HPA replicas, mean | 8.845 | 8.538 | -3.5% | -0.8582 to +0.2427 | no |
| pods started | 4 | 1.9 | -52.5% | -3.425 to -0.7746 | yes, better |
| pod start wait, total (s) | 13 | 2.9 | -77.7% | -18.11 to -2.089 | yes, better |
| pod start wait, mean (s) | 2.93 | 1.383 | -52.8% | -2.998 to -0.09574 | yes, better |
