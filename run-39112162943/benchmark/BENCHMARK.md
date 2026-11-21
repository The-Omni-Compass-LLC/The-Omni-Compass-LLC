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
| duration (min) | 20.20 | 20.02 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.00 | -0.9% |
| power (W), mean | 629 | 643 | +2.3% |
| power (W), peak | 651 | 687 | +5.5% |
| energy (Wh) | 212 | 215 | +1.4% |
| energy, parked workers still on at idle power (Wh) | 212 | 215 | +1.4% |
| CPU used (cores), mean | 0.878 | 1.28 | +45.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.053 | +45.4% |
| energy per core-hour (Wh) | 716 | 504 | -29.6% |
| node-hours per core-hour | 6.83 | 4.70 | -31.2% |
| pending pods, pod-minutes | 0.000 | 0.567 | new |
| pending pods, peak | 0.000 | 2.00 | new |
| HPA replicas, mean | 8.89 | 9.26 | +4.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.30 | 0.550 | -57.7% |
| requests timed | 1,065 | 1,100 | +3.3% |
| time over the response line (% of samples) | 0.188 | 0.000 | -100.0% |
| response time (ms), mean | 129 | 95.63 | -25.6% |
| response time (ms), median | 112 | 82.40 | -26.6% |
| response time (ms), 95th percentile | 262 | 153 | -41.6% |
| response time (ms), 99th percentile | 372 | 170 | -54.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.3739 | 5.0753 | -31.2% | [-3.7961, -0.7778] | GAIN |
| kwh_per_core_hour | 0.7699 | 0.5413 | -29.7% | [-0.3763, -0.0832] | GAIN |
| utilisation | 0.0363 | 0.0543 | +49.7% | [+0.0054, +0.0322] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 1.7848 | n/a | [+0.0000, +5.3543] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.8109 | 1.7389 | -54.4% | [-6.0198, +1.8633] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.393 0.422 0.446 0.47 0.489 0.506 0.522 0.535 0.547 0.558 0.563 0.568 0.572 0.577 0.581 0.585 0.588 0.589 0.591
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
| 0 | 6.00 | 6.00 | 614 | 619 | 4.00 | 5.00 | 0.000 | 0.500 | 0.481 | 0.615 |
| 1 | 6.00 | 6.00 | 624 | 633 | 5.50 | 7.00 | 0.000 | 0.000 | 0.744 | 0.985 |
| 2 | 6.00 | 6.00 | 618 | 623 | 6.00 | 7.00 | 0.000 | 0.000 | 0.580 | 0.744 |
| 3 | 6.00 | 6.00 | 620 | 638 | 6.00 | 7.00 | 0.000 | 0.000 | 0.673 | 1.15 |
| 4 | 6.00 | 6.00 | 633 | 652 | 8.00 | 10.00 | 0.000 | 0.000 | 0.966 | 1.50 |
| 5 | 6.00 | 6.00 | 634 | 650 | 9.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.45 |
| 6 | 6.00 | 6.00 | 635 | 648 | 9.75 | 10.00 | 0.000 | 0.000 | 1.03 | 1.38 |
| 7 | 6.00 | 6.00 | 646 | 679 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.23 |
| 8 | 6.00 | 6.00 | 645 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.12 |
| 9 | 6.00 | 6.00 | 646 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.14 |
| 10 | 6.00 | 6.00 | 645 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.02 |
| 11 | 6.00 | 6.00 | 620 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.631 | 0.713 |
| 12 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.592 | 0.784 |
| 13 | 6.00 | 6.00 | 624 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.743 | 1.07 |
| 14 | 6.00 | 6.00 | 630 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.927 | 1.42 |
| 15 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.982 | 1.42 |
| 16 | 6.00 | 6.00 | 631 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 0.928 | 1.27 |
| 17 | 6.00 | 6.00 | 626 | 637 | 10.00 | 10.00 | 0.000 | 0.000 | 0.828 | 1.13 |
| 18 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.573 | 0.766 |
| 19 | 6.00 | 6.00 | 620 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.628 | 0.772 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
