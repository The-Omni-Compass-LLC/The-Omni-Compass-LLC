# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 100 copies: native | Compute / AI / Cloud, 100 copies: omni | Physics / Robotics / Autonomous, 100 copies: native | Physics / Robotics / Autonomous, 100 copies: omni | Energy / Facility / Industrial, 100 copies: native | Energy / Facility / Industrial, 100 copies: omni | Distribution / Specialized, 100 copies: native | Distribution / Specialized, 100 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 3334 | 3026 | 3255 | 2797 | 3380 | 3015 | 4260 | 3830 |
| response time (ms), 99th percentile | 5329 | 5390 | 5057 | 5085 | 5846 | 5498 | 6538 | 6555 |
| time over the response line (% of samples) | 56.44 | 50.85 | 52.55 | 46.17 | 54.32 | 47.04 | 63.36 | 58.32 |
| failed requests (%) | 39.28 | 38.65 | 35.98 | 34.27 | 34.08 | 32.83 | 46.73 | 46.43 |
| HPA replicas, mean | 9.842 | 9.845 | 9.844 | 9.838 | 9.85 | 9.836 | 9.866 | 9.86 |
| pods started | 3.536 | 3.214 | 3.25 | 3.464 | 3.357 | 3.571 | 2.929 | 2.964 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 281.8 | 283.7 | 281.6 | 284.2 | 282.5 | 287 | 284.3 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 281.8 | 283.7 | 281.6 | 284.2 | 282.5 | 287 | 284.3 |
| CPU used with Omni's own (cores), mean | 2.978 | 2.811 | 2.898 | 2.791 | 2.967 | 2.86 | 3.131 | 2.947 |
| host CPU busy, the real machine under kind (%) | 88.52 | 90.94 | 86.75 | 87.96 | 88.94 | 91.13 | 92.84 | 94.51 |
| organism work | 2.126e+12 | 2.126e+12 | 2.214e+12 | 2.214e+12 | 6.65e+12 | 6.65e+12 | 2.171e+12 | 2.171e+12 |
| organism energy (J) | 1.544e+12 | 1.545e+12 | 1.98e+12 | 1.981e+12 | 1.098e+15 | 1.098e+15 | 5.723e+12 | 5.724e+12 |
| organism time over the line (% of steps) | 1.963 | 1.892 | 4.564 | 4.47 | 1.484 | 1.395 | 2.479 | 2.391 |
| organism work per energy | 1.377 | 1.376 | 1.118 | 1.117 | 0.006054 | 0.006054 | 0.3794 | 0.3793 |
| organism behind its window (s) | 1.543 | 1.889 | 0.7607 | 0.9857 | 1.275 | 1.15 | 1.079 | 2.082 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3334 | 3026 | -9.3% | -1057 to +439.8 | better (inside the noise) |
| response time (ms), 99th percentile | 5329 | 5390 | +1.1% | -575.9 to +697.8 | WORSE (inside the noise) |
| time over the response line (% of samples) | 56.44 | 50.85 | -9.9% | -7.038 to -4.141 | better |
| failed requests (%) | 39.28 | 38.65 | -1.6% | -3.415 to +2.158 | better (inside the noise) |
| HPA replicas, mean | 9.842 | 9.845 | +0.0% | -0.01066 to +0.01701 | WORSE (inside the noise) |
| pods started | 3.536 | 3.214 | -9.1% | -0.6248 to -0.0181 | better |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.489e-16 to +1.31e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.7 | 281.8 | -1.0% | -3.775 to -2.095 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.7 | 281.8 | -1.0% | -3.775 to -2.095 | better |
| CPU used with Omni's own (cores), mean | 2.978 | 2.811 | -5.6% | -0.2113 to -0.1227 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.52 | 90.94 | +2.7% | +1.411 to +3.42 | shown, not judged (more or less is not better by itself) |
| organism work | 2.126e+12 | 2.126e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.544e+12 | 1.545e+12 | +0.1% | +8.502e+08 to +8.502e+08 | WORSE |
| organism time over the line (% of steps) | 1.963 | 1.892 | -3.6% | -0.07143 to -0.07143 | better |
| organism work per energy | 1.377 | 1.376 | -0.1% | -0.0007578 to -0.0007578 | WORSE |
| organism behind its window (s) | 1.543 | 1.889 | +22.5% | +0.1373 to +0.5556 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 100 copies: better on 5, worse on 2 (organism energy (J); organism work per energy), inside the noise on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3255 | 2797 | -14.1% | -1038 to +123.3 | better (inside the noise) |
| response time (ms), 99th percentile | 5057 | 5085 | +0.6% | -561.7 to +618.8 | WORSE (inside the noise) |
| time over the response line (% of samples) | 52.55 | 46.17 | -12.1% | -8.212 to -4.552 | better |
| failed requests (%) | 35.98 | 34.27 | -4.7% | -2.842 to -0.5746 | better |
| HPA replicas, mean | 9.844 | 9.838 | -0.1% | -0.02606 to +0.01389 | better (inside the noise) |
| pods started | 3.25 | 3.464 | +6.6% | -0.2293 to +0.6578 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +1.791e-16 to +1.09e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 283.7 | 281.6 | -0.7% | -2.816 to -1.235 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 283.7 | 281.6 | -0.7% | -2.816 to -1.235 | better |
| CPU used with Omni's own (cores), mean | 2.898 | 2.791 | -3.7% | -0.1316 to -0.08317 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 86.75 | 87.96 | +1.4% | +0.7035 to +1.731 | shown, not judged (more or less is not better by itself) |
| organism work | 2.214e+12 | 2.214e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.98e+12 | 1.981e+12 | +0.0% | +8.723e+08 to +8.723e+08 | WORSE |
| organism time over the line (% of steps) | 4.564 | 4.47 | -2.1% | -0.09382 to -0.09382 | better |
| organism work per energy | 1.118 | 1.117 | -0.0% | -0.0004922 to -0.0004922 | WORSE |
| organism behind its window (s) | 0.7607 | 0.9857 | +29.6% | +0.03436 to +0.4156 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 100 copies: better on 5, worse on 0, inside the noise on 4

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3380 | 3015 | -10.8% | -882.9 to +151.4 | better (inside the noise) |
| response time (ms), 99th percentile | 5846 | 5498 | -5.9% | -899.1 to +203.5 | better (inside the noise) |
| time over the response line (% of samples) | 54.32 | 47.04 | -13.4% | -8.794 to -5.77 | better |
| failed requests (%) | 34.08 | 32.83 | -3.7% | -2.232 to -0.2614 | better |
| HPA replicas, mean | 9.85 | 9.836 | -0.1% | -0.04128 to +0.01355 | better (inside the noise) |
| pods started | 3.357 | 3.571 | +6.4% | -0.4495 to +0.8781 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -6.412e-16 to +7.681e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 284.2 | 282.5 | -0.6% | -2.407 to -0.9236 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 284.2 | 282.5 | -0.6% | -2.407 to -0.9236 | better |
| CPU used with Omni's own (cores), mean | 2.967 | 2.86 | -3.6% | -0.144 to -0.06997 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 88.94 | 91.13 | +2.5% | +1.294 to +3.087 | shown, not judged (more or less is not better by itself) |
| organism work | 6.65e+12 | 6.65e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.098e+15 | 1.098e+15 | +0.0% | +8.696e+08 to +8.696e+08 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.484 | 1.395 | -5.9% | -0.08819 to -0.08819 | better |
| organism work per energy | 0.006054 | 0.006054 | -0.0% | -4.793e-09 to -4.793e-09 | same (under one part in a million) |
| organism behind its window (s) | 1.275 | 1.15 | -9.8% | -0.412 to +0.162 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 100 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5

28 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 4260 | 3830 | -10.1% | -1152 to +293 | better (inside the noise) |
| response time (ms), 99th percentile | 6538 | 6555 | +0.3% | -617.9 to +651.7 | WORSE (inside the noise) |
| time over the response line (% of samples) | 63.36 | 58.32 | -8.0% | -6.375 to -3.715 | better |
| failed requests (%) | 46.73 | 46.43 | -0.6% | -2.622 to +2.03 | better (inside the noise) |
| HPA replicas, mean | 9.866 | 9.86 | -0.1% | -0.02892 to +0.01869 | better (inside the noise) |
| pods started | 2.929 | 2.964 | +1.2% | -0.5023 to +0.5737 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.032e-16 to +1.346e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 287 | 284.3 | -0.9% | -3.521 to -1.83 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 287 | 284.3 | -0.9% | -3.521 to -1.83 | better |
| CPU used with Omni's own (cores), mean | 3.131 | 2.947 | -5.9% | -0.2193 to -0.1498 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 92.84 | 94.51 | +1.8% | +0.9056 to +2.435 | shown, not judged (more or less is not better by itself) |
| organism work | 2.171e+12 | 2.171e+12 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.723e+12 | 5.724e+12 | +0.0% | +8.844e+08 to +8.844e+08 | WORSE |
| organism time over the line (% of steps) | 2.479 | 2.391 | -3.6% | -0.08846 to -0.08846 | better |
| organism work per energy | 0.3794 | 0.3793 | -0.0% | -5.862e-05 to -5.862e-05 | WORSE |
| organism behind its window (s) | 1.079 | 2.082 | +93.0% | +0.7819 to +1.225 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
