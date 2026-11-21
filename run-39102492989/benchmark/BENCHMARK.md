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
| duration (min) | 20.10 | 20.03 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.00 | -0.3% |
| power (W), mean | 630 | 642 | +2.0% |
| power (W), peak | 669 | 687 | +2.7% |
| energy (Wh) | 211 | 214 | +1.6% |
| energy, parked workers still on at idle power (Wh) | 211 | 214 | +1.6% |
| CPU used (cores), mean | 0.920 | 1.24 | +34.9% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.052 | +34.9% |
| energy per core-hour (Wh) | 684 | 517 | -24.4% |
| node-hours per core-hour | 6.52 | 4.83 | -25.8% |
| pending pods, pod-minutes | 0.533 | 0.267 | -50.0% |
| pending pods, peak | 2.00 | 1.00 | -50.0% |
| HPA replicas, mean | 9.04 | 9.28 | +2.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.800 | +2.1% |
| requests timed | 1,040 | 1,095 | +5.3% |
| time over the response line (% of samples) | 0.481 | 0.000 | -100.0% |
| response time (ms), mean | 154 | 96.26 | -37.7% |
| response time (ms), median | 130 | 82.00 | -36.7% |
| response time (ms), 95th percentile | 307 | 155 | -49.7% |
| response time (ms), 99th percentile | 432 | 202 | -53.4% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 9; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.0545 | 5.1758 | -26.6% | [-3.3578, -0.3995] | GAIN |
| kwh_per_core_hour | 0.7375 | 0.5514 | -25.2% | [-0.3264, -0.0450] | GAIN |
| utilisation | 0.0378 | 0.0530 | +40.0% | [+0.0030, +0.0284] | GAIN |
| pending_pod_minutes_per_hour | 1.5484 | 0.8466 | -45.3% | [-4.6452, +1.8379] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2143 | 2.5397 | +14.7% | [-3.4743, +4.4259] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.393 0.422 0.447 0.469 0.489 0.506 0.522 0.535 0.548 0.557 0.563 0.568 0.572 0.577 0.582 0.585 0.589 0.59 0.591
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
| 0 | 6.00 | 6.00 | 623 | 621 | 4.50 | 5.25 | 0.500 | 0.250 | 0.729 | 0.655 |
| 1 | 6.00 | 6.00 | 631 | 629 | 6.00 | 7.00 | 0.000 | 0.000 | 0.942 | 0.926 |
| 2 | 6.00 | 6.00 | 618 | 623 | 6.00 | 7.00 | 0.000 | 0.000 | 0.572 | 0.739 |
| 3 | 6.00 | 6.00 | 624 | 635 | 6.00 | 7.00 | 0.000 | 0.000 | 0.792 | 1.05 |
| 4 | 6.00 | 6.00 | 636 | 650 | 9.00 | 10.00 | 0.000 | 0.000 | 1.06 | 1.43 |
| 5 | 6.00 | 6.00 | 634 | 651 | 10.00 | 10.00 | 0.000 | 0.000 | 1.04 | 1.42 |
| 6 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.35 |
| 7 | 6.00 | 6.00 | 647 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.35 | 2.06 |
| 8 | 6.00 | 6.00 | 646 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 1.97 |
| 9 | 6.00 | 6.00 | 646 | 678 | 10.00 | 10.00 | 0.000 | 0.000 | 1.36 | 2.19 |
| 10 | 6.00 | 6.00 | 637 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.97 |
| 11 | 6.00 | 6.00 | 619 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.595 | 0.702 |
| 12 | 6.00 | 6.00 | 617 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.581 | 0.717 |
| 13 | 6.00 | 6.00 | 621 | 637 | 10.00 | 10.00 | 0.000 | 0.000 | 0.679 | 1.11 |
| 14 | 6.00 | 6.00 | 631 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.35 |
| 15 | 6.00 | 6.00 | 634 | 649 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.43 |
| 16 | 6.00 | 6.00 | 634 | 650 | 10.00 | 10.00 | 0.000 | 0.000 | 1.01 | 1.44 |
| 17 | 6.00 | 6.00 | 628 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.861 | 0.972 |
| 18 | 6.00 | 6.00 | 617 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.591 | 0.818 |
| 19 | 6.00 | 6.00 | 618 | 621 | 10.00 | 10.00 | 0.000 | 0.000 | 0.587 | 0.663 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
