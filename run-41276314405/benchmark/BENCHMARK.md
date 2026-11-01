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
| duration (min) | 20.23 | 20.05 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.00 | -0.9% |
| power (W), mean | 629 | 641 | +2.0% |
| power (W), peak | 652 | 681 | +4.4% |
| energy (Wh) | 212 | 214 | +1.0% |
| energy, parked workers still on at idle power (Wh) | 212 | 214 | +1.0% |
| CPU used (cores), mean | 0.897 | 1.22 | +35.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.051 | +35.9% |
| energy per core-hour (Wh) | 702 | 527 | -25.0% |
| node-hours per core-hour | 6.69 | 4.93 | -26.4% |
| pending pods, pod-minutes | 0.800 | 0.533 | -33.3% |
| pending pods, peak | 3.00 | 2.00 | -33.3% |
| HPA replicas, mean | 9.00 | 9.35 | +3.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.783 | +46.9% |
| requests timed | 1,035 | 1,100 | +6.3% |
| time over the response line (% of samples) | 1.35 | 0.000 | -100.0% |
| response time (ms), mean | 163 | 95.67 | -41.3% |
| response time (ms), median | 133 | 82.50 | -37.9% |
| response time (ms), 95th percentile | 321 | 154 | -52.0% |
| response time (ms), 99th percentile | 530 | 180 | -66.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.3031 | 5.3481 | -26.8% | [-3.5342, -0.3280] | GAIN |
| kwh_per_core_hour | 0.7624 | 0.5686 | -25.4% | [-0.3516, -0.0344] | GAIN |
| utilisation | 0.0369 | 0.0517 | +40.2% | [+0.0024, +0.0285] | GAIN |
| pending_pod_minutes_per_hour | 2.2857 | 1.7067 | -25.3% | [-6.8571, +4.5410] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5178 | 2.4470 | +61.2% | [-2.2739, +4.9917] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 1.0 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.468 0.487 0.504 0.52 0.534 0.546 0.556 0.562 0.567 0.572 0.576 0.581 0.584 0.588 0.589 0.591
- nodes decided per minute: 6 6 5 5 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 616 | 620 | 6.00 | 5.00 | 0.000 | 0.000 | 0.565 | 0.680 |
| 1 | 6.00 | 6.00 | 619 | 623 | 6.00 | 6.50 | 0.000 | 0.000 | 0.617 | 0.724 |
| 2 | 6.00 | 6.00 | 618 | 626 | 6.00 | 7.00 | 0.000 | 0.500 | 0.626 | 0.811 |
| 3 | 6.00 | 6.00 | 622 | 633 | 6.00 | 9.00 | 0.750 | 0.000 | 0.696 | 0.998 |
| 4 | 6.00 | 6.00 | 634 | 642 | 9.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.26 |
| 5 | 6.00 | 6.00 | 632 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.33 |
| 6 | 6.00 | 6.00 | 633 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 0.978 | 1.33 |
| 7 | 6.00 | 6.00 | 646 | 672 | 9.50 | 10.00 | 0.000 | 0.000 | 1.35 | 2.03 |
| 8 | 6.00 | 6.00 | 649 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 2.12 |
| 9 | 6.00 | 6.00 | 646 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 2.02 |
| 10 | 6.00 | 6.00 | 646 | 666 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.89 |
| 11 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.581 | 0.757 |
| 12 | 6.00 | 6.00 | 620 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.642 | 0.803 |
| 13 | 6.00 | 6.00 | 624 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.752 | 1.08 |
| 14 | 6.00 | 6.00 | 633 | 642 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.22 |
| 15 | 6.00 | 6.00 | 634 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.35 |
| 16 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.39 |
| 17 | 6.00 | 6.00 | 627 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.846 | 1.10 |
| 18 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.621 | 0.756 |
| 19 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.594 | 0.775 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
