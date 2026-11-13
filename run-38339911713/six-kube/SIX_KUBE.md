# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3069 | 3409 | 4598 | 3153 | 3921 | 3250 | 4817 | 3140 |
| response time (ms), 99th percentile | 5106 | 5770 | 7232 | 6068 | 6272 | 5396 | 7295 | 6603 |
| time over the response line (% of samples) | 51.72 | 47.42 | 70 | 61.78 | 60.26 | 55.06 | 60.31 | 55.46 |
| failed requests (%) | 33.02 | 34.84 | 49.9 | 49.55 | 42.71 | 43.06 | 41 | 42.56 |
| HPA replicas, mean | 9.835 | 9.822 | 9.917 | 9.93 | 9.871 | 9.864 | 9.868 | 9.858 |
| pods started | 3.6 | 3.8 | 1.8 | 1.5 | 2.7 | 2.8 | 2.7 | 2.9 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 283.6 | 281.2 | 288.7 | 286.7 | 284.2 | 281.6 | 287.1 | 283.8 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.6 | 281.2 | 288.7 | 286.7 | 284.2 | 281.6 | 287.1 | 283.8 |
| CPU used with Omni's own (cores), mean | 2.877 | 2.727 | 3.222 | 3.09 | 2.987 | 2.833 | 3.135 | 2.956 |
| host CPU busy, the real machine under kind (%) | 85.16 | 87.84 | 96.14 | 96.97 | 89.78 | 90.95 | 92.34 | 94.06 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 1.4 | 2.04 | 0.86 | 1.24 | 1.27 | 1.45 | 1.05 | 2.14 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3069 | 3409 | +11.1% | -1604 to +2284 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 5106 | 5770 | +13.0% | -795.3 to +2125 | WORSE (inside the noise) |
| time over the response line (% of samples) | 51.72 | 47.42 | -8.3% | -6.102 to -2.512 | better |
| failed requests (%) | 33.02 | 34.84 | +5.5% | -2.349 to +5.993 | WORSE (inside the noise) |
| HPA replicas, mean | 9.835 | 9.822 | -0.1% | -0.03412 to +0.008818 | better (inside the noise) |
| pods started | 3.6 | 3.8 | +5.6% | -0.2524 to +0.6524 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.5e-16 to +1.216e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 283.6 | 281.2 | -0.8% | -4.5 to -0.2873 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.6 | 281.2 | -0.8% | -4.5 to -0.2873 | better |
| CPU used with Omni's own (cores), mean | 2.877 | 2.727 | -5.2% | -0.2428 to -0.05714 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 85.16 | 87.84 | +3.1% | +0.6683 to +4.693 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | WORSE |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | WORSE |
| organism behind its window (s) | 1.4 | 2.04 | +45.7% | +0.2119 to +1.068 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4598 | 3153 | -31.4% | -2900 to +11.35 | better (inside the noise) |
| response time (ms), 99th percentile | 7232 | 6068 | -16.1% | -2934 to +606.1 | better (inside the noise) |
| time over the response line (% of samples) | 70 | 61.78 | -11.7% | -11.62 to -4.812 | better |
| failed requests (%) | 49.9 | 49.55 | -0.7% | -2.394 to +1.7 | better (inside the noise) |
| HPA replicas, mean | 9.917 | 9.93 | +0.1% | -0.03333 to +0.05832 | WORSE (inside the noise) |
| pods started | 1.8 | 1.5 | -16.7% | -1.369 to +0.769 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.416e-16 to +1.863e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 288.7 | 286.7 | -0.7% | -2.788 to -1.243 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 288.7 | 286.7 | -0.7% | -2.788 to -1.243 | better |
| CPU used with Omni's own (cores), mean | 3.222 | 3.09 | -4.1% | -0.1674 to -0.09634 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 96.14 | 96.97 | +0.9% | +0.08816 to +1.574 | shown, not judged (more or less is not better by itself) |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | WORSE |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | better |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | WORSE |
| organism behind its window (s) | 0.86 | 1.24 | +44.2% | +0.05517 to +0.7048 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 4, worse on 0, inside the noise on 5

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3921 | 3250 | -17.1% | -1746 to +403.4 | better (inside the noise) |
| response time (ms), 99th percentile | 6272 | 5396 | -14.0% | -2023 to +272.1 | better (inside the noise) |
| time over the response line (% of samples) | 60.26 | 55.06 | -8.6% | -7.257 to -3.15 | better |
| failed requests (%) | 42.71 | 43.06 | +0.8% | -1.723 to +2.426 | WORSE (inside the noise) |
| HPA replicas, mean | 9.871 | 9.864 | -0.1% | -0.04611 to +0.03159 | better (inside the noise) |
| pods started | 2.7 | 2.8 | +3.7% | -0.8204 to +1.02 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -8.939e-16 to +1.249e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.2 | 281.6 | -0.9% | -3.933 to -1.106 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.2 | 281.6 | -0.9% | -3.933 to -1.106 | better |
| CPU used with Omni's own (cores), mean | 2.987 | 2.833 | -5.2% | -0.2175 to -0.09182 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 89.78 | 90.95 | +1.3% | +0.2789 to +2.062 | shown, not judged (more or less is not better by itself) |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.27 | 1.45 | +14.2% | -0.5084 to +0.8684 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4817 | 3140 | -34.8% | -3155 to -199.6 | better |
| response time (ms), 99th percentile | 7295 | 6603 | -9.5% | -2281 to +896.8 | better (inside the noise) |
| time over the response line (% of samples) | 60.31 | 55.46 | -8.1% | -6.69 to -3.025 | better |
| failed requests (%) | 41 | 42.56 | +3.8% | -3.13 to +6.243 | WORSE (inside the noise) |
| HPA replicas, mean | 9.868 | 9.858 | -0.1% | -0.05217 to +0.03087 | better (inside the noise) |
| pods started | 2.7 | 2.9 | +7.4% | -0.7417 to +1.142 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -5.436e-16 to +8.989e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 287.1 | 283.8 | -1.2% | -5.023 to -1.729 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287.1 | 283.8 | -1.2% | -5.023 to -1.729 | better |
| CPU used with Omni's own (cores), mean | 3.135 | 2.956 | -5.7% | -0.2437 to -0.1132 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 92.34 | 94.06 | +1.9% | +0.1669 to +3.273 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | WORSE |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | better |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | WORSE |
| organism behind its window (s) | 1.05 | 2.14 | +103.8% | +0.609 to +1.571 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
