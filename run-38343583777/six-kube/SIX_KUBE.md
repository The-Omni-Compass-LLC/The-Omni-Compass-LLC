# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1484 | 825.4 | 1972 | 1265 | 1729 | 1091 | 1964 | 1189 | 1520 | 1049 | 1748 | 925.3 |
| response time (ms), 99th percentile | 3807 | 3036 | 4762 | 4244 | 4338 | 3564 | 4769 | 3926 | 3491 | 3193 | 4168 | 3218 |
| time over the response line (% of samples) | 25.21 | 14.33 | 22.92 | 11.56 | 20.14 | 9.941 | 32.59 | 16.34 | 24.5 | 13.12 | 27.88 | 15.7 |
| failed requests (%) | 8.829 | 7.85 | 4.976 | 4.425 | 4.609 | 3.67 | 8.497 | 7.047 | 6.96 | 6.108 | 8.982 | 8.223 |
| HPA replicas, mean | 9.677 | 9.659 | 9.695 | 9.701 | 9.633 | 9.648 | 9.681 | 9.706 | 9.604 | 9.532 | 9.724 | 9.7 |
| pods started | 4.317 | 4.634 | 4.098 | 3.756 | 4.439 | 4.244 | 3.927 | 3.805 | 4.707 | 4.951 | 3.829 | 4.317 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.1 | 183.7 | 183.4 | 182.1 | 181.4 | 186.6 | 186.3 | 183.3 | 183 | 185.8 | 185.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.1 | 183.7 | 183.4 | 182.1 | 181.4 | 186.6 | 186.3 | 183.3 | 183 | 185.8 | 185.6 |
| CPU used with Omni's own (cores), mean | 2.374 | 2.35 | 2.362 | 2.328 | 2.205 | 2.157 | 2.577 | 2.543 | 2.295 | 2.262 | 2.514 | 2.495 |
| host CPU busy, the real machine under kind (%) | 69.54 | 69.07 | 69 | 68.28 | 64.61 | 63.47 | 75.57 | 74.97 | 67.26 | 66.49 | 73.33 | 73.23 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0.002439 | 0 | 0.002439 | 0 | 0 | 0 | 0 | 0 | 0.002439 | 0.004878 | 0.01951 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1484 | 825.4 | -44.4% | -834.1 to -482.2 | better |
| response time (ms), 99th percentile | 3807 | 3036 | -20.2% | -1215 to -326.3 | better |
| time over the response line (% of samples) | 25.21 | 14.33 | -43.2% | -13.38 to -8.388 | better |
| failed requests (%) | 8.829 | 7.85 | -11.1% | -1.537 to -0.4221 | better |
| HPA replicas, mean | 9.677 | 9.659 | -0.2% | -0.0502 to +0.01511 | better (inside the noise) |
| pods started | 4.317 | 4.634 | +7.3% | -0.1443 to +0.7785 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.833e-16 to +2.1e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.5 | 184.1 | -0.2% | -0.7137 to -0.06291 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.5 | 184.1 | -0.2% | -0.7137 to -0.06291 | better |
| CPU used with Omni's own (cores), mean | 2.374 | 2.35 | -1.0% | -0.04118 to -0.007795 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.54 | 69.07 | -0.7% | -0.9646 to +0.008795 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.624e+05 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.142e-05 | WORSE |
| organism behind its window (s) | 0 | 0.002439 | +0.00244 | -0.002341 to +0.00722 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1972 | 1265 | -35.9% | -896.5 to -518.5 | better |
| response time (ms), 99th percentile | 4762 | 4244 | -10.9% | -833.7 to -202.6 | better |
| time over the response line (% of samples) | 22.92 | 11.56 | -49.6% | -13.34 to -9.369 | better |
| failed requests (%) | 4.976 | 4.425 | -11.1% | -0.9063 to -0.1966 | better |
| HPA replicas, mean | 9.695 | 9.701 | +0.1% | -0.02264 to +0.03537 | WORSE (inside the noise) |
| pods started | 4.098 | 3.756 | -8.3% | -0.7383 to +0.05535 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.361e-16 to +1.329e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.7 | 183.4 | -0.2% | -0.5247 to -0.05227 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.7 | 183.4 | -0.2% | -0.5247 to -0.05227 | better |
| CPU used with Omni's own (cores), mean | 2.362 | 2.328 | -1.5% | -0.04697 to -0.02176 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69 | 68.28 | -1.0% | -1.042 to -0.401 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.244e-05 to -8.243e-05 | WORSE |
| organism behind its window (s) | 0 | 0.002439 | +0.00244 | -0.002341 to +0.00722 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 7, worse on 0, inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1729 | 1091 | -36.9% | -827.9 to -447.3 | better |
| response time (ms), 99th percentile | 4338 | 3564 | -17.9% | -1052 to -496.9 | better |
| time over the response line (% of samples) | 20.14 | 9.941 | -50.7% | -12.45 to -7.96 | better |
| failed requests (%) | 4.609 | 3.67 | -20.4% | -1.339 to -0.5388 | better |
| HPA replicas, mean | 9.633 | 9.648 | +0.2% | -0.01696 to +0.04715 | WORSE (inside the noise) |
| pods started | 4.439 | 4.244 | -4.4% | -0.6802 to +0.2899 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -2.222e-16 to +3.955e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.1 | 181.4 | -0.3% | -0.8358 to -0.412 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.1 | 181.4 | -0.3% | -0.8358 to -0.412 | better |
| CPU used with Omni's own (cores), mean | 2.205 | 2.157 | -2.2% | -0.05757 to -0.03769 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 64.61 | 63.47 | -1.8% | -1.402 to -0.8818 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1964 | 1189 | -39.5% | -950.4 to -599.5 | better |
| response time (ms), 99th percentile | 4769 | 3926 | -17.7% | -1179 to -507.4 | better |
| time over the response line (% of samples) | 32.59 | 16.34 | -49.9% | -19.33 to -13.16 | better |
| failed requests (%) | 8.497 | 7.047 | -17.1% | -1.87 to -1.031 | better |
| HPA replicas, mean | 9.681 | 9.706 | +0.3% | -0.009053 to +0.05873 | WORSE (inside the noise) |
| pods started | 3.927 | 3.805 | -3.1% | -0.6117 to +0.3678 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.601e-16 to +8.353e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.6 | 186.3 | -0.2% | -0.5503 to -0.1136 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.6 | 186.3 | -0.2% | -0.5503 to -0.1136 | better |
| CPU used with Omni's own (cores), mean | 2.577 | 2.543 | -1.3% | -0.04585 to -0.02179 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.57 | 74.97 | -0.8% | -0.8915 to -0.311 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 5, worse on 0, inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1520 | 1049 | -31.0% | -585.8 to -356.2 | better |
| response time (ms), 99th percentile | 3491 | 3193 | -8.5% | -624.1 to +28.75 | better (inside the noise) |
| time over the response line (% of samples) | 24.5 | 13.12 | -46.4% | -14.29 to -8.453 | better |
| failed requests (%) | 6.96 | 6.108 | -12.2% | -1.336 to -0.3693 | better |
| HPA replicas, mean | 9.604 | 9.532 | -0.8% | -0.1309 to -0.01401 | better |
| pods started | 4.707 | 4.951 | +5.2% | -0.2292 to +0.717 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.728e-16 to +1.695e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.3 | 183 | -0.2% | -0.6715 to +0.08747 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.3 | 183 | -0.2% | -0.6715 to +0.08747 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.295 | 2.262 | -1.5% | -0.05225 to -0.01502 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 67.26 | 66.49 | -1.1% | -1.201 to -0.3426 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0.002439 | +0.00244 | -0.002341 to +0.00722 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 5, worse on 1 (pods started), inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1748 | 925.3 | -47.1% | -1040 to -605.6 | better |
| response time (ms), 99th percentile | 4168 | 3218 | -22.8% | -1342 to -556.4 | better |
| time over the response line (% of samples) | 27.88 | 15.7 | -43.7% | -14.38 to -9.984 | better |
| failed requests (%) | 8.982 | 8.223 | -8.5% | -1.137 to -0.3815 | better |
| HPA replicas, mean | 9.724 | 9.7 | -0.2% | -0.04944 to +0.001476 | better (inside the noise) |
| pods started | 3.829 | 4.317 | +12.7% | +0.0652 to +0.9104 | WORSE |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.068e-17 to +5.859e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.8 | 185.6 | -0.1% | -0.5152 to +0.1881 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.8 | 185.6 | -0.1% | -0.5152 to +0.1881 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.514 | 2.495 | -0.7% | -0.03221 to -0.004639 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 73.33 | 73.23 | -0.1% | -0.4043 to +0.1947 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.004878 | 0.01951 | +300.0% | -0.002898 to +0.03217 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
