# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3728 | 2528 | 3384 | 2720 | 3430 | 2397 | 3145 | 2476 |
| response time (ms), 99th percentile | 5956 | 5235 | 5190 | 4954 | 5513 | 4733 | 5292 | 4872 |
| time over the response line (% of samples) | 59.81 | 59.04 | 50.82 | 48.95 | 53.64 | 52.2 | 48.84 | 49.15 |
| failed requests (%) | 46.48 | 50.43 | 38.48 | 41.97 | 40.52 | 44.56 | 38.24 | 40.81 |
| HPA replicas, mean | 9.864 | 12.28 | 9.831 | 12.56 | 9.831 | 12.65 | 9.817 | 12.72 |
| pods started | 3.065 | 5.823 | 3.581 | 7 | 3.532 | 6.79 | 3.694 | 7.032 |
| worker nodes in service, mean | 6 | 6 | 5.997 | 6 | 6 | 5.999 | 5.999 | 5.997 |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 278 | 275.6 | 276.4 | 276.3 | 276.7 | 276 | 276.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 278 | 275.5 | 276.4 | 276.3 | 276.7 | 276 | 276.4 |
| CPU used with Omni's own (cores), mean | 2.507 | 2.548 | 2.39 | 2.43 | 2.426 | 2.46 | 2.414 | 2.463 |
| host CPU busy, the real machine under kind (%) | 76.34 | 83.96 | 73.28 | 78.42 | 74.91 | 80.64 | 73.05 | 80.38 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.8871 | 1.234 | 0.3677 | 0.8468 | 0.7435 | 0.9887 | 0.4742 | 2.011 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3728 | 2528 | -32.2% | -1767 to -632.2 | GAIN |
| response time (ms), 99th percentile | 5956 | 5235 | -12.1% | -1238 to -204.9 | GAIN |
| time over the response line (% of samples) | 59.81 | 59.04 | -1.3% | -1.833 to +0.2953 | EVEN, inside the noise (cut) |
| failed requests (%) | 46.48 | 50.43 | +8.5% | +2.567 to +5.331 | LOSS |
| HPA replicas, mean | 9.864 | 12.28 | +24.5% | +2.017 to +2.821 | power given |
| pods started | 3.065 | 5.823 | +90.0% | +2.207 to +3.31 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -0.0003424 to +0.001056 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 277.5 | 278 | +0.2% | +0.1883 to +0.955 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 277.5 | 278 | +0.2% | +0.1957 to +0.9691 | power given |
| CPU used with Omni's own (cores), mean | 2.507 | 2.548 | +1.6% | +0.03056 to +0.05109 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.34 | 83.96 | +10.0% | +7.373 to +7.876 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 0.8871 | 1.234 | +39.1% | +0.2743 to +0.4193 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3384 | 2720 | -19.6% | -1300 to -28.43 | GAIN |
| response time (ms), 99th percentile | 5190 | 4954 | -4.5% | -724.7 to +254 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 50.82 | 48.95 | -3.7% | -2.655 to -1.088 | GAIN |
| failed requests (%) | 38.48 | 41.97 | +9.1% | +1.913 to +5.077 | LOSS |
| HPA replicas, mean | 9.831 | 12.56 | +27.8% | +2.22 to +3.238 | power given |
| pods started | 3.581 | 7 | +95.5% | +2.628 to +4.211 | power given |
| worker nodes in service, mean | 5.997 | 6 | +0.1% | -0.002545 to +0.009327 | EVEN, inside the noise (up) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.6 | 276.4 | +0.3% | +0.4581 to +1.156 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.5 | 276.4 | +0.3% | +0.5124 to +1.307 | power given |
| CPU used with Omni's own (cores), mean | 2.39 | 2.43 | +1.7% | +0.03015 to +0.05136 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.28 | 78.42 | +7.0% | +4.859 to +5.412 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.3677 | 0.8468 | +130.3% | +0.4146 to +0.5434 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 4 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (failed requests (%)), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3430 | 2397 | -30.1% | -1600 to -464.8 | GAIN |
| response time (ms), 99th percentile | 5513 | 4733 | -14.2% | -1324 to -236.3 | GAIN |
| time over the response line (% of samples) | 53.64 | 52.2 | -2.7% | -2.081 to -0.7808 | GAIN |
| failed requests (%) | 40.52 | 44.56 | +10.0% | +2.767 to +5.313 | LOSS |
| HPA replicas, mean | 9.831 | 12.65 | +28.6% | +2.353 to +3.278 | power given |
| pods started | 3.532 | 6.79 | +92.2% | +2.531 to +3.985 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.001918 to +0.00139 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.3 | 276.7 | +0.2% | -0.1453 to +1.009 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.3 | 276.7 | +0.2% | -0.1732 to +1.021 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.426 | 2.46 | +1.4% | +0.0244 to +0.0432 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.91 | 80.64 | +7.6% | +5.474 to +5.97 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7435 | 0.9887 | +33.0% | +0.1579 to +0.3324 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3145 | 2476 | -21.3% | -1182 to -156.1 | GAIN |
| response time (ms), 99th percentile | 5292 | 4872 | -7.9% | -946.9 to +106.4 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 48.84 | 49.15 | +0.6% | -1.057 to +1.674 | EVEN, inside the noise (up) |
| failed requests (%) | 38.24 | 40.81 | +6.7% | +1.032 to +4.105 | LOSS |
| HPA replicas, mean | 9.817 | 12.72 | +29.6% | +2.419 to +3.395 | power given |
| pods started | 3.694 | 7.032 | +90.4% | +2.672 to +4.006 | power given |
| worker nodes in service, mean | 5.999 | 5.997 | -0.0% | -0.00725 to +0.003846 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 276.5 | +0.2% | -0.08524 to +1.084 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 276.4 | +0.2% | -0.1837 to +1.078 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.414 | 2.463 | +2.0% | +0.03311 to +0.06488 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.05 | 80.38 | +10.0% | +6.932 to +7.72 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.4742 | 2.011 | +324.1% | -0.3327 to +3.407 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
