# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni alone |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 5.821 |
| node-hours | 1.517 | 1.512 | 1.469 |
| energy (Wh) | 158.6 | 158.4 | 155.2 |
| response time (ms), mean | 112.8 | 112.1 | 113.1 |
| response time (ms), 95th percentile | 238.4 | 239.9 | 239.2 |
| response time (ms), 99th percentile | 373 | 362.6 | 352.3 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.2767 | 0.2133 | 0.2 |
| utilisation (used / allocatable) | 0.03531 | 0.03639 | 0.03763 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.028e-15 to +1.317e-15 | no |
| node-hours | 1.517 | 1.512 | -0.3% | -0.01888 to +0.009549 | no |
| energy (Wh) | 158.6 | 158.4 | -0.2% | -1.55 to +1.06 | no |
| response time (ms), mean | 112.8 | 112.1 | -0.6% | -4.743 to +3.392 | no |
| response time (ms), 95th percentile | 238.4 | 239.9 | +0.7% | -25.94 to +29.04 | no |
| response time (ms), 99th percentile | 373 | 362.6 | -2.8% | -49.68 to +28.93 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2767 | 0.2133 | -22.9% | -0.8013 to +0.6747 | no |
| utilisation (used / allocatable) | 0.03531 | 0.03639 | +3.1% | +0.0002654 to +0.001901 | yes, better |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.821 | -3.0% | -0.6774 to +0.3186 | no |
| node-hours | 1.517 | 1.469 | -3.2% | -0.1712 to +0.07491 | no |
| energy (Wh) | 158.6 | 155.2 | -2.2% | -12.59 to +5.75 | no |
| response time (ms), mean | 112.8 | 113.1 | +0.2% | -2.765 to +3.224 | no |
| response time (ms), 95th percentile | 238.4 | 239.2 | +0.4% | -29.61 to +31.32 | no |
| response time (ms), 99th percentile | 373 | 352.3 | -5.5% | -51.56 to +10.29 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2767 | 0.2 | -27.7% | -0.9176 to +0.7643 | no |
| utilisation (used / allocatable) | 0.03531 | 0.03763 | +6.6% | -0.001264 to +0.005907 | no |
