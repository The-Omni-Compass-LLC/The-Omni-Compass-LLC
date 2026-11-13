# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1307 | 1050 | 1563 | 1210 | 1276 | 908.3 | 1656 | 1663 | 1762 | 1765 | 1572 | 1472 |
| response time (ms), 99th percentile | 4572 | 4636 | 4950 | 4258 | 4148 | 3820 | 4574 | 5217 | 4394 | 4473 | 4385 | 4289 |
| time over the response line (% of samples) | 19.7 | 14.53 | 20.27 | 14.29 | 14.15 | 10.03 | 26.11 | 19 | 28.66 | 20.45 | 23.98 | 21.32 |
| failed requests (%) | 8.054 | 8.062 | 7.396 | 6.991 | 4.396 | 4.579 | 8.543 | 7.515 | 12.24 | 10.39 | 10.46 | 11.12 |
| HPA replicas, mean | 9.644 | 13.77 | 9.578 | 13.29 | 9.567 | 12.59 | 9.638 | 13.86 | 9.597 | 13.27 | 9.65 | 13.79 |
| pods started | 5.25 | 11 | 5.5 | 9.875 | 5.375 | 9 | 4.75 | 10.38 | 5.25 | 10.12 | 5.286 | 11.43 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.7 | 180.4 | 179.3 | 177.7 | 177.9 | 182.9 | 182.2 | 181 | 180.8 | 181.1 | 181.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.7 | 180.4 | 179.3 | 177.7 | 177.9 | 182.9 | 182.2 | 181 | 180.8 | 181.1 | 181.1 |
| CPU used with Omni's own (cores), mean | 2.048 | 2.045 | 1.969 | 1.962 | 1.764 | 1.766 | 2.19 | 2.188 | 2.08 | 2.075 | 2.08 | 2.102 |
| host CPU busy, the real machine under kind (%) | 60.89 | 61.27 | 58.57 | 58.68 | 52.47 | 52.69 | 64.31 | 65.04 | 61.82 | 61.99 | 61.81 | 62.64 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: lower on 3 (time over the response line (% of samples); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1307 | 1050 | -19.7% | -614.4 to +99.76 | lower (inside the noise) |
| response time (ms), 99th percentile | 4572 | 4636 | +1.4% | -1554 to +1683 | higher (inside the noise) |
| time over the response line (% of samples) | 19.7 | 14.53 | -26.2% | -8.789 to -1.555 | lower |
| failed requests (%) | 8.054 | 8.062 | +0.1% | -1.21 to +1.227 | higher (inside the noise) |
| HPA replicas, mean | 9.644 | 13.77 | +42.8% | +2.545 to +5.712 | higher |
| pods started | 5.25 | 11 | +109.5% | +3.354 to +8.146 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.962e-16 to +1.118e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.7 | -0.1% | -1.397 to +0.861 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.7 | -0.1% | -1.397 to +0.861 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.048 | 2.045 | -0.2% | -0.04976 to +0.04226 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.89 | 61.27 | +0.6% | -1.263 to +2.021 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.614e+05 to +8.63e+05 | higher |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | lower |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.154e-05 to -8.139e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: lower on 6 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 2

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1563 | 1210 | -22.6% | -691.6 to -14.71 | lower |
| response time (ms), 99th percentile | 4950 | 4258 | -14.0% | -1935 to +550.5 | lower (inside the noise) |
| time over the response line (% of samples) | 20.27 | 14.29 | -29.5% | -9.529 to -2.442 | lower |
| failed requests (%) | 7.396 | 6.991 | -5.5% | -1.447 to +0.6355 | lower (inside the noise) |
| HPA replicas, mean | 9.578 | 13.29 | +38.7% | +1.757 to +5.662 | higher |
| pods started | 5.5 | 9.875 | +79.5% | +2.099 to +6.651 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.489e-15 to -3.977e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.4 | 179.3 | -0.6% | -2.024 to -0.2054 | lower |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.4 | 179.3 | -0.6% | -2.024 to -0.2054 | lower |
| CPU used with Omni's own (cores), mean | 1.969 | 1.962 | -0.4% | -0.03011 to +0.01557 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.57 | 58.68 | +0.2% | -0.6402 to +0.8698 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | higher |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | lower |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.242e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1276 | 908.3 | -28.8% | -815.4 to +79.1 | lower (inside the noise) |
| response time (ms), 99th percentile | 4148 | 3820 | -7.9% | -950.2 to +294.3 | lower (inside the noise) |
| time over the response line (% of samples) | 14.15 | 10.03 | -29.1% | -7.75 to -0.4957 | lower |
| failed requests (%) | 4.396 | 4.579 | +4.2% | -0.6371 to +1.003 | higher (inside the noise) |
| HPA replicas, mean | 9.567 | 12.59 | +31.6% | +0.8411 to +5.21 | higher |
| pods started | 5.375 | 9 | +67.4% | +0.9832 to +6.267 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.462e-15 to +1.017e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 177.7 | 177.9 | +0.1% | -0.4928 to +0.8645 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 177.7 | 177.9 | +0.1% | -0.4928 to +0.8645 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.764 | 1.766 | +0.1% | -0.04074 to +0.04586 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 52.47 | 52.69 | +0.4% | -0.7274 to +1.159 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | lower |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 4 (response time (ms), 99th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1656 | 1663 | +0.4% | -349.2 to +363.8 | higher (inside the noise) |
| response time (ms), 99th percentile | 4574 | 5217 | +14.1% | +45.12 to +1242 | higher |
| time over the response line (% of samples) | 26.11 | 19 | -27.2% | -10.93 to -3.294 | lower |
| failed requests (%) | 8.543 | 7.515 | -12.0% | -1.781 to -0.2754 | lower |
| HPA replicas, mean | 9.638 | 13.86 | +43.8% | +2.751 to +5.696 | higher |
| pods started | 4.75 | 10.38 | +118.4% | +3.532 to +7.718 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.132e-15 to +2.435e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 182.2 | -0.4% | -1.572 to +0.2658 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 182.2 | -0.4% | -1.572 to +0.2658 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.19 | 2.188 | -0.1% | -0.01441 to +0.01198 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 64.31 | 65.04 | +1.1% | +0.303 to +1.143 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | higher |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | lower |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1762 | 1765 | +0.2% | -321.9 to +327.6 | higher (inside the noise) |
| response time (ms), 99th percentile | 4394 | 4473 | +1.8% | -727 to +885.1 | higher (inside the noise) |
| time over the response line (% of samples) | 28.66 | 20.45 | -28.6% | -14.31 to -2.111 | lower |
| failed requests (%) | 12.24 | 10.39 | -15.1% | -3.704 to +0.01677 | lower (inside the noise) |
| HPA replicas, mean | 9.597 | 13.27 | +38.3% | +1.57 to +5.778 | higher |
| pods started | 5.25 | 10.12 | +92.9% | +2.577 to +7.173 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.522e-15 to +4.122e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 180.8 | -0.1% | -1.397 to +0.9108 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 180.8 | -0.1% | -1.397 to +0.9108 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.08 | 2.075 | -0.2% | -0.03874 to +0.02868 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.82 | 61.99 | +0.3% | -0.3434 to +0.6857 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | lower |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: lower on 1 (organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 6

7 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1572 | 1472 | -6.4% | -1064 to +862.1 | lower (inside the noise) |
| response time (ms), 99th percentile | 4385 | 4289 | -2.2% | -1581 to +1389 | lower (inside the noise) |
| time over the response line (% of samples) | 23.98 | 21.32 | -11.1% | -14.8 to +9.466 | lower (inside the noise) |
| failed requests (%) | 10.46 | 11.12 | +6.3% | -4.431 to +5.743 | higher (inside the noise) |
| HPA replicas, mean | 9.65 | 13.79 | +42.9% | +2.357 to +5.923 | higher |
| pods started | 5.286 | 11.43 | +116.2% | +2.24 to +10.05 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.528e-15 to +7.672e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 181.1 | -0.0% | -1.563 to +1.553 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 181.1 | -0.0% | -1.563 to +1.553 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.08 | 2.102 | +1.1% | -0.05807 to +0.1025 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.81 | 62.64 | +1.3% | -1.179 to +2.842 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4.002e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | lower |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.989e-09 to -4.984e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
