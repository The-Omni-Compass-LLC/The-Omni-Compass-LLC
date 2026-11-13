# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1608 | 1110 | 1329 | 1847 | 1799 | 1803 | 1543 | 1482 | 1777 | 1257 | 1367 | 1062 |
| response time (ms), 99th percentile | 4439 | 4417 | 5143 | 5075 | 5542 | 4870 | 4593 | 4450 | 4584 | 4670 | 3901 | 4421 |
| time over the response line (% of samples) | 26.95 | 18.04 | 18.73 | 13.59 | 17.33 | 13.11 | 26.59 | 18.94 | 23.5 | 16.41 | 22.51 | 15.47 |
| failed requests (%) | 12.49 | 9.661 | 6.459 | 5.314 | 5.532 | 5.043 | 8.951 | 8.272 | 8.987 | 6.359 | 10.79 | 8.467 |
| HPA replicas, mean | 9.647 | 12.52 | 9.646 | 13.39 | 9.571 | 13.12 | 9.601 | 12.96 | 9.613 | 13.35 | 9.623 | 12.05 |
| pods started | 5.125 | 9.5 | 4.875 | 9.25 | 5.75 | 9.75 | 4.625 | 8.5 | 5.375 | 11.62 | 5.125 | 9.375 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181 | 180.7 | 180.2 | 180.2 | 179.2 | 180.3 | 180.4 | 181.1 | 181.7 | 180 | 179.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181 | 180.7 | 180.2 | 180.2 | 179.2 | 180.3 | 180.4 | 181.1 | 181.7 | 180 | 179.8 |
| CPU used with Omni's own (cores), mean | 2.12 | 2.101 | 1.995 | 2.006 | 1.951 | 1.971 | 2.037 | 2.03 | 2.082 | 2.096 | 1.988 | 1.97 |
| host CPU busy, the real machine under kind (%) | 62.85 | 62.73 | 59.24 | 59.57 | 58.14 | 58.55 | 60.83 | 60.97 | 62.4 | 62.76 | 59.18 | 59.16 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1608 | 1110 | -31.0% | -956.3 to -39.99 | GAIN |
| response time (ms), 99th percentile | 4439 | 4417 | -0.5% | -1496 to +1453 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.95 | 18.04 | -33.0% | -14.42 to -3.385 | GAIN |
| failed requests (%) | 12.49 | 9.661 | -22.6% | -4.97 to -0.6792 | GAIN |
| HPA replicas, mean | 9.647 | 12.52 | +29.8% | +1.345 to +4.404 | power given |
| pods started | 5.125 | 9.5 | +85.4% | +2.536 to +6.214 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.05e-15 to +1.05e-15 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181 | -0.2% | -1.439 to +0.7385 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181 | -0.2% | -1.439 to +0.7385 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.12 | 2.101 | -0.9% | -0.04468 to +0.006527 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.85 | 62.73 | -0.2% | -1.005 to +0.7567 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.614e+05 to +8.628e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.152e-05 to -8.139e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1329 | 1847 | +38.9% | -512.2 to +1547 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5143 | 5075 | -1.3% | -1304 to +1169 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 18.73 | 13.59 | -27.4% | -8.32 to -1.959 | GAIN |
| failed requests (%) | 6.459 | 5.314 | -17.7% | -2.313 to +0.02239 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.646 | 13.39 | +38.8% | +1.969 to +5.519 | power given |
| pods started | 4.875 | 9.25 | +89.7% | +1.55 to +7.2 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.174e-15 to +7.298e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.7 | 180.2 | -0.3% | -1.76 to +0.696 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.7 | 180.2 | -0.3% | -1.76 to +0.696 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.995 | 2.006 | +0.6% | -0.01323 to +0.03565 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.24 | 59.57 | +0.6% | -0.198 to +0.8588 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 3 (response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1799 | 1803 | +0.2% | -896.3 to +904.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5542 | 4870 | -12.1% | -1165 to -178.9 | GAIN |
| time over the response line (% of samples) | 17.33 | 13.11 | -24.4% | -7.618 to -0.8255 | GAIN |
| failed requests (%) | 5.532 | 5.043 | -8.8% | -1.766 to +0.7875 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.571 | 13.12 | +37.1% | +1.681 to +5.419 | power given |
| pods started | 5.75 | 9.75 | +69.6% | +1.952 to +6.048 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.494e-15 to +6.062e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.2 | 179.2 | -0.6% | -2.593 to +0.4521 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.2 | 179.2 | -0.6% | -2.593 to +0.4521 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.951 | 1.971 | +1.0% | -0.005624 to +0.04639 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.14 | 58.55 | +0.7% | -0.191 to +1.021 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1543 | 1482 | -4.0% | -478.6 to +356.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4593 | 4450 | -3.1% | -758 to +472.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.59 | 18.94 | -28.8% | -13.27 to -2.023 | GAIN |
| failed requests (%) | 8.951 | 8.272 | -7.6% | -1.483 to +0.1254 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.601 | 12.96 | +35.0% | +1.071 to +5.651 | power given |
| pods started | 4.625 | 8.5 | +83.8% | +0.7967 to +6.953 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.49e-16 to +1.215e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.3 | 180.4 | +0.1% | -0.7023 to +0.8923 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.3 | 180.4 | +0.1% | -0.7023 to +0.8923 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.037 | 2.03 | -0.3% | -0.02767 to +0.01452 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.83 | 60.97 | +0.2% | -0.4731 to +0.76 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1777 | 1257 | -29.3% | -1491 to +450.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4584 | 4670 | +1.9% | -1310 to +1482 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 23.5 | 16.41 | -30.2% | -13.88 to -0.2986 | GAIN |
| failed requests (%) | 8.987 | 6.359 | -29.2% | -8.076 to +2.82 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.613 | 13.35 | +38.8% | +2.952 to +4.516 | power given |
| pods started | 5.375 | 11.62 | +116.3% | +4.854 to +7.646 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.282e-15 to +2.833e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 181.7 | +0.4% | +0.07443 to +1.198 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 181.7 | +0.4% | +0.07443 to +1.198 | power given |
| CPU used with Omni's own (cores), mean | 2.082 | 2.096 | +0.7% | -0.002535 to +0.03055 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.4 | 62.76 | +0.6% | -0.7103 to +1.419 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1367 | 1062 | -22.3% | -790.8 to +179.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3901 | 4421 | +13.3% | -773.5 to +1815 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.51 | 15.47 | -31.3% | -12.42 to -1.665 | GAIN |
| failed requests (%) | 10.79 | 8.467 | -21.5% | -4.309 to -0.3334 | GAIN |
| HPA replicas, mean | 9.623 | 12.05 | +25.2% | +0.4397 to +4.405 | power given |
| pods started | 5.125 | 9.375 | +82.9% | +1.541 to +6.959 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.467e-16 to +9.908e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.8 | -0.1% | -1.093 to +0.7892 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.8 | -0.1% | -1.093 to +0.7892 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.988 | 1.97 | -0.9% | -0.04331 to +0.007475 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.18 | 59.16 | -0.0% | -0.6016 to +0.5623 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.984e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
