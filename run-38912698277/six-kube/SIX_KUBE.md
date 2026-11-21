# The organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1661 | 1415 | 1794 | 1632 | 1647 | 1446 | 1881 | 1771 |
| response time (ms), 99th percentile | 5114 | 4969 | 5447 | 5413 | 4780 | 4664 | 4913 | 5294 |
| time over the response line (% of samples) | 26.92 | 18.15 | 20.32 | 14.59 | 16.98 | 12.31 | 28.33 | 20.59 |
| failed requests (%) | 11.29 | 9.118 | 6.943 | 6.284 | 5.713 | 5.131 | 9.205 | 8.253 |
| HPA replicas, mean | 9.67 | 12.62 | 9.643 | 13.49 | 9.589 | 13.03 | 9.628 | 13.56 |
| pods started | 5.048 | 10.37 | 4.935 | 9.79 | 5.242 | 9.194 | 4.903 | 9.79 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.8 | 181.1 | 180.5 | 179.6 | 178.8 | 182.2 | 182.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.8 | 181.1 | 180.5 | 179.6 | 178.8 | 182.2 | 182.1 |
| CPU used with Omni's own (cores), mean | 2.164 | 2.152 | 2.043 | 2.049 | 1.895 | 1.902 | 2.18 | 2.185 |
| host CPU busy, the real machine under kind (%) | 64.13 | 64.03 | 60.56 | 61.01 | 56.35 | 56.66 | 64.49 | 65.07 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1661 | 1415 | -14.8% | -391.8 to -101 | GAIN |
| response time (ms), 99th percentile | 5114 | 4969 | -2.8% | -522 to +233.3 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 26.92 | 18.15 | -32.6% | -10.48 to -7.062 | GAIN |
| failed requests (%) | 11.29 | 9.118 | -19.3% | -2.987 to -1.366 | GAIN |
| HPA replicas, mean | 9.67 | 12.62 | +30.5% | +2.52 to +3.374 | power given |
| pods started | 5.048 | 10.37 | +105.4% | +4.842 to +5.803 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.167e-16 to +4.421e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.8 | 181.8 | +0.0% | -0.2921 to +0.3302 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.8 | 181.8 | +0.0% | -0.2921 to +0.3302 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.164 | 2.152 | -0.5% | -0.02036 to -0.003431 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.13 | 64.03 | -0.2% | -0.3476 to +0.1545 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.619e+05 to +8.623e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.144e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1794 | 1632 | -9.0% | -343.9 to +20.61 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5447 | 5413 | -0.6% | -321.8 to +253.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 20.32 | 14.59 | -28.2% | -6.738 to -4.722 | GAIN |
| failed requests (%) | 6.943 | 6.284 | -9.5% | -0.9237 to -0.3942 | GAIN |
| HPA replicas, mean | 9.643 | 13.49 | +39.9% | +3.349 to +4.339 | power given |
| pods started | 4.935 | 9.79 | +98.4% | +4.218 to +5.492 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.688e-16 to -1.048e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.5 | -0.4% | -0.9771 to -0.3037 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.5 | -0.4% | -0.9771 to -0.3037 | GAIN |
| CPU used with Omni's own (cores), mean | 2.043 | 2.049 | +0.3% | -0.0008194 to +0.01222 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.56 | 61.01 | +0.7% | +0.2865 to +0.612 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.245e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 1

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1647 | 1446 | -12.2% | -380 to -20.93 | GAIN |
| response time (ms), 99th percentile | 4780 | 4664 | -2.4% | -387.3 to +153.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 16.98 | 12.31 | -27.5% | -5.642 to -3.702 | GAIN |
| failed requests (%) | 5.713 | 5.131 | -10.2% | -0.8744 to -0.2905 | GAIN |
| HPA replicas, mean | 9.589 | 13.03 | +35.9% | +2.87 to +4.006 | power given |
| pods started | 5.242 | 9.194 | +75.4% | +3.292 to +4.612 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.087e-16 to -2.514e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.6 | 178.8 | -0.4% | -1.12 to -0.4636 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.6 | 178.8 | -0.4% | -1.12 to -0.4636 | GAIN |
| CPU used with Omni's own (cores), mean | 1.895 | 1.902 | +0.4% | +0.0004441 to +0.01415 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.35 | 56.66 | +0.6% | +0.1086 to +0.5121 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1881 | 1771 | -5.9% | -238.9 to +18.5 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4913 | 5294 | +7.7% | +66.68 to +694.4 | LOSS |
| time over the response line (% of samples) | 28.33 | 20.59 | -27.3% | -9.089 to -6.401 | GAIN |
| failed requests (%) | 9.205 | 8.253 | -10.3% | -1.313 to -0.5915 | GAIN |
| HPA replicas, mean | 9.628 | 13.56 | +40.9% | +3.447 to +4.425 | power given |
| pods started | 4.903 | 9.79 | +99.7% | +4.221 to +5.553 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.094e-16 to +1.229e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 182.1 | -0.0% | -0.4027 to +0.227 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 182.1 | -0.0% | -0.4027 to +0.227 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.18 | 2.185 | +0.2% | -0.001814 to +0.01266 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.49 | 65.07 | +0.9% | +0.3868 to +0.7738 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
