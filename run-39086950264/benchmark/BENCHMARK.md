# Omni-Compass benchmark: Kubernetes native vs Kubernetes + Omni-Compass

Two identical kind clusters (1 control plane + 6 workers), same add-ons, workload (php-apache + HPA, target 50),
load schedule and capture. **Native**: Omni-Compass not running. **Omni**: Omni-Compass drives the HPA target, the
node pool (cordon/drain/uncordon), the power cap (in-place CPU limits on the app pods, enforced by the kernel), heat
(harness law on live power), security (hold signal) and the rollout guard. Response times are real HTTP requests timed
every 5 s. Power is a declared model (idle 100 W + 150 W x utilisation per worker in service; parked workers on
standby at idle power), not a meter.

## Gauges

| Gauge | Native | Omni-Compass | Change |
|---|---:|---:|---:|
| duration (min) | 20.23 | 20.02 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.00 | -1.1% |
| power (W), mean | 628 | 639 | +1.7% |
| power (W), peak | 648 | 678 | +4.6% |
| energy (Wh) | 212 | 213 | +0.7% |
| energy, parked workers still on at idle power (Wh) | 212 | 213 | +0.7% |
| CPU used (cores), mean | 0.848 | 1.14 | +34.2% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.047 | +34.2% |
| energy per core-hour (Wh) | 740 | 561 | -24.2% |
| node-hours per core-hour | 7.07 | 5.27 | -25.5% |
| pending pods, pod-minutes | 0.250 | 0.567 | +126.7% |
| pending pods, peak | 1.00 | 2.00 | +100.0% |
| HPA replicas, mean | 8.73 | 9.27 | +6.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.03 | 0.550 | -46.8% |
| requests timed | 1,100 | 1,120 | +1.8% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 95.64 | 75.91 | -20.6% |
| response time (ms), median | 83.40 | 67.50 | -19.1% |
| response time (ms), 95th percentile | 219 | 106 | -51.8% |
| response time (ms), 99th percentile | 314 | 131 | -58.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.7461 | 5.9271 | -23.5% | [-3.6173, -0.0595] | GAIN |
| kwh_per_core_hour | 0.8067 | 0.6263 | -22.4% | [-0.3520, -0.0145] | GAIN |
| utilisation | 0.0350 | 0.0468 | +33.5% | [+0.0005, +0.0241] | GAIN |
| pending_pod_minutes_per_hour | 0.7258 | 1.6320 | +124.9% | [-2.0015, +4.8960] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.9818 | 1.5840 | -46.9% | [-4.4334, +1.6331] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.393 0.422 0.446 0.469 0.488 0.504 0.52 0.533 0.545 0.555 0.561 0.566 0.571 0.575 0.579 0.583 0.587 0.588 0.59
- nodes decided per minute: 6 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
- HPA target decided per minute (%): 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77

## Reset

```
restored target: 50
workers in service: 6 of 6
Omni records left after kill: none
```

## Minute by minute

| min | nodes native | nodes omni | power W native | power W omni | replicas native | replicas omni | pending native | pending omni | CPU native | CPU omni |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.00 | 6.00 | 615 | 622 | 4.00 | 5.00 | 0.000 | 0.500 | 0.505 | 0.691 |
| 1 | 6.00 | 6.00 | 620 | 625 | 5.00 | 7.00 | 0.000 | 0.000 | 0.626 | 0.777 |
| 2 | 6.00 | 6.00 | 615 | 622 | 5.00 | 7.00 | 0.000 | 0.000 | 0.511 | 0.692 |
| 3 | 6.00 | 6.00 | 619 | 634 | 5.50 | 7.00 | 0.250 | 0.000 | 0.630 | 0.832 |
| 4 | 6.00 | 6.00 | 633 | 645 | 8.00 | 10.00 | 0.000 | 0.000 | 0.989 | 1.31 |
| 5 | 6.00 | 6.00 | 630 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 0.914 | 1.31 |
| 6 | 6.00 | 6.00 | 630 | 644 | 9.00 | 10.00 | 0.000 | 0.000 | 0.916 | 1.30 |
| 7 | 6.00 | 6.00 | 644 | 665 | 9.50 | 10.00 | 0.000 | 0.000 | 1.29 | 1.85 |
| 8 | 6.00 | 6.00 | 647 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 1.86 |
| 9 | 6.00 | 6.00 | 642 | 667 | 10.00 | 10.00 | 0.000 | 0.000 | 1.23 | 1.95 |
| 10 | 6.00 | 6.00 | 640 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 1.63 |
| 11 | 6.00 | 6.00 | 618 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.598 | 0.630 |
| 12 | 6.00 | 6.00 | 619 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.594 | 0.717 |
| 13 | 6.00 | 6.00 | 622 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.689 | 0.844 |
| 14 | 6.00 | 6.00 | 631 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.951 | 1.19 |
| 15 | 6.00 | 6.00 | 633 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.991 | 1.28 |
| 16 | 6.00 | 6.00 | 634 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.28 |
| 17 | 6.00 | 6.00 | 626 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.814 | 0.945 |
| 18 | 6.00 | 6.00 | 618 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.605 | 0.641 |
| 19 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.513 | 0.773 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
