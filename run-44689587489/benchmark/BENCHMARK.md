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
| duration (min) | 20.10 | 20.10 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.01 | +0.0% |
| power (W), mean | 628 | 642 | +2.2% |
| power (W), peak | 651 | 687 | +5.5% |
| energy (Wh) | 210 | 215 | +2.2% |
| energy, parked workers still on at idle power (Wh) | 210 | 215 | +2.2% |
| CPU used (cores), mean | 0.865 | 1.22 | +41.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.051 | +41.4% |
| energy per core-hour (Wh) | 726 | 525 | -27.7% |
| node-hours per core-hour | 6.94 | 4.90 | -29.3% |
| pending pods, pod-minutes | 0.800 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.91 | 9.31 | +4.4% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.05 | 0.533 | -49.2% |
| requests timed | 1,050 | 1,095 | +4.3% |
| time over the response line (% of samples) | 1.05 | 0.000 | -100.0% |
| response time (ms), mean | 145 | 96.13 | -33.7% |
| response time (ms), median | 117 | 81.10 | -30.6% |
| response time (ms), 95th percentile | 330 | 154 | -53.5% |
| response time (ms), 99th percentile | 507 | 204 | -59.7% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.5151 | 5.4163 | -27.9% | [-3.7619, -0.3847] | GAIN |
| kwh_per_core_hour | 0.7836 | 0.5755 | -26.6% | [-0.3730, -0.0405] | GAIN |
| utilisation | 0.0356 | 0.0518 | +45.4% | [+0.0037, +0.0301] | GAIN |
| pending_pod_minutes_per_hour | 2.3040 | 0.0000 | -100.0% | [-6.9120, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.0179 | 1.6865 | -44.1% | [-6.6054, +2.6110] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.352 0.359 0.365 0.37 0.376 0.381 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.429 0.434 0.438 0.442 0.446 0.45 0.454 0.458 0.461 0.465 0.469 0.472 0.475 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.499 0.502 0.505 0.507 0.51 0.513 0.515 0.518 0.52 0.523 0.525 0.527 0.53 0.532 0.534 0.536 0.538 0.54 0.542 0.544 0.546 0.547 0.549 0.551 0.553 0.555 0.556 0.557 0.558 0.559 0.56 0.561 0.561 0.562 0.563 0.564 0.565 0.566 0.567 0.567 0.568 0.569 0.569 0.57 0.571 0.572 0.573 0.574 0.575 0.576 0.577 0.577 0.578 0.579 0.58 0.58 0.581 0.582 0.582 0.583 0.583 0.584 0.585 0.585 0.586 0.586 0.587 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.59 0.59 0.59 0.59
- nodes decided per minute: 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
- HPA target decided per minute (%): 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77

## Reset

```
restored target: 50
workers in service: 6 of 6
Omni records left after kill: none
```

## Minute by minute

| min | nodes native | nodes omni | power W native | power W omni | replicas native | replicas omni | pending native | pending omni | CPU native | CPU omni |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.00 | 6.00 | 616 | 620 | 5.00 | 6.00 | 0.000 | 0.000 | 0.526 | 0.646 |
| 1 | 6.00 | 6.00 | 618 | 622 | 5.00 | 6.75 | 0.000 | 0.000 | 0.593 | 0.710 |
| 2 | 6.00 | 6.00 | 617 | 623 | 5.75 | 7.00 | 0.000 | 0.000 | 0.589 | 0.746 |
| 3 | 6.00 | 6.00 | 623 | 630 | 6.25 | 7.00 | 0.750 | 0.000 | 0.725 | 0.915 |
| 4 | 6.00 | 6.00 | 631 | 652 | 9.00 | 10.00 | 0.000 | 0.000 | 0.926 | 1.48 |
| 5 | 6.00 | 6.00 | 633 | 644 | 9.00 | 10.00 | 0.000 | 0.000 | 0.982 | 1.30 |
| 6 | 6.00 | 6.00 | 632 | 646 | 9.00 | 10.00 | 0.000 | 0.000 | 0.994 | 1.35 |
| 7 | 6.00 | 6.00 | 643 | 675 | 9.75 | 10.00 | 0.000 | 0.000 | 1.26 | 2.10 |
| 8 | 6.00 | 6.00 | 644 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.02 |
| 9 | 6.00 | 6.00 | 645 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 1.99 |
| 10 | 6.00 | 6.00 | 637 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.12 | 1.93 |
| 11 | 6.00 | 6.00 | 618 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.590 | 0.669 |
| 12 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.588 | 0.705 |
| 13 | 6.00 | 6.00 | 622 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.656 | 0.977 |
| 14 | 6.00 | 6.00 | 634 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.47 |
| 15 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.968 | 1.40 |
| 16 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.969 | 1.33 |
| 17 | 6.00 | 6.00 | 629 | 641 | 10.00 | 10.00 | 0.000 | 0.000 | 0.882 | 1.21 |
| 18 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.617 | 0.839 |
| 19 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.620 | 0.797 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
