# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2316 | 2592 | 2951 | 3065 | 2384 | 3015 | 3304 | 3448 | 3313 | 3942 | 2349 | 3063 |
| response time (ms), 99th percentile | 4605 | 5037 | 5984 | 5937 | 5204 | 6004 | 5888 | 5967 | 5692 | 6251 | 4706 | 5672 |
| time over the response line (% of samples) | 37.83 | 33.25 | 48.18 | 45.14 | 48.92 | 46.78 | 48.67 | 42.57 | 51.91 | 48.58 | 40.73 | 38.28 |
| failed requests (%) | 20.67 | 20.13 | 33.32 | 33.88 | 34.01 | 34.8 | 28.78 | 28.34 | 35.08 | 35.13 | 21.66 | 23.36 |
| HPA replicas, mean | 9.672 | 13.62 | 9.71 | 13.53 | 9.721 | 13.96 | 9.683 | 13.83 | 9.759 | 13.54 | 9.743 | 12.96 |
| pods started | 5 | 9.366 | 4.317 | 8.537 | 4.22 | 9 | 4.878 | 9.317 | 3.61 | 7.707 | 3.61 | 7.171 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.6 | 184.5 | 184.4 | 185 | 184.5 | 184.7 | 184.7 | 184.9 | 184.6 | 184.1 | 184.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.6 | 184.5 | 184.4 | 185 | 184.5 | 184.6 | 184.7 | 184.9 | 184.6 | 184.1 | 184.1 |
| CPU used with Omni's own (cores), mean | 2.3 | 2.319 | 2.407 | 2.427 | 2.418 | 2.441 | 2.416 | 2.434 | 2.424 | 2.442 | 2.332 | 2.366 |
| host CPU busy, the real machine under kind (%) | 67.78 | 69.17 | 71.86 | 72.97 | 72.46 | 73.71 | 70.9 | 72.29 | 72.41 | 74.3 | 69.96 | 73.44 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.004878 | 0.01463 | 0.002439 | 0.01463 | 0.007317 | 0.01707 | 0.007317 | 0.0122 | 0.1049 | 0.1122 | 0.161 | 0.1927 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2316 | 2592 | +11.9% | -153 to +704.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4605 | 5037 | +9.4% | -174.7 to +1039 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 37.83 | 33.25 | -12.1% | -5.987 to -3.179 | GAIN |
| failed requests (%) | 20.67 | 20.13 | -2.6% | -1.432 to +0.352 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.672 | 13.62 | +40.9% | +3.33 to +4.576 | power given |
| pods started | 5 | 9.366 | +87.3% | +3.598 to +5.133 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.453e-16 to +2.72e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183.6 | +0.2% | -0.09721 to +0.6651 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183.6 | +0.2% | -0.09721 to +0.6651 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.3 | 2.319 | +0.8% | +0.01361 to +0.02525 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.78 | 69.17 | +2.1% | +1.223 to +1.563 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.004878 | 0.01463 | +200.0% | -0.003595 to +0.02311 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2951 | 3065 | +3.9% | -371.3 to +598.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5984 | 5937 | -0.8% | -731.4 to +637.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 48.18 | 45.14 | -6.3% | -4.238 to -1.839 | GAIN |
| failed requests (%) | 33.32 | 33.88 | +1.7% | -0.2158 to +1.333 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.71 | 13.53 | +39.4% | +3.11 to +4.533 | power given |
| pods started | 4.317 | 8.537 | +97.7% | +3.369 to +5.07 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002367 to +0.0007677 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.4 | -0.1% | -0.5629 to +0.3454 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.4 | -0.1% | -0.5745 to +0.3245 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.407 | 2.427 | +0.8% | +0.01375 to +0.02706 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.86 | 72.97 | +1.5% | +0.9169 to +1.297 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0.002439 | 0.01463 | +500.0% | +0.002054 to +0.02234 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2384 | 3015 | +26.5% | +173 to +1090 | LOSS |
| response time (ms), 99th percentile | 5204 | 6004 | +15.4% | +1.85 to +1600 | LOSS |
| time over the response line (% of samples) | 48.92 | 46.78 | -4.4% | -3.424 to -0.8569 | GAIN |
| failed requests (%) | 34.01 | 34.8 | +2.3% | -0.006644 to +1.588 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.721 | 13.96 | +43.7% | +3.606 to +4.882 | power given |
| pods started | 4.22 | 9 | +113.3% | +3.924 to +5.637 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.028e-16 to +3.461e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.5 | -0.3% | -0.882 to -0.04764 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.5 | -0.3% | -0.882 to -0.04764 | GAIN |
| CPU used with Omni's own (cores), mean | 2.418 | 2.441 | +1.0% | +0.01618 to +0.03137 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.46 | 73.71 | +1.7% | +1.053 to +1.448 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.007317 | 0.01707 | +133.3% | -0.005247 to +0.02476 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3304 | 3448 | +4.4% | -258.9 to +546.7 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5888 | 5967 | +1.3% | -384.4 to +542.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 48.67 | 42.57 | -12.5% | -7.965 to -4.223 | GAIN |
| failed requests (%) | 28.78 | 28.34 | -1.6% | -1.623 to +0.7292 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.683 | 13.83 | +42.8% | +3.503 to +4.789 | power given |
| pods started | 4.878 | 9.317 | +91.0% | +3.598 to +5.28 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.0007772 to +0.002397 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.7 | 184.7 | +0.1% | -0.3389 to +0.5378 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.7 | +0.1% | -0.331 to +0.5625 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.416 | 2.434 | +0.7% | +0.008522 to +0.0273 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.9 | 72.29 | +2.0% | +1.137 to +1.653 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.007317 | 0.0122 | +66.7% | -0.008727 to +0.01848 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 95th percentile; response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3313 | 3942 | +19.0% | +187.7 to +1072 | LOSS |
| response time (ms), 99th percentile | 5692 | 6251 | +9.8% | +33.58 to +1083 | LOSS |
| time over the response line (% of samples) | 51.91 | 48.58 | -6.4% | -4.642 to -2.018 | GAIN |
| failed requests (%) | 35.08 | 35.13 | +0.1% | -1.247 to +1.338 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.759 | 13.54 | +38.7% | +3.227 to +4.334 | power given |
| pods started | 3.61 | 7.707 | +113.5% | +3.294 to +4.901 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0004341 to +0.001338 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.6 | -0.2% | -0.7211 to +0.04674 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 184.6 | -0.2% | -0.7097 to +0.05358 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.424 | 2.442 | +0.8% | +0.007073 to +0.03009 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.41 | 74.3 | +2.6% | +1.514 to +2.263 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1049 | 0.1122 | +7.0% | -0.008574 to +0.02321 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2349 | 3063 | +30.4% | +319.9 to +1108 | LOSS |
| response time (ms), 99th percentile | 4706 | 5672 | +20.5% | +327.7 to +1603 | LOSS |
| time over the response line (% of samples) | 40.73 | 38.28 | -6.0% | -3.583 to -1.315 | GAIN |
| failed requests (%) | 21.66 | 23.36 | +7.9% | +0.9126 to +2.495 | LOSS |
| HPA replicas, mean | 9.743 | 12.96 | +33.0% | +2.646 to +3.782 | power given |
| pods started | 3.61 | 7.171 | +98.6% | +2.833 to +4.289 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.875e-16 to +5.341e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.1 | -0.0% | -0.4217 to +0.3618 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.1 | -0.0% | -0.4217 to +0.3618 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.332 | 2.366 | +1.4% | +0.02692 to +0.04 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.96 | 73.44 | +5.0% | +3.299 to +3.671 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.161 | 0.1927 | +19.7% | +0.01182 to +0.05159 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
