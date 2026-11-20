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
| duration (min) | 20.13 | 20.27 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.03 | +0.7% |
| power (W), mean | 626 | 643 | +2.6% |
| power (W), peak | 656 | 684 | +4.3% |
| energy (Wh) | 210 | 217 | +3.3% |
| energy, parked workers still on at idle power (Wh) | 210 | 217 | +3.3% |
| CPU used (cores), mean | 0.822 | 1.26 | +53.7% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.034 | 0.053 | +53.7% |
| energy per core-hour (Wh) | 762 | 509 | -33.3% |
| node-hours per core-hour | 7.30 | 4.75 | -34.9% |
| pending pods, pod-minutes | 0.500 | 0.800 | +60.0% |
| pending pods, peak | 1.00 | 3.00 | +200.0% |
| HPA replicas, mean | 8.84 | 9.43 | +6.7% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.02 | 0.533 | -47.5% |
| requests timed | 1,125 | 1,100 | -2.2% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 68.64 | 93.78 | +36.6% |
| response time (ms), median | 45.80 | 82.45 | +80.0% |
| response time (ms), 95th percentile | 168 | 152 | -9.7% |
| response time (ms), 99th percentile | 269 | 177 | -34.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.2232 | 5.3856 | -34.5% | [-4.8072, -0.8718] | GAIN |
| kwh_per_core_hour | 0.8540 | 0.5720 | -33.0% | [-0.4754, -0.0906] | GAIN |
| utilisation | 0.0339 | 0.0516 | +52.5% | [+0.0055, +0.0311] | GAIN |
| pending_pod_minutes_per_hour | 1.5000 | 2.2677 | +51.2% | [-4.5000, +6.8031] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.9947 | 1.4759 | -50.7% | [-5.2152, +1.5965] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.393 0.421 0.446 0.469 0.489 0.505 0.522 0.535 0.546 0.557 0.562 0.568 0.572 0.578 0.581 0.585 0.588 0.589 0.59
- nodes decided per minute: 6 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
- HPA target decided per minute (%): 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77 77

## Reset

```
restored target: 50
workers in service: 6 of 6
Omni records left after kill: none
```

## Minute by minute

| min | nodes native | nodes omni | power W native | power W omni | replicas native | replicas omni | pending native | pending omni | CPU native | CPU omni |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 6.00 | 6.00 | 617 | 619 | 4.75 | 5.00 | 0.000 | 0.750 | 0.586 | 0.600 |
| 1 | 6.00 | 6.00 | 613 | 637 | 5.00 | 8.00 | 0.000 | 0.000 | 0.459 | 1.10 |
| 2 | 6.00 | 6.00 | 616 | 623 | 5.00 | 8.00 | 0.000 | 0.000 | 0.514 | 0.739 |
| 3 | 6.00 | 6.00 | 617 | 637 | 5.00 | 8.00 | 0.500 | 0.000 | 0.574 | 1.14 |
| 4 | 6.00 | 6.00 | 631 | 652 | 7.50 | 10.00 | 0.000 | 0.000 | 0.969 | 1.47 |
| 5 | 6.00 | 6.00 | 630 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 0.927 | 1.50 |
| 6 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.42 |
| 7 | 6.00 | 6.00 | 644 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.12 |
| 8 | 6.00 | 6.00 | 645 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.06 |
| 9 | 6.00 | 6.00 | 648 | 668 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 1.93 |
| 10 | 6.00 | 6.00 | 638 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.16 | 2.11 |
| 11 | 6.00 | 6.00 | 616 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.562 | 0.728 |
| 12 | 6.00 | 6.00 | 616 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.538 | 0.790 |
| 13 | 6.00 | 6.00 | 619 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.609 | 1.13 |
| 14 | 6.00 | 6.00 | 632 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.957 | 1.42 |
| 15 | 6.00 | 6.00 | 632 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.976 | 1.32 |
| 16 | 6.00 | 6.00 | 631 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.934 | 1.42 |
| 17 | 6.00 | 6.00 | 626 | 636 | 10.00 | 10.00 | 0.000 | 0.000 | 0.801 | 1.10 |
| 18 | 6.00 | 6.00 | 615 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.511 | 0.709 |
| 19 | 6.00 | 6.00 | 615 | 619 | 10.00 | 10.00 | 0.000 | 0.000 | 0.491 | 0.637 |
| 20 |  | 6.00 |  | 628 |  | 10.00 |  | 0.000 |  | 0.857 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
