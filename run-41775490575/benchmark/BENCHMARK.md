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
| duration (min) | 20.22 | 20.07 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.01 | -0.7% |
| power (W), mean | 629 | 641 | +1.9% |
| power (W), peak | 654 | 682 | +4.4% |
| energy (Wh) | 212 | 214 | +1.1% |
| energy, parked workers still on at idle power (Wh) | 212 | 214 | +1.1% |
| CPU used (cores), mean | 0.892 | 1.20 | +34.0% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.037 | 0.050 | +34.0% |
| energy per core-hour (Wh) | 705 | 536 | -23.9% |
| node-hours per core-hour | 6.73 | 5.02 | -25.4% |
| pending pods, pod-minutes | 0.267 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.96 | 9.28 | +3.5% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 1.07 | +36.2% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 1.25 | 0.000 | -100.0% |
| response time (ms), mean | 156 | 95.14 | -39.2% |
| response time (ms), median | 129 | 81.20 | -37.2% |
| response time (ms), 95th percentile | 309 | 154 | -50.0% |
| response time (ms), 99th percentile | 519 | 185 | -64.4% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.4190 | 5.4632 | -26.4% | [-3.6271, -0.2966] | GAIN |
| kwh_per_core_hour | 0.7740 | 0.5803 | -25.0% | [-0.3590, -0.0314] | GAIN |
| utilisation | 0.0367 | 0.0507 | +38.2% | [+0.0014, +0.0280] | GAIN |
| pending_pod_minutes_per_hour | 0.7559 | 0.0000 | -100.0% | [-2.2677, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2677 | 3.3729 | +48.7% | [-3.7795, +6.7192] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.371 0.376 0.382 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.43 0.434 0.438 0.442 0.446 0.45 0.454 0.458 0.462 0.465 0.469 0.472 0.476 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.499 0.502 0.505 0.508 0.51 0.513 0.516 0.518 0.521 0.523 0.525 0.528 0.53 0.532 0.534 0.537 0.539 0.541 0.542 0.544 0.546 0.548 0.55 0.551 0.553 0.554 0.556 0.557 0.558 0.559 0.56 0.561 0.562 0.562 0.563 0.564 0.565 0.566 0.566 0.567 0.568 0.569 0.57 0.57 0.571 0.572 0.573 0.574 0.575 0.575 0.576 0.577 0.578 0.578 0.579 0.58 0.58 0.581 0.582 0.582 0.583 0.584 0.584 0.585 0.585 0.586 0.586 0.587 0.587 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.59 0.59
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
| 0 | 6.00 | 6.00 | 616 | 621 | 5.00 | 5.00 | 0.000 | 0.000 | 0.557 | 0.680 |
| 1 | 6.00 | 6.00 | 616 | 625 | 5.00 | 6.75 | 0.000 | 0.000 | 0.560 | 0.792 |
| 2 | 6.00 | 6.00 | 619 | 621 | 5.00 | 7.00 | 0.000 | 0.000 | 0.605 | 0.667 |
| 3 | 6.00 | 6.00 | 623 | 633 | 5.75 | 7.50 | 0.250 | 0.000 | 0.718 | 1.01 |
| 4 | 6.00 | 6.00 | 633 | 642 | 9.25 | 10.00 | 0.000 | 0.000 | 1.00 | 1.27 |
| 5 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.32 |
| 6 | 6.00 | 6.00 | 633 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 0.985 | 1.37 |
| 7 | 6.00 | 6.00 | 649 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 2.15 |
| 8 | 6.00 | 6.00 | 648 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.39 | 2.01 |
| 9 | 6.00 | 6.00 | 647 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.41 | 1.91 |
| 10 | 6.00 | 6.00 | 642 | 660 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 1.70 |
| 11 | 6.00 | 6.00 | 621 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.674 | 0.770 |
| 12 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.625 | 0.725 |
| 13 | 6.00 | 6.00 | 626 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.824 | 0.789 |
| 14 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.989 | 1.36 |
| 15 | 6.00 | 6.00 | 634 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.32 |
| 16 | 6.00 | 6.00 | 630 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.926 | 1.39 |
| 17 | 6.00 | 6.00 | 627 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.838 | 1.12 |
| 18 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.627 | 0.689 |
| 19 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.575 | 0.795 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
