# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 775.2 | 478 | 1778 | 1246 | 1466 | 711.2 | 2400 | 1666 | 2180 | 1380 | 1281 | 799 |
| response time (ms), 99th percentile | 2175 | 1431 | 5590 | 5298 | 4542 | 3597 | 6161 | 5570 | 4925 | 4810 | 3388 | 2363 |
| time over the response line (% of samples) | 14.2 | 7.877 | 29.33 | 15.8 | 21.56 | 8.947 | 36.92 | 19.68 | 41.89 | 19.09 | 24.24 | 13.48 |
| failed requests (%) | 4.36 | 4.258 | 9.301 | 7.849 | 4.924 | 4.257 | 10.12 | 8.712 | 10.28 | 8.418 | 7.934 | 7.381 |
| HPA replicas, mean | 9.518 | 9.502 | 9.802 | 9.825 | 9.741 | 9.725 | 9.733 | 9.781 | 9.805 | 9.804 | 9.6 | 9.642 |
| pods started | 6 | 6.125 | 3.25 | 2.75 | 4.25 | 4.5 | 3.5 | 2.625 | 2.875 | 2.75 | 5.5 | 4.75 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.9 | 187.4 | 186.7 | 184.1 | 183.4 | 188.7 | 188.6 | 190.4 | 189.7 | 183.9 | 183.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.9 | 187.4 | 186.7 | 184.1 | 183.4 | 188.7 | 188.6 | 190.4 | 189.7 | 183.9 | 183.2 |
| CPU used with Omni's own (cores), mean | 1.951 | 1.938 | 2.666 | 2.625 | 2.365 | 2.298 | 2.803 | 2.779 | 2.951 | 2.929 | 2.303 | 2.269 |
| host CPU busy, the real machine under kind (%) | 58.11 | 57.98 | 77.65 | 76.63 | 69.6 | 68.49 | 81.09 | 80.8 | 85.18 | 84.4 | 67.75 | 67.1 |
| organism work | 2.084e+10 | 2.084e+10 | 2.159e+10 | 2.159e+10 | 6.707e+10 | 6.707e+10 | 2.137e+10 | 2.137e+10 | 6.94e+10 | 6.94e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.479e+10 | 1.48e+10 | 1.915e+10 | 1.916e+10 | 1.016e+13 | 1.016e+13 | 5.591e+10 | 5.592e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.957 | 1.951 | 4.28 | 4.275 | 1.391 | 1.385 | 2.293 | 2.289 | 2.428 | 2.426 | 2.389 | 2.384 |
| organism work per energy | 1.409 | 1.408 | 1.128 | 1.127 | 0.006603 | 0.006603 | 0.3823 | 0.3822 | 0.006798 | 0.006798 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.0125 | 0.0125 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 2, worse on 2 (organism energy (J); organism work per energy), inside the noise on 7

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 775.2 | 478 | -38.3% | -408.8 to -185.7 | better |
| response time (ms), 99th percentile | 2175 | 1431 | -34.2% | -1510 to +22.16 | better (inside the noise) |
| time over the response line (% of samples) | 14.2 | 7.877 | -44.5% | -12.66 to +0.01261 | better (inside the noise) |
| failed requests (%) | 4.36 | 4.258 | -2.3% | -0.6097 to +0.4061 | better (inside the noise) |
| HPA replicas, mean | 9.518 | 9.502 | -0.2% | -0.1344 to +0.1025 | better (inside the noise) |
| pods started | 6 | 6.125 | +2.1% | -1.094 to +1.344 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.908e-16 to +5.467e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.8 | 179.9 | +0.1% | -0.5656 to +0.8068 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.8 | 179.9 | +0.1% | -0.5656 to +0.8068 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.951 | 1.938 | -0.6% | -0.04985 to +0.02511 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 58.11 | 57.98 | -0.2% | -1.149 to +0.8887 | shown, not judged (more or less is not better by itself) |
| organism work | 2.084e+10 | 2.084e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.479e+10 | 1.48e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.957 | 1.951 | -0.3% | -0.005503 to -0.005503 | better |
| organism work per energy | 1.409 | 1.408 | -0.1% | -0.001007 to -0.001007 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1778 | 1246 | -29.9% | -1307 to +245 | better (inside the noise) |
| response time (ms), 99th percentile | 5590 | 5298 | -5.2% | -2001 to +1417 | better (inside the noise) |
| time over the response line (% of samples) | 29.33 | 15.8 | -46.1% | -18.86 to -8.179 | better |
| failed requests (%) | 9.301 | 7.849 | -15.6% | -2.614 to -0.2882 | better |
| HPA replicas, mean | 9.802 | 9.825 | +0.2% | -0.04582 to +0.09246 | WORSE (inside the noise) |
| pods started | 3.25 | 2.75 | -15.4% | -1.841 to +0.8408 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.939e-16 to +7.939e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 187.4 | 186.7 | -0.4% | -1.465 to +0.06654 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.4 | 186.7 | -0.4% | -1.465 to +0.06654 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.666 | 2.625 | -1.6% | -0.07305 to -0.01002 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 77.65 | 76.63 | -1.3% | -1.681 to -0.3481 | shown, not judged (more or less is not better by itself) |
| organism work | 2.159e+10 | 2.159e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.915e+10 | 1.916e+10 | +0.1% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 4.28 | 4.275 | -0.1% | -0.005288 to -0.005288 | better |
| organism work per energy | 1.128 | 1.127 | -0.1% | -0.0006228 to -0.0006228 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1466 | 711.2 | -51.5% | -1054 to -455.4 | better |
| response time (ms), 99th percentile | 4542 | 3597 | -20.8% | -1778 to -111.8 | better |
| time over the response line (% of samples) | 21.56 | 8.947 | -58.5% | -17.48 to -7.739 | better |
| failed requests (%) | 4.924 | 4.257 | -13.5% | -1.447 to +0.1133 | better (inside the noise) |
| HPA replicas, mean | 9.741 | 9.725 | -0.2% | -0.08321 to +0.05023 | better (inside the noise) |
| pods started | 4.25 | 4.5 | +5.9% | -1.072 to +1.572 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.436e-16 to +1.332e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.1 | 183.4 | -0.4% | -1.371 to +0.006805 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.1 | 183.4 | -0.4% | -1.371 to +0.006805 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.365 | 2.298 | -2.8% | -0.0953 to -0.03906 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.6 | 68.49 | -1.6% | -1.769 to -0.4506 | shown, not judged (more or less is not better by itself) |
| organism work | 6.707e+10 | 6.707e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 1.391 | 1.385 | -0.4% | -0.006206 to -0.006206 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -6.877e-09 to -6.877e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2400 | 1666 | -30.6% | -1084 to -383.6 | better |
| response time (ms), 99th percentile | 6161 | 5570 | -9.6% | -1655 to +471.3 | better (inside the noise) |
| time over the response line (% of samples) | 36.92 | 19.68 | -46.7% | -24.01 to -10.49 | better |
| failed requests (%) | 10.12 | 8.712 | -13.9% | -2.455 to -0.3691 | better |
| HPA replicas, mean | 9.733 | 9.781 | +0.5% | -0.06994 to +0.1666 | WORSE (inside the noise) |
| pods started | 3.5 | 2.625 | -25.0% | -2.794 to +1.044 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.614e-16 to +5.614e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 188.7 | 188.6 | -0.0% | -0.341 to +0.1656 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.7 | 188.6 | -0.0% | -0.341 to +0.1656 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.803 | 2.779 | -0.9% | -0.05194 to +0.003839 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.09 | 80.8 | -0.4% | -0.9948 to +0.4004 | shown, not judged (more or less is not better by itself) |
| organism work | 2.137e+10 | 2.137e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.591e+10 | 5.592e+10 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.293 | 2.289 | -0.2% | -0.003516 to -0.003516 | better |
| organism work per energy | 0.3823 | 0.3822 | -0.0% | -7.234e-05 to -7.234e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2180 | 1380 | -36.7% | -1036 to -564.3 | better |
| response time (ms), 99th percentile | 4925 | 4810 | -2.3% | -1522 to +1293 | better (inside the noise) |
| time over the response line (% of samples) | 41.89 | 19.09 | -54.4% | -28.31 to -17.29 | better |
| failed requests (%) | 10.28 | 8.418 | -18.1% | -3.173 to -0.5543 | better |
| HPA replicas, mean | 9.805 | 9.804 | -0.0% | -0.1099 to +0.1082 | better (inside the noise) |
| pods started | 2.875 | 2.75 | -4.3% | -1.937 to +1.687 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.876e-16 to +8.876e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 190.4 | 189.7 | -0.3% | -1.58 to +0.3043 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.4 | 189.7 | -0.3% | -1.58 to +0.3043 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.951 | 2.929 | -0.7% | -0.06084 to +0.01681 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.18 | 84.4 | -0.9% | -1.322 to -0.2411 | shown, not judged (more or less is not better by itself) |
| organism work | 6.94e+10 | 6.94e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +1.058e+07 to +1.058e+07 | WORSE |
| organism time over the line (% of steps) | 2.428 | 2.426 | -0.1% | -0.002659 to -0.002659 | better |
| organism work per energy | 0.006798 | 0.006798 | -0.0% | -7.046e-09 to -7.046e-09 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1281 | 799 | -37.6% | -715.8 to -248.3 | better |
| response time (ms), 99th percentile | 3388 | 2363 | -30.2% | -2146 to +97.14 | better (inside the noise) |
| time over the response line (% of samples) | 24.24 | 13.48 | -44.4% | -18.34 to -3.182 | better |
| failed requests (%) | 7.934 | 7.381 | -7.0% | -1.413 to +0.306 | better (inside the noise) |
| HPA replicas, mean | 9.6 | 9.642 | +0.4% | -0.04032 to +0.123 | WORSE (inside the noise) |
| pods started | 5.5 | 4.75 | -13.6% | -2.633 to +1.133 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.49e-16 to +1.215e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.9 | 183.2 | -0.4% | -1.758 to +0.3218 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.9 | 183.2 | -0.4% | -1.758 to +0.3218 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.303 | 2.269 | -1.5% | -0.08204 to +0.01391 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 67.75 | 67.1 | -1.0% | -1.981 to +0.6754 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4.232e+07 to +4.232e+07 | WORSE |
| organism time over the line (% of steps) | 2.389 | 2.384 | -0.2% | -0.00513 to -0.00513 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -5.274e-08 to -5.274e-08 | WORSE |
| organism behind its window (s) | 0.0125 | 0.0125 | +0.0% | -0.04469 to +0.04469 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
