# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni alone |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 3.774 | 5.821 |
| node-hours | 1.513 | 0.9517 | 1.473 |
| energy (Wh) | 158.5 | 118.3 | 157.9 |
| response time (ms), mean | 116.2 | 82.42 | 73.6 |
| response time (ms), 95th percentile | 244.3 | 144.7 | 113.1 |
| response time (ms), 99th percentile | 367.7 | 234.1 | 145.1 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.2067 | 0.54 | 0.32 |
| utilisation (used / allocatable) | 0.03647 | 0.06954 | 0.04792 |
| CPU used (cores), mean | 0.8752 | 1.051 | 1.112 |
| energy per core-hour (Wh) | 721.7 | 451.8 | 567.7 |
| HPA replicas, mean | 8.803 | 9.239 | 9.738 |

## B: Omni-Compass on top vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.774 | -37.1% | -2.439 to -2.013 | yes, better |
| node-hours | 1.513 | 0.9517 | -37.1% | -0.611 to -0.5117 | yes, better |
| energy (Wh) | 158.5 | 118.3 | -25.4% | -44.5 to -35.96 | yes, better |
| response time (ms), mean | 116.2 | 82.42 | -29.1% | -55.02 to -12.57 | yes, better |
| response time (ms), 95th percentile | 244.3 | 144.7 | -40.8% | -142.1 to -57.3 | yes, better |
| response time (ms), 99th percentile | 367.7 | 234.1 | -36.4% | -197.5 to -69.85 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2067 | 0.54 | +161.3% | -0.6099 to +1.277 | no |
| utilisation (used / allocatable) | 0.03647 | 0.06954 | +90.7% | +0.02673 to +0.03942 | yes, better |
| CPU used (cores), mean | 0.8752 | 1.051 | +20.0% | +0.0902 to +0.2605 | yes, better |
| energy per core-hour (Wh) | 721.7 | 451.8 | -37.4% | -282.4 to -257.3 | yes, better |
| HPA replicas, mean | 8.803 | 9.239 | +5.0% | -0.1209 to +0.9928 | no |

## C: Omni-Compass decides (strict) vs native, 5 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.821 | -3.0% | -0.6772 to +0.3185 | no |
| node-hours | 1.513 | 1.473 | -2.6% | -0.1662 to +0.08616 | no |
| energy (Wh) | 158.5 | 157.9 | -0.4% | -10.1 to +8.894 | no |
| response time (ms), mean | 116.2 | 73.6 | -36.7% | -66.89 to -18.34 | yes, better |
| response time (ms), 95th percentile | 244.3 | 113.1 | -53.7% | -177.9 to -84.62 | yes, better |
| response time (ms), 99th percentile | 367.7 | 145.1 | -60.5% | -291.5 to -153.8 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.2067 | 0.32 | +54.8% | -0.6008 to +0.8275 | no |
| utilisation (used / allocatable) | 0.03647 | 0.04792 | +31.4% | +0.0059 to +0.01701 | yes, better |
| CPU used (cores), mean | 0.8752 | 1.112 | +27.1% | +0.1469 to +0.3268 | yes, better |
| energy per core-hour (Wh) | 721.7 | 567.7 | -21.3% | -197.3 to -110.6 | yes, better |
| HPA replicas, mean | 8.803 | 9.738 | +10.6% | +0.725 to +1.145 | yes, worse |
