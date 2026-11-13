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
| duration (min) | 20.08 | 20.17 |  |
| worker nodes in service, mean | 6.00 | 6.00 | +0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.01 | 2.02 | +0.4% |
| power (W), mean | 625 | 641 | +2.6% |
| power (W), peak | 646 | 682 | +5.6% |
| energy (Wh) | 209 | 216 | +3.0% |
| energy, parked workers still on at idle power (Wh) | 209 | 216 | +3.0% |
| CPU used (cores), mean | 0.790 | 1.22 | +54.1% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | +0.0% |
| utilisation (used / allocatable) | 0.033 | 0.051 | +54.1% |
| energy per core-hour (Wh) | 791 | 527 | -33.4% |
| node-hours per core-hour | 7.59 | 4.93 | -35.1% |
| pending pods, pod-minutes | 0.533 | 0.000 | -100.0% |
| pending pods, peak | 1.00 | 0.000 | -100.0% |
| HPA replicas, mean | 8.59 | 9.59 | +11.6% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.800 | 0.250 | -68.8% |
| requests timed | 1,130 | 1,100 | -2.7% |
| time over the response line (% of samples) | 0.000 | 0.000 | 0 |
| response time (ms), mean | 65.50 | 93.75 | +43.1% |
| response time (ms), median | 45.00 | 79.70 | +77.1% |
| response time (ms), 95th percentile | 157 | 153 | -2.6% |
| response time (ms), 99th percentile | 244 | 193 | -21.1% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 8.3389 | 5.6191 | -32.6% | [-4.5214, -0.8190] | GAIN |
| kwh_per_core_hour | 0.8656 | 0.5955 | -31.2% | [-0.4444, -0.0878] | GAIN |
| utilisation | 0.0327 | 0.0499 | +52.5% | [+0.0050, +0.0304] | GAIN |
| pending_pod_minutes_per_hour | 1.5122 | 0.0000 | -100.0% | [-4.5366, +0.0000] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2801 | 0.7619 | -66.6% | [-3.8710, +0.7921] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.358 0.392 0.42 0.445 0.468 0.487 0.504 0.52 0.533 0.545 0.556 0.562 0.567 0.571 0.576 0.58 0.584 0.587 0.588 0.59
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
| 0 | 6.00 | 6.00 | 616 | 620 | 4.00 | 8.00 | 0.000 | 0.000 | 0.546 | 0.629 |
| 1 | 6.00 | 6.00 | 616 | 622 | 5.00 | 8.00 | 0.000 | 0.000 | 0.515 | 0.724 |
| 2 | 6.00 | 6.00 | 614 | 621 | 5.00 | 8.00 | 0.000 | 0.000 | 0.465 | 0.681 |
| 3 | 6.00 | 6.00 | 620 | 637 | 5.00 | 8.00 | 0.500 | 0.000 | 0.616 | 1.11 |
| 4 | 6.00 | 6.00 | 633 | 647 | 8.00 | 10.00 | 0.000 | 0.000 | 0.981 | 1.39 |
| 5 | 6.00 | 6.00 | 628 | 648 | 8.00 | 10.00 | 0.000 | 0.000 | 0.868 | 1.37 |
| 6 | 6.00 | 6.00 | 630 | 644 | 8.00 | 10.00 | 0.000 | 0.000 | 0.919 | 1.30 |
| 7 | 6.00 | 6.00 | 644 | 670 | 9.50 | 10.00 | 0.000 | 0.000 | 1.29 | 1.98 |
| 8 | 6.00 | 6.00 | 643 | 675 | 10.00 | 10.00 | 0.000 | 0.000 | 1.30 | 2.05 |
| 9 | 6.00 | 6.00 | 642 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.24 | 2.14 |
| 10 | 6.00 | 6.00 | 636 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.09 | 1.95 |
| 11 | 6.00 | 6.00 | 616 | 625 | 10.00 | 10.00 | 0.000 | 0.000 | 0.535 | 0.779 |
| 12 | 6.00 | 6.00 | 614 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.471 | 0.832 |
| 13 | 6.00 | 6.00 | 619 | 634 | 10.00 | 10.00 | 0.000 | 0.000 | 0.584 | 1.03 |
| 14 | 6.00 | 6.00 | 628 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.918 | 1.32 |
| 15 | 6.00 | 6.00 | 631 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.938 | 1.33 |
| 16 | 6.00 | 6.00 | 628 | 645 | 10.00 | 10.00 | 0.000 | 0.000 | 0.867 | 1.32 |
| 17 | 6.00 | 6.00 | 618 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.592 | 1.06 |
| 18 | 6.00 | 6.00 | 615 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.508 | 0.739 |
| 19 | 6.00 | 6.00 | 619 | 626 | 10.00 | 10.00 | 0.000 | 0.000 | 0.628 | 0.774 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
