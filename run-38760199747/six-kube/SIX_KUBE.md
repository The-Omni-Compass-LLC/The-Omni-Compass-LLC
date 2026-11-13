# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2781 | 3599 | 2429 | 2775 | 2228 | 3147 | 3193 | 3881 | 3559 | 4355 | 2281 | 3178 |
| response time (ms), 99th percentile | 5570 | 6349 | 5372 | 5427 | 4717 | 6123 | 5867 | 6263 | 6049 | 6806 | 4960 | 5576 |
| time over the response line (% of samples) | 49.71 | 44.41 | 41.7 | 39.79 | 48.02 | 45.3 | 53.35 | 49.52 | 55.74 | 52.07 | 45.44 | 43.04 |
| failed requests (%) | 28.9 | 27.85 | 27.48 | 28.54 | 32.84 | 33.64 | 35.57 | 34.74 | 38.27 | 37.94 | 25.64 | 26.89 |
| HPA replicas, mean | 9.712 | 14.1 | 9.675 | 13.44 | 9.697 | 13.58 | 9.721 | 14.21 | 9.794 | 13.95 | 9.793 | 13.39 |
| pods started | 4.659 | 8.976 | 4.585 | 9.049 | 4.317 | 8.561 | 4.35 | 9.3 | 2.951 | 7.854 | 2.902 | 7.098 |
| worker nodes in service, mean | 6 | 5.997 | 6 | 6 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.3 | 184 | 183.8 | 184.9 | 184.5 | 184.7 | 184.6 | 185.5 | 185.2 | 184.6 | 184.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.2 | 184 | 183.8 | 184.9 | 184.5 | 184.7 | 184.6 | 185.4 | 185.2 | 184.6 | 184.5 |
| CPU used with Omni's own (cores), mean | 2.471 | 2.49 | 2.334 | 2.345 | 2.421 | 2.439 | 2.425 | 2.436 | 2.468 | 2.496 | 2.398 | 2.427 |
| host CPU busy, the real machine under kind (%) | 72.59 | 74.04 | 69.83 | 70.72 | 72.36 | 73.47 | 71.55 | 72.81 | 73.88 | 75.86 | 72.15 | 75.45 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.004878 | 0.01463 | 0 | 0.0122 | 0.002439 | 0.0122 | 0.0075 | 0.015 | 0.1024 | 0.1146 | 0.1634 | 0.1902 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2781 | 3599 | +29.4% | +288.6 to +1348 | LOSS |
| response time (ms), 99th percentile | 5570 | 6349 | +14.0% | +186.9 to +1371 | LOSS |
| time over the response line (% of samples) | 49.71 | 44.41 | -10.7% | -6.745 to -3.848 | GAIN |
| failed requests (%) | 28.9 | 27.85 | -3.6% | -2.263 to +0.163 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.712 | 14.1 | +45.1% | +3.905 to +4.863 | power given |
| pods started | 4.659 | 8.976 | +92.7% | +3.67 to +4.964 | power given |
| worker nodes in service, mean | 6 | 5.997 | -0.0% | -0.008187 to +0.002655 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 185.3 | +0.1% | -0.2743 to +0.7085 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 185.2 | +0.1% | -0.3433 to +0.6657 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.471 | 2.49 | +0.8% | +0.01229 to +0.02617 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.59 | 74.04 | +2.0% | +1.262 to +1.628 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.004878 | 0.01463 | +200.0% | -0.003595 to +0.02311 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2429 | 2775 | +14.2% | -68.3 to +759.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5372 | 5427 | +1.0% | -423 to +533.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 41.7 | 39.79 | -4.6% | -2.973 to -0.8574 | GAIN |
| failed requests (%) | 27.48 | 28.54 | +3.9% | +0.3877 to +1.731 | LOSS |
| HPA replicas, mean | 9.675 | 13.44 | +38.9% | +3.067 to +4.463 | power given |
| pods started | 4.585 | 9.049 | +97.3% | +3.614 to +5.313 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.773e-16 to +2.473e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184 | 183.8 | -0.1% | -0.5844 to +0.2027 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184 | 183.8 | -0.1% | -0.5844 to +0.2027 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.334 | 2.345 | +0.5% | +0.002499 to +0.01862 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.83 | 70.72 | +1.3% | +0.6384 to +1.146 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0 | 0.0122 | +0.0122 | +0.002054 to +0.02234 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2228 | 3147 | +41.2% | +324.8 to +1512 | LOSS |
| response time (ms), 99th percentile | 4717 | 6123 | +29.8% | +565.5 to +2247 | LOSS |
| time over the response line (% of samples) | 48.02 | 45.3 | -5.7% | -3.929 to -1.508 | GAIN |
| failed requests (%) | 32.84 | 33.64 | +2.4% | +0.03887 to +1.559 | LOSS |
| HPA replicas, mean | 9.697 | 13.58 | +40.1% | +3.217 to +4.552 | power given |
| pods started | 4.317 | 8.561 | +98.3% | +3.376 to +5.112 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001195 to +0.0003874 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.5 | -0.2% | -0.8143 to +0.0606 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.5 | -0.2% | -0.8241 to +0.05407 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.421 | 2.439 | +0.8% | +0.01058 to +0.02626 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.36 | 73.47 | +1.5% | +0.9406 to +1.276 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.002439 | 0.0122 | +400.0% | -0.001707 to +0.02122 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3193 | 3881 | +21.6% | +158 to +1219 | LOSS |
| response time (ms), 99th percentile | 5867 | 6263 | +6.8% | -132.3 to +924.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.35 | 49.52 | -7.2% | -5.624 to -2.019 | GAIN |
| failed requests (%) | 35.57 | 34.74 | -2.3% | -2.145 to +0.4914 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.721 | 14.21 | +46.2% | +3.939 to +5.038 | power given |
| pods started | 4.35 | 9.3 | +113.8% | +4.231 to +5.669 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.418e-17 to +7.403e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.6 | -0.0% | -0.5372 to +0.3533 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.7 | 184.6 | -0.0% | -0.5372 to +0.3533 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.425 | 2.436 | +0.5% | +0.003831 to +0.01875 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.55 | 72.81 | +1.8% | +1.022 to +1.501 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.0075 | 0.015 | +100.0% | -0.0072 to +0.0222 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3559 | 4355 | +22.4% | +111.2 to +1480 | LOSS |
| response time (ms), 99th percentile | 6049 | 6806 | +12.5% | +155.7 to +1358 | LOSS |
| time over the response line (% of samples) | 55.74 | 52.07 | -6.6% | -4.896 to -2.437 | GAIN |
| failed requests (%) | 38.27 | 37.94 | -0.9% | -1.348 to +0.6729 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.794 | 13.95 | +42.4% | +3.701 to +4.611 | power given |
| pods started | 2.951 | 7.854 | +166.1% | +4.232 to +5.572 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001241 to +0.003827 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.5 | 185.2 | -0.2% | -0.6836 to +0.08809 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.2 | -0.1% | -0.6703 to +0.1267 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.468 | 2.496 | +1.1% | +0.01945 to +0.03492 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.88 | 75.86 | +2.7% | +1.849 to +2.123 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1024 | 0.1146 | +11.9% | -0.00856 to +0.03295 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2281 | 3178 | +39.3% | +458.6 to +1336 | LOSS |
| response time (ms), 99th percentile | 4960 | 5576 | +12.4% | -52.68 to +1285 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.44 | 43.04 | -5.3% | -3.571 to -1.218 | GAIN |
| failed requests (%) | 25.64 | 26.89 | +4.9% | +0.4906 to +2.011 | LOSS |
| HPA replicas, mean | 9.793 | 13.39 | +36.7% | +3.143 to +4.052 | power given |
| pods started | 2.902 | 7.098 | +144.5% | +3.457 to +4.933 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.309e-16 to +5.475e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.5 | -0.0% | -0.5225 to +0.3501 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.5 | -0.0% | -0.5225 to +0.3501 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.398 | 2.427 | +1.2% | +0.02079 to +0.03841 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.15 | 75.45 | +4.6% | +3.02 to +3.575 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.1634 | 0.1902 | +16.4% | +0.002128 to +0.05153 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
