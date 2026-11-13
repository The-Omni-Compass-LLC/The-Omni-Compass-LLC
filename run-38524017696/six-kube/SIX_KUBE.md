# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4079 | 4717 | 3687 | 4375 | 3905 | 3744 | 3617 | 3915 |
| response time (ms), 99th percentile | 6472 | 7091 | 6451 | 6511 | 6268 | 6169 | 6026 | 6539 |
| time over the response line (% of samples) | 62.88 | 62.84 | 59.47 | 57.98 | 52.8 | 51.63 | 53.45 | 53.65 |
| failed requests (%) | 47.05 | 48.6 | 47 | 46.21 | 38.54 | 38.33 | 41.69 | 42.91 |
| HPA replicas, mean | 9.87 | 15.29 | 9.857 | 14.63 | 9.817 | 14.73 | 9.826 | 14.78 |
| pods started | 2.857 | 8.643 | 3.143 | 7.893 | 3.929 | 8.964 | 3.571 | 9.107 |
| worker nodes in service, mean | 5.999 | 6 | 6 | 6 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 278.6 | 277 | 277.1 | 276.9 | 277.4 | 276.9 | 277.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.2 | 278.6 | 277 | 277.1 | 276.9 | 277.4 | 276.9 | 277.4 |
| CPU used with Omni's own (cores), mean | 2.549 | 2.591 | 2.464 | 2.492 | 2.458 | 2.495 | 2.465 | 2.513 |
| host CPU busy, the real machine under kind (%) | 77.64 | 85.55 | 75.81 | 80.5 | 75.49 | 81.17 | 74.61 | 81.7 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 1 | 1.246 | 0.3714 | 0.9179 | 0.7143 | 1.068 | 0.4893 | 1.079 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 7

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4079 | 4717 | +15.6% | -326.1 to +1602 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6472 | 7091 | +9.6% | -130.1 to +1367 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 62.88 | 62.84 | -0.1% | -1.972 to +1.891 | EVEN, inside the noise (cut) |
| failed requests (%) | 47.05 | 48.6 | +3.3% | -0.8452 to +3.949 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.87 | 15.29 | +54.9% | +5.252 to +5.592 | power given |
| pods started | 2.857 | 8.643 | +202.5% | +5.342 to +6.229 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001038 to +0.003201 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 278.3 | 278.6 | +0.1% | -0.1389 to +0.7756 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 278.2 | 278.6 | +0.1% | -0.1318 to +0.834 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.549 | 2.591 | +1.7% | +0.02615 to +0.05883 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 77.64 | 85.55 | +10.2% | +7.5 to +8.328 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 1 | 1.246 | +24.6% | +0.1199 to +0.3729 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3687 | 4375 | +18.7% | -17.83 to +1394 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6451 | 6511 | +0.9% | -489.1 to +608.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 59.47 | 57.98 | -2.5% | -2.594 to -0.3957 | GAIN |
| failed requests (%) | 47 | 46.21 | -1.7% | -2.048 to +0.4546 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.857 | 14.63 | +48.4% | +4.061 to +5.482 | power given |
| pods started | 3.143 | 7.893 | +151.1% | +3.749 to +5.751 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.503e-15 to -4.002e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 277 | 277.1 | +0.0% | -0.3917 to +0.5057 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277 | 277.1 | +0.0% | -0.3917 to +0.5057 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.464 | 2.492 | +1.1% | +0.01711 to +0.03749 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.81 | 80.5 | +6.2% | +4.361 to +5.029 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.3714 | 0.9179 | +147.1% | +0.4278 to +0.6651 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 7

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3905 | 3744 | -4.1% | -992.7 to +671.8 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6268 | 6169 | -1.6% | -789.8 to +591.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 52.8 | 51.63 | -2.2% | -2.459 to +0.1252 | EVEN, inside the noise (cut) |
| failed requests (%) | 38.54 | 38.33 | -0.5% | -2.019 to +1.598 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.817 | 14.73 | +50.1% | +4.294 to +5.535 | power given |
| pods started | 3.929 | 8.964 | +128.2% | +4.131 to +5.94 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002767 to +0.0008973 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.4 | +0.2% | -0.1421 to +1.103 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.4 | +0.2% | -0.1728 to +1.077 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.495 | +1.5% | +0.02485 to +0.0499 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.49 | 81.17 | +7.5% | +5.294 to +6.071 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7143 | 1.068 | +49.5% | +0.2462 to +0.461 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3617 | 3915 | +8.2% | -54.46 to +649 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6026 | 6539 | +8.5% | -106.6 to +1133 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.45 | 53.65 | +0.4% | -1.229 to +1.626 | EVEN, inside the noise (up) |
| failed requests (%) | 41.69 | 42.91 | +2.9% | -0.1038 to +2.535 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.826 | 14.78 | +50.4% | +4.455 to +5.446 | power given |
| pods started | 3.571 | 9.107 | +155.0% | +4.961 to +6.11 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.902e-16 to +6.549e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.4 | +0.2% | -0.1171 to +1.138 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.4 | +0.2% | -0.1171 to +1.138 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.465 | 2.513 | +1.9% | +0.03254 to +0.06205 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.61 | 81.7 | +9.5% | +6.739 to +7.443 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.4893 | 1.079 | +120.4% | +0.4733 to +0.7053 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
