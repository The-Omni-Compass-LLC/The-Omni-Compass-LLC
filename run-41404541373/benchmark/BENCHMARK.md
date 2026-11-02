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
| duration (min) | 20.03 | 20.17 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.02 | +0.7% |
| power (W), mean | 628 | 630 | +0.3% |
| power (W), peak | 651 | 664 | +2.1% |
| energy (Wh) | 210 | 212 | +1.0% |
| energy, parked workers still on at idle power (Wh) | 210 | 212 | +1.0% |
| CPU used (cores), mean | 0.853 | 0.902 | +5.7% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.036 | 0.038 | +5.7% |
| energy per core-hour (Wh) | 736 | 698 | -5.1% |
| node-hours per core-hour | 7.03 | 6.65 | -5.4% |
| pending pods, pod-minutes | 0.250 | 0.800 | +220.0% |
| pending pods, peak | 1.00 | 3.00 | +200.0% |
| HPA replicas, mean | 9.06 | 9.00 | -0.7% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.500 | 0.783 | +56.7% |
| requests timed | 1,070 | 1,150 | +7.5% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 126 | 46.15 | -63.5% |
| response time (ms), median | 113 | 40.70 | -63.9% |
| response time (ms), 95th percentile | 263 | 69.07 | -73.8% |
| response time (ms), 99th percentile | 376 | 82.90 | -77.9% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.7464 | 7.6437 | -1.3% | [-2.2797, +2.0645] | STEADY, no significant difference |
| kwh_per_core_hour | 0.8066 | 0.7964 | -1.3% | [-0.2154, +0.2007] | STEADY, no significant difference |
| utilisation | 0.0351 | 0.0372 | +5.9% | [-0.0084, +0.0132] | STEADY, no significant difference |
| pending_pod_minutes_per_hour | 0.7143 | 2.3040 | +222.6% | [-2.1429, +6.9120] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4343 | 2.2560 | +57.3% | [-2.1006, +3.7440] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.352 0.358 0.364 0.37 0.376 0.381 0.386 0.391 0.396 0.401 0.406 0.411 0.415 0.42 0.424 0.428 0.433 0.437 0.441 0.445 0.449 0.452 0.456 0.46 0.463 0.467 0.47 0.473 0.476 0.48 0.483 0.486 0.488 0.491 0.494 0.497 0.499 0.502 0.505 0.507 0.51 0.512 0.515 0.517 0.519 0.522 0.524 0.526 0.528 0.53 0.532 0.534 0.536 0.538 0.54 0.541 0.543 0.545 0.546 0.548 0.549 0.551 0.552 0.553 0.554 0.555 0.556 0.557 0.558 0.559 0.56 0.56 0.561 0.562 0.563 0.564 0.565 0.565 0.566 0.567 0.568 0.569 0.57 0.57 0.571 0.572 0.573 0.573 0.574 0.575 0.575 0.576 0.577 0.577 0.578 0.578 0.579 0.579 0.58 0.581 0.581 0.582 0.582 0.582 0.582 0.583 0.583 0.583 0.583 0.584 0.584 0.584 0.585 0.585 0.585 0.585
- nodes decided per minute: 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 617 | 614 | 5.25 | 4.00 | 0.000 | 0.000 | 0.553 | 0.487 |
| 1 | 6.00 | 6.00 | 616 | 615 | 6.00 | 4.50 | 0.000 | 0.000 | 0.553 | 0.521 |
| 2 | 6.00 | 6.00 | 616 | 616 | 6.00 | 6.00 | 0.000 | 0.000 | 0.550 | 0.560 |
| 3 | 6.00 | 6.00 | 620 | 622 | 6.00 | 6.75 | 0.000 | 0.000 | 0.652 | 0.673 |
| 4 | 6.00 | 6.00 | 632 | 634 | 8.50 | 9.25 | 0.250 | 0.750 | 0.967 | 1.00 |
| 5 | 6.00 | 6.00 | 632 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.953 | 0.996 |
| 6 | 6.00 | 6.00 | 633 | 642 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.22 |
| 7 | 6.00 | 6.00 | 645 | 653 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 1.53 |
| 8 | 6.00 | 6.00 | 647 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 1.37 |
| 9 | 6.00 | 6.00 | 646 | 658 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 1.66 |
| 10 | 6.00 | 6.00 | 641 | 653 | 10.00 | 10.00 | 0.000 | 0.000 | 1.22 | 1.53 |
| 11 | 6.00 | 6.00 | 616 | 615 | 10.00 | 10.00 | 0.000 | 0.000 | 0.553 | 0.517 |
| 12 | 6.00 | 6.00 | 614 | 618 | 10.00 | 10.00 | 0.000 | 0.000 | 0.489 | 0.589 |
| 13 | 6.00 | 6.00 | 620 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.626 | 0.758 |
| 14 | 6.00 | 6.00 | 632 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.951 | 0.975 |
| 15 | 6.00 | 6.00 | 632 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.950 | 1.02 |
| 16 | 6.00 | 6.00 | 632 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.969 | 0.957 |
| 17 | 6.00 | 6.00 | 624 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.755 | 0.848 |
| 18 | 6.00 | 6.00 | 618 | 613 | 10.00 | 10.00 | 0.000 | 0.000 | 0.577 | 0.455 |
| 19 | 6.00 | 6.00 | 618 | 616 | 10.00 | 10.00 | 0.000 | 0.000 | 0.603 | 0.544 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
