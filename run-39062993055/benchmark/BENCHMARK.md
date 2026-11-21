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
| duration (min) | 20.15 | 20.27 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.03 | +0.6% |
| power (W), mean | 631 | 642 | +1.9% |
| power (W), peak | 657 | 684 | +4.1% |
| energy (Wh) | 212 | 217 | +2.5% |
| energy, parked workers still on at idle power (Wh) | 212 | 217 | +2.5% |
| CPU used (cores), mean | 0.929 | 1.25 | +34.7% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.039 | 0.052 | +34.7% |
| energy per core-hour (Wh) | 679 | 514 | -24.3% |
| node-hours per core-hour | 6.46 | 4.80 | -25.7% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 9.16 | 9.27 | +1.2% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 1.03 | 0.517 | -50.0% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 0.577 | 0.000 | -100.0% |
| response time (ms), mean | 156 | 95.41 | -38.8% |
| response time (ms), median | 129 | 81.60 | -36.7% |
| response time (ms), 95th percentile | 316 | 154 | -51.4% |
| response time (ms), 99th percentile | 437 | 192 | -56.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 6.8980 | 5.4275 | -21.3% | [-2.9359, -0.0176] | GAIN |
| kwh_per_core_hour | 0.7224 | 0.5761 | -20.3% | [-0.2854, -0.0015] | GAIN |
| utilisation | 0.0382 | 0.0513 | +34.2% | [+0.0015, +0.0260] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 0.7559 | -0.8% | [-2.2857, +2.2677] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.9877 | 1.5178 | -49.2% | [-6.6834, +2.2797] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.421 0.446 0.469 0.488 0.505 0.521 0.535 0.547 0.557 0.563 0.568 0.572 0.578 0.581 0.585 0.588 0.59 0.59
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
| 0 | 6.00 | 6.00 | 628 | 620 | 4.25 | 5.00 | 0.000 | 0.250 | 0.855 | 0.625 |
| 1 | 6.00 | 6.00 | 626 | 631 | 6.25 | 7.00 | 0.000 | 0.000 | 0.828 | 0.949 |
| 2 | 6.00 | 6.00 | 620 | 624 | 7.00 | 7.00 | 0.000 | 0.000 | 0.640 | 0.706 |
| 3 | 6.00 | 6.00 | 625 | 641 | 7.00 | 7.00 | 0.000 | 0.000 | 0.757 | 1.21 |
| 4 | 6.00 | 6.00 | 634 | 644 | 9.25 | 10.00 | 0.000 | 0.000 | 1.03 | 1.32 |
| 5 | 6.00 | 6.00 | 636 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.37 |
| 6 | 6.00 | 6.00 | 633 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.48 |
| 7 | 6.00 | 6.00 | 647 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.33 | 2.11 |
| 8 | 6.00 | 6.00 | 645 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.31 | 2.01 |
| 9 | 6.00 | 6.00 | 647 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.11 |
| 10 | 6.00 | 6.00 | 639 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.17 | 2.06 |
| 11 | 6.00 | 6.00 | 618 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.589 | 0.798 |
| 12 | 6.00 | 6.00 | 619 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.646 | 0.775 |
| 13 | 6.00 | 6.00 | 624 | 633 | 10.00 | 10.00 | 0.250 | 0.000 | 0.778 | 1.03 |
| 14 | 6.00 | 6.00 | 634 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.00 | 1.41 |
| 15 | 6.00 | 6.00 | 634 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.34 |
| 16 | 6.00 | 6.00 | 632 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 0.976 | 1.42 |
| 17 | 6.00 | 6.00 | 629 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.902 | 1.11 |
| 18 | 6.00 | 6.00 | 620 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.632 | 0.725 |
| 19 | 6.00 | 6.00 | 620 | 620 | 10.00 | 10.00 | 0.000 | 0.000 | 0.639 | 0.687 |
| 20 |  | 6.00 |  | 627 |  | 10.00 |  | 0.000 |  | 0.811 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
