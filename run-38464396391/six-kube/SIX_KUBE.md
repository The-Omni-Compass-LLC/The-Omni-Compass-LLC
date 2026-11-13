# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1676 | 1569 | 1749 | 1669 | 1547 | 1462 | 1584 | 1513 | 1969 | 1937 | 1520 | 1253 |
| response time (ms), 99th percentile | 4629 | 5222 | 5004 | 4980 | 5051 | 4786 | 4901 | 4575 | 5066 | 5110 | 4755 | 4916 |
| time over the response line (% of samples) | 29.58 | 21.16 | 18.95 | 13.52 | 17.82 | 13.16 | 24.1 | 17.53 | 28.89 | 22.08 | 24.05 | 16.67 |
| failed requests (%) | 13.12 | 11.64 | 6.571 | 5.733 | 6.047 | 5.56 | 7.337 | 6.935 | 12.35 | 10.7 | 9.89 | 8.575 |
| HPA replicas, mean | 9.686 | 14.12 | 9.578 | 13.13 | 9.61 | 13.29 | 9.585 | 13.49 | 9.639 | 13.76 | 9.653 | 13.88 |
| pods started | 4.854 | 10.17 | 5.463 | 9.415 | 5.098 | 9.512 | 5.475 | 10.07 | 4.634 | 10.29 | 5.146 | 10.61 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.3 | 180.1 | 179.1 | 180.1 | 179.4 | 181.6 | 181.3 | 181.5 | 182.1 | 181.1 | 181.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.3 | 180.1 | 179.1 | 180.1 | 179.4 | 181.6 | 181.3 | 181.5 | 182.1 | 181.1 | 181.4 |
| CPU used with Omni's own (cores), mean | 2.202 | 2.2 | 1.949 | 1.941 | 1.95 | 1.958 | 2.096 | 2.097 | 2.158 | 2.161 | 2.104 | 2.093 |
| host CPU busy, the real machine under kind (%) | 65.19 | 65.56 | 57.86 | 57.89 | 57.96 | 58.23 | 62.08 | 62.46 | 63.76 | 64.35 | 62.38 | 62.59 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 4 (response time (ms), 99th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1676 | 1569 | -6.4% | -313.3 to +99.94 | lower (inside the noise) |
| response time (ms), 99th percentile | 4629 | 5222 | +12.8% | +162.8 to +1024 | higher |
| time over the response line (% of samples) | 29.58 | 21.16 | -28.5% | -10.22 to -6.625 | lower |
| failed requests (%) | 13.12 | 11.64 | -11.3% | -2.042 to -0.9213 | lower |
| HPA replicas, mean | 9.686 | 14.12 | +45.8% | +3.906 to +4.961 | higher |
| pods started | 4.854 | 10.17 | +109.5% | +4.523 to +6.111 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.853e-16 to +1.521e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.3 | -0.0% | -0.4761 to +0.3856 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.3 | -0.0% | -0.4761 to +0.3856 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.202 | 2.2 | -0.1% | -0.009175 to +0.005185 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.19 | 65.56 | +0.6% | +0.1812 to +0.5571 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.621e+05 to +8.624e+05 | higher |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | lower |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.146e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: lower on 6 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1749 | 1669 | -4.6% | -375 to +214.8 | lower (inside the noise) |
| response time (ms), 99th percentile | 5004 | 4980 | -0.5% | -286.9 to +239.5 | lower (inside the noise) |
| time over the response line (% of samples) | 18.95 | 13.52 | -28.7% | -6.775 to -4.09 | lower |
| failed requests (%) | 6.571 | 5.733 | -12.8% | -1.246 to -0.431 | lower |
| HPA replicas, mean | 9.578 | 13.13 | +37.1% | +2.824 to +4.279 | higher |
| pods started | 5.463 | 9.415 | +72.3% | +3.119 to +4.784 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.003e-16 to +6.709e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 179.1 | -0.6% | -1.474 to -0.5951 | lower |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 179.1 | -0.6% | -1.474 to -0.5951 | lower |
| CPU used with Omni's own (cores), mean | 1.949 | 1.941 | -0.4% | -0.01829 to +0.003854 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.86 | 57.89 | +0.1% | -0.2753 to +0.3339 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | higher |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | lower |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.243e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: lower on 5 (time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1547 | 1462 | -5.5% | -259.5 to +89.35 | lower (inside the noise) |
| response time (ms), 99th percentile | 5051 | 4786 | -5.3% | -593.1 to +62.3 | lower (inside the noise) |
| time over the response line (% of samples) | 17.82 | 13.16 | -26.1% | -5.697 to -3.618 | lower |
| failed requests (%) | 6.047 | 5.56 | -8.0% | -0.7665 to -0.2064 | lower |
| HPA replicas, mean | 9.61 | 13.29 | +38.3% | +2.996 to +4.37 | higher |
| pods started | 5.098 | 9.512 | +86.6% | +3.514 to +5.315 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.341e-16 to +2.752e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.1 | 179.4 | -0.4% | -1.096 to -0.2973 | lower |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.1 | 179.4 | -0.4% | -1.096 to -0.2973 | lower |
| CPU used with Omni's own (cores), mean | 1.95 | 1.958 | +0.4% | -0.001991 to +0.01684 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.96 | 58.23 | +0.5% | +0.03662 to +0.4879 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | lower |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1584 | 1513 | -4.5% | -233.1 to +91.68 | lower (inside the noise) |
| response time (ms), 99th percentile | 4901 | 4575 | -6.7% | -673.4 to +21.33 | lower (inside the noise) |
| time over the response line (% of samples) | 24.1 | 17.53 | -27.3% | -8.182 to -4.965 | lower |
| failed requests (%) | 7.337 | 6.935 | -5.5% | -0.7484 to -0.05497 | lower |
| HPA replicas, mean | 9.585 | 13.49 | +40.8% | +3.298 to +4.517 | higher |
| pods started | 5.475 | 10.07 | +84.0% | +3.842 to +5.358 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.727e-16 to +6.555e-18 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 181.3 | -0.2% | -0.6799 to +0.1138 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 181.3 | -0.2% | -0.6799 to +0.1138 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.096 | 2.097 | +0.1% | -0.006369 to +0.008723 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.08 | 62.46 | +0.6% | +0.1658 to +0.5991 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | higher |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | lower |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: lower on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), higher on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1969 | 1937 | -1.6% | -213.6 to +150.3 | lower (inside the noise) |
| response time (ms), 99th percentile | 5066 | 5110 | +0.9% | -429.5 to +516.2 | higher (inside the noise) |
| time over the response line (% of samples) | 28.89 | 22.08 | -23.6% | -8.635 to -4.981 | lower |
| failed requests (%) | 12.35 | 10.7 | -13.4% | -2.815 to -0.4979 | lower |
| HPA replicas, mean | 9.639 | 13.76 | +42.7% | +3.485 to +4.753 | higher |
| pods started | 4.634 | 10.29 | +122.1% | +4.989 to +6.328 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.769e-16 to +2.169e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 182.1 | +0.3% | +0.3027 to +0.835 | higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 182.1 | +0.3% | +0.3027 to +0.835 | higher |
| CPU used with Omni's own (cores), mean | 2.158 | 2.161 | +0.1% | -0.006534 to +0.01282 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.76 | 64.35 | +0.9% | +0.3542 to +0.8312 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | lower |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: lower on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1520 | 1253 | -17.6% | -499.6 to -34.66 | lower |
| response time (ms), 99th percentile | 4755 | 4916 | +3.4% | -291.1 to +612.2 | higher (inside the noise) |
| time over the response line (% of samples) | 24.05 | 16.67 | -30.7% | -9.154 to -5.603 | lower |
| failed requests (%) | 9.89 | 8.575 | -13.3% | -1.882 to -0.7475 | lower |
| HPA replicas, mean | 9.653 | 13.88 | +43.8% | +3.665 to +4.795 | higher |
| pods started | 5.146 | 10.61 | +106.2% | +4.821 to +6.106 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.002e-16 to -7.966e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 181.4 | +0.1% | -0.09518 to +0.5764 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 181.4 | +0.1% | -0.09518 to +0.5764 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.104 | 2.093 | -0.5% | -0.02424 to +0.002123 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.38 | 62.59 | +0.3% | -0.1988 to +0.6193 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | lower |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
