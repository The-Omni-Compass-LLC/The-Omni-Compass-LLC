# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2588 | 3308 | 2388 | 2431 | 2597 | 2506 | 2027 | 2949 | 2025 | 2181 | 2501 | 3276 |
| response time (ms), 99th percentile | 4906 | 6537 | 4719 | 4528 | 5207 | 5638 | 4012 | 4958 | 2952 | 2862 | 4455 | 5092 |
| time over the response line (% of samples) | 53.95 | 46.54 | 41.55 | 39.17 | 45.14 | 44.37 | 43.34 | 40.26 | 29.57 | 28.54 | 34.9 | 33.02 |
| failed requests (%) | 32.68 | 30.92 | 29.3 | 30.17 | 31.4 | 32.58 | 29.23 | 30.02 | 21.48 | 22.13 | 16.52 | 17.85 |
| HPA replicas, mean | 9.71 | 14.32 | 9.652 | 13.43 | 9.696 | 13.98 | 9.665 | 13.45 | 9.643 | 12.97 | 9.752 | 14.44 |
| pods started | 5 | 9.2 | 5.1 | 8.5 | 4.1 | 10.3 | 5 | 8.4 | 4.7 | 9.1 | 3.7 | 9.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.992 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.7 | 183.7 | 184.1 | 184.1 | 184.8 | 183.2 | 183.6 | 181.7 | 181.2 | 183.7 | 183.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.7 | 183.7 | 183.9 | 184.1 | 184.8 | 183.2 | 183.6 | 181.7 | 181.2 | 183.7 | 183.4 |
| CPU used with Omni's own (cores), mean | 2.465 | 2.486 | 2.296 | 2.323 | 2.379 | 2.4 | 2.275 | 2.284 | 2.071 | 2.088 | 2.307 | 2.338 |
| host CPU busy, the real machine under kind (%) | 72.85 | 74.29 | 68.79 | 70.07 | 70.94 | 71.92 | 67.21 | 68.33 | 62.12 | 63.69 | 68.91 | 72.5 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0.03 | 0 | 0.01 | 0 | 0 | 0.01 | 0.02 | 0.09 | 0.08 | 0.13 | 0.16 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2588 | 3308 | +27.8% | -85.19 to +1526 | higher (inside the noise) |
| response time (ms), 99th percentile | 4906 | 6537 | +33.3% | -547.6 to +3811 | higher (inside the noise) |
| time over the response line (% of samples) | 53.95 | 46.54 | -13.7% | -10.29 to -4.537 | lower |
| failed requests (%) | 32.68 | 30.92 | -5.4% | -2.759 to -0.7665 | lower |
| HPA replicas, mean | 9.71 | 14.32 | +47.4% | +3.263 to +5.948 | higher |
| pods started | 5 | 9.2 | +84.0% | +2.947 to +5.453 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.05e-15 to +1.405e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 185.7 | +0.2% | -0.7623 to +1.419 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 185.7 | +0.2% | -0.7623 to +1.419 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.465 | 2.486 | +0.9% | +0.008732 to +0.03334 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.85 | 74.29 | +2.0% | +1.196 to +1.679 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | higher |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | lower |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | lower |
| organism behind its window (s) | 0 | 0.03 | +0.03 | -0.004553 to +0.06455 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2388 | 2431 | +1.8% | -824 to +910.4 | higher (inside the noise) |
| response time (ms), 99th percentile | 4719 | 4528 | -4.1% | -1410 to +1027 | lower (inside the noise) |
| time over the response line (% of samples) | 41.55 | 39.17 | -5.7% | -4.756 to -0.01021 | lower |
| failed requests (%) | 29.3 | 30.17 | +3.0% | -1.148 to +2.884 | higher (inside the noise) |
| HPA replicas, mean | 9.652 | 13.43 | +39.1% | +1.91 to +5.639 | higher |
| pods started | 5.1 | 8.5 | +66.7% | +1.578 to +5.222 | higher |
| worker nodes in service, mean | 6 | 5.992 | -0.1% | -0.02754 to +0.01065 | lower (inside the noise) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.1 | +0.2% | -1.143 to +1.785 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.9 | +0.1% | -1.104 to +1.396 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.296 | 2.323 | +1.1% | +0.008462 to +0.04434 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.79 | 70.07 | +1.9% | +0.7 to +1.855 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | higher |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | lower |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | lower |
| organism behind its window (s) | 0 | 0.01 | +0.01 | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: lower on 1 (organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2597 | 2506 | -3.5% | -972.7 to +791.1 | lower (inside the noise) |
| response time (ms), 99th percentile | 5207 | 5638 | +8.3% | -667.5 to +1530 | higher (inside the noise) |
| time over the response line (% of samples) | 45.14 | 44.37 | -1.7% | -2.845 to +1.311 | lower (inside the noise) |
| failed requests (%) | 31.4 | 32.58 | +3.8% | -0.3806 to +2.742 | higher (inside the noise) |
| HPA replicas, mean | 9.696 | 13.98 | +44.2% | +2.8 to +5.766 | higher |
| pods started | 4.1 | 10.3 | +151.2% | +4.329 to +8.071 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.895e-16 to +2.566e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.8 | +0.4% | -0.238 to +1.639 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.8 | +0.4% | -0.238 to +1.639 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.379 | 2.4 | +0.9% | +0.0008369 to +0.04119 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.94 | 71.92 | +1.4% | +0.3695 to +1.588 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | lower |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: lower on 2 (organism time over the line (% of steps); organism work per energy), higher on 4 (response time (ms), 95th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2027 | 2949 | +45.5% | +101.7 to +1742 | higher |
| response time (ms), 99th percentile | 4012 | 4958 | +23.6% | -331.4 to +2223 | higher (inside the noise) |
| time over the response line (% of samples) | 43.34 | 40.26 | -7.1% | -8.334 to +2.185 | lower (inside the noise) |
| failed requests (%) | 29.23 | 30.02 | +2.7% | -1.779 to +3.357 | higher (inside the noise) |
| HPA replicas, mean | 9.665 | 13.45 | +39.2% | +1.969 to +5.606 | higher |
| pods started | 5 | 8.4 | +68.0% | +1.133 to +5.667 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.235e-16 to +4.235e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.6 | +0.3% | -0.6695 to +1.594 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.6 | +0.3% | -0.6695 to +1.594 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.275 | 2.284 | +0.4% | -0.008525 to +0.02527 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.21 | 68.33 | +1.7% | +0.2461 to +1.985 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | higher |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | lower |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | lower |
| organism behind its window (s) | 0.01 | 0.02 | +100.0% | -0.01262 to +0.03262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2025 | 2181 | +7.7% | -341.7 to +653.4 | higher (inside the noise) |
| response time (ms), 99th percentile | 2952 | 2862 | -3.0% | -508.4 to +329.2 | lower (inside the noise) |
| time over the response line (% of samples) | 29.57 | 28.54 | -3.5% | -1.899 to -0.1608 | lower |
| failed requests (%) | 21.48 | 22.13 | +3.0% | -0.7199 to +2.016 | higher (inside the noise) |
| HPA replicas, mean | 9.643 | 12.97 | +34.5% | +1.667 to +4.986 | higher |
| pods started | 4.7 | 9.1 | +93.6% | +2.343 to +6.457 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.7 | 181.2 | -0.3% | -1.26 to +0.2362 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.7 | 181.2 | -0.3% | -1.26 to +0.2362 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.071 | 2.088 | +0.8% | -0.004574 to +0.03814 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.12 | 63.69 | +2.5% | +1.163 to +1.976 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | lower |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.09 | 0.08 | -11.1% | -0.0506 to +0.0306 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: lower on 2 (organism time over the line (% of steps); organism work per energy), higher on 4 (failed requests (%); HPA replicas, mean; pods started; organism energy (J)), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2501 | 3276 | +31.0% | -194.2 to +1744 | higher (inside the noise) |
| response time (ms), 99th percentile | 4455 | 5092 | +14.3% | -303.6 to +1578 | higher (inside the noise) |
| time over the response line (% of samples) | 34.9 | 33.02 | -5.4% | -5.019 to +1.263 | lower (inside the noise) |
| failed requests (%) | 16.52 | 17.85 | +8.1% | +0.2282 to +2.435 | higher |
| HPA replicas, mean | 9.752 | 14.44 | +48.0% | +3.488 to +5.883 | higher |
| pods started | 3.7 | 9.5 | +156.8% | +3.99 to +7.61 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.033e-16 to +9.586e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.4 | -0.2% | -1.14 to +0.5872 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.4 | -0.2% | -1.14 to +0.5872 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.307 | 2.338 | +1.3% | +0.01552 to +0.04586 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.91 | 72.5 | +5.2% | +3 to +4.186 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | higher |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | lower |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | lower |
| organism behind its window (s) | 0.13 | 0.16 | +23.1% | -0.004553 to +0.06455 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
