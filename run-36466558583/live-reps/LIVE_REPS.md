# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.745 |
| node-hours | 1.514 | 1.201 |
| energy (Wh) | 159 | 138 |
| response time (ms), mean | 151.9 | 107.5 |
| response time (ms), 95th percentile | 304.9 | 191.4 |
| response time (ms), 99th percentile | 438.1 | 298.7 |
| failed requests (%) | 0 | 0 |
| pending pods, pod-minutes | 0.105 | 0.355 |
| utilisation (used / allocatable) | 0.03796 | 0.06066 |
| CPU used (cores), mean | 0.911 | 1.146 |
| energy per core-hour (Wh) | 692 | 479.4 |
| HPA replicas, mean | 8.942 | 7.844 |
| pods started | 4.6 | 6.3 |
| pod start wait, total (s) | 10.2 | 17 |
| pod start wait, mean (s) | 2.135 | 2.404 |

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.745 | -20.9% | -1.524 to -0.986 | yes, better |
| node-hours | 1.514 | 1.201 | -20.7% | -0.3815 to -0.2453 | yes, better |
| energy (Wh) | 159 | 138 | -13.2% | -26.16 to -15.72 | yes, better |
| response time (ms), mean | 151.9 | 107.5 | -29.2% | -55.45 to -33.36 | yes, better |
| response time (ms), 95th percentile | 304.9 | 191.4 | -37.2% | -148.4 to -78.55 | yes, better |
| response time (ms), 99th percentile | 438.1 | 298.7 | -31.8% | -191.3 to -87.37 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.105 | 0.355 | +238.1% | -0.07431 to +0.5743 | no |
| utilisation (used / allocatable) | 0.03796 | 0.06066 | +59.8% | +0.01839 to +0.027 | yes, better |
| CPU used (cores), mean | 0.911 | 1.146 | +25.8% | +0.1706 to +0.3002 | yes, better |
| energy per core-hour (Wh) | 692 | 479.4 | -30.7% | -239.9 to -185.2 | yes, better |
| HPA replicas, mean | 8.942 | 7.844 | -12.3% | -1.616 to -0.5808 | yes, better |
| pods started | 4.6 | 6.3 | +37.0% | -0.1174 to +3.517 | no |
| pod start wait, total (s) | 10.2 | 17 | +66.7% | -1.979 to +15.58 | no |
| pod start wait, mean (s) | 2.135 | 2.404 | +12.6% | -1.064 to +1.602 | no |
