# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1809 | 989.8 | 1959 | 911.7 | 1775 | 894.7 | 2373 | 1636 | 1520 | 1010 | 1497 | 828.1 |
| response time (ms), 99th percentile | 4390 | 3633 | 5150 | 4335 | 4887 | 4222 | 5232 | 4730 | 3488 | 2834 | 3795 | 3200 |
| time over the response line (% of samples) | 31.4 | 16.42 | 26.38 | 12.5 | 23.49 | 11.23 | 35.84 | 18.89 | 25.26 | 13.14 | 25.57 | 13.15 |
| failed requests (%) | 10.26 | 8.817 | 7.36 | 6.547 | 6.105 | 5.283 | 9.99 | 8.452 | 6.442 | 5.689 | 7.575 | 6.688 |
| HPA replicas, mean | 9.745 | 9.764 | 9.739 | 9.775 | 9.733 | 9.729 | 9.719 | 9.722 | 9.635 | 9.56 | 9.691 | 9.678 |
| pods started | 3.61 | 3.439 | 4.244 | 3.537 | 4.024 | 4.171 | 3.537 | 3.512 | 4.366 | 4.659 | 4.146 | 4.439 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 186.8 | 186.4 | 185.2 | 184.7 | 184 | 183.7 | 187.6 | 187.2 | 183.7 | 183.3 | 184.7 | 184.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.8 | 186.4 | 185.2 | 184.7 | 184 | 183.7 | 187.6 | 187.2 | 183.7 | 183.3 | 184.7 | 184.3 |
| CPU used with Omni's own (cores), mean | 2.607 | 2.572 | 2.474 | 2.433 | 2.375 | 2.343 | 2.689 | 2.664 | 2.327 | 2.298 | 2.414 | 2.38 |
| host CPU busy, the real machine under kind (%) | 76.2 | 75.46 | 72.26 | 71.3 | 69.45 | 68.78 | 78.09 | 77.5 | 68.08 | 67.62 | 70.86 | 70.31 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0.002439 | 0 | 0 | 0 | 0 | 0 | 0.002439 | 0.009756 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1809 | 989.8 | -45.3% | -1009 to -628.8 | better |
| response time (ms), 99th percentile | 4390 | 3633 | -17.2% | -1144 to -370.2 | better |
| time over the response line (% of samples) | 31.4 | 16.42 | -47.7% | -17.44 to -12.52 | better |
| failed requests (%) | 10.26 | 8.817 | -14.0% | -1.943 to -0.9358 | better |
| HPA replicas, mean | 9.745 | 9.764 | +0.2% | -0.003688 to +0.04311 | WORSE (inside the noise) |
| pods started | 3.61 | 3.439 | -4.7% | -0.5751 to +0.2336 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.02e-16 to +1.121e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.8 | 186.4 | -0.2% | -0.6548 to -0.1153 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.8 | 186.4 | -0.2% | -0.6548 to -0.1153 | better |
| CPU used with Omni's own (cores), mean | 2.607 | 2.572 | -1.4% | -0.04938 to -0.02157 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.2 | 75.46 | -1.0% | -1.05 to -0.4363 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001007 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 8, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1959 | 911.7 | -53.5% | -1300 to -795 | better |
| response time (ms), 99th percentile | 5150 | 4335 | -15.8% | -1258 to -371.6 | better |
| time over the response line (% of samples) | 26.38 | 12.5 | -52.6% | -16.28 to -11.48 | better |
| failed requests (%) | 7.36 | 6.547 | -11.0% | -1.184 to -0.4414 | better |
| HPA replicas, mean | 9.739 | 9.775 | +0.4% | +0.004809 to +0.0681 | WORSE |
| pods started | 4.244 | 3.537 | -16.7% | -1.273 to -0.1419 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.66e-16 to +2.061e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 184.7 | -0.2% | -0.6433 to -0.2558 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 184.7 | -0.2% | -0.6433 to -0.2558 | better |
| CPU used with Omni's own (cores), mean | 2.474 | 2.433 | -1.7% | -0.05247 to -0.03085 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.26 | 71.3 | -1.3% | -1.276 to -0.6471 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1775 | 894.7 | -49.6% | -1122 to -638.2 | better |
| response time (ms), 99th percentile | 4887 | 4222 | -13.6% | -1068 to -261 | better |
| time over the response line (% of samples) | 23.49 | 11.23 | -52.2% | -14.6 to -9.923 | better |
| failed requests (%) | 6.105 | 5.283 | -13.5% | -1.124 to -0.5204 | better |
| HPA replicas, mean | 9.733 | 9.729 | -0.0% | -0.02817 to +0.02067 | better (inside the noise) |
| pods started | 4.024 | 4.171 | +3.6% | -0.2896 to +0.5823 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.723e-16 to +3.589e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.7 | -0.1% | -0.4669 to -0.05129 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.7 | -0.1% | -0.4669 to -0.05129 | better |
| CPU used with Omni's own (cores), mean | 2.375 | 2.343 | -1.3% | -0.0424 to -0.02136 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.45 | 68.78 | -1.0% | -1.006 to -0.3465 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0.002439 | 0 | -100.0% | -0.00722 to +0.002341 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2373 | 1636 | -31.1% | -947.5 to -526.8 | better |
| response time (ms), 99th percentile | 5232 | 4730 | -9.6% | -807.9 to -196.5 | better |
| time over the response line (% of samples) | 35.84 | 18.89 | -47.3% | -19.64 to -14.25 | better |
| failed requests (%) | 9.99 | 8.452 | -15.4% | -1.997 to -1.08 | better |
| HPA replicas, mean | 9.719 | 9.722 | +0.0% | -0.02644 to +0.03352 | WORSE (inside the noise) |
| pods started | 3.537 | 3.512 | -0.7% | -0.5296 to +0.4809 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.545e-16 to +3.545e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 187.6 | 187.2 | -0.2% | -0.7036 to +0.01244 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.6 | 187.2 | -0.2% | -0.7036 to +0.01244 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.689 | 2.664 | -0.9% | -0.03784 to -0.01161 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.09 | 77.5 | -0.8% | -0.9353 to -0.2563 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 8, worse on 2 (organism energy (J); organism work per energy), inside the noise on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1520 | 1010 | -33.5% | -687.9 to -331.8 | better |
| response time (ms), 99th percentile | 3488 | 2834 | -18.7% | -945.5 to -361.9 | better |
| time over the response line (% of samples) | 25.26 | 13.14 | -48.0% | -15.17 to -9.063 | better |
| failed requests (%) | 6.442 | 5.689 | -11.7% | -1.302 to -0.2047 | better |
| HPA replicas, mean | 9.635 | 9.56 | -0.8% | -0.1284 to -0.02288 | better |
| pods started | 4.366 | 4.659 | +6.7% | -0.2559 to +0.8413 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.222e-16 to +3.955e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.3 | -0.2% | -0.6861 to -0.02634 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.3 | -0.2% | -0.6861 to -0.02634 | better |
| CPU used with Omni's own (cores), mean | 2.327 | 2.298 | -1.3% | -0.04774 to -0.01052 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 68.08 | 67.62 | -0.7% | -0.9354 to +0.006932 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1497 | 828.1 | -44.7% | -814.7 to -523 | better |
| response time (ms), 99th percentile | 3795 | 3200 | -15.7% | -960.1 to -228.9 | better |
| time over the response line (% of samples) | 25.57 | 13.15 | -48.6% | -14.99 to -9.849 | better |
| failed requests (%) | 7.575 | 6.688 | -11.7% | -1.223 to -0.5522 | better |
| HPA replicas, mean | 9.691 | 9.678 | -0.1% | -0.04867 to +0.02268 | better (inside the noise) |
| pods started | 4.146 | 4.439 | +7.1% | -0.1574 to +0.7428 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.573e-16 to +3.14e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.3 | -0.2% | -0.7109 to -0.08842 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.3 | -0.2% | -0.7109 to -0.08842 | better |
| CPU used with Omni's own (cores), mean | 2.414 | 2.38 | -1.4% | -0.05206 to -0.01774 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 70.86 | 70.31 | -0.8% | -0.9812 to -0.1344 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.232e+07 to +4.232e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.274e-08 to -5.274e-08 | WORSE |
| organism behind its window (s) | 0.002439 | 0.009756 | +300.0% | -0.003265 to +0.0179 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
