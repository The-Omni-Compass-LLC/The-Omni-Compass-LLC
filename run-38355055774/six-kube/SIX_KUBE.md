# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1909 | 1167 | 1641 | 1067 | 1976 | 1173 | 1641 | 939.5 | 1762 | 1305 | 1365 | 649.4 |
| response time (ms), 99th percentile | 4542 | 4709 | 3488 | 2898 | 4676 | 4123 | 4051 | 3524 | 4026 | 3781 | 3043 | 1981 |
| time over the response line (% of samples) | 35.58 | 21.01 | 17.17 | 8.248 | 21.79 | 11.04 | 26.7 | 10.66 | 32.1 | 18.98 | 21.78 | 11.34 |
| failed requests (%) | 13.52 | 11.65 | 3.43 | 2.975 | 4.647 | 4.118 | 5.83 | 4.274 | 10.67 | 9.093 | 6.781 | 5.978 |
| HPA replicas, mean | 9.728 | 9.766 | 9.606 | 9.643 | 9.688 | 9.672 | 9.651 | 9.681 | 9.62 | 9.575 | 9.663 | 9.616 |
| pods started | 4 | 3.5 | 4.75 | 4.375 | 3.875 | 4.125 | 4.625 | 4.125 | 4.875 | 4.25 | 4.625 | 5.25 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 188.8 | 188.7 | 181.2 | 180.6 | 182.9 | 182.6 | 185.6 | 184.5 | 185.9 | 185.1 | 183.4 | 183.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.8 | 188.7 | 181.2 | 180.6 | 182.9 | 182.6 | 185.6 | 184.5 | 185.9 | 185.1 | 183.4 | 183.1 |
| CPU used with Omni's own (cores), mean | 2.734 | 2.716 | 2.13 | 2.08 | 2.282 | 2.247 | 2.499 | 2.399 | 2.484 | 2.45 | 2.257 | 2.217 |
| host CPU busy, the real machine under kind (%) | 79.11 | 78.76 | 62.67 | 61.12 | 66.96 | 66.07 | 72.98 | 70.8 | 72.46 | 71.76 | 66.61 | 65.84 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.025 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1909 | 1167 | -38.9% | -1218 to -266.1 | better |
| response time (ms), 99th percentile | 4542 | 4709 | +3.7% | -909.5 to +1242 | WORSE (inside the noise) |
| time over the response line (% of samples) | 35.58 | 21.01 | -40.9% | -21.33 to -7.79 | better |
| failed requests (%) | 13.52 | 11.65 | -13.8% | -3.564 to -0.1747 | better |
| HPA replicas, mean | 9.728 | 9.766 | +0.4% | -0.03068 to +0.1064 | WORSE (inside the noise) |
| pods started | 4 | 3.5 | -12.5% | -1.841 to +0.8408 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.118e-15 to +8.962e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.8 | 188.7 | -0.1% | -0.5465 to +0.163 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.8 | 188.7 | -0.1% | -0.5465 to +0.163 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.734 | 2.716 | -0.7% | -0.04371 to +0.00816 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 79.11 | 78.76 | -0.4% | -1.006 to +0.3155 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.62e+05 to +8.631e+05 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.155e-05 to -8.145e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1641 | 1067 | -35.0% | -1361 to +213.6 | better (inside the noise) |
| response time (ms), 99th percentile | 3488 | 2898 | -16.9% | -1407 to +228.7 | better (inside the noise) |
| time over the response line (% of samples) | 17.17 | 8.248 | -52.0% | -14.84 to -3.008 | better |
| failed requests (%) | 3.43 | 2.975 | -13.3% | -1.464 to +0.5521 | better (inside the noise) |
| HPA replicas, mean | 9.606 | 9.643 | +0.4% | -0.0197 to +0.09385 | WORSE (inside the noise) |
| pods started | 4.75 | 4.375 | -7.9% | -1.368 to +0.6181 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.362e-16 to +8.803e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.2 | 180.6 | -0.4% | -1.25 to -0.06368 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.2 | 180.6 | -0.4% | -1.25 to -0.06368 | better |
| CPU used with Omni's own (cores), mean | 2.13 | 2.08 | -2.3% | -0.09155 to -0.007392 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 62.67 | 61.12 | -2.5% | -2.707 to -0.4072 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.407e+06 to +1.408e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.244e-05 to -8.24e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 2, worse on 0, inside the noise on 7

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1976 | 1173 | -40.6% | -1666 to +60.31 | better (inside the noise) |
| response time (ms), 99th percentile | 4676 | 4123 | -11.8% | -1178 to +71.08 | better (inside the noise) |
| time over the response line (% of samples) | 21.79 | 11.04 | -49.4% | -16.84 to -4.673 | better |
| failed requests (%) | 4.647 | 4.118 | -11.4% | -1.134 to +0.07655 | better (inside the noise) |
| HPA replicas, mean | 9.688 | 9.672 | -0.2% | -0.07008 to +0.03814 | better (inside the noise) |
| pods started | 3.875 | 4.125 | +6.5% | -0.4912 to +0.9912 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.327e-15 to +8.831e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.9 | 182.6 | -0.2% | -1.019 to +0.4547 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.9 | 182.6 | -0.2% | -1.019 to +0.4547 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.282 | 2.247 | -1.6% | -0.08321 to +0.01218 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 66.96 | 66.07 | -1.3% | -2.237 to +0.468 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1641 | 939.5 | -42.7% | -983.4 to -419.2 | better |
| response time (ms), 99th percentile | 4051 | 3524 | -13.0% | -1224 to +170.1 | better (inside the noise) |
| time over the response line (% of samples) | 26.7 | 10.66 | -60.1% | -23.97 to -8.116 | better |
| failed requests (%) | 5.83 | 4.274 | -26.7% | -3.158 to +0.04587 | better (inside the noise) |
| HPA replicas, mean | 9.651 | 9.681 | +0.3% | -0.04872 to +0.1105 | WORSE (inside the noise) |
| pods started | 4.625 | 4.125 | -10.8% | -1.913 to +0.9134 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.252e-16 to +9.472e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.6 | 184.5 | -0.6% | -1.549 to -0.6738 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.6 | 184.5 | -0.6% | -1.549 to -0.6738 | better |
| CPU used with Omni's own (cores), mean | 2.499 | 2.399 | -4.0% | -0.1581 to -0.0431 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.98 | 70.8 | -3.0% | -3.782 to -0.5847 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.376e+05 to +8.377e+05 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.718e-06 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 2, worse on 0, inside the noise on 7

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1762 | 1305 | -25.9% | -1033 to +118.5 | better (inside the noise) |
| response time (ms), 99th percentile | 4026 | 3781 | -6.1% | -1121 to +631.5 | better (inside the noise) |
| time over the response line (% of samples) | 32.1 | 18.98 | -40.9% | -21.55 to -4.699 | better |
| failed requests (%) | 10.67 | 9.093 | -14.8% | -3.352 to +0.1883 | better (inside the noise) |
| HPA replicas, mean | 9.62 | 9.575 | -0.5% | -0.2509 to +0.1602 | better (inside the noise) |
| pods started | 4.875 | 4.25 | -12.8% | -2.233 to +0.9826 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -9.472e-16 to +7.252e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 185.1 | -0.4% | -1.617 to +0.195 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 185.1 | -0.4% | -1.617 to +0.195 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.484 | 2.45 | -1.4% | -0.06547 to -0.00337 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 72.46 | 71.76 | -1.0% | -1.772 to +0.392 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 3, worse on 0, inside the noise on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1365 | 649.4 | -52.4% | -1214 to -216.2 | better |
| response time (ms), 99th percentile | 3043 | 1981 | -34.9% | -2554 to +429.5 | better (inside the noise) |
| time over the response line (% of samples) | 21.78 | 11.34 | -47.9% | -17.5 to -3.364 | better |
| failed requests (%) | 6.781 | 5.978 | -11.8% | -1.799 to +0.1925 | better (inside the noise) |
| HPA replicas, mean | 9.663 | 9.616 | -0.5% | -0.139 to +0.0463 | better (inside the noise) |
| pods started | 4.625 | 5.25 | +13.5% | -0.2619 to +1.512 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.467e-16 to +9.908e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 183.4 | 183.1 | -0.2% | -0.9969 to +0.3434 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 183.4 | 183.1 | -0.2% | -0.9969 to +0.3434 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.257 | 2.217 | -1.8% | -0.07344 to -0.007644 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 66.61 | 65.84 | -1.1% | -1.581 to +0.05402 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.985e-09 to -4.984e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0.025 | +0.025 | -0.01371 to +0.06371 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
