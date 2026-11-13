# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2394 | 945.9 | 2850 | 1667 | 2306 | 1359 | 3041 | 2038 | 3335 | 1975 | 2217 | 1253 |
| response time (ms), 99th percentile | 4687 | 3075 | 5626 | 3994 | 4840 | 3591 | 5159 | 4287 | 5702 | 4585 | 4602 | 3361 |
| time over the response line (% of samples) | 43.52 | 26.17 | 48.02 | 36.29 | 44.19 | 31.58 | 50.07 | 37.15 | 53.97 | 42.88 | 45.71 | 32.72 |
| failed requests (%) | 20.45 | 18.34 | 29.09 | 26.5 | 25.63 | 23.15 | 29.04 | 26.76 | 33.34 | 31.88 | 23.17 | 21.6 |
| HPA replicas, mean | 9.7 | 9.733 | 9.749 | 9.755 | 9.691 | 9.72 | 9.739 | 9.752 | 9.772 | 9.788 | 9.758 | 9.763 |
| pods started | 4.537 | 4.024 | 3.415 | 3.488 | 4.171 | 3.927 | 3.878 | 3.634 | 3.439 | 3.244 | 3.415 | 3.537 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 189 | 188.6 | 190.2 | 190 | 189.3 | 188.9 | 189.8 | 189.5 | 190.6 | 189.9 | 189 | 188 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189 | 188.6 | 190.2 | 190 | 189.3 | 188.9 | 189.8 | 189.5 | 190.6 | 189.9 | 189 | 188 |
| CPU used with Omni's own (cores), mean | 2.863 | 2.819 | 2.956 | 2.922 | 2.866 | 2.825 | 2.956 | 2.911 | 2.983 | 2.936 | 2.847 | 2.772 |
| host CPU busy, the real machine under kind (%) | 82.48 | 82.04 | 86.22 | 85.88 | 83.45 | 83.02 | 85.08 | 84.79 | 87.06 | 87.32 | 83.74 | 84.69 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.06829 | 0.06829 | 0.06585 | 0.07317 | 0.05122 | 0.06829 | 0.08049 | 0.07317 | 0.1951 | 0.2317 | 0.3415 | 0.3561 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 8, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 0

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2394 | 945.9 | -60.5% | -1839 to -1058 | better |
| response time (ms), 99th percentile | 4687 | 3075 | -34.4% | -2213 to -1010 | better |
| time over the response line (% of samples) | 43.52 | 26.17 | -39.9% | -20.3 to -14.39 | better |
| failed requests (%) | 20.45 | 18.34 | -10.3% | -2.904 to -1.311 | better |
| HPA replicas, mean | 9.7 | 9.733 | +0.3% | +0.01077 to +0.05639 | WORSE |
| pods started | 4.537 | 4.024 | -11.3% | -0.9178 to -0.1066 | better |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.746e-16 to +4.179e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189 | 188.6 | -0.2% | -0.6768 to -0.1224 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189 | 188.6 | -0.2% | -0.6768 to -0.1224 | better |
| CPU used with Omni's own (cores), mean | 2.863 | 2.819 | -1.5% | -0.05484 to -0.03347 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.48 | 82.04 | -0.5% | -0.7272 to -0.1494 | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | WORSE |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | WORSE |
| organism behind its window (s) | 0.06829 | 0.06829 | +0.0% | -0.01677 to +0.01677 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2850 | 1667 | -41.5% | -1575 to -790.8 | better |
| response time (ms), 99th percentile | 5626 | 3994 | -29.0% | -2220 to -1044 | better |
| time over the response line (% of samples) | 48.02 | 36.29 | -24.4% | -13.4 to -10.05 | better |
| failed requests (%) | 29.09 | 26.5 | -8.9% | -3.426 to -1.754 | better |
| HPA replicas, mean | 9.749 | 9.755 | +0.1% | -0.01712 to +0.02838 | WORSE (inside the noise) |
| pods started | 3.415 | 3.488 | +2.1% | -0.3103 to +0.4567 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.986e-16 to +3.986e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 190.2 | 190 | -0.1% | -0.5478 to +0.07939 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.2 | 190 | -0.1% | -0.5478 to +0.07939 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.956 | 2.922 | -1.1% | -0.04608 to -0.02156 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.22 | 85.88 | -0.4% | -0.6964 to -0.0001225 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | WORSE |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | better |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | WORSE |
| organism behind its window (s) | 0.06585 | 0.07317 | +11.1% | -0.005286 to +0.01992 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 7, worse on 1 (HPA replicas, mean), inside the noise on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2306 | 1359 | -41.1% | -1214 to -680.6 | better |
| response time (ms), 99th percentile | 4840 | 3591 | -25.8% | -1872 to -624.5 | better |
| time over the response line (% of samples) | 44.19 | 31.58 | -28.5% | -14.93 to -10.28 | better |
| failed requests (%) | 25.63 | 23.15 | -9.7% | -3.218 to -1.737 | better |
| HPA replicas, mean | 9.691 | 9.72 | +0.3% | +0.006041 to +0.05116 | WORSE |
| pods started | 4.171 | 3.927 | -5.8% | -0.6476 to +0.1598 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.674e-18 to +6.566e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.3 | 188.9 | -0.2% | -0.7195 to -0.07578 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.3 | 188.9 | -0.2% | -0.7195 to -0.07578 | better |
| CPU used with Omni's own (cores), mean | 2.866 | 2.825 | -1.4% | -0.05338 to -0.02895 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 83.45 | 83.02 | -0.5% | -0.7907 to -0.07456 | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | better |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.05122 | 0.06829 | +33.3% | +0.0004442 to +0.0337 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3041 | 2038 | -33.0% | -1405 to -601.8 | better |
| response time (ms), 99th percentile | 5159 | 4287 | -16.9% | -1385 to -359.3 | better |
| time over the response line (% of samples) | 50.07 | 37.15 | -25.8% | -15.06 to -10.78 | better |
| failed requests (%) | 29.04 | 26.76 | -7.9% | -3.141 to -1.421 | better |
| HPA replicas, mean | 9.739 | 9.752 | +0.1% | -0.01242 to +0.03703 | WORSE (inside the noise) |
| pods started | 3.878 | 3.634 | -6.3% | -0.6756 to +0.1878 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.664e-16 to +5.13e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 189.8 | 189.5 | -0.2% | -0.7018 to +0.02595 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189.8 | 189.5 | -0.2% | -0.7018 to +0.02595 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.956 | 2.911 | -1.5% | -0.05568 to -0.03455 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.08 | 84.79 | -0.3% | -0.5651 to -0.02156 | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | WORSE |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | better |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | WORSE |
| organism behind its window (s) | 0.08049 | 0.07317 | -9.1% | -0.0179 to +0.003265 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 7, worse on 0, inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3335 | 1975 | -40.8% | -1846 to -872.9 | better |
| response time (ms), 99th percentile | 5702 | 4585 | -19.6% | -1674 to -560.2 | better |
| time over the response line (% of samples) | 53.97 | 42.88 | -20.6% | -13.42 to -8.77 | better |
| failed requests (%) | 33.34 | 31.88 | -4.4% | -2.49 to -0.4468 | better |
| HPA replicas, mean | 9.772 | 9.788 | +0.2% | -0.01285 to +0.04321 | WORSE (inside the noise) |
| pods started | 3.439 | 3.244 | -5.7% | -0.6451 to +0.2549 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.666e-16 to +5.266e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.6 | 189.9 | -0.3% | -1.064 to -0.2471 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.6 | 189.9 | -0.3% | -1.064 to -0.2471 | better |
| CPU used with Omni's own (cores), mean | 2.983 | 2.936 | -1.6% | -0.06133 to -0.03296 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 87.06 | 87.32 | +0.3% | -0.07328 to +0.5997 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | better |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.1951 | 0.2317 | +18.7% | -0.007111 to +0.08028 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2217 | 1253 | -43.5% | -1237 to -693 | better |
| response time (ms), 99th percentile | 4602 | 3361 | -27.0% | -1835 to -646.4 | better |
| time over the response line (% of samples) | 45.71 | 32.72 | -28.4% | -15.36 to -10.62 | better |
| failed requests (%) | 23.17 | 21.6 | -6.8% | -2.267 to -0.8674 | better |
| HPA replicas, mean | 9.758 | 9.763 | +0.1% | -0.02251 to +0.03229 | WORSE (inside the noise) |
| pods started | 3.415 | 3.537 | +3.6% | -0.3011 to +0.545 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.439e-16 to +3.439e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 189 | 188 | -0.5% | -1.483 to -0.5653 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 189 | 188 | -0.5% | -1.483 to -0.5653 | better |
| CPU used with Omni's own (cores), mean | 2.847 | 2.772 | -2.6% | -0.09056 to -0.0603 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 83.74 | 84.69 | +1.1% | +0.5335 to +1.372 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | WORSE |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | WORSE |
| organism behind its window (s) | 0.3415 | 0.3561 | +4.3% | -0.03207 to +0.06134 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
