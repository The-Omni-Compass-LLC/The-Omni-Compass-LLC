# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2598 | 3598 | 3255 | 2814 | 2664 | 2123 | 3856 | 3432 |
| response time (ms), 99th percentile | 4865 | 5326 | 4879 | 4956 | 4045 | 4256 | 6025 | 5332 |
| time over the response line (% of samples) | 41.55 | 33.84 | 52.62 | 46.67 | 42.65 | 38.16 | 54.64 | 49.89 |
| failed requests (%) | 13.51 | 14.7 | 36.92 | 35.32 | 30.55 | 30.6 | 39.44 | 39.62 |
| HPA replicas, mean | 9.779 | 9.779 | 9.817 | 9.814 | 9.804 | 9.797 | 9.813 | 9.83 |
| pods started | 5.2 | 4.8 | 4 | 3.8 | 4.1 | 4.4 | 3.8 | 3.6 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 283.9 | 282.4 | 282.2 | 280.2 | 279.6 | 278.8 | 284.8 | 282 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.9 | 282.4 | 282.2 | 280.2 | 279.6 | 278.8 | 284.8 | 282 |
| CPU used with Omni's own (cores), mean | 2.913 | 2.808 | 2.817 | 2.598 | 2.678 | 2.466 | 2.976 | 2.708 |
| host CPU busy, the real machine under kind (%) | 85.31 | 89.23 | 84.47 | 85.46 | 80.86 | 82.72 | 88.26 | 90.11 |
| organism work | 2.126e+12 | 2.126e+12 | 2.213e+12 | 2.213e+12 | 6.649e+12 | 6.649e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.539e+12 | 1.54e+12 | 1.975e+12 | 1.976e+12 | 1.098e+15 | 1.098e+15 | 5.718e+12 | 5.719e+12 |
| organism time over the line (% of steps) | 1.958 | 1.952 | 4.623 | 4.615 | 1.468 | 1.459 | 2.485 | 2.476 |
| organism work per energy | 1.381 | 1.38 | 1.12 | 1.12 | 0.006054 | 0.006054 | 0.3796 | 0.3795 |
| organism behind its window (s) | 1.44 | 1.52 | 0.91 | 1.34 | 1.22 | 0.65 | 0.75 | 1.78 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2598 | 3598 | +38.5% | -762 to +2763 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 4865 | 5326 | +9.5% | -866.8 to +1789 | WORSE (inside the noise) |
| time over the response line (% of samples) | 41.55 | 33.84 | -18.6% | -10.65 to -4.77 | better |
| failed requests (%) | 13.51 | 14.7 | +8.8% | -1.631 to +4.019 | WORSE (inside the noise) |
| HPA replicas, mean | 9.779 | 9.779 | -0.0% | -0.0296 to +0.02942 | better (inside the noise) |
| pods started | 5.2 | 4.8 | -7.7% | -1.003 to +0.2032 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.72e-15 to +1.72e-15 | same |
| energy, parked workers still on at idle power (Wh, declared model) | 283.9 | 282.4 | -0.5% | -2.492 to -0.5173 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.9 | 282.4 | -0.5% | -2.492 to -0.5173 | better |
| CPU used with Omni's own (cores), mean | 2.873 | 2.808 | -2.3% | -0.14 to +0.01066 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.31 | 89.23 | +4.6% | +1.971 to +5.859 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.539e+12 | 1.54e+12 | +0.1% | +1.052e+09 to +1.052e+09 | WORSE |
| organism time over the line (% of steps) | 1.958 | 1.952 | -0.3% | -0.005715 to -0.005715 | better |
| organism work per energy | 1.381 | 1.38 | -0.1% | -0.0009433 to -0.0009432 | WORSE |
| organism behind its window (s) | 1.44 | 1.52 | +5.6% | -0.1935 to +0.3535 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3255 | 2814 | -13.6% | -1822 to +939.8 | better (inside the noise) |
| response time (ms), 99th percentile | 4879 | 4956 | +1.6% | -784.8 to +939.5 | WORSE (inside the noise) |
| time over the response line (% of samples) | 52.62 | 46.67 | -11.3% | -9.585 to -2.324 | better |
| failed requests (%) | 36.92 | 35.32 | -4.3% | -2.888 to -0.3152 | better |
| HPA replicas, mean | 9.817 | 9.814 | -0.0% | -0.05924 to +0.0532 | better (inside the noise) |
| pods started | 4 | 3.8 | -5.0% | -1.54 to +1.14 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -3.642e-16 to +2.496e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 282.2 | 280.2 | -0.7% | -3.094 to -0.8606 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 282.2 | 280.2 | -0.7% | -3.094 to -0.8606 | better |
| CPU used with Omni's own (cores), mean | 2.705 | 2.598 | -4.0% | -0.1616 to -0.053 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 84.47 | 85.46 | +1.2% | +0.3055 to +1.661 | shown, not judged (more or less is not better by itself) |
| organism work | 2.213e+12 | 2.213e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.975e+12 | 1.976e+12 | +0.1% | +1.052e+09 to +1.052e+09 | WORSE |
| organism time over the line (% of steps) | 4.623 | 4.615 | -0.2% | -0.007107 to -0.007107 | better |
| organism work per energy | 1.12 | 1.12 | -0.1% | -0.0005963 to -0.0005963 | WORSE |
| organism behind its window (s) | 0.91 | 1.34 | +47.3% | +0.03525 to +0.8248 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 2, worse on 0, inside the noise on 7

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2664 | 2123 | -20.3% | -1322 to +239.7 | better (inside the noise) |
| response time (ms), 99th percentile | 4045 | 4256 | +5.2% | -724.8 to +1148 | WORSE (inside the noise) |
| time over the response line (% of samples) | 42.65 | 38.16 | -10.5% | -8.176 to -0.7988 | better |
| failed requests (%) | 30.55 | 30.6 | +0.2% | -1.05 to +1.15 | WORSE (inside the noise) |
| HPA replicas, mean | 9.804 | 9.797 | -0.1% | -0.03365 to +0.01962 | better (inside the noise) |
| pods started | 4.1 | 4.4 | +7.3% | -0.1828 to +0.7828 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.161e-16 to +1.304e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 279.6 | 278.8 | -0.3% | -2.115 to +0.469 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 279.6 | 278.8 | -0.3% | -2.115 to +0.469 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.534 | 2.466 | -2.7% | -0.1292 to -0.006751 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 80.86 | 82.72 | +2.3% | +0.5552 to +3.167 | shown, not judged (more or less is not better by itself) |
| organism work | 6.649e+12 | 6.649e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +1.052e+09 to +1.052e+09 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.468 | 1.459 | -0.6% | -0.00836 to -0.00836 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -5.797e-09 to -5.797e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.22 | 0.65 | -46.7% | -0.8828 to -0.2572 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3856 | 3432 | -11.0% | -1676 to +828.2 | better (inside the noise) |
| response time (ms), 99th percentile | 6025 | 5332 | -11.5% | -1967 to +580.8 | better (inside the noise) |
| time over the response line (% of samples) | 54.64 | 49.89 | -8.7% | -6.172 to -3.316 | better |
| failed requests (%) | 39.44 | 39.62 | +0.5% | -2.286 to +2.651 | WORSE (inside the noise) |
| HPA replicas, mean | 9.813 | 9.83 | +0.2% | -0.0523 to +0.08652 | WORSE (inside the noise) |
| pods started | 3.8 | 3.6 | -5.3% | -1.879 to +1.479 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -7.733e-16 to +1.484e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.8 | 282 | -1.0% | -3.946 to -1.709 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.8 | 282 | -1.0% | -3.946 to -1.709 | better |
| CPU used with Omni's own (cores), mean | 2.834 | 2.708 | -4.5% | -0.2183 to -0.03513 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.26 | 90.11 | +2.1% | +0.3738 to +3.326 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.718e+12 | 5.719e+12 | +0.0% | +1.052e+09 to +1.052e+09 | WORSE |
| organism time over the line (% of steps) | 2.485 | 2.476 | -0.3% | -0.008263 to -0.008263 | better |
| organism work per energy | 0.3796 | 0.3795 | -0.0% | -6.981e-05 to -6.981e-05 | WORSE |
| organism behind its window (s) | 0.75 | 1.78 | +137.3% | +0.5531 to +1.507 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
