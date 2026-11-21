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
| duration (min) | 20.15 | 20.00 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.00 | -0.7% |
| power (W), mean | 629 | 643 | +2.2% |
| power (W), peak | 654 | 682 | +4.4% |
| energy (Wh) | 211 | 214 | +1.4% |
| energy, parked workers still on at idle power (Wh) | 211 | 214 | +1.4% |
| CPU used (cores), mean | 0.891 | 1.26 | +41.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.052 | +41.1% |
| energy per core-hour (Wh) | 706 | 511 | -27.6% |
| node-hours per core-hour | 6.73 | 4.77 | -29.1% |
| pending pods, pod-minutes | 0.267 | 0.533 | +100.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.04 | 9.19 | +1.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.800 | 1.05 | +31.3% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 0.577 | 0.000 | -100.0% |
| response time (ms), mean | 157 | 95.03 | -39.3% |
| response time (ms), median | 128 | 83.10 | -35.1% |
| response time (ms), 95th percentile | 310 | 154 | -50.2% |
| response time (ms), 99th percentile | 455 | 170 | -62.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2931 | 5.1549 | -29.3% | [-3.6043, -0.6223] | GAIN |
| kwh_per_core_hour | 0.7613 | 0.5492 | -27.9% | [-0.3544, -0.0695] | GAIN |
| utilisation | 0.0367 | 0.0534 | +45.4% | [+0.0041, +0.0306] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 1.6798 | +120.5% | [-2.2857, +5.0394] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2496 | 3.2927 | +46.4% | [-3.0115, +5.8820] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.393 0.422 0.446 0.469 0.489 0.506 0.522 0.535 0.547 0.557 0.563 0.568 0.572 0.577 0.582 0.585 0.588 0.59 0.591
- nodes decided per minute: 6 5 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 616 | 626 | 5.00 | 4.75 | 0.000 | 0.500 | 0.538 | 0.803 |
| 1 | 6.00 | 6.00 | 624 | 628 | 6.00 | 6.00 | 0.000 | 0.000 | 0.763 | 0.869 |
| 2 | 6.00 | 6.00 | 617 | 622 | 6.00 | 6.75 | 0.000 | 0.000 | 0.604 | 0.691 |
| 3 | 6.00 | 6.00 | 620 | 636 | 6.00 | 7.00 | 0.000 | 0.000 | 0.656 | 1.09 |
| 4 | 6.00 | 6.00 | 634 | 643 | 8.50 | 10.00 | 0.000 | 0.000 | 1.05 | 1.27 |
| 5 | 6.00 | 6.00 | 632 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.49 |
| 6 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.41 |
| 7 | 6.00 | 6.00 | 649 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 2.06 |
| 8 | 6.00 | 6.00 | 644 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.01 |
| 9 | 6.00 | 6.00 | 646 | 677 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.17 |
| 10 | 6.00 | 6.00 | 640 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.18 | 2.08 |
| 11 | 6.00 | 6.00 | 620 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.608 | 0.741 |
| 12 | 6.00 | 6.00 | 620 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.625 | 0.717 |
| 13 | 6.00 | 6.00 | 623 | 635 | 10.00 | 10.00 | 0.250 | 0.000 | 0.713 | 1.03 |
| 14 | 6.00 | 6.00 | 633 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.39 |
| 15 | 6.00 | 6.00 | 634 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.50 |
| 16 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.970 | 1.39 |
| 17 | 6.00 | 6.00 | 627 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.872 | 0.969 |
| 18 | 6.00 | 6.00 | 620 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.616 | 0.757 |
| 19 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.621 | 0.816 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
