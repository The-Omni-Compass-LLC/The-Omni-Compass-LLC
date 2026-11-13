# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 5.917 | 5.085 | 5.902 |
| node-hours | 1.499 | 1.288 | 1.496 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.4 | 164.9 | 165.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 147.6 | 163.4 |
| response time (ms), mean | 208 | 125.4 | 156.8 |
| response time (ms), 95th percentile | 387.8 | 166.7 | 144.9 |
| response time (ms), 99th percentile | 1096 | 1208 | 1430 |
| time over the response line (% of samples) | 7.382 | 5.04 | 4.992 |
| failed requests (%) | 4.388 | 3.555 | 3.668 |
| pending pods, pod-minutes | 0.3967 | 0.2767 | 0.2933 |
| utilisation (used / allocatable) | 0.06709 | 0.07515 | 0.06581 |
| CPU used (cores), mean | 1.588 | 1.522 | 1.554 |
| Omni's own CPU (cores), mean | 0 | 0.01799 | 0.00911 |
| CPU used with Omni's own (cores), mean | 1.588 | 1.54 | 1.563 |
| energy per core-hour (Wh, the 25 W standby model) | 425.1 | 386.5 | 430.4 |
| HPA replicas, mean | 8.624 | 8.563 | 8.528 |
| pods started | 4.7 | 4.5 | 4 |
| pod start wait, total (s) | 16.5 | 9.6 | 15.7 |
| pod start wait, mean (s) | 3.083 | 1.846 | 2.823 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.917 | 5.085 | -14.1% | -1.558 to -0.1053 | yes, better |
| node-hours | 1.499 | 1.288 | -14.1% | -0.3983 to -0.02356 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 165.4 | 164.9 | -0.3% | -1.452 to +0.3271 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 147.6 | -10.0% | -30.03 to -2.583 | yes, better |
| response time (ms), mean | 208 | 125.4 | -39.7% | -136.7 to -28.55 | yes, better |
| response time (ms), 95th percentile | 387.8 | 166.7 | -57.0% | -269.8 to -172.5 | yes, better |
| response time (ms), 99th percentile | 1096 | 1208 | +10.2% | -754.1 to +978.7 | no |
| time over the response line (% of samples) | 7.382 | 5.04 | -31.7% | -3.793 to -0.8906 | yes, better |
| failed requests (%) | 4.388 | 3.555 | -19.0% | -1.539 to -0.1268 | yes, better |
| pending pods, pod-minutes | 0.3967 | 0.2767 | -30.3% | -0.4453 to +0.2053 | no |
| utilisation (used / allocatable) | 0.06709 | 0.07515 | +12.0% | -0.003486 to +0.01961 | no |
| CPU used (cores), mean | 1.588 | 1.522 | -4.1% | -0.1201 to -0.011 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01799 | +0.018 (native is 0) | +0.01506 to +0.02092 | yes, more |
| CPU used with Omni's own (cores), mean | 1.588 | 1.54 | -3.0% | -0.1004 to +0.005248 | no |
| energy per core-hour (Wh, the 25 W standby model) | 425.1 | 386.5 | -9.1% | -92.8 to +15.62 | no |
| HPA replicas, mean | 8.624 | 8.563 | -0.7% | -0.3802 to +0.2566 | no |
| pods started | 4.7 | 4.5 | -4.3% | -1.54 to +1.14 | no |
| pod start wait, total (s) | 16.5 | 9.6 | -41.8% | -13.91 to +0.1122 | no |
| pod start wait, mean (s) | 3.083 | 1.846 | -40.1% | -2.202 to -0.2718 | yes, better |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.917 | 5.902 | -0.3% | -0.03604 to +0.005091 | no |
| node-hours | 1.499 | 1.496 | -0.2% | -0.008929 to +0.003374 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.4 | 165.3 | -0.1% | -0.6236 to +0.282 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 163.9 | 163.4 | -0.3% | -1.048 to +0.1149 | no |
| response time (ms), mean | 208 | 156.8 | -24.6% | -120.3 to +17.83 | no |
| response time (ms), 95th percentile | 387.8 | 144.9 | -62.6% | -292.7 to -193.2 | yes, better |
| response time (ms), 99th percentile | 1096 | 1430 | +30.5% | -360.7 to +1030 | no |
| time over the response line (% of samples) | 7.382 | 4.992 | -32.4% | -3.428 to -1.353 | yes, better |
| failed requests (%) | 4.388 | 3.668 | -16.4% | -1.344 to -0.09716 | yes, better |
| pending pods, pod-minutes | 0.3967 | 0.2933 | -26.1% | -0.3319 to +0.1253 | no |
| utilisation (used / allocatable) | 0.06709 | 0.06581 | -1.9% | -0.003024 to +0.0004724 | no |
| CPU used (cores), mean | 1.588 | 1.554 | -2.1% | -0.07381 to +0.006721 | no |
| Omni's own CPU (cores), mean | 0 | 0.00911 | +0.00911 (native is 0) | +0.007951 to +0.01027 | yes, more |
| CPU used with Omni's own (cores), mean | 1.588 | 1.563 | -1.5% | -0.06422 to +0.01534 | no |
| energy per core-hour (Wh, the 25 W standby model) | 425.1 | 430.4 | +1.3% | -2.385 to +13.09 | no |
| HPA replicas, mean | 8.624 | 8.528 | -1.1% | -0.5904 to +0.3983 | no |
| pods started | 4.7 | 4 | -14.9% | -2.133 to +0.7326 | no |
| pod start wait, total (s) | 16.5 | 15.7 | -4.8% | -9.461 to +7.861 | no |
| pod start wait, mean (s) | 3.083 | 2.823 | -8.4% | -1.524 to +1.005 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 71 | 13.9 |  |
| machine down | omni | 45 | 10.2 | -26 s (-37%) |
| machine down | bowl | 36 | 8.9 | -35 s (-49%) |
| spike | native | 241 | 54.4 |  |
| spike | omni | 232 | 35.5 | -9 s (-4%) |
| spike | bowl | 222 | 47.0 | -19 s (-8%) |
| runaway pod started | native | 88 | 8.9 |  |
| runaway pod started | omni | 60 | 3.9 | -28 s (-32%) |
| runaway pod started | bowl | 72 | 6.3 | -16 s (-18%) |
| probe blind | native | 62 | 0.5 |  |
| probe blind | omni | 60 | 0.0 | -2 s (-4%) |
| probe blind | bowl | 61 | 0.2 | -2 s (-3%) |
