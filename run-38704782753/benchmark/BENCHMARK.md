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
| duration (min) | 20.13 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.01 | -0.2% |
| power (W), mean | 629 | 635 | +0.9% |
| power (W), peak | 652 | 672 | +3.0% |
| energy (Wh) | 211 | 213 | +0.7% |
| energy, parked workers still on at idle power (Wh) | 211 | 213 | +0.7% |
| CPU used (cores), mean | 0.898 | 1.05 | +17.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.037 | 0.044 | +17.4% |
| energy per core-hour (Wh) | 701 | 602 | -14.1% |
| node-hours per core-hour | 6.68 | 5.69 | -14.8% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.11 | 9.07 | -0.4% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.800 | +50.0% |
| requests timed | 1,035 | 1,130 | +9.2% |
| time over the response line (% of samples) | 1.45 | 0.000 | -100.0% |
| response time (ms), mean | 160 | 64.77 | -59.5% |
| response time (ms), median | 130 | 57.45 | -55.7% |
| response time (ms), 95th percentile | 338 | 94.81 | -72.0% |
| response time (ms), 99th percentile | 535 | 118 | -77.9% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2898 | 6.4720 | -11.2% | [-2.5895, +0.9503] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7613 | 0.6799 | -10.7% | [-0.2498, +0.0937] | EVEN, no significant difference |
| utilisation | 0.0370 | 0.0431 | +16.6% | [-0.0048, +0.0179] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4877 | 2.2616 | +52.0% | [-2.1780, +3.7313] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.467 0.486 0.502 0.517 0.531 0.542 0.552 0.558 0.563 0.568 0.573 0.577 0.581 0.585 0.586 0.588
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
| 0 | 6.00 | 6.00 | 621 | 630 | 6.00 | 4.50 | 0.000 | 0.000 | 0.667 | 0.918 |
| 1 | 6.00 | 6.00 | 617 | 619 | 6.00 | 6.00 | 0.000 | 0.000 | 0.576 | 0.601 |
| 2 | 6.00 | 6.00 | 619 | 620 | 6.00 | 6.00 | 0.000 | 0.000 | 0.585 | 0.639 |
| 3 | 6.00 | 6.00 | 620 | 622 | 6.00 | 6.00 | 0.000 | 0.000 | 0.649 | 0.790 |
| 4 | 6.00 | 6.00 | 635 | 639 | 9.00 | 9.50 | 0.000 | 0.000 | 1.07 | 1.15 |
| 5 | 6.00 | 6.00 | 634 | 642 | 9.67 | 10.00 | 0.000 | 0.000 | 1.03 | 1.23 |
| 6 | 6.00 | 6.00 | 633 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.993 | 1.29 |
| 7 | 6.00 | 6.00 | 646 | 662 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 1.76 |
| 8 | 6.00 | 6.00 | 649 | 664 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 1.82 |
| 9 | 6.00 | 6.00 | 647 | 658 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.66 |
| 10 | 6.00 | 6.00 | 636 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.37 |
| 11 | 6.00 | 6.00 | 619 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.641 | 0.560 |
| 12 | 6.00 | 6.00 | 617 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.553 | 0.626 |
| 13 | 6.00 | 6.00 | 624 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.763 | 0.817 |
| 14 | 6.00 | 6.00 | 634 | 641 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.21 |
| 15 | 6.00 | 6.00 | 637 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 1.08 | 1.15 |
| 16 | 6.00 | 6.00 | 633 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 0.998 | 1.25 |
| 17 | 6.00 | 6.00 | 628 | 629 | 10.00 | 10.00 | 0.000 | 0.000 | 0.849 | 0.896 |
| 18 | 6.00 | 6.00 | 620 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.647 | 0.651 |
| 19 | 6.00 | 6.00 | 617 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.611 | 0.563 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
