# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 5.79 | 6 |
| node-hours | 1.509 | 1.46 | 1.51 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.8 | 172.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 168.8 | 172.4 |
| response time (ms), mean | 567.9 | 378.4 | 525.7 |
| response time (ms), 95th percentile | 2437 | 1522 | 2486 |
| response time (ms), 99th percentile | 5913 | 4358 | 6105 |
| time over the response line (% of samples) | 25.28 | 17.59 | 23.78 |
| failed requests (%) | 4.515 | 2.848 | 3.789 |
| pending pods, pod-minutes | 1.345 | 1.892 | 1.73 |
| utilisation (used / allocatable) | 0.1002 | 0.1021 | 0.09928 |
| CPU used (cores), mean | 2.404 | 2.377 | 2.383 |
| Omni's own CPU (cores), mean | 0 | 0.02341 | 0.01449 |
| CPU used with Omni's own (cores), mean | 2.404 | 2.4 | 2.397 |
| energy per core-hour (Wh, the 25 W standby model) | 295.2 | 289.9 | 297.1 |
| HPA replicas, mean | 15.31 | 15.5 | 15.27 |
| pods started | 3.9 | 2.8 | 3.3 |
| pod start wait, total (s) | 9.1 | 4.7 | 11.1 |
| pod start wait, mean (s) | 2.065 | 1.59 | 2.5 |
| second app: response time (ms), 95th percentile | 280.2 | 263.1 | 278.8 |
| second app: response time (ms), 99th percentile | 889.6 | 903.4 | 671.5 |
| second app: time over the response line (% of samples) | 15.5 | 15.28 | 15.23 |
| second app: failed requests (%) | 13.8 | 14.54 | 14.1 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.79 | -3.5% | -0.6373 to +0.2164 | no |
| node-hours | 1.509 | 1.46 | -3.2% | -0.1576 to +0.06042 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.8 | +0.1% | -0.9528 to +1.428 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 168.8 | -2.2% | -12.28 to +4.787 | no |
| response time (ms), mean | 567.9 | 378.4 | -33.4% | -282.5 to -96.54 | yes, better |
| response time (ms), 95th percentile | 2437 | 1522 | -37.5% | -1548 to -281.4 | yes, better |
| response time (ms), 99th percentile | 5913 | 4358 | -26.3% | -2881 to -227 | yes, better |
| time over the response line (% of samples) | 25.28 | 17.59 | -30.4% | -11.11 to -4.282 | yes, better |
| failed requests (%) | 4.515 | 2.848 | -36.9% | -3.322 to -0.01217 | yes, better |
| pending pods, pod-minutes | 1.345 | 1.892 | +40.6% | -0.3097 to +1.403 | no |
| utilisation (used / allocatable) | 0.1002 | 0.1021 | +1.9% | -0.003337 to +0.007241 | no |
| CPU used (cores), mean | 2.404 | 2.377 | -1.1% | -0.05809 to +0.004352 | no |
| Omni's own CPU (cores), mean | 0 | 0.02341 | +0.0234 (native is 0) | +0.02079 to +0.02603 | yes, more |
| CPU used with Omni's own (cores), mean | 2.404 | 2.4 | -0.1% | -0.03694 to +0.03002 | no |
| energy per core-hour (Wh, the 25 W standby model) | 295.2 | 289.9 | -1.8% | -19.86 to +9.341 | no |
| HPA replicas, mean | 15.31 | 15.5 | +1.2% | -0.119 to +0.4968 | no |
| pods started | 3.9 | 2.8 | -28.2% | -2.19 to -0.009955 | yes, better |
| pod start wait, total (s) | 9.1 | 4.7 | -48.4% | -8.964 to +0.164 | no |
| pod start wait, mean (s) | 2.065 | 1.59 | -23.0% | -1.115 to +0.1648 | no |
| second app: response time (ms), 95th percentile | 280.2 | 263.1 | -6.1% | -54.25 to +20.16 | no |
| second app: response time (ms), 99th percentile | 889.6 | 903.4 | +1.6% | -848 to +875.6 | no |
| second app: time over the response line (% of samples) | 15.5 | 15.28 | -1.4% | -0.8296 to +0.38 | no |
| second app: failed requests (%) | 13.8 | 14.54 | +5.3% | +0.1896 to +1.277 | yes, worse |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.675e-16 to +6.451e-16 | no |
| node-hours | 1.509 | 1.51 | +0.0% | -0.0007327 to +0.002066 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.5 | 172.4 | -0.1% | -0.3724 to +0.07732 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.5 | 172.4 | -0.1% | -0.3724 to +0.07732 | no |
| response time (ms), mean | 567.9 | 525.7 | -7.4% | -98.82 to +14.36 | no |
| response time (ms), 95th percentile | 2437 | 2486 | +2.0% | -415 to +512.6 | no |
| response time (ms), 99th percentile | 5913 | 6105 | +3.3% | -633.9 to +1019 | no |
| time over the response line (% of samples) | 25.28 | 23.78 | -5.9% | -3.425 to +0.4179 | no |
| failed requests (%) | 4.515 | 3.789 | -16.1% | -2.177 to +0.7241 | no |
| pending pods, pod-minutes | 1.345 | 1.73 | +28.6% | -0.6722 to +1.442 | no |
| utilisation (used / allocatable) | 0.1002 | 0.09928 | -0.9% | -0.00147 to -0.0002803 | yes, less |
| CPU used (cores), mean | 2.404 | 2.383 | -0.9% | -0.03527 to -0.006728 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01449 | +0.0145 (native is 0) | +0.0118 to +0.01718 | yes, more |
| CPU used with Omni's own (cores), mean | 2.404 | 2.397 | -0.3% | -0.01975 to +0.006737 | no |
| energy per core-hour (Wh, the 25 W standby model) | 295.2 | 297.1 | +0.6% | -0.01853 to +3.837 | no |
| HPA replicas, mean | 15.31 | 15.27 | -0.3% | -0.4683 to +0.3897 | no |
| pods started | 3.9 | 3.3 | -15.4% | -1.677 to +0.4769 | no |
| pod start wait, total (s) | 9.1 | 11.1 | +22.0% | -2.781 to +6.781 | no |
| pod start wait, mean (s) | 2.065 | 2.5 | +21.1% | -0.4018 to +1.272 | no |
| second app: response time (ms), 95th percentile | 280.2 | 278.8 | -0.5% | -28.08 to +25.35 | no |
| second app: response time (ms), 99th percentile | 889.6 | 671.5 | -24.5% | -863.5 to +427.3 | no |
| second app: time over the response line (% of samples) | 15.5 | 15.23 | -1.8% | -0.6016 to +0.04964 | no |
| second app: failed requests (%) | 13.8 | 14.1 | +2.1% | -0.2618 to +0.8517 | no |
