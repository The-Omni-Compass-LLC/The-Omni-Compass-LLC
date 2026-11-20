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
| duration (min) | 20.03 | 20.13 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.01 | +0.5% |
| power (W), mean | 627 | 637 | +1.6% |
| power (W), peak | 648 | 675 | +4.2% |
| energy (Wh) | 209 | 214 | +2.1% |
| energy, parked workers still on at idle power (Wh) | 209 | 214 | +2.1% |
| CPU used (cores), mean | 0.836 | 1.11 | +32.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.046 | +32.4% |
| energy per core-hour (Wh) | 750 | 576 | -23.3% |
| node-hours per core-hour | 7.18 | 5.42 | -24.5% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.26 | 9.25 | -0.1% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.500 | 0.500 | +0.0% |
| requests timed | 1,065 | 1,120 | +5.2% |
| time over the response line (% of samples) | 0.376 | 0.000 | -100.0% |
| response time (ms), mean | 127 | 75.27 | -40.7% |
| response time (ms), median | 113 | 67.50 | -40.4% |
| response time (ms), 95th percentile | 256 | 106 | -58.7% |
| response time (ms), 99th percentile | 377 | 128 | -66.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.8379 | 6.2543 | -20.2% | [-3.4141, +0.2193] | STEADY, no significant difference |
| kwh_per_core_hour | 0.8157 | 0.6582 | -19.3% | [-0.3287, +0.0221] | STEADY, no significant difference |
| utilisation | 0.0345 | 0.0454 | +31.7% | [-0.0008, +0.0240] | STEADY, no significant difference |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4400 | 1.4819 | +2.9% | [-2.8381, +2.3276] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.37 0.376 0.381 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.429 0.433 0.437 0.441 0.445 0.45 0.454 0.457 0.461 0.465 0.468 0.472 0.475 0.478 0.482 0.485 0.488 0.491 0.494 0.496 0.499 0.502 0.504 0.507 0.51 0.513 0.515 0.518 0.52 0.523 0.525 0.527 0.529 0.531 0.533 0.535 0.537 0.539 0.541 0.543 0.545 0.546 0.548 0.55 0.552 0.553 0.554 0.555 0.556 0.557 0.558 0.559 0.56 0.561 0.562 0.563 0.564 0.564 0.565 0.566 0.567 0.567 0.568 0.569 0.57 0.571 0.572 0.572 0.573 0.574 0.575 0.575 0.576 0.577 0.578 0.578 0.579 0.58 0.58 0.581 0.581 0.582 0.583 0.583 0.584 0.584 0.585 0.585 0.585 0.585 0.586 0.586 0.586 0.586 0.587 0.587 0.587 0.587 0.588 0.588 0.588
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
| 0 | 6.00 | 6.00 | 618 | 620 | 5.50 | 5.00 | 0.000 | 0.000 | 0.607 | 0.627 |
| 1 | 6.00 | 6.00 | 616 | 621 | 7.00 | 6.50 | 0.000 | 0.000 | 0.526 | 0.668 |
| 2 | 6.00 | 6.00 | 615 | 622 | 7.00 | 7.00 | 0.000 | 0.000 | 0.528 | 0.726 |
| 3 | 6.00 | 6.00 | 619 | 626 | 7.00 | 7.00 | 0.000 | 0.000 | 0.625 | 0.801 |
| 4 | 6.00 | 6.00 | 634 | 648 | 9.25 | 10.00 | 0.000 | 0.000 | 0.963 | 1.39 |
| 5 | 6.00 | 6.00 | 632 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.983 | 1.29 |
| 6 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.978 | 1.39 |
| 7 | 6.00 | 6.00 | 643 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 1.99 |
| 8 | 6.00 | 6.00 | 644 | 663 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 1.79 |
| 9 | 6.00 | 6.00 | 647 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 1.87 |
| 10 | 6.00 | 6.00 | 635 | 656 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.72 |
| 11 | 6.00 | 6.00 | 617 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.565 | 0.634 |
| 12 | 6.00 | 6.00 | 619 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.615 | 0.658 |
| 13 | 6.00 | 6.00 | 620 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.653 | 0.743 |
| 14 | 6.00 | 6.00 | 632 | 643 | 10.00 | 10.00 | 0.000 | 0.000 | 1.000 | 1.25 |
| 15 | 6.00 | 6.00 | 629 | 640 | 10.00 | 10.00 | 0.000 | 0.000 | 0.904 | 1.17 |
| 16 | 6.00 | 6.00 | 630 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.925 | 1.31 |
| 17 | 6.00 | 6.00 | 621 | 629 | 10.00 | 10.00 | 0.000 | 0.000 | 0.667 | 0.918 |
| 18 | 6.00 | 6.00 | 618 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.583 | 0.678 |
| 19 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.608 | 0.696 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
