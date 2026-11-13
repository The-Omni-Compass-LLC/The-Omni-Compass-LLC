# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1980 | 897.7 | 2335 | 1282 | 2734 | 1375 | 3606 | 2462 | 3187 | 1970 | 2383 | 1255 |
| response time (ms), 99th percentile | 4076 | 3112 | 4701 | 3854 | 5446 | 3989 | 5982 | 5235 | 5197 | 4259 | 4951 | 3804 |
| time over the response line (% of samples) | 38.14 | 24.44 | 39.43 | 26.31 | 49.6 | 35.28 | 55.8 | 41.2 | 51.22 | 42.75 | 52.39 | 37.93 |
| failed requests (%) | 18.52 | 16.49 | 20.36 | 18.82 | 28.37 | 26.37 | 31.19 | 28.81 | 34.21 | 32.98 | 27.9 | 26.03 |
| HPA replicas, mean | 9.704 | 9.716 | 9.699 | 9.694 | 9.757 | 9.76 | 9.776 | 9.785 | 9.772 | 9.757 | 9.816 | 9.809 |
| pods started | 4.244 | 4.122 | 4.098 | 4.146 | 3.512 | 3.415 | 3.585 | 3.293 | 3.268 | 3.512 | 2.8 | 3 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 187.5 | 187.3 | 188.3 | 187.8 | 190.7 | 190.4 | 191.4 | 191.1 | 189.6 | 188.7 | 190.9 | 189.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.5 | 187.3 | 188.3 | 187.8 | 190.7 | 190.4 | 191.4 | 191.1 | 189.6 | 188.7 | 190.9 | 189.8 |
| CPU used with Omni's own (cores), mean | 2.735 | 2.688 | 2.791 | 2.754 | 3.016 | 2.988 | 3.101 | 3.054 | 2.89 | 2.816 | 3.017 | 2.957 |
| host CPU busy, the real machine under kind (%) | 78.71 | 78.21 | 81 | 80.35 | 87.51 | 87.29 | 89.28 | 89.02 | 84.63 | 84.15 | 88.63 | 89.79 |
| organism work | 2.18e+11 | 2.18e+11 | 2.265e+11 | 2.265e+11 | 6.677e+11 | 6.677e+11 | 2.225e+11 | 2.225e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.579e+11 | 1.58e+11 | 2.012e+11 | 2.013e+11 | 1.103e+14 | 1.103e+14 | 5.684e+11 | 5.685e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.011 | 2.004 | 4.863 | 4.855 | 1.448 | 1.44 | 2.578 | 2.569 | 2.71 | 2.707 | 2.615 | 2.607 |
| organism work per energy | 1.381 | 1.38 | 1.126 | 1.125 | 0.006054 | 0.006054 | 0.3915 | 0.3914 | 0.006232 | 0.006232 | 0.012 | 0.012 |
| organism behind its window (s) | 0.06098 | 0.05122 | 0.05366 | 0.03902 | 0.07805 | 0.07317 | 0.09512 | 0.08293 | 0.222 | 0.2341 | 0.3175 | 0.4171 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1980 | 897.7 | -54.7% | -1400 to -763.8 | better |
| response time (ms), 99th percentile | 4076 | 3112 | -23.7% | -1506 to -422.1 | better |
| time over the response line (% of samples) | 38.14 | 24.44 | -35.9% | -16.49 to -10.91 | better |
| failed requests (%) | 18.52 | 16.49 | -11.0% | -2.923 to -1.141 | better |
| HPA replicas, mean | 9.704 | 9.716 | +0.1% | -0.01342 to +0.03617 | WORSE (inside the noise) |
| pods started | 4.244 | 4.122 | -2.9% | -0.545 to +0.3011 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.006e-16 to +2.106e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.5 | 187.3 | -0.2% | -0.6269 to +0.05869 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.5 | 187.3 | -0.2% | -0.6269 to +0.05869 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.735 | 2.688 | -1.7% | -0.06511 to -0.02907 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.71 | 78.21 | -0.6% | -1.036 to +0.02845 | shown, not judged (more or less is not better by itself) |
| organism work | 2.18e+11 | 2.18e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.579e+11 | 1.58e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.011 | 2.004 | -0.3% | -0.006761 to -0.006761 | better |
| organism work per energy | 1.381 | 1.38 | -0.1% | -0.0009278 to -0.0009278 | WORSE |
| organism behind its window (s) | 0.06098 | 0.05122 | -16.0% | -0.02122 to +0.001707 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2335 | 1282 | -45.1% | -1382 to -724 | better |
| response time (ms), 99th percentile | 4701 | 3854 | -18.0% | -1392 to -302 | better |
| time over the response line (% of samples) | 39.43 | 26.31 | -33.3% | -15.65 to -10.58 | better |
| failed requests (%) | 20.36 | 18.82 | -7.6% | -2.188 to -0.8941 | better |
| HPA replicas, mean | 9.699 | 9.694 | -0.0% | -0.03409 to +0.02527 | better (inside the noise) |
| pods started | 4.098 | 4.146 | +1.2% | -0.454 to +0.5515 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.797e-16 to +3.064e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.3 | 187.8 | -0.2% | -0.7472 to -0.146 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.3 | 187.8 | -0.2% | -0.7472 to -0.146 | better |
| CPU used with Omni's own (cores), mean | 2.791 | 2.754 | -1.3% | -0.05261 to -0.02022 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81 | 80.35 | -0.8% | -1.103 to -0.1888 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.012e+11 | 2.013e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 4.863 | 4.855 | -0.2% | -0.008037 to -0.008037 | better |
| organism work per energy | 1.126 | 1.125 | -0.1% | -0.0005938 to -0.0005938 | WORSE |
| organism behind its window (s) | 0.05366 | 0.03902 | -27.3% | -0.03077 to +0.001507 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 5, worse on 0, inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2734 | 1375 | -49.7% | -1742 to -976.7 | better |
| response time (ms), 99th percentile | 5446 | 3989 | -26.8% | -2122 to -793.7 | better |
| time over the response line (% of samples) | 49.6 | 35.28 | -28.9% | -16.45 to -12.2 | better |
| failed requests (%) | 28.37 | 26.37 | -7.0% | -2.706 to -1.292 | better |
| HPA replicas, mean | 9.757 | 9.76 | +0.0% | -0.01753 to +0.0248 | WORSE (inside the noise) |
| pods started | 3.512 | 3.415 | -2.8% | -0.4775 to +0.2823 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.075e-16 to +5.108e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.7 | 190.4 | -0.1% | -0.5884 to +0.02132 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.7 | 190.4 | -0.1% | -0.5884 to +0.02132 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.016 | 2.988 | -0.9% | -0.03572 to -0.01875 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 87.51 | 87.29 | -0.2% | -0.3834 to -0.04268 | shown, not judged (more or less is not better by itself) |
| organism work | 6.677e+11 | 6.677e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.448 | 1.44 | -0.6% | -0.008511 to -0.008511 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -5.827e-09 to -5.827e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.07805 | 0.07317 | -6.3% | -0.02536 to +0.0156 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3606 | 2462 | -31.7% | -1649 to -638.1 | better |
| response time (ms), 99th percentile | 5982 | 5235 | -12.5% | -1292 to -202.1 | better |
| time over the response line (% of samples) | 55.8 | 41.2 | -26.2% | -16.72 to -12.49 | better |
| failed requests (%) | 31.19 | 28.81 | -7.6% | -3.586 to -1.167 | better |
| HPA replicas, mean | 9.776 | 9.785 | +0.1% | -0.0161 to +0.03384 | WORSE (inside the noise) |
| pods started | 3.585 | 3.293 | -8.2% | -0.7323 to +0.1469 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.453e-16 to +2.72e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191.4 | 191.1 | -0.1% | -0.6549 to +0.1314 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.4 | 191.1 | -0.1% | -0.6549 to +0.1314 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.101 | 3.054 | -1.5% | -0.05792 to -0.03596 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.28 | 89.02 | -0.3% | -0.5482 to +0.02706 | shown, not judged (more or less is not better by itself) |
| organism work | 2.225e+11 | 2.225e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.684e+11 | 5.685e+11 | +0.0% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.578 | 2.569 | -0.3% | -0.008527 to -0.008527 | better |
| organism work per energy | 0.3915 | 0.3914 | -0.0% | -7.311e-05 to -7.311e-05 | WORSE |
| organism behind its window (s) | 0.09512 | 0.08293 | -12.8% | -0.03798 to +0.01359 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 7, worse on 0, inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3187 | 1970 | -38.2% | -1800 to -636 | better |
| response time (ms), 99th percentile | 5197 | 4259 | -18.1% | -1564 to -312.7 | better |
| time over the response line (% of samples) | 51.22 | 42.75 | -16.5% | -10.99 to -5.955 | better |
| failed requests (%) | 34.21 | 32.98 | -3.6% | -2.181 to -0.2811 | better |
| HPA replicas, mean | 9.772 | 9.757 | -0.2% | -0.04369 to +0.01283 | better (inside the noise) |
| pods started | 3.268 | 3.512 | +7.5% | -0.2341 to +0.722 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.771e-16 to +5.237e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.6 | 188.7 | -0.5% | -1.343 to -0.4848 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.6 | 188.7 | -0.5% | -1.343 to -0.4848 | better |
| CPU used with Omni's own (cores), mean | 2.89 | 2.816 | -2.5% | -0.08838 to -0.05863 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.63 | 84.15 | -0.6% | -0.948 to -0.02332 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.71 | 2.707 | -0.1% | -0.003646 to -0.003646 | better |
| organism work per energy | 0.006232 | 0.006232 | -0.0% | -5.971e-09 to -5.971e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.222 | 0.2341 | +5.5% | -0.03819 to +0.06258 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2383 | 1245 | -47.7% | -1514 to -761.5 | better |
| response time (ms), 99th percentile | 4951 | 3847 | -22.3% | -1830 to -377.9 | better |
| time over the response line (% of samples) | 52.39 | 37.56 | -28.3% | -16.76 to -12.9 | better |
| failed requests (%) | 27.9 | 25.76 | -7.7% | -2.891 to -1.388 | better |
| HPA replicas, mean | 9.816 | 9.807 | -0.1% | -0.03173 to +0.01389 | better (inside the noise) |
| pods started | 2.8 | 3.025 | +8.0% | -0.1561 to +0.6061 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.603e-16 to +5.824e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.9 | 189.8 | -0.6% | -1.539 to -0.7015 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.9 | 189.8 | -0.6% | -1.539 to -0.7015 | better |
| CPU used with Omni's own (cores), mean | 3.017 | 2.951 | -2.2% | -0.07751 to -0.05465 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.63 | 89.59 | +1.1% | +0.6921 to +1.244 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +4.246e+08 to +4.246e+08 | WORSE |
| organism time over the line (% of steps) | 2.615 | 2.607 | -0.3% | -0.007918 to -0.007918 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -4.582e-08 to -4.582e-08 | WORSE |
| organism behind its window (s) | 0.3175 | 0.41 | +29.1% | +0.02504 to +0.16 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
