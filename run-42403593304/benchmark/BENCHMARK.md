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
| duration (min) | 20.03 | 20.23 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.02 | +1.0% |
| power (W), mean | 627 | 640 | +2.1% |
| power (W), peak | 650 | 686 | +5.5% |
| energy (Wh) | 209 | 216 | +3.1% |
| energy, parked workers still on at idle power (Wh) | 209 | 216 | +3.1% |
| CPU used (cores), mean | 0.833 | 1.18 | +42.2% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.035 | 0.049 | +42.2% |
| energy per core-hour (Wh) | 753 | 541 | -28.2% |
| node-hours per core-hour | 7.21 | 5.07 | -29.7% |
| pending pods, pod-minutes | 0.000 | 0.533 | new |
| pending pods, peak | 0.000 | 2.00 | new |
| HPA replicas, mean | 8.60 | 9.26 | +7.8% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.32 | 0.517 | -60.8% |
| requests timed | 1,100 | 1,105 | +0.5% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 94.81 | 88.30 | -6.9% |
| response time (ms), median | 84.45 | 74.70 | -11.5% |
| response time (ms), 95th percentile | 211 | 142 | -32.8% |
| response time (ms), 99th percentile | 300 | 170 | -43.2% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.9279 | 5.8445 | -26.3% | [-3.9184, -0.2051] | GAIN |
| kwh_per_core_hour | 0.8247 | 0.6178 | -25.1% | [-0.3844, -0.0237] | GAIN |
| utilisation | 0.0343 | 0.0485 | +41.5% | [+0.0020, +0.0278] | GAIN |
| pending_pod_minutes_per_hour | 0.0000 | 1.5238 | n/a | [+0.0000, +4.5714] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 3.7917 | 1.4762 | -61.1% | [-7.6608, +1.5599] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.333 0.34 0.346 0.352 0.358 0.364 0.37 0.376 0.381 0.387 0.392 0.397 0.402 0.407 0.412 0.416 0.421 0.425 0.429 0.434 0.438 0.442 0.446 0.45 0.454 0.458 0.461 0.465 0.469 0.472 0.475 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.499 0.502 0.505 0.507 0.51 0.513 0.515 0.518 0.52 0.523 0.525 0.527 0.529 0.532 0.534 0.536 0.538 0.54 0.542 0.544 0.546 0.547 0.549 0.551 0.553 0.554 0.555 0.556 0.557 0.558 0.559 0.56 0.561 0.562 0.563 0.564 0.565 0.565 0.566 0.567 0.568 0.568 0.569 0.57 0.571 0.572 0.573 0.574 0.574 0.575 0.576 0.577 0.578 0.578 0.579 0.58 0.58 0.581 0.582 0.582 0.583 0.583 0.584 0.585 0.585 0.586 0.586 0.586 0.587 0.587 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.589
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
| 0 | 6.00 | 6.00 | 616 | 615 | 4.25 | 5.00 | 0.000 | 0.000 | 0.545 | 0.509 |
| 1 | 6.00 | 6.00 | 617 | 624 | 5.00 | 6.00 | 0.000 | 0.000 | 0.531 | 0.786 |
| 2 | 6.00 | 6.00 | 615 | 621 | 5.00 | 7.00 | 0.000 | 0.000 | 0.497 | 0.687 |
| 3 | 6.00 | 6.00 | 619 | 633 | 5.00 | 7.75 | 0.000 | 0.500 | 0.600 | 0.985 |
| 4 | 6.00 | 6.00 | 629 | 648 | 6.75 | 10.00 | 0.000 | 0.000 | 0.870 | 1.39 |
| 5 | 6.00 | 6.00 | 628 | 652 | 8.00 | 10.00 | 0.000 | 0.000 | 0.891 | 1.44 |
| 6 | 6.00 | 6.00 | 633 | 642 | 9.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.22 |
| 7 | 6.00 | 6.00 | 646 | 671 | 9.67 | 10.00 | 0.000 | 0.000 | 1.35 | 2.04 |
| 8 | 6.00 | 6.00 | 642 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 2.03 |
| 9 | 6.00 | 6.00 | 645 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.15 |
| 10 | 6.00 | 6.00 | 642 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.22 | 2.03 |
| 11 | 6.00 | 6.00 | 618 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.595 | 0.668 |
| 12 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.520 | 0.729 |
| 13 | 6.00 | 6.00 | 624 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.705 | 0.947 |
| 14 | 6.00 | 6.00 | 632 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.962 | 1.34 |
| 15 | 6.00 | 6.00 | 633 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.980 | 1.31 |
| 16 | 6.00 | 6.00 | 629 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.905 | 1.37 |
| 17 | 6.00 | 6.00 | 621 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.754 | 0.948 |
| 18 | 6.00 | 6.00 | 617 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.561 | 0.705 |
| 19 | 6.00 | 6.00 | 619 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.586 | 0.682 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
