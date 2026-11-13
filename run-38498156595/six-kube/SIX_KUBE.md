# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1758 | 1858 | 3751 | 4773 | 2493 | 3209 | 2623 | 3051 | 4316 | 4462 | 2010 | 2591 |
| response time (ms), 99th percentile | 3643 | 3597 | 7330 | 7259 | 5810 | 7284 | 6055 | 5449 | 6315 | 6538 | 4627 | 4888 |
| time over the response line (% of samples) | 31.85 | 28.69 | 59.14 | 53.56 | 52.48 | 50.92 | 43.63 | 38.36 | 54.48 | 49.81 | 40.82 | 38.63 |
| failed requests (%) | 19.39 | 19.61 | 40.37 | 40.13 | 35.33 | 36.72 | 25.29 | 25.06 | 31.68 | 32.23 | 24.41 | 25.57 |
| HPA replicas, mean | 9.642 | 13.5 | 9.742 | 15.15 | 9.729 | 14.99 | 9.681 | 14.27 | 9.746 | 14.36 | 9.806 | 14.23 |
| pods started | 5.125 | 9.375 | 4.5 | 9.125 | 4.125 | 10.38 | 4.75 | 10.12 | 3.75 | 9.125 | 2.75 | 8.625 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 181.7 | 185.9 | 186.8 | 186 | 185.9 | 185.1 | 184.6 | 185.4 | 184.8 | 185 | 184.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 181.7 | 185.9 | 186.8 | 186 | 185.9 | 185.1 | 184.6 | 185.4 | 184.8 | 185 | 184.1 |
| CPU used with Omni's own (cores), mean | 2.124 | 2.149 | 2.565 | 2.586 | 2.54 | 2.559 | 2.435 | 2.45 | 2.483 | 2.499 | 2.388 | 2.415 |
| host CPU busy, the real machine under kind (%) | 62.65 | 64.07 | 76.42 | 77.38 | 75.42 | 76.78 | 71.04 | 72.23 | 73.64 | 75.51 | 71.75 | 75.2 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0.0375 | 0 | 0 | 0.1 | 0.1125 | 0.1625 | 0.1875 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1758 | 1858 | +5.7% | -950.6 to +1152 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3643 | 3597 | -1.2% | -895.9 to +805.2 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 31.85 | 28.69 | -9.9% | -6.007 to -0.32 | GAIN |
| failed requests (%) | 19.39 | 19.61 | +1.1% | -1.46 to +1.905 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.642 | 13.5 | +40.0% | +1.839 to +5.878 | power given |
| pods started | 5.125 | 9.375 | +82.9% | +1.692 to +6.808 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.317e-15 to +1.317e-15 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 181.3 | 181.7 | +0.2% | -0.5758 to +1.36 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.3 | 181.7 | +0.2% | -0.5758 to +1.36 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.124 | 2.149 | +1.1% | +0.005205 to +0.04346 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.65 | 64.07 | +2.3% | +0.95 to +1.893 | shown, not judged |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | power given |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | GAIN |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), EVEN (inside the noise) on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3751 | 4773 | +27.2% | -961.3 to +3006 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 7330 | 7259 | -1.0% | -1964 to +1820 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 59.14 | 53.56 | -9.4% | -7.648 to -3.513 | GAIN |
| failed requests (%) | 40.37 | 40.13 | -0.6% | -3.025 to +2.551 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.742 | 15.15 | +55.5% | +5.277 to +5.537 | power given |
| pods started | 4.5 | 9.125 | +102.8% | +3.738 to +5.512 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.174e-15 to +7.298e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 186.8 | +0.5% | +0.02098 to +1.866 | power given |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 186.8 | +0.5% | +0.02098 to +1.866 | power given |
| CPU used with Omni's own (cores), mean | 2.565 | 2.586 | +0.8% | +0.003744 to +0.03661 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 76.42 | 77.38 | +1.2% | +0.747 to +1.16 | shown, not judged |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | power given |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | GAIN |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2493 | 3209 | +28.7% | -1257 to +2689 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 5810 | 7284 | +25.4% | -1118 to +4064 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 52.48 | 50.92 | -3.0% | -4.78 to +1.653 | EVEN, inside the noise (cut) |
| failed requests (%) | 35.33 | 36.72 | +4.0% | -1.11 to +3.901 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.729 | 14.99 | +54.1% | +5.119 to +5.41 | power given |
| pods started | 4.125 | 10.38 | +151.5% | +5.006 to +7.494 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.431e-16 to +1.087e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 185.9 | -0.0% | -1.656 to +1.502 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 185.9 | -0.0% | -1.656 to +1.502 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.54 | 2.559 | +0.7% | +0.004692 to +0.03169 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 75.42 | 76.78 | +1.8% | +1.097 to +1.619 | shown, not judged |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | GAIN |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0.0375 | +0.0375 | -0.005775 to +0.08078 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2623 | 3051 | +16.3% | -430.1 to +1286 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6055 | 5449 | -10.0% | -1829 to +617.8 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 43.63 | 38.36 | -12.1% | -8.831 to -1.713 | GAIN |
| failed requests (%) | 25.29 | 25.06 | -0.9% | -0.9605 to +0.5093 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.681 | 14.27 | +47.4% | +3.021 to +6.158 | power given |
| pods started | 4.75 | 10.12 | +113.2% | +3.482 to +7.268 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.97e-16 to +3.97e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 185.1 | 184.6 | -0.3% | -2.332 to +1.174 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.1 | 184.6 | -0.3% | -2.332 to +1.174 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.435 | 2.45 | +0.6% | +0.001436 to +0.02964 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.04 | 72.23 | +1.7% | +0.5568 to +1.829 | shown, not judged |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | power given |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | GAIN |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4316 | 4462 | +3.4% | -1093 to +1385 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 6315 | 6538 | +3.5% | -944.1 to +1390 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 54.48 | 49.81 | -8.6% | -9.631 to +0.2867 | EVEN, inside the noise (cut) |
| failed requests (%) | 31.68 | 32.23 | +1.7% | -2.643 to +3.743 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.746 | 14.36 | +47.4% | +3.053 to +6.184 | power given |
| pods started | 3.75 | 9.125 | +143.3% | +3.43 to +7.32 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.037e-15 to +8.146e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.4 | 184.8 | -0.3% | -1.764 to +0.6429 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.4 | 184.8 | -0.3% | -1.764 to +0.6429 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.483 | 2.499 | +0.6% | -0.003042 to +0.03513 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 73.64 | 75.51 | +2.5% | +1.552 to +2.18 | shown, not judged |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | GAIN |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0.1 | 0.1125 | +12.5% | -0.01706 to +0.04206 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: GAIN on 1 (organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2010 | 2591 | +28.9% | -1027 to +2190 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 4627 | 4888 | +5.7% | -1125 to +1648 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 40.82 | 38.63 | -5.4% | -6.709 to +2.328 | EVEN, inside the noise (cut) |
| failed requests (%) | 24.41 | 25.57 | +4.8% | -0.2657 to +2.596 | EVEN, inside the noise (up) |
| HPA replicas, mean | 9.806 | 14.23 | +45.1% | +2.947 to +5.892 | power given |
| pods started | 2.75 | 8.625 | +213.6% | +5.579 to +6.171 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.716e-16 to +1.194e-15 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185 | 184.1 | -0.5% | -1.88 to +0.04794 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185 | 184.1 | -0.5% | -1.88 to +0.04794 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.388 | 2.415 | +1.1% | +0.0139 to +0.03976 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 71.75 | 75.2 | +4.8% | +3.132 to +3.762 | shown, not judged |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | power given |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | GAIN |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | LOSS |
| organism behind its window (s) | 0.1625 | 0.1875 | +15.4% | -0.09112 to +0.1411 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
