# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top |
|---|---:|---:|
| worker nodes in service, mean | 6 | 4.921 |
| node-hours | 1.517 | 1.244 |
| energy (Wh) | 158.9 | 140.8 |
| response time (ms), mean | 129.9 | 83.68 |
| response time (ms), 95th percentile | 267.4 | 126.9 |
| response time (ms), 99th percentile | 371.5 | 170.9 |
| failed requests (%) | 0 | 0 |
| pending pods, pod-minutes | 0.2033 | 0.52 |
| utilisation (used / allocatable) | 0.03641 | 0.058 |
| CPU used (cores), mean | 0.8739 | 1.125 |
| energy per core-hour (Wh) | 721.8 | 503.3 |
| HPA replicas, mean | 8.886 | 6.73 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.921 | -18.0% | -1.823 to -0.3341 | yes, better |
| node-hours | 1.517 | 1.244 | -18.0% | -0.4686 to -0.07752 | yes, better |
| energy (Wh) | 158.9 | 140.8 | -11.3% | -32.69 to -3.365 | yes, better |
| response time (ms), mean | 129.9 | 83.68 | -35.6% | -70.85 to -21.69 | yes, better |
| response time (ms), 95th percentile | 267.4 | 126.9 | -52.6% | -191.4 to -89.72 | yes, better |
| response time (ms), 99th percentile | 371.5 | 170.9 | -54.0% | -275.9 to -125.3 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2033 | 0.52 | +155.7% | -0.1906 to +0.8239 | no |
| utilisation (used / allocatable) | 0.03641 | 0.058 | +59.3% | +0.01037 to +0.03281 | yes, better |
| CPU used (cores), mean | 0.8739 | 1.125 | +28.7% | +0.1512 to +0.3501 | yes, better |
| energy per core-hour (Wh) | 721.8 | 503.3 | -30.3% | -274.3 to -162.8 | yes, better |
| HPA replicas, mean | 8.886 | 6.73 | -24.3% | -3.555 to -0.7563 | yes, better |
