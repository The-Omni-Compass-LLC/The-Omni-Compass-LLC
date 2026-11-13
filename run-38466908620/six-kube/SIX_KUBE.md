# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1656 | 1398 | 1779 | 1513 | 1741 | 1524 | 1702 | 1516 | 2165 | 2065 | 1670 | 1449 |
| response time (ms), 99th percentile | 5020 | 4818 | 5341 | 5297 | 5783 | 5306 | 4418 | 4403 | 5210 | 5422 | 4514 | 4445 |
| time over the response line (% of samples) | 27.11 | 19.63 | 19.57 | 14.06 | 19.75 | 14.74 | 25.77 | 18.68 | 32.08 | 23.74 | 26.8 | 18.85 |
| failed requests (%) | 12.27 | 10.89 | 6.092 | 5.957 | 6.543 | 6.243 | 8.663 | 7.963 | 14.18 | 11.19 | 12.09 | 10.57 |
| HPA replicas, mean | 9.688 | 13.87 | 9.612 | 13.53 | 9.644 | 13.89 | 9.587 | 13.23 | 9.662 | 14.11 | 9.667 | 13.41 |
| pods started | 4.707 | 10 | 5.146 | 9.61 | 4.927 | 9.951 | 5.171 | 9.195 | 4.732 | 10.29 | 4.683 | 9.78 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 182 | 180.6 | 179.6 | 180.9 | 180.2 | 181.1 | 180.7 | 182 | 182.6 | 181.1 | 181 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 182 | 180.6 | 179.6 | 180.9 | 180.2 | 181.1 | 180.7 | 182 | 182.6 | 181.1 | 181 |
| CPU used with Omni's own (cores), mean | 2.158 | 2.157 | 1.994 | 2.002 | 2.031 | 2.044 | 2.072 | 2.072 | 2.217 | 2.214 | 2.087 | 2.092 |
| host CPU busy, the real machine under kind (%) | 63.93 | 64.41 | 59.05 | 59.46 | 60.16 | 60.48 | 61.27 | 61.72 | 65.53 | 65.86 | 62.03 | 62.46 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 5 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism energy (J)), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1656 | 1398 | -15.6% | -544.8 to +28.51 | lower (inside the noise) |
| response time (ms), 99th percentile | 5020 | 4818 | -4.0% | -760.5 to +357.6 | lower (inside the noise) |
| time over the response line (% of samples) | 27.11 | 19.63 | -27.6% | -9.002 to -5.948 | lower |
| failed requests (%) | 12.27 | 10.89 | -11.3% | -1.934 to -0.8283 | lower |
| HPA replicas, mean | 9.688 | 13.87 | +43.2% | +3.588 to +4.781 | higher |
| pods started | 4.707 | 10 | +112.4% | +4.494 to +6.092 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.341e-16 to +1.875e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.6 | 182 | +0.2% | +0.09535 to +0.7811 | higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.6 | 182 | +0.2% | +0.09535 to +0.7811 | higher |
| CPU used with Omni's own (cores), mean | 2.158 | 2.157 | -0.0% | -0.00887 to +0.007806 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.93 | 64.41 | +0.8% | +0.2881 to +0.6808 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.622e+05 to +8.625e+05 | higher |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | lower |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.149e-05 to -8.147e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: lower on 6 (response time (ms), 95th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1779 | 1513 | -14.9% | -497.3 to -34.33 | lower |
| response time (ms), 99th percentile | 5341 | 5297 | -0.8% | -404.5 to +315.8 | lower (inside the noise) |
| time over the response line (% of samples) | 19.57 | 14.06 | -28.2% | -6.784 to -4.239 | lower |
| failed requests (%) | 6.092 | 5.957 | -2.2% | -0.4465 to +0.1763 | lower (inside the noise) |
| HPA replicas, mean | 9.612 | 13.53 | +40.8% | +3.27 to +4.567 | higher |
| pods started | 5.146 | 9.61 | +86.7% | +3.716 to +5.21 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.17e-16 to +5.378e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.6 | 179.6 | -0.5% | -1.305 to -0.5113 | lower |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.6 | 179.6 | -0.5% | -1.305 to -0.5113 | lower |
| CPU used with Omni's own (cores), mean | 1.994 | 2.002 | +0.4% | -0.0007857 to +0.01696 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 59.05 | 59.46 | +0.7% | +0.1987 to +0.615 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | higher |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | lower |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: lower on 6 (response time (ms), 95th percentile; response time (ms), 99th percentile; time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1741 | 1524 | -12.5% | -429.2 to -4.929 | lower |
| response time (ms), 99th percentile | 5783 | 5306 | -8.2% | -826.8 to -127.4 | lower |
| time over the response line (% of samples) | 19.75 | 14.74 | -25.4% | -5.943 to -4.077 | lower |
| failed requests (%) | 6.543 | 6.243 | -4.6% | -0.6275 to +0.02713 | lower (inside the noise) |
| HPA replicas, mean | 9.644 | 13.89 | +44.0% | +3.676 to +4.809 | higher |
| pods started | 4.927 | 9.951 | +102.0% | +4.27 to +5.779 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.752e-16 to +1.419e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.9 | 180.2 | -0.4% | -1.098 to -0.2915 | lower |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.9 | 180.2 | -0.4% | -1.098 to -0.2915 | lower |
| CPU used with Omni's own (cores), mean | 2.031 | 2.044 | +0.7% | +0.007007 to +0.02012 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.16 | 60.48 | +0.5% | +0.1257 to +0.5097 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | lower |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1702 | 1516 | -10.9% | -382.6 to +12.36 | lower (inside the noise) |
| response time (ms), 99th percentile | 4418 | 4403 | -0.3% | -440.7 to +412.1 | lower (inside the noise) |
| time over the response line (% of samples) | 25.77 | 18.68 | -27.5% | -8.853 to -5.324 | lower |
| failed requests (%) | 8.663 | 7.963 | -8.1% | -1.059 to -0.3412 | lower |
| HPA replicas, mean | 9.587 | 13.23 | +38.0% | +2.943 to +4.342 | higher |
| pods started | 5.171 | 9.195 | +77.8% | +3.19 to +4.858 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.896e-16 to +1.863e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 180.7 | -0.2% | -0.7526 to +0.05457 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 180.7 | -0.2% | -0.7526 to +0.05457 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.072 | 2.072 | -0.0% | -0.007223 to +0.006824 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.27 | 61.72 | +0.7% | +0.2471 to +0.6488 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | higher |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | lower |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: lower on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), higher on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2165 | 2065 | -4.6% | -396.2 to +195.2 | lower (inside the noise) |
| response time (ms), 99th percentile | 5210 | 5422 | +4.1% | -237.2 to +660 | higher (inside the noise) |
| time over the response line (% of samples) | 32.08 | 23.74 | -26.0% | -10.39 to -6.287 | lower |
| failed requests (%) | 14.18 | 11.19 | -21.1% | -4.494 to -1.491 | lower |
| HPA replicas, mean | 9.662 | 14.11 | +46.0% | +3.896 to +4.999 | higher |
| pods started | 4.732 | 10.29 | +117.5% | +5.013 to +6.109 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.702e-16 to +2.969e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 182.6 | +0.3% | +0.2303 to +0.9089 | higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 182.6 | +0.3% | +0.2303 to +0.9089 | higher |
| CPU used with Omni's own (cores), mean | 2.217 | 2.214 | -0.2% | -0.01323 to +0.005754 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 65.53 | 65.86 | +0.5% | +0.07746 to +0.5868 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | lower |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: lower on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1670 | 1449 | -13.2% | -351.2 to -91.33 | lower |
| response time (ms), 99th percentile | 4514 | 4445 | -1.5% | -473.3 to +334.6 | lower (inside the noise) |
| time over the response line (% of samples) | 26.8 | 18.85 | -29.7% | -9.85 to -6.047 | lower |
| failed requests (%) | 12.09 | 10.57 | -12.6% | -2.169 to -0.8721 | lower |
| HPA replicas, mean | 9.667 | 13.41 | +38.7% | +3.014 to +4.47 | higher |
| pods started | 4.683 | 9.78 | +108.9% | +4.333 to +5.862 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.781e-16 to +2.826e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.1 | 181 | -0.0% | -0.4211 to +0.3448 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.1 | 181 | -0.0% | -0.4211 to +0.3448 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.087 | 2.092 | +0.2% | -0.003812 to +0.01334 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.03 | 62.46 | +0.7% | +0.1964 to +0.6652 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | lower |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
