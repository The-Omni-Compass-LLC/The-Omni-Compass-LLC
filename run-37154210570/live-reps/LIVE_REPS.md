# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 4.784 | 5.972 |
| node-hours | 1.512 | 1.208 | 1.506 |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.8 | 172.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 149.8 | 171.8 |
| response time (ms), mean | 577.9 | 314.2 | 412.8 |
| response time (ms), 95th percentile | 2537 | 1157 | 2006 |
| response time (ms), 99th percentile | 6111 | 4377 | 4584 |
| time over the response line (% of samples) | 25.27 | 15.26 | 20.58 |
| failed requests (%) | 3.892 | 4.015 | 4.902 |
| pending pods, pod-minutes | 1.373 | 2.775 | 2.268 |
| utilisation (used / allocatable) | 0.09886 | 0.1231 | 0.09756 |
| CPU used (cores), mean | 2.373 | 2.352 | 2.334 |
| Omni's own CPU (cores), mean | 0 | 0.0265 | 0.01515 |
| CPU used with Omni's own (cores), mean | 2.373 | 2.379 | 2.349 |
| energy per core-hour (Wh, the 25 W standby model) | 297.9 | 258.5 | 301.2 |
| HPA replicas, mean | 15.29 | 14.36 | 14.48 |
| pods started | 4.2 | 4.3 | 4.7 |
| pod start wait, total (s) | 9.8 | 16 | 17 |
| pod start wait, mean (s) | 1.955 | 3.693 | 3.588 |
| second app: response time (ms), 95th percentile | 286.7 | 249.3 | 255.4 |
| second app: response time (ms), 99th percentile | 909.2 | 722.4 | 1139 |
| second app: time over the response line (% of samples) | 14.78 | 14.45 | 14.6 |
| second app: failed requests (%) | 13.39 | 13.72 | 13.46 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.784 | -20.3% | -1.632 to -0.7986 | yes, better |
| node-hours | 1.512 | 1.208 | -20.1% | -0.4085 to -0.2004 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.8 | +0.1% | -0.7483 to +1.25 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 149.8 | -13.2% | -30.75 to -14.79 | yes, better |
| response time (ms), mean | 577.9 | 314.2 | -45.6% | -371.2 to -156.2 | yes, better |
| response time (ms), 95th percentile | 2537 | 1157 | -54.4% | -2037 to -723.9 | yes, better |
| response time (ms), 99th percentile | 6111 | 4377 | -28.4% | -3124 to -344.1 | yes, better |
| time over the response line (% of samples) | 25.27 | 15.26 | -39.6% | -13.09 to -6.932 | yes, better |
| failed requests (%) | 3.892 | 4.015 | +3.2% | -0.7577 to +1.004 | no |
| pending pods, pod-minutes | 1.373 | 2.775 | +102.1% | +0.1867 to +2.617 | yes, worse |
| utilisation (used / allocatable) | 0.09886 | 0.1231 | +24.5% | +0.01652 to +0.03201 | yes, more |
| CPU used (cores), mean | 2.373 | 2.352 | -0.9% | -0.04802 to +0.007377 | no |
| Omni's own CPU (cores), mean | 0 | 0.0265 | +0.0265 (native is 0) | +0.02235 to +0.03065 | yes, more |
| CPU used with Omni's own (cores), mean | 2.373 | 2.379 | +0.3% | -0.02175 to +0.03411 | no |
| energy per core-hour (Wh, the 25 W standby model) | 297.9 | 258.5 | -13.2% | -57.05 to -21.8 | yes, better |
| HPA replicas, mean | 15.29 | 14.36 | -6.1% | -1.681 to -0.1925 | yes, better |
| pods started | 4.2 | 4.3 | +2.4% | -1.348 to +1.548 | no |
| pod start wait, total (s) | 9.8 | 16 | +63.3% | -2.803 to +15.2 | no |
| pod start wait, mean (s) | 1.955 | 3.693 | +88.8% | +0.3636 to +3.111 | yes, worse |
| second app: response time (ms), 95th percentile | 286.7 | 249.3 | -13.1% | -101.7 to +26.92 | no |
| second app: response time (ms), 99th percentile | 909.2 | 722.4 | -20.5% | -758.5 to +384.9 | no |
| second app: time over the response line (% of samples) | 14.78 | 14.45 | -2.2% | -1.225 to +0.5771 | no |
| second app: failed requests (%) | 13.39 | 13.72 | +2.5% | -0.03806 to +0.7006 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.972 | -0.5% | -0.07577 to +0.02022 | no |
| node-hours | 1.512 | 1.506 | -0.5% | -0.01974 to +0.006071 | no |
| energy, parked workers still on at idle power (Wh, declared model) | 172.6 | 172.3 | -0.2% | -0.7682 to +0.1433 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 172.6 | 171.8 | -0.5% | -1.913 to +0.2385 | no |
| response time (ms), mean | 577.9 | 412.8 | -28.6% | -238.8 to -91.42 | yes, better |
| response time (ms), 95th percentile | 2537 | 2006 | -21.0% | -887 to -176.7 | yes, better |
| response time (ms), 99th percentile | 6111 | 4584 | -25.0% | -2573 to -481.6 | yes, better |
| time over the response line (% of samples) | 25.27 | 20.58 | -18.6% | -6.224 to -3.153 | yes, better |
| failed requests (%) | 3.892 | 4.902 | +26.0% | +0.1186 to +1.902 | yes, worse |
| pending pods, pod-minutes | 1.373 | 2.268 | +65.2% | +0.1554 to +1.635 | yes, worse |
| utilisation (used / allocatable) | 0.09886 | 0.09756 | -1.3% | -0.002733 to +0.0001199 | no |
| CPU used (cores), mean | 2.373 | 2.334 | -1.6% | -0.06974 to -0.008022 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01515 | +0.0152 (native is 0) | +0.01327 to +0.01703 | yes, more |
| CPU used with Omni's own (cores), mean | 2.373 | 2.349 | -1.0% | -0.05502 to +0.007557 | no |
| energy per core-hour (Wh, the 25 W standby model) | 297.9 | 301.2 | +1.1% | -0.9463 to +7.407 | no |
| HPA replicas, mean | 15.29 | 14.48 | -5.3% | -1.132 to -0.4945 | yes, better |
| pods started | 4.2 | 4.7 | +11.9% | -0.2726 to +1.273 | no |
| pod start wait, total (s) | 9.8 | 17 | +73.5% | +3.525 to +10.88 | yes, worse |
| pod start wait, mean (s) | 1.955 | 3.588 | +83.5% | +0.8709 to +2.394 | yes, worse |
| second app: response time (ms), 95th percentile | 286.7 | 255.4 | -10.9% | -70.07 to +7.454 | no |
| second app: response time (ms), 99th percentile | 909.2 | 1139 | +25.3% | -237.3 to +696.6 | no |
| second app: time over the response line (% of samples) | 14.78 | 14.6 | -1.2% | -0.8628 to +0.5079 | no |
| second app: failed requests (%) | 13.39 | 13.46 | +0.6% | -0.2357 to +0.3893 | no |
