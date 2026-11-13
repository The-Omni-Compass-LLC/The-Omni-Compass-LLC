# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2980 | 1474 | 2825 | 1282 | 3222 | 1640 | 3328 | 1892 | 3983 | 2745 | 2556 | 1639 |
| response time (ms), 99th percentile | 5460 | 4960 | 4766 | 4112 | 6594 | 3640 | 7013 | 5593 | 5883 | 5428 | 5758 | 4901 |
| time over the response line (% of samples) | 53.08 | 36.23 | 44.1 | 32.57 | 60.01 | 45.1 | 52.75 | 33.65 | 56.99 | 48.75 | 58.28 | 43.99 |
| failed requests (%) | 26.93 | 24.47 | 25.74 | 23.43 | 38.55 | 34.86 | 23.91 | 21.87 | 37.07 | 35.91 | 30.89 | 29.51 |
| HPA replicas, mean | 9.804 | 9.791 | 9.766 | 9.766 | 9.786 | 9.862 | 9.785 | 9.793 | 9.795 | 9.825 | 9.884 | 9.852 |
| pods started | 3 | 3.5 | 3.3 | 3.5 | 3.4 | 1.8 | 3.4 | 3.3 | 3.2 | 2.7 | 1.8 | 2.4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 192.1 | 191 | 189.4 | 188.7 | 192.9 | 192 | 193.1 | 192.1 | 190.4 | 190.3 | 192.7 | 191.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.1 | 191 | 189.4 | 188.7 | 192.9 | 192 | 193.1 | 192.1 | 190.4 | 190.3 | 192.7 | 191.5 |
| CPU used with Omni's own (cores), mean | 3.103 | 3.066 | 2.903 | 2.852 | 3.147 | 3.122 | 3.176 | 3.13 | 3.023 | 2.978 | 3.181 | 3.097 |
| host CPU busy, the real machine under kind (%) | 89.45 | 89.36 | 84.64 | 83.91 | 91.77 | 91.6 | 91.44 | 91.33 | 88.6 | 88.7 | 93.36 | 94.15 |
| organism work | 2.18e+11 | 2.18e+11 | 2.265e+11 | 2.265e+11 | 6.677e+11 | 6.677e+11 | 2.225e+11 | 2.225e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.579e+11 | 1.58e+11 | 2.012e+11 | 2.013e+11 | 1.103e+14 | 1.103e+14 | 5.684e+11 | 5.685e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.011 | 2.004 | 4.863 | 4.855 | 1.448 | 1.44 | 2.578 | 2.569 | 2.71 | 2.707 | 2.615 | 2.607 |
| organism work per energy | 1.381 | 1.38 | 1.126 | 1.125 | 0.006054 | 0.006054 | 0.3915 | 0.3914 | 0.006232 | 0.006232 | 0.012 | 0.012 |
| organism behind its window (s) | 0.11 | 0.09 | 0.09 | 0.06 | 0.13 | 0.1 | 0.12 | 0.14 | 0.25 | 0.2 | 0.41 | 0.49 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2980 | 1474 | -50.5% | -2557 to -454.8 | better |
| response time (ms), 99th percentile | 5460 | 4960 | -9.2% | -1729 to +727.8 | better (inside the noise) |
| time over the response line (% of samples) | 53.08 | 36.23 | -31.7% | -21.44 to -12.26 | better |
| failed requests (%) | 26.93 | 24.47 | -9.1% | -4.356 to -0.5471 | better |
| HPA replicas, mean | 9.804 | 9.791 | -0.1% | -0.0722 to +0.0457 | better (inside the noise) |
| pods started | 3 | 3.5 | +16.7% | -0.4685 to +1.469 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.227e-15 to +1.05e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.1 | 191 | -0.6% | -2.146 to -0.005786 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.1 | 191 | -0.6% | -2.146 to -0.005786 | better |
| CPU used with Omni's own (cores), mean | 3.103 | 3.066 | -1.2% | -0.04808 to -0.02474 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.45 | 89.36 | -0.1% | -0.4962 to +0.3112 | shown, not judged (more or less is not better by itself) |
| organism work | 2.18e+11 | 2.18e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.579e+11 | 1.58e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.011 | 2.004 | -0.3% | -0.006761 to -0.006761 | better |
| organism work per energy | 1.381 | 1.38 | -0.1% | -0.0009278 to -0.0009278 | WORSE |
| organism behind its window (s) | 0.11 | 0.09 | -18.2% | -0.07642 to +0.03642 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2825 | 1282 | -54.6% | -2585 to -500.2 | better |
| response time (ms), 99th percentile | 4766 | 4112 | -13.7% | -2106 to +798.1 | better (inside the noise) |
| time over the response line (% of samples) | 44.1 | 32.57 | -26.1% | -15.93 to -7.125 | better |
| failed requests (%) | 25.74 | 23.43 | -9.0% | -3.815 to -0.7995 | better |
| HPA replicas, mean | 9.766 | 9.766 | +0.0% | -0.07242 to +0.07302 | WORSE (inside the noise) |
| pods started | 3.3 | 3.5 | +6.1% | -1.097 to +1.497 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.277e-16 to +1.038e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.4 | 188.7 | -0.4% | -2.194 to +0.6443 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.4 | 188.7 | -0.4% | -2.194 to +0.6443 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.903 | 2.852 | -1.7% | -0.09389 to -0.006471 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.64 | 83.91 | -0.9% | -2.129 to +0.6596 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.012e+11 | 2.013e+11 | +0.1% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 4.863 | 4.855 | -0.2% | -0.008037 to -0.008037 | better |
| organism work per energy | 1.126 | 1.125 | -0.1% | -0.0005938 to -0.0005938 | WORSE |
| organism behind its window (s) | 0.09 | 0.06 | -33.3% | -0.06455 to +0.004553 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 8, worse on 1 (HPA replicas, mean), inside the noise on 0

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3222 | 1640 | -49.1% | -2777 to -387.9 | better |
| response time (ms), 99th percentile | 6594 | 3640 | -44.8% | -5046 to -864 | better |
| time over the response line (% of samples) | 60.01 | 45.1 | -24.8% | -19.22 to -10.6 | better |
| failed requests (%) | 38.55 | 34.86 | -9.6% | -5.942 to -1.436 | better |
| HPA replicas, mean | 9.786 | 9.862 | +0.8% | +0.01404 to +0.138 | WORSE |
| pods started | 3.4 | 1.8 | -47.1% | -2.728 to -0.4715 | better |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.417e-15 to +1.735e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.9 | 192 | -0.5% | -1.699 to -0.1069 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.9 | 192 | -0.5% | -1.699 to -0.1069 | better |
| CPU used with Omni's own (cores), mean | 3.147 | 3.122 | -0.8% | -0.03915 to -0.01046 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.77 | 91.6 | -0.2% | -0.5584 to +0.213 | shown, not judged (more or less is not better by itself) |
| organism work | 6.677e+11 | 6.677e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.448 | 1.44 | -0.6% | -0.008511 to -0.008511 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -5.827e-09 to -5.827e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.13 | 0.1 | -23.1% | -0.08889 to +0.02889 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3328 | 1892 | -43.1% | -2026 to -846.1 | better |
| response time (ms), 99th percentile | 7013 | 5593 | -20.2% | -2373 to -466.4 | better |
| time over the response line (% of samples) | 52.75 | 33.65 | -36.2% | -23.64 to -14.55 | better |
| failed requests (%) | 23.91 | 21.87 | -8.5% | -3.776 to -0.2944 | better |
| HPA replicas, mean | 9.785 | 9.793 | +0.1% | -0.06292 to +0.07897 | WORSE (inside the noise) |
| pods started | 3.4 | 3.3 | -2.9% | -1.241 to +1.041 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.066e-16 to +1.162e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 193.1 | 192.1 | -0.5% | -1.742 to -0.2037 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.1 | 192.1 | -0.5% | -1.742 to -0.2037 | better |
| CPU used with Omni's own (cores), mean | 3.176 | 3.13 | -1.5% | -0.07152 to -0.02185 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.44 | 91.33 | -0.1% | -0.5239 to +0.3139 | shown, not judged (more or less is not better by itself) |
| organism work | 2.225e+11 | 2.225e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.684e+11 | 5.685e+11 | +0.0% | +1.062e+08 to +1.062e+08 | WORSE |
| organism time over the line (% of steps) | 2.578 | 2.569 | -0.3% | -0.008527 to -0.008527 | better |
| organism work per energy | 0.3915 | 0.3914 | -0.0% | -7.311e-05 to -7.311e-05 | WORSE |
| organism behind its window (s) | 0.12 | 0.14 | +16.7% | -0.08003 to +0.12 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 3, worse on 0, inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3983 | 2745 | -31.1% | -2424 to -52.74 | better |
| response time (ms), 99th percentile | 5883 | 5428 | -7.7% | -2001 to +1090 | better (inside the noise) |
| time over the response line (% of samples) | 56.99 | 48.75 | -14.5% | -12.95 to -3.54 | better |
| failed requests (%) | 37.07 | 35.91 | -3.1% | -4.378 to +2.045 | better (inside the noise) |
| HPA replicas, mean | 9.795 | 9.825 | +0.3% | -0.01148 to +0.07183 | WORSE (inside the noise) |
| pods started | 3.2 | 2.7 | -15.6% | -1.273 to +0.2726 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.615e-16 to +4.062e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.4 | 190.3 | -0.1% | -1.067 to +0.7801 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.4 | 190.3 | -0.1% | -1.067 to +0.7801 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.023 | 2.978 | -1.5% | -0.06436 to -0.02739 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.6 | 88.7 | +0.1% | -0.4541 to +0.6602 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +1.062e+08 to +1.062e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.71 | 2.707 | -0.1% | -0.003646 to -0.003646 | better |
| organism work per energy | 0.006232 | 0.006232 | -0.0% | -5.971e-09 to -5.971e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.25 | 0.2 | -20.0% | -0.1273 to +0.02726 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2556 | 1639 | -35.9% | -1269 to -567.1 | better |
| response time (ms), 99th percentile | 5758 | 4901 | -14.9% | -2341 to +627 | better (inside the noise) |
| time over the response line (% of samples) | 58.28 | 43.99 | -24.5% | -17.41 to -11.17 | better |
| failed requests (%) | 30.89 | 29.51 | -4.5% | -2.906 to +0.146 | better (inside the noise) |
| HPA replicas, mean | 9.884 | 9.852 | -0.3% | -0.08762 to +0.02455 | better (inside the noise) |
| pods started | 1.8 | 2.4 | +33.3% | -0.3048 to +1.505 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.585e-16 to +9.69e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 192.7 | 191.5 | -0.7% | -2.522 to -0.02952 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 192.7 | 191.5 | -0.7% | -2.522 to -0.02952 | better |
| CPU used with Omni's own (cores), mean | 3.181 | 3.097 | -2.6% | -0.1125 to -0.0557 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 93.36 | 94.15 | +0.8% | +0.437 to +1.144 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +4.246e+08 to +4.246e+08 | WORSE |
| organism time over the line (% of steps) | 2.615 | 2.607 | -0.3% | -0.007918 to -0.007918 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -4.582e-08 to -4.582e-08 | WORSE |
| organism behind its window (s) | 0.41 | 0.49 | +19.5% | -0.138 to +0.298 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
