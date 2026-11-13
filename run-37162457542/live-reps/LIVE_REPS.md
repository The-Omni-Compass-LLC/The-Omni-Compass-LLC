# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 3.164 | 5.75 |
| node-hours | 2.679 | 1.413 | 2.573 |
| energy, parked workers still on at idle power (Wh, declared model) | 306.5 | 306.4 | 306.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.5 | 211.4 | 298.1 |
| response time (ms), mean | 340.4 | 262 | 198.4 |
| response time (ms), 95th percentile | 924.3 | 798.6 | 411.5 |
| response time (ms), 99th percentile | 3606 | 3666 | 2600 |
| time over the response line (% of samples) | 19.58 | 15.5 | 9.925 |
| failed requests (%) | 7.298 | 6.885 | 6.6 |
| pending pods, pod-minutes | 0.245 | 0.2683 | 0.2367 |
| utilisation (used / allocatable) | 0.101 | 0.1877 | 0.1027 |
| CPU used (cores), mean | 2.424 | 2.35 | 2.373 |
| Omni's own CPU (cores), mean | 0 | 0.01481 | 0.01051 |
| CPU used with Omni's own (cores), mean | 2.424 | 2.365 | 2.383 |
| energy per core-hour (Wh, the 25 W standby model) | 292 | 205 | 288.8 |
| HPA replicas, mean | 9.336 | 8.752 | 8.334 |
| pods started | 3.8 | 6.7 | 5.1 |
| pod start wait, total (s) | 9.1 | 10.9 | 10.2 |
| pod start wait, mean (s) | 2.024 | 1.625 | 1.886 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.164 | -47.3% | -3.182 to -2.489 | yes, better |
| node-hours | 2.679 | 1.413 | -47.2% | -1.42 to -1.111 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 306.5 | 306.4 | -0.0% | -1.342 to +1.115 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.5 | 211.4 | -31.0% | -106.6 to -83.69 | yes, better |
| response time (ms), mean | 340.4 | 262 | -23.0% | -104.9 to -52.03 | yes, better |
| response time (ms), 95th percentile | 924.3 | 798.6 | -13.6% | -210.2 to -41.08 | yes, better |
| response time (ms), 99th percentile | 3606 | 3666 | +1.7% | -867.5 to +987.5 | no |
| time over the response line (% of samples) | 19.58 | 15.5 | -20.9% | -5.934 to -2.238 | yes, better |
| failed requests (%) | 7.298 | 6.885 | -5.7% | -0.9184 to +0.09272 | no |
| pending pods, pod-minutes | 0.245 | 0.2683 | +9.5% | -0.2981 to +0.3448 | no |
| utilisation (used / allocatable) | 0.101 | 0.1877 | +85.8% | +0.06874 to +0.1047 | yes, more |
| CPU used (cores), mean | 2.424 | 2.35 | -3.1% | -0.1092 to -0.04016 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01481 | +0.0148 (native is 0) | +0.01306 to +0.01656 | yes, more |
| CPU used with Omni's own (cores), mean | 2.424 | 2.365 | -2.5% | -0.09289 to -0.02684 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 292 | 205 | -29.8% | -114.7 to -59.42 | yes, better |
| HPA replicas, mean | 9.336 | 8.752 | -6.3% | -0.8815 to -0.2865 | yes, better |
| pods started | 3.8 | 6.7 | +76.3% | +1.759 to +4.041 | yes, worse |
| pod start wait, total (s) | 9.1 | 10.9 | +19.8% | -6.085 to +9.685 | no |
| pod start wait, mean (s) | 2.024 | 1.625 | -19.7% | -1.401 to +0.6028 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.75 | -4.2% | -0.4304 to -0.06983 | yes, better |
| node-hours | 2.679 | 2.573 | -3.9% | -0.181 to -0.02997 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 306.5 | 306.5 | +0.0% | -1.101 to +1.106 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.5 | 298.1 | -2.7% | -13.93 to -2.863 | yes, better |
| response time (ms), mean | 340.4 | 198.4 | -41.7% | -186.4 to -97.73 | yes, better |
| response time (ms), 95th percentile | 924.3 | 411.5 | -55.5% | -612.7 to -412.8 | yes, better |
| response time (ms), 99th percentile | 3606 | 2600 | -27.9% | -2501 to +488.2 | no |
| time over the response line (% of samples) | 19.58 | 9.925 | -49.3% | -11.99 to -7.331 | yes, better |
| failed requests (%) | 7.298 | 6.6 | -9.6% | -1.086 to -0.3102 | yes, better |
| pending pods, pod-minutes | 0.245 | 0.2367 | -3.4% | -0.2333 to +0.2166 | no |
| utilisation (used / allocatable) | 0.101 | 0.1027 | +1.7% | -0.0004573 to +0.003853 | no |
| CPU used (cores), mean | 2.424 | 2.373 | -2.1% | -0.06372 to -0.0399 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01051 | +0.0105 (native is 0) | +0.009172 to +0.01185 | yes, more |
| CPU used with Omni's own (cores), mean | 2.424 | 2.383 | -1.7% | -0.05355 to -0.02905 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 292 | 288.8 | -1.1% | -9.197 to +2.776 | no |
| HPA replicas, mean | 9.336 | 8.334 | -10.7% | -1.453 to -0.5509 | yes, better |
| pods started | 3.8 | 5.1 | +34.2% | +0.2856 to +2.314 | yes, worse |
| pod start wait, total (s) | 9.1 | 10.2 | +12.1% | -3.826 to +6.026 | no |
| pod start wait, mean (s) | 2.024 | 1.886 | -6.8% | -0.788 to +0.5108 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 16.2 |  |  | 10 |
| omni | 16.2 | +0.0% | -2.0 to +2.0 | 10 |
| bowl | 24.6 | +51.9% | +6.2 to +10.6 | 10 |
