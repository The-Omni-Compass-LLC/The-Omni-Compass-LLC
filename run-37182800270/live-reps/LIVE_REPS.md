# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 5.531 | 5.92 |
| node-hours | 2.681 | 2.473 | 2.645 |
| energy, parked workers still on at idle power (Wh, declared model) | 306.6 | 306.2 | 305.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.6 | 290.4 | 303.1 |
| response time (ms), mean | 342.3 | 213 | 205.5 |
| response time (ms), 95th percentile | 932.6 | 452.7 | 463.8 |
| response time (ms), 99th percentile | 3516 | 3269 | 2805 |
| time over the response line (% of samples) | 20.11 | 10.27 | 10.66 |
| failed requests (%) | 7.518 | 6.299 | 6.545 |
| pending pods, pod-minutes | 0.4883 | 0.3283 | 0.375 |
| utilisation (used / allocatable) | 0.1006 | 0.1067 | 0.1 |
| CPU used (cores), mean | 2.415 | 2.363 | 2.366 |
| Omni's own CPU (cores), mean | 0 | 0.01487 | 0.01077 |
| CPU used with Omni's own (cores), mean | 2.415 | 2.378 | 2.376 |
| energy per core-hour (Wh, the 25 W standby model) | 294.4 | 278.3 | 298.3 |
| HPA replicas, mean | 9.253 | 9.29 | 9.039 |
| pods started | 4.4 | 3.7 | 4.3 |
| pod start wait, total (s) | 15 | 5.7 | 10 |
| pod start wait, mean (s) | 2.924 | 1.372 | 2.043 |
| host CPU busy, the real machine under kind (%) | 69.77 | 68.85 | 68.62 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.531 | -7.8% | -1.115 to +0.176 | no |
| node-hours | 2.681 | 2.473 | -7.8% | -0.4924 to +0.07607 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 306.6 | 306.2 | -0.2% | -1.461 to +0.5285 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.6 | 290.4 | -5.3% | -37.16 to +4.68 | no |
| response time (ms), mean | 342.3 | 213 | -37.8% | -163.1 to -95.41 | yes, better |
| response time (ms), 95th percentile | 932.6 | 452.7 | -51.5% | -599.5 to -360.3 | yes, better |
| response time (ms), 99th percentile | 3516 | 3269 | -7.0% | -1244 to +750 | no |
| time over the response line (% of samples) | 20.11 | 10.27 | -48.9% | -12.38 to -7.308 | yes, better |
| failed requests (%) | 7.518 | 6.299 | -16.2% | -1.749 to -0.6891 | yes, better |
| pending pods, pod-minutes | 0.4883 | 0.3283 | -32.8% | -0.4999 to +0.1799 | no |
| utilisation (used / allocatable) | 0.1006 | 0.1067 | +6.1% | -0.005156 to +0.01739 | no |
| CPU used (cores), mean | 2.415 | 2.363 | -2.2% | -0.06437 to -0.04009 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01487 | +0.0149 (native is 0) | +0.0132 to +0.01654 | yes, more |
| CPU used with Omni's own (cores), mean | 2.415 | 2.378 | -1.5% | -0.04938 to -0.02533 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 294.4 | 278.3 | -5.5% | -49.81 to +17.57 | no |
| HPA replicas, mean | 9.253 | 9.29 | +0.4% | -0.1285 to +0.2029 | no |
| pods started | 4.4 | 3.7 | -15.9% | -1.918 to +0.5181 | no |
| pod start wait, total (s) | 15 | 5.7 | -62.0% | -16.3 to -2.299 | yes, better |
| pod start wait, mean (s) | 2.924 | 1.372 | -53.1% | -2.554 to -0.5481 | yes, better |
| host CPU busy, the real machine under kind (%) | 69.77 | 68.85 | -1.3% | -1.212 to -0.6213 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.92 | -1.3% | -0.1566 to -0.002866 | yes, better |
| node-hours | 2.681 | 2.645 | -1.3% | -0.07159 to +0.0001452 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 306.6 | 305.8 | -0.3% | -1.187 to -0.5505 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.6 | 303.1 | -1.2% | -6.299 to -0.7716 | yes, better |
| response time (ms), mean | 342.3 | 205.5 | -40.0% | -176 to -97.64 | yes, better |
| response time (ms), 95th percentile | 932.6 | 463.8 | -50.3% | -610.8 to -326.8 | yes, better |
| response time (ms), 99th percentile | 3516 | 2805 | -20.2% | -1608 to +184.2 | no |
| time over the response line (% of samples) | 20.11 | 10.66 | -47.0% | -12.14 to -6.759 | yes, better |
| failed requests (%) | 7.518 | 6.545 | -12.9% | -1.345 to -0.601 | yes, better |
| pending pods, pod-minutes | 0.4883 | 0.375 | -23.2% | -0.3437 to +0.1171 | no |
| utilisation (used / allocatable) | 0.1006 | 0.1 | -0.6% | -0.002071 to +0.0008871 | no |
| CPU used (cores), mean | 2.415 | 2.366 | -2.0% | -0.05826 to -0.04048 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01077 | +0.0108 (native is 0) | +0.009532 to +0.01201 | yes, more |
| CPU used with Omni's own (cores), mean | 2.415 | 2.376 | -1.6% | -0.04782 to -0.02939 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 294.4 | 298.3 | +1.3% | -0.9622 to +8.68 | no |
| HPA replicas, mean | 9.253 | 9.039 | -2.3% | -0.5624 to +0.1344 | no |
| pods started | 4.4 | 4.3 | -2.3% | -1.625 to +1.425 | no |
| pod start wait, total (s) | 15 | 10 | -33.3% | -11.89 to +1.894 | no |
| pod start wait, mean (s) | 2.924 | 2.043 | -30.1% | -1.708 to -0.05219 | yes, better |
| host CPU busy, the real machine under kind (%) | 69.77 | 68.62 | -1.6% | -1.491 to -0.7976 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.2 |  |  | 10 |
| omni | 25.2 | +55.6% | +6.7 to +11.3 | 10 |
| bowl | 24.0 | +48.1% | +5.7 to +9.9 | 10 |
