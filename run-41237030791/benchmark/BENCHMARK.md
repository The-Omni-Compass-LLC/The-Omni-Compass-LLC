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
| duration (min) | 20.23 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.7% |
| power (W), mean | 629 | 643 | +2.1% |
| power (W), peak | 651 | 687 | +5.5% |
| energy (Wh) | 212 | 215 | +1.4% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.4% |
| CPU used (cores), mean | 0.901 | 1.25 | +39.2% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.052 | +39.2% |
| energy per core-hour (Wh) | 698 | 512 | -26.6% |
| node-hours per core-hour | 6.66 | 4.78 | -28.2% |
| pending pods, pod-minutes | 0.533 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.07 | 9.42 | +3.9% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.533 | +0.0% |
| requests timed | 1,020 | 1,095 | +7.4% |
| time over the response line (% of samples) | 0.882 | 0.000 | -100.0% |
| response time (ms), mean | 179 | 97.02 | -45.7% |
| response time (ms), median | 144 | 82.30 | -42.9% |
| response time (ms), 95th percentile | 357 | 158 | -55.6% |
| response time (ms), 99th percentile | 494 | 205 | -58.5% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2705 | 5.2131 | -28.3% | [-3.6429, -0.4448] | GAIN |
| kwh_per_core_hour | 0.7590 | 0.5548 | -26.9% | [-0.3634, -0.0464] | GAIN |
| utilisation | 0.0371 | 0.0533 | +43.7% | [+0.0032, +0.0304] | GAIN |
| pending_pod_minutes_per_hour | 1.5118 | 0.0000 | -100.0% | [-4.5354, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5178 | 1.6865 | +11.1% | [-2.9450, +3.3662] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.445 0.468 0.488 0.505 0.521 0.534 0.547 0.557 0.563 0.568 0.572 0.577 0.581 0.585 0.588 0.59 0.591
- nodes decided per minute: 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 618 | 620 | 5.00 | 6.00 | 0.000 | 0.000 | 0.575 | 0.663 |
| 1 | 6.00 | 6.00 | 617 | 627 | 6.00 | 7.00 | 0.000 | 0.000 | 0.582 | 0.821 |
| 2 | 6.00 | 6.00 | 619 | 624 | 6.00 | 8.00 | 0.000 | 0.000 | 0.636 | 0.776 |
| 3 | 6.00 | 6.00 | 622 | 632 | 6.00 | 8.00 | 0.000 | 0.000 | 0.699 | 0.977 |
| 4 | 6.00 | 6.00 | 633 | 651 | 9.00 | 10.00 | 0.500 | 0.000 | 1.00 | 1.48 |
| 5 | 6.00 | 6.00 | 634 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.44 |
| 6 | 6.00 | 6.00 | 634 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.46 |
| 7 | 6.00 | 6.00 | 647 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.06 |
| 8 | 6.00 | 6.00 | 647 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.06 |
| 9 | 6.00 | 6.00 | 648 | 679 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 2.17 |
| 10 | 6.00 | 6.00 | 638 | 664 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 1.80 |
| 11 | 6.00 | 6.00 | 620 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.639 | 0.784 |
| 12 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.627 | 0.763 |
| 13 | 6.00 | 6.00 | 624 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.770 | 0.996 |
| 14 | 6.00 | 6.00 | 633 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.43 |
| 15 | 6.00 | 6.00 | 637 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.38 |
| 16 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.996 | 1.36 |
| 17 | 6.00 | 6.00 | 627 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.844 | 1.22 |
| 18 | 6.00 | 6.00 | 620 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.621 | 0.788 |
| 19 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.615 | 0.755 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
