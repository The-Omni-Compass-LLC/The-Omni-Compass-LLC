# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1743 | 946.7 | 1514 | 820.9 | 1746 | 1067 | 2512 | 1633 | 2128 | 1471 | 1637 | 867.5 |
| response time (ms), 99th percentile | 4607 | 3372 | 4610 | 3873 | 4910 | 4319 | 5444 | 4855 | 4483 | 3763 | 4258 | 3446 |
| time over the response line (% of samples) | 30.39 | 15.59 | 22.56 | 10.67 | 24.26 | 11.65 | 35.33 | 19.56 | 32.27 | 18.47 | 30.26 | 16.24 |
| failed requests (%) | 10.05 | 8.313 | 6.022 | 4.996 | 6.342 | 5.466 | 10.31 | 8.713 | 9.366 | 8.179 | 10.13 | 8.741 |
| HPA replicas, mean | 9.742 | 9.746 | 9.728 | 9.737 | 9.72 | 9.75 | 9.702 | 9.728 | 9.69 | 9.658 | 9.73 | 9.729 |
| pods started | 3.732 | 3.78 | 4.244 | 4.268 | 4.098 | 3.707 | 3.683 | 3.268 | 3.732 | 3.829 | 3.683 | 3.805 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 186.9 | 186.3 | 183.9 | 183.4 | 184 | 183.8 | 187.4 | 187.1 | 186.2 | 185.8 | 186.5 | 186.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.9 | 186.3 | 183.9 | 183.4 | 184 | 183.8 | 187.4 | 187.1 | 186.2 | 185.8 | 186.5 | 186.1 |
| CPU used with Omni's own (cores), mean | 2.592 | 2.546 | 2.356 | 2.306 | 2.365 | 2.342 | 2.674 | 2.653 | 2.533 | 2.516 | 2.553 | 2.525 |
| host CPU busy, the real machine under kind (%) | 75.53 | 74.66 | 68.95 | 68.05 | 69.13 | 68.56 | 77.5 | 77.24 | 73.82 | 73.57 | 74.84 | 74.35 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0.002439 | 0 | 0 | 0 | 0 | 0 | 0 | 0.002439 | 0 | 0.004878 | 0 | 0.01707 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1743 | 946.7 | -45.7% | -955.3 to -637.4 | better |
| response time (ms), 99th percentile | 4607 | 3372 | -26.8% | -1682 to -789.6 | better |
| time over the response line (% of samples) | 30.39 | 15.59 | -48.7% | -17.37 to -12.23 | better |
| failed requests (%) | 10.05 | 8.313 | -17.3% | -2.402 to -1.074 | better |
| HPA replicas, mean | 9.742 | 9.746 | +0.0% | -0.02519 to +0.03212 | WORSE (inside the noise) |
| pods started | 3.732 | 3.78 | +1.3% | -0.4398 to +0.5374 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.417e-16 to +3.117e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.9 | 186.3 | -0.3% | -0.8623 to -0.1814 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.9 | 186.3 | -0.3% | -0.8623 to -0.1814 | better |
| CPU used with Omni's own (cores), mean | 2.592 | 2.546 | -1.8% | -0.06268 to -0.02998 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.53 | 74.66 | -1.1% | -1.231 to -0.502 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001006 | WORSE |
| organism behind its window (s) | 0.002439 | 0 | -100.0% | -0.00722 to +0.002341 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1514 | 820.9 | -45.8% | -876 to -511.1 | better |
| response time (ms), 99th percentile | 4610 | 3873 | -16.0% | -1086 to -386.4 | better |
| time over the response line (% of samples) | 22.56 | 10.67 | -52.7% | -14.09 to -9.68 | better |
| failed requests (%) | 6.022 | 4.996 | -17.0% | -1.463 to -0.5896 | better |
| HPA replicas, mean | 9.728 | 9.737 | +0.1% | -0.02068 to +0.03691 | WORSE (inside the noise) |
| pods started | 4.244 | 4.268 | +0.6% | -0.4165 to +0.4653 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.615e-16 to +4.348e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.4 | -0.2% | -0.623 to -0.2326 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.4 | -0.2% | -0.623 to -0.2326 | better |
| CPU used with Omni's own (cores), mean | 2.356 | 2.306 | -2.1% | -0.06131 to -0.03923 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 68.95 | 68.05 | -1.3% | -1.216 to -0.5831 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1746 | 1067 | -38.9% | -891.3 to -466.1 | better |
| response time (ms), 99th percentile | 4910 | 4319 | -12.0% | -1014 to -168.9 | better |
| time over the response line (% of samples) | 24.26 | 11.65 | -52.0% | -15.12 to -10.1 | better |
| failed requests (%) | 6.342 | 5.466 | -13.8% | -1.209 to -0.5434 | better |
| HPA replicas, mean | 9.72 | 9.75 | +0.3% | -0.001149 to +0.06177 | WORSE (inside the noise) |
| pods started | 4.098 | 3.707 | -9.5% | -0.8927 to +0.1122 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.803e-16 to +1.47e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.8 | -0.1% | -0.5395 to +0.09329 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.8 | -0.1% | -0.5395 to +0.09329 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.365 | 2.342 | -1.0% | -0.03451 to -0.01168 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.13 | 68.56 | -0.8% | -0.9294 to -0.2231 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 6, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2512 | 1633 | -35.0% | -1102 to -655.3 | better |
| response time (ms), 99th percentile | 5444 | 4855 | -10.8% | -1011 to -165.9 | better |
| time over the response line (% of samples) | 35.33 | 19.56 | -44.6% | -18.71 to -12.83 | better |
| failed requests (%) | 10.31 | 8.713 | -15.5% | -2.086 to -1.117 | better |
| HPA replicas, mean | 9.702 | 9.728 | +0.3% | +0.0007225 to +0.05131 | WORSE |
| pods started | 3.683 | 3.268 | -11.3% | -0.8136 to -0.01567 | better |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.195e-16 to +3.628e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.4 | 187.1 | -0.2% | -0.7366 to +0.0405 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.4 | 187.1 | -0.2% | -0.7366 to +0.0405 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.674 | 2.653 | -0.8% | -0.03697 to -0.003991 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 77.5 | 77.24 | -0.3% | -0.6281 to +0.12 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0.002439 | +0.00244 | -0.002341 to +0.00722 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2128 | 1471 | -30.9% | -867.1 to -447.3 | better |
| response time (ms), 99th percentile | 4483 | 3763 | -16.1% | -1127 to -312.3 | better |
| time over the response line (% of samples) | 32.27 | 18.47 | -42.8% | -16.79 to -10.81 | better |
| failed requests (%) | 9.366 | 8.179 | -12.7% | -1.81 to -0.5648 | better |
| HPA replicas, mean | 9.69 | 9.658 | -0.3% | -0.07036 to +0.007385 | better (inside the noise) |
| pods started | 3.732 | 3.829 | +2.6% | -0.3177 to +0.5128 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.248e-16 to +3.682e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.2 | 185.8 | -0.2% | -0.6083 to -0.09439 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.2 | 185.8 | -0.2% | -0.6083 to -0.09439 | better |
| CPU used with Omni's own (cores), mean | 2.533 | 2.516 | -0.7% | -0.0309 to -0.003848 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.82 | 73.57 | -0.3% | -0.5971 to +0.08535 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0 | 0.004878 | +0.00488 | -0.001798 to +0.01155 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1637 | 867.5 | -47.0% | -927.8 to -611.5 | better |
| response time (ms), 99th percentile | 4258 | 3446 | -19.1% | -1185 to -438.5 | better |
| time over the response line (% of samples) | 30.26 | 16.24 | -46.4% | -16.64 to -11.42 | better |
| failed requests (%) | 10.13 | 8.741 | -13.7% | -1.899 to -0.8734 | better |
| HPA replicas, mean | 9.73 | 9.729 | -0.0% | -0.03205 to +0.03017 | better (inside the noise) |
| pods started | 3.683 | 3.805 | +3.3% | -0.4349 to +0.6788 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.605e-16 to +2.006e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.5 | 186.1 | -0.2% | -0.6908 to -0.1288 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.5 | 186.1 | -0.2% | -0.6908 to -0.1288 | better |
| CPU used with Omni's own (cores), mean | 2.553 | 2.525 | -1.1% | -0.04332 to -0.01315 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.84 | 74.35 | -0.7% | -0.8293 to -0.155 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.232e+07 to +4.232e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.274e-08 to -5.274e-08 | WORSE |
| organism behind its window (s) | 0 | 0.01707 | +0.0171 | +0.003552 to +0.03059 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
