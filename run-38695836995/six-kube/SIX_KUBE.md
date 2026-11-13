# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1594 | 1523 | 2223 | 1861 | 1446 | 1349 | 1186 | 1206 | 1183 | 1227 | 1034 | 773.8 |
| response time (ms), 99th percentile | 3819 | 4506 | 6146 | 5987 | 3996 | 3973 | 3505 | 3606 | 3341 | 3466 | 4128 | 3662 |
| time over the response line (% of samples) | 31.03 | 20.64 | 22.96 | 15.99 | 14.36 | 10.07 | 17.61 | 13.04 | 20.52 | 13.66 | 14.45 | 9.781 |
| failed requests (%) | 13.95 | 11.56 | 8.599 | 6.807 | 4.284 | 3.996 | 5.943 | 5.297 | 8.47 | 5.299 | 5.405 | 4.495 |
| HPA replicas, mean | 9.641 | 12.2 | 9.655 | 13.85 | 9.556 | 12.47 | 9.533 | 12.47 | 9.528 | 11.71 | 9.6 | 12.07 |
| pods started | 5.4 | 11.1 | 5.1 | 10.3 | 5.7 | 9.3 | 5.6 | 9 | 5.6 | 10.5 | 5.2 | 10.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.4 | 182.6 | 181.2 | 178.6 | 177.6 | 179.4 | 179.3 | 179.8 | 179.3 | 178.7 | 178.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.4 | 182.6 | 181.2 | 178.6 | 177.6 | 179.4 | 179.3 | 179.8 | 179.3 | 178.7 | 178.7 |
| CPU used with Omni's own (cores), mean | 2.19 | 2.174 | 2.165 | 2.153 | 1.799 | 1.805 | 1.897 | 1.896 | 1.922 | 1.912 | 1.849 | 1.843 |
| host CPU busy, the real machine under kind (%) | 64.68 | 64.49 | 63.98 | 63.76 | 53.84 | 54.23 | 56.7 | 57 | 57.19 | 57.31 | 54.92 | 55.52 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1594 | 1523 | -4.5% | -595 to +452.7 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3819 | 4506 | +18.0% | -481.9 to +1856 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 31.03 | 20.64 | -33.5% | -15.73 to -5.052 | GAIN |
| failed requests (%) | 13.95 | 11.56 | -17.2% | -4.395 to -0.3945 | GAIN |
| HPA replicas, mean | 9.641 | 12.2 | +26.6% | +1.418 to +3.708 | power given |
| pods started | 5.4 | 11.1 | +105.6% | +3.704 to +7.696 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.4 | -0.5% | -1.936 to +0.2374 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.4 | -0.5% | -1.936 to +0.2374 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.19 | 2.174 | -0.7% | -0.04485 to +0.01301 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.68 | 64.49 | -0.3% | -0.8977 to +0.517 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.626e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.15e-05 to -8.141e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 2

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2223 | 1861 | -16.3% | -1427 to +702.9 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6146 | 5987 | -2.6% | -970.9 to +653.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 22.96 | 15.99 | -30.4% | -9.712 to -4.228 | GAIN |
| failed requests (%) | 8.599 | 6.807 | -20.8% | -3.244 to -0.3387 | GAIN |
| HPA replicas, mean | 9.655 | 13.85 | +43.5% | +3.211 to +5.187 | power given |
| pods started | 5.1 | 10.3 | +102.0% | +4.2 to +6.2 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.692e-16 to +3.363e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 181.2 | -0.8% | -2.412 to -0.3767 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 181.2 | -0.8% | -2.412 to -0.3767 | GAIN |
| CPU used with Omni's own (cores), mean | 2.165 | 2.153 | -0.5% | -0.02992 to +0.006415 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.98 | 63.76 | -0.3% | -0.5297 to +0.09575 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.242e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 4 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1446 | 1349 | -6.7% | -402.3 to +208.2 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 3996 | 3973 | -0.6% | -521 to +474.7 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.36 | 10.07 | -29.9% | -7.08 to -1.52 | GAIN |
| failed requests (%) | 4.284 | 3.996 | -6.7% | -1.209 to +0.6338 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.556 | 12.47 | +30.5% | +1.201 to +4.621 | power given |
| pods started | 5.7 | 9.3 | +63.2% | +1.907 to +5.293 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.395e-16 to +4.066e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 178.6 | 177.6 | -0.6% | -1.89 to -0.1075 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.6 | 177.6 | -0.6% | -1.89 to -0.1075 | GAIN |
| CPU used with Omni's own (cores), mean | 1.799 | 1.805 | +0.3% | -0.01314 to +0.02394 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 53.84 | 54.23 | +0.7% | -0.3498 to +1.116 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 2 (time over the response line (% of samples); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1186 | 1206 | +1.7% | -367.3 to +407.1 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3505 | 3606 | +2.9% | -595.5 to +796.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 17.61 | 13.04 | -26.0% | -7.795 to -1.352 | GAIN |
| failed requests (%) | 5.943 | 5.297 | -10.9% | -1.509 to +0.218 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.533 | 12.47 | +30.9% | +1.188 to +4.695 | power given |
| pods started | 5.6 | 9 | +60.7% | +1.289 to +5.511 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.4 | 179.3 | -0.0% | -0.9394 to +0.8877 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.4 | 179.3 | -0.0% | -0.9394 to +0.8877 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.897 | 1.896 | -0.0% | -0.01523 to +0.01342 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 56.7 | 57 | +0.5% | -0.3178 to +0.9142 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1183 | 1227 | +3.7% | -114.7 to +201.6 | EVEN, inside the noise (up) |
| response time (ms), 99th percentile | 3341 | 3466 | +3.7% | -685.5 to +935.4 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 20.52 | 13.66 | -33.4% | -12.19 to -1.536 | GAIN |
| failed requests (%) | 8.47 | 5.299 | -37.4% | -6.163 to -0.1782 | GAIN |
| HPA replicas, mean | 9.528 | 11.71 | +22.9% | +0.6067 to +3.752 | power given |
| pods started | 5.6 | 10.5 | +87.5% | +2.435 to +7.365 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.547e-15 to +1.259e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.3 | -0.3% | -1.608 to +0.5195 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.3 | -0.3% | -1.608 to +0.5195 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 1.922 | 1.912 | -0.5% | -0.03665 to +0.01643 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.19 | 57.31 | +0.2% | -0.504 to +0.7582 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 2 (response time (ms), 95th percentile; organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1034 | 773.8 | -25.2% | -475.3 to -45.07 | GAIN |
| response time (ms), 99th percentile | 4128 | 3662 | -11.3% | -1275 to +343.6 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 14.45 | 9.781 | -32.3% | -9.714 to +0.3667 | EVEN, inside the noise (cut) |
| failed requests (%) | 5.405 | 4.495 | -16.8% | -3.491 to +1.672 | EVEN, inside the noise (cut) |
| HPA replicas, mean | 9.6 | 12.07 | +25.7% | +0.9905 to +3.95 | power given |
| pods started | 5.2 | 10.9 | +109.6% | +3.412 to +7.988 | power given |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.99e-16 to +5.99e-16 | EVEN, the same |
| energy, parked workers still on at idle power (Wh, declared model) | 178.7 | 178.7 | +0.0% | -0.7391 to +0.885 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 178.7 | 178.7 | +0.0% | -0.7391 to +0.885 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 1.849 | 1.843 | -0.3% | -0.0271 to +0.0155 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 54.92 | 55.52 | +1.1% | -0.1901 to +1.38 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
