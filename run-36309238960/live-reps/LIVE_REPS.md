# Repeated live runs on kind (native vs Omni on top vs Omni alone)

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.3 | -11.7% | -1.891 to +0.4903 | no |
| node-hours | 1.511 | 1.334 | -11.7% | -0.4855 to +0.1312 | no |
| energy (Wh) | 166.8 | 148.5 | -11.0% | -50.12 to +13.53 | no |
| response time (ms), mean | 192 | 237.4 | +23.6% | -35.17 to +125.9 | no |
| response time (ms), 95th percentile | 378.9 | 482.8 | +27.4% | -16.98 to +224.8 | no |
| response time (ms), 99th percentile | 517.6 | 669.4 | +29.3% | -1.975 to +305.5 | no |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.71 | 0.3933 | -44.6% | -0.9611 to +0.3278 | no |
| utilisation (used / allocatable) | 0.07394 | 0.08251 | +11.6% | -0.008004 to +0.02515 | no |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 4.835 | -19.4% | -2.7 to +0.3698 | no |
| node-hours | 1.511 | 1.225 | -18.9% | -0.6791 to +0.1069 | no |
| energy (Wh) | 166.8 | 137.2 | -17.8% | -68.4 to +9.145 | no |
| response time (ms), mean | 192 | 221.5 | +15.4% | -71.21 to +130.2 | no |
| response time (ms), 95th percentile | 378.9 | 449.3 | +18.6% | -119.4 to +260.2 | no |
| response time (ms), 99th percentile | 517.6 | 626.5 | +21.0% | -113.9 to +331.6 | no |
| failed requests (%) | 0 | 0.02667 | +0.0267 (native is 0) | -0.04736 to +0.1007 | no |
| pending pods, pod-minutes | 0.71 | 0.3867 | -45.5% | -0.6121 to -0.03455 | yes, better |
| utilisation (used / allocatable) | 0.07394 | 0.0891 | +20.5% | -0.01632 to +0.04665 | no |
