# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 5.916 | 5.043 | 5.893 |
| node-hours | 1.497 | 1.276 | 1.491 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.6 | 165 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 146.5 | 162.9 |
| response time (ms), mean | 202.4 | 115.4 | 126.7 |
| response time (ms), 95th percentile | 386 | 163.8 | 161.5 |
| response time (ms), 99th percentile | 1779 | 1048 | 1289 |
| time over the response line (% of samples) | 6.99 | 4.411 | 4.967 |
| failed requests (%) | 3.804 | 3.345 | 3.658 |
| pending pods, pod-minutes | 0.4533 | 0.2767 | 0.32 |
| utilisation (used / allocatable) | 0.06636 | 0.07494 | 0.06561 |
| CPU used (cores), mean | 1.57 | 1.511 | 1.546 |
| Omni's own CPU (cores), mean | 0 | 0.01644 | 0.00887 |
| CPU used with Omni's own (cores), mean | 1.57 | 1.528 | 1.555 |
| energy per core-hour (Wh, the 25 W standby model) | 430.7 | 387.5 | 431.4 |
| HPA replicas, mean | 8.536 | 8.733 | 8.588 |
| pods started | 5 | 4.1 | 4 |
| pod start wait, total (s) | 17.2 | 8.5 | 13.3 |
| pod start wait, mean (s) | 3.153 | 1.907 | 2.538 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.916 | 5.043 | -14.8% | -1.631 to -0.1145 | yes, better |
| node-hours | 1.497 | 1.276 | -14.8% | -0.413 to -0.03062 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 164.6 | -0.4% | -1.158 to -0.1373 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 146.5 | -10.5% | -31.16 to -3.114 | yes, better |
| response time (ms), mean | 202.4 | 115.4 | -43.0% | -121.3 to -52.55 | yes, better |
| response time (ms), 95th percentile | 386 | 163.8 | -57.6% | -265.5 to -178.9 | yes, better |
| response time (ms), 99th percentile | 1779 | 1048 | -41.1% | -2017 to +555.5 | no |
| time over the response line (% of samples) | 6.99 | 4.411 | -36.9% | -3.644 to -1.515 | yes, better |
| failed requests (%) | 3.804 | 3.345 | -12.1% | -1.03 to +0.1125 | no |
| pending pods, pod-minutes | 0.4533 | 0.2767 | -39.0% | -0.4869 to +0.1336 | no |
| utilisation (used / allocatable) | 0.06636 | 0.07494 | +12.9% | -0.002285 to +0.01946 | no |
| CPU used (cores), mean | 1.57 | 1.511 | -3.8% | -0.09287 to -0.02494 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01644 | +0.0164 (native is 0) | +0.01383 to +0.01905 | yes, more |
| CPU used with Omni's own (cores), mean | 1.57 | 1.528 | -2.7% | -0.07482 to -0.01011 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 430.7 | 387.5 | -10.0% | -97.41 to +11.02 | no |
| HPA replicas, mean | 8.536 | 8.733 | +2.3% | -0.02034 to +0.4139 | no |
| pods started | 5 | 4.1 | -18.0% | -1.99 to +0.19 | no |
| pod start wait, total (s) | 17.2 | 8.5 | -50.6% | -13.42 to -3.979 | yes, better |
| pod start wait, mean (s) | 3.153 | 1.907 | -39.5% | -2.06 to -0.4324 | yes, better |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.916 | 5.893 | -0.4% | -0.05766 to +0.01113 | no |
| node-hours | 1.497 | 1.491 | -0.4% | -0.01403 to +0.002254 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.2 | 165 | -0.1% | -0.8064 to +0.3162 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.6 | 162.9 | -0.4% | -1.269 to -0.1042 | yes, better |
| response time (ms), mean | 202.4 | 126.7 | -37.4% | -125.4 to -26.04 | yes, better |
| response time (ms), 95th percentile | 386 | 161.5 | -58.2% | -290 to -159 | yes, better |
| response time (ms), 99th percentile | 1779 | 1289 | -27.5% | -1932 to +952.7 | no |
| time over the response line (% of samples) | 6.99 | 4.967 | -28.9% | -3.17 to -0.8767 | yes, better |
| failed requests (%) | 3.804 | 3.658 | -3.8% | -0.6664 to +0.3743 | no |
| pending pods, pod-minutes | 0.4533 | 0.32 | -29.4% | -0.2704 to +0.003753 | no |
| utilisation (used / allocatable) | 0.06636 | 0.06561 | -1.1% | -0.002902 to +0.001407 | no |
| CPU used (cores), mean | 1.57 | 1.546 | -1.5% | -0.06924 to +0.02092 | no |
| Omni's own CPU (cores), mean | 0 | 0.00887 | +0.00887 (native is 0) | +0.007297 to +0.01044 | yes, more |
| CPU used with Omni's own (cores), mean | 1.57 | 1.555 | -1.0% | -0.06014 to +0.02957 | no |
| energy per core-hour (Wh, the 25 W standby model) | 430.7 | 431.4 | +0.2% | -9.982 to +11.54 | no |
| HPA replicas, mean | 8.536 | 8.588 | +0.6% | -0.3526 to +0.4566 | no |
| pods started | 5 | 4 | -20.0% | -2.216 to +0.2158 | no |
| pod start wait, total (s) | 17.2 | 13.3 | -22.7% | -8.602 to +0.8021 | no |
| pod start wait, mean (s) | 3.153 | 2.538 | -19.5% | -1.537 to +0.3067 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 52 | 13.5 |  |
| machine down | omni | 41 | 9.0 | -12 s (-22%) |
| machine down | bowl | 41 | 9.5 | -11 s (-21%) |
| spike | native | 238 | 50.5 |  |
| spike | omni | 213 | 32.7 | -25 s (-11%) |
| spike | bowl | 214 | 45.1 | -25 s (-10%) |
| runaway pod started | native | 76 | 7.7 |  |
| runaway pod started | omni | 56 | 3.7 | -19 s (-26%) |
| runaway pod started | bowl | 69 | 5.7 | -7 s (-9%) |
| probe blind | native | 67 | 0.6 |  |
| probe blind | omni | 54 | 0.0 | -13 s (-19%) |
| probe blind | bowl | 60 | 0.1 | -7 s (-10%) |
