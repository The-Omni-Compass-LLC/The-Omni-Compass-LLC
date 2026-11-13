# Repeated live runs on kind (native vs Omni watching only vs Omni on top vs Omni alone)

## All columns, mean over repetitions

| Gauge | Native | Omni on top | Omni on top, bowl law |
|---|---:|---:|---:|
| worker nodes in service, mean | 6 | 3.958 | 5.697 |
| node-hours | 1.522 | 1.003 | 1.443 |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.3 | 159.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 120.5 | 153.6 |
| response time (ms), mean | 156.4 | 89.3 | 80.28 |
| response time (ms), 95th percentile | 346.9 | 149.2 | 123.5 |
| response time (ms), 99th percentile | 571.1 | 245.9 | 165.2 |
| failed requests (%) | 0 | 0 | 0 |
| pending pods, pod-minutes | 0.265 | 0.1283 | 0.1567 |
| utilisation (used / allocatable) | 0.03926 | 0.05353 | 0.03882 |
| CPU used (cores), mean | 0.9423 | 0.8514 | 0.8874 |
| Omni's own CPU (cores), mean | 0 | 0.0184 | 0.01081 |
| CPU used with Omni's own (cores), mean | 0.9423 | 0.8698 | 0.8982 |
| energy per core-hour (Wh, the 25 W standby model) | 722 | 586.9 | 724 |
| HPA replicas, mean | 8.559 | 6.357 | 7.907 |
| pods started | 3.9 | 3.2 | 3.1 |
| pod start wait, total (s) | 11.2 | 6.2 | 8 |
| pod start wait, mean (s) | 2.64 | 2.126 | 2.61 |

**Energy on kind is a declared model, not a meter.** Every worker stays powered and Ready in every arm; the first
energy row counts a parked worker at its full idle power, which is what kind does. The second counts it at the
declared standby power, which needs a node autoscaler that really removes the machine; this run has none.

## B: Omni-Compass on top vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 3.958 | -34.0% | -2.573 to -1.511 | yes, better |
| node-hours | 1.522 | 1.003 | -34.1% | -0.652 to -0.3852 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.3 | -0.4% | -1.133 to -0.2884 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 120.5 | -24.7% | -49.3 to -29.71 | yes, better |
| response time (ms), mean | 156.4 | 89.3 | -42.9% | -89.71 to -44.58 | yes, better |
| response time (ms), 95th percentile | 346.9 | 149.2 | -57.0% | -257.8 to -137.7 | yes, better |
| response time (ms), 99th percentile | 571.1 | 245.9 | -56.9% | -444.4 to -206 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.265 | 0.1283 | -51.6% | -0.3747 to +0.1014 | no |
| utilisation (used / allocatable) | 0.03926 | 0.05353 | +36.3% | +0.009594 to +0.01894 | yes, more |
| CPU used (cores), mean | 0.9423 | 0.8514 | -9.7% | -0.1136 to -0.06826 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.0184 | +0.0184 (native is 0) | +0.01528 to +0.02152 | yes, more |
| CPU used with Omni's own (cores), mean | 0.9423 | 0.8698 | -7.7% | -0.09371 to -0.05137 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 722 | 586.9 | -18.7% | -218.3 to -51.81 | yes, better |
| HPA replicas, mean | 8.559 | 6.357 | -25.7% | -3.195 to -1.209 | yes, better |
| pods started | 3.9 | 3.2 | -17.9% | -2.008 to +0.6081 | no |
| pod start wait, total (s) | 11.2 | 6.2 | -44.6% | -10.93 to +0.9274 | no |
| pod start wait, mean (s) | 2.64 | 2.126 | -19.5% | -2.625 to +1.597 | no |

## B with the bowl law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.697 | -5.1% | -0.4104 to -0.1961 | yes, better |
| node-hours | 1.522 | 1.443 | -5.2% | -0.1059 to -0.05226 | yes, better |
| energy, parked workers still on at idle power (Wh, declared model) | 160 | 159.3 | -0.4% | -1.41 to -0.00945 | yes, better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 160 | 153.6 | -4.0% | -8.397 to -4.535 | yes, better |
| response time (ms), mean | 156.4 | 80.28 | -48.7% | -100.7 to -51.63 | yes, better |
| response time (ms), 95th percentile | 346.9 | 123.5 | -64.4% | -289.7 to -157.1 | yes, better |
| response time (ms), 99th percentile | 571.1 | 165.2 | -71.1% | -535.4 to -276.5 | yes, better |
| failed requests (%) | 0 | 0 | +0 (native is 0) | +0 to +0 | no |
| pending pods, pod-minutes | 0.265 | 0.1567 | -40.9% | -0.4418 to +0.2252 | no |
| utilisation (used / allocatable) | 0.03926 | 0.03882 | -1.1% | -0.001565 to +0.0006847 | no |
| CPU used (cores), mean | 0.9423 | 0.8874 | -5.8% | -0.08301 to -0.02676 | yes, less |
| Omni's own CPU (cores), mean | 0 | 0.01081 | +0.0108 (native is 0) | +0.009254 to +0.01237 | yes, more |
| CPU used with Omni's own (cores), mean | 0.9423 | 0.8982 | -4.7% | -0.07111 to -0.01704 | yes, less |
| energy per core-hour (Wh, the 25 W standby model) | 722 | 724 | +0.3% | -23.85 to +27.98 | no |
| HPA replicas, mean | 8.559 | 7.907 | -7.6% | -1.284 to -0.01979 | yes, better |
| pods started | 3.9 | 3.1 | -20.5% | -2.097 to +0.4972 | no |
| pod start wait, total (s) | 11.2 | 8 | -28.6% | -7.918 to +1.518 | no |
| pod start wait, mean (s) | 2.64 | 2.61 | -1.1% | -0.872 to +0.812 | no |
