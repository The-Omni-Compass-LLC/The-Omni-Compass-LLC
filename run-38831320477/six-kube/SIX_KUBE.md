# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1428 | 1303 | 1458 | 1575 | 1350 | 1293 | 2008 | 1829 | 1997 | 1793 | 1520 | 1241 |
| response time (ms), 99th percentile | 4289 | 4670 | 4794 | 4701 | 4218 | 4286 | 5381 | 5199 | 4821 | 4977 | 4138 | 4320 |
| time over the response line (% of samples) | 23.73 | 17.79 | 17.35 | 12.65 | 15.63 | 11.33 | 29.28 | 21.31 | 30.78 | 22.58 | 22.63 | 15.79 |
| failed requests (%) | 10.46 | 9.616 | 5.848 | 4.939 | 5.572 | 4.875 | 10 | 9.304 | 12.71 | 10.29 | 9.701 | 7.989 |
| HPA replicas, mean | 9.629 | 12.1 | 9.591 | 13.15 | 9.591 | 12.56 | 9.638 | 13.79 | 9.641 | 13.14 | 9.619 | 11.88 |
| pods started | 5.244 | 9.659 | 5.39 | 9.561 | 5.098 | 9.244 | 4.902 | 9.732 | 4.95 | 10.03 | 5.512 | 10.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.5 | 179.9 | 179 | 179.1 | 178.4 | 182.4 | 182 | 181.8 | 181.6 | 180.6 | 180.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.5 | 179.9 | 179 | 179.1 | 178.4 | 182.4 | 182 | 181.8 | 181.6 | 180.6 | 180.3 |
| CPU used with Omni's own (cores), mean | 2.046 | 2.044 | 1.948 | 1.944 | 1.858 | 1.854 | 2.19 | 2.193 | 2.179 | 2.16 | 2.025 | 2.017 |
| host CPU busy, the real machine under kind (%) | 60.52 | 60.88 | 57.65 | 57.85 | 55.36 | 55.51 | 64.64 | 65.24 | 64.31 | 64.51 | 60.17 | 60.27 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0.002439 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1428 | 1303 | -8.8% | -298.6 to +47.29 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4289 | 4670 | +8.9% | -79.18 to +841.7 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.73 | 17.79 | -25.0% | -7.774 to -4.109 | GAIN |
| failed requests (%) | 10.46 | 9.616 | -8.1% | -1.499 to -0.192 | GAIN |
| HPA replicas, mean | 9.629 | 12.1 | +25.7% | +1.849 to +3.103 | power given |
| pods started | 5.244 | 9.659 | +84.2% | +3.713 to +5.116 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.103e-16 to +3.375e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.5 | -0.2% | -0.7033 to +0.02961 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.5 | -0.2% | -0.7033 to +0.02961 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.046 | 2.044 | -0.1% | -0.01248 to +0.00905 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.52 | 60.88 | +0.6% | +0.06972 to +0.6407 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.625e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.145e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1458 | 1575 | +8.0% | -171.2 to +405 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4794 | 4701 | -1.9% | -445.7 to +258.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 17.35 | 12.65 | -27.1% | -5.903 to -3.506 | GAIN |
| failed requests (%) | 5.848 | 4.939 | -15.5% | -1.371 to -0.448 | GAIN |
| HPA replicas, mean | 9.591 | 13.15 | +37.1% | +2.913 to +4.2 | power given |
| pods started | 5.39 | 9.561 | +77.4% | +3.434 to +4.908 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.7e-16 to +1.367e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.9 | 179 | -0.5% | -1.322 to -0.5104 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.9 | 179 | -0.5% | -1.322 to -0.5104 | GAIN |
| CPU used with Omni's own (cores), mean | 1.948 | 1.944 | -0.2% | -0.01096 to +0.003086 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.65 | 57.85 | +0.3% | +0.04728 to +0.3523 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1350 | 1293 | -4.2% | -294.3 to +181 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4218 | 4286 | +1.6% | -317.2 to +452 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 15.63 | 11.33 | -27.6% | -5.529 to -3.084 | GAIN |
| failed requests (%) | 5.572 | 4.875 | -12.5% | -1.048 to -0.3459 | GAIN |
| HPA replicas, mean | 9.591 | 12.56 | +31.0% | +2.262 to +3.679 | power given |
| pods started | 5.098 | 9.244 | +81.3% | +3.222 to +5.071 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.674e-16 to +4.84e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.1 | 178.4 | -0.4% | -1.09 to -0.358 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.1 | 178.4 | -0.4% | -1.09 to -0.358 | GAIN |
| CPU used with Omni's own (cores), mean | 1.858 | 1.854 | -0.2% | -0.01235 to +0.005065 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 55.36 | 55.51 | +0.3% | -0.073 to +0.3786 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.002439 | 0 | -100.0% | -0.00722 to +0.002341 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2008 | 1829 | -8.9% | -361 to +2.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5381 | 5199 | -3.4% | -561.9 to +198.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 29.28 | 21.31 | -27.2% | -9.554 to -6.397 | GAIN |
| failed requests (%) | 10 | 9.304 | -7.0% | -0.9847 to -0.4081 | GAIN |
| HPA replicas, mean | 9.638 | 13.79 | +43.1% | +3.59 to +4.711 | power given |
| pods started | 4.902 | 9.732 | +98.5% | +4.077 to +5.582 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.163e-16 to +2.863e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.4 | 182 | -0.3% | -0.9392 to -0.02173 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.4 | 182 | -0.3% | -0.9392 to -0.02173 | GAIN |
| CPU used with Omni's own (cores), mean | 2.19 | 2.193 | +0.1% | -0.005442 to +0.01129 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.64 | 65.24 | +0.9% | +0.3675 to +0.8426 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1997 | 1793 | -10.2% | -466.1 to +56.81 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4821 | 4977 | +3.2% | -353.1 to +665.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 30.78 | 22.58 | -26.7% | -10.32 to -6.092 | GAIN |
| failed requests (%) | 12.71 | 10.29 | -19.0% | -3.63 to -1.212 | GAIN |
| HPA replicas, mean | 9.641 | 13.14 | +36.3% | +2.863 to +4.128 | power given |
| pods started | 4.95 | 10.03 | +102.5% | +4.454 to +5.696 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.554e-16 to +3.366e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.6 | -0.1% | -0.7689 to +0.3922 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.6 | -0.1% | -0.7689 to +0.3922 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.179 | 2.16 | -0.8% | -0.03148 to -0.005449 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.31 | 64.51 | +0.3% | -0.0446 to +0.433 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1520 | 1241 | -18.4% | -458.2 to -100.3 | GAIN |
| response time (ms), 99th percentile | 4138 | 4320 | +4.4% | -222 to +585.2 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.63 | 15.79 | -30.2% | -8.948 to -4.737 | GAIN |
| failed requests (%) | 9.701 | 7.989 | -17.7% | -2.748 to -0.6766 | GAIN |
| HPA replicas, mean | 9.619 | 11.88 | +23.5% | +1.713 to +2.803 | power given |
| pods started | 5.512 | 10.2 | +85.0% | +3.824 to +5.542 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.408e-16 to +1.209e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 180.3 | -0.2% | -0.7062 to +0.1336 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 180.3 | -0.2% | -0.7062 to +0.1336 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.025 | 2.017 | -0.4% | -0.01991 to +0.003415 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.17 | 60.27 | +0.2% | -0.2711 to +0.4735 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
