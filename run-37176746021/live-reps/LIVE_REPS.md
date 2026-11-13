# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 5.351 | 5.765 |
| node-hours | 2.688 | 2.394 | 2.579 |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.4 | 305.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 283.7 | 297.6 |
| response time (ms), mean | 318.8 | 187.9 | 179.5 |
| response time (ms), 95th percentile | 868.8 | 417.4 | 381.9 |
| response time (ms), 99th percentile | 2524 | 2301 | 1890 |
| time over the response line (% of samples) | 19.2 | 9.727 | 9.944 |
| failed requests (%) | 7.518 | 6.337 | 6.573 |
| pending pods, pod-minutes | 0.425 | 0.1583 | 0.6567 |
| utilisation (used / allocatable) | 0.09895 | 0.1084 | 0.09986 |
| CPU used (cores), mean | 2.375 | 2.315 | 2.32 |
| Omni's own CPU (cores), mean | 0 | 0.01447 | 0.0103 |
| CPU used with Omni's own (cores), mean | 2.375 | 2.329 | 2.33 |
| energy per core-hour (Wh, the 25 W standby model) | 300.2 | 277.7 | 297.9 |
| HPA replicas, mean | 9.225 | 9.292 | 8.042 |
| pods started | 4.1 | 3.4 | 5.7 |
| pod start wait, total (s) | 12.6 | 5.2 | 13.6 |
| pod start wait, mean (s) | 2.583 | 1.346 | 2.421 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.351 | -10.8% | -1.476 to +0.178 | no |
| node-hours | 2.688 | 2.394 | -10.9% | -0.6632 to +0.0768 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.4 | -0.4% | -2.508 to +0.04299 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 283.7 | -7.5% | -50.84 to +4.951 | no |
| response time (ms), mean | 318.8 | 187.9 | -41.1% | -173.5 to -88.19 | yes, better |
| response time (ms), 95th percentile | 868.8 | 417.4 | -52.0% | -602 to -300.9 | yes, better |
| response time (ms), 99th percentile | 2524 | 2301 | -8.8% | -1266 to +820.6 | no |
| time over the response line (% of samples) | 19.2 | 9.727 | -49.3% | -12.63 to -6.32 | yes, better |
| failed requests (%) | 7.518 | 6.337 | -15.7% | -1.801 to -0.5614 | yes, better |
| pending pods, pod-minutes | 0.425 | 0.1583 | -62.7% | -0.5481 to +0.01473 | no |
| utilisation (used / allocatable) | 0.09895 | 0.1084 | +9.6% | -0.004866 to +0.02379 | no |
| CPU used (cores), mean | 2.375 | 2.315 | -2.5% | -0.09532 to -0.0247 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01447 | +0.0145 (native is 0) | +0.0124 to +0.01654 | yes, more |
| CPU used with Omni's own (cores), mean | 2.375 | 2.329 | -1.9% | -0.0821 to -0.008987 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 300.2 | 277.7 | -7.5% | -58.51 to +13.52 | no |
| HPA replicas, mean | 9.225 | 9.292 | +0.7% | -0.149 to +0.2828 | no |
| pods started | 4.1 | 3.4 | -17.1% | -1.964 to +0.5639 | no |
| pod start wait, total (s) | 12.6 | 5.2 | -58.7% | -13.4 to -1.404 | yes, better |
| pod start wait, mean (s) | 2.583 | 1.346 | -47.9% | -2.043 to -0.4307 | yes, better |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.765 | -3.9% | -0.4607 to -0.009241 | yes, better |
| node-hours | 2.688 | 2.579 | -4.0% | -0.2103 to -0.005948 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.5 | -0.4% | -1.916 to -0.4485 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 297.6 | -3.0% | -16.93 to -1.18 | yes, better |
| response time (ms), mean | 318.8 | 179.5 | -43.7% | -173.3 to -105.2 | yes, better |
| response time (ms), 95th percentile | 868.8 | 381.9 | -56.0% | -600.3 to -373.5 | yes, better |
| response time (ms), 99th percentile | 2524 | 1890 | -25.1% | -1306 to +38.73 | no |
| time over the response line (% of samples) | 19.2 | 9.944 | -48.2% | -12.05 to -6.462 | yes, better |
| failed requests (%) | 7.518 | 6.573 | -12.6% | -1.43 to -0.4602 | yes, better |
| pending pods, pod-minutes | 0.425 | 0.6567 | +54.5% | -0.03882 to +0.5022 | no |
| utilisation (used / allocatable) | 0.09895 | 0.09986 | +0.9% | -0.001281 to +0.003086 | no |
| CPU used (cores), mean | 2.375 | 2.32 | -2.3% | -0.0781 to -0.03187 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0103 | +0.0103 (native is 0) | +0.008778 to +0.01182 | yes, more |
| CPU used with Omni's own (cores), mean | 2.375 | 2.33 | -1.9% | -0.0687 to -0.02067 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 300.2 | 297.9 | -0.7% | -9.618 to +5.124 | no |
| HPA replicas, mean | 9.225 | 8.042 | -12.8% | -2.315 to -0.05011 | yes, better |
| pods started | 4.1 | 5.7 | +39.0% | -0.6418 to +3.842 | no |
| pod start wait, total (s) | 12.6 | 13.6 | +7.9% | -5.53 to +7.53 | no |
| pod start wait, mean (s) | 2.583 | 2.421 | -6.3% | -0.7559 to +0.4328 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 17.4 |  |  | 10 |
| omni | 25.2 | +44.8% | +4.9 to +10.7 | 10 |
| bowl | 24.6 | +41.4% | +5.4 to +9.0 | 10 |
