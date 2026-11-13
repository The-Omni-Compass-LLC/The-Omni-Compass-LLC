# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3204 | 3872 | 4055 | 4501 | 3691 | 3789 | 3173 | 3205 |
| response time (ms), 99th percentile | 5431 | 5783 | 6151 | 6391 | 6014 | 6046 | 5171 | 5379 |
| time over the response line (% of samples) | 53.54 | 52.94 | 52.42 | 52.23 | 53.13 | 52.67 | 45.7 | 47.19 |
| failed requests (%) | 42.21 | 42.98 | 37.51 | 39.37 | 39.74 | 40.92 | 35.43 | 37.48 |
| HPA replicas, mean | 9.837 | 14.92 | 9.823 | 14.47 | 9.837 | 14.55 | 9.809 | 14.85 |
| pods started | 3.371 | 8.903 | 3.742 | 9.306 | 3.339 | 8.919 | 3.758 | 9.468 |
| worker nodes in service, mean | 6 | 6 | 6 | 5.996 | 6 | 5.999 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 276.6 | 276.6 | 276.8 | 276.7 | 276.7 | 275.3 | 276.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 276.6 | 276.6 | 276.7 | 276.7 | 276.7 | 275.3 | 276.4 |
| CPU used with Omni's own (cores), mean | 2.41 | 2.458 | 2.435 | 2.466 | 2.431 | 2.466 | 2.383 | 2.448 |
| host CPU busy, the real machine under kind (%) | 73.43 | 81.2 | 74.1 | 79.09 | 74.74 | 80.67 | 72.15 | 79.89 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 0.9081 | 1.279 | 0.3952 | 0.8371 | 0.7097 | 1.81 | 0.4774 | 1.077 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 3 (response time (ms), 95th percentile; response time (ms), 99th percentile; organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 2

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3204 | 3872 | +20.8% | +220.4 to +1115 | LOSS |
| response time (ms), 99th percentile | 5431 | 5783 | +6.5% | +4.197 to +699.1 | LOSS |
| time over the response line (% of samples) | 53.54 | 52.94 | -1.1% | -1.51 to +0.321 | EVEN, inside the noise (cut) |
| failed requests (%) | 42.21 | 42.98 | +1.8% | -0.1669 to +1.715 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.837 | 14.92 | +51.7% | +4.788 to +5.374 | power given |
| pods started | 3.371 | 8.903 | +164.1% | +5.089 to +5.976 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.256e-16 to +2.105e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 276 | 276.6 | +0.2% | +0.2672 to +1.006 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276 | 276.6 | +0.2% | +0.2672 to +1.006 | power given |
| CPU used with Omni's own (cores), mean | 2.41 | 2.458 | +2.0% | +0.03752 to +0.0585 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.43 | 81.2 | +10.6% | +7.501 to +8.039 | shown, not judged |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | power given |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | LOSS |
| organism behind its window (s) | 0.9081 | 1.279 | +40.9% | +0.2724 to +0.4696 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4055 | 4501 | +11.0% | -61.39 to +954.5 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6151 | 6391 | +3.9% | -71.08 to +550.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.42 | 52.23 | -0.4% | -1.045 to +0.6728 | EVEN, inside the noise (cut) |
| failed requests (%) | 37.51 | 39.37 | +5.0% | +0.3587 to +3.355 | LOSS |
| HPA replicas, mean | 9.823 | 14.47 | +47.3% | +4.179 to +5.118 | power given |
| pods started | 3.742 | 9.306 | +148.7% | +4.942 to +6.187 | power given |
| worker nodes in service, mean | 6 | 5.996 | -0.1% | -0.0117 to +0.003796 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.6 | 276.8 | +0.1% | -0.1291 to +0.4601 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.6 | 276.7 | +0.0% | -0.3814 to +0.4745 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.435 | 2.466 | +1.3% | +0.02301 to +0.03971 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.1 | 79.09 | +6.7% | +4.775 to +5.201 | shown, not judged |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | power given |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | GAIN |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | LOSS |
| organism behind its window (s) | 0.3952 | 0.8371 | +111.8% | +0.3839 to +0.4999 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 7

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3691 | 3789 | +2.7% | -472.5 to +668.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6014 | 6046 | +0.5% | -445.3 to +509 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 53.13 | 52.67 | -0.9% | -1.293 to +0.3763 | EVEN, inside the noise (cut) |
| failed requests (%) | 39.74 | 40.92 | +3.0% | -0.06662 to +2.42 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.837 | 14.55 | +47.9% | +4.263 to +5.159 | power given |
| pods started | 3.339 | 8.919 | +167.1% | +4.916 to +6.245 | power given |
| worker nodes in service, mean | 6 | 5.999 | -0.0% | -0.002971 to +0.0009637 | EVEN, inside the noise (cut) |
| energy, parked workers still on at idle power (Wh, declared model) | 276.7 | 276.7 | -0.0% | -0.3894 to +0.3759 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 276.7 | 276.7 | -0.0% | -0.4358 to +0.3618 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.431 | 2.466 | +1.4% | +0.02301 to +0.04642 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 74.74 | 80.67 | +7.9% | +5.642 to +6.224 | shown, not judged |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | GAIN |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.7097 | 1.81 | +155.0% | -0.4962 to +2.696 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3173 | 3205 | +1.0% | -374.7 to +438.8 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5171 | 5379 | +4.0% | -169.9 to +586.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 45.7 | 47.19 | +3.3% | -0.05208 to +3.034 | EVEN, inside the noise (up) |
| failed requests (%) | 35.43 | 37.48 | +5.8% | +0.5122 to +3.601 | LOSS |
| HPA replicas, mean | 9.809 | 14.85 | +51.4% | +4.776 to +5.314 | power given |
| pods started | 3.758 | 9.468 | +151.9% | +5.365 to +6.054 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.927e-16 to -9.538e-18 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 275.3 | 276.4 | +0.4% | +0.7609 to +1.438 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 275.3 | 276.4 | +0.4% | +0.7609 to +1.438 | power given |
| CPU used with Omni's own (cores), mean | 2.383 | 2.448 | +2.7% | +0.05114 to +0.07813 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.15 | 79.89 | +10.7% | +7.371 to +8.12 | shown, not judged |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | power given |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | GAIN |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | LOSS |
| organism behind its window (s) | 0.4774 | 1.077 | +125.7% | +0.5308 to +0.6692 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
