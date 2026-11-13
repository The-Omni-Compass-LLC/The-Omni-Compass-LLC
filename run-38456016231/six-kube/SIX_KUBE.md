# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says which way the number went, lower or higher; whether that serves the system is the reader's to judge (response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill are amounts waited or spent; the organism's work and work per energy are amounts done). A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1484 | 1980 | 1936 | 2311 | 1233 | 1534 | 1290 | 1262 | 1978 | 1764 | 1637 | 1251 |
| response time (ms), 99th percentile | 4568 | 4912 | 6191 | 5456 | 4404 | 4535 | 3760 | 4403 | 5151 | 5852 | 4001 | 3784 |
| time over the response line (% of samples) | 30.16 | 22.57 | 23.95 | 18.91 | 17.93 | 13.56 | 19.42 | 13.74 | 30.8 | 23.12 | 25.57 | 18.32 |
| failed requests (%) | 14.06 | 12.98 | 8.147 | 7.701 | 6.661 | 5.961 | 5.988 | 5.311 | 11.68 | 10.84 | 11.66 | 10.74 |
| HPA replicas, mean | 9.65 | 13.3 | 9.69 | 14.56 | 9.57 | 13.03 | 9.548 | 12.95 | 9.683 | 14.52 | 9.615 | 12.75 |
| pods started | 5 | 9.4 | 4.5 | 9.3 | 5.7 | 9 | 5.8 | 9.8 | 4.7 | 10.7 | 5.1 | 9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 181.3 | 182.3 | 181.3 | 180 | 179.1 | 179.7 | 179.7 | 182.7 | 183.4 | 180.5 | 180.4 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 181.3 | 182.3 | 181.3 | 180 | 179.1 | 179.7 | 179.7 | 182.7 | 183.4 | 180.5 | 180.4 |
| CPU used with Omni's own (cores), mean | 2.115 | 2.126 | 2.14 | 2.148 | 1.931 | 1.942 | 1.964 | 1.959 | 2.27 | 2.273 | 2.029 | 2.025 |
| host CPU busy, the real machine under kind (%) | 62.69 | 63.34 | 63.63 | 63.96 | 57.3 | 57.87 | 58.6 | 58.82 | 67.23 | 67.64 | 60.48 | 60.77 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 4 (response time (ms), 95th percentile; HPA replicas, mean; pods started; organism energy (J)), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1484 | 1980 | +33.5% | +110.8 to +881.9 | higher |
| response time (ms), 99th percentile | 4568 | 4912 | +7.5% | -350.5 to +1039 | higher (inside the noise) |
| time over the response line (% of samples) | 30.16 | 22.57 | -25.2% | -12.17 to -3.026 | lower |
| failed requests (%) | 14.06 | 12.98 | -7.7% | -1.782 to -0.3814 | lower |
| HPA replicas, mean | 9.65 | 13.3 | +37.8% | +1.814 to +5.486 | higher |
| pods started | 5 | 9.4 | +88.0% | +2.847 to +5.953 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.449e-15 to +5.604e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 181.3 | +0.1% | -0.8103 to +1.023 | higher (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 181.3 | +0.1% | -0.8103 to +1.023 | higher (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.115 | 2.126 | +0.5% | -0.01312 to +0.03345 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.69 | 63.34 | +1.0% | -0.008804 to +1.318 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.63e+05 | higher |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | lower |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.154e-05 to -8.142e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: lower on 5 (time over the response line (% of samples); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1936 | 2311 | +19.4% | -327.3 to +1079 | higher (inside the noise) |
| response time (ms), 99th percentile | 6191 | 5456 | -11.9% | -2087 to +616.4 | lower (inside the noise) |
| time over the response line (% of samples) | 23.95 | 18.91 | -21.0% | -7.254 to -2.823 | lower |
| failed requests (%) | 8.147 | 7.701 | -5.5% | -1.329 to +0.4379 | lower (inside the noise) |
| HPA replicas, mean | 9.69 | 14.56 | +50.3% | +4.493 to +5.255 | higher |
| pods started | 4.5 | 9.3 | +106.7% | +3.692 to +5.908 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.781e-16 to +1.822e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.3 | -0.5% | -1.81 to -0.1792 | lower |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.3 | -0.5% | -1.81 to -0.1792 | lower |
| CPU used with Omni's own (cores), mean | 2.14 | 2.148 | +0.4% | -0.00342 to +0.01872 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.63 | 63.96 | +0.5% | -0.1199 to +0.7956 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | higher |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | lower |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.246e-05 to -8.245e-05 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1233 | 1534 | +24.4% | -155.9 to +757.8 | higher (inside the noise) |
| response time (ms), 99th percentile | 4404 | 4535 | +3.0% | -536 to +799.1 | higher (inside the noise) |
| time over the response line (% of samples) | 17.93 | 13.56 | -24.4% | -6.963 to -1.782 | lower |
| failed requests (%) | 6.661 | 5.961 | -10.5% | -1.418 to +0.01848 | lower (inside the noise) |
| HPA replicas, mean | 9.57 | 13.03 | +36.2% | +1.721 to +5.206 | higher |
| pods started | 5.7 | 9 | +57.9% | +1.514 to +5.086 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.279e-15 to +2.128e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180 | 179.1 | -0.5% | -2.105 to +0.2945 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180 | 179.1 | -0.5% | -2.105 to +0.2945 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.931 | 1.942 | +0.6% | -0.009855 to +0.0313 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 57.3 | 57.87 | +1.0% | +0.0237 to +1.112 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | lower |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: lower on 4 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps); organism work per energy), higher on 3 (HPA replicas, mean; pods started; organism energy (J)), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1290 | 1262 | -2.2% | -221.2 to +165.1 | lower (inside the noise) |
| response time (ms), 99th percentile | 3760 | 4403 | +17.1% | -128 to +1414 | higher (inside the noise) |
| time over the response line (% of samples) | 19.42 | 13.74 | -29.2% | -9.702 to -1.655 | lower |
| failed requests (%) | 5.988 | 5.311 | -11.3% | -1.339 to -0.01651 | lower |
| HPA replicas, mean | 9.548 | 12.95 | +35.7% | +1.764 to +5.045 | higher |
| pods started | 5.8 | 9.8 | +69.0% | +2.216 to +5.784 | higher |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.547e-15 to +1.259e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 179.7 | 179.7 | -0.0% | -1.109 to +1.039 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 179.7 | 179.7 | -0.0% | -1.109 to +1.039 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 1.964 | 1.959 | -0.3% | -0.04703 to +0.03617 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 58.6 | 58.82 | +0.4% | -1.084 to +1.524 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | higher |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | lower |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | lower |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: lower on 2 (time over the response line (% of samples); organism time over the line (% of steps)), higher on 4 (HPA replicas, mean; pods started; energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this)), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1978 | 1764 | -10.8% | -531.7 to +104.2 | lower (inside the noise) |
| response time (ms), 99th percentile | 5151 | 5852 | +13.6% | -507.1 to +1908 | higher (inside the noise) |
| time over the response line (% of samples) | 30.8 | 23.12 | -24.9% | -10.88 to -4.469 | lower |
| failed requests (%) | 11.68 | 10.84 | -7.2% | -1.764 to +0.07223 | lower (inside the noise) |
| HPA replicas, mean | 9.683 | 14.52 | +50.0% | +4.46 to +5.213 | higher |
| pods started | 4.7 | 10.7 | +127.7% | +4.694 to +7.306 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.246e-16 to +1.102e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.7 | 183.4 | +0.3% | +0.002466 to +1.225 | higher |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.7 | 183.4 | +0.3% | +0.002466 to +1.225 | higher |
| CPU used with Omni's own (cores), mean | 2.27 | 2.273 | +0.2% | -0.01231 to +0.01971 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.23 | 67.64 | +0.6% | -0.08051 to +0.9017 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | lower |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: lower on 3 (response time (ms), 95th percentile; time over the response line (% of samples); organism time over the line (% of steps)), higher on 2 (HPA replicas, mean; pods started), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1637 | 1251 | -23.6% | -699.5 to -71.79 | lower |
| response time (ms), 99th percentile | 4001 | 3784 | -5.4% | -737.6 to +304 | lower (inside the noise) |
| time over the response line (% of samples) | 25.57 | 18.32 | -28.4% | -12.12 to -2.392 | lower |
| failed requests (%) | 11.66 | 10.74 | -7.9% | -2.216 to +0.3782 | lower (inside the noise) |
| HPA replicas, mean | 9.615 | 12.75 | +32.6% | +1.223 to +5.045 | higher |
| pods started | 5.1 | 9 | +76.5% | +1.627 to +6.173 | higher |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.785e-16 to +8.338e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 180.5 | 180.4 | -0.0% | -0.6643 to +0.5352 | lower (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 180.5 | 180.4 | -0.0% | -0.6643 to +0.5352 | lower (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.029 | 2.025 | -0.2% | -0.02405 to +0.01687 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 60.48 | 60.77 | +0.5% | -0.2543 to +0.8292 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | lower |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
