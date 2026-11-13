# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1663 | 1031 | 1847 | 935.4 | 1550 | 822.8 | 2459 | 1518 | 1916 | 1160 | 1834 | 929.8 |
| response time (ms), 99th percentile | 4582 | 3733 | 5105 | 4566 | 4581 | 4119 | 5248 | 4167 | 4455 | 3368 | 4590 | 3539 |
| time over the response line (% of samples) | 31.74 | 16.54 | 26.95 | 12.83 | 24.04 | 11.37 | 34.16 | 17.58 | 29.5 | 14.61 | 30.57 | 17.04 |
| failed requests (%) | 10.24 | 8.948 | 7.943 | 6.448 | 6.628 | 5.863 | 9.32 | 7.809 | 7.594 | 6.299 | 10.83 | 9.603 |
| HPA replicas, mean | 9.736 | 9.744 | 9.77 | 9.775 | 9.734 | 9.769 | 9.696 | 9.717 | 9.699 | 9.655 | 9.713 | 9.69 |
| pods started | 3.854 | 3.61 | 3.585 | 3.61 | 4.122 | 3.659 | 3.775 | 3.5 | 3.912 | 4.353 | 3.949 | 4.053 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 186.9 | 186.5 | 185.4 | 184.8 | 184.5 | 184.1 | 187.3 | 186.6 | 186.3 | 185 | 186.4 | 186.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.9 | 186.5 | 185.4 | 184.8 | 184.5 | 184.1 | 187.3 | 186.6 | 186.3 | 185 | 186.4 | 186.1 |
| CPU used with Omni's own (cores), mean | 2.605 | 2.581 | 2.484 | 2.428 | 2.412 | 2.376 | 2.655 | 2.58 | 2.536 | 2.446 | 2.56 | 2.527 |
| host CPU busy, the real machine under kind (%) | 76.12 | 75.68 | 72.53 | 71.1 | 70.55 | 69.76 | 77.08 | 75.35 | 73.93 | 71.81 | 74.84 | 74.23 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0.0025 | 0 | 0.002941 | 0.002941 | 0 | 0.01316 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1663 | 1031 | -38.0% | -826.3 to -435.8 | better |
| response time (ms), 99th percentile | 4582 | 3733 | -18.5% | -1327 to -371.4 | better |
| time over the response line (% of samples) | 31.74 | 16.54 | -47.9% | -17.98 to -12.41 | better |
| failed requests (%) | 10.24 | 8.948 | -12.6% | -1.985 to -0.6011 | better |
| HPA replicas, mean | 9.736 | 9.744 | +0.1% | -0.02676 to +0.04298 | WORSE (inside the noise) |
| pods started | 3.854 | 3.61 | -6.3% | -0.7862 to +0.2984 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.496e-16 to +4.962e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.9 | 186.5 | -0.2% | -0.6169 to -0.1038 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.9 | 186.5 | -0.2% | -0.6169 to -0.1038 | better |
| CPU used with Omni's own (cores), mean | 2.605 | 2.581 | -0.9% | -0.04224 to -0.007166 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.12 | 75.68 | -0.6% | -0.8914 to +0.01253 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001007 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1847 | 935.4 | -49.3% | -1123 to -699.7 | better |
| response time (ms), 99th percentile | 5105 | 4566 | -10.6% | -943 to -134.6 | better |
| time over the response line (% of samples) | 26.95 | 12.83 | -52.4% | -16.69 to -11.54 | better |
| failed requests (%) | 7.943 | 6.448 | -18.8% | -2.047 to -0.9428 | better |
| HPA replicas, mean | 9.77 | 9.775 | +0.0% | -0.01993 to +0.02923 | WORSE (inside the noise) |
| pods started | 3.585 | 3.61 | +0.7% | -0.4473 to +0.4961 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.605e-16 to +2.006e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 184.8 | -0.3% | -0.9401 to -0.2679 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 184.8 | -0.3% | -0.9401 to -0.2679 | better |
| CPU used with Omni's own (cores), mean | 2.484 | 2.428 | -2.3% | -0.07683 to -0.03519 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.53 | 71.1 | -2.0% | -2.021 to -0.8284 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 8, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1550 | 822.8 | -46.9% | -935.8 to -518.3 | better |
| response time (ms), 99th percentile | 4581 | 4119 | -10.1% | -911.9 to -12.26 | better |
| time over the response line (% of samples) | 24.04 | 11.37 | -52.7% | -15.01 to -10.33 | better |
| failed requests (%) | 6.628 | 5.863 | -11.5% | -1.177 to -0.3524 | better |
| HPA replicas, mean | 9.734 | 9.769 | +0.4% | +0.01299 to +0.05768 | WORSE |
| pods started | 4.122 | 3.659 | -11.2% | -0.8572 to -0.06964 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.417e-16 to +3.551e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.1 | -0.2% | -0.6449 to -0.2106 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.1 | -0.2% | -0.6449 to -0.2106 | better |
| CPU used with Omni's own (cores), mean | 2.412 | 2.376 | -1.5% | -0.04923 to -0.02305 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 70.55 | 69.76 | -1.1% | -1.109 to -0.4815 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 3

39 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2435 | 1555 | -36.2% | -1127 to -634.4 | better |
| response time (ms), 99th percentile | 5194 | 4271 | -17.8% | -1285 to -561.2 | better |
| time over the response line (% of samples) | 33.65 | 18.03 | -46.4% | -18.54 to -12.71 | better |
| failed requests (%) | 9.151 | 8.01 | -12.5% | -1.612 to -0.6702 | better |
| HPA replicas, mean | 9.693 | 9.732 | +0.4% | +0.004274 to +0.07257 | WORSE |
| pods started | 3.795 | 3.385 | -10.8% | -0.9525 to +0.132 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.358e-16 to +1.803e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.2 | 187 | -0.1% | -0.4243 to +0.02539 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.2 | 187 | -0.1% | -0.4243 to +0.02539 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.64 | 2.615 | -1.0% | -0.03812 to -0.01361 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.71 | 76.3 | -0.5% | -0.7425 to -0.07507 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0.002564 | 0 | -100.0% | -0.00759 to +0.002462 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

33 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1877 | 1192 | -36.5% | -872.6 to -497.2 | better |
| response time (ms), 99th percentile | 4413 | 3465 | -21.5% | -1329 to -565.2 | better |
| time over the response line (% of samples) | 28.98 | 15.05 | -48.1% | -16.6 to -11.24 | better |
| failed requests (%) | 7.347 | 6.49 | -11.7% | -1.433 to -0.2816 | better |
| HPA replicas, mean | 9.692 | 9.669 | -0.2% | -0.0649 to +0.01901 | better (inside the noise) |
| pods started | 4 | 4.273 | +6.8% | -0.1561 to +0.7015 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.035e-16 to +5.803e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.4 | -0.3% | -0.98 to -0.2608 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.4 | -0.3% | -0.98 to -0.2608 | better |
| CPU used with Omni's own (cores), mean | 2.516 | 2.481 | -1.4% | -0.05563 to -0.01475 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.4 | 72.75 | -0.9% | -1.169 to -0.121 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0.00303 | 0.00303 | +0.0% | -0.00853 to +0.00853 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

37 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1780 | 911.1 | -48.8% | -1098 to -638.4 | better |
| response time (ms), 99th percentile | 4415 | 3444 | -22.0% | -1397 to -545.2 | better |
| time over the response line (% of samples) | 29.91 | 16.72 | -44.1% | -15.95 to -10.42 | better |
| failed requests (%) | 10.68 | 9.419 | -11.8% | -1.912 to -0.6069 | better |
| HPA replicas, mean | 9.701 | 9.685 | -0.2% | -0.06069 to +0.02735 | better (inside the noise) |
| pods started | 4.081 | 4.108 | +0.7% | -0.5179 to +0.572 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.029e-16 to +3.509e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.1 | 185.9 | -0.1% | -0.5198 to +0.1648 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.1 | 185.9 | -0.1% | -0.5198 to +0.1648 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.535 | 2.51 | -1.0% | -0.03882 to -0.01032 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.13 | 73.78 | -0.5% | -0.7217 to +0.01828 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.232e+07 to +4.232e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.274e-08 to -5.274e-08 | WORSE |
| organism behind its window (s) | 0 | 0.01081 | +0.0108 | +0.0006673 to +0.02095 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
