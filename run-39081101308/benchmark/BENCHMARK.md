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
| duration (min) | 20.22 | 20.02 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.00 | -1.0% |
| power (W), mean | 629 | 643 | +2.3% |
| power (W), peak | 654 | 687 | +5.0% |
| energy (Wh) | 212 | 215 | +1.3% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.3% |
| CPU used (cores), mean | 0.878 | 1.27 | +44.5% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.037 | 0.053 | +44.5% |
| energy per core-hour (Wh) | 716 | 507 | -29.2% |
| node-hours per core-hour | 6.83 | 4.73 | -30.8% |
| pending pods, pod-minutes | 0.533 | 0.533 | +0.0% |
| pending pods, peak | 1.00 | 2.00 | +100.0% |
| HPA replicas, mean | 8.93 | 9.40 | +5.3% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.800 | +54.8% |
| requests timed | 1,070 | 1,100 | +2.8% |
| time over the response line (% of samples) | 0.187 | 0.000 | -100.0% |
| response time (ms), mean | 125 | 95.04 | -24.0% |
| response time (ms), median | 111 | 82.45 | -25.8% |
| response time (ms), 95th percentile | 261 | 151 | -42.2% |
| response time (ms), 99th percentile | 406 | 178 | -56.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.6202 | 5.1128 | -32.9% | [-4.3188, -0.7602] | GAIN |
| kwh_per_core_hour | 0.7942 | 0.5450 | -31.4% | [-0.4253, -0.0831] | GAIN |
| utilisation | 0.0362 | 0.0539 | +49.0% | [+0.0045, +0.0324] | GAIN |
| pending_pod_minutes_per_hour | 1.5122 | 1.6798 | +11.1% | [-4.5366, +5.0394] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4517 | 2.4798 | +70.8% | [-2.1834, +5.0282] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.469 0.488 0.505 0.521 0.534 0.547 0.557 0.563 0.568 0.572 0.577 0.581 0.585 0.588 0.59 0.591
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
| 0 | 6.00 | 6.00 | 616 | 632 | 5.00 | 5.00 | 0.000 | 0.500 | 0.505 | 0.965 |
| 1 | 6.00 | 6.00 | 618 | 624 | 5.00 | 7.50 | 0.000 | 0.000 | 0.574 | 0.779 |
| 2 | 6.00 | 6.00 | 616 | 625 | 5.00 | 8.00 | 0.000 | 0.000 | 0.535 | 0.724 |
| 3 | 6.00 | 6.00 | 620 | 634 | 5.00 | 8.00 | 0.500 | 0.000 | 0.636 | 1.04 |
| 4 | 6.00 | 6.00 | 638 | 649 | 9.00 | 10.00 | 0.000 | 0.000 | 1.11 | 1.42 |
| 5 | 6.00 | 6.00 | 634 | 653 | 10.00 | 10.00 | 0.000 | 0.000 | 0.972 | 1.53 |
| 6 | 6.00 | 6.00 | 633 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.42 |
| 7 | 6.00 | 6.00 | 648 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.97 |
| 8 | 6.00 | 6.00 | 648 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 2.18 |
| 9 | 6.00 | 6.00 | 649 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 2.21 |
| 10 | 6.00 | 6.00 | 644 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.08 |
| 11 | 6.00 | 6.00 | 616 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.526 | 0.729 |
| 12 | 6.00 | 6.00 | 619 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.618 | 0.785 |
| 13 | 6.00 | 6.00 | 624 | 637 | 10.00 | 10.00 | 0.000 | 0.000 | 0.720 | 1.08 |
| 14 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.992 | 1.34 |
| 15 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.41 |
| 16 | 6.00 | 6.00 | 633 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.41 |
| 17 | 6.00 | 6.00 | 627 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.862 | 0.945 |
| 18 | 6.00 | 6.00 | 615 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.540 | 0.780 |
| 19 | 6.00 | 6.00 | 616 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.542 | 0.687 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
