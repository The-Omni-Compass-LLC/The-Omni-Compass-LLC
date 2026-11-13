# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column says in words whether it is better or worse. Lower is better for response times, time over the line, failed requests, pods started, replicas, machines, energy and the bill (less spent). Higher is better for the organism's work and work per energy. A change whose interval crosses zero is marked inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud, 1,000 copies: native | Compute / AI / Cloud, 1,000 copies: omni | Physics / Robotics / Autonomous, 1,000 copies: native | Physics / Robotics / Autonomous, 1,000 copies: omni | Energy / Facility / Industrial, 1,000 copies: native | Energy / Facility / Industrial, 1,000 copies: omni | Distribution / Specialized, 1,000 copies: native | Distribution / Specialized, 1,000 copies: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 2586 | 3493 | 2173 | 4003 | 3372 | 2172 | 2729 | 3909 |
| response time (ms), 99th percentile | 5342 | 6982 | 4302 | 6830 | 5681 | 3363 | 5392 | 6191 |
| time over the response line (% of samples) | 62.35 | 67.68 | 51.94 | 64.76 | 64.84 | 37.22 | 68.09 | 56.58 |
| failed requests (%) | 43.45 | 54.27 | 36.4 | 55.36 | 56.53 | 33 | 43.24 | 45.55 |
| HPA replicas, mean | 9.933 | 9.885 | 9.919 | 9.908 | 9.931 | 9.884 | 9.934 | 9.892 |
| pods started | 5.2 | 4.778 | 5.5 | 5.1 | 5 | 5.9 | 5.1 | 5.2 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 1417 | 1412 | 1405 | 1405 | 1408 | 1384 | 1429 | 1400 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1417 | 1412 | 1405 | 1405 | 1408 | 1384 | 1429 | 1400 |
| CPU used with Omni's own (cores), mean | 2.976 | 2.924 | 2.829 |  | 2.863 | 2.936 | 3.143 |  |
| host CPU busy, the real machine under kind (%) | 90.74 | 98.98 | 88.04 | 96.04 | 90.75 | 86.75 | 93.78 | 93.73 |
| organism work | 2.121e+13 | 2.121e+13 | 2.209e+13 | 2.209e+13 | 6.636e+13 | 6.636e+13 | 2.164e+13 | 2.164e+13 |
| organism energy (J) | 1.537e+13 | 1.538e+13 | 1.975e+13 | 1.976e+13 | 1.104e+16 | 1.104e+16 | 5.703e+13 | 5.704e+13 |
| organism time over the line (% of steps) | 1.931 | 1.926 | 4.658 | 4.652 | 1.444 | 1.436 | 2.453 | 2.445 |
| organism work per energy | 1.379 | 1.379 | 1.119 | 1.118 | 0.00601 | 0.00601 | 0.3795 | 0.3795 |
| organism behind its window (s) | 12.98 | 2987 | 8.01 | 1105 | 9.61 | 964.7 | 12.62 | 1318 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud, 1,000 copies: better on 2, worse on 2 (organism energy (J); organism work per energy), inside the noise on 7; OFF THE CLOCK in 9 of 9 repetitions (the organism ended up to 3,518 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

9 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2832 | 3493 | +23.3% | -1310 to +2631 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 5875 | 6982 | +18.8% | -1452 to +3666 | WORSE (inside the noise) |
| time over the response line (% of samples) | 69.11 | 67.68 | -2.1% | -23.11 to +20.25 | better (inside the noise) |
| failed requests (%) | 48.28 | 54.27 | +12.4% | -30.83 to +42.81 | WORSE (inside the noise) |
| HPA replicas, mean | 9.939 | 9.885 | -0.5% | -0.07969 to -0.02878 | better |
| pods started | 5 | 4.778 | -4.4% | -1.146 to +0.7016 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.952e-16 to +6.978e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1425 | 1412 | -0.9% | -38.97 to +12.29 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1425 | 1412 | -0.9% | -38.97 to +12.29 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 3.081 | 2.924 | -5.1% | -0.4946 to +0.1793 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 93.92 | 98.98 | +5.4% | -5.104 to +15.23 | shown, not judged (more or less is not better by itself) |
| organism work | 2.121e+13 | 2.121e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.537e+13 | 1.538e+13 | +0.1% | +1.052e+10 to +1.052e+10 | WORSE |
| organism time over the line (% of steps) | 1.931 | 1.926 | -0.3% | -0.005367 to -0.005367 | better |
| organism work per energy | 1.379 | 1.379 | -0.1% | -0.0009433 to -0.0009433 | WORSE |
| organism behind its window (s) | 13.52 | 2987 | +21990.3% | +2339 to +3608 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous, 1,000 copies: better on 1, worse on 2 (organism energy (J); organism work per energy), inside the noise on 8; OFF THE CLOCK in 8 of 10 repetitions (the organism ended up to 1,587 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2173 | 4003 | +84.2% | -887.7 to +4548 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 4302 | 6830 | +58.8% | -1469 to +6525 | WORSE (inside the noise) |
| time over the response line (% of samples) | 51.94 | 64.76 | +24.7% | -25.39 to +51.03 | WORSE (inside the noise) |
| failed requests (%) | 36.4 | 55.36 | +52.1% | -14.21 to +52.12 | WORSE (inside the noise) |
| HPA replicas, mean | 9.919 | 9.908 | -0.1% | -0.04757 to +0.02726 | better (inside the noise) |
| pods started | 5.5 | 5.1 | -7.3% | -1.477 to +0.6769 | better (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +2.094e-16 to +1.212e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1405 | 1405 | -0.0% | -33.66 to +33.41 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1405 | 1405 | -0.0% | -33.66 to +33.41 | better (inside the noise) |
| host CPU busy, the real machine under kind (%) | 88.04 | 96.04 | +9.1% | -6.098 to +22.1 | shown, not judged (more or less is not better by itself) |
| organism work | 2.209e+13 | 2.209e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.975e+13 | 1.976e+13 | +0.1% | +1.052e+10 to +1.052e+10 | WORSE |
| organism time over the line (% of steps) | 4.658 | 4.652 | -0.1% | -0.006546 to -0.006546 | better |
| organism work per energy | 1.119 | 1.118 | -0.1% | -0.0005957 to -0.0005957 | WORSE |
| organism behind its window (s) | 8.01 | 1105 | +13700.7% | +671.9 to +1523 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial, 1,000 copies: better on 2, worse on 0, inside the noise on 7; OFF THE CLOCK in 4 of 10 repetitions (the organism ended up to 2,564 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 3372 | 2172 | -35.6% | -3283 to +882.8 | better (inside the noise) |
| response time (ms), 99th percentile | 5681 | 3363 | -40.8% | -5370 to +732.9 | better (inside the noise) |
| time over the response line (% of samples) | 64.84 | 37.22 | -42.6% | -65.31 to +10.07 | better (inside the noise) |
| failed requests (%) | 56.53 | 33 | -41.6% | -59.18 to +12.11 | better (inside the noise) |
| HPA replicas, mean | 9.931 | 9.884 | -0.5% | -0.0891 to -0.005317 | better |
| pods started | 5 | 5.9 | +18.0% | -0.19 to +1.99 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | -4.062e-16 to +7.615e-16 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1408 | 1384 | -1.7% | -59.6 to +10.8 | better (inside the noise) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1408 | 1384 | -1.7% | -59.6 to +10.8 | better (inside the noise) |
| CPU used with Omni's own (cores), mean | 2.728 | 2.936 | +7.6% | -1.395 to +1.81 | shown, not judged (more or less is not better by itself) |
| host CPU busy, the real machine under kind (%) | 90.75 | 86.75 | -4.4% | -18.72 to +10.72 | shown, not judged (more or less is not better by itself) |
| organism work | 6.636e+13 | 6.636e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 1.104e+16 | 1.104e+16 | +0.0% | +1.052e+10 to +1.052e+10 | same (under one part in a million) |
| organism time over the line (% of steps) | 1.444 | 1.436 | -0.6% | -0.008013 to -0.008013 | better |
| organism work per energy | 0.00601 | 0.00601 | -0.0% | -5.726e-09 to -5.726e-09 | same (under one part in a million) |
| organism behind its window (s) | 9.61 | 964.7 | +9938.9% | +68.86 to +1841 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized, 1,000 copies: better on 4, worse on 2 (organism energy (J); organism work per energy), inside the noise on 5; OFF THE CLOCK in 6 of 10 repetitions (the organism ended up to 2,401 s after its window: the machine could not step this many muscles in time, and the cell's last steps saw a cluster at rest)

10 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2729 | 3909 | +43.2% | -763.1 to +3123 | WORSE (inside the noise) |
| response time (ms), 99th percentile | 5392 | 6191 | +14.8% | -1546 to +3143 | WORSE (inside the noise) |
| time over the response line (% of samples) | 68.09 | 56.58 | -16.9% | -25.48 to +2.466 | better (inside the noise) |
| failed requests (%) | 43.24 | 45.55 | +5.3% | -18.72 to +23.35 | WORSE (inside the noise) |
| HPA replicas, mean | 9.934 | 9.892 | -0.4% | -0.05964 to -0.02405 | better |
| pods started | 5.1 | 5.2 | +2.0% | -0.5263 to +0.7263 | WORSE (inside the noise) |
| worker nodes in service, mean | 6 | 6 | +0.0% | +3.874e-17 to +1.56e-15 | same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 1429 | 1400 | -2.0% | -49.01 to -8.431 | better |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 1429 | 1400 | -2.0% | -49.01 to -8.431 | better |
| host CPU busy, the real machine under kind (%) | 93.78 | 93.73 | -0.0% | -7.477 to +7.39 | shown, not judged (more or less is not better by itself) |
| organism work | 2.164e+13 | 2.164e+13 | +0.0% | +0 to +0 | same |
| organism energy (J) | 5.703e+13 | 5.704e+13 | +0.0% | +1.052e+10 to +1.052e+10 | WORSE |
| organism time over the line (% of steps) | 2.453 | 2.445 | -0.3% | -0.007771 to -0.007771 | better |
| organism work per energy | 0.3795 | 0.3795 | -0.0% | -7e-05 to -7e-05 | WORSE |
| organism behind its window (s) | 12.62 | 1318 | +10344.9% | +496 to +2115 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

## Not in this run

- The whole tower, every muscle once
- The four stacked, duplicates kept

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
