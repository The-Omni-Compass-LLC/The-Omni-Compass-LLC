# The six organisms with the real Kubernetes cluster inside: native against native with Omni-Compass on top

> © 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. `SPDX-License-Identifier: LicenseRef-OmniCompass-Evaluation-1.0` All patents, copyrights and trademarks filed in the USA. www.omni-compass.com

Each organism runs on the measured window's clock with the cluster as one more muscle (`tools/run_kil.py`): its own compute demand drives the load generator, the cluster's watts are its heat and load. Native: the stacks' own controllers and Kubernetes alone. Omni: the compass law on every simulated muscle and the live controller on the cluster, handed back at 90% of the window. Cluster rows are measured on the real cluster (energy is the declared power model; the bill, where present, is Azure's own count of machines). Organism rows are models (evidence S).

How to read it: every change is omni against native (omni is Omni-Compass on top of native), and the Reading column gives its word, GAIN, EVEN or LOSS, by what the gauge is for and never by its sign (the key: `docs/HOW_TO_READ_THE_RESULTS.md`): response times, time over the line and failed requests are time waited, missed or failed, so a fall is GAIN; the organism's work and work per energy are work done, so a rise is GAIN; pods started, replicas, machines, energy and the bill are resources spent, so a fall is a cut, a GAIN, and a rise is **power given**, never a loss. A change whose interval crosses zero reads EVEN, inside the noise. The organism must keep the window's clock: the row "organism behind its window" says how long after the window its last step ended (0 is on the clock), and a repetition where either arm ended more than 5% of the window late is marked OFF THE CLOCK in the organism's line, because its last steps saw a cluster whose load schedule had already ended.

## Twelve columns, mean over repetitions

| Gauge | Compute / AI / Cloud: native | Compute / AI / Cloud: omni | Physics / Robotics / Autonomous: native | Physics / Robotics / Autonomous: omni | Energy / Facility / Industrial: native | Energy / Facility / Industrial: omni | Distribution / Specialized: native | Distribution / Specialized: omni | The whole tower, every muscle once: native | The whole tower, every muscle once: omni | The four stacked, duplicates kept: native | The four stacked, duplicates kept: omni |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| response time (ms), 95th percentile | 1693 | 1580 | 2313 | 2040 | 2080 | 2043 | 1711 | 1524 | 1557 | 1513 | 1860 | 1747 |
| response time (ms), 99th percentile | 5001 | 5094 | 6077 | 6152 | 6771 | 6253 | 4607 | 4546 | 4481 | 4875 | 5451 | 5508 |
| time over the response line (% of samples) | 31.61 | 22.39 | 22.58 | 16.81 | 23.4 | 17.09 | 25.9 | 18.21 | 24.27 | 16.88 | 32.47 | 23.24 |
| failed requests (%) | 14.41 | 12.13 | 7.857 | 7.235 | 7.846 | 6.865 | 8.536 | 7.512 | 9.416 | 7.166 | 14.68 | 12.57 |
| HPA replicas, mean | 9.707 | 12.33 | 9.653 | 13.96 | 9.678 | 14.22 | 9.616 | 13.38 | 9.611 | 12.87 | 9.716 | 12.6 |
| pods started | 4.439 | 9.829 | 4.976 | 9.634 | 4.805 | 10.24 | 4.854 | 9.878 | 5.195 | 10.56 | 4.61 | 9.707 |
| worker nodes in service, mean | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 | 6 |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.2 | 182 | 180.8 | 182.2 | 181.7 | 181.5 | 181.6 | 181 | 181.1 | 182.6 | 182.9 |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.2 | 182 | 180.8 | 182.2 | 181.7 | 181.5 | 181.6 | 181 | 181.1 | 182.6 | 182.9 |
| CPU used with Omni's own (cores), mean | 2.235 | 2.219 | 2.122 | 2.122 | 2.161 | 2.162 | 2.119 | 2.119 | 2.082 | 2.077 | 2.26 | 2.265 |
| host CPU busy, the real machine under kind (%) | 66.22 | 66.08 | 62.77 | 63.03 | 63.83 | 63.96 | 62.72 | 63.1 | 61.71 | 61.97 | 67.2 | 67.65 |
| organism work | 2.085e+10 | 2.085e+10 | 2.16e+10 | 2.16e+10 | 6.708e+10 | 6.708e+10 | 2.138e+10 | 2.138e+10 | 6.941e+10 | 6.941e+10 | 1.309e+11 | 1.309e+11 |
| organism energy (J) | 1.485e+10 | 1.486e+10 | 1.921e+10 | 1.921e+10 | 1.016e+13 | 1.016e+13 | 5.596e+10 | 5.596e+10 | 1.021e+13 | 1.021e+13 | 1.025e+13 | 1.025e+13 |
| organism time over the line (% of steps) | 1.976 | 1.93 | 4.251 | 4.164 | 1.42 | 1.367 | 2.303 | 2.262 | 2.431 | 2.409 | 2.401 | 2.345 |
| organism work per energy | 1.404 | 1.403 | 1.125 | 1.124 | 0.006603 | 0.006603 | 0.382 | 0.382 | 0.006799 | 0.006799 | 0.01277 | 0.01277 |
| organism behind its window (s) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

## Each organism: omni against native, paired by repetition

### Compute / AI / Cloud: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1693 | 1580 | -6.7% | -292.1 to +66.95 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5001 | 5094 | +1.9% | -478.8 to +664.3 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 31.61 | 22.39 | -29.2% | -11.21 to -7.228 | GAIN |
| failed requests (%) | 14.41 | 12.13 | -15.8% | -3.177 to -1.384 | GAIN |
| HPA replicas, mean | 9.707 | 12.33 | +27.0% | +2.07 to +3.171 | power given |
| pods started | 4.439 | 9.829 | +121.4% | +4.71 to +6.071 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -8.595e-16 to -2.669e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.3 | 182.2 | -0.1% | -0.4934 to +0.2702 | EVEN, inside the noise (cut) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.3 | 182.2 | -0.1% | -0.4934 to +0.2702 | EVEN, inside the noise (cut) |
| CPU used with Omni's own (cores), mean | 2.235 | 2.219 | -0.7% | -0.02983 to -0.00261 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 66.22 | 66.08 | -0.2% | -0.5298 to +0.241 | shown, not judged |
| organism work | 2.085e+10 | 2.085e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.485e+10 | 1.486e+10 | +0.0% | +8.618e+05 to +8.624e+05 | power given |
| organism time over the line (% of steps) | 1.976 | 1.93 | -2.3% | -0.0463 to -0.0463 | GAIN |
| organism work per energy | 1.404 | 1.403 | -0.0% | -8.148e-05 to -8.143e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Physics / Robotics / Autonomous: GAIN on 6 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2313 | 2040 | -11.8% | -527 to -18.8 | GAIN |
| response time (ms), 99th percentile | 6077 | 6152 | +1.2% | -322.7 to +474.1 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 22.58 | 16.81 | -25.6% | -6.879 to -4.662 | GAIN |
| failed requests (%) | 7.857 | 7.235 | -7.9% | -1.035 to -0.209 | GAIN |
| HPA replicas, mean | 9.653 | 13.96 | +44.6% | +3.765 to +4.844 | power given |
| pods started | 4.976 | 9.634 | +93.6% | +4.011 to +5.306 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -4.69e-16 to +2.523e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182 | 180.8 | -0.7% | -1.646 to -0.8567 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182 | 180.8 | -0.7% | -1.646 to -0.8567 | GAIN |
| CPU used with Omni's own (cores), mean | 2.122 | 2.122 | -0.0% | -0.009137 to +0.008836 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.77 | 63.03 | +0.4% | +0.01993 to +0.4807 | shown, not judged |
| organism work | 2.16e+10 | 2.16e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.921e+10 | 1.921e+10 | +0.0% | +1.408e+06 to +1.408e+06 | power given |
| organism time over the line (% of steps) | 4.251 | 4.164 | -2.1% | -0.08767 to -0.08767 | GAIN |
| organism work per energy | 1.125 | 1.124 | -0.0% | -8.245e-05 to -8.244e-05 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Energy / Facility / Industrial: GAIN on 6 (response time (ms), 99th percentile; time over the response line (% of samples); failed requests (%); energy, parked workers still on at idle power (Wh, declared model); energy, parked workers at 25 W standby (Wh, declared model; kind never does this); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 1

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 2080 | 2043 | -1.7% | -326 to +253.6 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 6771 | 6253 | -7.7% | -825.9 to -211 | GAIN |
| time over the response line (% of samples) | 23.4 | 17.09 | -27.0% | -7.502 to -5.126 | GAIN |
| failed requests (%) | 7.846 | 6.865 | -12.5% | -1.44 to -0.5214 | GAIN |
| HPA replicas, mean | 9.678 | 14.22 | +47.0% | +4.163 to +4.926 | power given |
| pods started | 4.805 | 10.24 | +113.2% | +4.862 to +6.016 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -6.31e-16 to +1.11e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.2 | 181.7 | -0.3% | -0.9224 to -0.01182 | GAIN |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.2 | 181.7 | -0.3% | -0.9224 to -0.01182 | GAIN |
| CPU used with Omni's own (cores), mean | 2.161 | 2.162 | +0.1% | -0.009453 to +0.01208 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 63.83 | 63.96 | +0.2% | -0.1006 to +0.3443 | shown, not judged |
| organism work | 6.708e+10 | 6.708e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.016e+13 | 1.016e+13 | +0.0% | +8.945e+05 to +8.945e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 1.42 | 1.367 | -3.7% | -0.05295 to -0.05295 | GAIN |
| organism work per energy | 0.006603 | 0.006603 | -0.0% | -5.815e-10 to -5.815e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### Distribution / Specialized: GAIN on 4 (response time (ms), 95th percentile; time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (organism work per energy), power given on 3 (HPA replicas, mean; pods started; organism energy (J)), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1711 | 1524 | -10.9% | -326.7 to -47.17 | GAIN |
| response time (ms), 99th percentile | 4607 | 4546 | -1.3% | -431.6 to +310.1 | EVEN, inside the noise (cut) |
| time over the response line (% of samples) | 25.9 | 18.21 | -29.7% | -9.41 to -5.958 | GAIN |
| failed requests (%) | 8.536 | 7.512 | -12.0% | -1.585 to -0.4628 | GAIN |
| HPA replicas, mean | 9.616 | 13.38 | +39.2% | +3.184 to +4.352 | power given |
| pods started | 4.854 | 9.878 | +103.5% | +4.261 to +5.788 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.975e-16 to +3.109e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181.5 | 181.6 | +0.0% | -0.3521 to +0.4397 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181.5 | 181.6 | +0.0% | -0.3521 to +0.4397 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.119 | 2.119 | -0.0% | -0.0079 to +0.007656 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 62.72 | 63.1 | +0.6% | +0.1771 to +0.5714 | shown, not judged |
| organism work | 2.138e+10 | 2.138e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 5.596e+10 | 5.596e+10 | +0.0% | +8.378e+05 to +8.378e+05 | power given |
| organism time over the line (% of steps) | 2.303 | 2.262 | -1.8% | -0.04132 to -0.04132 | GAIN |
| organism work per energy | 0.382 | 0.382 | -0.0% | -5.719e-06 to -5.719e-06 | LOSS |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The whole tower, every muscle once: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 1 (response time (ms), 99th percentile), power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 3

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1557 | 1513 | -2.8% | -333.6 to +245 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 4481 | 4875 | +8.8% | +6.457 to +780.5 | LOSS |
| time over the response line (% of samples) | 24.27 | 16.88 | -30.5% | -9.269 to -5.516 | GAIN |
| failed requests (%) | 9.416 | 7.166 | -23.9% | -3.392 to -1.107 | GAIN |
| HPA replicas, mean | 9.611 | 12.87 | +33.9% | +2.681 to +3.841 | power given |
| pods started | 5.195 | 10.56 | +103.3% | +4.589 to +6.143 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -3.815e-16 to +1.649e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 181 | 181.1 | +0.1% | -0.1362 to +0.4344 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 181 | 181.1 | +0.1% | -0.1362 to +0.4344 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.082 | 2.077 | -0.3% | -0.01337 to +0.002624 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 61.71 | 61.97 | +0.4% | +0.0592 to +0.4541 | shown, not judged |
| organism work | 6.941e+10 | 6.941e+10 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.021e+13 | 1.021e+13 | +0.0% | +8.93e+05 to +8.93e+05 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.431 | 2.409 | -0.9% | -0.02296 to -0.02296 | GAIN |
| organism work per energy | 0.006799 | 0.006799 | -0.0% | -5.947e-10 to -5.947e-10 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

### The four stacked, duplicates kept: GAIN on 3 (time over the response line (% of samples); failed requests (%); organism time over the line (% of steps)), LOSS on 0, power given on 2 (HPA replicas, mean; pods started), EVEN (inside the noise) on 4

41 paired repetitions.

| Gauge | native | omni | Change | 95% interval of the difference | Reading |
|---|---:|---:|---:|---:|---|
| response time (ms), 95th percentile | 1860 | 1747 | -6.1% | -323.9 to +98.27 | EVEN, inside the noise (cut) |
| response time (ms), 99th percentile | 5451 | 5508 | +1.1% | -467.3 to +582 | EVEN, inside the noise (up) |
| time over the response line (% of samples) | 32.47 | 23.24 | -28.4% | -10.85 to -7.613 | GAIN |
| failed requests (%) | 14.68 | 12.57 | -14.3% | -2.834 to -1.369 | GAIN |
| HPA replicas, mean | 9.716 | 12.6 | +29.7% | +2.322 to +3.445 | power given |
| pods started | 4.61 | 9.707 | +110.6% | +4.453 to +5.743 | power given |
| worker nodes in service, mean | 6 | 6 | -0.0% | -5.7e-16 to +1.367e-16 | EVEN, the same (under one part in a million) |
| energy, parked workers still on at idle power (Wh, declared model) | 182.6 | 182.9 | +0.2% | -0.04677 to +0.601 | EVEN, inside the noise (up) |
| energy, parked workers at 25 W standby (Wh, declared model; kind never does this) | 182.6 | 182.9 | +0.2% | -0.04677 to +0.601 | EVEN, inside the noise (up) |
| CPU used with Omni's own (cores), mean | 2.26 | 2.265 | +0.2% | -0.004235 to +0.01433 | shown, not judged |
| host CPU busy, the real machine under kind (%) | 67.2 | 67.65 | +0.7% | +0.2197 to +0.6841 | shown, not judged |
| organism work | 1.309e+11 | 1.309e+11 | +0.0% | +0 to +0 | EVEN, the same |
| organism energy (J) | 1.025e+13 | 1.025e+13 | +0.0% | +4e+06 to +4e+06 | EVEN, the same (under one part in a million) |
| organism time over the line (% of steps) | 2.401 | 2.345 | -2.3% | -0.05547 to -0.05547 | GAIN |
| organism work per energy | 0.01277 | 0.01277 | -0.0% | -4.986e-09 to -4.985e-09 | EVEN, the same (under one part in a million) |
| organism behind its window (s) | 0 | 0 | +0 | +0 to +0 | shown, not judged (0 is on the clock; past 5% of the window the repetition is off the clock) |

---

*© 2026 The Omni-Compass LLC. All rights reserved. **Evaluation and simulation use only.** Any commercial use, commercialization, monetization, production use, redistribution or hosted service of any part of Omni-Compass requires a signed, paid Omni-Compass Enterprise License from The Omni-Compass LLC. Every copy, export, report and printout carries this notice with `LICENSE`, `NOTICE` and `DISCLOSURES.md`. All patents, copyrights and trademarks filed in the USA. www.omni-compass.com*
