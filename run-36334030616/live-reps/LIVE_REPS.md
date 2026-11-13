# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni alone |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 2.612 | 2.238 |
| node-hours | 1.51 | 0.6577 | 0.5632 |
| energy (Wh) | 158.3 | 94.56 | 87.49 |
| response time (ms), mean | 134.1 | 130.4 | 129.1 |
| response time (ms), 95th percentile | 287.2 | 272.7 | 260.1 |
| response time (ms), 99th percentile | 413.4 | 399.6 | 380 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.2633 | 0.7433 | 0.9967 |
| utilisation (used / allocatable) | 0.0371 | 0.08383 | 0.09378 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 2.612 | -56.5% | -4.217 to -2.56 | yes, better |
| node-hours | 1.51 | 0.6577 | -56.4% | -1.057 to -0.6467 | yes, better |
| energy (Wh) | 158.3 | 94.56 | -40.2% | -79.03 to -48.37 | yes, better |
| response time (ms), mean | 134.1 | 130.4 | -2.7% | -8.874 to +1.555 | no |
| response time (ms), 95th percentile | 287.2 | 272.7 | -5.1% | -42.6 to +13.56 | no |
| response time (ms), 99th percentile | 413.4 | 399.6 | -3.3% | -55.93 to +28.37 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2633 | 0.7433 | +182.3% | +0.05209 to +0.9079 | yes, worse |
| utilisation (used / allocatable) | 0.0371 | 0.08383 | +126.0% | +0.02687 to +0.0666 | yes, better |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 2.238 | -62.7% | -3.959 to -3.565 | yes, better |
| node-hours | 1.51 | 0.5632 | -62.7% | -1 to -0.8927 | yes, better |
| energy (Wh) | 158.3 | 87.49 | -44.7% | -74.95 to -66.6 | yes, better |
| response time (ms), mean | 134.1 | 129.1 | -3.7% | -9.283 to -0.6174 | yes, better |
| response time (ms), 95th percentile | 287.2 | 260.1 | -9.4% | -46.57 to -7.564 | yes, better |
| response time (ms), 99th percentile | 413.4 | 380 | -8.1% | -59.39 to -7.317 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2633 | 0.9967 | +278.5% | -0.1066 to +1.573 | no |
| utilisation (used / allocatable) | 0.0371 | 0.09378 | +152.8% | +0.04982 to +0.06354 | yes, better |
