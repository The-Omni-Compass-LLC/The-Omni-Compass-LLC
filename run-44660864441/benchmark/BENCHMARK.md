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
| duration (min) | 20.10 | 20.17 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.3% |
| power (W), mean | 625 | 642 | +2.7% |
| power (W), peak | 651 | 684 | +5.1% |
| energy (Wh) | 209 | 216 | +3.1% |
| energy, parked workers still on at idle power (Wh) | 209 | 216 | +3.1% |
| CPU used (cores), mean | 0.786 | 1.24 | +58.4% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.033 | 0.052 | +58.4% |
| energy per core-hour (Wh) | 796 | 516 | -35.1% |
| node-hours per core-hour | 7.64 | 4.82 | -36.9% |
| pending pods, pod-minutes | 0.250 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.82 | 9.45 | +7.1% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.517 | 0.533 | +3.2% |
| requests timed | 1,130 | 1,095 | -3.1% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 66.32 | 98.30 | +48.2% |
| response time (ms), median | 44.65 | 85.30 | +91.0% |
| response time (ms), 95th percentile | 160 | 157 | -1.7% |
| response time (ms), 99th percentile | 257 | 187 | -27.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.5449 | 5.3154 | -37.8% | [-5.2159, -1.1822] | GAIN |
| kwh_per_core_hour | 0.8859 | 0.5650 | -36.2% | [-0.5223, -0.1272] | GAIN |
| utilisation | 0.0325 | 0.0527 | +62.4% | [+0.0070, +0.0349] | GAIN |
| pending_pod_minutes_per_hour | 0.7258 | 0.0000 | -100.0% | [-2.1774, +0.0000] | STEADY, no significant difference |
| hpa_shortfall_minutes_per_hour | 1.5122 | 1.6932 | +12.0% | [-3.6833, +3.3865] | STEADY, no significant difference |

## What Omni-Compass did

- decisions: 120 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 4
- power cap decided per minute: 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 1.0 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.327 0.334 0.34 0.346 0.353 0.359 0.365 0.371 0.376 0.382 0.387 0.392 0.397 0.402 0.407 0.412 0.417 0.421 0.425 0.43 0.434 0.438 0.442 0.446 0.45 0.454 0.458 0.462 0.465 0.469 0.472 0.476 0.479 0.482 0.485 0.488 0.491 0.494 0.497 0.5 0.502 0.505 0.508 0.51 0.513 0.516 0.518 0.521 0.523 0.526 0.528 0.53 0.532 0.535 0.537 0.539 0.541 0.543 0.545 0.546 0.548 0.55 0.552 0.553 0.555 0.556 0.557 0.558 0.559 0.56 0.561 0.562 0.563 0.564 0.565 0.566 0.566 0.567 0.568 0.569 0.569 0.57 0.571 0.572 0.573 0.574 0.574 0.575 0.576 0.577 0.578 0.578 0.579 0.58 0.581 0.581 0.582 0.583 0.583 0.584 0.585 0.585 0.586 0.586 0.587 0.587 0.587 0.587 0.588 0.588 0.588 0.588 0.589 0.589 0.589 0.589 0.59 0.59 0.59 0.59
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
| 0 | 6.00 | 6.00 | 613 | 621 | 5.00 | 6.00 | 0.000 | 0.000 | 0.457 | 0.679 |
| 1 | 6.00 | 6.00 | 613 | 625 | 5.00 | 7.50 | 0.000 | 0.000 | 0.463 | 0.764 |
| 2 | 6.00 | 6.00 | 614 | 626 | 5.00 | 8.00 | 0.000 | 0.000 | 0.474 | 0.825 |
| 3 | 6.00 | 6.00 | 618 | 633 | 5.00 | 8.00 | 0.250 | 0.000 | 0.570 | 0.998 |
| 4 | 6.00 | 6.00 | 631 | 646 | 7.25 | 10.00 | 0.000 | 0.000 | 0.934 | 1.36 |
| 5 | 6.00 | 6.00 | 632 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 0.964 | 1.39 |
| 6 | 6.00 | 6.00 | 635 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.40 |
| 7 | 6.00 | 6.00 | 644 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.28 | 2.02 |
| 8 | 6.00 | 6.00 | 646 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.15 |
| 9 | 6.00 | 6.00 | 638 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.15 | 2.12 |
| 10 | 6.00 | 6.00 | 639 | 671 | 10.00 | 10.00 | 0.000 | 0.000 | 1.16 | 2.00 |
| 11 | 6.00 | 6.00 | 615 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.534 | 0.720 |
| 12 | 6.00 | 6.00 | 611 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.437 | 0.796 |
| 13 | 6.00 | 6.00 | 618 | 629 | 10.00 | 10.00 | 0.000 | 0.000 | 0.606 | 0.941 |
| 14 | 6.00 | 6.00 | 627 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.847 | 1.43 |
| 15 | 6.00 | 6.00 | 630 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.907 | 1.43 |
| 16 | 6.00 | 6.00 | 628 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.844 | 1.42 |
| 17 | 6.00 | 6.00 | 625 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.801 | 1.00 |
| 18 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.580 | 0.764 |
| 19 | 6.00 | 6.00 | 614 | 627 | 9.75 | 10.00 | 0.000 | 0.000 | 0.487 | 0.805 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
