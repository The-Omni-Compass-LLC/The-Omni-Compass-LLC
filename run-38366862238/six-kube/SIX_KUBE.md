# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 10 copies: native | Compute / AI / Cloud, 10 copies: omni | Physics / Robotics / Autonomous, 10 copies: native | Physics / Robotics / Autonomous, 10 copies: omni | Energy / Facility / Industrial, 10 copies: native | Energy / Facility / Industrial, 10 copies: omni | Distribution / Specialized, 10 copies: native | Distribution / Specialized, 10 copies: omni | The whole tower, every muscle once, 10 copies: native | The whole tower, every muscle once, 10 copies: omni | The four stacked, duplicates kept, 10 copies: native | The four stacked, duplicates kept, 10 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1894 | 886.9 | 2377 | 1515 | 2109 | 1473 | 3632 | 2562 | 3880 | 2041 | 2838 | 1502 |
| response time (ms), 99th percentile | 3606 | 2214 | 4086 | 3684 | 4081 | 3140 | 6268 | 6078 | 6899 | 6113 | 5558 | 4635 |
| time over the response line (% of samples) | 42.52 | 30.64 | 45.87 | 34.36 | 31.23 | 21.25 | 57.25 | 45.84 | 67.06 | 53.77 | 63.58 | 44.42 |
| failed requests (%) | 24.47 | 22.64 | 27.52 | 24.52 | 16.45 | 14.69 | 35.18 | 32.54 | 39.95 | 40.1 | 30.98 | 28.57 |
| HPA replicas, mean | 9.714 | 9.726 | 9.701 | 9.678 | 9.622 | 9.655 | 9.818 | 9.806 | 9.837 | 9.868 | 9.825 | 9.861 |
| pods started | 4.125 | 4 | 3.875 | 4.5 | 5.25 | 4.625 | 2.5 | 3.125 | 2.75 | 2.25 | 3.125 | 2.25 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 187.7 | 187.6 | 190.2 | 189.8 | 186.3 | 186.4 | 191.8 | 191.8 | 193.3 | 192.9 | 193 | 191.6 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.7 | 187.6 | 190.2 | 189.8 | 186.3 | 186.4 | 191.8 | 191.8 | 193.3 | 192.9 | 193 | 191.6 |
| CPU used with Omni's own (cores), mean | 2.75 | 2.71 | 2.905 | 2.872 | 2.607 | 2.577 | 3.131 | 3.093 | 3.275 | 3.22 | 3.212 | 3.134 |
| host CPU busy, the real machine under kind (%) | 79.4 | 79.3 | 84.72 | 83.92 | 76.43 | 76.34 | 89.9 | 89.89 | 95.18 | 95.46 | 94.15 | 95.14 |
| organism work | 2.181e+11 | 2.181e+11 | 2.265e+11 | 2.265e+11 | 6.678e+11 | 6.678e+11 | 2.226e+11 | 2.226e+11 | 6.905e+11 | 6.905e+11 | 1.335e+12 | 1.335e+12 |
| organism energy (J) | 1.584e+11 | 1.585e+11 | 2.017e+11 | 2.018e+11 | 1.103e+14 | 1.103e+14 | 5.689e+11 | 5.69e+11 | 1.108e+14 | 1.108e+14 | 1.112e+14 | 1.112e+14 |
| organism time over the line (% of steps) | 2.018 | 1.945 | 4.802 | 4.711 | 1.468 | 1.384 | 2.574 | 2.478 | 2.707 | 2.671 | 2.61 | 2.524 |
| organism work per energy | 1.377 | 1.376 | 1.123 | 1.123 | 0.006055 | 0.006055 | 0.3913 | 0.3912 | 0.006233 | 0.006233 | 0.012 | 0.012 |
| organism behind its window (s) | 0.075 | 0.0625 | 0.0875 | 0.075 | 0.0375 | 0.025 | 0.0875 | 0.125 | 0.2125 | 0.275 | 0.45 | 0.375 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 10 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1894 | 886.9 | -53.2% | -1692 to -321.2 | better |
| response time (ms), 99th percentile | 3606 | 2214 | -38.6% | -2412 to -372.3 | better |
| time over the response line (% of samples) | 42.52 | 30.64 | -27.9% | -19.78 to -3.976 | better |
| failed requests (%) | 24.47 | 22.64 | -7.5% | -3.381 to -0.2931 | better |
| HPA replicas, mean | 9.714 | 9.726 | +0.1% | -0.03974 to +0.06308 | WORSE (inside the noise) |
| pods started | 4.125 | 4 | -3.0% | -0.9537 to +0.7037 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.742e-15 to +6.316e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 187.7 | 187.6 | -0.1% | -0.5707 to +0.3697 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 187.7 | 187.6 | -0.1% | -0.5707 to +0.3697 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.75 | 2.71 | -1.5% | -0.07144 to -0.008767 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 79.4 | 79.3 | -0.1% | -1.129 to +0.9304 | shown, not judged (more or less is not better by itself) |
| organism work | 2.181e+11 | 2.181e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.584e+11 | 1.585e+11 | +0.1% | +8.192e+07 to +8.192e+07 | WORSE |
| organism time over the line (% of steps) | 2.018 | 1.945 | -3.6% | -0.07361 to -0.07361 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007116 to -0.0007116 | WORSE |
| organism behind its window (s) | 0.075 | 0.0625 | -16.7% | -0.04206 to +0.01706 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 10 copies: better on 2, worse on 2 (organism energy (J); organism work per energy), inside the noise on 7

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2377 | 1515 | -36.3% | -1815 to +91 | better (inside the noise) |
| response time (ms), 99th percentile | 4086 | 3684 | -9.8% | -1469 to +666.5 | better (inside the noise) |
| time over the response line (% of samples) | 45.87 | 34.36 | -25.1% | -17.28 to -5.751 | better |
| failed requests (%) | 27.52 | 24.52 | -10.9% | -6.139 to +0.1348 | better (inside the noise) |
| HPA replicas, mean | 9.701 | 9.678 | -0.2% | -0.08775 to +0.04221 | better (inside the noise) |
| pods started | 3.875 | 4.5 | +16.1% | -0.4641 to +1.714 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.011e-15 to +2.346e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 190.2 | 189.8 | -0.2% | -1.509 to +0.7529 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 190.2 | 189.8 | -0.2% | -1.509 to +0.7529 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.905 | 2.872 | -1.2% | -0.09254 to +0.02502 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.72 | 83.92 | -0.9% | -2.59 to +0.9972 | shown, not judged (more or less is not better by itself) |
| organism work | 2.265e+11 | 2.265e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 2.017e+11 | 2.018e+11 | +0.0% | +8.456e+07 to +8.456e+07 | WORSE |
| organism time over the line (% of steps) | 4.802 | 4.711 | -1.9% | -0.09169 to -0.09169 | better |
| organism work per energy | 1.123 | 1.123 | -0.0% | -0.0004707 to -0.0004707 | WORSE |
| organism behind its window (s) | 0.0875 | 0.075 | -14.3% | -0.08228 to +0.05728 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 10 copies: better on 2, worse on 0, inside the noise on 7

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2109 | 1473 | -30.2% | -1352 to +79.26 | better (inside the noise) |
| response time (ms), 99th percentile | 4081 | 3140 | -23.1% | -2077 to +193.3 | better (inside the noise) |
| time over the response line (% of samples) | 31.23 | 21.25 | -31.9% | -16.35 to -3.591 | better |
| failed requests (%) | 16.45 | 14.69 | -10.7% | -3.674 to +0.1507 | better (inside the noise) |
| HPA replicas, mean | 9.622 | 9.655 | +0.3% | -0.04197 to +0.1082 | WORSE (inside the noise) |
| pods started | 5.25 | 4.625 | -11.9% | -1.884 to +0.6342 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -2.06e-15 to +5.053e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 186.3 | 186.4 | +0.0% | -1.12 to +1.299 | WORSE (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 186.3 | 186.4 | +0.0% | -1.12 to +1.299 | WORSE (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.607 | 2.577 | -1.2% | -0.07828 to +0.01645 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 76.43 | 76.34 | -0.1% | -1.198 to +1.027 | shown, not judged (more or less is not better by itself) |
| organism work | 6.678e+11 | 6.678e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.103e+14 | 1.103e+14 | +0.0% | +8.139e+07 to +8.139e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.384 | -5.7% | -0.0842 to -0.0842 | better |
| organism work per energy | 0.006055 | 0.006055 | -0.0% | -4.468e-09 to -4.468e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.0375 | 0.025 | -33.3% | -0.04206 to +0.01706 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 10 copies: better on 3, worse on 3 (pods started; organism energy (J); organism work per energy), inside the noise on 5

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3632 | 2562 | -29.4% | -2155 to +16.17 | better (inside the noise) |
| response time (ms), 99th percentile | 6268 | 6078 | -3.0% | -2211 to +1832 | better (inside the noise) |
| time over the response line (% of samples) | 57.25 | 45.84 | -19.9% | -16.37 to -6.461 | better |
| failed requests (%) | 35.18 | 32.54 | -7.5% | -4.516 to -0.773 | better |
| HPA replicas, mean | 9.818 | 9.806 | -0.1% | -0.05185 to +0.02717 | better (inside the noise) |
| pods started | 2.5 | 3.125 | +25.0% | +0.002882 to +1.247 | WORSE |
| worker nodes in service, mean | 6 | 6 | +0.0% | -9.716e-16 to +1.194e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 191.8 | 191.8 | -0.0% | -0.6386 to +0.5213 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 191.8 | 191.8 | -0.0% | -0.6386 to +0.5213 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.131 | 3.093 | -1.2% | -0.05223 to -0.02403 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.9 | 89.89 | -0.0% | -0.4823 to +0.4524 | shown, not judged (more or less is not better by itself) |
| organism work | 2.226e+11 | 2.226e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.689e+11 | 5.69e+11 | +0.0% | +8.794e+07 to +8.794e+07 | WORSE |
| organism time over the line (% of steps) | 2.574 | 2.478 | -3.7% | -0.09599 to -0.09599 | better |
| organism work per energy | 0.3913 | 0.3912 | -0.0% | -6.048e-05 to -6.048e-05 | WORSE |
| organism behind its window (s) | 0.0875 | 0.125 | +42.9% | -0.02471 to +0.09971 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once, 10 copies: better on 3, worse on 0, inside the noise on 6

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3880 | 2041 | -47.4% | -2892 to -786.9 | better |
| response time (ms), 99th percentile | 6899 | 6113 | -11.4% | -2929 to +1356 | better (inside the noise) |
| time over the response line (% of samples) | 67.06 | 53.77 | -19.8% | -20.29 to -6.301 | better |
| failed requests (%) | 39.95 | 40.1 | +0.4% | -3.212 to +3.516 | WORSE (inside the noise) |
| HPA replicas, mean | 9.837 | 9.868 | +0.3% | -0.04011 to +0.1029 | WORSE (inside the noise) |
| pods started | 2.75 | 2.25 | -18.2% | -1.841 to +0.8408 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -1.705e-15 to +1.038e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 193.3 | 192.9 | -0.2% | -1.247 to +0.4787 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193.3 | 192.9 | -0.2% | -1.247 to +0.4787 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.275 | 3.22 | -1.7% | -0.06937 to -0.03947 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 95.18 | 95.46 | +0.3% | -0.09693 to +0.6523 | shown, not judged (more or less is not better by itself) |
| organism work | 6.905e+11 | 6.905e+11 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.108e+14 | 1.108e+14 | +0.0% | +8.142e+07 to +8.142e+07 | same (under one part in a million) |
| organism time over the line (% of steps) | 2.707 | 2.671 | -1.3% | -0.03651 to -0.03651 | better |
| organism work per energy | 0.006233 | 0.006233 | -0.0% | -4.58e-09 to -4.58e-09 | same (under one part in a million) |
| organism behind its window (s) | 0.2125 | 0.275 | +29.4% | -0.02619 to +0.1512 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept, 10 copies: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

8 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2838 | 1502 | -47.1% | -2196 to -476.8 | better |
| response time (ms), 99th percentile | 5558 | 4635 | -16.6% | -3240 to +1394 | better (inside the noise) |
| time over the response line (% of samples) | 63.58 | 44.42 | -30.1% | -22.89 to -15.44 | better |
| failed requests (%) | 30.98 | 28.57 | -7.8% | -4.197 to -0.6322 | better |
| HPA replicas, mean | 9.825 | 9.861 | +0.4% | -0.02272 to +0.09474 | WORSE (inside the noise) |
| pods started | 3.125 | 2.25 | -28.0% | -2.009 to +0.259 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.171e-15 to +1.394e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 193 | 191.6 | -0.7% | -2.702 to -0.1412 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 193 | 191.6 | -0.7% | -2.702 to -0.1412 | better |
| CPU used with Omni's own (cores), mean | 3.212 | 3.134 | -2.4% | -0.1027 to -0.0529 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 94.15 | 95.14 | +1.1% | +0.7862 to +1.194 | shown, not judged (more or less is not better by itself) |
| organism work | 1.335e+12 | 1.335e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.112e+14 | 1.112e+14 | +0.0% | +3.358e+08 to +3.358e+08 | WORSE |
| organism time over the line (% of steps) | 2.61 | 2.524 | -3.3% | -0.08578 to -0.08578 | better |
| organism work per energy | 0.012 | 0.012 | -0.0% | -3.624e-08 to -3.624e-08 | WORSE |
| organism behind its window (s) | 0.45 | 0.375 | -16.7% | -0.2282 to +0.0782 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
