# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2444 | 2050 | 3768 | 2664 | 3916 | 2423 | 3838 | 2343 |
| response time (ms), 99th percentile | 3972 | 3783 | 5952 | 5325 | 5978 | 5061 | 5861 | 5278 |
| time over the response line (% of samples) | 40.6 | 39.96 | 55.42 | 53.67 | 51.7 | 49.67 | 61.78 | 60.29 |
| failed requests (%) | 30.93 | 33.47 | 40.71 | 45.64 | 38.9 | 41.76 | 51.1 | 52.83 |
| HPA replicas, mean | 9.807 | 12.56 | 9.834 | 12.33 | 9.836 | 11.74 | 9.868 | 12.26 |
| pods started | 4.107 | 7.679 | 3.643 | 5.857 | 3.286 | 5.643 | 2.714 | 4.929 |
| worker nodes in service, mean | 6 | 6 | 5.999 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.7 | 276.6 | 277.1 | 275.8 | 276.8 | 276.9 | 277.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 274.7 | 276.5 | 277.1 | 275.8 | 276.8 | 276.9 | 277.4 |
| CPU used with Omni's own (cores), mean | 2.281 | 2.346 | 2.458 | 2.49 | 2.403 | 2.442 | 2.485 | 2.523 |
| host CPU busy, the real machine under kind (%) | 69.44 | 77.48 | 75.24 | 80.01 | 73.97 | 79.69 | 75.9 | 83.08 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.8143 | 1.089 | 0.3786 | 0.8643 | 0.7036 | 0.9429 | 0.5214 | 1.086 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2444 | 2050 | -16.1% | -941.3 to +152.3 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3972 | 3783 | -4.8% | -708.3 to +330.5 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 40.6 | 39.96 | -1.6% | -1.867 to +0.5929 | EVEN, inside the noise (cut) |
| failed requests (%) | 30.93 | 33.47 | +8.2% | +0.8073 to +4.279 | LOSS |
| HPA replicas, mean | 9.807 | 12.56 | +28.1% | +2.06 to +3.445 | power given |
| pods started | 4.107 | 7.679 | +87.0% | +2.679 to +4.464 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -0.001311 to +0.000425 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 273.9 | 274.7 | +0.3% | -0.4335 to +1.932 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 273.9 | 274.7 | +0.3% | -0.4465 to +1.918 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.281 | 2.346 | +2.8% | +0.04344 to +0.08649 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 69.44 | 77.48 | +11.6% | +7.539 to +8.538 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 0.8143 | 1.089 | +33.8% | +0.214 to +0.336 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3768 | 2664 | -29.3% | -1988 to -218.8 | GAIN |
| response time (ms), 99th percentile | 5952 | 5325 | -10.5% | -1396 to +141.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 55.42 | 53.67 | -3.2% | -2.957 to -0.5556 | GAIN |
| failed requests (%) | 40.71 | 45.64 | +12.1% | +2.741 to +7.125 | LOSS |
| HPA replicas, mean | 9.834 | 12.33 | +25.4% | +1.724 to +3.272 | power given |
| pods started | 3.643 | 5.857 | +60.8% | +1.189 to +3.239 | power given |
| worker nodes in service, mean | 5.999 | 6 | +0.0% | -0.001292 to +0.001625 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 277.1 | +0.2% | -0.09075 to +1.232 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.5 | 277.1 | +0.2% | -0.1157 to +1.268 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.458 | 2.49 | +1.3% | +0.01771 to +0.04677 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.24 | 80.01 | +6.3% | +4.43 to +5.116 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.3786 | 0.8643 | +128.3% | +0.3787 to +0.5927 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), EVEN (inside the noise) on 0

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3916 | 2423 | -38.1% | -2302 to -684.2 | GAIN |
| response time (ms), 99th percentile | 5978 | 5061 | -15.3% | -1766 to -69.07 | GAIN |
| time over the response line (% of samples) | 51.7 | 49.67 | -3.9% | -2.785 to -1.276 | GAIN |
| failed requests (%) | 38.9 | 41.76 | +7.4% | +1.063 to +4.662 | LOSS |
| HPA replicas, mean | 9.836 | 11.74 | +19.3% | +1.138 to +2.659 | power given |
| pods started | 3.286 | 5.643 | +71.7% | +1.328 to +3.386 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.046e-15 to +9.388e-17 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.8 | 276.8 | +0.3% | +0.5462 to +1.375 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.8 | 276.8 | +0.3% | +0.5462 to +1.375 | power given |
| CPU used with Omni's own (cores), mean | 2.403 | 2.442 | +1.6% | +0.02312 to +0.05484 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.97 | 79.69 | +7.7% | +5.315 to +6.127 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7036 | 0.9429 | +34.0% | +0.1278 to +0.3508 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3838 | 2343 | -39.0% | -2351 to -638.2 | GAIN |
| response time (ms), 99th percentile | 5861 | 5278 | -9.9% | -1726 to +560.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 61.78 | 60.29 | -2.4% | -2.549 to -0.4328 | GAIN |
| failed requests (%) | 51.1 | 52.83 | +3.4% | -0.1759 to +3.638 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.868 | 12.26 | +24.3% | +1.634 to +3.16 | power given |
| pods started | 2.714 | 4.929 | +81.6% | +1.235 to +3.194 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.914e-16 to +5.011e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.9 | 277.4 | +0.2% | -0.1116 to +1.12 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.9 | 277.4 | +0.2% | -0.1116 to +1.12 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.485 | 2.523 | +1.6% | +0.02017 to +0.057 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.9 | 83.08 | +9.5% | +6.697 to +7.669 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.5214 | 1.086 | +108.2% | +0.4734 to +0.6551 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
