# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top |
|---|---:|---:|
| worker nodes in service, mean | 6 | 3.833 |
| node-hours | 1.519 | 0.9677 |
| energy (Wh) | 159.6 | 120.7 |
| response time (ms), mean | 161.6 | 116.4 |
| response time (ms), 95th percentile | 323.6 | 212.2 |
| response time (ms), 99th percentile | 457.9 | 306.5 |
| failed requests (%) | 0 | 0 |
| pending pods, pod-minutes | 0.21 | 0.9767 |
| utilisation (used / allocatable) | 0.03872 | 0.07582 |
| CPU used (cores), mean | 0.9294 | 1.151 |
| energy per core-hour (Wh) | 678.5 | 414.8 |
| HPA replicas, mean | 8.912 | 9.179 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.833 | -36.1% | -2.801 to -1.533 | yes, better |
| node-hours | 1.519 | 0.9677 | -36.3% | -0.7072 to -0.3948 | yes, better |
| energy (Wh) | 159.6 | 120.7 | -24.4% | -50.78 to -27.07 | yes, better |
| response time (ms), mean | 161.6 | 116.4 | -28.0% | -56.79 to -33.63 | yes, better |
| response time (ms), 95th percentile | 323.6 | 212.2 | -34.4% | -152.9 to -69.94 | yes, better |
| response time (ms), 99th percentile | 457.9 | 306.5 | -33.1% | -240.2 to -62.65 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.21 | 0.9767 | +365.1% | +0.321 to +1.212 | yes, worse |
| utilisation (used / allocatable) | 0.03872 | 0.07582 | +95.8% | +0.02777 to +0.04643 | yes, better |
| CPU used (cores), mean | 0.9294 | 1.151 | +23.9% | +0.1583 to +0.2855 | yes, better |
| energy per core-hour (Wh) | 678.5 | 414.8 | -38.9% | -292.1 to -235.3 | yes, better |
| HPA replicas, mean | 8.912 | 9.179 | +3.0% | -0.0859 to +0.6202 | no |
