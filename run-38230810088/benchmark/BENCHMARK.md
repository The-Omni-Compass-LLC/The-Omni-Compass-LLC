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
| duration (min) | 20.18 | 20.15 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | -0.2% better |
| power (W), mean | 626 | 644 | +2.8% worse |
| power (W), peak | 650 | 684 | +5.3% worse |
| energy (Wh) | 211 | 216 | +2.7% worse |
| energy, parked workers still on at idle power (Wh) | 211 | 216 | +2.7% worse |
| CPU used (cores), mean | 0.802 | 1.28 | +60.1% better |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.033 | 0.053 | +60.1% better |
| energy per core-hour (Wh) | 781 | 502 | -35.8% better |
| node-hours per core-hour | 7.48 | 4.68 | -37.5% better |
| pending pods, pod-minutes | 0.533 | 0.267 | -50.0% better |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 8.75 | 9.48 | +8.3% worse |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.533 | -31.9% better |
| requests timed | 1,125 | 1,090 | -3.1% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 67.94 | 105 | +54.1% worse |
| response time (ms), median | 45.30 | 89.85 | +98.3% worse |
| response time (ms), 95th percentile | 170 | 172 | +1.0% worse |
| response time (ms), 99th percentile | 252 | 218 | -13.5% better |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.2548 | 5.1533 | -37.6% | [-4.9713, -1.2315] | better |
| kwh_per_core_hour | 0.8574 | 0.5490 | -36.0% | [-0.4936, -0.1280] | better |
| utilisation | 0.0331 | 0.0543 | +64.0% | [+0.0079, +0.0359] | better |
| pending_pod_minutes_per_hour | 1.5122 | 0.8399 | -44.5% | [-4.5366, +1.8642] | no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2322 | 1.6798 | -24.7% | [-3.5536, +2.5791] | no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.469 0.488 0.505 0.521 0.535 0.547 0.557 0.562 0.568 0.572 0.577 0.582 0.586 0.588 0.589 0.591
- nodes decided per minute: 6 5 4 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
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
| 0 | 6.00 | 6.00 | 614 | 619 | 5.00 | 6.00 | 0.000 | 0.250 | 0.475 | 0.635 |
| 1 | 6.00 | 6.00 | 616 | 626 | 5.00 | 8.00 | 0.000 | 0.000 | 0.520 | 0.817 |
| 2 | 6.00 | 6.00 | 614 | 627 | 5.00 | 8.00 | 0.000 | 0.000 | 0.478 | 0.831 |
| 3 | 6.00 | 6.00 | 617 | 642 | 5.00 | 8.00 | 0.500 | 0.000 | 0.548 | 1.23 |
| 4 | 6.00 | 6.00 | 632 | 648 | 8.00 | 10.00 | 0.000 | 0.000 | 0.950 | 1.41 |
| 5 | 6.00 | 6.00 | 629 | 648 | 9.00 | 10.00 | 0.000 | 0.000 | 0.859 | 1.42 |
| 6 | 6.00 | 6.00 | 632 | 652 | 9.00 | 10.00 | 0.000 | 0.000 | 0.963 | 1.50 |
| 7 | 6.00 | 6.00 | 641 | 680 | 9.33 | 10.00 | 0.000 | 0.000 | 1.22 | 2.25 |
| 8 | 6.00 | 6.00 | 643 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.26 | 2.10 |
| 9 | 6.00 | 6.00 | 644 | 677 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.14 |
| 10 | 6.00 | 6.00 | 642 | 664 | 10.00 | 10.00 | 0.000 | 0.000 | 1.22 | 1.85 |
| 11 | 6.00 | 6.00 | 615 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.491 | 0.743 |
| 12 | 6.00 | 6.00 | 617 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.579 | 0.774 |
| 13 | 6.00 | 6.00 | 624 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.724 | 0.980 |
| 14 | 6.00 | 6.00 | 632 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 0.932 | 1.49 |
| 15 | 6.00 | 6.00 | 630 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.915 | 1.38 |
| 16 | 6.00 | 6.00 | 631 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 0.920 | 1.46 |
| 17 | 6.00 | 6.00 | 621 | 641 | 10.00 | 10.00 | 0.000 | 0.000 | 0.706 | 1.20 |
| 18 | 6.00 | 6.00 | 615 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.525 | 0.678 |
| 19 | 6.00 | 6.00 | 617 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.575 | 0.841 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
