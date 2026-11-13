# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1666 | 835.2 | 1801 | 873.7 | 1722 | 904.5 | 1540 | 913.9 | 1860 | 1269 | 1348 | 995 |
| response time (ms), 99th percentile | 4731 | 3723 | 4681 | 3886 | 4424 | 4384 | 3388 | 2482 | 3943 | 3771 | 3605 | 3348 |
| time over the response line (% of samples) | 30.22 | 16.86 | 26.67 | 13.8 | 21.47 | 9.219 | 22.32 | 11.85 | 28.99 | 14.63 | 24.75 | 12.74 |
| failed requests (%) | 10.39 | 9.387 | 8.214 | 7.29 | 4.576 | 3.708 | 6.61 | 5.746 | 7.864 | 6.131 | 8.551 | 7.222 |
| HPA replicas, mean | 9.704 | 9.737 | 9.765 | 9.757 | 9.737 | 9.737 | 9.572 | 9.599 | 9.653 | 9.669 | 9.659 | 9.613 |
| pods started | 4.4 | 3.7 | 3.4 | 4 | 4.3 | 4.1 | 4.8 | 4.6 | 4.3 | 4 | 4.5 | 5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 186.6 | 186 | 185.6 | 185 | 183.7 | 183.4 | 183 | 182.6 | 185.1 | 184.7 | 183.1 | 182.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.6 | 186 | 185.6 | 185 | 183.7 | 183.4 | 183 | 182.6 | 185.1 | 184.7 | 183.1 | 182.6 |
| CPU used with Omni's own (cores), mean | 2.586 | 2.557 | 2.488 | 2.455 | 2.31 | 2.263 | 2.187 | 2.167 | 2.472 | 2.426 | 2.299 | 2.256 |
| host CPU busy, the real machine under kind (%) | 75.75 | 74.92 | 72.88 | 72.29 | 67.82 | 66.99 | 64.63 | 64.25 | 72.24 | 71.22 | 67.62 | 67.16 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0.01 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.01 | 0.01 | 0.01 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1666 | 835.2 | -49.9% | -1358 to -303.5 | better |
| response time (ms), 99th percentile | 4731 | 3723 | -21.3% | -2160 to +145.2 | better (inside the noise) |
| time over the response line (% of samples) | 30.22 | 16.86 | -44.2% | -19.44 to -7.273 | better |
| failed requests (%) | 10.39 | 9.387 | -9.6% | -1.806 to -0.1937 | better |
| HPA replicas, mean | 9.704 | 9.737 | +0.3% | -0.04295 to +0.1083 | WORSE (inside the noise) |
| pods started | 4.4 | 3.7 | -15.9% | -2.133 to +0.7326 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.224e-15 to -1.901e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.6 | 186 | -0.3% | -1.496 to +0.2862 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.6 | 186 | -0.3% | -1.496 to +0.2862 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.586 | 2.557 | -1.1% | -0.06006 to +0.002428 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.75 | 74.92 | -1.1% | -1.784 to +0.1301 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.057e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001006 | WORSE |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1801 | 873.7 | -51.5% | -1440 to -415 | better |
| response time (ms), 99th percentile | 4681 | 3886 | -17.0% | -1566 to -23.35 | better |
| time over the response line (% of samples) | 26.67 | 13.8 | -48.3% | -18.17 to -7.569 | better |
| failed requests (%) | 8.214 | 7.29 | -11.2% | -1.606 to -0.2411 | better |
| HPA replicas, mean | 9.765 | 9.757 | -0.1% | -0.08635 to +0.06908 | better (inside the noise) |
| pods started | 3.4 | 4 | +17.6% | -0.6707 to +1.871 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.338e-16 to +4.785e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185 | -0.4% | -1.572 to +0.2308 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 185 | -0.4% | -1.572 to +0.2308 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.488 | 2.455 | -1.3% | -0.05805 to -0.008829 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.88 | 72.29 | -0.8% | -1.068 to -0.1219 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1722 | 904.5 | -47.5% | -1333 to -301.4 | better |
| response time (ms), 99th percentile | 4424 | 4384 | -0.9% | -736.6 to +656.9 | better (inside the noise) |
| time over the response line (% of samples) | 21.47 | 9.219 | -57.1% | -18.17 to -6.331 | better |
| failed requests (%) | 4.576 | 3.708 | -19.0% | -1.701 to -0.0366 | better |
| HPA replicas, mean | 9.737 | 9.737 | -0.0% | -0.07318 to +0.07149 | better (inside the noise) |
| pods started | 4.3 | 4.1 | -4.7% | -1.623 to +1.223 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.162e-15 to +8.066e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.4 | -0.2% | -1.045 to +0.4684 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.4 | -0.2% | -1.045 to +0.4684 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.31 | 2.263 | -2.0% | -0.07992 to -0.01413 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 67.82 | 66.99 | -1.2% | -1.339 to -0.3182 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1540 | 913.9 | -40.6% | -1095 to -156.9 | better |
| response time (ms), 99th percentile | 3388 | 2482 | -26.7% | -1620 to -191 | better |
| time over the response line (% of samples) | 22.32 | 11.85 | -46.9% | -18.29 to -2.655 | better |
| failed requests (%) | 6.61 | 5.746 | -13.1% | -1.752 to +0.02605 | better (inside the noise) |
| HPA replicas, mean | 9.572 | 9.599 | +0.3% | -0.03854 to +0.09338 | WORSE (inside the noise) |
| pods started | 4.8 | 4.6 | -4.2% | -1.2 to +0.8003 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.989e-16 to +5.436e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183 | 182.6 | -0.2% | -1.311 to +0.5892 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183 | 182.6 | -0.2% | -1.311 to +0.5892 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.187 | 2.167 | -0.9% | -0.05197 to +0.01198 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 64.63 | 64.25 | -0.6% | -1.336 to +0.5696 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1860 | 1269 | -31.8% | -1124 to -56.86 | better |
| response time (ms), 99th percentile | 3943 | 3771 | -4.4% | -1132 to +786.9 | better (inside the noise) |
| time over the response line (% of samples) | 28.99 | 14.63 | -49.5% | -21.61 to -7.119 | better |
| failed requests (%) | 7.864 | 6.131 | -22.0% | -3.238 to -0.2261 | better |
| HPA replicas, mean | 9.653 | 9.669 | +0.2% | -0.09043 to +0.1234 | WORSE (inside the noise) |
| pods started | 4.3 | 4 | -7.0% | -1.733 to +1.133 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 184.7 | -0.2% | -1.543 to +0.7782 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 184.7 | -0.2% | -1.543 to +0.7782 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.472 | 2.426 | -1.8% | -0.06896 to -0.02211 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.24 | 71.22 | -1.4% | -1.588 to -0.4598 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1348 | 995 | -26.2% | -677.8 to -28.44 | better |
| response time (ms), 99th percentile | 3605 | 3348 | -7.1% | -746.4 to +232.6 | better (inside the noise) |
| time over the response line (% of samples) | 24.75 | 12.74 | -48.5% | -19.37 to -4.658 | better |
| failed requests (%) | 8.551 | 7.222 | -15.5% | -2.406 to -0.2506 | better |
| HPA replicas, mean | 9.659 | 9.613 | -0.5% | -0.1409 to +0.04847 | better (inside the noise) |
| pods started | 4.5 | 5 | +11.1% | -1.017 to +2.017 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.793e-16 to +1.057e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.1 | 182.6 | -0.2% | -1.251 to +0.3566 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.1 | 182.6 | -0.2% | -1.251 to +0.3566 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.299 | 2.256 | -1.8% | -0.05945 to -0.02552 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 67.62 | 67.16 | -0.7% | -1.005 to +0.07495 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.232e+07 to +4.232e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.274e-08 to -5.274e-08 | WORSE |
| organism behind its window (s) | 0.01 | 0.01 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
