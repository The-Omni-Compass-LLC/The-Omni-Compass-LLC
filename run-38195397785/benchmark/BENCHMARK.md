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
| duration (min) | 20.25 | 20.25 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.02 | 2.02 | +0.0% |
| power (W), mean | 630 | 641 | +1.8% worse |
| power (W), peak | 652 | 680 | +4.1% worse |
| energy (Wh) | 213 | 216 | +1.8% worse |
| energy, parked workers still on at idle power (Wh) | 213 | 216 | +1.8% worse |
| CPU used (cores), mean | 0.921 | 1.22 | +32.8% better |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.038 | 0.051 | +32.8% better |
| energy per core-hour (Wh) | 684 | 524 | -23.4% better |
| node-hours per core-hour | 6.51 | 4.90 | -24.7% better |
| pending pods, pod-minutes | 0.267 | 0.000 | -100.0% better |
| pending pods, peak | 1.00 | 0.000 | -100.0% better |
| HPA replicas, mean | 9.02 | 9.38 | +4.0% worse |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.783 | 0.783 | +0.0% |
| requests timed | 1,040 | 1,100 | +5.8% |
| time over the response line (% of samples) | 0.865 | 0.000 | -100.0% better |
| response time (ms), mean | 157 | 95.40 | -39.4% better |
| response time (ms), median | 130 | 83.40 | -35.8% better |
| response time (ms), 95th percentile | 313 | 154 | -50.7% better |
| response time (ms), 99th percentile | 466 | 196 | -57.9% better |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.0639 | 5.5396 | -21.6% | [-3.1234, +0.0177] | no significant difference |
| kwh_per_core_hour | 0.7387 | 0.5874 | -20.5% | [-0.3064, +0.0010] | no significant difference |
| utilisation | 0.0379 | 0.0501 | +32.3% | [+0.0005, +0.0253] | better |
| pending_pod_minutes_per_hour | 0.7619 | 0.0000 | -100.0% | [-2.2857, +0.0000] | no significant difference |
| hpa_shortfall_minutes_per_hour | 2.1964 | 2.2135 | +0.8% | [-3.5587, +3.6805] | no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.392 0.421 0.446 0.468 0.487 0.504 0.519 0.533 0.545 0.555 0.561 0.566 0.57 0.575 0.58 0.583 0.586 0.588 0.589
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
| 0 | 6.00 | 6.00 | 618 | 622 | 5.00 | 6.00 | 0.000 | 0.000 | 0.581 | 0.683 |
| 1 | 6.00 | 6.00 | 619 | 626 | 5.00 | 7.00 | 0.250 | 0.000 | 0.623 | 0.795 |
| 2 | 6.00 | 6.00 | 627 | 623 | 6.00 | 7.00 | 0.000 | 0.000 | 0.833 | 0.753 |
| 3 | 6.00 | 6.00 | 625 | 635 | 6.00 | 8.00 | 0.000 | 0.000 | 0.818 | 1.05 |
| 4 | 6.00 | 6.00 | 635 | 645 | 9.00 | 10.00 | 0.000 | 0.000 | 1.07 | 1.34 |
| 5 | 6.00 | 6.00 | 630 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.956 | 1.32 |
| 6 | 6.00 | 6.00 | 633 | 642 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.26 |
| 7 | 6.00 | 6.00 | 644 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.29 | 2.03 |
| 8 | 6.00 | 6.00 | 647 | 673 | 10.00 | 10.00 | 0.000 | 0.000 | 1.37 | 2.10 |
| 9 | 6.00 | 6.00 | 648 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.40 | 2.13 |
| 10 | 6.00 | 6.00 | 649 | 672 | 10.00 | 10.00 | 0.000 | 0.000 | 1.43 | 2.04 |
| 11 | 6.00 | 6.00 | 621 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.649 | 0.772 |
| 12 | 6.00 | 6.00 | 619 | 622 | 10.00 | 10.00 | 0.000 | 0.000 | 0.609 | 0.745 |
| 13 | 6.00 | 6.00 | 624 | 633 | 10.00 | 10.00 | 0.000 | 0.000 | 0.783 | 1.01 |
| 14 | 6.00 | 6.00 | 634 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.995 | 1.32 |
| 15 | 6.00 | 6.00 | 634 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.38 |
| 16 | 6.00 | 6.00 | 633 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 0.998 | 1.41 |
| 17 | 6.00 | 6.00 | 630 | 631 | 10.00 | 10.00 | 0.000 | 0.000 | 0.908 | 0.955 |
| 18 | 6.00 | 6.00 | 617 | 628 | 10.00 | 10.00 | 0.000 | 0.000 | 0.606 | 0.881 |
| 19 | 6.00 | 6.00 | 619 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.600 | 0.757 |
| 20 |  | 6.00 |  | 621 |  | 10.00 |  | 0.000 |  | 0.677 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
