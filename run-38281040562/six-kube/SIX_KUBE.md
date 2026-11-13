# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 4241 | 4617 | 3637 | 2741 | 3631 | 2889 | 2561 | 2672 |
| response time (ms), 99th percentile | 7209 | 7993 | 5862 | 5527 | 6375 | 5899 | 4154 | 4806 |
| time over the response line (% of samples) | 74.17 | 66.03 | 58.78 | 49.8 | 50.92 | 42.33 | 37.35 | 29.95 |
| failed requests (%) | 46.13 | 45.68 | 37.51 | 35.82 | 25.49 | 24.1 | 20.64 | 20.09 |
| HPA replicas, mean | 9.852 | 9.875 | 9.844 | 9.864 | 9.829 | 9.827 | 9.775 | 9.772 |
| pods started | 3.5 | 2.8 | 3.5 | 2.9 | 3.9 | 3.7 | 4.5 | 4.7 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 290 | 286.4 | 286.2 | 284.2 | 285.6 | 283.7 | 281.2 | 280.5 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 290 | 286.4 | 286.2 | 284.2 | 285.6 | 283.7 | 281.2 | 280.5 |
| CPU used with Omni's own (cores), mean | 3.318 | 3.104 | 3.078 | 2.964 | 3.024 | 2.922 | 2.76 | 2.688 |
| host CPU busy, the real machine under kind (%) | 97.45 | 98.43 | 91.5 | 92.49 | 89.74 | 91.63 | 81.31 | 84.92 |
| organism work | 2.126e+12 | 2.126e+12 | 2.213e+12 | 2.213e+12 | 6.649e+12 | 6.649e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.539e+12 | 1.54e+12 | 1.975e+12 | 1.976e+12 | 1.098e+15 | 1.098e+15 | 5.718e+12 | 5.719e+12 |
| organism time over the line (% of steps) | 1.958 | 1.952 | 4.623 | 4.615 | 1.468 | 1.459 | 2.485 | 2.476 |
| organism work per energy | 1.381 | 1.38 | 1.12 | 1.12 | 0.006054 | 0.006054 | 0.3796 | 0.3795 |
| organism behind its window (s) | 1.63 | 2.14 | 1.1 | 1.53 | 1.24 | 0.52 | 0.63 | 1.22 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4241 | 4617 | +8.9% | -1152 to +1905 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 7209 | 7993 | +10.9% | -378.4 to +1946 | WORSE (inside the noise) |
| time over the response line (% of samples) | 74.17 | 66.03 | -11.0% | -11.81 to -4.477 | better |
| failed requests (%) | 46.13 | 45.68 | -1.0% | -3.459 to +2.558 | better (inside the noise) |
| HPA replicas, mean | 9.852 | 9.875 | +0.2% | -0.01092 to +0.05648 | WORSE (inside the noise) |
| pods started | 3.5 | 2.8 | -20.0% | -1.595 to +0.1953 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.221e-15 to +1.576e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 290 | 286.4 | -1.2% | -5.028 to -2.02 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 290 | 286.4 | -1.2% | -5.028 to -2.02 | better |
| CPU used with Omni's own (cores), mean | 3.318 | 3.104 | -6.5% | -0.244 to -0.1843 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 97.45 | 98.43 | +1.0% | +0.2648 to +1.701 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.539e+12 | 1.54e+12 | +0.1% | +1.052e+09 to +1.052e+09 | WORSE |
| organism time over the line (% of steps) | 1.958 | 1.952 | -0.3% | -0.005715 to -0.005715 | better |
| organism work per energy | 1.381 | 1.38 | -0.1% | -0.0009432 to -0.0009432 | WORSE |
| organism behind its window (s) | 1.63 | 2.14 | +31.3% | +0.01851 to +1.001 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3637 | 2741 | -24.6% | -2077 to +285.7 | better (inside the noise) |
| response time (ms), 99th percentile | 5862 | 5527 | -5.7% | -1260 to +589.9 | better (inside the noise) |
| time over the response line (% of samples) | 58.78 | 49.8 | -15.3% | -11.52 to -6.454 | better |
| failed requests (%) | 37.51 | 35.82 | -4.5% | -3.304 to -0.07542 | better |
| HPA replicas, mean | 9.844 | 9.864 | +0.2% | -0.03691 to +0.07713 | WORSE (inside the noise) |
| pods started | 3.5 | 2.9 | -17.1% | -1.778 to +0.5778 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.126e-15 to +1.304e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 286.2 | 284.2 | -0.7% | -3.366 to -0.5946 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 286.2 | 284.2 | -0.7% | -3.366 to -0.5946 | better |
| CPU used with Omni's own (cores), mean | 3.078 | 2.964 | -3.7% | -0.1492 to -0.07974 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.5 | 92.49 | +1.1% | +0.3113 to +1.673 | shown, not judged (more or less is not better by itself) |
| organism work | 2.213e+12 | 2.213e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.975e+12 | 1.976e+12 | +0.1% | +1.052e+09 to +1.052e+09 | WORSE |
| organism time over the line (% of steps) | 4.623 | 4.615 | -0.2% | -0.007112 to -0.007103 | better |
| organism work per energy | 1.12 | 1.12 | -0.1% | -0.0005963 to -0.0005963 | WORSE |
| organism behind its window (s) | 1.1 | 1.53 | +39.1% | -0.1676 to +1.028 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3631 | 2889 | -20.4% | -1793 to +309.5 | better (inside the noise) |
| response time (ms), 99th percentile | 6375 | 5899 | -7.5% | -1204 to +252.4 | better (inside the noise) |
| time over the response line (% of samples) | 50.92 | 42.33 | -16.9% | -12.86 to -4.307 | better |
| failed requests (%) | 25.49 | 24.1 | -5.4% | -3.651 to +0.8785 | better (inside the noise) |
| HPA replicas, mean | 9.829 | 9.827 | -0.0% | -0.0413 to +0.03695 | better (inside the noise) |
| pods started | 3.9 | 3.7 | -5.1% | -1.079 to +0.6793 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.02e-16 to +1.823e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.6 | 283.7 | -0.7% | -3.75 to -0.03374 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.6 | 283.7 | -0.7% | -3.75 to -0.03374 | better |
| CPU used with Omni's own (cores), mean | 3.024 | 2.922 | -3.4% | -0.1481 to -0.05516 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.74 | 91.63 | +2.1% | +0.7839 to +2.997 | shown, not judged (more or less is not better by itself) |
| organism work | 6.649e+12 | 6.649e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +1.052e+09 to +1.052e+09 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.459 | -0.6% | -0.00836 to -0.00836 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -5.797e-09 to -5.797e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.24 | 0.52 | -58.1% | -1.06 to -0.3798 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 2, worse on 2 (organism energy (J); organism work per energy), inside the noise on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2561 | 2672 | +4.3% | -675.5 to +897.1 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 4154 | 4806 | +15.7% | -583.1 to +1887 | WORSE (inside the noise) |
| time over the response line (% of samples) | 37.35 | 29.95 | -19.8% | -10.61 to -4.195 | better |
| failed requests (%) | 20.64 | 20.09 | -2.7% | -3.812 to +2.712 | better (inside the noise) |
| HPA replicas, mean | 9.775 | 9.772 | -0.0% | -0.03826 to +0.0313 | better (inside the noise) |
| pods started | 4.5 | 4.7 | +4.4% | -0.6121 to +1.012 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.957e-16 to +1.661e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 281.2 | 280.5 | -0.3% | -2.721 to +1.127 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 281.2 | 280.5 | -0.3% | -2.721 to +1.127 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.76 | 2.688 | -2.6% | -0.1514 to +0.006435 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 81.31 | 84.92 | +4.4% | +1.725 to +5.487 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.718e+12 | 5.719e+12 | +0.0% | +1.052e+09 to +1.052e+09 | WORSE |
| organism time over the line (% of steps) | 2.485 | 2.476 | -0.3% | -0.008263 to -0.008263 | better |
| organism work per energy | 0.3796 | 0.3795 | -0.0% | -6.981e-05 to -6.981e-05 | WORSE |
| organism behind its window (s) | 0.63 | 1.22 | +93.7% | +0.2108 to +0.9692 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
