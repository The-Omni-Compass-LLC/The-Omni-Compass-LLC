# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni watches only | Omni on top | Omni alone |
|---|---:|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 | 5.634 |
| node-hours | 1.509 | 1.512 | 1.511 | 1.416 |
| energy (Wh) | 158.2 | 158.4 | 158.5 | 149.1 |
| response time (ms), mean | 138 | 116.9 | 141.8 | 153.8 |
| response time (ms), 95th percentile | 283.6 | 246 | 286.9 | 316.5 |
| response time (ms), 99th percentile | 410.8 | 341.5 | 420 | 444.8 |
| failed requests (%) | 0 | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.32 | 0.43 | 0.2133 | 0.1033 |
| utilisation (used / allocatable) | 0.03737 | 0.03631 | 0.03756 | 0.04044 |

## W: Omni-Compass watches only (dry run: the cost of being there) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.019e-16 to +1.612e-15 | no |
| node-hours | 1.509 | 1.512 | +0.2% | -0.01577 to +0.0231 | no |
| energy (Wh) | 158.2 | 158.4 | +0.1% | -0.9897 to +1.302 | no |
| response time (ms), mean | 138 | 116.9 | -15.3% | -109.3 to +67.09 | no |
| response time (ms), 95th percentile | 283.6 | 246 | -13.3% | -187 to +111.8 | no |
| response time (ms), 99th percentile | 410.8 | 341.5 | -16.9% | -296.5 to +157.9 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.32 | 0.43 | +34.4% | -0.9885 to +1.209 | no |
| utilisation (used / allocatable) | 0.03737 | 0.03631 | -2.8% | -0.006407 to +0.004298 | no |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.124e-15 to +1.835e-15 | no |
| node-hours | 1.509 | 1.511 | +0.1% | -0.01588 to +0.01988 | no |
| energy (Wh) | 158.2 | 158.5 | +0.2% | -1.033 to +1.528 | no |
| response time (ms), mean | 138 | 141.8 | +2.7% | -75.2 to +82.77 | no |
| response time (ms), 95th percentile | 283.6 | 286.9 | +1.2% | -124.3 to +130.9 | no |
| response time (ms), 99th percentile | 410.8 | 420 | +2.2% | -195.8 to +214.2 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.32 | 0.2133 | -33.3% | -0.97 to +0.7566 | no |
| utilisation (used / allocatable) | 0.03737 | 0.03756 | +0.5% | -0.003947 to +0.004331 | no |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.634 | -6.1% | -0.9876 to +0.256 | no |
| node-hours | 1.509 | 1.416 | -6.2% | -0.2493 to +0.0631 | no |
| energy (Wh) | 158.2 | 149.1 | -5.8% | -25.12 to +6.8 | no |
| response time (ms), mean | 138 | 153.8 | +11.4% | -34.95 to +66.38 | no |
| response time (ms), 95th percentile | 283.6 | 316.5 | +11.6% | -68.37 to +134.2 | no |
| response time (ms), 99th percentile | 410.8 | 444.8 | +8.3% | -128.8 to +196.9 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.32 | 0.1033 | -67.7% | -0.8906 to +0.4573 | no |
| utilisation (used / allocatable) | 0.03737 | 0.04044 | +8.2% | -0.001363 to +0.007519 | no |
