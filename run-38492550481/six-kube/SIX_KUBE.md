# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3041 | 3321 | 2798 | 3301 | 2540 | 2936 | 3010 | 3459 | 3310 | 3997 | 2851 | 3991 |
| response time (ms), 99th percentile | 6013 | 6577 | 5569 | 6213 | 5249 | 5639 | 5219 | 5771 | 5789 | 6189 | 5793 | 6314 |
| time over the response line (% of samples) | 50.83 | 44.6 | 44.33 | 41.95 | 39.85 | 37.36 | 48.16 | 42.51 | 52.84 | 49.36 | 42.25 | 41.71 |
| failed requests (%) | 27.66 | 26.96 | 29.64 | 30.24 | 25.78 | 26.23 | 30.4 | 29.21 | 35.55 | 35.37 | 20.75 | 22.4 |
| HPA replicas, mean | 9.73 | 14.68 | 9.669 | 14.14 | 9.638 | 13.82 | 9.677 | 14.17 | 9.778 | 14.55 | 9.744 | 14.3 |
| pods started | 4.439 | 9.829 | 4.829 | 9.659 | 5.024 | 9.78 | 4.976 | 9.585 | 3.293 | 8.439 | 3.756 | 8.683 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.4 | 184.4 | 184.2 | 183.5 | 183.9 | 184.3 | 184.3 | 185 | 184.3 | 185.1 | 184.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.4 | 184.4 | 184.2 | 183.5 | 183.9 | 184.3 | 184.3 | 185 | 184.3 | 185.1 | 184.9 |
| CPU used with Omni's own (cores), mean | 2.492 | 2.509 | 2.401 | 2.411 | 2.323 | 2.34 | 2.388 | 2.402 | 2.416 | 2.437 | 2.426 | 2.456 |
| host CPU busy, the real machine under kind (%) | 73.09 | 74.53 | 71.25 | 72.24 | 68.93 | 70.18 | 70.03 | 71.38 | 72.26 | 74.29 | 72.6 | 75.98 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.009756 | 0.01463 | 0.004878 | 0.0122 | 0.002439 | 0.0122 | 0.007317 | 0.0122 | 0.1 | 0.1049 | 0.139 | 0.2024 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3041 | 3321 | +9.2% | -82.23 to +642.9 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6013 | 6577 | +9.4% | -37.72 to +1166 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 50.83 | 44.6 | -12.3% | -8.034 to -4.441 | GAIN |
| failed requests (%) | 27.66 | 26.96 | -2.5% | -1.501 to +0.09846 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.73 | 14.68 | +50.8% | +4.512 to +5.379 | power given |
| pods started | 4.439 | 9.829 | +121.4% | +4.696 to +6.084 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.815e-16 to +1.649e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 185.4 | -0.0% | -0.4744 to +0.4524 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 185.4 | -0.0% | -0.4744 to +0.4524 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.492 | 2.509 | +0.7% | +0.01314 to +0.0201 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.09 | 74.53 | +2.0% | +1.287 to +1.587 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.009756 | 0.01463 | +50.0% | -0.01035 to +0.02011 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2798 | 3301 | +18.0% | -41.37 to +1047 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5569 | 6213 | +11.6% | +61.63 to +1227 | LOSS |
| time over the response line (% of samples) | 44.33 | 41.95 | -5.4% | -3.431 to -1.341 | GAIN |
| failed requests (%) | 29.64 | 30.24 | +2.0% | -0.393 to +1.579 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.669 | 14.14 | +46.3% | +3.902 to +5.043 | power given |
| pods started | 4.829 | 9.659 | +100.0% | +4.173 to +5.485 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002702 to +0.0008762 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.4 | 184.2 | -0.1% | -0.7076 to +0.4102 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.4 | 184.2 | -0.1% | -0.7518 to +0.4179 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.401 | 2.411 | +0.4% | -0.0004526 to +0.02022 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.25 | 72.24 | +1.4% | +0.7403 to +1.231 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0.004878 | 0.0122 | +150.0% | -0.005286 to +0.01992 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2540 | 2936 | +15.6% | -71.27 to +862.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5249 | 5639 | +7.4% | -292.7 to +1072 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 39.85 | 37.36 | -6.3% | -3.49 to -1.493 | GAIN |
| failed requests (%) | 25.78 | 26.23 | +1.8% | -0.2636 to +1.173 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.638 | 13.82 | +43.4% | +3.542 to +4.818 | power given |
| pods started | 5.024 | 9.78 | +94.7% | +3.988 to +5.524 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.296e-16 to +5.196e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.5 | 183.9 | +0.2% | -0.06988 to +0.7447 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.5 | 183.9 | +0.2% | -0.06988 to +0.7447 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.323 | 2.34 | +0.7% | +0.009435 to +0.02465 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.93 | 70.18 | +1.8% | +1.068 to +1.425 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.002439 | 0.0122 | +400.0% | -0.001707 to +0.02122 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3010 | 3459 | +14.9% | -22.79 to +921.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5219 | 5771 | +10.6% | +53.37 to +1050 | LOSS |
| time over the response line (% of samples) | 48.16 | 42.51 | -11.7% | -7.3 to -3.992 | GAIN |
| failed requests (%) | 30.4 | 29.21 | -3.9% | -2.088 to -0.2909 | GAIN |
| HPA replicas, mean | 9.677 | 14.17 | +46.5% | +3.917 to +5.077 | power given |
| pods started | 4.976 | 9.585 | +92.6% | +3.905 to +5.314 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.89e-16 to +3.157e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 184.3 | +0.0% | -0.4166 to +0.5514 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 184.3 | +0.0% | -0.4166 to +0.5514 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.388 | 2.402 | +0.6% | +0.008185 to +0.02067 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.03 | 71.38 | +1.9% | +1.177 to +1.523 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0.007317 | 0.0122 | +66.7% | -0.008727 to +0.01848 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 95th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3310 | 3997 | +20.8% | +194.4 to +1181 | LOSS |
| response time (ms), 99th percentile | 5789 | 6189 | +6.9% | -52.86 to +853 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.84 | 49.36 | -6.6% | -4.652 to -2.302 | GAIN |
| failed requests (%) | 35.55 | 35.37 | -0.5% | -1.053 to +0.6848 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.778 | 14.55 | +48.8% | +4.279 to +5.264 | power given |
| pods started | 3.293 | 8.439 | +156.3% | +4.477 to +5.815 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.774e-16 to +4.373e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.3 | -0.3% | -1.003 to -0.2869 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.3 | -0.3% | -1.003 to -0.2869 | GAIN |
| CPU used with Omni's own (cores), mean | 2.416 | 2.437 | +0.9% | +0.01086 to +0.03186 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.26 | 74.29 | +2.8% | +1.72 to +2.333 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.1049 | +4.9% | -0.008727 to +0.01848 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2851 | 3991 | +40.0% | +629.2 to +1651 | LOSS |
| response time (ms), 99th percentile | 5793 | 6314 | +9.0% | -101.7 to +1142 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 42.25 | 41.71 | -1.3% | -2.114 to +1.029 | EVEN, inside the noise (cut) |
| failed requests (%) | 20.75 | 22.4 | +8.0% | +0.9303 to +2.375 | LOSS |
| HPA replicas, mean | 9.744 | 14.3 | +46.8% | +3.991 to +5.124 | power given |
| pods started | 3.756 | 8.683 | +131.2% | +4.294 to +5.559 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.746e-16 to +4.179e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 184.9 | -0.1% | -0.6015 to +0.1596 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 184.9 | -0.1% | -0.6015 to +0.1596 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.456 | +1.2% | +0.02259 to +0.03653 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.6 | 75.98 | +4.6% | +3.121 to +3.626 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.139 | 0.2024 | +45.6% | +0.03625 to +0.09058 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
