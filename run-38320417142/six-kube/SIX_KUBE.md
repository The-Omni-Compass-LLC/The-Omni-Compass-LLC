# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1781 | 965.4 | 2434 | 1733 | 2101 | 1513 | 2321 | 1598 | 1647 | 1133 | 1487 | 933.8 |
| response time (ms), 99th percentile | 4194 | 3179 | 5908 | 5964 | 5196 | 4949 | 6074 | 5025 | 3868 | 2997 | 4617 | 3422 |
| time over the response line (% of samples) | 30.99 | 17.03 | 29.18 | 14.62 | 25.8 | 13.96 | 40.21 | 20.13 | 27.32 | 15.72 | 28.75 | 15.72 |
| failed requests (%) | 10.9 | 9.245 | 7.452 | 5.632 | 6.115 | 5.333 | 10.66 | 8.925 | 8.677 | 7.937 | 8.915 | 8.232 |
| HPA replicas, mean | 9.727 | 9.733 | 9.699 | 9.777 | 9.721 | 9.728 | 9.781 | 9.757 | 9.616 | 9.627 | 9.712 | 9.754 |
| pods started | 3.9 | 3.9 | 4 | 3.1 | 3.4 | 3.1 | 3.1 | 3.6 | 4.4 | 3.9 | 4.1 | 3.5 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 186.8 | 186.2 | 185.9 | 185.4 | 184.3 | 183.6 | 190.3 | 190.2 | 184.6 | 184.6 | 186 | 186.1 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.8 | 186.2 | 185.9 | 185.4 | 184.3 | 183.6 | 190.3 | 190.2 | 184.6 | 184.6 | 186 | 186.1 |
| CPU used with Omni's own (cores), mean | 2.563 | 2.531 | 2.613 | 2.553 | 2.408 | 2.378 | 2.94 | 2.911 | 2.392 | 2.405 | 2.538 | 2.537 |
| host CPU busy, the real machine under kind (%) | 74.75 | 74.07 | 75.78 | 74.46 | 70.24 | 69.31 | 85.03 | 84.26 | 70.02 | 70.15 | 74.22 | 74.3 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.597e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.927 | 4.251 | 4.179 | 1.42 | 1.364 | 2.303 | 2.264 | 2.431 | 2.407 | 2.401 | 2.347 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0.02 | 0.01 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1781 | 965.4 | -45.8% | -1178 to -453.9 | better |
| response time (ms), 99th percentile | 4194 | 3179 | -24.2% | -1787 to -243.2 | better |
| time over the response line (% of samples) | 30.99 | 17.03 | -45.0% | -20.02 to -7.889 | better |
| failed requests (%) | 10.9 | 9.245 | -15.2% | -3.313 to +0.0004689 | better (inside the noise) |
| HPA replicas, mean | 9.727 | 9.733 | +0.1% | -0.03493 to +0.04853 | WORSE (inside the noise) |
| pods started | 3.9 | 3.9 | +0.0% | -0.9537 to +0.9537 | same |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.47e-16 to +1.358e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.8 | 186.2 | -0.3% | -1.529 to +0.2727 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.8 | 186.2 | -0.3% | -1.529 to +0.2727 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.563 | 2.531 | -1.3% | -0.06944 to +0.005098 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.75 | 74.07 | -0.9% | -1.432 to +0.06514 | shown, not judged (more or less is not better by itself) |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +6.834e+06 to +6.836e+06 | WORSE |
| organism time over the line (% of steps) | 1.976 | 1.927 | -2.5% | -0.04938 to -0.04938 | better |
| organism work per energy | 1.404 | 1.403 | -0.0% | -0.0006456 to -0.0006455 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2434 | 1733 | -28.8% | -1096 to -307.3 | better |
| response time (ms), 99th percentile | 5908 | 5964 | +0.9% | -564.9 to +676.3 | WORSE (inside the noise) |
| time over the response line (% of samples) | 29.18 | 14.62 | -49.9% | -19.34 to -9.769 | better |
| failed requests (%) | 7.452 | 5.632 | -24.4% | -3.083 to -0.5576 | better |
| HPA replicas, mean | 9.699 | 9.777 | +0.8% | -0.00169 to +0.1568 | WORSE (inside the noise) |
| pods started | 4 | 3.1 | -22.5% | -2.225 to +0.4254 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.023e-16 to +1.213e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 185.9 | 185.4 | -0.3% | -0.8558 to -0.1684 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 185.9 | 185.4 | -0.3% | -0.8558 to -0.1684 | better |
| CPU used with Omni's own (cores), mean | 2.613 | 2.553 | -2.3% | -0.08792 to -0.03173 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 75.78 | 74.46 | -1.7% | -1.862 to -0.7823 | shown, not judged (more or less is not better by itself) |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +9.059e+06 to +9.06e+06 | WORSE |
| organism time over the line (% of steps) | 4.251 | 4.179 | -1.7% | -0.07219 to -0.07219 | better |
| organism work per energy | 1.125 | 1.124 | -0.0% | -0.0005302 to -0.0005302 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: better on 3, worse on 0, inside the noise on 6

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2101 | 1513 | -28.0% | -1135 to -40.88 | better |
| response time (ms), 99th percentile | 5196 | 4949 | -4.8% | -1083 to +588.8 | better (inside the noise) |
| time over the response line (% of samples) | 25.8 | 13.96 | -45.9% | -17.37 to -6.302 | better |
| failed requests (%) | 6.115 | 5.333 | -12.8% | -1.632 to +0.06695 | better (inside the noise) |
| HPA replicas, mean | 9.721 | 9.728 | +0.1% | -0.04511 to +0.05894 | WORSE (inside the noise) |
| pods started | 3.4 | 3.1 | -8.8% | -1.257 to +0.6567 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.363e-16 to +8.692e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.3 | 183.6 | -0.4% | -1.46 to +0.01826 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.3 | 183.6 | -0.4% | -1.46 to +0.01826 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.408 | 2.378 | -1.3% | -0.05961 to -0.001531 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 70.24 | 69.31 | -1.3% | -1.5 to -0.3548 | shown, not judged (more or less is not better by itself) |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +6.914e+06 to +6.914e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.364 | -4.0% | -0.05642 to -0.05642 | better |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -4.494e-09 to -4.494e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2321 | 1598 | -31.1% | -1123 to -321.4 | better |
| response time (ms), 99th percentile | 6074 | 5025 | -17.3% | -1891 to -206.6 | better |
| time over the response line (% of samples) | 40.21 | 20.13 | -49.9% | -23.47 to -16.68 | better |
| failed requests (%) | 10.66 | 8.925 | -16.3% | -2.89 to -0.5751 | better |
| HPA replicas, mean | 9.781 | 9.757 | -0.3% | -0.1039 to +0.05484 | better (inside the noise) |
| pods started | 3.1 | 3.6 | +16.1% | -0.7729 to +1.773 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.43e-16 to +7.206e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.3 | 190.2 | -0.1% | -0.4691 to +0.2595 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.3 | 190.2 | -0.1% | -0.4691 to +0.2595 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.94 | 2.911 | -1.0% | -0.05351 to -0.005783 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.03 | 84.26 | -0.9% | -1.46 to -0.08604 | shown, not judged (more or less is not better by itself) |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.596e+10 | 5.597e+10 | +0.0% | +6.376e+06 to +6.376e+06 | WORSE |
| organism time over the line (% of steps) | 2.303 | 2.264 | -1.7% | -0.03874 to -0.03874 | better |
| organism work per energy | 0.382 | 0.382 | -0.0% | -4.352e-05 to -4.352e-05 | WORSE |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1647 | 1133 | -31.2% | -774.2 to -252.7 | better |
| response time (ms), 99th percentile | 3868 | 2997 | -22.5% | -1395 to -347.8 | better |
| time over the response line (% of samples) | 27.32 | 15.72 | -42.5% | -17.51 to -5.7 | better |
| failed requests (%) | 8.677 | 7.937 | -8.5% | -1.674 to +0.1927 | better (inside the noise) |
| HPA replicas, mean | 9.616 | 9.627 | +0.1% | -0.07632 to +0.09854 | WORSE (inside the noise) |
| pods started | 4.4 | 3.9 | -11.4% | -1.408 to +0.4079 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.623e-16 to +1.25e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 184.6 | 184.6 | +0.0% | -0.7416 to +0.8765 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 184.6 | 184.6 | +0.0% | -0.7416 to +0.8765 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.392 | 2.405 | +0.5% | -0.02067 to +0.04608 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 70.02 | 70.15 | +0.2% | -0.7787 to +1.049 | shown, not judged (more or less is not better by itself) |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +6.908e+06 to +6.908e+06 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.407 | -1.0% | -0.02447 to -0.02447 | better |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -4.601e-09 to -4.601e-09 | same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1487 | 933.8 | -37.2% | -888.8 to -217.2 | better |
| response time (ms), 99th percentile | 4617 | 3422 | -25.9% | -2112 to -278.6 | better |
| time over the response line (% of samples) | 28.75 | 15.72 | -45.3% | -18.61 to -7.456 | better |
| failed requests (%) | 8.915 | 8.232 | -7.7% | -1.522 to +0.156 | better (inside the noise) |
| HPA replicas, mean | 9.712 | 9.754 | +0.4% | -0.0271 to +0.1122 | WORSE (inside the noise) |
| pods started | 4.1 | 3.5 | -14.6% | -1.998 to +0.7985 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.494e-16 to +6.718e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186 | 186.1 | +0.0% | -0.5283 to +0.6201 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186 | 186.1 | +0.0% | -0.5283 to +0.6201 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.538 | 2.537 | -0.0% | -0.03933 to +0.03787 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 74.22 | 74.3 | +0.1% | -0.7913 to +0.9629 | shown, not judged (more or less is not better by itself) |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +2.918e+07 to +2.918e+07 | WORSE |
| organism time over the line (% of steps) | 2.401 | 2.347 | -2.2% | -0.05328 to -0.05328 | better |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -3.637e-08 to -3.637e-08 | WORSE |
| organism behind its window (s) | 0.02 | 0.01 | -50.0% | -0.0506 to +0.0306 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
