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
| duration (min) | 20.07 | 20.27 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.03 | +1.0% |
| power (W), mean | 628 | 643 | +2.5% |
| power (W), peak | 651 | 690 | +6.0% |
| energy (Wh) | 210 | 217 | +3.5% |
| energy, parked workers still on at idle power (Wh) | 210 | 217 | +3.5% |
| CPU used (cores), mean | 0.860 | 1.28 | +48.7% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.036 | 0.053 | +48.7% |
| energy per core-hour (Wh) | 731 | 503 | -31.1% |
| node-hours per core-hour | 6.98 | 4.69 | -32.7% |
| pending pods, pod-minutes | 0.267 | 0.267 | +0.0% |
| pending pods, peak | 1.00 | 1.00 | +0.0% |
| HPA replicas, mean | 8.77 | 9.35 | +6.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.767 | 1.02 | +32.6% |
| requests timed | 1,055 | 1,090 | +3.3% |
| time over the response line (% of samples) | 0.474 | 0.000 | -100.0% |
| response time (ms), mean | 142 | 104 | -26.6% |
| response time (ms), median | 116 | 92.35 | -20.2% |
| response time (ms), 95th percentile | 300 | 147 | -51.0% |
| response time (ms), 99th percentile | 449 | 211 | -52.9% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.6144 | 5.2287 | -31.3% | [-3.9833, -0.8226] | GAIN |
| kwh_per_core_hour | 0.7935 | 0.5565 | -29.9% | [-0.3891, -0.0846] | GAIN |
| utilisation | 0.0354 | 0.0525 | +48.3% | [+0.0053, +0.0304] | GAIN |
| pending_pod_minutes_per_hour | 0.7619 | 0.7559 | -0.8% | [-2.2857, +2.2617] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.1905 | 2.9291 | +33.7% | [-2.9527, +5.1324] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.393 0.421 0.446 0.469 0.488 0.505 0.52 0.534 0.546 0.556 0.562 0.567 0.572 0.577 0.581 0.585 0.588 0.59 0.591
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
| 0 | 6.00 | 6.00 | 617 | 624 | 5.00 | 5.25 | 0.000 | 0.250 | 0.569 | 0.750 |
| 1 | 6.00 | 6.00 | 616 | 628 | 5.00 | 7.00 | 0.000 | 0.000 | 0.533 | 0.880 |
| 2 | 6.00 | 6.00 | 617 | 625 | 5.00 | 7.25 | 0.000 | 0.000 | 0.543 | 0.822 |
| 3 | 6.00 | 6.00 | 624 | 640 | 5.50 | 8.00 | 0.250 | 0.000 | 0.774 | 1.17 |
| 4 | 6.00 | 6.00 | 632 | 647 | 8.00 | 10.00 | 0.000 | 0.000 | 0.976 | 1.38 |
| 5 | 6.00 | 6.00 | 633 | 652 | 9.00 | 10.00 | 0.000 | 0.000 | 0.962 | 1.51 |
| 6 | 6.00 | 6.00 | 630 | 646 | 9.00 | 10.00 | 0.000 | 0.000 | 0.941 | 1.34 |
| 7 | 6.00 | 6.00 | 645 | 673 | 9.50 | 10.00 | 0.000 | 0.000 | 1.31 | 2.10 |
| 8 | 6.00 | 6.00 | 644 | 677 | 10.00 | 10.00 | 0.000 | 0.000 | 1.27 | 2.14 |
| 9 | 6.00 | 6.00 | 648 | 674 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 2.09 |
| 10 | 6.00 | 6.00 | 638 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.10 | 1.99 |
| 11 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.584 | 0.749 |
| 12 | 6.00 | 6.00 | 617 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.581 | 0.781 |
| 13 | 6.00 | 6.00 | 622 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.708 | 1.07 |
| 14 | 6.00 | 6.00 | 635 | 648 | 10.00 | 10.00 | 0.000 | 0.000 | 1.05 | 1.40 |
| 15 | 6.00 | 6.00 | 633 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 1.02 | 1.36 |
| 16 | 6.00 | 6.00 | 629 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 0.915 | 1.36 |
| 17 | 6.00 | 6.00 | 621 | 641 | 10.00 | 10.00 | 0.000 | 0.000 | 0.674 | 1.24 |
| 18 | 6.00 | 6.00 | 616 | 630 | 10.00 | 10.00 | 0.000 | 0.000 | 0.584 | 0.888 |
| 19 | 6.00 | 6.00 | 618 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.590 | 0.832 |
| 20 |  | 6.00 |  | 622 |  | 10.00 |  | 0.000 |  | 0.698 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
