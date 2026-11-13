# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2963 | 2615 | 3379 | 2691 | 2778 | 2098 | 3162 | 2651 |
| response time (ms), 99th percentile | 4754 | 4886 | 6163 | 5715 | 4256 | 3930 | 4801 | 5011 |
| time over the response line (% of samples) | 42.06 | 41.15 | 54.99 | 54.26 | 35.13 | 34 | 51.67 | 50.77 |
| failed requests (%) | 30.23 | 32.17 | 43.37 | 48.21 | 26.81 | 29.8 | 42.93 | 44.42 |
| HPA replicas, mean | 9.786 | 11.45 | 9.854 | 13.16 | 9.789 | 11.73 | 9.835 | 13.57 |
| pods started | 4.3 | 7.1 | 3.4 | 7 | 4.1 | 7.1 | 3.2 | 7.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275 | 276.6 | 277.3 | 273 | 273.3 | 275.9 | 276.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 275 | 276.6 | 277.3 | 273 | 273.3 | 275.9 | 276.9 |
| CPU used with Omni's own (cores), mean | 2.32 | 2.371 | 2.428 | 2.473 | 2.189 | 2.222 | 2.395 | 2.443 |
| host CPU busy, the real machine under kind (%) | 70.42 | 78.31 | 75.1 | 80.16 | 66.92 | 72.63 | 73.01 | 80.3 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.88 | 1.22 | 0.51 | 1.02 | 0.7 | 0.86 | 0.53 | 1.09 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2963 | 2615 | -11.7% | -1661 to +964.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4754 | 4886 | +2.8% | -726.3 to +990.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 42.06 | 41.15 | -2.2% | -5.358 to +3.535 | EVEN, inside the noise (cut) |
| failed requests (%) | 30.23 | 32.17 | +6.4% | -0.7316 to +4.62 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.786 | 11.45 | +17.0% | +0.5828 to +2.753 | power given |
| pods started | 4.3 | 7.1 | +65.1% | +0.9593 to +4.641 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.009e-15 to +2.324e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 274.6 | 275 | +0.1% | -0.6388 to +1.393 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 274.6 | 275 | +0.1% | -0.6388 to +1.393 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.32 | 2.371 | +2.2% | +0.01189 to +0.09067 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.42 | 78.31 | +11.2% | +6.777 to +9.002 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 0.88 | 1.22 | +38.6% | +0.1083 to +0.5717 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3379 | 2691 | -20.4% | -1811 to +435.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6163 | 5715 | -7.3% | -1481 to +585.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 54.99 | 54.26 | -1.3% | -2.088 to +0.6209 | EVEN, inside the noise (cut) |
| failed requests (%) | 43.37 | 48.21 | +11.1% | +2.435 to +7.236 | LOSS |
| HPA replicas, mean | 9.854 | 13.16 | +33.6% | +2.319 to +4.3 | power given |
| pods started | 3.4 | 7 | +105.9% | +1.308 to +5.892 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.126e-15 to +1.304e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 277.3 | +0.3% | +0.03911 to +1.41 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 277.3 | +0.3% | +0.03911 to +1.41 | power given |
| CPU used with Omni's own (cores), mean | 2.428 | 2.473 | +1.8% | +0.02046 to +0.06904 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.1 | 80.16 | +6.7% | +4.48 to +5.626 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.51 | 1.02 | +100.0% | +0.2522 to +0.7678 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2778 | 2098 | -24.5% | -2201 to +840.5 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4256 | 3930 | -7.7% | -1527 to +874.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 35.13 | 34 | -3.2% | -2.351 to +0.1025 | EVEN, inside the noise (cut) |
| failed requests (%) | 26.81 | 29.8 | +11.1% | -0.386 to +6.353 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.789 | 11.73 | +19.8% | +0.4927 to +3.381 | power given |
| pods started | 4.1 | 7.1 | +73.2% | +0.8147 to +5.185 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.939e-16 to +1.249e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 273 | 273.3 | +0.1% | -0.3895 to +0.9633 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273 | 273.3 | +0.1% | -0.3895 to +0.9633 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.189 | 2.222 | +1.5% | +0.01248 to +0.05211 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.92 | 72.63 | +8.5% | +5.026 to +6.393 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7 | 0.86 | +22.9% | +0.01225 to +0.3078 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3162 | 2651 | -16.2% | -1580 to +559.1 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4801 | 5011 | +4.4% | -1224 to +1644 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 51.67 | 50.77 | -1.7% | -2.672 to +0.8834 | EVEN, inside the noise (cut) |
| failed requests (%) | 42.93 | 44.42 | +3.5% | -0.858 to +3.821 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.835 | 13.57 | +38.0% | +2.676 to +4.794 | power given |
| pods started | 3.2 | 7.2 | +125.0% | +2.455 to +5.545 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.744e-15 to +1.922e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.9 | 276.9 | +0.4% | +0.2402 to +1.92 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.9 | 276.9 | +0.4% | +0.2402 to +1.92 | power given |
| CPU used with Omni's own (cores), mean | 2.395 | 2.443 | +2.0% | +0.02412 to +0.07292 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.01 | 80.3 | +10.0% | +6.492 to +8.081 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.53 | 1.09 | +105.7% | +0.3436 to +0.7764 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
