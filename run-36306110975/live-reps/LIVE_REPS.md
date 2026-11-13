# Repeated live runs on kind (native vs Omni on top vs Omni alone)

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.145e-16 to +1.991e-15 | no |
| node-hours | 1.512 | 1.515 | +0.2% | -0.009273 to +0.01461 | no |
| energy (Wh) | 167 | 167.1 | +0.0% | -2.147 to +2.306 | no |
| response time (ms), mean | 206.9 | 247.6 | +19.7% | -41.82 to +123.2 | no |
| response time (ms), 95th percentile | 417.1 | 502.7 | +20.5% | -54.58 to +225.7 | no |
| response time (ms), 99th percentile | 549.4 | 709.8 | +29.2% | -43.25 to +364.1 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.4 | 0.4033 | +0.8% | -0.3555 to +0.3621 | no |
| utilisation (used / allocatable) | 0.07441 | 0.0732 | -1.6% | -0.006842 to +0.004417 | no |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.174e-16 to +1.204e-15 | yes, worse |
| node-hours | 1.512 | 1.511 | -0.1% | -0.01562 to +0.01229 | no |
| energy (Wh) | 167 | 165.9 | -0.7% | -4.138 to +1.856 | no |
| response time (ms), mean | 206.9 | 216.7 | +4.7% | -102.2 to +121.8 | no |
| response time (ms), 95th percentile | 417.1 | 444.6 | +6.6% | -146.9 to +201.8 | no |
| response time (ms), 99th percentile | 549.4 | 617.5 | +12.4% | -133.3 to +269.6 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.4 | 0.4167 | +4.2% | -0.3615 to +0.3948 | no |
| utilisation (used / allocatable) | 0.07441 | 0.06994 | -6.0% | -0.01342 to +0.004475 | no |
