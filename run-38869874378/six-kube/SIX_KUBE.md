# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1658 | 1551 | 1894 | 1690 | 1743 | 1751 | 1714 | 1503 | 1485 | 1586 |
| response time (ms), 99th percentile | 5350 | 5477 | 5300 | 5273 | 5376 | 5286 | 4868 | 4667 | 5042 | 4870 |
| time over the response line (% of samples) | 27.33 | 19.6 | 20 | 14.54 | 21.21 | 15.21 | 24.12 | 17.35 | 26.78 | 19.81 |
| failed requests (%) | 11.65 | 9.628 | 6.936 | 6.32 | 7.561 | 6.589 | 7.711 | 6.952 | 11.91 | 10.34 |
| HPA replicas, mean | 9.686 | 12.82 | 9.592 | 13.02 | 9.624 | 13.28 | 9.597 | 13.41 | 9.668 | 12.33 |
| pods started | 4.9 | 10.8 | 5.28 | 9.18 | 4.94 | 9.36 | 5.22 | 9.9 | 4.939 | 10.33 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 182.1 | 180.5 | 179.4 | 180.9 | 179.9 | 181.4 | 181.5 | 181.4 | 181.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 182.1 | 180.5 | 179.4 | 180.9 | 179.9 | 181.4 | 181.5 | 181.4 | 181.7 |
| CPU used with Omni's own (cores), mean | 2.193 | 2.184 | 1.971 | 1.977 | 2.009 | 2.006 | 2.119 | 2.119 | 2.151 | 2.146 |
| host CPU busy, the real machine under kind (%) | 64.94 | 65.06 | 58.54 | 58.8 | 59.53 | 59.62 | 62.8 | 63.25 | 63.94 | 64.16 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1658 | 1551 | -6.5% | -326.9 to +112.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5350 | 5477 | +2.4% | -365.6 to +620.9 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 27.33 | 19.6 | -28.3% | -9.569 to -5.902 | GAIN |
| failed requests (%) | 11.65 | 9.628 | -17.3% | -2.93 to -1.103 | GAIN |
| HPA replicas, mean | 9.686 | 12.82 | +32.4% | +2.662 to +3.608 | power given |
| pods started | 4.9 | 10.8 | +120.4% | +5.225 to +6.575 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.355e-16 to +2.546e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 182.1 | +0.0% | -0.2517 to +0.3638 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 182.1 | +0.0% | -0.2517 to +0.3638 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.193 | 2.184 | -0.4% | -0.02042 to +0.002419 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.94 | 65.06 | +0.2% | -0.1702 to +0.4176 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.144e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1894 | 1690 | -10.7% | -484.6 to +77.79 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5300 | 5273 | -0.5% | -276 to +222.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20 | 14.54 | -27.3% | -6.591 to -4.313 | GAIN |
| failed requests (%) | 6.936 | 6.32 | -8.9% | -0.9728 to -0.259 | GAIN |
| HPA replicas, mean | 9.592 | 13.02 | +35.7% | +2.791 to +4.062 | power given |
| pods started | 5.28 | 9.18 | +73.9% | +3.132 to +4.668 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.845e-16 to +1.603e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 179.4 | -0.6% | -1.416 to -0.7559 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 179.4 | -0.6% | -1.416 to -0.7559 | GAIN |
| CPU used with Omni's own (cores), mean | 1.971 | 1.977 | +0.3% | -0.001234 to +0.01348 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.54 | 58.8 | +0.4% | +0.07764 to +0.4396 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 2

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1743 | 1751 | +0.5% | -213.1 to +228.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5376 | 5286 | -1.7% | -385.2 to +205 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 21.21 | 15.21 | -28.3% | -7.155 to -4.848 | GAIN |
| failed requests (%) | 7.561 | 6.589 | -12.8% | -1.334 to -0.6095 | GAIN |
| HPA replicas, mean | 9.624 | 13.28 | +38.0% | +3.061 to +4.251 | power given |
| pods started | 4.94 | 9.36 | +89.5% | +3.673 to +5.167 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.481e-16 to +1.573e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 179.9 | -0.6% | -1.429 to -0.6216 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 179.9 | -0.6% | -1.429 to -0.6216 | GAIN |
| CPU used with Omni's own (cores), mean | 2.009 | 2.006 | -0.1% | -0.009915 to +0.004602 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.53 | 59.62 | +0.2% | -0.07487 to +0.2626 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

50 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1714 | 1503 | -12.3% | -337.9 to -84.51 | GAIN |
| response time (ms), 99th percentile | 4868 | 4667 | -4.1% | -502.1 to +101.9 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 24.12 | 17.35 | -28.1% | -8.158 to -5.397 | GAIN |
| failed requests (%) | 7.711 | 6.952 | -9.8% | -1.051 to -0.4676 | GAIN |
| HPA replicas, mean | 9.597 | 13.41 | +39.7% | +3.307 to +4.317 | power given |
| pods started | 5.22 | 9.9 | +89.7% | +4.043 to +5.317 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.2e-16 to +8.052e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181.5 | +0.0% | -0.3379 to +0.3715 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181.5 | +0.0% | -0.3379 to +0.3715 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.119 | 2.119 | -0.0% | -0.01065 to +0.01001 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.8 | 63.25 | +0.7% | +0.1949 to +0.6988 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

49 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1485 | 1586 | +6.8% | -96.31 to +299.4 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5042 | 4870 | -3.4% | -584.2 to +240.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.78 | 19.81 | -26.0% | -8.494 to -5.447 | GAIN |
| failed requests (%) | 11.91 | 10.34 | -13.2% | -2.247 to -0.8963 | GAIN |
| HPA replicas, mean | 9.668 | 12.33 | +27.5% | +2.165 to +3.155 | power given |
| pods started | 4.939 | 10.33 | +109.1% | +4.695 to +6.08 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.468e-16 to +1.568e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.4 | 181.7 | +0.1% | -0.0138 to +0.5544 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.4 | 181.7 | +0.1% | -0.0138 to +0.5544 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.151 | 2.146 | -0.2% | -0.01396 to +0.003658 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.94 | 64.16 | +0.3% | -0.006931 to +0.4391 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
