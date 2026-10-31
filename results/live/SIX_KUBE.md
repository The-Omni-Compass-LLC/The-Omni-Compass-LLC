# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, STEADY or LOSS, by what the gauge is for and never by its sign (a resource spent that rose reads **power given**, never a loss; the key: `docs/HOW_TO_READ_THE_RESULTS.md`). The aim is lower for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). The aim is higher for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower (656 muscles): native | The whole tower (656 muscles): omni | The four stacked, duplicates kept (1,226): native | The four stacked, duplicates kept (1,226): omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3967 | 2653 | 2440 | 1767 | 1951 | 1482 | 2830 | 1943 | 2085 | 1247 | 3703 | 2803 |
| response time (ms), 99th percentile | 6847 | 6803 | 5070 | 4977 | 3487 | 3123 | 6635 | 6333 | 3462 | 2724 | 6354 | 6724 |
| time over the response line (% of samples) | 41.04 | 26.66 | 28.36 | 15.49 | 21.59 | 10.38 | 40.7 | 21.05 | 25.79 | 14.7 | 55.6 | 42.95 |
| failed requests (%) | 14.93 | 13.3 | 5.718 | 4.96 | 3.75 | 3.249 | 11.1 | 9.331 | 12.76 | 9.126 | 31.72 | 27.56 |
| HPA replicas, mean | 9.846 | 9.893 | 9.65 | 9.147 | 9.691 | 8.981 | 9.786 | 9.864 | 9.54 | 9.242 | 9.767 | 9.778 |
| pods started | 2.8 | 1.8 | 4.4 | 3.8 | 4.2 | 4.8 | 3.6 | 2.4 | 5.8 | 4.8 | 3.2 | 3 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.873 | 6 | 5.885 | 6 | 5.997 | 6 | 5.9 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 191 | 190.8 | 184.9 | 184.5 | 183.3 | 182.7 | 190.6 | 189.5 | 182.7 | 182.1 | 191.9 | 191.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191 | 190.8 | 184.9 | 182 | 183.3 | 180.4 | 190.6 | 189.4 | 182.7 | 180.1 | 191.9 | 191.5 |
| CPU used with Omni's own (cores), mean | 2.993 | 2.977 | 2.459 | 2.398 | 2.33 | 2.268 | 2.96 | 2.926 | 2.22 | 2.169 | 3.186 | 3.146 |
| host CPU busy, the real machine under kind (%) | 86.29 | 85.98 | 71.57 | 70.68 | 67.77 | 66.65 | 85.72 | 84.85 | 64.89 | 64.35 | 90.74 | 90.1 |
| organism work | 1.675e+10 | 1.675e+10 | 1.665e+10 | 1.665e+10 | 5.708e+10 | 5.708e+10 | 1.674e+10 | 1.674e+10 | 5.728e+10 | 5.728e+10 | 1.075e+11 | 1.075e+11 |
| organism energy (J) | 1.129e+10 | 1.128e+10 | 1.097e+10 | 1.096e+10 | 6.237e+10 | 6.225e+10 | 1.114e+10 | 1.113e+10 | 6.473e+10 | 6.461e+10 | 9.862e+10 | 9.847e+10 |
| organism time over the line (% of steps) | 2.087 | 2.059 | 3.515 | 3.499 | 1.667 | 1.634 | 2.37 | 2.35 | 2.546 | 2.532 | 2.535 | 2.512 |
| organism work per energy | 1.484 | 1.485 | 1.518 | 1.519 | 0.9151 | 0.9169 | 1.503 | 1.504 | 0.8849 | 0.8866 | 1.09 | 1.091 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: toward their aims on 6, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3967 | 2653 | -33.1% | -3240 to +610.3 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 6847 | 6803 | -0.6% | -809.5 to +721.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 41.04 | 26.66 | -35.0% | -18.49 to -10.27 | GAIN |
| failed requests (%) | 14.93 | 13.3 | -10.9% | -4.624 to +1.373 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.846 | 9.893 | +0.5% | -0.03468 to +0.1276 | STEADY, inside the noise (up) |
| pods started | 2.8 | 1.8 | -35.7% | -1.878 to -0.1222 | GAIN |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.257e-15 to +1.257e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 191 | 190.8 | -0.1% | -1.168 to +0.7358 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191 | 190.8 | -0.1% | -1.168 to +0.7358 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.993 | 2.977 | -0.5% | -0.05753 to +0.02608 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 86.29 | 85.98 | -0.4% | -1.223 to +0.6021 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.675e+10 | 1.675e+10 | +0.0% | +1312 to +1312 | GAIN |
| organism energy (J) | 1.129e+10 | 1.128e+10 | -0.1% | -1.049e+07 to -1.049e+07 | GAIN |
| organism time over the line (% of steps) | 2.087 | 2.059 | -1.3% | -0.02778 to -0.02778 | GAIN |
| organism work per energy | 1.484 | 1.485 | +0.1% | +0.001381 to +0.001381 | GAIN |

### Physics / Robotics / Autonomous: toward their aims on 6, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2440 | 1767 | -27.6% | -1232 to -113.9 | GAIN |
| response time (ms), 99th percentile | 5070 | 4977 | -1.8% | -1121 to +933.9 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 28.36 | 15.49 | -45.4% | -24.83 to -0.9005 | GAIN |
| failed requests (%) | 5.718 | 4.96 | -13.3% | -1.98 to +0.4628 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.65 | 9.147 | -5.2% | -1.56 to +0.554 | STEADY, inside the noise (cut) |
| pods started | 4.4 | 3.8 | -13.6% | -2.483 to +1.283 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 5.873 | -2.1% | -0.3431 to +0.08898 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.9 | 184.5 | -0.2% | -1.55 to +0.7196 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.9 | 182 | -1.6% | -8.362 to +2.415 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.459 | 2.398 | -2.5% | -0.07981 to -0.04232 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 71.57 | 70.68 | -1.2% | -2.052 to +0.2695 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.665e+10 | 1.665e+10 | +0.0% | +1310 to +1310 | GAIN |
| organism energy (J) | 1.097e+10 | 1.096e+10 | -0.1% | -1.01e+07 to -1.007e+07 | GAIN |
| organism time over the line (% of steps) | 3.515 | 3.499 | -0.5% | -0.0159 to -0.0159 | GAIN |
| organism work per energy | 1.518 | 1.519 | +0.1% | +0.001395 to +0.001398 | GAIN |

### Energy / Facility / Industrial: toward their aims on 6, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1951 | 1482 | -24.0% | -869.8 to -66.92 | GAIN |
| response time (ms), 99th percentile | 3487 | 3123 | -10.5% | -1086 to +356.6 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 21.59 | 10.38 | -51.9% | -20.43 to -2.003 | GAIN |
| failed requests (%) | 3.75 | 3.249 | -13.4% | -1.662 to +0.6606 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.691 | 8.981 | -7.3% | -1.666 to +0.2471 | STEADY, inside the noise (cut) |
| pods started | 4.2 | 4.8 | +14.3% | -0.8155 to +2.015 | STEADY, inside the noise (up) |
| worker nodes in service, mean | 6 | 5.885 | -1.9% | -0.3113 to +0.08181 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 182.7 | -0.3% | -1.574 to +0.3982 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 180.4 | -1.6% | -7.257 to +1.456 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.33 | 2.268 | -2.6% | -0.1104 to -0.01306 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 67.77 | 66.65 | -1.7% | -2.365 to +0.1213 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.708e+10 | 5.708e+10 | +0.0% | +1312 to +1312 | GAIN |
| organism energy (J) | 6.237e+10 | 6.225e+10 | -0.2% | -1.236e+08 to -1.236e+08 | GAIN |
| organism time over the line (% of steps) | 1.667 | 1.634 | -2.0% | -0.03251 to -0.03251 | GAIN |
| organism work per energy | 0.9151 | 0.9169 | +0.2% | +0.001817 to +0.001817 | GAIN |

### Distribution / Specialized: toward their aims on 6, away from them on 0, inside the noise on 7

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2830 | 1943 | -31.3% | -1467 to -306 | GAIN |
| response time (ms), 99th percentile | 6635 | 6333 | -4.6% | -1563 to +958.7 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 40.7 | 21.05 | -48.3% | -24.98 to -14.33 | GAIN |
| failed requests (%) | 11.1 | 9.331 | -15.9% | -3.947 to +0.4088 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.786 | 9.864 | +0.8% | -0.07229 to +0.2287 | STEADY, inside the noise (up) |
| pods started | 3.6 | 2.4 | -33.3% | -3.588 to +1.188 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 5.997 | -0.1% | -0.01251 to +0.005883 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.6 | 189.5 | -0.6% | -2.45 to +0.05682 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.6 | 189.4 | -0.7% | -2.594 to +0.06735 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.96 | 2.926 | -1.2% | -0.08749 to +0.01878 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 85.72 | 84.85 | -1.0% | -2.489 to +0.7393 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.674e+10 | 1.674e+10 | +0.0% | +1312 to +1312 | GAIN |
| organism energy (J) | 1.114e+10 | 1.113e+10 | -0.1% | -1.022e+07 to -1.022e+07 | GAIN |
| organism time over the line (% of steps) | 2.37 | 2.35 | -0.8% | -0.01978 to -0.01978 | GAIN |
| organism work per energy | 1.503 | 1.504 | +0.1% | +0.00138 to +0.00138 | GAIN |

### The whole tower (656 muscles): toward their aims on 4, away from them on 0, inside the noise on 9

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2085 | 1247 | -40.2% | -1947 to +270.1 | STEADY, inside the noise (cut) |
| response time (ms), 99th percentile | 3462 | 2724 | -21.3% | -2356 to +879.8 | STEADY, inside the noise (cut) |
| time over the response line (% of samples) | 25.79 | 14.7 | -43.0% | -27.45 to +5.27 | STEADY, inside the noise (cut) |
| failed requests (%) | 12.76 | 9.126 | -28.5% | -10 to +2.743 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.54 | 9.242 | -3.1% | -1.025 to +0.4276 | STEADY, inside the noise (cut) |
| pods started | 5.8 | 4.8 | -17.2% | -3.483 to +1.483 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 5.9 | -1.7% | -0.2778 to +0.07715 | STEADY, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 182.1 | -0.3% | -1.319 to +0.1882 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 180.1 | -1.4% | -5.564 to +0.3997 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.22 | 2.169 | -2.3% | -0.1143 to +0.01234 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 64.89 | 64.35 | -0.8% | -2.192 to +1.108 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 5.728e+10 | 5.728e+10 | +0.0% | +1310 to +1310 | GAIN |
| organism energy (J) | 6.473e+10 | 6.461e+10 | -0.2% | -1.238e+08 to -1.238e+08 | GAIN |
| organism time over the line (% of steps) | 2.546 | 2.532 | -0.5% | -0.01334 to -0.01334 | GAIN |
| organism work per energy | 0.8849 | 0.8866 | +0.2% | +0.001696 to +0.001696 | GAIN |

### The four stacked, duplicates kept (1,226): toward their aims on 5, away from them on 0, inside the noise on 6

5 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3703 | 2803 | -24.3% | -1522 to -278.9 | GAIN |
| response time (ms), 99th percentile | 6354 | 6724 | +5.8% | -2257 to +2996 | STEADY, inside the noise (up) |
| time over the response line (% of samples) | 55.6 | 42.95 | -22.7% | -19.2 to -6.1 | GAIN |
| failed requests (%) | 31.72 | 27.56 | -13.1% | -10.45 to +2.119 | STEADY, inside the noise (cut) |
| HPA replicas, mean | 9.767 | 9.778 | +0.1% | -0.188 to +0.2088 | STEADY, inside the noise (up) |
| pods started | 3.2 | 3 | -6.2% | -3.164 to +2.764 | STEADY, inside the noise (cut) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.635e-15 to +1.635e-15 | STEADY, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 191.9 | 191.5 | -0.2% | -1.394 to +0.4899 | STEADY, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.9 | 191.5 | -0.2% | -1.394 to +0.4899 | STEADY, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 3.186 | 3.146 | -1.2% | -0.09983 to +0.02028 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| host CPU busy, the real machine under kind (%) | 90.74 | 90.1 | -0.7% | -1.954 to +0.6643 | shown, not judged (more or less is neither GAIN nor LOSS by itself) |
| organism work | 1.075e+11 | 1.075e+11 | -0.0% | +0 to +0 | STEADY, the same |
| organism energy (J) | 9.862e+10 | 9.847e+10 | -0.2% | -1.484e+08 to -1.484e+08 | GAIN |
| organism time over the line (% of steps) | 2.535 | 2.512 | -0.9% | -0.02311 to -0.02311 | GAIN |
| organism work per energy | 1.09 | 1.091 | +0.2% | +0.001643 to +0.001643 | GAIN |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and Simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
