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
| duration (min) | 20.22 | 20.13 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.4% |
| power (W), mean | 628 | 638 | +1.6% |
| power (W), peak | 654 | 678 | +3.7% |
| energy (Wh) | 212 | 214 | +1.2% |
| energy, parked workers still on at idle power (Wh) | 212 | 214 | +1.2% |
| CPU used (cores), mean | 0.872 | 1.14 | +31.3% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.036 | 0.048 | +31.3% |
| energy per core-hour (Wh) | 721 | 558 | -22.6% |
| node-hours per core-hour | 6.88 | 5.24 | -23.8% |
| pending pods, pod-minutes | 0.250 | 0.500 | +100.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 8.78 | 9.30 | +5.9% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.517 | -34.0% |
| requests timed | 1,065 | 1,110 | +4.2% |
| time over the response line (% of samples) | 0.188 | 0.000 | -100.0% |
| response time (ms), mean | 129 | 83.72 | -35.2% |
| response time (ms), median | 114 | 70.70 | -38.0% |
| response time (ms), 95th percentile | 272 | 140 | -48.4% |
| response time (ms), 99th percentile | 366 | 178 | -51.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.5595 | 5.9579 | -21.2% | [-3.4535, +0.2269] | EVEN, no significant difference |
| kwh_per_core_hour | 0.7881 | 0.6287 | -20.2% | [-0.3375, +0.0181] | EVEN, no significant difference |
| utilisation | 0.0360 | 0.0470 | +30.4% | [-0.0007, +0.0236] | EVEN, no significant difference |
| pending_pod_minutes_per_hour | 0.7680 | 1.4286 | +86.0% | [-1.5897, +2.8571] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.3040 | 1.4762 | -35.9% | [-3.8400, +2.1429] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.469 0.488 0.504 0.52 0.533 0.545 0.555 0.561 0.566 0.57 0.575 0.58 0.583 0.587 0.588 0.589
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
| 0 | 6.00 | 6.00 | 617 | 620 | 5.00 | 6.00 | 0.000 | 0.000 | 0.567 | 0.638 |
| 1 | 6.00 | 6.00 | 615 | 620 | 5.00 | 6.50 | 0.000 | 0.250 | 0.526 | 0.652 |
| 2 | 6.00 | 6.00 | 617 | 621 | 5.00 | 7.00 | 0.000 | 0.000 | 0.568 | 0.694 |
| 3 | 6.00 | 6.00 | 621 | 628 | 5.00 | 7.00 | 0.250 | 0.000 | 0.632 | 0.884 |
| 4 | 6.00 | 6.00 | 636 | 645 | 8.50 | 10.00 | 0.000 | 0.000 | 1.08 | 1.29 |
| 5 | 6.00 | 6.00 | 629 | 642 | 9.00 | 10.00 | 0.000 | 0.000 | 0.901 | 1.24 |
| 6 | 6.00 | 6.00 | 635 | 640 | 9.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.18 |
| 7 | 6.00 | 6.00 | 647 | 675 | 9.67 | 10.00 | 0.000 | 0.000 | 1.36 | 2.10 |
| 8 | 6.00 | 6.00 | 647 | 663 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 1.79 |
| 9 | 6.00 | 6.00 | 647 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.96 |
| 10 | 6.00 | 6.00 | 642 | 666 | 10.00 | 10.00 | 0.000 | 0.000 | 1.25 | 1.88 |
| 11 | 6.00 | 6.00 | 617 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.549 | 0.675 |
| 12 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.551 | 0.755 |
| 13 | 6.00 | 6.00 | 626 | 628 | 10.00 | 10.00 | 0.000 | 0.250 | 0.791 | 0.899 |
| 14 | 6.00 | 6.00 | 634 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.27 |
| 15 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.36 |
| 16 | 6.00 | 6.00 | 634 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.28 |
| 17 | 6.00 | 6.00 | 626 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.817 | 1.14 |
| 18 | 6.00 | 6.00 | 618 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.596 | 0.661 |
| 19 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.569 | 0.727 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
