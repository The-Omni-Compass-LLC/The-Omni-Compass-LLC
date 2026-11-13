# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3566 | 3312 | 3795 | 2941 | 3612 | 3115 | 4298 | 3635 |
| response time (ms), 99th percentile | 5794 | 5455 | 6224 | 5839 | 5854 | 5852 | 6374 | 5953 |
| time over the response line (% of samples) | 58.36 | 53.18 | 61.75 | 55.2 | 58.31 | 52.29 | 57.43 | 53.08 |
| failed requests (%) | 41.14 | 39.9 | 43.78 | 42.85 | 40.19 | 39.07 | 39.47 | 41.05 |
| HPA replicas, mean | 9.854 | 9.846 | 9.874 | 9.868 | 9.869 | 9.865 | 9.851 | 9.843 |
| pods started | 3.21 | 3.323 | 2.726 | 2.774 | 2.919 | 2.952 | 3.129 | 3.274 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 284.9 | 282.4 | 285.7 | 283.8 | 285.1 | 282.8 | 285.8 | 283.2 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.9 | 282.4 | 285.7 | 283.8 | 285.1 | 282.8 | 285.8 | 283.2 |
| CPU used with Omni's own (cores), mean | 2.99 | 2.821 | 3.042 | 2.916 | 2.999 | 2.868 | 3.046 | 2.89 |
| host CPU busy, the real machine under kind (%) | 88.91 | 91.46 | 91.01 | 92.21 | 90.22 | 91.92 | 90.09 | 92.59 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 1.669 | 2.055 | 0.8581 | 1.302 | 1.306 | 1.248 | 1.055 | 1.971 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3566 | 3312 | -7.1% | -736.5 to +227.9 | better (inside the noise) |
| response time (ms), 99th percentile | 5794 | 5455 | -5.9% | -783.8 to +105.1 | better (inside the noise) |
| time over the response line (% of samples) | 58.36 | 53.18 | -8.9% | -5.967 to -4.395 | better |
| failed requests (%) | 41.14 | 39.9 | -3.0% | -2.455 to -0.01823 | better |
| HPA replicas, mean | 9.854 | 9.846 | -0.1% | -0.02402 to +0.008627 | better (inside the noise) |
| pods started | 3.21 | 3.323 | +3.5% | -0.2751 to +0.5009 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.042e-16 to +1.186e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.9 | 282.4 | -0.9% | -3.103 to -1.858 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.9 | 282.4 | -0.9% | -3.103 to -1.858 | better |
| CPU used with Omni's own (cores), mean | 2.99 | 2.821 | -5.7% | -0.2049 to -0.1337 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.91 | 91.46 | +2.9% | +1.734 to +3.369 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | WORSE |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | WORSE |
| organism behind its window (s) | 1.669 | 2.055 | +23.1% | +0.205 to +0.5659 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 6, worse on 2 (organism energy (J); organism work per energy), inside the noise on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3795 | 2941 | -22.5% | -1247 to -462.1 | better |
| response time (ms), 99th percentile | 6224 | 5839 | -6.2% | -823.8 to +53.41 | better (inside the noise) |
| time over the response line (% of samples) | 61.75 | 55.2 | -10.6% | -7.616 to -5.496 | better |
| failed requests (%) | 43.78 | 42.85 | -2.1% | -1.589 to -0.2678 | better |
| HPA replicas, mean | 9.874 | 9.868 | -0.1% | -0.0216 to +0.01015 | better (inside the noise) |
| pods started | 2.726 | 2.774 | +1.8% | -0.3245 to +0.4212 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.332e-16 to +1.027e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.7 | 283.8 | -0.7% | -2.32 to -1.468 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.7 | 283.8 | -0.7% | -2.32 to -1.468 | better |
| CPU used with Omni's own (cores), mean | 3.042 | 2.916 | -4.1% | -0.1422 to -0.109 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 91.01 | 92.21 | +1.3% | +0.8163 to +1.579 | shown, not judged (more or less is not better by itself) |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | WORSE |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | better |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | WORSE |
| organism behind its window (s) | 0.8581 | 1.302 | +51.7% | +0.2851 to +0.602 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 6, worse on 0, inside the noise on 3

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3612 | 3115 | -13.8% | -904.1 to -89.25 | better |
| response time (ms), 99th percentile | 5854 | 5852 | -0.0% | -479.3 to +475.1 | better (inside the noise) |
| time over the response line (% of samples) | 58.31 | 52.29 | -10.3% | -6.938 to -5.096 | better |
| failed requests (%) | 40.19 | 39.07 | -2.8% | -2.013 to -0.2203 | better |
| HPA replicas, mean | 9.869 | 9.865 | -0.0% | -0.02166 to +0.01405 | better (inside the noise) |
| pods started | 2.919 | 2.952 | +1.1% | -0.3783 to +0.4428 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -1.968e-16 to +5.406e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.1 | 282.8 | -0.8% | -2.767 to -1.744 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.1 | 282.8 | -0.8% | -2.767 to -1.744 | better |
| CPU used with Omni's own (cores), mean | 2.999 | 2.868 | -4.4% | -0.1535 to -0.1083 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 90.22 | 91.92 | +1.9% | +1.202 to +2.202 | shown, not judged (more or less is not better by itself) |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.306 | 1.248 | -4.4% | -0.1846 to +0.0685 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

62 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4298 | 3635 | -15.4% | -1191 to -136.2 | better |
| response time (ms), 99th percentile | 6374 | 5953 | -6.6% | -886.7 to +43.44 | better (inside the noise) |
| time over the response line (% of samples) | 57.43 | 53.08 | -7.6% | -5.189 to -3.521 | better |
| failed requests (%) | 39.47 | 41.05 | +4.0% | -0.4027 to +3.57 | WORSE (inside the noise) |
| HPA replicas, mean | 9.851 | 9.843 | -0.1% | -0.02256 to +0.007161 | better (inside the noise) |
| pods started | 3.129 | 3.274 | +4.6% | -0.1794 to +0.4697 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +4.73e-16 to +1.217e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 285.8 | 283.2 | -0.9% | -3.149 to -2.021 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 285.8 | 283.2 | -0.9% | -3.149 to -2.021 | better |
| CPU used with Omni's own (cores), mean | 3.046 | 2.89 | -5.1% | -0.1884 to -0.1233 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 90.09 | 92.59 | +2.8% | +1.708 to +3.306 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | WORSE |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | better |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | WORSE |
| organism behind its window (s) | 1.055 | 1.971 | +86.9% | +0.7515 to +1.081 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
