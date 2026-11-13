# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 5.432 | 5.863 |
| node-hours | 2.683 | 2.427 | 2.621 |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.9 | 305.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 286.9 | 301.1 |
| response time (ms), mean | 334.4 | 209.5 | 209.7 |
| response time (ms), 95th percentile | 890.3 | 409.2 | 445.1 |
| response time (ms), 99th percentile | 3305 | 3295 | 3408 |
| time over the response line (% of samples) | 19.64 | 9.5 | 10.86 |
| failed requests (%) | 6.893 | 5.913 | 6.613 |
| pending pods, pod-minutes | 0.3533 | 0.11 | 1.597 |
| utilisation (used / allocatable) | 0.1003 | 0.1098 | 0.1003 |
| CPU used (cores), mean | 2.408 | 2.37 | 2.351 |
| Omni's own CPU (cores), mean | 0 | 0.0144 | 0.01391 |
| CPU used with Omni's own (cores), mean | 2.408 | 2.384 | 2.365 |
| energy per core-hour (Wh, the 25 W standby model) | 289.3 | 272.4 | 291.2 |
| HPA replicas, mean | 9.243 | 9.305 | 16.49 |
| pods started | 4.6 | 3.8 | 26.2 |
| pod start wait, total (s) | 14.8 | 5.9 | 105.4 |
| pod start wait, mean (s) | 2.955 | 1.456 | 4.017 |
| host CPU busy, the real machine under kind (%) | 69.36 | 69.01 | 68.7 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.432 | -9.5% | -1.137 to +0.001234 | no |
| node-hours | 2.683 | 2.427 | -9.6% | -0.5092 to -0.003598 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.9 | -0.3% | -1.765 to +0.1747 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 286.9 | -6.5% | -38.64 to -0.9797 | yes, better |
| response time (ms), mean | 334.4 | 209.5 | -37.3% | -146.1 to -103.6 | yes, better |
| response time (ms), 95th percentile | 890.3 | 409.2 | -54.0% | -536.9 to -425.2 | yes, better |
| response time (ms), 99th percentile | 3305 | 3295 | -0.3% | -1102 to +1081 | no |
| time over the response line (% of samples) | 19.64 | 9.5 | -51.6% | -11.88 to -8.395 | yes, better |
| failed requests (%) | 6.893 | 5.913 | -14.2% | -1.505 to -0.4536 | yes, better |
| pending pods, pod-minutes | 0.3533 | 0.11 | -68.9% | -0.4586 to -0.02807 | yes, better |
| utilisation (used / allocatable) | 0.1003 | 0.1098 | +9.4% | -0.001357 to +0.02023 | no |
| CPU used (cores), mean | 2.408 | 2.37 | -1.6% | -0.06514 to -0.009952 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0144 | +0.0144 (native is 0) | +0.01315 to +0.01565 | yes, more |
| CPU used with Omni's own (cores), mean | 2.408 | 2.384 | -1.0% | -0.05077 to +0.004473 | no |
| energy per core-hour (Wh, the 25 W standby model) | 289.3 | 272.4 | -5.8% | -38.86 to +5.117 | no |
| HPA replicas, mean | 9.243 | 9.305 | +0.7% | -0.1644 to +0.2883 | no |
| pods started | 4.6 | 3.8 | -17.4% | -2.097 to +0.4972 | no |
| pod start wait, total (s) | 14.8 | 5.9 | -60.1% | -14.05 to -3.748 | yes, better |
| pod start wait, mean (s) | 2.955 | 1.456 | -50.7% | -2.15 to -0.8489 | yes, better |
| host CPU busy, the real machine under kind (%) | 69.36 | 69.01 | -0.5% | -1.121 to +0.4255 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.863 | -2.3% | -0.2597 to -0.01329 | yes, better |
| node-hours | 2.683 | 2.621 | -2.3% | -0.113 to -0.0115 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 306.7 | 305.7 | -0.3% | -2.096 to +0.06092 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 306.7 | 301.1 | -1.8% | -9.33 to -1.867 | yes, better |
| response time (ms), mean | 334.4 | 209.7 | -37.3% | -155.6 to -93.73 | yes, better |
| response time (ms), 95th percentile | 890.3 | 445.1 | -50.0% | -517.3 to -373.1 | yes, better |
| response time (ms), 99th percentile | 3305 | 3408 | +3.1% | -995 to +1202 | no |
| time over the response line (% of samples) | 19.64 | 10.86 | -44.7% | -9.975 to -7.577 | yes, better |
| failed requests (%) | 6.893 | 6.613 | -4.1% | -0.5916 to +0.03216 | no |
| pending pods, pod-minutes | 0.3533 | 1.597 | +351.9% | -0.2235 to +2.71 | no |
| utilisation (used / allocatable) | 0.1003 | 0.1003 | -0.0% | -0.001908 to +0.001852 | no |
| CPU used (cores), mean | 2.408 | 2.351 | -2.3% | -0.06866 to -0.04374 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01391 | +0.0139 (native is 0) | +0.0122 to +0.01562 | yes, more |
| CPU used with Omni's own (cores), mean | 2.408 | 2.365 | -1.8% | -0.05498 to -0.0296 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 289.3 | 291.2 | +0.6% | -2.034 to +5.732 | no |
| HPA replicas, mean | 9.243 | 16.49 | +78.4% | +4.263 to +10.23 | yes, worse |
| pods started | 4.6 | 26.2 | +469.6% | +20.2 to +23 | yes, worse |
| pod start wait, total (s) | 14.8 | 105.4 | +612.2% | +79.51 to +101.7 | yes, worse |
| pod start wait, mean (s) | 2.955 | 4.017 | +35.9% | +0.1717 to +1.952 | yes, worse |
| host CPU busy, the real machine under kind (%) | 69.36 | 68.7 | -0.9% | -1.179 to -0.1367 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 15.0 |  |  | 10 |
| omni | 27.6 | +84.0% | +9.4 to +15.8 | 10 |
| bowl | 24.6 | +64.0% | +7.4 to +11.8 | 10 |
