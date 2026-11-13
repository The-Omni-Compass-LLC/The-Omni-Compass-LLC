# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2394 | 3315 | 2547 | 2320 | 2534 | 3104 | 3546 | 3427 | 1956 | 2794 |
| response time (ms), 99th percentile | 4666 | 6485 | 5225 | 4544 | 5435 | 6065 | 6085 | 6098 | 5117 | 6338 |
| time over the response line (% of samples) | 50.26 | 46.29 | 37.68 | 35.82 | 51.25 | 48.35 | 35.58 | 30.41 | 48.39 | 48.69 |
| failed requests (%) | 29.51 | 29.26 | 24.77 | 25.06 | 37.08 | 36.77 | 13.19 | 13.37 | 28.08 | 30.91 |
| HPA replicas, mean | 9.748 | 13.96 | 9.639 | 12.99 | 9.701 | 13.65 | 9.635 | 14.36 | 9.812 | 13.83 |
| pods started | 3.875 | 8.5 | 4.875 | 8.625 | 4.625 | 8.5 | 5.375 | 11 | 2.75 | 6.625 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185.4 | 183.7 | 184.3 | 185.2 | 185.8 | 184.2 | 184.1 | 185.6 | 186.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 185.4 | 183.7 | 184.3 | 185.2 | 185.8 | 184.2 | 184.1 | 185.6 | 186.3 |
| CPU used with Omni's own (cores), mean | 2.488 | 2.506 | 2.308 | 2.332 | 2.46 | 2.481 | 2.385 | 2.408 | 2.527 | 2.574 |
| host CPU busy, the real machine under kind (%) | 72.95 | 74.38 | 68.75 | 69.92 | 73.76 | 74.81 | 70.26 | 72.32 | 76.16 | 80.04 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.025 | 0.0125 | 0.0125 | 0 | 0.0125 | 0.0125 | 0.1 | 0.1 | 0.1875 | 0.2 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 2 (response time (ms), 99th percentile; organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2394 | 3315 | +38.5% | -38.41 to +1880 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4666 | 6485 | +39.0% | +180.2 to +3458 | LOSS |
| time over the response line (% of samples) | 50.26 | 46.29 | -7.9% | -5.739 to -2.197 | GAIN |
| failed requests (%) | 29.51 | 29.26 | -0.8% | -1.681 to +1.183 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.748 | 13.96 | +43.2% | +2.722 to +5.696 | power given |
| pods started | 3.875 | 8.5 | +119.4% | +2.841 to +6.409 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.171e-15 to +1.394e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 185.4 | -0.1% | -1.601 to +1.301 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 185.4 | -0.1% | -1.601 to +1.301 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.488 | 2.506 | +0.7% | +0.007506 to +0.02809 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 72.95 | 74.38 | +2.0% | +0.9638 to +1.891 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0.025 | 0.0125 | -50.0% | -0.06609 to +0.04109 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2547 | 2320 | -8.9% | -1948 to +1494 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5225 | 4544 | -13.0% | -2644 to +1282 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 37.68 | 35.82 | -4.9% | -5.94 to +2.226 | EVEN, inside the noise (cut) |
| failed requests (%) | 24.77 | 25.06 | +1.2% | -1.147 to +1.724 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.639 | 12.99 | +34.7% | +1.03 to +5.664 | power given |
| pods started | 4.875 | 8.625 | +76.9% | +1.232 to +6.268 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.939e-16 to +7.939e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 184.3 | +0.4% | -0.3104 to +1.611 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 184.3 | +0.4% | -0.3104 to +1.611 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.308 | 2.332 | +1.1% | +0.003816 to +0.04583 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 68.75 | 69.92 | +1.7% | +0.7496 to +1.585 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0.0125 | 0 | -100.0% | -0.04206 to +0.01706 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2534 | 3104 | +22.5% | -469.9 to +1608 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5435 | 6065 | +11.6% | -1187 to +2449 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 51.25 | 48.35 | -5.7% | -7.191 to +1.393 | EVEN, inside the noise (cut) |
| failed requests (%) | 37.08 | 36.77 | -0.8% | -2.693 to +2.07 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.701 | 13.65 | +40.7% | +2.05 to +5.847 | power given |
| pods started | 4.625 | 8.5 | +83.8% | +1.409 to +6.341 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.25e-16 to +8.47e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 185.8 | +0.4% | -0.4298 to +1.756 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 185.8 | +0.4% | -0.4298 to +1.756 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.46 | 2.481 | +0.9% | +0.01021 to +0.0318 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.76 | 74.81 | +1.4% | +0.6556 to +1.441 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.0125 | 0.0125 | +0.0% | -0.04469 to +0.04469 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3546 | 3427 | -3.4% | -1114 to +875.4 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6085 | 6098 | +0.2% | -421.3 to +447.6 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 35.58 | 30.41 | -14.5% | -8.714 to -1.64 | GAIN |
| failed requests (%) | 13.19 | 13.37 | +1.3% | -1.839 to +2.193 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.635 | 14.36 | +49.1% | +3.857 to +5.595 | power given |
| pods started | 5.375 | 11 | +104.7% | +4.081 to +7.169 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.498e-16 to +1.238e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.2 | 184.1 | -0.1% | -1.358 to +1.094 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.2 | 184.1 | -0.1% | -1.358 to +1.094 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.385 | 2.408 | +1.0% | +0.003494 to +0.04205 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 70.26 | 72.32 | +2.9% | +1.62 to +2.504 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.1 | +0.0% | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 2 (failed requests (%); organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1956 | 2794 | +42.8% | -129.5 to +1806 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5117 | 6338 | +23.9% | -428.9 to +2871 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 48.39 | 48.69 | +0.6% | -4.743 to +5.328 | EVEN, inside the noise (up) |
| failed requests (%) | 28.08 | 30.91 | +10.1% | +0.5214 to +5.132 | LOSS |
| HPA replicas, mean | 9.812 | 13.83 | +40.9% | +3.262 to +4.768 | power given |
| pods started | 2.75 | 6.625 | +140.9% | +2.237 to +5.513 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.264e-15 to +1.042e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 186.3 | +0.4% | -0.5358 to +2.074 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 186.3 | +0.4% | -0.5358 to +2.074 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.527 | 2.574 | +1.9% | +0.0193 to +0.07583 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.16 | 80.04 | +5.1% | +3.278 to +4.475 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.1875 | 0.2 | +6.7% | -0.07037 to +0.09537 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- Distribution / Specialized

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
