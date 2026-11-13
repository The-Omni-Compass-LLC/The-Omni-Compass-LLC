# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2155 | 2918 | 2092 | 2114 | 1516 | 1588 | 4220 | 4527 | 1453 | 1851 | 2822 | 3864 |
| response time (ms), 99th percentile | 4797 | 5650 | 5130 | 4908 | 3388 | 3378 | 7092 | 7058 | 2324 | 2592 | 6105 | 6584 |
| time over the response line (% of samples) | 45.26 | 40.77 | 28.46 | 26.64 | 37.13 | 34.07 | 52.66 | 47.96 | 22.43 | 19.94 | 49.86 | 46.68 |
| failed requests (%) | 26.09 | 26.32 | 16.65 | 17.45 | 25.86 | 26.02 | 29.55 | 29.86 | 16.18 | 15.88 | 25.93 | 27.26 |
| HPA replicas, mean | 9.697 | 14.18 | 9.601 | 13.48 | 9.58 | 12.48 | 9.688 | 13.91 | 9.598 | 11.72 | 9.798 | 13.67 |
| pods started | 4.8 | 9.7 | 5.6 | 10.5 | 5.6 | 8.2 | 4.8 | 9.9 | 5.4 | 7.6 | 3.2 | 7.1 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.5 | 182.8 | 183.1 | 183.2 | 183.2 | 185.7 | 184.9 | 180.6 | 180.8 | 185.4 | 185.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.5 | 182.8 | 183.1 | 183.2 | 183.2 | 185.7 | 184.9 | 180.6 | 180.8 | 185.4 | 185.5 |
| CPU used with Omni's own (cores), mean | 2.383 | 2.405 | 2.23 | 2.259 | 2.259 | 2.274 | 2.496 | 2.505 | 1.992 | 2.02 | 2.491 | 2.518 |
| host CPU busy, the real machine under kind (%) | 70.51 | 71.93 | 66.07 | 67.37 | 67.16 | 68.2 | 72.97 | 74.33 | 59.61 | 61.59 | 74.59 | 77.85 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.01 | 0 | 0 | 0 | 0 | 0 | 0.01 | 0 | 0.07 | 0.11 | 0.16 | 0.17 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2155 | 2918 | +35.4% | -727.4 to +2252 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4797 | 5650 | +17.8% | -1589 to +3295 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.26 | 40.77 | -9.9% | -7.536 to -1.446 | GAIN |
| failed requests (%) | 26.09 | 26.32 | +0.9% | -1.668 to +2.13 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.697 | 14.18 | +46.3% | +3.313 to +5.658 | power given |
| pods started | 4.8 | 9.7 | +102.1% | +3.338 to +6.462 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.337e-15 to +2.707e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 184.5 | +0.2% | -0.5816 to +1.336 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 184.5 | +0.2% | -0.5816 to +1.336 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.383 | 2.405 | +0.9% | +0.008052 to +0.03543 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.51 | 71.93 | +2.0% | +0.9268 to +1.92 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2092 | 2114 | +1.0% | -928.3 to +971 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5130 | 4908 | -4.3% | -909.8 to +465.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 28.46 | 26.64 | -6.4% | -3.615 to -0.02366 | GAIN |
| failed requests (%) | 16.65 | 17.45 | +4.8% | -2.446 to +4.038 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.601 | 13.48 | +40.4% | +2.355 to +5.411 | power given |
| pods started | 5.6 | 10.5 | +87.5% | +2.95 to +6.85 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.535e-15 to +4.694e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.8 | 183.1 | +0.2% | -0.6127 to +1.187 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.8 | 183.1 | +0.2% | -0.6127 to +1.187 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.23 | 2.259 | +1.3% | +0.005781 to +0.05228 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.07 | 67.37 | +2.0% | +0.7076 to +1.905 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1516 | 1588 | +4.8% | -799.2 to +943.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3388 | 3378 | -0.3% | -988.3 to +968.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 37.13 | 34.07 | -8.3% | -6.939 to +0.804 | EVEN, inside the noise (cut) |
| failed requests (%) | 25.86 | 26.02 | +0.6% | -1.351 to +1.663 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.58 | 12.48 | +30.3% | +1.068 to +4.74 | power given |
| pods started | 5.6 | 8.2 | +46.4% | +0.259 to +4.941 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.25e-15 to +3.623e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.2 | 183.2 | +0.0% | -1.033 to +1.159 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.2 | 183.2 | +0.0% | -1.033 to +1.159 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.259 | 2.274 | +0.6% | -0.01638 to +0.04486 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.16 | 68.2 | +1.5% | -0.01315 to +2.088 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4220 | 4527 | +7.3% | -1254 to +1868 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 7092 | 7058 | -0.5% | -1222 to +1153 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 52.66 | 47.96 | -8.9% | -9.368 to -0.04774 | GAIN |
| failed requests (%) | 29.55 | 29.86 | +1.0% | -1.886 to +2.495 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.688 | 13.91 | +43.6% | +2.633 to +5.808 | power given |
| pods started | 4.8 | 9.9 | +106.2% | +2.929 to +7.271 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.615e-16 to +4.062e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 184.9 | -0.4% | -1.684 to +0.02542 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 184.9 | -0.4% | -1.684 to +0.02542 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.496 | 2.505 | +0.4% | -0.002458 to +0.02078 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.97 | 74.33 | +1.9% | +1.003 to +1.726 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.01 | 0 | -100.0% | -0.03262 to +0.01262 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1453 | 1851 | +27.4% | -412.6 to +1208 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 2324 | 2592 | +11.5% | -971.9 to +1508 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.43 | 19.94 | -11.1% | -4.352 to -0.6174 | GAIN |
| failed requests (%) | 16.18 | 15.88 | -1.8% | -1.617 to +1.029 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.598 | 11.72 | +22.1% | +0.5226 to +3.72 | power given |
| pods started | 5.4 | 7.6 | +40.7% | +0.5208 to +3.879 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.242e-16 to +5.794e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.8 | +0.2% | -0.5073 to +1.057 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.8 | +0.2% | -0.5073 to +1.057 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.992 | 2.02 | +1.4% | +0.005171 to +0.04959 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.61 | 61.59 | +3.3% | +1.219 to +2.752 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.07 | 0.11 | +57.1% | +0.003062 to +0.07694 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2822 | 3864 | +36.9% | +35.38 to +2050 | LOSS |
| response time (ms), 99th percentile | 6105 | 6584 | +7.8% | -1091 to +2048 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 49.86 | 46.68 | -6.4% | -6.778 to +0.4098 | EVEN, inside the noise (cut) |
| failed requests (%) | 25.93 | 27.26 | +5.1% | +0.01286 to +2.657 | LOSS |
| HPA replicas, mean | 9.798 | 13.67 | +39.5% | +2.745 to +4.99 | power given |
| pods started | 3.2 | 7.1 | +121.9% | +2.532 to +5.268 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.009e-15 to +2.324e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.5 | +0.0% | -0.8472 to +0.9379 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.5 | +0.0% | -0.8472 to +0.9379 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.491 | 2.518 | +1.1% | +0.0203 to +0.03336 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.59 | 77.85 | +4.4% | +3.008 to +3.504 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.16 | 0.17 | +6.2% | -0.0306 to +0.0506 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
