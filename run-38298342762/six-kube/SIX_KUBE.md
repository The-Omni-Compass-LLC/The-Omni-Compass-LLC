# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2810 | 1479 | 2757 | 1500 | 2284 | 1350 | 3320 | 1901 | 3200 | 2156 | 2685 | 1227 |
| response time (ms), 99th percentile | 5538 | 4276 | 5385 | 4368 | 5199 | 3940 | 5405 | 4614 | 5376 | 4844 | 4883 | 3362 |
| time over the response line (% of samples) | 55.82 | 36.91 | 46.75 | 32.24 | 49.84 | 36.12 | 48.15 | 34.88 | 52.8 | 41.31 | 48.91 | 36.91 |
| failed requests (%) | 29.31 | 26.21 | 24.77 | 22.69 | 29.7 | 26.88 | 26.29 | 24.53 | 32.69 | 30.27 | 26.96 | 25.25 |
| HPA replicas, mean | 9.81 | 9.824 | 9.743 | 9.759 | 9.768 | 9.771 | 9.729 | 9.743 | 9.76 | 9.794 | 9.792 | 9.804 |
| pods started | 2.976 | 2.829 | 3.707 | 3.537 | 3.22 | 3.317 | 3.976 | 3.805 | 3.683 | 3.073 | 3 | 2.78 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 191.6 | 191.6 | 190.4 | 190.2 | 190.4 | 190.2 | 189.5 | 189.2 | 190.5 | 189.4 | 189.6 | 188.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.6 | 191.6 | 190.4 | 190.2 | 190.4 | 190.2 | 189.5 | 189.2 | 190.5 | 189.4 | 189.6 | 188.6 |
| CPU used with Omni's own (cores), mean | 3.152 | 3.116 | 3.005 | 2.963 | 3.008 | 2.971 | 2.928 | 2.876 | 2.969 | 2.91 | 2.887 | 2.813 |
| host CPU busy, the real machine under kind (%) | 91.04 | 90.9 | 86.9 | 86.35 | 87.33 | 87.04 | 84.56 | 83.95 | 86.68 | 86.45 | 85.02 | 85.66 |
| organism work | 2.18e+11 | 2.18e+11 | 2.265e+11 | 2.265e+11 | 6.677e+11 | 6.677e+11 | 2.225e+11 | 2.225e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.579e+11 | 1.58e+11 | 2.012e+11 | 2.013e+11 | 1.103e+14 | 1.103e+14 | 5.684e+11 | 5.685e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.011 | 2.004 | 4.863 | 4.855 | 1.448 | 1.44 | 2.578 | 2.569 | 2.71 | 2.707 | 2.615 | 2.607 |
| organism work per energy | 1.381 | 1.38 | 1.126 | 1.125 | 0.006054 | 0.006054 | 0.3915 | 0.3914 | 0.006232 | 0.006232 | 0.012 | 0.012 |
| organism behind its window (s) | 0.09512 | 0.0878 | 0.05366 | 0.05854 | 0.06585 | 0.07073 | 0.07805 | 0.07561 | 0.1927 | 0.2073 | 0.3293 | 0.378 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2810 | 1479 | -47.4% | -1615 to -1047 | better |
| response time (ms), 99th percentile | 5538 | 4276 | -22.8% | -1924 to -601.5 | better |
| time over the response line (% of samples) | 55.82 | 36.91 | -33.9% | -20.82 to -17 | better |
| failed requests (%) | 29.31 | 26.21 | -10.6% | -3.945 to -2.246 | better |
| HPA replicas, mean | 9.81 | 9.824 | +0.1% | -0.01223 to +0.0406 | WORSE (inside the noise) |
| pods started | 2.976 | 2.829 | -4.9% | -0.6282 to +0.3355 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.974e-18 to +6.952e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191.6 | 191.6 | -0.0% | -0.3619 to +0.3268 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.6 | 191.6 | -0.0% | -0.3619 to +0.3268 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.152 | 3.116 | -1.1% | -0.04747 to -0.02433 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.04 | 90.9 | -0.2% | -0.4539 to +0.1688 | shown, not judged (more or less is not better by itself) |
| organism work | 2.18e+11 | 2.18e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.579e+11 | 1.58e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.011 | 2.004 | -0.3% | -0.006761 to -0.006761 | better |
| organism work per energy | 1.381 | 1.38 | -0.1% | -0.0009278 to -0.0009278 | WORSE |
| organism behind its window (s) | 0.09512 | 0.0878 | -7.7% | -0.03328 to +0.01865 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2757 | 1500 | -45.6% | -1584 to -930.4 | better |
| response time (ms), 99th percentile | 5385 | 4368 | -18.9% | -1500 to -535.1 | better |
| time over the response line (% of samples) | 46.75 | 32.24 | -31.0% | -16.5 to -12.51 | better |
| failed requests (%) | 24.77 | 22.69 | -8.4% | -2.767 to -1.403 | better |
| HPA replicas, mean | 9.743 | 9.759 | +0.2% | -0.004446 to +0.03525 | WORSE (inside the noise) |
| pods started | 3.707 | 3.537 | -4.6% | -0.5323 to +0.1908 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.822e-16 to +4.555e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.4 | 190.2 | -0.1% | -0.4432 to +0.0816 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.4 | 190.2 | -0.1% | -0.4432 to +0.0816 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.005 | 2.963 | -1.4% | -0.05313 to -0.03149 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.9 | 86.35 | -0.6% | -0.8532 to -0.2503 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.012e+11 | 2.013e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 4.863 | 4.855 | -0.2% | -0.008037 to -0.008037 | better |
| organism work per energy | 1.126 | 1.125 | -0.1% | -0.0005938 to -0.0005938 | WORSE |
| organism behind its window (s) | 0.05366 | 0.05854 | +9.1% | -0.01035 to +0.02011 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 5, worse on 0, inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2284 | 1350 | -40.9% | -1215 to -652.8 | better |
| response time (ms), 99th percentile | 5199 | 3940 | -24.2% | -1983 to -534.9 | better |
| time over the response line (% of samples) | 49.84 | 36.12 | -27.5% | -15.86 to -11.6 | better |
| failed requests (%) | 29.7 | 26.88 | -9.5% | -3.635 to -2.008 | better |
| HPA replicas, mean | 9.768 | 9.771 | +0.0% | -0.02412 to +0.03019 | WORSE (inside the noise) |
| pods started | 3.22 | 3.317 | +3.0% | -0.345 to +0.5401 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.822e-16 to +2.222e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.4 | 190.2 | -0.1% | -0.4007 to +0.07469 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.4 | 190.2 | -0.1% | -0.4007 to +0.07469 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.008 | 2.971 | -1.2% | -0.04702 to -0.0268 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 87.33 | 87.04 | -0.3% | -0.5409 to -0.04259 | shown, not judged (more or less is not better by itself) |
| organism work | 6.677e+11 | 6.677e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.448 | 1.44 | -0.6% | -0.008511 to -0.008511 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -5.827e-09 to -5.827e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.06585 | 0.07073 | +7.4% | -0.001798 to +0.01155 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3320 | 1901 | -42.7% | -1876 to -961.3 | better |
| response time (ms), 99th percentile | 5405 | 4614 | -14.6% | -1283 to -298.6 | better |
| time over the response line (% of samples) | 48.15 | 34.88 | -27.6% | -15.58 to -10.97 | better |
| failed requests (%) | 26.29 | 24.53 | -6.7% | -2.483 to -1.038 | better |
| HPA replicas, mean | 9.729 | 9.743 | +0.1% | -0.01386 to +0.04199 | WORSE (inside the noise) |
| pods started | 3.976 | 3.805 | -4.3% | -0.6591 to +0.3176 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.572e-16 to +1.673e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.5 | 189.2 | -0.2% | -0.6311 to -0.06463 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.5 | 189.2 | -0.2% | -0.6311 to -0.06463 | better |
| CPU used with Omni's own (cores), mean | 2.928 | 2.876 | -1.8% | -0.06636 to -0.03895 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.56 | 83.95 | -0.7% | -0.9827 to -0.2355 | shown, not judged (more or less is not better by itself) |
| organism work | 2.225e+11 | 2.225e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.684e+11 | 5.685e+11 | +0.0% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.578 | 2.569 | -0.3% | -0.008527 to -0.008527 | better |
| organism work per energy | 0.3915 | 0.3914 | -0.0% | -7.311e-05 to -7.311e-05 | WORSE |
| organism behind its window (s) | 0.07805 | 0.07561 | -3.1% | -0.02461 to +0.01973 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 8, worse on 1 (HPA replicas, mean), inside the noise on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3200 | 2156 | -32.6% | -1505 to -582.6 | better |
| response time (ms), 99th percentile | 5376 | 4844 | -9.9% | -1040 to -24.9 | better |
| time over the response line (% of samples) | 52.8 | 41.31 | -21.8% | -13.65 to -9.341 | better |
| failed requests (%) | 32.69 | 30.27 | -7.4% | -3.622 to -1.211 | better |
| HPA replicas, mean | 9.76 | 9.794 | +0.3% | +0.008185 to +0.05966 | WORSE |
| pods started | 3.683 | 3.073 | -16.6% | -1.042 to -0.1775 | better |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.922e-17 to +5.658e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.5 | 189.4 | -0.6% | -1.552 to -0.7167 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.5 | 189.4 | -0.6% | -1.552 to -0.7167 | better |
| CPU used with Omni's own (cores), mean | 2.969 | 2.91 | -2.0% | -0.07018 to -0.04941 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.68 | 86.45 | -0.3% | -0.6008 to +0.1466 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.71 | 2.707 | -0.1% | -0.003646 to -0.003646 | better |
| organism work per energy | 0.006232 | 0.006232 | -0.0% | -5.971e-09 to -5.971e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.1927 | 0.2073 | +7.6% | -0.0213 to +0.05057 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2685 | 1227 | -54.3% | -1925 to -991.8 | better |
| response time (ms), 99th percentile | 4883 | 3362 | -31.2% | -2118 to -925.6 | better |
| time over the response line (% of samples) | 48.91 | 36.91 | -24.5% | -14.15 to -9.848 | better |
| failed requests (%) | 26.96 | 25.25 | -6.3% | -2.284 to -1.129 | better |
| HPA replicas, mean | 9.792 | 9.804 | +0.1% | -0.01207 to +0.03537 | WORSE (inside the noise) |
| pods started | 3 | 2.78 | -7.3% | -0.6098 to +0.1708 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.001e-16 to +2.701e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.6 | 188.6 | -0.6% | -1.472 to -0.646 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.6 | 188.6 | -0.6% | -1.472 to -0.646 | better |
| CPU used with Omni's own (cores), mean | 2.887 | 2.813 | -2.6% | -0.08507 to -0.06433 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.02 | 85.66 | +0.8% | +0.4147 to +0.8691 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +4.246e+08 to +4.246e+08 | WORSE |
| organism time over the line (% of steps) | 2.615 | 2.607 | -0.3% | -0.007918 to -0.007918 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -4.582e-08 to -4.582e-08 | WORSE |
| organism behind its window (s) | 0.3293 | 0.378 | +14.8% | +0.002297 to +0.09526 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
