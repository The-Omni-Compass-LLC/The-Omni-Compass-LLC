# The capacity test on kind: the same six machines, the load rising step by step, 10 paired repetitions

> © 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Source: GitHub Actions workflow `benchmark-reps` (`load_steps` 1 to 8, 200 s a step, 1,600 measured seconds per arm,
arms native / omni / compass, order rotated), run 37150909816, commit `422d60c`, 2026-10-03, job `aggregate` (job
111300598062, `python tools/live_reps.py reps`). Transcribed from the job's printed receipt; the run's artifact
`live-reps` (zip SHA-256 `610f44548e98e1a8d7f15918fde2ffe9a8f4e37dcb48eb5ae2cc19bddffce99e`) holds the same tables.
Design written before the run: `docs/K8S_COMPASS_PREREGISTRATION.md`, "The capacity test". Evidence class **L** (real
Kubernetes software on kind; energy is a declared model, not a meter).

**Result.** With the compass law and the verdict on top, the same six machines served **33.0 requests a second within the
line against native's 24.6: +34.1%, 95% interval of the paired difference +6.2 to +10.6 requests a second** (+25% to
+43%). Response times fell by about half at every percentile and failed requests fell 8.6%, both significant. One
measure is a LOSS clear of the noise: **pods started, 7.3 against 5.6 (+30.4%)**, with the allocation law 7.8 (+39.3%). The
mean HPA replicas are lower (−26.9%), so the extra starts are churn (pods removed between load steps and started again
on the next), not more pods held. By the one rule (no LOSS of more than 2%) the compass arm is therefore not yet
labelled GAIN; the cause and its correction are recorded in the preregistration, amendment of 2026-10-03 evening,
and the test is run again under it.

## Capacity

A run's capacity is the highest step at which no more than 5% of response samples are over the line or failed (and
every lower step held too), the first 30 s of each step left to settle. Each step adds one load generator (6 requests
a second).

| Arm | Capacity (requests a second), mean | Change against native | 95% interval of the difference (requests a second) | Repetitions |
|---|---:|---:|---:|---:|
| native | 24.6 |  |  | 10 |
| omni | 25.8 | +4.9% | -0.6 to +3.0 | 10 |
| compass | 33.0 | +34.1% | +6.2 to +10.6 | 10 |

## B: Omni-Compass on top (the allocation law) vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 2.882 | -52.0% | -3.404 to -2.832 | yes: GAIN |
| node-hours | 2.686 | 1.288 | -52.0% | -1.524 to -1.271 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 301.4 | 300.7 | -0.2% | -2.35 to +0.8926 | no |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.4 | 196.1 | -34.9% | -114.4 to -96.08 | yes: GAIN |
| response time (ms), mean | 281.1 | 233.2 | -17.0% | -91.83 to -3.902 | yes: GAIN |
| response time (ms), 95th percentile | 769.1 | 702.8 | -8.6% | -165.1 to +32.52 | no |
| response time (ms), 99th percentile | 2961 | 2987 | +0.9% | -1356 to +1407 | no |
| time over the response line (% of samples) | 13.37 | 10.14 | -24.1% | -5.423 to -1.024 | yes: GAIN |
| failed requests (%) | 3.471 | 3.32 | -4.4% | -0.6086 to +0.3051 | no |
| pending pods, pod-minutes | 0.61 | 0.4217 | -30.9% | -0.6211 to +0.2444 | no |
| utilisation (used / allocatable) | 0.08641 | 0.1733 | +100.6% | +0.0738 to +0.1001 | yes, up (shown, not judged) |
| CPU used (cores), mean | 2.074 | 1.998 | -3.7% | -0.1173 to -0.03485 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.01301 | +0.013 (native is 0) | +0.01097 to +0.01505 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.074 | 2.011 | -3.0% | -0.1027 to -0.02339 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 339.7 | 226.1 | -33.4% | -144.1 to -83.07 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.879 | 8.102 | -8.7% | -1.039 to -0.5141 | yes: GAIN |
| pods started | 5.6 | 7.8 | +39.3% | +1.388 to +3.012 | yes: power given |
| pod start wait, total (s) | 21.2 | 16.5 | -22.2% | -10.84 to +1.445 | no |
| pod start wait, mean (s) | 3.547 | 2.076 | -41.5% | -2.153 to -0.788 | yes: GAIN |

## B with the compass law: Omni-Compass on top, push and pull on the HPA target and the node pool vs native, 10 paired repetitions

| Gauge | Native | Omni | Change | 95% interval of the difference | Significant |
|---|---:|---:|---:|---:|---|
| worker nodes in service, mean | 6 | 5.431 | -9.5% | -0.858 to -0.2802 | yes: GAIN |
| node-hours | 2.686 | 2.425 | -9.7% | -0.3933 to -0.1286 | yes: GAIN |
| energy, parked workers still on at idle power (Wh, declared model) | 301.4 | 299.8 | -0.5% | -2.094 to -0.9953 | yes: GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 301.4 | 280.8 | -6.8% | -30.53 to -10.62 | yes: GAIN |
| response time (ms), mean | 281.1 | 150.5 | -46.5% | -170.9 to -90.31 | yes: GAIN |
| response time (ms), 95th percentile | 769.1 | 374.7 | -51.3% | -493.7 to -295 | yes: GAIN |
| response time (ms), 99th percentile | 2961 | 1676 | -43.4% | -2098 to -471.4 | yes: GAIN |
| time over the response line (% of samples) | 13.37 | 6.371 | -52.3% | -9.88 to -4.113 | yes: GAIN |
| failed requests (%) | 3.471 | 3.174 | -8.6% | -0.5345 to -0.05987 | yes: GAIN |
| pending pods, pod-minutes | 0.61 | 0.405 | -33.6% | -0.4845 to +0.07454 | no |
| utilisation (used / allocatable) | 0.08641 | 0.09161 | +6.0% | +0.002057 to +0.008331 | yes, up (shown, not judged) |
| CPU used (cores), mean | 2.074 | 2.009 | -3.1% | -0.08031 to -0.04968 | yes, down (shown, not judged) |
| Omni's own CPU (cores), mean | 0 | 0.00946 | +0.00946 (native is 0) | +0.008217 to +0.0107 | yes: power given |
| CPU used with Omni's own (cores), mean | 2.074 | 2.018 | -2.7% | -0.07102 to -0.04004 | yes: GAIN |
| energy per core-hour (Wh, the 25 W standby model) | 339.7 | 325.1 | -4.3% | -28.36 to -0.7399 | yes, down (shown, not judged) |
| HPA replicas, mean | 8.879 | 6.488 | -26.9% | -3.154 to -1.627 | yes: GAIN |
| pods started | 5.6 | 7.3 | +30.4% | +0.9422 to +2.458 | yes: power given |
| pod start wait, total (s) | 21.2 | 20.8 | -1.9% | -6.537 to +5.737 | no |
| pod start wait, mean (s) | 3.547 | 2.821 | -20.5% | -1.517 to +0.06589 | no |

Energy on kind is a declared model, not a meter: every worker stays powered and Ready in every arm; the first energy
row counts a parked worker at its full idle power, which is what kind does; the second counts it at a declared
standby power, which needs a node autoscaler that really removes the machine. This run has none.

---

*© 2026 Dubra Software Inc. / The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from Dubra Software Inc. / The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
