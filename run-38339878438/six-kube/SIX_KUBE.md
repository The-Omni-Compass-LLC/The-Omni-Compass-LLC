# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1529 | 792.2 | 2541 | 1514 | 2462 | 1703 | 1417 | 943.1 | 2628 | 1961 | 1697 | 962.5 |
| response time (ms), 99th percentile | 3073 | 2261 | 4436 | 3347 | 5767 | 5818 | 2912 | 2164 | 4716 | 3923 | 3570 | 2301 |
| time over the response line (% of samples) | 32.44 | 20.78 | 43.22 | 30.39 | 43.7 | 29.28 | 24.02 | 18.95 | 46.98 | 41.14 | 34.71 | 27.35 |
| failed requests (%) | 15.91 | 14.55 | 26.07 | 23.68 | 21.5 | 19.11 | 14.33 | 13.96 | 32.77 | 31.4 | 19.84 | 18.77 |
| HPA replicas, mean | 9.625 | 9.658 | 9.695 | 9.723 | 9.696 | 9.75 | 9.607 | 9.601 | 9.688 | 9.707 | 9.68 | 9.695 |
| pods started | 5.5 | 4.8 | 4 | 3.6 | 4.2 | 3.6 | 5.2 | 5.4 | 4.5 | 4.3 | 4.3 | 4 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.4 | 188.7 | 188.5 | 190 | 189.5 | 183.7 | 182.7 | 187.9 | 187.2 | 185.5 | 184.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.4 | 188.7 | 188.5 | 190 | 189.5 | 183.7 | 182.7 | 187.9 | 187.2 | 185.5 | 184.2 |
| CPU used with Omni's own (cores), mean | 2.549 | 2.496 | 2.821 | 2.778 | 2.979 | 2.929 | 2.29 | 2.209 | 2.744 | 2.706 | 2.481 | 2.415 |
| host CPU busy, the real machine under kind (%) | 73.68 | 73.13 | 82.52 | 81.85 | 85.73 | 85.11 | 66.93 | 65.25 | 80.62 | 80.95 | 73.28 | 74.26 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.05 | 0.04 | 0.04 | 0.07 | 0.05 | 0.05 | 0.03 | 0.03 | 0.21 | 0.16 | 0.27 | 0.26 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1529 | 792.2 | -48.2% | -1283 to -189.7 | better |
| response time (ms), 99th percentile | 3073 | 2261 | -26.4% | -2528 to +905 | better (inside the noise) |
| time over the response line (% of samples) | 32.44 | 20.78 | -36.0% | -19.11 to -4.221 | better |
| failed requests (%) | 15.91 | 14.55 | -8.5% | -2.792 to +0.08474 | better (inside the noise) |
| HPA replicas, mean | 9.625 | 9.658 | +0.3% | -0.02692 to +0.09148 | WORSE (inside the noise) |
| pods started | 5.5 | 4.8 | -12.7% | -1.595 to +0.1953 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.4 | -0.3% | -1.426 to +0.3132 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.4 | -0.3% | -1.426 to +0.3132 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.549 | 2.496 | -2.1% | -0.09193 to -0.0134 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.68 | 73.13 | -0.7% | -1.432 to +0.3333 | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | WORSE |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | WORSE |
| organism behind its window (s) | 0.05 | 0.04 | -20.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2541 | 1514 | -40.4% | -1914 to -140.6 | better |
| response time (ms), 99th percentile | 4436 | 3347 | -24.5% | -2463 to +285.5 | better (inside the noise) |
| time over the response line (% of samples) | 43.22 | 30.39 | -29.7% | -18.09 to -7.562 | better |
| failed requests (%) | 26.07 | 23.68 | -9.1% | -4.291 to -0.4766 | better |
| HPA replicas, mean | 9.695 | 9.723 | +0.3% | -0.03788 to +0.0951 | WORSE (inside the noise) |
| pods started | 4 | 3.6 | -10.0% | -1.528 to +0.7285 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.805e-16 to +8.91e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.7 | 188.5 | -0.1% | -0.7553 to +0.2253 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.7 | 188.5 | -0.1% | -0.7553 to +0.2253 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.821 | 2.778 | -1.5% | -0.07277 to -0.01239 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 82.52 | 81.85 | -0.8% | -1.435 to +0.09321 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | WORSE |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | better |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | WORSE |
| organism behind its window (s) | 0.04 | 0.07 | +75.0% | -0.01828 to +0.07828 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 4, worse on 1 (HPA replicas, mean), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2462 | 1703 | -30.8% | -1385 to -132.1 | better |
| response time (ms), 99th percentile | 5767 | 5818 | +0.9% | -1458 to +1560 | WORSE (inside the noise) |
| time over the response line (% of samples) | 43.7 | 29.28 | -33.0% | -19.95 to -8.881 | better |
| failed requests (%) | 21.5 | 19.11 | -11.1% | -3.988 to -0.7992 | better |
| HPA replicas, mean | 9.696 | 9.75 | +0.6% | +0.0169 to +0.09093 | WORSE |
| pods started | 4.2 | 3.6 | -14.3% | -1.203 to +0.0032 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.88e-16 to +6.104e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190 | 189.5 | -0.3% | -1.52 to +0.502 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190 | 189.5 | -0.3% | -1.52 to +0.502 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.979 | 2.929 | -1.7% | -0.07998 to -0.01925 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.73 | 85.11 | -0.7% | -1.509 to +0.2788 | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | better |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.05 | 0.05 | +0.0% | -0.03372 to +0.03372 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1417 | 943.1 | -33.4% | -1199 to +252.5 | better (inside the noise) |
| response time (ms), 99th percentile | 2912 | 2164 | -25.7% | -2074 to +578.2 | better (inside the noise) |
| time over the response line (% of samples) | 24.02 | 18.95 | -21.1% | -8.105 to -2.029 | better |
| failed requests (%) | 14.33 | 13.96 | -2.5% | -1.191 to +0.4599 | better (inside the noise) |
| HPA replicas, mean | 9.607 | 9.601 | -0.1% | -0.07099 to +0.05784 | better (inside the noise) |
| pods started | 5.2 | 5.4 | +3.8% | -0.7417 to +1.142 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.47e-16 to +1.358e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 182.7 | -0.5% | -1.757 to -0.2227 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 182.7 | -0.5% | -1.757 to -0.2227 | better |
| CPU used with Omni's own (cores), mean | 2.29 | 2.209 | -3.5% | -0.1224 to -0.03949 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 66.93 | 65.25 | -2.5% | -3.23 to -0.1202 | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | WORSE |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | better |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | WORSE |
| organism behind its window (s) | 0.03 | 0.03 | +0.0% | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 2, worse on 0, inside the noise on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2628 | 1961 | -25.4% | -1510 to +177.2 | better (inside the noise) |
| response time (ms), 99th percentile | 4716 | 3923 | -16.8% | -1598 to +11.86 | better (inside the noise) |
| time over the response line (% of samples) | 46.98 | 41.14 | -12.4% | -9.303 to -2.389 | better |
| failed requests (%) | 32.77 | 31.4 | -4.2% | -4.098 to +1.356 | better (inside the noise) |
| HPA replicas, mean | 9.688 | 9.707 | +0.2% | -0.04736 to +0.08681 | WORSE (inside the noise) |
| pods started | 4.5 | 4.3 | -4.4% | -1.308 to +0.9081 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.286e-16 to +9.063e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.9 | 187.2 | -0.4% | -1.861 to +0.3452 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.9 | 187.2 | -0.4% | -1.861 to +0.3452 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.744 | 2.706 | -1.4% | -0.06798 to -0.007245 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 80.62 | 80.95 | +0.4% | -0.3876 to +1.046 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | better |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.21 | 0.16 | -23.8% | -0.1343 to +0.0343 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1697 | 962.5 | -43.3% | -1272 to -196 | better |
| response time (ms), 99th percentile | 3570 | 2301 | -35.5% | -2720 to +182.6 | better (inside the noise) |
| time over the response line (% of samples) | 34.71 | 27.35 | -21.2% | -12.3 to -2.41 | better |
| failed requests (%) | 19.84 | 18.77 | -5.4% | -2.319 to +0.1745 | better (inside the noise) |
| HPA replicas, mean | 9.68 | 9.695 | +0.2% | -0.01493 to +0.04615 | WORSE (inside the noise) |
| pods started | 4.3 | 4 | -7.0% | -0.6455 to +0.04553 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.046e-16 to +1.193e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 184.2 | -0.7% | -2.088 to -0.4195 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.5 | 184.2 | -0.7% | -2.088 to -0.4195 | better |
| CPU used with Omni's own (cores), mean | 2.481 | 2.415 | -2.6% | -0.09947 to -0.03134 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.28 | 74.26 | +1.3% | -0.05803 to +2.025 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | WORSE |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | WORSE |
| organism behind its window (s) | 0.27 | 0.26 | -3.7% | -0.09564 to +0.07564 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
