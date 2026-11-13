# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1645 | 760 | 2803 | 2134 | 2568 | 1727 | 966.9 | 579.4 | 1542 | 1097 | 1927 | 1115 |
| response time (ms), 99th percentile | 3953 | 3049 | 7246 | 6568 | 6516 | 6284 | 2532 | 2388 | 3431 | 3185 | 5036 | 4097 |
| time over the response line (% of samples) | 25.7 | 13.09 | 34.94 | 18.82 | 33.44 | 17.74 | 16.51 | 6.815 | 26.12 | 16.27 | 33.49 | 18.82 |
| failed requests (%) | 8.224 | 7.055 | 8.375 | 7.599 | 8.824 | 7.266 | 2.781 | 2.379 | 8.975 | 8.08 | 11.6 | 10.05 |
| HPA replicas, mean | 9.679 | 9.714 | 9.843 | 9.857 | 9.82 | 9.85 | 9.574 | 9.609 | 9.654 | 9.651 | 9.786 | 9.765 |
| pods started | 4.7 | 4.4 | 2.6 | 2.1 | 2.6 | 2.2 | 5.3 | 5.1 | 4.4 | 4.3 | 3.2 | 3.3 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 184.7 | 188.4 | 188.4 | 187.8 | 187.7 | 182.3 | 181.8 | 184.6 | 184.1 | 187.8 | 187.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 184.7 | 188.4 | 188.4 | 187.8 | 187.7 | 182.3 | 181.8 | 184.6 | 184.1 | 187.8 | 187.3 |
| CPU used with Omni's own (cores), mean | 2.447 | 2.418 | 2.829 | 2.821 | 2.791 | 2.758 | 2.148 | 2.106 | 2.385 | 2.379 | 2.69 | 2.67 |
| host CPU busy, the real machine under kind (%) | 71.87 | 71.29 | 81.9 | 81.82 | 80.66 | 79.94 | 64 | 62.8 | 69.93 | 69.88 | 78.3 | 78.21 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.02 | 0.01 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1645 | 760 | -53.8% | -1419 to -351.8 | better |
| response time (ms), 99th percentile | 3953 | 3049 | -22.9% | -1931 to +123 | better (inside the noise) |
| time over the response line (% of samples) | 25.7 | 13.09 | -49.1% | -18.54 to -6.668 | better |
| failed requests (%) | 8.224 | 7.055 | -14.2% | -2.357 to +0.01977 | better (inside the noise) |
| HPA replicas, mean | 9.679 | 9.714 | +0.4% | -0.005761 to +0.07668 | WORSE (inside the noise) |
| pods started | 4.7 | 4.4 | -6.4% | -1.257 to +0.6567 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.146e-15 to +9.679e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.3 | 184.7 | -0.3% | -1.287 to +0.0213 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.3 | 184.7 | -0.3% | -1.287 to +0.0213 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.447 | 2.418 | -1.2% | -0.06688 to +0.007774 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 71.87 | 71.29 | -0.8% | -1.23 to +0.07896 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.613e+05 to +8.627e+05 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.151e-05 to -8.138e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 3, worse on 2 (organism energy (J); organism work per energy), inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2803 | 2134 | -23.9% | -1168 to -171.9 | better |
| response time (ms), 99th percentile | 7246 | 6568 | -9.4% | -1553 to +196.5 | better (inside the noise) |
| time over the response line (% of samples) | 34.94 | 18.82 | -46.1% | -18.8 to -13.44 | better |
| failed requests (%) | 8.375 | 7.599 | -9.3% | -1.792 to +0.2406 | better (inside the noise) |
| HPA replicas, mean | 9.843 | 9.857 | +0.1% | -0.03657 to +0.06312 | WORSE (inside the noise) |
| pods started | 2.6 | 2.1 | -19.2% | -1.408 to +0.4079 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.161e-16 to +1.304e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 188.4 | 188.4 | -0.0% | -0.3888 to +0.3726 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 188.4 | 188.4 | -0.0% | -0.3888 to +0.3726 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.829 | 2.821 | -0.3% | -0.03535 to +0.01865 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.9 | 81.82 | -0.1% | -0.5321 to +0.3538 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.409e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.247e-05 to -8.244e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2568 | 1727 | -32.7% | -1437 to -244.5 | better |
| response time (ms), 99th percentile | 6516 | 6284 | -3.6% | -953.8 to +490 | better (inside the noise) |
| time over the response line (% of samples) | 33.44 | 17.74 | -46.9% | -18.42 to -12.97 | better |
| failed requests (%) | 8.824 | 7.266 | -17.7% | -2.755 to -0.3614 | better |
| HPA replicas, mean | 9.82 | 9.85 | +0.3% | -0.03897 to +0.09944 | WORSE (inside the noise) |
| pods started | 2.6 | 2.2 | -15.4% | -1.625 to +0.8251 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.432e-15 to +1.073e-17 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.8 | 187.7 | -0.1% | -0.5512 to +0.2427 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.8 | 187.7 | -0.1% | -0.5512 to +0.2427 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.791 | 2.758 | -1.2% | -0.05859 to -0.008197 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 80.66 | 79.94 | -0.9% | -1.399 to -0.04818 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 966.9 | 579.4 | -40.1% | -529.6 to -245.3 | better |
| response time (ms), 99th percentile | 2532 | 2388 | -5.7% | -758.8 to +470.6 | better (inside the noise) |
| time over the response line (% of samples) | 16.51 | 6.815 | -58.7% | -14.65 to -4.736 | better |
| failed requests (%) | 2.781 | 2.379 | -14.5% | -0.9429 to +0.1392 | better (inside the noise) |
| HPA replicas, mean | 9.574 | 9.609 | +0.4% | -0.02759 to +0.09685 | WORSE (inside the noise) |
| pods started | 5.3 | 5.1 | -3.8% | -1.142 to +0.7417 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.312e-15 to +6.012e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 181.8 | -0.3% | -0.852 to -0.2574 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 181.8 | -0.3% | -0.852 to -0.2574 | better |
| CPU used with Omni's own (cores), mean | 2.148 | 2.106 | -2.0% | -0.07073 to -0.01431 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 64 | 62.8 | -1.9% | -1.945 to -0.4644 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.377e+05 to +8.378e+05 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 3, worse on 0, inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1542 | 1097 | -28.9% | -737.9 to -153.2 | better |
| response time (ms), 99th percentile | 3431 | 3185 | -7.2% | -1056 to +564.7 | better (inside the noise) |
| time over the response line (% of samples) | 26.12 | 16.27 | -37.7% | -15.17 to -4.535 | better |
| failed requests (%) | 8.975 | 8.08 | -10.0% | -1.931 to +0.1425 | better (inside the noise) |
| HPA replicas, mean | 9.654 | 9.651 | -0.0% | -0.0582 to +0.0525 | better (inside the noise) |
| pods started | 4.4 | 4.3 | -2.3% | -0.7263 to +0.5263 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.755e-16 to +1.441e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.1 | -0.3% | -1.31 to +0.2682 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.1 | -0.3% | -1.31 to +0.2682 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.385 | 2.379 | -0.2% | -0.04578 to +0.03457 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 69.93 | 69.88 | -0.1% | -1.093 to +0.9869 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1927 | 1115 | -42.1% | -1311 to -313.2 | better |
| response time (ms), 99th percentile | 5036 | 4097 | -18.6% | -2053 to +175.1 | better (inside the noise) |
| time over the response line (% of samples) | 33.49 | 18.82 | -43.8% | -20.09 to -9.245 | better |
| failed requests (%) | 11.6 | 10.05 | -13.4% | -2.902 to -0.2033 | better |
| HPA replicas, mean | 9.786 | 9.765 | -0.2% | -0.05825 to +0.01547 | better (inside the noise) |
| pods started | 3.2 | 3.3 | +3.1% | -0.5263 to +0.7263 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.213e-15 to +5.023e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.8 | 187.3 | -0.2% | -1.16 to +0.2492 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.8 | 187.3 | -0.2% | -1.16 to +0.2492 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.69 | 2.67 | -0.8% | -0.04961 to +0.009147 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 78.3 | 78.21 | -0.1% | -0.6898 to +0.5081 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +3.999e+06 to +4.001e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.02 | 0.01 | -50.0% | -0.0506 to +0.0306 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
