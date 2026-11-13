# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1638 | 940.6 | 2039 | 1059 | 1762 | 1051 | 2389 | 1661 | 2401 | 1429 | 1649 | 1113 |
| response time (ms), 99th percentile | 4082 | 3212 | 5298 | 4780 | 5298 | 5074 | 4974 | 4755 | 5468 | 4416 | 4542 | 3790 |
| time over the response line (% of samples) | 28.32 | 15.24 | 28.65 | 14.45 | 27.33 | 13.23 | 34.87 | 18.5 | 38.2 | 20.76 | 31.77 | 16.81 |
| failed requests (%) | 9.81 | 8.319 | 8.61 | 7.674 | 7.593 | 6.494 | 9.838 | 8.395 | 10.75 | 9.484 | 10.62 | 9.183 |
| HPA replicas, mean | 9.699 | 9.677 | 9.75 | 9.79 | 9.787 | 9.809 | 9.702 | 9.72 | 9.765 | 9.737 | 9.741 | 9.768 |
| pods started | 4.081 | 4.297 | 4.053 | 3.564 | 3.5 | 3.098 | 3.763 | 3.579 | 3.195 | 3.293 | 3.75 | 3.528 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185 | 186 | 185.9 | 185.6 | 185.4 | 187.4 | 187.2 | 188.3 | 187.9 | 187.2 | 186.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185 | 186 | 185.9 | 185.6 | 185.4 | 187.4 | 187.2 | 188.3 | 187.9 | 187.2 | 186.4 |
| CPU used with Omni's own (cores), mean | 2.478 | 2.447 | 2.542 | 2.522 | 2.525 | 2.499 | 2.643 | 2.625 | 2.761 | 2.737 | 2.622 | 2.574 |
| host CPU busy, the real machine under kind (%) | 72.29 | 71.81 | 74.09 | 73.7 | 73.84 | 73.23 | 77.1 | 76.62 | 80.24 | 79.7 | 76.78 | 76.02 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.002439 | 0.004878 | 0.01111 | 0.01667 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

36 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1621 | 940.5 | -42.0% | -907.8 to -453.6 | better |
| response time (ms), 99th percentile | 4057 | 3228 | -20.4% | -1130 to -529 | better |
| time over the response line (% of samples) | 28.06 | 15.21 | -45.8% | -15.91 to -9.784 | better |
| failed requests (%) | 9.633 | 8.337 | -13.5% | -1.847 to -0.7456 | better |
| HPA replicas, mean | 9.692 | 9.671 | -0.2% | -0.058 to +0.01679 | better (inside the noise) |
| pods started | 4.167 | 4.361 | +4.7% | -0.3399 to +0.7288 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.234e-16 to +2.754e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 184.9 | -0.1% | -0.5628 to +0.008772 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 184.9 | -0.1% | -0.5628 to +0.008772 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.461 | 2.434 | -1.1% | -0.0397 to -0.01373 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 71.82 | 71.45 | -0.5% | -0.7504 to +0.009564 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001007 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 8, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 0

37 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2036 | 1037 | -49.1% | -1310 to -687.8 | better |
| response time (ms), 99th percentile | 5262 | 4650 | -11.6% | -1069 to -155.9 | better |
| time over the response line (% of samples) | 28.53 | 14.04 | -50.8% | -17.01 to -11.97 | better |
| failed requests (%) | 8.675 | 7.474 | -13.8% | -1.608 to -0.7938 | better |
| HPA replicas, mean | 9.745 | 9.787 | +0.4% | +0.01456 to +0.06873 | WORSE |
| pods started | 4.135 | 3.595 | -13.1% | -1.065 to -0.01658 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.567e-16 to +2.607e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.7 | -0.2% | -0.6059 to -0.01577 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.7 | -0.2% | -0.6059 to -0.01577 | better |
| CPU used with Omni's own (cores), mean | 2.535 | 2.497 | -1.5% | -0.04964 to -0.02761 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.87 | 73.02 | -1.1% | -1.069 to -0.6296 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1762 | 1053 | -40.2% | -897.3 to -521.1 | better |
| response time (ms), 99th percentile | 5298 | 4977 | -6.1% | -754.8 to +112.4 | better (inside the noise) |
| time over the response line (% of samples) | 27.33 | 13.11 | -52.0% | -16.5 to -11.93 | better |
| failed requests (%) | 7.593 | 6.43 | -15.3% | -1.53 to -0.795 | better |
| HPA replicas, mean | 9.787 | 9.804 | +0.2% | -0.003277 to +0.03755 | WORSE (inside the noise) |
| pods started | 3.5 | 3.175 | -9.3% | -0.6989 to +0.04891 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.038e-16 to +3.594e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185.3 | -0.1% | -0.4728 to -0.06633 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 185.3 | -0.1% | -0.4728 to -0.06633 | better |
| CPU used with Omni's own (cores), mean | 2.525 | 2.488 | -1.5% | -0.04711 to -0.02828 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.84 | 72.95 | -1.2% | -1.1 to -0.6738 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

38 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2389 | 1661 | -30.5% | -946.1 to -510.1 | better |
| response time (ms), 99th percentile | 4974 | 4755 | -4.4% | -691.8 to +253.8 | better (inside the noise) |
| time over the response line (% of samples) | 34.87 | 18.5 | -46.9% | -19.46 to -13.27 | better |
| failed requests (%) | 9.838 | 8.395 | -14.7% | -1.985 to -0.9015 | better |
| HPA replicas, mean | 9.702 | 9.72 | +0.2% | -0.01114 to +0.04578 | WORSE (inside the noise) |
| pods started | 3.763 | 3.579 | -4.9% | -0.6681 to +0.2997 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.397e-16 to +5.605e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.4 | 187.2 | -0.1% | -0.4272 to +0.01617 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.4 | 187.2 | -0.1% | -0.4272 to +0.01617 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.643 | 2.625 | -0.7% | -0.03173 to -0.005 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 77.1 | 76.62 | -0.6% | -0.7971 to -0.1486 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2401 | 1429 | -40.5% | -1170 to -773.5 | better |
| response time (ms), 99th percentile | 5468 | 4416 | -19.2% | -1473 to -630.2 | better |
| time over the response line (% of samples) | 38.2 | 20.76 | -45.7% | -20.12 to -14.76 | better |
| failed requests (%) | 10.75 | 9.484 | -11.8% | -2.165 to -0.3701 | better |
| HPA replicas, mean | 9.765 | 9.737 | -0.3% | -0.06696 to +0.0112 | better (inside the noise) |
| pods started | 3.195 | 3.293 | +3.1% | -0.3503 to +0.5454 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.295e-16 to +2.562e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.3 | 187.9 | -0.2% | -0.8199 to +0.01504 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.3 | 187.9 | -0.2% | -0.8199 to +0.01504 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.761 | 2.737 | -0.9% | -0.0386 to -0.01047 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 80.24 | 79.7 | -0.7% | -0.9661 to -0.1033 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0.002439 | 0.004878 | +100.0% | -0.00591 to +0.01079 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 7, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 1

36 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1649 | 1113 | -32.5% | -670.4 to -401.5 | better |
| response time (ms), 99th percentile | 4542 | 3790 | -16.6% | -1250 to -254.6 | better |
| time over the response line (% of samples) | 31.77 | 16.81 | -47.1% | -17.47 to -12.44 | better |
| failed requests (%) | 10.62 | 9.183 | -13.5% | -1.944 to -0.9322 | better |
| HPA replicas, mean | 9.741 | 9.768 | +0.3% | +0.005464 to +0.0492 | WORSE |
| pods started | 3.75 | 3.528 | -5.9% | -0.6647 to +0.2203 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.243e-16 to +6.177e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.2 | 186.4 | -0.5% | -1.231 to -0.4956 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.2 | 186.4 | -0.5% | -1.231 to -0.4956 | better |
| CPU used with Omni's own (cores), mean | 2.622 | 2.574 | -1.8% | -0.06462 to -0.03045 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.78 | 76.02 | -1.0% | -1.237 to -0.2826 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.232e+07 to +4.232e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.274e-08 to -5.274e-08 | WORSE |
| organism behind its window (s) | 0.01111 | 0.01667 | +50.0% | -0.009953 to +0.02106 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
