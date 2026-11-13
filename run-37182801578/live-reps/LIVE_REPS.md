# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 5.607 | 6 |
| node-hours | 1.513 | 1.415 | 1.511 |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.6 | 171.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 164.2 | 171.3 |
| response time (ms), mean | 493.4 | 329.7 | 433.7 |
| response time (ms), 95th percentile | 2105 | 1238 | 2126 |
| response time (ms), 99th percentile | 5284 | 4248 | 4742 |
| time over the response line (% of samples) | 22.09 | 13.7 | 20.25 |
| failed requests (%) | 3.524 | 2.167 | 3.275 |
| pending pods, pod-minutes | 1.622 | 1.548 | 1.23 |
| utilisation (used / allocatable) | 0.09516 | 0.09929 | 0.09397 |
| CPU used (cores), mean | 2.284 | 2.248 | 2.255 |
| Omni's own CPU (cores), mean | 0 | 0.02175 | 0.01375 |
| CPU used with Omni's own (cores), mean | 2.284 | 2.27 | 2.269 |
| energy per core-hour (Wh, the 25 W standby model) | 309.8 | 297.6 | 314.3 |
| HPA replicas, mean | 15.06 | 15.14 | 15.16 |
| pods started | 4.4 | 3.9 | 3.8 |
| pod start wait, total (s) | 10.4 | 5.9 | 12.2 |
| pod start wait, mean (s) | 2.081 | 1.348 | 2.324 |
| host CPU busy, the real machine under kind (%) | 65.61 | 65.82 | 65.59 |
| host cores (the real machine under kind) | 4 | 4 | 4 |
| second app: response time (ms), 95th percentile | 288.1 | 291.9 | 290.7 |
| second app: response time (ms), 99th percentile | 1880 | 1283 | 2076 |
| second app: time over the response line (% of samples) | 13.73 | 13.49 | 13.36 |
| second app: failed requests (%) | 11.81 | 12.07 | 11.79 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.607 | -6.6% | -0.8759 to +0.08941 | no |
| node-hours | 1.513 | 1.415 | -6.4% | -0.2206 to +0.02567 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.6 | -0.1% | -1.146 to +0.8719 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 164.2 | -4.4% | -17.1 to +1.957 | no |
| response time (ms), mean | 493.4 | 329.7 | -33.2% | -237.9 to -89.39 | yes, better |
| response time (ms), 95th percentile | 2105 | 1238 | -41.2% | -1374 to -360.2 | yes, better |
| response time (ms), 99th percentile | 5284 | 4248 | -19.6% | -1671 to -401.2 | yes, better |
| time over the response line (% of samples) | 22.09 | 13.7 | -38.0% | -11.98 to -4.798 | yes, better |
| failed requests (%) | 3.524 | 2.167 | -38.5% | -2.712 to -0.001125 | yes, better |
| pending pods, pod-minutes | 1.622 | 1.548 | -4.5% | -0.719 to +0.5723 | no |
| utilisation (used / allocatable) | 0.09516 | 0.09929 | +4.3% | -0.002221 to +0.01048 | no |
| CPU used (cores), mean | 2.284 | 2.248 | -1.5% | -0.07638 to +0.005647 | no |
| Omni's own CPU (cores), mean | 0 | 0.02175 | +0.0218 (native is 0) | +0.01839 to +0.02511 | yes, more |
| CPU used with Omni's own (cores), mean | 2.284 | 2.27 | -0.6% | -0.05587 to +0.02863 | no |
| energy per core-hour (Wh, the 25 W standby model) | 309.8 | 297.6 | -3.9% | -30.01 to +5.571 | no |
| HPA replicas, mean | 15.06 | 15.14 | +0.5% | -0.1497 to +0.2987 | no |
| pods started | 4.4 | 3.9 | -11.4% | -1.469 to +0.4685 | no |
| pod start wait, total (s) | 10.4 | 5.9 | -43.3% | -10.09 to +1.094 | no |
| pod start wait, mean (s) | 2.081 | 1.348 | -35.2% | -1.454 to -0.01176 | yes, better |
| host CPU busy, the real machine under kind (%) | 65.61 | 65.82 | +0.3% | -0.6006 to +1.009 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 288.1 | 291.9 | +1.3% | -19.34 to +26.98 | no |
| second app: response time (ms), 99th percentile | 1880 | 1283 | -31.7% | -2039 to +846.5 | no |
| second app: time over the response line (% of samples) | 13.73 | 13.49 | -1.8% | -0.6854 to +0.2045 | no |
| second app: failed requests (%) | 11.81 | 12.07 | +2.2% | -0.346 to +0.8646 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | no |
| node-hours | 1.513 | 1.511 | -0.1% | -0.004162 to +0.0001621 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 171.7 | 171.3 | -0.2% | -0.7523 to -0.1063 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 171.7 | 171.3 | -0.2% | -0.7523 to -0.1063 | yes, better |
| response time (ms), mean | 493.4 | 433.7 | -12.1% | -112.5 to -6.818 | yes, better |
| response time (ms), 95th percentile | 2105 | 2126 | +1.0% | -363.8 to +406.4 | no |
| response time (ms), 99th percentile | 5284 | 4742 | -10.3% | -1211 to +126.9 | no |
| time over the response line (% of samples) | 22.09 | 20.25 | -8.3% | -3.843 to +0.1811 | no |
| failed requests (%) | 3.524 | 3.275 | -7.0% | -1.527 to +1.03 | no |
| pending pods, pod-minutes | 1.622 | 1.23 | -24.2% | -1.194 to +0.4111 | no |
| utilisation (used / allocatable) | 0.09516 | 0.09397 | -1.3% | -0.001975 to -0.0004052 | yes, less |
| CPU used (cores), mean | 2.284 | 2.255 | -1.3% | -0.0474 to -0.009724 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01375 | +0.0138 (native is 0) | +0.01097 to +0.01653 | yes, more |
| CPU used with Omni's own (cores), mean | 2.284 | 2.269 | -0.6% | -0.03517 to +0.005543 | no |
| energy per core-hour (Wh, the 25 W standby model) | 309.8 | 314.3 | +1.5% | +0.726 to +8.324 | yes, worse |
| HPA replicas, mean | 15.06 | 15.16 | +0.7% | -0.2173 to +0.4135 | no |
| pods started | 4.4 | 3.8 | -13.6% | -1.728 to +0.5285 | no |
| pod start wait, total (s) | 10.4 | 12.2 | +17.3% | -3.084 to +6.684 | no |
| pod start wait, mean (s) | 2.081 | 2.324 | +11.7% | -0.4434 to +0.9296 | no |
| host CPU busy, the real machine under kind (%) | 65.61 | 65.59 | -0.0% | -0.5804 to +0.5357 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |
| second app: response time (ms), 95th percentile | 288.1 | 290.7 | +0.9% | -25.83 to +31.08 | no |
| second app: response time (ms), 99th percentile | 1880 | 2076 | +10.5% | -877.6 to +1271 | no |
| second app: time over the response line (% of samples) | 13.73 | 13.36 | -2.7% | -0.8355 to +0.09483 | no |
| second app: failed requests (%) | 11.81 | 11.79 | -0.2% | -0.4397 to +0.392 | no |
