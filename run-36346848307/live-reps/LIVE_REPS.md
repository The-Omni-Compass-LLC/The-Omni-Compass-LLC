# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni alone |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 6 | 6 |
| node-hours | 1.516 | 1.515 | 1.524 |
| energy (Wh) | 159.3 | 162.4 | 163.2 |
| response time (ms), mean | 162.1 | 98.66 | 97.38 |
| response time (ms), 95th percentile | 328.5 | 152.3 | 150.7 |
| response time (ms), 99th percentile | 473.9 | 204.3 | 179.5 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.05333 | 0.32 | 0.1067 |
| utilisation (used / allocatable) | 0.03864 | 0.05286 | 0.05188 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.055e-15 to +3.187e-15 | no |
| node-hours | 1.516 | 1.515 | -0.1% | -0.01607 to +0.0134 | no |
| energy (Wh) | 159.3 | 162.4 | +1.9% | +1.608 to +4.604 | yes, worse |
| response time (ms), mean | 162.1 | 98.66 | -39.1% | -74.12 to -52.73 | yes, better |
| response time (ms), 95th percentile | 328.5 | 152.3 | -53.6% | -209.6 to -142.7 | yes, better |
| response time (ms), 99th percentile | 473.9 | 204.3 | -56.9% | -320.8 to -218.4 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.05333 | 0.32 | +500.0% | -0.1388 to +0.6721 | no |
| utilisation (used / allocatable) | 0.03864 | 0.05286 | +36.8% | +0.01343 to +0.01501 | yes, better |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.433e-16 to +1.988e-15 | yes, worse |
| node-hours | 1.516 | 1.524 | +0.5% | +0.0046 to +0.0114 | yes, worse |
| energy (Wh) | 159.3 | 163.2 | +2.4% | +3.416 to +4.288 | yes, worse |
| response time (ms), mean | 162.1 | 97.38 | -39.9% | -75.8 to -53.6 | yes, better |
| response time (ms), 95th percentile | 328.5 | 150.7 | -54.1% | -210.5 to -145.1 | yes, better |
| response time (ms), 99th percentile | 473.9 | 179.5 | -62.1% | -349.2 to -239.7 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.05333 | 0.1067 | +100.0% | -0.2236 to +0.3303 | no |
| utilisation (used / allocatable) | 0.03864 | 0.05188 | +34.3% | +0.01241 to +0.01407 | yes, better |
