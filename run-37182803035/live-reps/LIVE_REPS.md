# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 5.915 | 5.318 | 5.903 |
| node-hours | 1.494 | 1.347 | 1.49 |
| energy, parked workers still on at idle power (Wh, declared model) | 165.9 | 165.8 | 165.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.3 | 152.8 | 163.7 |
| response time (ms), mean | 230.3 | 124.9 | 117.5 |
| response time (ms), 95th percentile | 441.2 | 186.5 | 164.5 |
| response time (ms), 99th percentile | 1245 | 749.1 | 742.5 |
| time over the response line (% of samples) | 8.494 | 5.344 | 5.382 |
| failed requests (%) | 5.006 | 3.981 | 4.335 |
| pending pods, pod-minutes | 0.4917 | 0.43 | 0.305 |
| utilisation (used / allocatable) | 0.0714 | 0.07519 | 0.07029 |
| CPU used (cores), mean | 1.689 | 1.604 | 1.66 |
| Omni's own CPU (cores), mean | 0 | 0.01873 | 0.00928 |
| CPU used with Omni's own (cores), mean | 1.689 | 1.622 | 1.67 |
| energy per core-hour (Wh, the 25 W standby model) | 398.9 | 381.2 | 403.9 |
| HPA replicas, mean | 8.728 | 8.832 | 8.752 |
| pods started | 4.8 | 3.7 | 4 |
| pod start wait, total (s) | 14.7 | 16.2 | 11.4 |
| pod start wait, mean (s) | 2.702 | 3.004 | 2.344 |
| host CPU busy, the real machine under kind (%) | 48.26 | 46.89 | 47.66 |
| host cores (the real machine under kind) | 4 | 4 | 4 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.318 | -10.1% | -1.211 to +0.01626 | no |
| node-hours | 1.494 | 1.347 | -9.8% | -0.2978 to +0.004648 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.9 | 165.8 | -0.1% | -1.095 to +0.8671 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.3 | 152.8 | -7.0% | -22.38 to -0.6029 | yes, better |
| response time (ms), mean | 230.3 | 124.9 | -45.7% | -147.1 to -63.52 | yes, better |
| response time (ms), 95th percentile | 441.2 | 186.5 | -57.7% | -311.6 to -197.9 | yes, better |
| response time (ms), 99th percentile | 1245 | 749.1 | -39.8% | -1058 to +66.67 | no |
| time over the response line (% of samples) | 8.494 | 5.344 | -37.1% | -4.126 to -2.175 | yes, better |
| failed requests (%) | 5.006 | 3.981 | -20.5% | -1.687 to -0.3641 | yes, better |
| pending pods, pod-minutes | 0.4917 | 0.43 | -12.5% | -0.4474 to +0.324 | no |
| utilisation (used / allocatable) | 0.0714 | 0.07519 | +5.3% | -0.004495 to +0.01206 | no |
| CPU used (cores), mean | 1.689 | 1.604 | -5.1% | -0.1221 to -0.04937 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01873 | +0.0187 (native is 0) | +0.01611 to +0.02135 | yes, more |
| CPU used with Omni's own (cores), mean | 1.689 | 1.622 | -4.0% | -0.1021 to -0.03193 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 398.9 | 381.2 | -4.4% | -57.01 to +21.71 | no |
| HPA replicas, mean | 8.728 | 8.832 | +1.2% | -0.1607 to +0.3691 | no |
| pods started | 4.8 | 3.7 | -22.9% | -2.241 to +0.04101 | no |
| pod start wait, total (s) | 14.7 | 16.2 | +10.2% | -16.83 to +19.83 | no |
| pod start wait, mean (s) | 2.702 | 3.004 | +11.1% | -2.334 to +2.936 | no |
| host CPU busy, the real machine under kind (%) | 48.26 | 46.89 | -2.9% | -2.265 to -0.4889 | yes, less |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 5.915 | 5.903 | -0.2% | -0.03447 to +0.009988 | no |
| node-hours | 1.494 | 1.49 | -0.2% | -0.01463 to +0.007184 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 165.9 | 165.5 | -0.2% | -1.067 to +0.3338 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 164.3 | 163.7 | -0.4% | -1.372 to +0.1807 | no |
| response time (ms), mean | 230.3 | 117.5 | -49.0% | -152.5 to -73.13 | yes, better |
| response time (ms), 95th percentile | 441.2 | 164.5 | -62.7% | -306.3 to -247.3 | yes, better |
| response time (ms), 99th percentile | 1245 | 742.5 | -40.4% | -1123 to +118.5 | no |
| time over the response line (% of samples) | 8.494 | 5.382 | -36.6% | -3.814 to -2.409 | yes, better |
| failed requests (%) | 5.006 | 4.335 | -13.4% | -1.152 to -0.1902 | yes, better |
| pending pods, pod-minutes | 0.4917 | 0.305 | -38.0% | -0.4173 to +0.04394 | no |
| utilisation (used / allocatable) | 0.0714 | 0.07029 | -1.6% | -0.002941 to +0.0007209 | no |
| CPU used (cores), mean | 1.689 | 1.66 | -1.7% | -0.07021 to +0.01231 | no |
| Omni's own CPU (cores), mean | 0 | 0.00928 | +0.00928 (native is 0) | +0.008408 to +0.01015 | yes, more |
| CPU used with Omni's own (cores), mean | 1.689 | 1.67 | -1.2% | -0.06093 to +0.02159 | no |
| energy per core-hour (Wh, the 25 W standby model) | 398.9 | 403.9 | +1.3% | -5.579 to +15.65 | no |
| HPA replicas, mean | 8.728 | 8.752 | +0.3% | -0.2394 to +0.2879 | no |
| pods started | 4.8 | 4 | -16.7% | -1.742 to +0.1417 | no |
| pod start wait, total (s) | 14.7 | 11.4 | -22.4% | -7.389 to +0.789 | no |
| pod start wait, mean (s) | 2.702 | 2.344 | -13.3% | -0.9352 to +0.219 | no |
| host CPU busy, the real machine under kind (%) | 48.26 | 47.66 | -1.3% | -1.398 to +0.185 | no |
| host cores (the real machine under kind) | 4 | 4 | +0.0% | +0 to +0 | no |

## The fault test: the same faults at the same moments in every arm

Time to recover: from the fault's start until responses stay under the line for 30 seconds straight (at most 300 s). Over the line: the share of response samples over the line or failed in the 300 seconds after the fault. Paired means over the repetitions; lower is better in both.

| Fault | Arm | Time to recover (s) | Over the line (%) | Change in recovery against native |
|---|---|---:|---:|---:|
| machine down | native | 89 | 15.6 |  |
| machine down | omni | 41 | 9.7 | -48 s (-54%) |
| machine down | bowl | 35 | 8.0 | -54 s (-61%) |
| spike | native | 263 | 66.8 |  |
| spike | omni | 252 | 48.6 | -10 s (-4%) |
| spike | bowl | 241 | 62.9 | -22 s (-8%) |
| runaway pod started | native | 121 | 11.2 |  |
| runaway pod started | omni | 83 | 5.7 | -38 s (-32%) |
| runaway pod started | bowl | 96 | 8.6 | -25 s (-20%) |
| probe blind | native | 65 | 0.6 |  |
| probe blind | omni | 48 | 0.0 | -17 s (-26%) |
| probe blind | bowl | 54 | 0.0 | -11 s (-17%) |
