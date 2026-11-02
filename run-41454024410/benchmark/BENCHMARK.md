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
| duration (min) | 20.23 | 20.05 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.00 | -0.9% |
| power (W), mean | 628 | 641 | +2.0% |
| power (W), peak | 651 | 686 | +5.3% |
| energy (Wh) | 212 | 214 | +1.1% |
| energy, parked workers still on at idle power (Wh) | 212 | 214 | +1.1% |
| CPU used (cores), mean | 0.874 | 1.21 | +38.8% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.036 | 0.051 | +38.8% |
| energy per core-hour (Wh) | 719 | 529 | -26.5% |
| node-hours per core-hour | 6.87 | 4.95 | -28.0% |
| pending pods, pod-minutes | 0.000 | 0.000 | 0 |
| pending pods, peak | 0.000 | 0.000 | 0 |
| HPA replicas, mean | 8.89 | 9.26 | +4.1% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.500 | 0.783 | +56.7% |
| requests timed | 1,035 | 1,100 | +6.3% |
| time over the response line (% of samples) | 0.773 | 0.000 | -100.0% |
| response time (ms), mean | 161 | 94.85 | -41.1% |
| response time (ms), median | 132 | 80.95 | -38.4% |
| response time (ms), 95th percentile | 325 | 154 | -52.7% |
| response time (ms), 99th percentile | 495 | 191 | -61.5% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.4803 | 5.5020 | -26.4% | [-3.6701, -0.2150] | GAIN |
| kwh_per_core_hour | 0.7802 | 0.5838 | -25.2% | [-0.3602, -0.0255] | GAIN |
| utilisation | 0.0360 | 0.0514 | +43.0% | [+0.0023, +0.0302] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 0.0000 | n/a | [+0.0000, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.4819 | 2.4734 | +66.9% | [-2.2228, +5.0711] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.353 0.359 0.365 0.37 0.376 0.381 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.429 0.434 0.438 0.442 0.446 0.45 0.454 0.458 0.462 0.465 0.469 0.472 0.476 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.5 0.502 0.505 0.508 0.51 0.513 0.516 0.518 0.521 0.523 0.525 0.528 0.53 0.532 0.534 0.537 0.539 0.541 0.542 0.544 0.546 0.548 0.55 0.552 0.553 0.555 0.556 0.557 0.558 0.559 0.56 0.561 0.562 0.563 0.564 0.564 0.565 0.566 0.567 0.568 0.568 0.569 0.57 0.571 0.572 0.572 0.573 0.574 0.575 0.576 0.576 0.577 0.578 0.579 0.579 0.58 0.581 0.582 0.582 0.583 0.583 0.584 0.585 0.585 0.586 0.586 0.586 0.587 0.587 0.587 0.588 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.59 0.59
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
| 0 | 6.00 | 6.00 | 618 | 618 | 5.00 | 5.00 | 0.000 | 0.000 | 0.576 | 0.597 |
| 1 | 6.00 | 6.00 | 619 | 622 | 5.00 | 6.50 | 0.000 | 0.000 | 0.621 | 0.722 |
| 2 | 6.00 | 6.00 | 618 | 624 | 5.00 | 7.00 | 0.000 | 0.000 | 0.580 | 0.747 |
| 3 | 6.00 | 6.00 | 622 | 630 | 5.75 | 7.25 | 0.000 | 0.000 | 0.698 | 0.938 |
| 4 | 6.00 | 6.00 | 632 | 651 | 9.00 | 10.00 | 0.000 | 0.000 | 0.999 | 1.39 |
| 5 | 6.00 | 6.00 | 634 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 0.998 | 1.34 |
| 6 | 6.00 | 6.00 | 633 | 650 | 9.50 | 10.00 | 0.000 | 0.000 | 1.01 | 1.45 |
| 7 | 6.00 | 6.00 | 646 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.03 |
| 8 | 6.00 | 6.00 | 646 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.06 |
| 9 | 6.00 | 6.00 | 646 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.34 | 2.19 |
| 10 | 6.00 | 6.00 | 640 | 666 | 10.00 | 10.00 | 0.000 | 0.000 | 1.19 | 1.88 |
| 11 | 6.00 | 6.00 | 616 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.587 | 0.716 |
| 12 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.618 | 0.770 |
| 13 | 6.00 | 6.00 | 624 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.776 | 0.996 |
| 14 | 6.00 | 6.00 | 631 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.954 | 1.27 |
| 15 | 6.00 | 6.00 | 632 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.964 | 1.32 |
| 16 | 6.00 | 6.00 | 633 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.983 | 1.40 |
| 17 | 6.00 | 6.00 | 628 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.863 | 1.06 |
| 18 | 6.00 | 6.00 | 620 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.634 | 0.703 |
| 19 | 6.00 | 6.00 | 617 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.580 | 0.808 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
