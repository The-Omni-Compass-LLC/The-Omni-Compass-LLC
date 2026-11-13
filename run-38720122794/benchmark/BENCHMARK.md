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
| duration (min) | 20.02 | 20.18 |  |
| worker nodes in service, mean | 6.00 | 6.00 | -0.0% |
| worker nodes in service, min | 6.00 | 6.00 | +0.0% |
| worker nodes in service, max | 6.00 | 6.00 | +0.0% |
| node-hours | 2.00 | 2.02 | +0.8% |
| power (W), mean | 628 | 642 | +2.3% |
| power (W), peak | 652 | 688 | +5.5% |
| energy (Wh) | 209 | 216 | +3.2% |
| energy, parked workers still on at idle power (Wh) | 209 | 216 | +3.2% |
| CPU used (cores), mean | 0.860 | 1.24 | +44.3% |
| CPU allocatable (cores), mean | 24.00 | 24.00 | -0.0% |
| utilisation (used / allocatable) | 0.036 | 0.052 | +44.3% |
| energy per core-hour (Wh) | 730 | 518 | -29.1% |
| node-hours per core-hour | 6.98 | 4.84 | -30.7% |
| pending pods, pod-minutes | 0.250 | 0.533 | +113.3% |
| pending pods, peak | 1.00 | 2.00 | +100.0% |
| HPA replicas, mean | 9.04 | 9.43 | +4.3% |
| HPA replicas, peak | 10.00 | 10.00 | +0.0% |
| HPA shortfall (desired > current), minutes | 0.767 | 1.07 | +39.1% |
| requests timed | 1,070 | 1,100 | +2.8% |
| time over the response line (% of samples) | 0.187 | 0.000 | -100.0% |
| response time (ms), mean | 125 | 95.08 | -24.0% |
| response time (ms), median | 111 | 81.30 | -26.9% |
| response time (ms), 95th percentile | 249 | 155 | -38.0% |
| response time (ms), 99th percentile | 385 | 180 | -53.3% |
| failed requests (%) | 0.000 | 0.000 | 0 |

## Significance (2-minute blocks: native 10, omni 10; bootstrap 95% interval)

| Metric | Native | Omni-Compass | Change | 95% CI of difference | Verdict |
|---|---:|---:|---:|---|---|
| node_hours_per_core_hour | 7.6251 | 5.3930 | -29.3% | [-3.8610, -0.6918] | GAIN |
| kwh_per_core_hour | 0.7945 | 0.5734 | -27.8% | [-0.3766, -0.0673] | GAIN |
| utilisation | 0.0354 | 0.0508 | +43.7% | [+0.0038, +0.0284] | GAIN |
| pending_pod_minutes_per_hour | 0.7200 | 1.5238 | +111.6% | [-2.1600, +4.5714] | EVEN, no significant difference |
| hpa_shortfall_minutes_per_hour | 2.2142 | 3.0537 | +37.9% | [-3.5052, +6.1309] | EVEN, no significant difference |

## What Omni-Compass did

- decisions: 20 (one per minute)
- HPA target writes: 0
- node-pool resizes: 3
- scheduling-floor adds (pending pods): 0
- power-cap pod resizes (in place): 0
- rollout actions: 0
- power cap decided per minute: 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695 0.695
- heat (thermal) per minute: 0.359 0.393 0.421 0.446 0.468 0.488 0.504 0.52 0.534 0.545 0.555 0.561 0.566 0.571 0.576 0.581 0.584 0.587 0.589 0.59
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
| 0 | 6.00 | 6.00 | 614 | 636 | 5.00 | 5.00 | 0.000 | 0.500 | 0.492 | 1.06 |
| 1 | 6.00 | 6.00 | 618 | 624 | 5.25 | 8.00 | 0.250 | 0.000 | 0.603 | 0.746 |
| 2 | 6.00 | 6.00 | 624 | 623 | 6.00 | 8.00 | 0.000 | 0.000 | 0.758 | 0.698 |
| 3 | 6.00 | 6.00 | 620 | 634 | 6.00 | 8.00 | 0.000 | 0.000 | 0.640 | 1.01 |
| 4 | 6.00 | 6.00 | 634 | 647 | 9.25 | 10.00 | 0.000 | 0.000 | 1.00 | 1.37 |
| 5 | 6.00 | 6.00 | 631 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.965 | 1.37 |
| 6 | 6.00 | 6.00 | 627 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.867 | 1.36 |
| 7 | 6.00 | 6.00 | 643 | 669 | 10.00 | 10.00 | 0.000 | 0.000 | 1.25 | 1.95 |
| 8 | 6.00 | 6.00 | 645 | 679 | 10.00 | 10.00 | 0.000 | 0.000 | 1.32 | 2.24 |
| 9 | 6.00 | 6.00 | 647 | 670 | 10.00 | 10.00 | 0.000 | 0.000 | 1.38 | 2.00 |
| 10 | 6.00 | 6.00 | 640 | 676 | 10.00 | 10.00 | 0.000 | 0.000 | 1.15 | 2.15 |
| 11 | 6.00 | 6.00 | 618 | 623 | 10.00 | 10.00 | 0.000 | 0.000 | 0.588 | 0.743 |
| 12 | 6.00 | 6.00 | 618 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.607 | 0.755 |
| 13 | 6.00 | 6.00 | 620 | 638 | 10.00 | 10.00 | 0.000 | 0.000 | 0.660 | 0.930 |
| 14 | 6.00 | 6.00 | 634 | 647 | 10.00 | 10.00 | 0.000 | 0.000 | 1.03 | 1.38 |
| 15 | 6.00 | 6.00 | 631 | 646 | 10.00 | 10.00 | 0.000 | 0.000 | 0.940 | 1.38 |
| 16 | 6.00 | 6.00 | 631 | 644 | 10.00 | 10.00 | 0.000 | 0.000 | 0.930 | 1.29 |
| 17 | 6.00 | 6.00 | 623 | 635 | 10.00 | 10.00 | 0.000 | 0.000 | 0.724 | 1.07 |
| 18 | 6.00 | 6.00 | 616 | 624 | 10.00 | 10.00 | 0.000 | 0.000 | 0.569 | 0.705 |
| 19 | 6.00 | 6.00 | 618 | 627 | 10.00 | 10.00 | 0.000 | 0.000 | 0.593 | 0.822 |

## Limits

- kind nodes are containers sharing one CI machine; timings and CPU are noisier than real servers.
- The two arms ran on two different CI machines at the same time; machine-to-machine variation is part of the noise.
- Energy is modelled from utilisation and nodes in service with the declared constants above.
