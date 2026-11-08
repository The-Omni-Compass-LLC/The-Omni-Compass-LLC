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
| duration (min) | 20.15 | 20.13 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.01 | -0.1% |
| power (W), mean | 628 | 643 | +2.3% |
| power (W), peak | 651 | 681 | +4.6% |
| energy (Wh) | 211 | 216 | +2.2% |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.2% |
| CPU used (cores), mean | 0.872 | 1.26 | +44.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.052 | +44.4% |
| energy per core-hour (Wh) | 721 | 510 | -29.2% |
| node-hours per core-hour | 6.88 | 4.76 | -30.8% |
| pending pods, pod-minutes | 0.267 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.95 | 9.48 | +5.9% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.267 | 0.800 | +200.0% |
| requests timed | 1,055 | 1,095 | +3.8% |
| time over the response line (% of samples) | 0.853 | 0.000 | -100.0% |
| response time (ms), mean | 139 | 97.53 | -29.7% |
| response time (ms), median | 116 | 85.40 | -26.5% |
| response time (ms), 95th percentile | 293 | 152 | -48.1% |
| response time (ms), 99th percentile | 476 | 171 | -64.0% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.4962 | 5.2103 | -30.5% | [-3.9286, -0.6338] | GAIN |
| kwh_per_core_hour | 0.7818 | 0.5548 | -29.0% | [-0.3949, -0.0691] | GAIN |
| utilisation | 0.0359 | 0.0534 | +48.8% | [+0.0047, +0.0316] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 0.0000 | -100.0% | [-2.2857, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 0.7742 | 2.4932 | +222.0% | [-1.5484, +5.0914] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.371 0.376 0.382 0.387 0.393 0.398 0.403 0.408 0.412 0.417 0.421 0.426 0.43 0.434 0.438 0.443 0.447 0.451 0.455 0.458 0.462 0.466 0.469 0.473 0.476 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.5 0.503 0.505 0.508 0.511 0.513 0.516 0.519 0.521 0.523 0.526 0.528 0.53 0.533 0.535 0.537 0.539 0.541 0.543 0.545 0.547 0.548 0.55 0.552 0.553 0.555 0.556 0.558 0.559 0.56 0.56 0.561 0.562 0.563 0.564 0.565 0.566 0.567 0.567 0.568 0.569 0.57 0.57 0.571 0.572 0.573 0.574 0.575 0.576 0.576 0.577 0.578 0.579 0.58 0.58 0.581 0.582 0.582 0.583 0.584 0.584 0.585 0.585 0.586 0.586 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.589 0.59 0.59 0.59 0.59 0.591
- nodes decided per minute: 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 6 5 5 5 5 5 5 5 5 5 4 4 4 4 4 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 615 | 621 | 5.00 | 5.00 | 0.000 | 0.000 | 0.509 | 0.681 |
| 1 | 6.00 | 6.00 | 617 | 628 | 5.00 | 7.00 | 0.000 | 0.000 | 0.533 | 0.860 |
| 2 | 6.00 | 6.00 | 617 | 624 | 5.00 | 9.00 | 0.000 | 0.000 | 0.590 | 0.762 |
| 3 | 6.00 | 6.00 | 624 | 634 | 5.75 | 9.00 | 0.000 | 0.000 | 0.755 | 1.02 |
| 4 | 6.00 | 6.00 | 635 | 642 | 9.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.35 |
| 5 | 6.00 | 6.00 | 630 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.922 | 1.34 |
| 6 | 6.00 | 6.00 | 632 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.970 | 1.43 |
| 7 | 6.00 | 6.00 | 645 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.12 |
| 8 | 6.00 | 6.00 | 645 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.15 |
| 9 | 6.00 | 6.00 | 646 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.17 |
| 10 | 6.00 | 6.00 | 644 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 1.94 |
| 11 | 6.00 | 6.00 | 618 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.627 | 0.786 |
| 12 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.562 | 0.807 |
| 13 | 6.00 | 6.00 | 625 | 632 | 10.00 | 10.00 | 0.250 | 0.000 | 0.775 | 0.970 |
| 14 | 6.00 | 6.00 | 631 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.957 | 1.45 |
| 15 | 6.00 | 6.00 | 633 | 654 | 10.00 | 10.00 | 0.000 | 0.000 | 0.983 | 1.58 |
| 16 | 6.00 | 6.00 | 632 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.966 | 1.31 |
| 17 | 6.00 | 6.00 | 630 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.884 | 0.945 |
| 18 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.653 | 0.745 |
| 19 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.592 | 0.792 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
