# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 2.882 | 5.431 |
| node-hours | 2.686 | 1.288 | 2.425 |
| energy, parked workers still on at idle power (Wh, declared model) | 301.4 | 300.7 | 299.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.4 | 196.1 | 280.8 |
| response time (ms), mean | 281.1 | 233.2 | 150.5 |
| response time (ms), 95th percentile | 769.1 | 702.8 | 374.7 |
| response time (ms), 99th percentile | 2961 | 2987 | 1676 |
| time over the response line (% of samples) | 13.37 | 10.14 | 6.371 |
| failed requests (%) | 3.471 | 3.32 | 3.174 |
| pending pods, pod-minutes | 0.61 | 0.4217 | 0.405 |
| utilisation (used / allocatable) | 0.08641 | 0.1733 | 0.09161 |
| CPU used (cores), mean | 2.074 | 1.998 | 2.009 |
| Omni's own CPU (cores), mean | 0 | 0.01301 | 0.00946 |
| CPU used with Omni's own (cores), mean | 2.074 | 2.011 | 2.018 |
| energy per core-hour (Wh, the 25 W standby model) | 339.7 | 226.1 | 325.1 |
| HPA replicas, mean | 8.879 | 8.102 | 6.488 |
| pods started | 5.6 | 7.8 | 7.3 |
| pod start wait, total (s) | 21.2 | 16.5 | 20.8 |
| pod start wait, mean (s) | 3.547 | 2.076 | 2.821 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 2.882 | -52.0% | -3.404 to -2.832 | yes, better |
| node-hours | 2.686 | 1.288 | -52.0% | -1.524 to -1.271 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 301.4 | 300.7 | -0.2% | -2.35 to +0.8926 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.4 | 196.1 | -34.9% | -114.4 to -96.08 | yes, better |
| response time (ms), mean | 281.1 | 233.2 | -17.0% | -91.83 to -3.902 | yes, better |
| response time (ms), 95th percentile | 769.1 | 702.8 | -8.6% | -165.1 to +32.52 | no |
| response time (ms), 99th percentile | 2961 | 2987 | +0.9% | -1356 to +1407 | no |
| time over the response line (% of samples) | 13.37 | 10.14 | -24.1% | -5.423 to -1.024 | yes, better |
| failed requests (%) | 3.471 | 3.32 | -4.4% | -0.6086 to +0.3051 | no |
| pending pods, pod-minutes | 0.61 | 0.4217 | -30.9% | -0.6211 to +0.2444 | no |
| utilisation (used / allocatable) | 0.08641 | 0.1733 | +100.6% | +0.0738 to +0.1001 | yes, more |
| CPU used (cores), mean | 2.074 | 1.998 | -3.7% | -0.1173 to -0.03485 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01301 | +0.013 (native is 0) | +0.01097 to +0.01505 | yes, more |
| CPU used with Omni's own (cores), mean | 2.074 | 2.011 | -3.0% | -0.1027 to -0.02339 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 339.7 | 226.1 | -33.4% | -144.1 to -83.07 | yes, better |
| HPA replicas, mean | 8.879 | 8.102 | -8.7% | -1.039 to -0.5141 | yes, better |
| pods started | 5.6 | 7.8 | +39.3% | +1.388 to +3.012 | yes, worse |
| pod start wait, total (s) | 21.2 | 16.5 | -22.2% | -10.84 to +1.445 | no |
| pod start wait, mean (s) | 3.547 | 2.076 | -41.5% | -2.153 to -0.788 | yes, better |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.431 | -9.5% | -0.858 to -0.2802 | yes, better |
| node-hours | 2.686 | 2.425 | -9.7% | -0.3933 to -0.1286 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 301.4 | 299.8 | -0.5% | -2.094 to -0.9953 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.4 | 280.8 | -6.8% | -30.53 to -10.62 | yes, better |
| response time (ms), mean | 281.1 | 150.5 | -46.5% | -170.9 to -90.31 | yes, better |
| response time (ms), 95th percentile | 769.1 | 374.7 | -51.3% | -493.7 to -295 | yes, better |
| response time (ms), 99th percentile | 2961 | 1676 | -43.4% | -2098 to -471.4 | yes, better |
| time over the response line (% of samples) | 13.37 | 6.371 | -52.3% | -9.88 to -4.113 | yes, better |
| failed requests (%) | 3.471 | 3.174 | -8.6% | -0.5345 to -0.05987 | yes, better |
| pending pods, pod-minutes | 0.61 | 0.405 | -33.6% | -0.4845 to +0.07454 | no |
| utilisation (used / allocatable) | 0.08641 | 0.09161 | +6.0% | +0.002057 to +0.008331 | yes, more |
| CPU used (cores), mean | 2.074 | 2.009 | -3.1% | -0.08031 to -0.04968 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.00946 | +0.00946 (native is 0) | +0.008217 to +0.0107 | yes, more |
| CPU used with Omni's own (cores), mean | 2.074 | 2.018 | -2.7% | -0.07102 to -0.04004 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 339.7 | 325.1 | -4.3% | -28.36 to -0.7399 | yes, better |
| HPA replicas, mean | 8.879 | 6.488 | -26.9% | -3.154 to -1.627 | yes, better |
| pods started | 5.6 | 7.3 | +30.4% | +0.9422 to +2.458 | yes, worse |
| pod start wait, total (s) | 21.2 | 20.8 | -1.9% | -6.537 to +5.737 | no |
| pod start wait, mean (s) | 3.547 | 2.821 | -20.5% | -1.517 to +0.06589 | no |

## The capacity test: the same machines, the load rising step by step

Each step adds one load generator (6 requests a second each). A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and every lower step held too), the first 30 s of each step left to settle. Paired over the repetitions; higher is more work from the same machines.

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 24.6 |  |  | 10 |
| omni | 25.8 | +4.9% | -0.6 to +3.0 | 10 |
| bowl | 33.0 | +34.1% | +6.2 to +10.6 | 10 |
