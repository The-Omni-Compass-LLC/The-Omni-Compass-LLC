# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni alone |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 3.872 | 6 |
| node-hours | 1.516 | 0.9803 | 1.519 |
| energy (Wh) | 159.2 | 121.9 | 162.5 |
| response time (ms), mean | 153.9 | 110.6 | 94.18 |
| response time (ms), 95th percentile | 320.8 | 204.7 | 151.5 |
| response time (ms), 99th percentile | 475.4 | 293.3 | 185.5 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.16 | 0.94 | 0.5233 |
| utilisation (used / allocatable) | 0.03846 | 0.07533 | 0.0515 |
| CPU used (cores), mean | 0.9229 | 1.166 | 1.236 |
| energy per core-hour (Wh) | 683.3 | 413.4 | 519.6 |
| HPA replicas, mean | 8.942 | 9.217 | 9.834 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.872 | -35.5% | -2.505 to -1.75 | yes, better |
| node-hours | 1.516 | 0.9803 | -35.3% | -0.6245 to -0.4462 | yes, better |
| energy (Wh) | 159.2 | 121.9 | -23.4% | -44.53 to -30.03 | yes, better |
| response time (ms), mean | 153.9 | 110.6 | -28.2% | -58.36 to -28.41 | yes, better |
| response time (ms), 95th percentile | 320.8 | 204.7 | -36.2% | -178.6 to -53.66 | yes, better |
| response time (ms), 99th percentile | 475.4 | 293.3 | -38.3% | -294.6 to -69.61 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.16 | 0.94 | +487.5% | -0.1392 to +1.699 | no |
| utilisation (used / allocatable) | 0.03846 | 0.07533 | +95.9% | +0.03448 to +0.03926 | yes, better |
| CPU used (cores), mean | 0.9229 | 1.166 | +26.3% | +0.1544 to +0.3309 | yes, better |
| energy per core-hour (Wh) | 683.3 | 413.4 | -39.5% | -291.6 to -248.2 | yes, better |
| HPA replicas, mean | 8.942 | 9.217 | +3.1% | -0.3112 to +0.8601 | no |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.973e-16 to +1.918e-15 | no |
| node-hours | 1.516 | 1.519 | +0.2% | -0.01055 to +0.01721 | no |
| energy (Wh) | 159.2 | 162.5 | +2.1% | +2.147 to +4.539 | yes, worse |
| response time (ms), mean | 153.9 | 94.18 | -38.8% | -65.8 to -53.73 | yes, better |
| response time (ms), 95th percentile | 320.8 | 151.5 | -52.8% | -192.2 to -146.5 | yes, better |
| response time (ms), 99th percentile | 475.4 | 185.5 | -61.0% | -334.2 to -245.7 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.16 | 0.5233 | +227.1% | -0.365 to +1.092 | no |
| utilisation (used / allocatable) | 0.03846 | 0.0515 | +33.9% | +0.01181 to +0.01426 | yes, better |
| CPU used (cores), mean | 0.9229 | 1.236 | +33.9% | +0.2835 to +0.3423 | yes, better |
| energy per core-hour (Wh) | 683.3 | 519.6 | -24.0% | -183.8 to -143.5 | yes, better |
| HPA replicas, mean | 8.942 | 9.834 | +10.0% | +0.557 to +1.227 | yes, worse |
