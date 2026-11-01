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
| power (W), mean | 629 | 642 | +2.0% |
| power (W), peak | 652 | 684 | +4.8% |
| energy (Wh) | 212 | 214 | +0.9% |
| energy, parked workers still on at idle power (Wh) | 212 | 214 | +0.9% |
| CPU used (cores), mean | 0.902 | 1.25 | +38.3% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.052 | +38.3% |
| energy per core-hour (Wh) | 698 | 515 | -26.3% |
| node-hours per core-hour | 6.65 | 4.81 | -27.7% |
| pending pods, pod-minutes | 0.800 | 0.000 | -100.0% |
| pending pods, peak | 3.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.07 | 9.60 | +5.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 1.02 | +96.8% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 0.962 | 0.000 | -100.0% |
| response time (ms), mean | 157 | 96.35 | -38.6% |
| response time (ms), median | 130 | 83.30 | -36.0% |
| response time (ms), 95th percentile | 312 | 153 | -50.8% |
| response time (ms), 99th percentile | 487 | 192 | -60.6% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.3220 | 5.2687 | -28.0% | [-3.6960, -0.3505] | GAIN |
| kwh_per_core_hour | 0.7643 | 0.5603 | -26.7% | [-0.3690, -0.0384] | GAIN |
| utilisation | 0.0371 | 0.0528 | +42.3% | [+0.0028, +0.0296] | GAIN |
| pending_pod_minutes_per_hour | 2.2857 | 0.0000 | -100.0% | [-6.8571, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4762 | 3.2738 | +121.8% | [-2.9524, +7.3016] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.469 0.488 0.505 0.52 0.535 0.546 0.556 0.561 0.567 0.571 0.576 0.581 0.585 0.588 0.59 0.591
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
| 0 | 6.00 | 6.00 | 617 | 622 | 5.00 | 5.25 | 0.000 | 0.000 | 0.562 | 0.713 |
| 1 | 6.00 | 6.00 | 618 | 622 | 5.00 | 9.00 | 0.000 | 0.000 | 0.594 | 0.715 |
| 2 | 6.00 | 6.00 | 621 | 623 | 5.00 | 9.00 | 0.000 | 0.000 | 0.661 | 0.748 |
| 3 | 6.00 | 6.00 | 624 | 632 | 7.00 | 9.00 | 0.750 | 0.000 | 0.793 | 0.966 |
| 4 | 6.00 | 6.00 | 633 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.986 | 1.47 |
| 5 | 6.00 | 6.00 | 636 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 1.45 |
| 6 | 6.00 | 6.00 | 635 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.40 |
| 7 | 6.00 | 6.00 | 649 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 1.99 |
| 8 | 6.00 | 6.00 | 648 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.42 | 2.11 |
| 9 | 6.00 | 6.00 | 648 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.92 |
| 10 | 6.00 | 6.00 | 640 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.17 | 1.86 |
| 11 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.579 | 0.778 |
| 12 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.585 | 0.711 |
| 13 | 6.00 | 6.00 | 626 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.796 | 1.13 |
| 14 | 6.00 | 6.00 | 635 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.41 |
| 15 | 6.00 | 6.00 | 636 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.07 | 1.44 |
| 16 | 6.00 | 6.00 | 633 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.48 |
| 17 | 6.00 | 6.00 | 625 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.804 | 1.17 |
| 18 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.647 | 0.717 |
| 19 | 6.00 | 6.00 | 616 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.586 | 0.846 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
