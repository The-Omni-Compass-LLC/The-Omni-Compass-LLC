# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 5.914 | 5.624 | 5.908 |
| node-hours | 1.498 | 1.425 | 1.492 |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.2 | 166.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 159.1 | 164.5 |
| response time (ms), mean | 203.6 | 135.9 | 153 |
| response time (ms), 95th percentile | 417.9 | 150.7 | 162.2 |
| response time (ms), 99th percentile | 936.9 | 1017 | 1059 |
| time over the response line (% of samples) | 8.648 | 5.19 | 6.265 |
| failed requests (%) | 5.595 | 4.265 | 4.874 |
| pending pods, pod-minutes | 0.6717 | 0.36 | 0.23 |
| utilisation (used / allocatable) | 0.07428 | 0.07344 | 0.07328 |
| CPU used (cores), mean | 1.757 | 1.661 | 1.733 |
| Omni's own CPU (cores), mean | 0 | 0.01907 | 0.00969 |
| CPU used with Omni's own (cores), mean | 1.757 | 1.68 | 1.742 |
| energy per core-hour (Wh, the 25 W standby model) | 380.8 | 381.4 | 384 |
| HPA replicas, mean | 8.962 | 9.267 | 9.15 |
| pods started | 4.1 | 2.4 | 2.7 |
| pod start wait, total (s) | 26.9 | 5.1 | 8.5 |
| pod start wait, mean (s) | 5.841 | 1.511 | 2.136 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.624 | -4.9% | -0.7601 to +0.1809 | no |
| node-hours | 1.498 | 1.425 | -4.9% | -0.1939 to +0.0465 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.2 | -0.5% | -1.274 to -0.4633 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 159.1 | -3.9% | -15.17 to +2.426 | no |
| response time (ms), mean | 203.6 | 135.9 | -33.3% | -90.43 to -45.04 | yes, better |
| response time (ms), 95th percentile | 417.9 | 150.7 | -63.9% | -310 to -224.4 | yes, better |
| response time (ms), 99th percentile | 936.9 | 1017 | +8.6% | -750.2 to +910.9 | no |
| time over the response line (% of samples) | 8.648 | 5.19 | -40.0% | -4.202 to -2.714 | yes, better |
| failed requests (%) | 5.595 | 4.265 | -23.8% | -2.104 to -0.5556 | yes, better |
| pending pods, pod-minutes | 0.6717 | 0.36 | -46.4% | -1.044 to +0.4206 | no |
| utilisation (used / allocatable) | 0.07428 | 0.07344 | -1.1% | -0.007099 to +0.005415 | no |
| CPU used (cores), mean | 1.757 | 1.661 | -5.5% | -0.1281 to -0.06366 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01907 | +0.0191 (native is 0) | +0.01664 to +0.0215 | yes, more |
| CPU used with Omni's own (cores), mean | 1.757 | 1.68 | -4.4% | -0.1079 to -0.04577 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 380.8 | 381.4 | +0.2% | -30.82 to +32.05 | no |
| HPA replicas, mean | 8.962 | 9.267 | +3.4% | -0.08126 to +0.6906 | no |
| pods started | 4.1 | 2.4 | -41.5% | -3.21 to -0.1901 | yes, better |
| pod start wait, total (s) | 26.9 | 5.1 | -81.0% | -45.33 to +1.726 | no |
| pod start wait, mean (s) | 5.841 | 1.511 | -74.1% | -9.464 to +0.8035 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.914 | 5.908 | -0.1% | -0.02353 to +0.01182 | no |
| node-hours | 1.498 | 1.492 | -0.4% | -0.01752 to +0.004077 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 167.1 | 166.2 | -0.5% | -1.56 to -0.09146 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 165.4 | 164.5 | -0.6% | -1.842 to -0.01792 | yes, better |
| response time (ms), mean | 203.6 | 153 | -24.9% | -101.8 to +0.5159 | no |
| response time (ms), 95th percentile | 417.9 | 162.2 | -61.2% | -295.4 to -216 | yes, better |
| response time (ms), 99th percentile | 936.9 | 1059 | +13.1% | -400.1 to +644.9 | no |
| time over the response line (% of samples) | 8.648 | 6.265 | -27.6% | -3.235 to -1.531 | yes, better |
| failed requests (%) | 5.595 | 4.874 | -12.9% | -1.154 to -0.2864 | yes, better |
| pending pods, pod-minutes | 0.6717 | 0.23 | -65.8% | -1.13 to +0.2462 | no |
| utilisation (used / allocatable) | 0.07428 | 0.07328 | -1.3% | -0.003161 to +0.001162 | no |
| CPU used (cores), mean | 1.757 | 1.733 | -1.4% | -0.07451 to +0.02529 | no |
| Omni's own CPU (cores), mean | 0 | 0.00969 | +0.00969 (native is 0) | +0.009102 to +0.01028 | yes, more |
| CPU used with Omni's own (cores), mean | 1.757 | 1.742 | -0.8% | -0.06477 to +0.03493 | no |
| energy per core-hour (Wh, the 25 W standby model) | 380.8 | 384 | +0.9% | -6.41 to +12.96 | no |
| HPA replicas, mean | 8.962 | 9.15 | +2.1% | -0.164 to +0.5386 | no |
| pods started | 4.1 | 2.7 | -34.1% | -2.757 to -0.0428 | yes, better |
| pod start wait, total (s) | 26.9 | 8.5 | -68.4% | -43.92 to +7.116 | no |
| pod start wait, mean (s) | 5.841 | 2.136 | -63.4% | -9.057 to +1.647 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 98 | 16.0 |  |
| machine down | omni | 45 | 9.1 | -53 s (-54%) |
| machine down | bowl | 41 | 9.8 | -57 s (-58%) |
| spike | native | 277 | 68.7 |  |
| spike | omni | 256 | 45.7 | -21 s (-8%) |
| spike | bowl | 269 | 65.8 | -8 s (-3%) |
| runaway pod started | native | 130 | 11.7 |  |
| runaway pod started | omni | 82 | 5.6 | -48 s (-37%) |
| runaway pod started | bowl | 116 | 9.7 | -14 s (-11%) |
| probe blind | native | 62 | 0.1 |  |
| probe blind | omni | 60 | 0.1 | -2 s (-3%) |
| probe blind | bowl | 60 | 0.1 | -2 s (-4%) |
