# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2900 | 1599 | 2698 | 1420 | 2118 | 926 | 3187 | 1660 | 3429 | 1980 | 2304 | 1195 |
| response time (ms), 99th percentile | 5443 | 3786 | 5621 | 3997 | 4141 | 2976 | 4780 | 3723 | 6221 | 4634 | 4405 | 4021 |
| time over the response line (% of samples) | 60.85 | 41.37 | 49.03 | 34.21 | 38.05 | 26.06 | 41.49 | 30.09 | 58.63 | 48.51 | 41.47 | 26.95 |
| failed requests (%) | 32.73 | 28.18 | 25.64 | 23.07 | 20.74 | 20.08 | 22.89 | 21.65 | 37.74 | 36.04 | 18.24 | 16.39 |
| HPA replicas, mean | 9.835 | 9.819 | 9.766 | 9.769 | 9.722 | 9.718 | 9.642 | 9.696 | 9.784 | 9.796 | 9.746 | 9.748 |
| pods started | 2.7 | 2.9 | 3.4 | 3.4 | 3.8 | 3.9 | 5 | 4.3 | 3.4 | 3.2 | 3.8 | 3.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 192.5 | 192.6 | 191 | 191 | 188 | 187.7 | 187.2 | 187 | 191.1 | 190.7 | 188.4 | 187.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.5 | 192.6 | 191 | 191 | 188 | 187.7 | 187.2 | 187 | 191.1 | 190.7 | 188.4 | 187.2 |
| CPU used with Omni's own (cores), mean | 3.24 | 3.207 | 3.057 | 3.038 | 2.788 | 2.734 | 2.702 | 2.652 | 3.086 | 3.031 | 2.764 | 2.702 |
| host CPU busy, the real machine under kind (%) | 93.15 | 93.11 | 88.58 | 88.6 | 81.12 | 80.21 | 78.2 | 77.58 | 90.06 | 90.16 | 81.09 | 81.92 |
| organism work | 2.18e+11 | 2.18e+11 | 2.265e+11 | 2.265e+11 | 6.677e+11 | 6.677e+11 | 2.225e+11 | 2.225e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.579e+11 | 1.58e+11 | 2.012e+11 | 2.013e+11 | 1.103e+14 | 1.103e+14 | 5.684e+11 | 5.685e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.011 | 2.004 | 4.863 | 4.855 | 1.448 | 1.44 | 2.578 | 2.569 | 2.71 | 2.707 | 2.615 | 2.607 |
| organism work per energy | 1.381 | 1.38 | 1.126 | 1.125 | 0.006054 | 0.006054 | 0.3915 | 0.3914 | 0.006232 | 0.006232 | 0.012 | 0.012 |
| organism behind its window (s) | 0.09 | 0.09 | 0.05 | 0.07 | 0.07 | 0.05 | 0.06 | 0.06 | 0.22 | 0.29 | 0.3 | 0.31 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2900 | 1599 | -44.8% | -2167 to -433.8 | better |
| response time (ms), 99th percentile | 5443 | 3786 | -30.4% | -3198 to -116.5 | better |
| time over the response line (% of samples) | 60.85 | 41.37 | -32.0% | -22.74 to -16.21 | better |
| failed requests (%) | 32.73 | 28.18 | -13.9% | -6.621 to -2.479 | better |
| HPA replicas, mean | 9.835 | 9.819 | -0.2% | -0.065 to +0.03373 | better (inside the noise) |
| pods started | 2.7 | 2.9 | +7.4% | -0.5388 to +0.9388 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +9.579e-17 to +1.681e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.5 | 192.6 | +0.0% | -0.7078 to +0.859 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.5 | 192.6 | +0.0% | -0.7078 to +0.859 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.24 | 3.207 | -1.0% | -0.05045 to -0.01555 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 93.15 | 93.11 | -0.0% | -0.4251 to +0.3507 | shown, not judged (more or less is not better by itself) |
| organism work | 2.18e+11 | 2.18e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.579e+11 | 1.58e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.011 | 2.004 | -0.3% | -0.006761 to -0.006761 | better |
| organism work per energy | 1.381 | 1.38 | -0.1% | -0.0009278 to -0.0009278 | WORSE |
| organism behind its window (s) | 0.09 | 0.09 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2698 | 1420 | -47.4% | -2153 to -403.5 | better |
| response time (ms), 99th percentile | 5621 | 3997 | -28.9% | -3051 to -197.8 | better |
| time over the response line (% of samples) | 49.03 | 34.21 | -30.2% | -19.15 to -10.5 | better |
| failed requests (%) | 25.64 | 23.07 | -10.0% | -4.105 to -1.038 | better |
| HPA replicas, mean | 9.766 | 9.769 | +0.0% | -0.04968 to +0.05603 | WORSE (inside the noise) |
| pods started | 3.4 | 3.4 | +0.0% | -1.168 to +1.168 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191 | 191 | -0.0% | -1.192 to +1.074 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191 | 191 | -0.0% | -1.192 to +1.074 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.057 | 3.038 | -0.6% | -0.04328 to +0.00444 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.58 | 88.6 | +0.0% | -0.7033 to +0.7587 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.012e+11 | 2.013e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 4.863 | 4.855 | -0.2% | -0.008037 to -0.008037 | better |
| organism work per energy | 1.126 | 1.125 | -0.1% | -0.0005938 to -0.0005938 | WORSE |
| organism behind its window (s) | 0.05 | 0.07 | +40.0% | -0.02524 to +0.06524 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 3, worse on 0, inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2118 | 926 | -56.3% | -1892 to -493 | better |
| response time (ms), 99th percentile | 4141 | 2976 | -28.1% | -2543 to +213.8 | better (inside the noise) |
| time over the response line (% of samples) | 38.05 | 26.06 | -31.5% | -18.01 to -5.971 | better |
| failed requests (%) | 20.74 | 20.08 | -3.2% | -1.5 to +0.1821 | better (inside the noise) |
| HPA replicas, mean | 9.722 | 9.718 | -0.0% | -0.05908 to +0.05079 | better (inside the noise) |
| pods started | 3.8 | 3.9 | +2.6% | -0.7564 to +0.9564 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.985e-16 to +8.985e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 188 | 187.7 | -0.2% | -0.8715 to +0.1623 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188 | 187.7 | -0.2% | -0.8715 to +0.1623 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.788 | 2.734 | -1.9% | -0.09224 to -0.01508 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.12 | 80.21 | -1.1% | -1.877 to +0.06471 | shown, not judged (more or less is not better by itself) |
| organism work | 6.677e+11 | 6.677e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.448 | 1.44 | -0.6% | -0.008511 to -0.008511 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -5.827e-09 to -5.827e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.07 | 0.05 | -28.6% | -0.06524 to +0.02524 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3187 | 1660 | -47.9% | -2878 to -174.3 | better |
| response time (ms), 99th percentile | 4780 | 3723 | -22.1% | -2018 to -95.34 | better |
| time over the response line (% of samples) | 41.49 | 30.09 | -27.5% | -18.14 to -4.667 | better |
| failed requests (%) | 22.89 | 21.65 | -5.4% | -4.382 to +1.896 | better (inside the noise) |
| HPA replicas, mean | 9.642 | 9.696 | +0.6% | -0.01448 to +0.1215 | WORSE (inside the noise) |
| pods started | 5 | 4.3 | -14.0% | -1.871 to +0.4705 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.159e-15 to +4.484e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.2 | 187 | -0.1% | -1.143 to +0.6601 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.2 | 187 | -0.1% | -1.143 to +0.6601 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.702 | 2.652 | -1.8% | -0.08521 to -0.01406 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.2 | 77.58 | -0.8% | -1.943 to +0.6983 | shown, not judged (more or less is not better by itself) |
| organism work | 2.225e+11 | 2.225e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.684e+11 | 5.685e+11 | +0.0% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.578 | 2.569 | -0.3% | -0.008527 to -0.008527 | better |
| organism work per energy | 0.3915 | 0.3914 | -0.0% | -7.311e-05 to -7.311e-05 | WORSE |
| organism behind its window (s) | 0.06 | 0.06 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3429 | 1980 | -42.3% | -2592 to -307 | better |
| response time (ms), 99th percentile | 6221 | 4634 | -25.5% | -2888 to -284.9 | better |
| time over the response line (% of samples) | 58.63 | 48.51 | -17.3% | -14.31 to -5.928 | better |
| failed requests (%) | 37.74 | 36.04 | -4.5% | -3.661 to +0.2452 | better (inside the noise) |
| HPA replicas, mean | 9.784 | 9.796 | +0.1% | -0.006554 to +0.03008 | WORSE (inside the noise) |
| pods started | 3.4 | 3.2 | -5.9% | -0.6524 to +0.2524 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.725e-16 to +1.738e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191.1 | 190.7 | -0.2% | -1.461 to +0.6818 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.1 | 190.7 | -0.2% | -1.461 to +0.6818 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.086 | 3.031 | -1.8% | -0.07292 to -0.03695 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 90.06 | 90.16 | +0.1% | -0.3758 to +0.5793 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.71 | 2.707 | -0.1% | -0.003646 to -0.003646 | better |
| organism work per energy | 0.006232 | 0.006232 | -0.0% | -5.971e-09 to -5.971e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.22 | 0.29 | +31.8% | -0.0369 to +0.1769 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2304 | 1195 | -48.1% | -1942 to -276.7 | better |
| response time (ms), 99th percentile | 4405 | 4021 | -8.7% | -1560 to +792.9 | better (inside the noise) |
| time over the response line (% of samples) | 41.47 | 26.95 | -35.0% | -21.66 to -7.386 | better |
| failed requests (%) | 18.24 | 16.39 | -10.1% | -3.877 to +0.1777 | better (inside the noise) |
| HPA replicas, mean | 9.746 | 9.748 | +0.0% | -0.05524 to +0.06099 | WORSE (inside the noise) |
| pods started | 3.8 | 3.7 | -2.6% | -1.08 to +0.8802 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.4 | 187.2 | -0.6% | -2.423 to +0.01035 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.4 | 187.2 | -0.6% | -2.423 to +0.01035 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.764 | 2.702 | -2.3% | -0.09676 to -0.02811 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.09 | 81.92 | +1.0% | -0.05973 to +1.707 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +4.246e+08 to +4.246e+08 | WORSE |
| organism time over the line (% of steps) | 2.615 | 2.607 | -0.3% | -0.007918 to -0.007918 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -4.582e-08 to -4.582e-08 | WORSE |
| organism behind its window (s) | 0.3 | 0.31 | +3.3% | -0.08204 to +0.102 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
