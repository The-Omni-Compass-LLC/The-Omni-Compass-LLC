# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2800 | 1560 | 2715 | 1908 | 1682 | 1018 | 3700 | 1974 | 3047 | 1742 | 1756 | 1028 |
| response time (ms), 99th percentile | 5224 | 2860 | 5612 | 4726 | 3566 | 2638 | 5777 | 3814 | 4715 | 3729 | 3677 | 2634 |
| time over the response line (% of samples) | 54.81 | 36.59 | 55.57 | 42.22 | 31.21 | 22.02 | 52.61 | 39.6 | 48.05 | 35.81 | 42.87 | 31.92 |
| failed requests (%) | 27.91 | 24.8 | 34.3 | 31.43 | 17.95 | 15.7 | 28.71 | 27.15 | 27.63 | 26.13 | 23.08 | 22.15 |
| HPA replicas, mean | 9.788 | 9.8 | 9.831 | 9.848 | 9.593 | 9.637 | 9.744 | 9.749 | 9.724 | 9.745 | 9.741 | 9.75 |
| pods started | 3.3 | 3.2 | 2.4 | 2.2 | 5.3 | 4.8 | 4 | 3.9 | 4.1 | 4.1 | 3.5 | 3.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 191.2 | 191.2 | 192.1 | 191.9 | 186 | 185.6 | 191 | 190.9 | 188.8 | 188.7 | 187.9 | 187.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.2 | 191.2 | 192.1 | 191.9 | 186 | 185.6 | 191 | 190.9 | 188.8 | 188.7 | 187.9 | 187.6 |
| CPU used with Omni's own (cores), mean | 3.129 | 3.09 | 3.14 | 3.106 | 2.536 | 2.472 | 3.075 | 3.048 | 2.86 | 2.792 | 2.735 | 2.674 |
| host CPU busy, the real machine under kind (%) | 89.87 | 89.54 | 91.24 | 90.99 | 74.14 | 72.94 | 88.57 | 88.49 | 83.31 | 83.05 | 80.41 | 81.36 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.944 | 4.802 | 4.711 | 1.468 | 1.383 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.525 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.07 | 0.12 | 0.08 | 0.08 | 0.02 | 0.04 | 0.08 | 0.09 | 0.25 | 0.26 | 0.33 | 0.35 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2800 | 1560 | -44.3% | -2190 to -289.1 | better |
| response time (ms), 99th percentile | 5224 | 2860 | -45.3% | -3230 to -1499 | better |
| time over the response line (% of samples) | 54.81 | 36.59 | -33.2% | -23.23 to -13.2 | better |
| failed requests (%) | 27.91 | 24.8 | -11.1% | -5.659 to -0.5601 | better |
| HPA replicas, mean | 9.788 | 9.8 | +0.1% | -0.04903 to +0.07392 | WORSE (inside the noise) |
| pods started | 3.3 | 3.2 | -3.0% | -1.08 to +0.8802 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.924e-16 to +7.924e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 191.2 | 191.2 | -0.0% | -0.7106 to +0.6651 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.2 | 191.2 | -0.0% | -0.7106 to +0.6651 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.129 | 3.09 | -1.3% | -0.06228 to -0.0164 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.87 | 89.54 | -0.4% | -1.167 to +0.5061 | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.78e+07 to +8.781e+07 | WORSE |
| organism time over the line (% of steps) | 2.018 | 1.944 | -3.7% | -0.07392 to -0.07392 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007627 to -0.0007627 | WORSE |
| organism behind its window (s) | 0.07 | 0.12 | +71.4% | +0.0123 to +0.0877 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2715 | 1908 | -29.7% | -1431 to -183.6 | better |
| response time (ms), 99th percentile | 5612 | 4726 | -15.8% | -2262 to +489.4 | better (inside the noise) |
| time over the response line (% of samples) | 55.57 | 42.22 | -24.0% | -17.34 to -9.365 | better |
| failed requests (%) | 34.3 | 31.43 | -8.4% | -5 to -0.7537 | better |
| HPA replicas, mean | 9.831 | 9.848 | +0.2% | -0.0443 to +0.07784 | WORSE (inside the noise) |
| pods started | 2.4 | 2.2 | -8.3% | -1.012 to +0.6121 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.531e-16 to +1.264e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.1 | 191.9 | -0.1% | -0.5659 to +0.2388 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.1 | 191.9 | -0.1% | -0.5659 to +0.2388 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.14 | 3.106 | -1.1% | -0.0686 to +0.001318 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.24 | 90.99 | -0.3% | -0.7917 to +0.2791 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +9.075e+07 to +9.075e+07 | WORSE |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09107 to -0.09107 | better |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0005052 to -0.0005052 | WORSE |
| organism behind its window (s) | 0.08 | 0.08 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 5, worse on 0, inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1682 | 1018 | -39.5% | -1039 to -288.9 | better |
| response time (ms), 99th percentile | 3566 | 2638 | -26.0% | -1622 to -233 | better |
| time over the response line (% of samples) | 31.21 | 22.02 | -29.4% | -15.07 to -3.304 | better |
| failed requests (%) | 17.95 | 15.7 | -12.5% | -4.282 to -0.2027 | better |
| HPA replicas, mean | 9.593 | 9.637 | +0.5% | -0.02663 to +0.1137 | WORSE (inside the noise) |
| pods started | 5.3 | 4.8 | -9.4% | -1.58 to +0.5796 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.788e-16 to +3.235e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.6 | -0.2% | -1.367 to +0.5145 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.6 | -0.2% | -1.367 to +0.5145 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.536 | 2.472 | -2.5% | -0.1248 to -0.004381 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.14 | 72.94 | -1.6% | -2.922 to +0.5217 | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.722e+07 to +8.722e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.383 | -5.8% | -0.08481 to -0.08481 | better |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.789e-09 to -4.789e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.02 | 0.04 | +100.0% | -0.01016 to +0.05016 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3700 | 1974 | -46.6% | -3320 to -131.8 | better |
| response time (ms), 99th percentile | 5777 | 3814 | -34.0% | -3759 to -167.8 | better |
| time over the response line (% of samples) | 52.61 | 39.6 | -24.7% | -19.34 to -6.69 | better |
| failed requests (%) | 28.71 | 27.15 | -5.4% | -3.663 to +0.5451 | better (inside the noise) |
| HPA replicas, mean | 9.744 | 9.749 | +0.0% | -0.03427 to +0.04388 | WORSE (inside the noise) |
| pods started | 4 | 3.9 | -2.5% | -0.8113 to +0.6113 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.617e-15 to +1.81e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191 | 190.9 | -0.0% | -0.5093 to +0.3638 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191 | 190.9 | -0.0% | -0.5093 to +0.3638 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.075 | 3.048 | -0.9% | -0.04809 to -0.00571 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.57 | 88.49 | -0.1% | -0.6218 to +0.4599 | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +9.434e+07 to +9.434e+07 | WORSE |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.0953 to -0.0953 | better |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.487e-05 to -6.487e-05 | WORSE |
| organism behind its window (s) | 0.08 | 0.09 | +12.5% | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 3, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3047 | 1742 | -42.8% | -2528 to -82.88 | better |
| response time (ms), 99th percentile | 4715 | 3729 | -20.9% | -2007 to +33.11 | better (inside the noise) |
| time over the response line (% of samples) | 48.05 | 35.81 | -25.5% | -18.93 to -5.554 | better |
| failed requests (%) | 27.63 | 26.13 | -5.4% | -3.272 to +0.2738 | better (inside the noise) |
| HPA replicas, mean | 9.724 | 9.745 | +0.2% | -0.03132 to +0.0735 | WORSE (inside the noise) |
| pods started | 4.1 | 4.1 | +0.0% | -1.012 to +1.012 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.924e-16 to +7.924e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 188.8 | 188.7 | -0.0% | -0.8301 to +0.7225 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.8 | 188.7 | -0.0% | -0.8301 to +0.7225 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.86 | 2.792 | -2.4% | -0.08758 to -0.04806 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 83.31 | 83.05 | -0.3% | -1.08 to +0.5714 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.725e+07 to +8.725e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.4% | -0.03677 to -0.03677 | better |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.909e-09 to -4.909e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.25 | 0.26 | +4.0% | -0.1533 to +0.1733 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1756 | 1028 | -41.5% | -1238 to -217.8 | better |
| response time (ms), 99th percentile | 3677 | 2634 | -28.4% | -2338 to +252.9 | better (inside the noise) |
| time over the response line (% of samples) | 42.87 | 31.92 | -25.5% | -15.85 to -6.052 | better |
| failed requests (%) | 23.08 | 22.15 | -4.0% | -2.314 to +0.4529 | better (inside the noise) |
| HPA replicas, mean | 9.741 | 9.75 | +0.1% | -0.03545 to +0.05345 | WORSE (inside the noise) |
| pods started | 3.5 | 3.5 | +0.0% | -0.754 to +0.754 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.718e-16 to +4.495e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.9 | 187.6 | -0.1% | -1.033 to +0.5133 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.9 | 187.6 | -0.1% | -1.033 to +0.5133 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.735 | 2.674 | -2.2% | -0.09036 to -0.03187 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 80.41 | 81.36 | +1.2% | +0.5996 to +1.303 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.601e+08 to +3.601e+08 | WORSE |
| organism time over the line (% of steps) | 2.61 | 2.525 | -3.3% | -0.08571 to -0.08571 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.887e-08 to -3.886e-08 | WORSE |
| organism behind its window (s) | 0.33 | 0.35 | +6.1% | -0.09583 to +0.1358 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
