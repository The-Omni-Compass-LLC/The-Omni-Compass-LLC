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
| duration (min) | 20.03 | 20.07 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.01 | +0.2% |
| power (W), mean | 627 | 643 | +2.5% |
| power (W), peak | 648 | 682 | +5.3% |
| energy (Wh) | 209 | 215 | +2.6% |
| energy, parked workers still on at idle power (Wh) | 209 | 215 | +2.6% |
| CPU used (cores), mean | 0.843 | 1.25 | +48.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.035 | 0.052 | +48.4% |
| energy per core-hour (Wh) | 744 | 514 | -31.0% |
| node-hours per core-hour | 7.12 | 4.80 | -32.6% |
| pending pods, pod-minutes | 0.500 | 0.000 | -100.0% |
| pending pods, peak | 2.00 | 0.000 | -100.0% |
| HPA replicas, mean | 9.17 | 9.28 | +1.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.533 | +3.2% |
| requests timed | 1,065 | 1,100 | +3.3% |
| time over the response line (% of samples) | 0.188 | 0.000 | -100.0% |
| response time (ms), mean | 127 | 95.12 | -25.1% |
| response time (ms), median | 114 | 82.20 | -27.7% |
| response time (ms), 95th percentile | 272 | 152 | -44.1% |
| response time (ms), 99th percentile | 358 | 193 | -46.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.8563 | 5.2820 | -32.8% | [-4.2993, -0.7402] | GAIN |
| kwh_per_core_hour | 0.8174 | 0.5619 | -31.3% | [-0.4264, -0.0805] | GAIN |
| utilisation | 0.0347 | 0.0532 | +53.5% | [+0.0051, +0.0328] | GAIN |
| pending_pod_minutes_per_hour | 1.4400 | 0.0000 | -100.0% | [-4.3200, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4942 | 1.6931 | +13.3% | [-2.7895, +2.7928] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.37 0.376 0.381 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.43 0.434 0.438 0.442 0.446 0.45 0.454 0.458 0.462 0.465 0.469 0.472 0.476 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.5 0.502 0.505 0.508 0.51 0.513 0.516 0.518 0.521 0.523 0.526 0.528 0.53 0.532 0.535 0.537 0.539 0.541 0.543 0.545 0.546 0.548 0.55 0.552 0.553 0.555 0.557 0.558 0.559 0.559 0.56 0.561 0.562 0.563 0.564 0.565 0.566 0.566 0.567 0.568 0.569 0.569 0.57 0.571 0.572 0.573 0.574 0.575 0.575 0.576 0.577 0.578 0.579 0.579 0.58 0.581 0.581 0.582 0.583 0.583 0.584 0.585 0.585 0.586 0.586 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.59 0.59 0.59 0.59 0.59 0.59
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
| 0 | 6.00 | 6.00 | 617 | 619 | 7.00 | 6.00 | 0.000 | 0.000 | 0.572 | 0.621 |
| 1 | 6.00 | 6.00 | 615 | 624 | 7.00 | 6.25 | 0.000 | 0.000 | 0.524 | 0.741 |
| 2 | 6.00 | 6.00 | 616 | 625 | 7.00 | 7.00 | 0.000 | 0.000 | 0.555 | 0.802 |
| 3 | 6.00 | 6.00 | 621 | 633 | 7.00 | 7.00 | 0.000 | 0.000 | 0.664 | 1.03 |
| 4 | 6.00 | 6.00 | 634 | 649 | 8.50 | 10.00 | 0.500 | 0.000 | 0.963 | 1.43 |
| 5 | 6.00 | 6.00 | 632 | 647 | 9.00 | 10.00 | 0.000 | 0.000 | 0.965 | 1.39 |
| 6 | 6.00 | 6.00 | 630 | 646 | 9.00 | 10.00 | 0.000 | 0.000 | 0.939 | 1.37 |
| 7 | 6.00 | 6.00 | 643 | 675 | 9.25 | 10.00 | 0.000 | 0.000 | 1.28 | 2.11 |
| 8 | 6.00 | 6.00 | 645 | 677 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.14 |
| 9 | 6.00 | 6.00 | 647 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.13 |
| 10 | 6.00 | 6.00 | 636 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 2.03 |
| 11 | 6.00 | 6.00 | 621 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.626 | 0.698 |
| 12 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.537 | 0.690 |
| 13 | 6.00 | 6.00 | 620 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.660 | 1.07 |
| 14 | 6.00 | 6.00 | 631 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.953 | 1.38 |
| 15 | 6.00 | 6.00 | 631 | 653 | 10.00 | 10.00 | 0.000 | 0.000 | 0.963 | 1.52 |
| 16 | 6.00 | 6.00 | 633 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.978 | 1.46 |
| 17 | 6.00 | 6.00 | 620 | 630 | 10.00 | 10.00 | 0.000 | 0.000 | 0.666 | 0.894 |
| 18 | 6.00 | 6.00 | 616 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.561 | 0.825 |
| 19 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.551 | 0.708 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
