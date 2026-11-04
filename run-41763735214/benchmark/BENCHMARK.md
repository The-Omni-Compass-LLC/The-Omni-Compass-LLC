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
| duration (min) | 20.23 | 20.25 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.1% |
| power (W), mean | 630 | 641 | +1.7% |
| power (W), peak | 651 | 678 | +4.1% |
| energy (Wh) | 212 | 216 | +1.8% |
| energy, parked workers still on at idle power (Wh) | 212 | 216 | +1.8% |
| CPU used (cores), mean | 0.911 | 1.21 | +32.3% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.038 | 0.050 | +32.3% |
| energy per core-hour (Wh) | 691 | 531 | -23.1% |
| node-hours per core-hour | 6.59 | 4.98 | -24.4% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.31 | 9.52 | +2.3% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.533 | 0.783 | +46.9% |
| requests timed | 1,040 | 1,105 | +6.2% |
| time over the response line (% of samples) | 0.769 | 0.000 | -100.0% |
| response time (ms), mean | 158 | 90.26 | -43.0% |
| response time (ms), median | 132 | 82.20 | -37.7% |
| response time (ms), 95th percentile | 315 | 124 | -60.5% |
| response time (ms), 99th percentile | 484 | 149 | -69.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.1266 | 5.6845 | -20.2% | [-3.0190, +0.1703] | STEADY, no significant difference |
| kwh_per_core_hour | 0.7448 | 0.6018 | -19.2% | [-0.2961, +0.0187] | STEADY, no significant difference |
| utilisation | 0.0376 | 0.0494 | +31.5% | [-0.0002, +0.0251] | STEADY, no significant difference |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5299 | 2.2261 | +45.5% | [-2.3457, +4.4522] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.37 0.376 0.382 0.387 0.392 0.397 0.402 0.407 0.412 0.417 0.421 0.426 0.43 0.434 0.438 0.442 0.447 0.451 0.454 0.458 0.462 0.465 0.469 0.473 0.476 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.5 0.502 0.505 0.508 0.51 0.513 0.516 0.518 0.521 0.523 0.526 0.528 0.53 0.532 0.534 0.536 0.538 0.54 0.542 0.544 0.546 0.548 0.549 0.551 0.553 0.554 0.555 0.557 0.558 0.559 0.56 0.56 0.561 0.562 0.563 0.564 0.565 0.566 0.566 0.567 0.568 0.569 0.57 0.57 0.571 0.572 0.573 0.574 0.575 0.576 0.576 0.577 0.578 0.579 0.58 0.58 0.581 0.582 0.582 0.583 0.584 0.584 0.585 0.585 0.586 0.586 0.587 0.587 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.589 0.59 0.59
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
| 0 | 6.00 | 6.00 | 617 | 620 | 7.00 | 6.00 | 0.000 | 0.000 | 0.561 | 0.661 |
| 1 | 6.00 | 6.00 | 620 | 627 | 7.00 | 7.00 | 0.000 | 0.000 | 0.656 | 0.802 |
| 2 | 6.00 | 6.00 | 616 | 625 | 7.00 | 8.50 | 0.000 | 0.000 | 0.559 | 0.774 |
| 3 | 6.00 | 6.00 | 625 | 638 | 7.00 | 9.25 | 0.000 | 0.000 | 0.771 | 1.12 |
| 4 | 6.00 | 6.00 | 636 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.31 |
| 5 | 6.00 | 6.00 | 634 | 646 | 9.67 | 10.00 | 0.000 | 0.000 | 1.01 | 1.35 |
| 6 | 6.00 | 6.00 | 635 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.40 |
| 7 | 6.00 | 6.00 | 646 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.05 |
| 8 | 6.00 | 6.00 | 649 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.99 |
| 9 | 6.00 | 6.00 | 645 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.00 |
| 10 | 6.00 | 6.00 | 645 | 658 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 1.69 |
| 11 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.627 | 0.745 |
| 12 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.627 | 0.746 |
| 13 | 6.00 | 6.00 | 623 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.740 | 0.991 |
| 14 | 6.00 | 6.00 | 634 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.47 |
| 15 | 6.00 | 6.00 | 635 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.48 |
| 16 | 6.00 | 6.00 | 633 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.39 |
| 17 | 6.00 | 6.00 | 628 | 632 | 10.00 | 10.00 | 0.000 | 0.000 | 0.897 | 0.976 |
| 18 | 6.00 | 6.00 | 617 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.562 | 0.677 |
| 19 | 6.00 | 6.00 | 621 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.705 | 0.728 |
| 20 |  | 6.00 |  | 624 |  | 10.00 |  | 0.000 |  | 0.746 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
