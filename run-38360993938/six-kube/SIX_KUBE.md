# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2290 | 1074 | 2426 | 1516 | 2668 | 1653 | 3392 | 2396 | 2329 | 1691 | 1829 | 1067 |
| response time (ms), 99th percentile | 4645 | 2970 | 4689 | 3807 | 5478 | 4741 | 5820 | 4713 | 4544 | 4102 | 4045 | 2885 |
| time over the response line (% of samples) | 47.15 | 29.92 | 44.13 | 31.35 | 48.33 | 36.34 | 51.04 | 39.1 | 44.36 | 34.15 | 43.09 | 29.82 |
| failed requests (%) | 23.58 | 21 | 24.44 | 22.09 | 29.76 | 27.23 | 29.91 | 27.79 | 25.7 | 23.91 | 20.65 | 19.13 |
| HPA replicas, mean | 9.733 | 9.775 | 9.703 | 9.731 | 9.731 | 9.753 | 9.761 | 9.769 | 9.74 | 9.742 | 9.742 | 9.77 |
| pods started | 4.122 | 3.439 | 4.195 | 3.829 | 3.732 | 3.439 | 3.61 | 3.341 | 3.732 | 3.829 | 3.732 | 3.439 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 189.8 | 189.7 | 189.9 | 189.8 | 190.1 | 189.8 | 190.3 | 190.1 | 189.2 | 188.2 | 188.9 | 188 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.8 | 189.7 | 189.9 | 189.8 | 190.1 | 189.8 | 190.3 | 190.1 | 189.2 | 188.2 | 188.9 | 188 |
| CPU used with Omni's own (cores), mean | 2.956 | 2.914 | 2.918 | 2.879 | 2.945 | 2.92 | 2.989 | 2.941 | 2.829 | 2.77 | 2.814 | 2.751 |
| host CPU busy, the real machine under kind (%) | 85.14 | 84.89 | 84.89 | 84.33 | 85.83 | 85.9 | 86.3 | 85.89 | 82.94 | 82.88 | 82.79 | 83.93 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.07073 | 0.07073 | 0.04878 | 0.05854 | 0.06829 | 0.07073 | 0.07073 | 0.07317 | 0.2098 | 0.2098 | 0.3195 | 0.3756 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 6, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2290 | 1074 | -53.1% | -1509 to -923.5 | better |
| response time (ms), 99th percentile | 4645 | 2970 | -36.1% | -2219 to -1131 | better |
| time over the response line (% of samples) | 47.15 | 29.92 | -36.5% | -19.89 to -14.56 | better |
| failed requests (%) | 23.58 | 21 | -11.0% | -3.452 to -1.717 | better |
| HPA replicas, mean | 9.733 | 9.775 | +0.4% | +0.0154 to +0.06798 | WORSE |
| pods started | 4.122 | 3.439 | -16.6% | -1.154 to -0.2115 | better |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.94e-16 to +3.94e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 189.8 | 189.7 | -0.1% | -0.3956 to +0.1835 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.8 | 189.7 | -0.1% | -0.3956 to +0.1835 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.956 | 2.914 | -1.4% | -0.05271 to -0.03281 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.14 | 84.89 | -0.3% | -0.5053 to +0.005784 | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | WORSE |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | WORSE |
| organism behind its window (s) | 0.07073 | 0.07073 | +0.0% | -0.01369 to +0.01369 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2426 | 1516 | -37.5% | -1179 to -639.8 | better |
| response time (ms), 99th percentile | 4689 | 3807 | -18.8% | -1350 to -413.5 | better |
| time over the response line (% of samples) | 44.13 | 31.35 | -29.0% | -14.64 to -10.93 | better |
| failed requests (%) | 24.44 | 22.09 | -9.6% | -3.189 to -1.511 | better |
| HPA replicas, mean | 9.703 | 9.731 | +0.3% | -0.004582 to +0.06059 | WORSE (inside the noise) |
| pods started | 4.195 | 3.829 | -8.7% | -0.8905 to +0.1588 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.838e-16 to +3.405e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.9 | 189.8 | -0.0% | -0.4154 to +0.2652 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.9 | 189.8 | -0.0% | -0.4154 to +0.2652 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.918 | 2.879 | -1.3% | -0.05448 to -0.02231 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.89 | 84.33 | -0.7% | -1.048 to -0.06978 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | WORSE |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | better |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | WORSE |
| organism behind its window (s) | 0.04878 | 0.05854 | +20.0% | -0.009366 to +0.02888 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 5, worse on 0, inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2668 | 1653 | -38.0% | -1357 to -672.8 | better |
| response time (ms), 99th percentile | 5478 | 4741 | -13.5% | -1461 to -13.19 | better |
| time over the response line (% of samples) | 48.33 | 36.34 | -24.8% | -14.05 to -9.927 | better |
| failed requests (%) | 29.76 | 27.23 | -8.5% | -3.302 to -1.758 | better |
| HPA replicas, mean | 9.731 | 9.753 | +0.2% | -0.002731 to +0.04538 | WORSE (inside the noise) |
| pods started | 3.732 | 3.439 | -7.8% | -0.6433 to +0.05796 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.161e-16 to +3.894e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.1 | 189.8 | -0.1% | -0.5412 to +0.06792 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.1 | 189.8 | -0.1% | -0.5412 to +0.06792 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.945 | 2.92 | -0.9% | -0.03951 to -0.01066 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.83 | 85.9 | +0.1% | -0.255 to +0.3869 | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | better |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.06829 | 0.07073 | +3.6% | -0.00591 to +0.01079 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3392 | 2396 | -29.4% | -1418 to -573.7 | better |
| response time (ms), 99th percentile | 5820 | 4713 | -19.0% | -1534 to -679.7 | better |
| time over the response line (% of samples) | 51.04 | 39.1 | -23.4% | -13.91 to -9.971 | better |
| failed requests (%) | 29.91 | 27.79 | -7.1% | -3.038 to -1.198 | better |
| HPA replicas, mean | 9.761 | 9.769 | +0.1% | -0.01488 to +0.0315 | WORSE (inside the noise) |
| pods started | 3.61 | 3.341 | -7.4% | -0.7067 to +0.1701 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.274e-16 to +4.874e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.3 | 190.1 | -0.1% | -0.556 to +0.1411 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.3 | 190.1 | -0.1% | -0.556 to +0.1411 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.989 | 2.941 | -1.6% | -0.06042 to -0.03428 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.3 | 85.89 | -0.5% | -0.7778 to -0.03652 | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | WORSE |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | better |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | WORSE |
| organism behind its window (s) | 0.07073 | 0.07317 | +3.4% | -0.008357 to +0.01323 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 7, worse on 0, inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2329 | 1691 | -27.4% | -962.9 to -314.3 | better |
| response time (ms), 99th percentile | 4544 | 4102 | -9.7% | -855.7 to -28.57 | better |
| time over the response line (% of samples) | 44.36 | 34.15 | -23.0% | -12.79 to -7.639 | better |
| failed requests (%) | 25.7 | 23.91 | -6.9% | -2.695 to -0.8752 | better |
| HPA replicas, mean | 9.74 | 9.742 | +0.0% | -0.01992 to +0.02417 | WORSE (inside the noise) |
| pods started | 3.732 | 3.829 | +2.6% | -0.2568 to +0.4519 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.271e-16 to +7.719e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.2 | 188.2 | -0.5% | -1.319 to -0.5619 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.2 | 188.2 | -0.5% | -1.319 to -0.5619 | better |
| CPU used with Omni's own (cores), mean | 2.829 | 2.77 | -2.1% | -0.06804 to -0.05106 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.94 | 82.88 | -0.1% | -0.3499 to +0.2131 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | better |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.2098 | 0.2098 | +0.0% | -0.03749 to +0.03749 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 7, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1829 | 1067 | -41.7% | -983.2 to -540.1 | better |
| response time (ms), 99th percentile | 4045 | 2885 | -28.7% | -1692 to -629.1 | better |
| time over the response line (% of samples) | 43.09 | 29.82 | -30.8% | -15.54 to -10.99 | better |
| failed requests (%) | 20.65 | 19.13 | -7.3% | -2.272 to -0.7619 | better |
| HPA replicas, mean | 9.742 | 9.77 | +0.3% | +0.007352 to +0.04936 | WORSE |
| pods started | 3.732 | 3.439 | -7.8% | -0.6628 to +0.07746 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.912e-16 to +5.079e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.9 | 188 | -0.5% | -1.317 to -0.434 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.9 | 188 | -0.5% | -1.317 to -0.434 | better |
| CPU used with Omni's own (cores), mean | 2.814 | 2.751 | -2.3% | -0.07864 to -0.04814 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.79 | 83.93 | +1.4% | +0.773 to +1.517 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | WORSE |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | WORSE |
| organism behind its window (s) | 0.3195 | 0.3756 | +17.6% | +0.005314 to +0.1069 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
