# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1688 | 959.2 | 2445 | 1588 | 2324 | 1526 | 1989 | 1298 | 1793 | 1177 | 1973 | 1147 |
| response time (ms), 99th percentile | 4153 | 3335 | 5901 | 5392 | 5386 | 4904 | 4915 | 4314 | 4018 | 3687 | 5257 | 3991 |
| time over the response line (% of samples) | 27.99 | 15.22 | 29 | 14.78 | 25.75 | 13.41 | 31.8 | 16.42 | 27.73 | 15.24 | 33.44 | 19.6 |
| failed requests (%) | 9.255 | 8.095 | 6.68 | 6.021 | 6.221 | 5.233 | 8.011 | 7.049 | 8.098 | 6.859 | 11.92 | 10.62 |
| HPA replicas, mean | 9.722 | 9.699 | 9.769 | 9.787 | 9.719 | 9.737 | 9.669 | 9.699 | 9.67 | 9.621 | 9.752 | 9.758 |
| pods started | 3.829 | 4.024 | 3.293 | 2.902 | 3.725 | 3.375 | 4.122 | 3.805 | 4.268 | 4.39 | 3.634 | 3.415 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 185.4 | 186.3 | 186.1 | 184.6 | 184.4 | 186.7 | 186.5 | 185.2 | 184.9 | 188 | 187.7 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 185.4 | 186.3 | 186.1 | 184.6 | 184.4 | 186.7 | 186.5 | 185.2 | 184.9 | 188 | 187.7 |
| CPU used with Omni's own (cores), mean | 2.502 | 2.472 | 2.619 | 2.579 | 2.455 | 2.421 | 2.602 | 2.58 | 2.458 | 2.435 | 2.696 | 2.682 |
| host CPU busy, the real machine under kind (%) | 72.93 | 72.39 | 75.96 | 75.2 | 71.7 | 70.8 | 75.74 | 75.3 | 71.77 | 71.28 | 78.7 | 78.39 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.002439 | 0.02195 | 0.02439 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1688 | 959.2 | -43.2% | -896 to -561.8 | better |
| response time (ms), 99th percentile | 4153 | 3335 | -19.7% | -1172 to -464.4 | better |
| time over the response line (% of samples) | 27.99 | 15.22 | -45.6% | -15.22 to -10.31 | better |
| failed requests (%) | 9.255 | 8.095 | -12.5% | -1.666 to -0.6544 | better |
| HPA replicas, mean | 9.722 | 9.699 | -0.2% | -0.05286 to +0.007562 | better (inside the noise) |
| pods started | 3.829 | 4.024 | +5.1% | -0.2549 to +0.6451 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.589e-16 to +2.723e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.7 | 185.4 | -0.1% | -0.6017 to +0.04548 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.7 | 185.4 | -0.1% | -0.6017 to +0.04548 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.502 | 2.472 | -1.2% | -0.04533 to -0.01537 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.93 | 72.39 | -0.7% | -0.8684 to -0.2184 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.617e+05 to +8.623e+05 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.147e-05 to -8.141e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 7, worse on 2 (organism energy (J); organism work per energy), inside the noise on 2

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2445 | 1588 | -35.1% | -1129 to -584.9 | better |
| response time (ms), 99th percentile | 5901 | 5392 | -8.6% | -874.4 to -143.7 | better |
| time over the response line (% of samples) | 29 | 14.78 | -49.0% | -15.86 to -12.58 | better |
| failed requests (%) | 6.68 | 6.021 | -9.9% | -0.9779 to -0.3403 | better |
| HPA replicas, mean | 9.769 | 9.787 | +0.2% | -0.01347 to +0.05099 | WORSE (inside the noise) |
| pods started | 3.293 | 2.902 | -11.9% | -0.9458 to +0.1653 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.373e-16 to +1.774e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.3 | 186.1 | -0.1% | -0.4211 to -0.07977 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.3 | 186.1 | -0.1% | -0.4211 to -0.07977 | better |
| CPU used with Omni's own (cores), mean | 2.619 | 2.579 | -1.5% | -0.05128 to -0.02767 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.96 | 75.2 | -1.0% | -1.022 to -0.4983 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.244e-05 to -8.243e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 7, worse on 0, inside the noise on 2

40 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2324 | 1526 | -34.3% | -1074 to -520.5 | better |
| response time (ms), 99th percentile | 5386 | 4904 | -8.9% | -803.6 to -160.1 | better |
| time over the response line (% of samples) | 25.75 | 13.41 | -47.9% | -14.38 to -10.31 | better |
| failed requests (%) | 6.221 | 5.233 | -15.9% | -1.393 to -0.5834 | better |
| HPA replicas, mean | 9.719 | 9.737 | +0.2% | -0.01158 to +0.04901 | WORSE (inside the noise) |
| pods started | 3.725 | 3.375 | -9.4% | -0.9095 to +0.2095 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.3e-16 to +2.08e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.4 | -0.1% | -0.5133 to -0.02047 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.4 | -0.1% | -0.5133 to -0.02047 | better |
| CPU used with Omni's own (cores), mean | 2.455 | 2.421 | -1.4% | -0.04691 to -0.02147 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 71.7 | 70.8 | -1.3% | -1.246 to -0.5583 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 3 (HPA replicas, mean; organism energy (J); organism work per energy), inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1989 | 1298 | -34.8% | -884.1 to -499.3 | better |
| response time (ms), 99th percentile | 4915 | 4314 | -12.2% | -969.3 to -232.4 | better |
| time over the response line (% of samples) | 31.8 | 16.42 | -48.3% | -18.09 to -12.66 | better |
| failed requests (%) | 8.011 | 7.049 | -12.0% | -1.357 to -0.5668 | better |
| HPA replicas, mean | 9.669 | 9.699 | +0.3% | +0.002591 to +0.05738 | WORSE |
| pods started | 4.122 | 3.805 | -7.7% | -0.763 to +0.1288 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.87e-16 to +5.375e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.7 | 186.5 | -0.1% | -0.3693 to +0.05996 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.7 | 186.5 | -0.1% | -0.3693 to +0.05996 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.602 | 2.58 | -0.8% | -0.03775 to -0.006223 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.74 | 75.3 | -0.6% | -0.8744 to -0.007181 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 6, worse on 0, inside the noise on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1793 | 1177 | -34.3% | -782.8 to -448.8 | better |
| response time (ms), 99th percentile | 4018 | 3687 | -8.2% | -675.9 to +14.44 | better (inside the noise) |
| time over the response line (% of samples) | 27.73 | 15.24 | -45.0% | -15 to -9.972 | better |
| failed requests (%) | 8.098 | 6.859 | -15.3% | -1.822 to -0.6563 | better |
| HPA replicas, mean | 9.67 | 9.621 | -0.5% | -0.1058 to +0.0081 | better (inside the noise) |
| pods started | 4.268 | 4.39 | +2.9% | -0.5024 to +0.7463 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -7.794e-16 to -4.391e-19 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.2 | 184.9 | -0.2% | -0.7046 to -0.04371 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.2 | 184.9 | -0.2% | -0.7046 to -0.04371 | better |
| CPU used with Omni's own (cores), mean | 2.458 | 2.435 | -0.9% | -0.03778 to -0.008531 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 71.77 | 71.28 | -0.7% | -0.8465 to -0.128 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0.002439 | +0.00244 | -0.002341 to +0.00722 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 5, worse on 0, inside the noise on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1973 | 1147 | -41.9% | -1035 to -617.1 | better |
| response time (ms), 99th percentile | 5257 | 3991 | -24.1% | -1733 to -799.4 | better |
| time over the response line (% of samples) | 33.44 | 19.6 | -41.4% | -16.08 to -11.6 | better |
| failed requests (%) | 11.92 | 10.62 | -10.9% | -1.76 to -0.8445 | better |
| HPA replicas, mean | 9.752 | 9.758 | +0.1% | -0.03192 to +0.04393 | WORSE (inside the noise) |
| pods started | 3.634 | 3.415 | -6.0% | -0.7475 to +0.3085 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.845e-16 to +3.845e-16 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 188 | 187.7 | -0.1% | -0.5677 to +0.04872 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188 | 187.7 | -0.1% | -0.5677 to +0.04872 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.696 | 2.682 | -0.5% | -0.02875 to +0.001005 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.7 | 78.39 | -0.4% | -0.65 to +0.04203 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.02195 | 0.02439 | +11.1% | -0.01864 to +0.02352 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
