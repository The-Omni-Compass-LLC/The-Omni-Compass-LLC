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
| duration (min) | 20.22 | 20.20 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | -0.1% |
| power (W), mean | 630 | 643 | +2.1% |
| power (W), peak | 652 | 684 | +4.8% |
| energy (Wh) | 212 | 216 | +2.0% |
| energy, parked workers still on at idle power (Wh) | 212 | 216 | +2.0% |
| CPU used (cores), mean | 0.916 | 1.26 | +38.0% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.053 | +38.0% |
| energy per core-hour (Wh) | 688 | 509 | -26.1% |
| node-hours per core-hour | 6.55 | 4.75 | -27.6% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 9.19 | 9.27 | +0.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.800 | 0.533 | -33.3% |
| requests timed | 1,025 | 1,095 | +6.8% |
| time over the response line (% of samples) | 0.683 | 0.000 | -100.0% |
| response time (ms), mean | 171 | 97.28 | -43.2% |
| response time (ms), median | 140 | 83.90 | -40.3% |
| response time (ms), 95th percentile | 363 | 158 | -56.5% |
| response time (ms), 99th percentile | 490 | 200 | -59.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.2465 | 5.2281 | -27.9% | [-3.6940, -0.2665] | GAIN |
| kwh_per_core_hour | 0.7569 | 0.5565 | -26.5% | [-0.3673, -0.0323] | GAIN |
| utilisation | 0.0376 | 0.0536 | +42.8% | [+0.0027, +0.0306] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2918 | 1.6798 | -26.7% | [-3.7437, +2.5977] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.37 0.376 0.381 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.43 0.434 0.438 0.442 0.446 0.45 0.455 0.458 0.462 0.466 0.469 0.473 0.476 0.479 0.482 0.486 0.489 0.492 0.495 0.497 0.5 0.503 0.506 0.508 0.511 0.514 0.516 0.519 0.521 0.524 0.526 0.529 0.531 0.533 0.535 0.537 0.539 0.541 0.543 0.545 0.547 0.549 0.551 0.552 0.554 0.556 0.557 0.558 0.559 0.56 0.561 0.562 0.563 0.563 0.564 0.565 0.566 0.567 0.568 0.568 0.569 0.57 0.571 0.571 0.572 0.573 0.574 0.575 0.576 0.576 0.577 0.578 0.579 0.58 0.58 0.581 0.582 0.582 0.583 0.584 0.584 0.585 0.586 0.586 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.59 0.59 0.59 0.59 0.59 0.591 0.591
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
| 0 | 6.00 | 6.00 | 617 | 620 | 5.00 | 5.00 | 0.000 | 0.000 | 0.594 | 0.654 |
| 1 | 6.00 | 6.00 | 620 | 623 | 6.50 | 7.00 | 0.000 | 0.000 | 0.645 | 0.728 |
| 2 | 6.00 | 6.00 | 619 | 626 | 7.00 | 7.00 | 0.000 | 0.000 | 0.603 | 0.807 |
| 3 | 6.00 | 6.00 | 624 | 636 | 7.00 | 7.00 | 0.000 | 0.000 | 0.771 | 1.06 |
| 4 | 6.00 | 6.00 | 636 | 652 | 9.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.51 |
| 5 | 6.00 | 6.00 | 634 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.37 |
| 6 | 6.00 | 6.00 | 635 | 652 | 10.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.50 |
| 7 | 6.00 | 6.00 | 648 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 2.06 |
| 8 | 6.00 | 6.00 | 649 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.43 | 2.11 |
| 9 | 6.00 | 6.00 | 647 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 2.20 |
| 10 | 6.00 | 6.00 | 642 | 665 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 1.86 |
| 11 | 6.00 | 6.00 | 622 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.693 | 0.765 |
| 12 | 6.00 | 6.00 | 620 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.629 | 0.784 |
| 13 | 6.00 | 6.00 | 624 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.761 | 1.02 |
| 14 | 6.00 | 6.00 | 635 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.36 |
| 15 | 6.00 | 6.00 | 636 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.11 | 1.45 |
| 16 | 6.00 | 6.00 | 638 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.13 | 1.53 |
| 17 | 6.00 | 6.00 | 626 | 639 | 10.00 | 10.00 | 0.000 | 0.000 | 0.791 | 1.13 |
| 18 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.576 | 0.746 |
| 19 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.577 | 0.774 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
