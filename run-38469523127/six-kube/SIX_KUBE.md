# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2207 | 3104 | 2622 | 2844 | 2664 | 3036 | 2633 | 3356 | 3184 | 3589 | 2840 | 3511 |
| response time (ms), 99th percentile | 4832 | 5560 | 5029 | 5356 | 5223 | 5861 | 5191 | 5598 | 5639 | 5912 | 5407 | 6315 |
| time over the response line (% of samples) | 42.12 | 37.85 | 44.38 | 42.26 | 40.88 | 39.67 | 42.64 | 38.71 | 47.68 | 44.45 | 46.17 | 43.27 |
| failed requests (%) | 23.93 | 23.33 | 30.24 | 31.08 | 26.34 | 27.34 | 26.15 | 25.44 | 31.64 | 31.6 | 22.94 | 23.67 |
| HPA replicas, mean | 9.692 | 14.3 | 9.674 | 14.05 | 9.656 | 13.98 | 9.688 | 13.95 | 9.75 | 14.31 | 9.781 | 14.63 |
| pods started | 4.756 | 9.829 | 4.537 | 10.02 | 4.878 | 9.585 | 4.707 | 10.07 | 3.683 | 8.805 | 3.293 | 8.878 |
| worker nodes in service, mean | 6 | 5.998 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.4 | 184.1 | 184.4 | 184 | 184.7 | 183.7 | 183.9 | 184.3 | 184.5 | 185.4 | 185.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.3 | 184.1 | 184.4 | 184 | 184.7 | 183.7 | 183.9 | 184.3 | 184.5 | 185.4 | 185.3 |
| CPU used with Omni's own (cores), mean | 2.355 | 2.373 | 2.377 | 2.401 | 2.358 | 2.38 | 2.317 | 2.336 | 2.37 | 2.398 | 2.472 | 2.497 |
| host CPU busy, the real machine under kind (%) | 69.3 | 70.66 | 70.76 | 71.97 | 70.66 | 71.78 | 68.16 | 69.59 | 70.69 | 72.88 | 73.79 | 77.06 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.004878 | 0.02927 | 0 | 0.004878 | 0.004878 | 0.02195 | 0.01463 | 0.0122 | 0.09268 | 0.1122 | 0.1488 | 0.1927 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 5 (response time (ms), 95th percentile; response time (ms), 99th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2207 | 3104 | +40.6% | +479.7 to +1315 | higher |
| response time (ms), 99th percentile | 4832 | 5560 | +15.1% | +195.8 to +1261 | higher |
| time over the response line (% of samples) | 42.12 | 37.85 | -10.1% | -5.705 to -2.843 | lower |
| failed requests (%) | 23.93 | 23.33 | -2.5% | -1.312 to +0.1071 | lower (inside the noise) |
| HPA replicas, mean | 9.692 | 14.3 | +47.5% | +4.057 to +5.149 | higher |
| pods started | 4.756 | 9.829 | +106.7% | +4.344 to +5.802 | higher |
| worker nodes in service, mean | 6 | 5.998 | -0.0% | -0.004596 to +0.00149 | lower (inside the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.4 | +0.2% | -0.1177 to +0.817 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.3 | +0.2% | -0.1526 to +0.7888 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.355 | 2.373 | +0.8% | +0.01118 to +0.02486 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.3 | 70.66 | +2.0% | +1.153 to +1.561 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | higher |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | lower |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | lower |
| organism behind its window (s) | 0.004878 | 0.02927 | +500.0% | +0.007934 to +0.04085 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 4 (failed requests (%); HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2622 | 2844 | +8.5% | -268.3 to +713.1 | higher (inside the noise) |
| response time (ms), 99th percentile | 5029 | 5356 | +6.5% | -226.7 to +881.5 | higher (inside the noise) |
| time over the response line (% of samples) | 44.38 | 42.26 | -4.8% | -3.268 to -0.9681 | lower |
| failed requests (%) | 30.24 | 31.08 | +2.8% | +0.04603 to +1.634 | higher |
| HPA replicas, mean | 9.674 | 14.05 | +45.2% | +3.796 to +4.956 | higher |
| pods started | 4.537 | 10.02 | +121.0% | +4.735 to +6.241 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.955e-16 to +2.222e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.4 | +0.1% | -0.1498 to +0.6782 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.4 | +0.1% | -0.1498 to +0.6782 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.377 | 2.401 | +1.0% | +0.01744 to +0.02986 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.76 | 71.97 | +1.7% | +1.003 to +1.411 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | higher |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | lower |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | lower |
| organism behind its window (s) | 0 | 0.004878 | +0.00488 | -0.001798 to +0.01155 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 6 (response time (ms), 99th percentile; failed requests (%); HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), inside the noise on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2664 | 3036 | +14.0% | -111.5 to +855.6 | higher (inside the noise) |
| response time (ms), 99th percentile | 5223 | 5861 | +12.2% | +93.91 to +1182 | higher |
| time over the response line (% of samples) | 40.88 | 39.67 | -3.0% | -2.126 to -0.3028 | lower |
| failed requests (%) | 26.34 | 27.34 | +3.8% | +0.2968 to +1.707 | higher |
| HPA replicas, mean | 9.656 | 13.98 | +44.8% | +3.709 to +4.939 | higher |
| pods started | 4.878 | 9.585 | +96.5% | +3.908 to +5.506 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.87e-16 to +3.003e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 184.7 | +0.4% | +0.4516 to +1.092 | higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 184.7 | +0.4% | +0.4516 to +1.092 | higher |
| CPU used with Omni's own (cores), mean | 2.358 | 2.38 | +0.9% | +0.01388 to +0.0302 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.66 | 71.78 | +1.6% | +0.8982 to +1.346 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | lower |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.004878 | 0.02195 | +350.0% | +0.001918 to +0.03223 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 4 (response time (ms), 95th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2633 | 3356 | +27.4% | +258.9 to +1186 | higher |
| response time (ms), 99th percentile | 5191 | 5598 | +7.8% | -91.39 to +905.8 | higher (inside the noise) |
| time over the response line (% of samples) | 42.64 | 38.71 | -9.2% | -5.669 to -2.205 | lower |
| failed requests (%) | 26.15 | 25.44 | -2.7% | -1.741 to +0.3313 | lower (inside the noise) |
| HPA replicas, mean | 9.688 | 13.95 | +43.9% | +3.649 to +4.866 | higher |
| pods started | 4.707 | 10.07 | +114.0% | +4.487 to +6.244 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.53e-16 to +2.664e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.9 | +0.1% | -0.1767 to +0.5929 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.9 | +0.1% | -0.1767 to +0.5929 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.317 | 2.336 | +0.8% | +0.01204 to +0.02709 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.16 | 69.59 | +2.1% | +1.187 to +1.658 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | higher |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | lower |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | lower |
| organism behind its window (s) | 0.01463 | 0.0122 | -16.7% | -0.01847 to +0.0136 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3184 | 3589 | +12.7% | -36.14 to +845.4 | higher (inside the noise) |
| response time (ms), 99th percentile | 5639 | 5912 | +4.9% | -143.1 to +690.7 | higher (inside the noise) |
| time over the response line (% of samples) | 47.68 | 44.45 | -6.8% | -4.579 to -1.893 | lower |
| failed requests (%) | 31.64 | 31.6 | -0.1% | -0.9524 to +0.8747 | lower (inside the noise) |
| HPA replicas, mean | 9.75 | 14.31 | +46.8% | +4.02 to +5.096 | higher |
| pods started | 3.683 | 8.805 | +139.1% | +4.338 to +5.906 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.404e-16 to +2.971e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.5 | +0.1% | -0.2113 to +0.6072 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.5 | +0.1% | -0.2113 to +0.6072 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.37 | 2.398 | +1.2% | +0.01989 to +0.03675 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.69 | 72.88 | +3.1% | +1.908 to +2.458 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | lower |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.09268 | 0.1122 | +21.1% | +0.007231 to +0.03179 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 5 (response time (ms), 95th percentile; response time (ms), 99th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2840 | 3511 | +23.6% | +383.3 to +958.2 | higher |
| response time (ms), 99th percentile | 5407 | 6315 | +16.8% | +285.5 to +1531 | higher |
| time over the response line (% of samples) | 46.17 | 43.27 | -6.3% | -4.644 to -1.162 | lower |
| failed requests (%) | 22.94 | 23.67 | +3.2% | -0.1184 to +1.593 | higher (inside the noise) |
| HPA replicas, mean | 9.781 | 14.63 | +49.6% | +4.421 to +5.283 | higher |
| pods started | 3.293 | 8.878 | +169.6% | +4.864 to +6.306 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.376e-16 to +1.438e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.3 | -0.1% | -0.6149 to +0.333 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.3 | -0.1% | -0.6149 to +0.333 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.472 | 2.497 | +1.0% | +0.01746 to +0.03433 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.79 | 77.06 | +4.4% | +2.96 to +3.571 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | higher |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | lower |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | lower |
| organism behind its window (s) | 0.1488 | 0.1927 | +29.5% | +0.01564 to +0.07216 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
